import base64


INPUT1 = "1c0111001f010100061a024b53535009181c"
INPUT2 = "686974207468652062756c6c277320657965"
EXPECTED = "746865206b696420646f6e277420706c6179"

def xor_buffers(buf1: bytes, buf2: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(buf1, buf2))

if __name__ == "__main__":
    result = xor_buffers(bytes.fromhex(INPUT1), bytes.fromhex(INPUT2))
    result_hex = result.hex()
    print(result_hex == EXPECTED)