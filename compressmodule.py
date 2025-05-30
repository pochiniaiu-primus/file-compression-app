import zlib, base64


def compress(input_file, output_file):
    # Read the input file content using UTF-8 encoding
    with open(input_file, 'r', encoding='utf-8') as file:
        file_content = file.read()

    # Convert the string to bytes for compression
    data_bytes = file_content.encode('utf-8')

    # Compress the byte data using maximum compression level 9
    compressed_bytes = zlib.compress(data_bytes, 9)

    # Encode the compressed bytes into Base64 to produce ASCII-safe output
    encoded_bytes = base64.b64encode(compressed_bytes)

    # Convert the encoded bytes back to a UTF-8 string for writing to a text file
    decoded_data = encoded_bytes.decode('utf-8')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decoded_data)


def decompress(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        file_content = file.read()
    encoded_data = file_content.encode('utf-8')
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
    decoded_data = decompressed_data.decode('utf-8')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decoded_data)
