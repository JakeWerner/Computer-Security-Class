#!/usr/bin/python3
# coding: latin-1
string_one = """CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC�]~��KM�4�XL���Vc�$��En<I���'�+��Z�8�g�i:��Bn�Z���\�`��
:!���h&5���
string_two = """CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC�]~��KM�4�XL���V��$��En<I���'�+��Z�8�g�i:�qBn�Z���\�`���
:!���h&5���

if __name__ == "__main__":
    if string_one == string_two:
        print("Use SHA-256 instead!")
    else:
        print("MD5 is perfectly secure!")