def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    for c in rgb:
        if c < 0 or c > 255:
            raise ValueError

    return f"#{''.join(f'{hex(c)[2:].upper():0>2}' for c in rgb)}"
