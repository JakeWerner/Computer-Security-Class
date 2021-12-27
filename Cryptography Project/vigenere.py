#!/usr/bin/python3

import sys
from collections import Counter

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)

# Func to find the mean of the frequency variances of a ciphertext
# Created from description in problem 4 of 2.1
def mean_var(s, key_length):
    if key_length > 1:
        freq_vars = []
        for i in range(0, key_length):
            freq_vars.append(pop_var(s[i::key_length]))
        return sum(freq_vars) / len(freq_vars)
    else:
        pop_var(s)

# Func that determines a string key of a Vigenere Cipher given
# prob_key_length: The most probable length of the key
# s: The ciphertext
# pop_var_of_english: The population variance of relative letter frequencies in English text
def determine_key(prob_key_length, s, pop_var_of_english):
    key_string = ""

    for i in range(0, prob_key_length):
        chi_squared_vals = {}
        # Starting at index 'i' in the ciphertext, obtain every other 'prob_key_length' 
        # character and find it's Caesar Cipher key
        current_ceas_ciph_str = s[i::prob_key_length]
        # Iterate through all 26 possible Caesar Cipher keys
        for ii in range(0, 26):
            new_ceas_string = ""
            for iii in range(0, len(current_ceas_ciph_str)):
                ceas_value = alphabet[(alphabet.find(current_ceas_ciph_str[iii]) - ii) % 26]
                new_ceas_string += ceas_value
            # Calculate letter frequencies of every character in given deciphered text
            freqs = Counter(new_ceas_string)
            chi_squared_val = 0
            # Iterate through all 26 English characters
            for iv in range(0, 26):
                current_letter = alphabet[iv]
                # Given the letter frequencies of each character in the alphabet, calculate the
                # expected number of characters we should see for the current iterated character in the deciphered text
                expected_num_letters = len(new_ceas_string) * letter_freqs[current_letter]
                # Perform a chi-squared test between the expected number of characters
                # and the actual number of characters we see for the current iterated character,
                # then sum all those chi-squared values together
                chi_squared_val += ((freqs[current_letter] - expected_num_letters) ** 2) / expected_num_letters
            # Store the summed chi-squared test into the current Ceasar Cipher key's
            # dictionary position we are testing
            chi_squared_vals[alphabet[ii]] = chi_squared_val
        # We find the Caesar Cipher key that yielded the most "English-like" deciphered text,
        # which is the key that had the lowest chi-squared value, then add that Caeser Cipher
        # key to the current Vigenere Cipher key we are constructing
        key_string += min(chi_squared_vals, key=chi_squared_vals.get)
    
    return key_string

# Func to decrypt a Caesar Cipher text given the key
# Used in debugging
def caesar_decrypt(s, key):
    decrypt_text = ""
    key_length = len(key)
    for i in range(len(s)):
        current_key_letter = key[i % key_length]
        decrypt_text += alphabet[(alphabet.find(s[i]) - alphabet.find(current_key_letter)) % 26]
    return decrypt_text


if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()

    #################################################################
    # Your code to determine the key and decrypt the ciphertext here

    # Problem 1
    # Calculates the population variance of relative letter frequencies within English text
    mu = sum(float(letter_freqs[v]) for v in letter_freqs)/len(letter_freqs)
    pop_var_of_english = sum((float(letter_freqs[c])-mu)**2 for c in letter_freqs)/len(letter_freqs)

    # Calculate most probable key length
    prob_key_length = 0
    mean_var_abs_diffs = {}
    # Iterate through each possible key length
    for i in range(2, 14):
        a = mean_var(cipher, i)
        # Calculate the difference between the population variance of English text
        # and the mean of the frequency variances in the ciphertext of a given key length,
        # then store in a list
        mean_var_abs_diffs[i] = abs(pop_var_of_english - a)
    # The probable key length is the key length that gives the most "English-like" ciphertext,
    # or the lowest difference between pop. var. of English text and mean freq. var. of ciphertext of a given key length
    prob_key_length = min(mean_var_abs_diffs, key=mean_var_abs_diffs.get)

    if prob_key_length > 0:
        # Determine Vigenere Cipher key
        key_string = determine_key(prob_key_length, cipher, pop_var_of_english)
        print(key_string)
    else:
        print("")