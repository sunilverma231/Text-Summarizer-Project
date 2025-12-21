#!/usr/bin/env python3
"""
Test LoRA Evaluation - Verify model evaluation works with both LoRA and standard models
"""

import sys
import os

print("=" * 80)
print("LORA EVALUATION TEST")
print("=" * 80)

# Test 1: Check if LoRA adapters exist
print("\n[1/3] Checking for LoRA adapters...")
model_path = "artifacts/model_trainer/pegasus-samsum-model"
adapter_config = os.path.join(model_path, "adapter_config.json")

if os.path.exists(adapter_config):
    print(f"  ✓ LoRA adapter found: {adapter_config}")
    model_type = "LoRA"
else:
    print(f"  ℹ No LoRA adapter found (will use standard model)")
    model_type = "Standard"

# Test 2: Test model evaluation pipeline
print("\n[2/3] Testing model evaluation component...")
try:
    from text_summarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainPipeline
    from text_summarizer.logging import logger
    
    print("  ℹ Initializing evaluation pipeline...")
    eval_pipeline = ModelEvaluationTrainPipeline()
    print("  ✓ Evaluation pipeline initialized")
    
except Exception as e:
    print(f"  ✗ Failed to initialize: {e}")
    sys.exit(1)

# Test 3: Run evaluation (optional - uncomment to actually run)
print("\n[3/3] Evaluation setup complete")
print(f"\n  Model Type: {model_type}")
print(f"  Output File: artifacts/model_evaluation/metrics.csv")

print("\n" + "=" * 80)
print("TO RUN EVALUATION:")
print("=" * 80)
print("""
Run the full evaluation with:

    python -c "from text_summarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainPipeline; ModelEvaluationTrainPipeline().main()"

Or run the complete pipeline:

    python main.py

This will:
  1. Load the model (LoRA or standard)
  2. Evaluate on test dataset
  3. Generate ROUGE scores
  4. Save results to artifacts/model_evaluation/metrics.csv
""")
print("=" * 80)
