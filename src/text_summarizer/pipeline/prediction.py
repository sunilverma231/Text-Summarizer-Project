from text_summarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline
from peft import PeftModel
import os


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        
        # Convert relative paths to absolute paths
        tokenizer_path = os.path.abspath(self.config.tokenizer_path)
        model_path = os.path.abspath(self.config.model_path)
        
        # Load tokenizer - use base model if custom tokenizer not available
        print(f"Loading tokenizer...")
        try:
            # First try to load from saved path
            if os.path.exists(tokenizer_path):
                print(f"  From: {tokenizer_path}")
                self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
            else:
                # Fallback to base model
                print(f"  From base model: google/pegasus-cnn_dailymail")
                self.tokenizer = AutoTokenizer.from_pretrained("google/pegasus-cnn_dailymail")
        except Exception as e:
            print(f"  Error loading tokenizer: {e}")
            print(f"  Using default tokenizer...")
            self.tokenizer = AutoTokenizer.from_pretrained("google/pegasus-cnn_dailymail")
        
        # Load model
        print(f"Loading model...")
        try:
            if os.path.exists(model_path):
                # Try to load as LoRA model first
                print(f"  From: {model_path}")
                try:
                    base_model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
                    self.model = PeftModel.from_pretrained(base_model, model_path)
                    print("  LoRA model loaded!")
                except:
                    # Load as regular model
                    self.model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
                    print("  Standard model loaded!")
            else:
                # Load base model from HuggingFace
                print(f"  From HuggingFace: google/pegasus-cnn_dailymail")
                self.model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-cnn_dailymail")
                print("  Base model loaded!")
        except Exception as e:
            print(f"  Error: {e}")
            print(f"  Using default model...")
            self.model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-cnn_dailymail")
        
        # Create pipeline
        self.pipe = pipeline("summarization", model=self.model, tokenizer=self.tokenizer)
        print("✓ Pipeline ready!")

    
    def predict(self, text):
        # Use the pre-loaded pipeline (fast, no reloading)
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}
        
        output = self.pipe(text, **gen_kwargs)[0]["summary_text"]
        
        return output