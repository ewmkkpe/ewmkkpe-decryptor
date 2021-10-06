from Crypto.Cipher import AES
import argparse
from common import *


def main():
    # AES CBC 방식, 256bit key with 128bit IV
    parser = argparse.ArgumentParser(description="Decryptor")
    parser.add_argument("-e", "--encrypted-value", dest="encrypted_value", action="store", help="encrypted HEX string", required=True)

    args, _ = parser.parse_known_args()
    encrypted_value = args.encrypted_value
    print(f"Encrypted Value : {encrypted_value}")

    filepath = "./conf/key.json"
    key, iv = load_key_iv(filepath)
    print(f"Length of Key : {8 * len(key)} bits", f"Length of IV : {8 * len(iv)} bits")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_bytes = bytes.fromhex(encrypted_value)
    encrypted_bytes_length = len(encrypted_bytes)
    print(f"Encrypted Bytes Length : {encrypted_bytes_length} Bytes")

    result = unpad(cipher.decrypt(encrypted_bytes))
    print()
    print(f"[Decrypted input]")
    print(result.decode('utf-8'))


if __name__ == '__main__':
    main()
