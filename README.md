#  **`LeafGuard AI`** - Agricultural Disease Detection

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-24.0+-blue.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## `Project Overview`
LeafGuard AI is a computer vision system for detecting crop diseases from leaf images, designed for the March 2025 Agri-Tech Datathon. The system uses deep learning to identify multiple diseases across maize, tomato, and potato crops.

##  `Features`
- Multi-class disease classification
- Reproducible Docker environments
- GPU support for training
- FastAPI inference endpoints
- Comprehensive data preprocessing

## `Tech Stack`
- **Python 3.9+** with PyTorch & OpenCV
- **Docker** for containerization
- **Git** for version control
- **FastAPI** for model serving

##  `Quick Start` (Windows PowerShell)

`powershell
# `Clone the repository`
git clone https://github.com/Tony405-spec/LeafGuard-AI.git
cd LeafGuard-AI

# `Build Docker image`
docker build -t leafguard-ai:dev -f docker/Dockerfile .

# `Run inference`
docker run --rm -v C:\Users\Administrator\projects\leafguard-ai/data:/app/data leafguard-ai:dev
 `Dataset`
Synthetic leaf disease dataset containing:

Healthy and diseased maize leaves

Northern Leaf Blight samples

Training/validation/test splits

 `Model Performance`
Coming soon - currently in development

 ***`Team`***

[] Tony405-spec - Lead Developer

[] Kate020-cpu - ML Engineer

`Timeline`
March 10: Docker setup & environment

March 11: Model development

March 12: Training pipeline

March 13: API deployment

March 14: Datathon submission

 `License`
MIT License - see LICENSE file
