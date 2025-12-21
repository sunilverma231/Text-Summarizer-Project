import os

# CRITICAL: Disable MPS BEFORE importing torch to force pure CPU training
# On macOS, PyTorch defaults to MPS (GPU) which has limited memory (~9GB)
# Set this FIRST, before any torch imports
os.environ['PYTORCH_DISABLE_MPS'] = '1'
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '0'

from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
from text_summarizer.entity import ModelTrainerConfig
from peft import get_peft_model, LoraConfig, TaskType
import torch
from inspect import signature


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):
        # Reduce parallelism to avoid macOS segfaults with NumPy/Torch
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
        try:
            torch.set_num_threads(1)
        except Exception:
            pass

        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        base_model = AutoModelForSeq2SeqLM.from_pretrained(
            self.config.model_ckpt,
            use_safetensors=True
        ).to(device)
        
        # Configure LoRA with higher rank for better quality
        lora_config = LoraConfig(
            r=16,  # Increased from 8 for better quality (more parameters)
            lora_alpha=32,
            target_modules=["q_proj", "v_proj"],  # Target attention modules
            lora_dropout=0.05,
            bias="none",
            task_type=TaskType.SEQ_2_SEQ_LM
        )
        
        # Apply LoRA to the model
        model_lora = get_peft_model(base_model, lora_config)
        model_lora.print_trainable_parameters()
        
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_lora)
        
        #loading data 
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # trainer_args = TrainingArguments(
        #     output_dir=self.config.root_dir, num_train_epochs=self.config.num_train_epochs, warmup_steps=self.config.warmup_steps,
        #     per_device_train_batch_size=self.config.per_device_train_batch_size, per_device_eval_batch_size=self.config.per_device_train_batch_size,
        #     weight_decay=self.config.weight_decay, logging_steps=self.config.logging_steps,
        #     evaluation_strategy=self.config.evaluation_strategy, eval_steps=self.config.eval_steps, save_steps=1e6,
        #     gradient_accumulation_steps=self.config.gradient_accumulation_steps
        # ) 


        # Build TrainingArguments - FAST MODE (1 hour target)
        # Optimized for speed - good enough quality
        args_dict = {
            "output_dir": self.config.root_dir,
            "num_train_epochs": 1,  # Single epoch - faster
            "warmup_steps": 20,  # Minimal warmup
            "per_device_train_batch_size": 1,
            "per_device_eval_batch_size": 1,
            "weight_decay": 0.01,
            "logging_steps": 20,  # Log less frequently
            "logging_strategy": "steps",
            "save_steps": int(1e6),
            "gradient_accumulation_steps": 1,  # Reduced from 4
            "dataloader_num_workers": 0,
            "report_to": "none",
            "no_cuda": True,
            "disable_tqdm": False,
            "learning_rate": 5e-4,
        }
        if "evaluation_strategy" in signature(TrainingArguments).parameters:
            args_dict["evaluation_strategy"] = "no"  # Disable eval during training (too slow)

        trainer_args = TrainingArguments(**args_dict)

        # Use minimal training data - 100 samples for quick training (~1 hour)
        # This gives decent quality while keeping speed reasonable
        train_size = min(100, len(dataset_samsum_pt["train"]))
        eval_size = min(30, len(dataset_samsum_pt["validation"]))
        
        train_dataset = dataset_samsum_pt["train"].select(range(train_size))
        eval_dataset = dataset_samsum_pt["validation"].select(range(eval_size))
        
        print(f"\n{'='*60}")
        print(f"TRAINING CONFIGURATION (LoRA - FAST MODE - 1 Hour)")
        print(f"{'='*60}")
        print(f"Training samples: {len(train_dataset)}")
        print(f"Evaluation samples: {len(eval_dataset)}")
        print(f"Number of epochs: 1")
        print(f"Warmup steps: 20")
        print(f"Learning rate: 5e-4")
        print(f"LoRA rank: 16")
        print(f"Gradient accumulation: 1 (disabled for speed)")
        print(f"Evaluation during training: No (faster)")
        print(f"\nESTIMATED TIME:")
        print(f"  Training: ~50-60 minutes on CPU")
        print(f"  Evaluation: ~5-10 minutes")
        print(f"  Total: ~1 hour")
        print(f"  Total: ~2.5-3.5 hours")
        print(f"{'='*60}\n")
        
        trainer = Trainer(model=model_lora, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=train_dataset, 
                  eval_dataset=eval_dataset)
        
        trainer.train()

        # Ensure evaluation runs even if evaluation_strategy is unsupported
        try:
            trainer.evaluate()
        except Exception:
            pass

        ## Save LoRA model
        model_lora.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))