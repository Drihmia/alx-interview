#!/usr/bin/python3
"""
converting decimal number into a binary number
"""
from math import ceil


def dec_to_bin(num: int) -> str:
    """
    converting decimal number into a binary number as a string
    """
    string = ''
    num_bits = 0
    while True:
        if num < 1:
            break
        if num % 2:
            string += '1'
        else:
            string += '0'
        num //= 2
        num_bits += 1
    reversed_string = string[::-1]
    # h = int(len(reversed_string)/2)
    # string = reversed_string[:h] + ' ' + reversed_string[h:]
    return reversed_string

def dec_to_bin_int(num: int) -> int:
    """
    converting decimal number into a binary number as an integer
    """
    num_bits = 0
    power = 1
    bin_num = 0
    while num > 0:
        if num % 2:
            bin_num += power
        num //= 2
        power *= 10
        num_bits += 1
    # print("inside bin_int", bin_num, num_bits)
    return bin_num


def check_dec_to_bin_int(num: int) -> bool:
    """check if my function dec_to_bin_int is valid"""
    custom = dec_to_bin_int(num)
    builtin = int(bin(num)[2:])
    # print(f"custom: {custom}\nbuilin: {builtin}")
    return custom == builtin

def dec_to_bin_bitwise(num: int) -> int:
    """
    converting decimal number into a binary number as an integer
    using bitwise operations.
    """
    num_bits = 0
    power = 1
    bin_num = 0
    while num > 0:
        if num & 1:
            bin_num += power
        num >>= 1
        power = (power << 3) + (power << 1)
        num_bits += 1
    # print("inside bin_int", bin_num, num_bits)
    return bin_num


def check_dec_to_bitwise(num: int) -> bool:
    """check if my function dec_to_bin_bitwise is valid"""
    custom = dec_to_bin_bitwise(num)
    builtin = int(bin(num)[2:])
    # print(f"custom: {custom}\nbuilin: {builtin}")
    return custom == builtin

def hex_to_bin(hexa: str) -> str:
    """
    converting hexadecimal into a Binary
    """
    # print(hexa)
    return dec_to_bin(int(hexa, 16))


def print_bin(Binary: str) -> None:
    """
    Print binary nums with space after each 4 num_bits
    """
    sep = 6
    Binary = Binary[::-1]
    for i in range(ceil(len(Binary) / 4)):
        Binary = Binary[:sep] + ' ' + Binary[sep:]
        sep += 7
    Binary = Binary[::-1]
    print('---------------', Binary)

def is_valid_utf8(byte_sequence):
    byte_sequence = bytes(byte_sequence)
    try:
        byte_sequence.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False

def is_valid_utf8_list(lst):
    for i in lst:
        print(i, "is", is_valid_utf8(i))
if __name__ == "__main__":
    from time import time, sleep
    # print_bin(dec_to_bin(48))
    # print("bin_int", dec_to_bin_int(48))
    # print_bin(dec_to_bin(49))
    # print("bin_int", dec_to_bin_int(49))
    # print_bin(dec_to_bin(123))
    # print("bin_int", dec_to_bin_int(123))
    # print_bin(dec_to_bin(229))
    # print("bin_int", dec_to_bin_int(229))
    # print("bin_int", dec_to_bin_int(1087155))
    # print("bin_int", dec_to_bin_int(1087155) == int(hex_to_bin("1096B3")))
    # print("bin_int", dec_to_bin_int(66376) == int(hex_to_bin("10348")))
    # print('-----------printing hexa to binary ----------')
    # print_bin(hex_to_bin("D55C"))
    # print_bin(hex_to_bin("10348"))
    # print_bin(hex_to_bin("1096B3"))
    # print(int(hex_to_bin("1096B3")))
    start = time()
    num = 987654
    limit = 1000000
    for i in range(limit):
        check_dec_to_bin_int(num)
    end = time()
    print("using normal operations:", end - start)
    for i in range(limit):
        dec_to_bin_bitwise(num)
    print("using bitwise operatios:", time() - end)
