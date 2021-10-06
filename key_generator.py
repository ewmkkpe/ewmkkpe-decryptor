import secrets
from common import *


def main():
    print("=================================================")
    print("[AES CBC 256 bit Secret Key in Hex]")
    secret_key_in_hex = secrets.token_hex(32)
    print(secret_key_in_hex)
    print()
    print("[in Human readable string]")
    print(convert_to_human_readable_string(secret_key_in_hex))

    print("=================================================")
    print("[AES CBC 128 bit IV in Hex]")
    iv_in_hex = secrets.token_hex(16)
    print(iv_in_hex)
    print()
    print("[in Human readable string]")
    print(convert_to_human_readable_string(iv_in_hex))
    print("=================================================")


if __name__ == '__main__':
    main()
