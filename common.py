import json

BS = 16


def unpad(s):
    return s[:-ord(s[len(s)-1:])]


def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def load_key_iv(filepath):
    with open(filepath, "r") as f:
        j = json.load(f)
        key = bytes.fromhex(j['key'])
        iv = bytes.fromhex(j['iv'])
        return key, iv


def convert_to_human_readable_string(string):
    return_string = ""
    for i in range(int(len(string) / 8)):
        return_string += f"{string[(i*8):(i*8+4)]} {string[(i*8+4):(i*8+8)]}\n"

    return return_string
