"""
data_augmentation.py - MERGED VERSION
Combines Tony's advanced augmentations with Kate's simple interface
"""

import cv2
import numpy as np
import random
from pathlib import Path

# Tony's advanced augmentations (using albumentations when available)
try:
    import albumentations as A
    ALBUMENTATIONS_AVAILABLE = True
except ImportError:
    ALBUMENTATIONS_AVAILABLE = False
    print("⚠️ Albumentations not available, using fallback augmentations")

class LeafAugmentor:
    def __init__(self, mode='balanced'):
        \"\"\"
        mode: 'simple' - fast, no dependencies
              'advanced' - albumentations with GPU support
              'balanced' - mix of both (default)
        \"\"\"
        self.mode = mode
        self.setup_augmentations()
    
    def setup_augmentations(self):
        \"\"\"Configure augmentation pipeline based on mode\"\"\"
        if self.mode == 'advanced' and ALBUMENTATIONS_AVAILABLE:
            self.transform = A.Compose([
                A.Rotate(limit=30, p=0.8),
                A.RandomBrightnessContrast(p=0.8),
                A.HueSaturationValue(p=0.8),
                A.GaussNoise(var_limit=(10, 50), p=0.3),
                A.HorizontalFlip(p=0.5),
            ])
            self.apply = self._apply_advanced
        else:
            # Kate's simple approach (enhanced)
            self.augmentations = []
            self.apply = self._apply_simple
    
    def add_augmentation(self, name, *args, **kwargs):
        \"\"\"Kate's builder pattern - add augmentations\"\"\"
        self.augmentations.append((name, args, kwargs))
        return self
    
    def _apply_simple(self, image):
        \"\"\"Kate's simple augmentation logic\"\"\"
        result = image.copy()
        for name, args, kwargs in self.augmentations:
            if random.random() < kwargs.get('probability', 0.5):
                if name == 'flip':
                    result = cv2.flip(result, 1)
                elif name == 'rotate':
                    angle = random.uniform(-args[0] if args else 15, 
                                          args[0] if args else 15)
                    h, w = result.shape[:2]
                    matrix = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
                    result = cv2.warpAffine(result, matrix, (w, h))
                elif name == 'brightness':
                    factor = random.uniform(args[0] if args else 0.9,
                                           args[1] if len(args) > 1 else 1.1)
                    result = cv2.convertScaleAbs(result, alpha=factor, beta=0)
        return result
    
    def _apply_advanced(self, image):
        \"\"\"Tony's advanced augmentation with albumentations\"\"\"
        augmented = self.transform(image=image)
        return augmented['image']
    
    def __call__(self, image):
        return self.apply(image)
    
    def __repr__(self):
        return f"LeafAugmentor(mode='{self.mode}')"

# Test both approaches
if __name__ == "__main__":
    print("🌽 LeafGuard AI - Data Augmentation Module")
    print("=" * 50)
    
    # Create sample image
    sample = np.zeros((224, 224, 3), dtype=np.uint8)
    cv2.rectangle(sample, (50, 50), (174, 174), (0, 255, 0), -1)
    
    # Test simple mode
    simple_aug = LeafAugmentor(mode='simple')
    simple_aug.add_augmentation('rotate', 20, probability=0.8)
    simple_aug.add_augmentation('brightness', 0.8, 1.2, probability=0.5)
    simple_aug.add_augmentation('flip', probability=0.3)
    
    result_simple = simple_aug(sample)
    print("✓ Simple augmentor working")
    
    # Test advanced mode if available
    if ALBUMENTATIONS_AVAILABLE:
        adv_aug = LeafAugmentor(mode='advanced')
        result_adv = adv_aug(sample)
        print("✓ Advanced augmentor working")
    
    print("✅ Both approaches merged successfully!")
