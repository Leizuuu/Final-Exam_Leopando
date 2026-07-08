from src.strategy import EncryptionStrategy, CompressionStrategy


class ServiceFactory:
    @staticmethod
    def get_service(service_name):
        if service_name.lower() == "encryption":
            return EncryptionStrategy(0x4F)
        if service_name.lower() == "compression":
            return CompressionStrategy(0.85)
        raise ValueError(f"Unknown service: {service_name}")
