from strategy import (
    DataProcessor,
    EncryptionStrategy,
    CompressionStrategy,
)

data_stream = [78, 82, 91, 65, 40, 99, 88]

processor = DataProcessor(EncryptionStrategy(0x4F))
encrypted = processor.execute(data_stream)

print("Original Data:", data_stream)
print("Encrypted Data:", encrypted)

processor.set_strategy(CompressionStrategy(0.85))
compressed = processor.execute(data_stream)

print("Compressed Data:", compressed)