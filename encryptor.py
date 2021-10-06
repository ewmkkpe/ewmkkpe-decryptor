from Crypto.Cipher import AES
import argparse
from common import *


def main():
    # AES CBC 방식, 256bit key with 128bit IV
    parser = argparse.ArgumentParser(description="Decryptor")
    parser.add_argument("-i", "--input-string", dest="input_string", action="store", help="plain string to encrypt", required=True)

    args, _ = parser.parse_known_args()
    input_string = args.input_string
    print(f"Input String : {input_string}")

    filepath = "./conf/key.json"
    key, iv = load_key_iv(filepath)
    print(f"Length of Key : {8 * len(key)} bits", f"Length of IV : {8 * len(iv)} bits")

    raw = pad(input_string)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = cipher.encrypt(raw)
    output_value = result.hex()

    print()
    print(f"[Encrypted Hex string]")
    print(output_value)

    print()
    print(f"[Human-Readable Encrypted Hex string]")
    print(convert_to_human_readable_string(output_value))


if __name__ == '__main__':
    main()
