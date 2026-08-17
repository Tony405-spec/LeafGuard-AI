import pytest

from scripts.train import SmokeTrainer


def test_smoke_trainer_rejects_non_positive_learning_rate():
    with pytest.raises(ValueError, match="positive"):
        SmokeTrainer(learning_rate=0)


def test_smoke_trainer_train_step_returns_loss():
    trainer = SmokeTrainer()

    assert trainer.train_step() == 1.0
