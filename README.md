# LeafGuard AI

LeafGuard AI is an agricultural disease-detection learning project for classifying crop leaf images. The current repository contains early training and image-decoding scripts plus a pinned base dependency file.

## Features

- Crop leaf image preprocessing utilities.
- PyTorch/OpenCV-oriented training environment.
- Reproducible dependency list in `requirements/base.txt`.
- Early training script for experimentation and debugging practice.

## Quick Start

```powershell
git clone https://github.com/Tony405-spec/LeafGuard-AI.git
cd LeafGuard-AI
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements/base.txt
```

Run the current scripts:

```powershell
python scripts/decode_image.py
python scripts/train.py
```

`scripts/decode_image.py` expects a base64 image at `data/raw/maize/leaf_sample_base64.txt` and writes `data/raw/maize/healthy_maize_001.jpg`.

## Data Layout

Use this layout for local experiments:

```text
data/
  raw/
    maize/
      leaf_sample_base64.txt
      healthy_maize_001.jpg
```

Do not commit private datasets, large generated image folders, or model checkpoints unless they are intentionally curated sample assets.

## Current Limitations

- `scripts/train.py` is a minimal debugging-practice script, not a complete production training pipeline.
- The repository does not yet include FastAPI serving code or Docker files even though those are future project goals.
- Model performance metrics are not available yet.

## License

MIT License. Add a `LICENSE` file if this repository is intended for public reuse under MIT terms.
