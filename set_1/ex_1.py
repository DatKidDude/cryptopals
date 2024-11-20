from binascii import a2b_hex, b2a_base64

def hex_to_base64(data_hex: bytes) -> bytes:
    """Decode the hex string and encode it using Base64"""
    return b2a_base64(a2b_hex(data_hex), newline=False)


if __name__ == "__main__":
    hex_string = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    solution = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    expected_solution = hex_to_base64(hex_string)
    assert expected_solution == solution
