# SPDX-FileCopyrightText: 2026 DJDevon3
# SPDX-License-Identifier: MIT
# Coded for Python 3.10.5
"""Quagmire Alternating Alphabets 2026-05-26"""

import string

STD = string.ascii_uppercase

def make_safe_filename(s):
    """Remove characters not allowed in Windows filenames."""
    unsafe = '<>:"/\\|?*'
    for ch in unsafe:
        s = s.replace(ch, "")
    return s


def keyword_alphabet(keyword, reverse=False):
    keyword = ''.join(dict.fromkeys(keyword.upper()))
    remain = ''.join(c for c in STD if c not in keyword)

    alpha = keyword + remain

    if reverse:
        alpha = alpha[::-1]

    return alpha


def rotate_to_top(alpha, letter):
    """
    Rotate alphabet so letter becomes first.
    """
    idx = alpha.index(letter)
    return alpha[idx:] + alpha[:idx]


def build_columnar_hybrid_matrix(ciphertext, alphabets):
    """
    First row = ciphertext
    Each column uses alternating alphabets
    """
    columns = []

    for i, c in enumerate(ciphertext):
        alpha = alphabets[i % len(alphabets)]
        rotated = rotate_to_top(alpha, c)
        columns.append(rotated)

    rows = []

    for r in range(26):
        row = [col[r] for col in columns]
        rows.append(row)

    return rows


def print_matrix(matrix):
    """
    Double-spaced console print
    """
    for row in matrix:
        print(" ".join(row))


def save_matrix(matrix, filename):
    """
    Double-spaced file save
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"MULTIPLE ALTERNATING ALPHABETS MATRIX\n")
        f.write(f"Alphabets: {alphabets}\n")
        f.write(f"Keywords:  {keyword0}-{keyword1}-{keyword2}-{keyword3}\n")
        f.write(f"Ciphertext: \n{ciphertext}\n")
        f.write("------------------ Matrix 0 ---------------------------\n")
        for row in matrix:
            f.write(" ".join(row) + "\n")
    print(f"\n\nResults saved to: {filename}")


# Config
ciphertext_mode = "K4"
keyword0 = "KRYPTOS"
keyword1 = "PALIMPSET"
keyword2 = "ABSCI"
keyword3 = "ABC"

A0 = keyword_alphabet(keyword0)
A1 = keyword_alphabet(keyword1, reverse=True)
A2 = keyword_alphabet(keyword2)
A3 = keyword_alphabet(keyword3, reverse=True)
alphabets = [A0, A1, A2, A3]

if (ciphertext_mode == "CUSTOM"):
    ciphertext = ("EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD")
if (ciphertext_mode == "K4"):
    ciphertext = ("OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR")

matrix = build_columnar_hybrid_matrix(ciphertext, alphabets)

# Print to CMD Prompt
print("\nCIPHERTEXT:")
print(" ".join(ciphertext))
print("\nMATRIX:")
print_matrix(matrix)

# Save Results to file
filename = f"Quagmire Alternating Alphabets Results\{keyword0}-{keyword1}-{keyword2}-{keyword3}.txt"
save_matrix(matrix, filename)

