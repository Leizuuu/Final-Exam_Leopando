import pytest
from src.factory import ServiceFactory
from src.strategy import EncryptionStrategy, CompressionStrategy


def test_factory_encryption():
    service = ServiceFactory.get_service("encryption")
    assert isinstance(service, EncryptionStrategy)


def test_factory_compression():
    service = ServiceFactory.get_service("compression")
    assert isinstance(service, CompressionStrategy)


def test_factory_invalid():
    with pytest.raises(ValueError):
        ServiceFactory.get_service("invalid")
