import base64


INPUT = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
EXPECTED = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


if __name__ == "__main__":
    bytes_representation = bytes.fromhex(INPUT)  
    base64_representation = base64.b64encode(bytes_representation)

    print(base64_representation == EXPECTED)