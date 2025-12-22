# End-to-End Text Summarizer with LoRA Fine-Tuning

A production-ready text summarization system built with **FastAPI**, **Hugging Face Transformers**, and **Parameter-Efficient Fine-Tuning (PEFT/LoRA)**. This project demonstrates a complete MLOps pipeline from data ingestion to deployment on AWS ECS.

## 🚀 Features

- **LoRA-based Fine-Tuning**: Migrated from full PEGASUS fine-tuning to Parameter-Efficient Fine-Tuning (LoRA) for faster training and lower resource consumption
- **FastAPI REST API**: Production-ready endpoints for training and inference
- **Modular Pipeline**: Separate stages for data ingestion, validation, transformation, training, and evaluation
- **Docker & AWS ECS Ready**: Optimized Dockerfile with Gunicorn/Uvicorn workers for cloud deployment
- **Automatic Fallback**: Smart model loading with fallback to base HuggingFace models if local artifacts are missing
- **Comprehensive Logging**: Full pipeline logging for debugging and monitoring

## �️ Tech Stack

### Core ML/NLP Frameworks
- **🤗 Transformers** - Pre-trained models and tokenizers (PEGASUS)
- **PEFT (Parameter-Efficient Fine-Tuning)** - LoRA adapters for efficient training
- **Datasets** - Hugging Face dataset loading and processing
- **Evaluate** - ROUGE score computation
- **PyTorch** - Deep learning backend

### Web Framework & API
- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - Lightning-fast ASGI server
- **Gunicorn** - Production WSGI server with worker management
- **Jinja2** - Template engine for web pages

### Performance Optimization
- **uvloop** - Ultra-fast asyncio event loop (Linux/macOS)
- **httptools** - High-performance HTTP request parsing
- **orjson** - Fast JSON serialization/deserialization

### Data Processing
- **Pandas** - Data manipulation and analysis
- **NLTK** - Natural language processing utilities
- **sacrebleu** - BLEU score calculation
- **rouge_score** - ROUGE metric implementation

### Deployment & DevOps
- **Docker** - Containerization
- **AWS ECS (Fargate)** - Container orchestration
- **AWS ECR** - Container registry
- **boto3** - AWS SDK for Python

### Development Tools
- **Conda** - Environment and package management
- **Jupyter Notebook** - Interactive development and experimentation
- **PyYAML** - YAML configuration parsing
- **python-box** - Dict-like object access
- **tqdm** - Progress bars

### Utilities
- **py7zr** - 7z archive extraction
- **ensure** - Assertion library
- **mypy-boto3-s3** - Type hints for boto3 S3

## �📊 Project Structure

```
Text-Summarizer-Project/
│
├── app.py                          # FastAPI application with /predict and /train endpoints
├── main.py                         # Pipeline orchestrator (runs all stages)
├── Dockerfile                      # Production-ready Docker image
├── requirements.txt                # Python dependencies
├── setup.py                        # Package installation
├── params.yaml                     # Training hyperparameters
├── README.md                       # This file
├── DEPLOY_ECS.md                   # AWS ECS deployment guide
├── FAST_TRAINING.md                # Fast training mode documentation
├── LORA_MIGRATION.md               # LoRA migration details
│
├── config/
│   └── config.yaml                 # Project configuration (paths, model names)
│
├── src/text_summarizer/
│   ├── __init__.py
│   ├── constants/                  # Constants and paths
│   ├── entity/                     # Data classes for configs
│   ├── logging/                    # Custom logging setup
│   ├── utils/
│   │   └── common.py               # Helper functions (read YAML, create dirs)
│   ├── config/
│   │   └── configuration.py        # Configuration manager
│   ├── components/
│   │   ├── data_ingestion.py       # Download and extract dataset
│   │   ├── data_validation.py      # Validate dataset schema
│   │   ├── data_transformation.py  # Tokenize and prepare data
│   │   ├── model_trainer.py        # LoRA fine-tuning with PEFT
│   │   └── model_evaluation.py     # ROUGE score evaluation
│   └── pipeline/
│       ├── stage_01_data_ingestion.py
│       ├── stage_02_data_validation.py
│       ├── stage_03_data_transformation.py
│       ├── stage_04_model_trainer.py
│       ├── stage_05_model_evaluation.py
│       └── prediction.py           # Prediction pipeline with LoRA support
│
├── research/                       # Jupyter notebooks for experimentation
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_validation.ipynb
│   ├── 03_data_transformation.ipynb
│   ├── 04_model_trainer.ipynb
│   └── 05_model_evaluation.ipynb
│
├── artifacts/                      # Generated during pipeline execution
│   ├── data_ingestion/             # Downloaded SAMSum dataset
│   ├── data_validation/            # Validation status
│   ├── data_transformation/        # Tokenized datasets
│   ├── model_trainer/              # LoRA adapters and tokenizer
│   └── model_evaluation/           # metrics.csv with ROUGE scores
│
└── tests/                          # Unit tests
    └── unit/

```


# Project Title

A brief description of what this project does and who it's for
# 🚀 End-to-End Text Summarizer with LoRA Fine-Tuning

[![CI/CD Pipeline - Deploy Docker on EC2](https://github.com/sunilverma231/Text-Summarizer-Project/actions/workflows/main.yaml/badge.svg)](https://github.com/sunilverma231/Text-Summarizer-Project/actions/workflows/main.yaml)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](http://51.20.86.12:8000)
![AWS](https://img.shields.io/badge/AWS-EC2-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production--ready-teal)
![Python](https://img.shields.io/badge/Python-3.10-blue)

🔗 **Live Application**: http://51.20.86.12:8000  
📘 **Swagger Docs**: http://51.20.86.12:8000/docs  

---

## 📌 Overview

A **production-ready text summarization system** built using **FastAPI**, **Hugging Face Transformers**, and **Parameter-Efficient Fine-Tuning (LoRA / PEFT)**.

This project demonstrates a **full MLOps lifecycle**:
- Data ingestion → training → evaluation
- Model serving via FastAPI
- Dockerized deployment
- CI/CD using GitHub Actions
- **Automated deployment on AWS EC2 using a self-hosted runner**

---

## 🚀 Features

- ✅ LoRA-based fine-tuning (PEFT)
- ✅ FastAPI REST API (`/train`, `/predict`)
- ✅ Modular ML pipeline architecture
- ✅ Docker + Gunicorn + Uvicorn
- ✅ CI/CD pipeline with GitHub Actions
- ✅ AWS ECR + EC2 deployment
- ✅ Self-hosted GitHub Actions runner
- ✅ Graceful model fallback
- ✅ Health checks & logging

---

## 🧠 Tech Stack

### Machine Learning / NLP
- 🤗 Transformers (PEGASUS)
- PEFT (LoRA)
- PyTorch
- ROUGE evaluation
- Hugging Face Datasets

### Backend
- FastAPI
- Gunicorn + Uvicorn
- Jinja2

### DevOps & Cloud
- Docker
- AWS EC2
- AWS ECR
- GitHub Actions (CI/CD)
- Self-hosted GitHub Runner

---

## 📂 Project Structure

```text
Text-Summarizer-Project/
│
├── app.py                          # FastAPI application with /predict and /train endpoints
├── main.py                         # Pipeline orchestrator (runs all stages)
├── Dockerfile                      # Production-ready Docker image
├── requirements.txt                # Python dependencies
├── setup.py                        # Package installation
├── params.yaml                     # Training hyperparameters
├── README.md                       # This file
├── DEPLOY_ECS.md                   # AWS ECS deployment guide
├── FAST_TRAINING.md                # Fast training mode documentation
├── LORA_MIGRATION.md               # LoRA migration details
│
├── config/
│   └── config.yaml                 # Project configuration (paths, model names)
│
├── src/text_summarizer/
│   ├── __init__.py
│   ├── constants/                  # Constants and paths
│   ├── entity/                     # Data classes for configs
│   ├── logging/                    # Custom logging setup
│   ├── utils/
│   │   └── common.py               # Helper functions (read YAML, create dirs)
│   ├── config/
│   │   └── configuration.py        # Configuration manager
│   ├── components/
│   │   ├── data_ingestion.py       # Download and extract dataset
│   │   ├── data_validation.py      # Validate dataset schema
│   │   ├── data_transformation.py  # Tokenize and prepare data
│   │   ├── model_trainer.py        # LoRA fine-tuning with PEFT
│   │   └── model_evaluation.py     # ROUGE score evaluation
│   └── pipeline/
│       ├── stage_01_data_ingestion.py
│       ├── stage_02_data_validation.py
│       ├── stage_03_data_transformation.py
│       ├── stage_04_model_trainer.py
│       ├── stage_05_model_evaluation.py
│       └── prediction.py           # Prediction pipeline with LoRA support
│
├── research/                       # Jupyter notebooks for experimentation
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_validation.ipynb
│   ├── 03_data_transformation.ipynb
│   ├── 04_model_trainer.ipynb
│   └── 05_model_evaluation.ipynb
│
├── artifacts/                      # Generated during pipeline execution
│   ├── data_ingestion/             # Downloaded SAMSum dataset
│   ├── data_validation/            # Validation status
│   ├── data_transformation/        # Tokenized datasets
│   ├── model_trainer/              # LoRA adapters and tokenizer
│   └── model_evaluation/           # metrics.csv with ROUGE scores
│
└── tests/                          # Unit tests
    └── unit/

## 🔄 Development Workflows

Follow these steps when making changes to the pipeline:

1. **Update config.yaml** - Modify paths, model names, or data sources
2. **Update params.yaml** - Adjust hyperparameters (learning rate, epochs, LoRA rank, etc.)
3. **Update entity** - Define data classes for new configurations
4. **Update configuration manager** - Add config parsing in `src/text_summarizer/config/configuration.py`
5. **Update components** - Implement core logic in `src/text_summarizer/components/`
6. **Update pipeline** - Wire components in `src/text_summarizer/pipeline/`
7. **Update main.py** - Add new pipeline stages
8. **Update app.py** - Expose new endpoints if needed

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.10+
- Conda (recommended) or virtualenv
- Docker (for containerized deployment)
- AWS CLI (for ECS deployment)

### STEP 01: Clone the Repository

```bash
git clone https://github.com/yourusername/Text-Summarizer-Project.git
cd Text-Summarizer-Project
```

### STEP 02: Create Conda Environment

```bash
conda create -n textS python=3.10 -y
conda activate textS
```

### STEP 03: Install Dependencies

```bash
pip install -r requirements.txt
```

## 🏃 How to Run

### Option 1: Run Full Pipeline (Training + Evaluation)

```bash
python main.py
```

This executes all stages:
1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training (LoRA)
5. Model Evaluation

**Training Modes:**
- **Fast Mode** (1 hour): 100 samples, 1 epoch, LoRA rank 16
- **Quality Mode** (6-8 hours): ~80% dataset, 3 epochs, LoRA rank 16

Edit `src/text_summarizer/components/model_trainer.py` to switch modes.

### Option 2: Run FastAPI Application

```bash
# Development mode
python app.py
```

Or with Gunicorn for production:

```bash
gunicorn -k uvicorn.workers.UvicornWorker app:app --workers 2 --bind 0.0.0.0:8000
```

Access the API:
- **Docs**: http://localhost:8000/docs
- **Root**: http://localhost:8000/
- **Predict**: POST http://localhost:8000/predict

**Example cURL:**
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Your long text here..."}'
```

### Stop the Application

Press `Ctrl+C` in the terminal, or:
```bash
pkill -f "python app.py"
pkill -f "gunicorn"
```

## 🧠 LoRA Migration & Challenges

### Migration from PEGASUS to LoRA

**Why LoRA?**
- **80-90% fewer trainable parameters** compared to full fine-tuning
- **Faster training**: 1 hour vs 6+ hours for similar quality
- **Lower memory footprint**: Trains on CPU/small GPUs
- **Modular adapters**: Easy to swap, version, and distribute

**Changes Made:**
1. Added `peft` to requirements
2. Updated `model_trainer.py`:
   - Applied `LoraConfig` with `target_modules=["q_proj", "v_proj"]`
   - Used `get_peft_model()` to wrap base PEGASUS
3. Updated `model_evaluation.py`:
   - Auto-detects LoRA adapters (`adapter_config.json`)
   - Falls back to standard model if no adapters found
4. Updated `prediction.py`:
   - Loads LoRA adapters via `PeftModel.from_pretrained()`
   - Falls back to base HuggingFace model if local artifacts missing

**See [LORA_MIGRATION.md](LORA_MIGRATION.md) for detailed migration notes.**

### Challenges Faced

| Challenge | Solution |
|-----------|----------|
| **Tokenizer path errors** | Used absolute paths; added fallback to base HuggingFace tokenizer |
| **Very low ROUGE scores** (0.01-0.05) | Increased LoRA rank from 8 to 16; used more training data and epochs |
| **Slow training** (6+ hours for 4% progress) | Created fast mode: 100 samples, 1 epoch, disabled eval during training |
| **Missing model artifacts on startup** | Implemented graceful fallback to download base model from HuggingFace |
| **Evaluation expecting LoRA adapters** | Added auto-detection logic to handle both LoRA and standard models |

## 📈 Model Performance

**Current Metrics** (Fast Mode - 1 hour training):
- ROUGE-1: ~0.15-0.25
- ROUGE-2: ~0.05-0.12
- ROUGE-L: ~0.12-0.20

**Quality Mode** (3 epochs, 80% dataset):
- Expected ROUGE-1: ~0.30-0.40
- Training Time: 6-8 hours on CPU

Check `artifacts/model_evaluation/metrics.csv` after training.

## 🐳 Docker & AWS Deployment

### Build Docker Image

```bash
docker build -t text-summarizer:latest .
```

### Run Locally

```bash
docker run -p 8000:8000 text-summarizer:latest
```

### Deploy to AWS ECS

See **[DEPLOY_ECS.md](DEPLOY_ECS.md)** for complete guide:

1. Create ECR repository
2. Push Docker image to ECR
3. Create ECS Task Definition (Fargate)
4. Create ECS Service with ALB
5. Test endpoints

**Quick ECR Push:**
```bash
# Replace with your details
aws ecr get-login-password --region eu-north-1 | \
  docker login --username AWS --password-stdin 474369734726.dkr.ecr.eu-north-1.amazonaws.com

docker tag text-summarizer:latest 474369734726.dkr.ecr.eu-north-1.amazonaws.com/text-s:latest
docker push 474369734726.dkr.ecr.eu-north-1.amazonaws.com/text-s:latest
```

## 🔐 AWS Deployment Prerequisites

### IAM Permissions Required
- `AmazonEC2ContainerRegistryFullAccess`
- `AmazonEC2FullAccess`
- `AmazonECS_FullAccess`

### GitHub Secrets (for CI/CD)
```
AWS_ACCESS_KEY_ID=<your-key>
AWS_SECRET_ACCESS_KEY=<your-secret>
AWS_REGION=eu-north-1
AWS_ECR_LOGIN_URI=474369734726.dkr.ecr.eu-north-1.amazonaws.com
ECR_REPOSITORY_NAME=text-s
```

## 📚 Additional Documentation

- **[FAST_TRAINING.md](FAST_TRAINING.md)** - Quick 1-hour training guide
- **[LORA_MIGRATION.md](LORA_MIGRATION.md)** - Detailed LoRA migration steps
- **[DEPLOY_ECS.md](DEPLOY_ECS.md)** - AWS ECS deployment walkthrough
- **[QUICKSTART.md](QUICKSTART.md)** - Quick start guide

## 🧪 Testing

Run unit tests:
```bash
pytest tests/
```

## 📝 Logs

Logs are saved to `logs/` directory. Each pipeline run creates a timestamped log file.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Contact

**Author**: Sunil Verma  
**Project**: Text Summarizer with LoRA  
**Repository**: https://github.com/yourusername/Text-Summarizer-Project

## 📄 License

See [LICENSE](LICENSE) file for details.

---

**Built with ❤️ using Transformers, PEFT, FastAPI, and AWS** 

