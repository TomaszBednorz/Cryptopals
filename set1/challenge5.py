
INPUT = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

EXPECTED = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""

KEY = "ICE"

def xor_buffers(buf1: bytes, buf2: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(buf1, buf2))

if __name__ == "__main__":
    result = []

    data = INPUT.encode()
    key = KEY.encode()
    for i in range(len(data)):
        xor_result = data[i] ^ key[i % len(key)]
        result.append(xor_result)

    result_hex = "".join(format(x, "02x") for x in result)
    print(result_hex == EXPECTED)
