"""
train.py - Training script with a BUG (for bisect practice)
"""
import torch
import numpy as np

class BuggyTrainer:
    def __init__(self):
        self.learning_rate = 0.1  # TOO HIGH! This will cause divergence
    
    def train_step(self):
        # Bug: no gradient clipping, high LR causes NaN
        loss = torch.tensor(1.0, requires_grad=True)
        loss.backward()
        # Missing optimizer step with proper LR
        return loss.item()

print("Training started...")
trainer = BuggyTrainer()
loss = trainer.train_step()
print(f"Loss: {loss}")

# This would normally fail with NaN after a few steps
