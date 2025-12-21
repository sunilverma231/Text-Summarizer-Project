#!/usr/bin/env python3
"""
Initialize Text Summarizer - Download data and set up models
This prepares the project for training
"""

import sys
import os

print("=" * 80)
print("TEXT SUMMARIZER - PROJECT INITIALIZATION")
print("=" * 80)

# Step 1: Download data
print("\n[1/3] Downloading dataset...")
try:
    import subprocess
    result = subprocess.run([
        "wget",
        "https://github.com/entbappy/Branching-tutorial/raw/master/summarizer-data.zip",
        "-O", 
        "/tmp/summarizer-data.zip"
    ], cwd="/Users/sunilverma/Text-Summarizer-Project")
    
    print("✓ Dataset downloaded")
except Exception as e:
    print(f"✗ Download failed: {e}")

# Step 2: Unzip data
print("\n[2/3] Extracting dataset...")
try:
    import zipfile
    with zipfile.ZipFile("/tmp/summarizer-data.zip", "r") as zip_ref:
        zip_ref.extractall("/Users/sunilverma/Text-Summarizer-Project/artifacts/")
    print("✓ Dataset extracted")
except Exception as e:
    print(f"✗ Extraction failed: {e}")

# Step 3: Setup base model and tokenizer
print("\n[3/3] Downloading base model and tokenizer...")
try:
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
    
    model_name = "google/pegasus-cnn_dailymail"
    print(f"  Downloading {model_name}...")
    
    # Create directory
    os.makedirs("artifacts/model_trainer", exist_ok=True)
    
    # Download tokenizer
    print("  - Tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.save_pretrained("artifacts/model_trainer/tokenizer")
    
    # Download model
    print("  - Base model...")
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    model.save_pretrained("artifacts/model_trainer/pegasus-samsum-model")
    
    print("✓ Model and tokenizer ready")
except Exception as e:
    print(f"✗ Model download failed: {e}")

print("\n" + "=" * 80)
print("INITIALIZATION COMPLETE")
print("=" * 80)
print("""
✓ Data downloaded to: artifacts/data_ingestion/
✓ Model ready at: artifacts/model_trainer/pegasus-samsum-model
✓ Tokenizer ready at: artifacts/model_trainer/tokenizer

Next steps:
1. Run data processing pipeline:
   python -c "from text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline; DataIngestionTrainPipeline().main()"
   
2. Run full training:
   python main.py

Or just run everything:
   python main.py
""")
print("=" * 80)
