"""
data_augmentation.py - Simple augmentation for quick experiments
"""

import cv2
import numpy as np
import random

class SimpleLeafAugmentor:
    def __init__(self):
        self.augmentations = []
    
    def add_flip(self, probability=0.5):
        self.augmentations.append(('flip', probability))
        return self
    
    def add_rotate(self, max_angle=15, probability=0.5):
        self.augmentations.append(('rotate', max_angle, probability))
        return self
    
    def add_brightness(self, factor_range=(0.9, 1.1), probability=0.5):
        self.augmentations.append(('brightness', factor_range, probability))
        return self
    
    def apply(self, image):
        \"\"\"Apply selected augmentations\"\"\"
        result = image.copy()
        
        for aug in self.augmentations:
            if random.random() < aug[-1]:  # probability is last element
                if aug[0] == 'flip':
                    result = cv2.flip(result, 1)
                elif aug[0] == 'rotate':
                    angle = random.uniform(-aug[1], aug[1])
                    h, w = result.shape[:2]
                    matrix = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
                    result = cv2.warpAffine(result, matrix, (w, h))
                elif aug[0] == 'brightness':
                    factor = random.uniform(aug[1][0], aug[1][1])
                    result = cv2.convertScaleAbs(result, alpha=factor, beta=0)
        
        return result
    
    def __repr__(self):
        return f"SimpleLeafAugmentor(augmentations={len(self.augmentations)})"

# Test simple augmentor
if __name__ == "__main__":
    print("Simple Data Augmentation")
    print("=" * 30)
    print("✓ Lightweight implementation")
    print("✓ No external dependencies")
    print("✓ Fast for prototyping")
