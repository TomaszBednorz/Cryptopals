import base64

english_freq = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228,
    'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025,
    'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987,
    's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150,
    'y': 1.974, 'z': 0.074, ' ': 13.000
}

INPUT = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def xor_buffers(buf1: bytes, buf2: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(buf1, buf2))

if __name__ == "__main__":
    data = bytes.fromhex(INPUT)

    best_score = 0
    best_result = None
    for key in range(256):
        result = xor_buffers(data, bytes([key] * len(data)))

        try:
            decoded = result.decode('utf-8')
        except:
            continue
        
        score = sum(english_freq.get(c.lower(), 0) for c in decoded)

        if score > best_score:
            best_score = score
            best_result = decoded
            
    print("Best result:", best_result)
    print("Score:", best_score)