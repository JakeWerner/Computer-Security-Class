#!/usr/bin/python3
# coding: latin-1
string_one = """CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCÅ]~Ÿ³KMû4üXLœˆÑVãí$ÎEn<I²œ›'¡+ÀøZ«8gäi:ãqBn÷ZÅÖÚ\À`‰¥†
:!ýïÍh&5ÉÔþ­)3Ö"3ý<àUÅ{ÉUq}"7WÂop‡óÃ«À/©5W¨ŽàèUg;$ÚVŠ”êÇ!CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"""
string_two = """CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCÅ]~Ÿ³KMû4üXLœˆÑVãí$ÎEn<I²œ›'¡+ÀøZ«8gäi:ãqBn÷ZÅÖÚ\À`‰¥†
:!ýïÍh&5ÉÔþ­)3Ö"3ý<àUÅ{ÉUq}"7WÂop‡óÃ«À/©5W¨ŽàèUg;$ÚVŠ”êÇ!CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"""

if __name__ == "__main__":
    if string_one == string_two:
        print("Use SHA-256 instead!")
    else:
        print("MD5 is perfectly secure!")
