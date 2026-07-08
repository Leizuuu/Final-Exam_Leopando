from src.strategy import DataProcessor
from src.factory import ServiceFactory


def main():
    data_stream = [78, 82, 91, 65, 40, 99, 88]

    processor = DataProcessor(ServiceFactory.get_service("encryption"))
    encrypted = processor.execute(data_stream)
    print("Original Data:", data_stream)
    print("Encrypted Data:", encrypted)

    processor.set_strategy(ServiceFactory.get_service("compression"))
    compressed = processor.execute(data_stream)
    print("Compressed Data:", compressed)


if __name__ == "__main__":
    main()
