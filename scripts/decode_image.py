import base64
import binascii
from pathlib import Path

import cv2
import numpy as np


def load_base64_image(base64_path, output_path):
    """Load a base64 encoded image and save it as an image file."""
    base64_path = Path(base64_path)
    output_path = Path(output_path)

    if not base64_path.exists():
        raise FileNotFoundError(f"Base64 image file not found: {base64_path}")

    img_data = base64_path.read_text(encoding="utf-8").strip()

    try:
        img_bytes = base64.b64decode(img_data, validate=True)
    except binascii.Error as exc:
        raise ValueError(f"Invalid base64 image data in {base64_path}") from exc

    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError(f"Decoded data is not a valid image: {base64_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(output_path), img):
        raise OSError(f"Failed to write decoded image to {output_path}")

    print(f"Image saved to {output_path}")
    return img


if __name__ == "__main__":
    base64_file = Path("data/raw/maize/leaf_sample_base64.txt")
    output_file = Path("data/raw/maize/healthy_maize_001.jpg")
    load_base64_image(base64_file, output_file)
