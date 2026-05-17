import base64

english_freq = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228,
    'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025,
    'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987,
    's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150,
    'y': 1.974, 'z': 0.074, ' ': 13.000
}

def hamming_distance(buf1: bytes, buf2: bytes) -> int:
    return sum(bin(a ^ b).count('1') for a, b in zip(buf1, buf2))


def avg_hamming_distance(data: bytes) -> float:
    best_keysize = None
    smallest_distance = float('inf')
    for keysize in range(2, 41):
        edit_distance = 0
        for i in range(0,10):
            edit_distance += hamming_distance(data[i*keysize:(i+1)*keysize], data[(i+1)*keysize:(i+2)*keysize])

        norm_distance = edit_distance / keysize

        if norm_distance < smallest_distance:
            smallest_distance = norm_distance
            best_keysize = keysize

    return best_keysize


def xor_buffers(buf1: bytes, buf2: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(buf1, buf2))

if __name__ == "__main__":  
    with open("challenge6_input.txt", "r") as f:
        data = base64.b64decode(f.read())

    best_keysize = avg_hamming_distance(data)

    blocks = [data[i:i+best_keysize] for i in range(0, len(data), best_keysize)]
    transposed_blocks = []

    for i in range(best_keysize):
        transposed_blocks.append(bytes(block[i] for block in blocks if i < len(block)))

    final_key = ""

    for i, block in enumerate(transposed_blocks):
        best_score = 0
        best_result = None
        best_key = None

        for key in range(256):
            result = xor_buffers(block, bytes([key] * len(block)))

            try:
                decoded = result.decode('utf-8')
            except:
                continue
            
            score = sum(english_freq.get(c.lower(), 0) for c in decoded)

            if score > best_score:
                best_score = score
                best_result = decoded
                best_key = key

        final_key += chr(best_key)
        print(f"Block {i}: Best result: {best_result}, Score: {best_score}")

    print("Final key:", final_key)
