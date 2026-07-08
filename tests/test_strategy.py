from src.strategy import EncryptionStrategy, CompressionStrategy


def test_encryption():
    strategy = EncryptionStrategy(0x4F)
    assert strategy.process([78, 82]) == [1, 29]


def test_compression():
    strategy = CompressionStrategy(0.85)
    assert strategy.process([100, 80]) == [85.0, 68.0]
