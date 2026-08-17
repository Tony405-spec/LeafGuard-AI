"""Minimal training smoke script for LeafGuard AI.

This is not a full model-training pipeline yet. It provides an import-safe
training step that future dataset/model code can extend.
"""

import torch


class SmokeTrainer:
    def __init__(self, learning_rate: float = 0.001):
        if learning_rate <= 0:
            raise ValueError("learning_rate must be positive")
        self.learning_rate = learning_rate

    def train_step(self) -> float:
        loss = torch.tensor(1.0, requires_grad=True)
        loss.backward()
        return float(loss.item())


def main() -> None:
    print("Training smoke check started...")
    trainer = SmokeTrainer()
    loss = trainer.train_step()
    print(f"Loss: {loss}")


if __name__ == "__main__":
    main()
