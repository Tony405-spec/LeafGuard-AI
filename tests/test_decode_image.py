import base64

import numpy as np
import pytest

from scripts.decode_image import load_base64_image


def test_load_base64_image_rejects_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError, match="not found"):
        load_base64_image(tmp_path / "missing.txt", tmp_path / "out.jpg")


def test_load_base64_image_rejects_invalid_base64(tmp_path):
    source = tmp_path / "bad.txt"
    source.write_text("not valid base64!", encoding="utf-8")

    with pytest.raises(ValueError, match="Invalid base64"):
        load_base64_image(source, tmp_path / "out.jpg")


def test_load_base64_image_rejects_non_image_bytes(tmp_path):
    source = tmp_path / "not_image.txt"
    source.write_text(base64.b64encode(b"hello").decode("ascii"), encoding="utf-8")

    with pytest.raises(ValueError, match="not a valid image"):
        load_base64_image(source, tmp_path / "out.jpg")


def test_load_base64_image_writes_decoded_image(tmp_path, monkeypatch):
    source = tmp_path / "image.txt"
    source.write_text(base64.b64encode(b"fake image bytes").decode("ascii"), encoding="utf-8")
    decoded = np.zeros((1, 1, 3), dtype=np.uint8)

    monkeypatch.setattr("scripts.decode_image.cv2.imdecode", lambda *_args, **_kwargs: decoded)
    monkeypatch.setattr("scripts.decode_image.cv2.imwrite", lambda *_args, **_kwargs: True)

    image = load_base64_image(source, tmp_path / "nested" / "out.jpg")

    assert image is decoded
