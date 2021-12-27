import secrets


def gen_key(parts=4, chars_per_part=8):
    hex_password = secrets.token_hex(int((parts * chars_per_part) / 2)).upper()
    return '-'.join(
        hex_password[i: i + chars_per_part]
        for i in range(0, len(hex_password), chars_per_part)
    )


gen_key()
