# SPDX-FileCopyrightText: 2026 DJDevon3
# SPDX-License-Identifier: MIT
# Coded for Python 3.10.5
"""Quagmire Alternating Alphabets 2026-05-26"""

import string
STD = string.ascii_uppercase

# Script Configuration Options
ciphertext_mode = "K4"
keyword0 = "ABC"
keyword1 = "ABC"
keyword2 = "ABC"
keyword3 = "ABC"

if (ciphertext_mode == "CUSTOM"):
    ciphertext = ("EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD")
if (ciphertext_mode == "K4_SNAKE"):
    ciphertext = ("O B K R O S S K G N R P Q Q V R L F W B B F I L O S B L U H G O X O U T W T Q S J Q S S E K Z Z W A T J K L U D I A W I N F B N Y P R A C K E U A U H U K G I D C J T X Z K D G W K P F Z M T T V")
if (ciphertext_mode == "K4"):
    ciphertext = ("OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR")
if (ciphertext_mode == "K4_SCYTALE_3"):
    ciphertext = ("O R X H B L B F V P G S W S S K W J U A N N V M P G Z J I U A K R B U O U S I B L Q R K O T J S Z A K D W F Y T Z K D X C G H U C K O G L O F W R Q N S T Q Q E Z T L I I B P T F W K T D K U E A")
if (ciphertext_mode == "K4_CRIB"):
    ciphertext = ("x x x x x x x x x x x x x x x x x x x x x E A S T N O R T H E A S T x x x x x x x x x x x x x x x x x x x x x x x x x x x x x B E R L I N C L O C K x x x x x x x x x x x x x x x x x x x x x x x")
ciphertext = ciphertext.upper()
ciphertext = ciphertext.replace(" ", "")
first_ten = ciphertext[0:10]


def make_safe_filename(s):
    """Remove characters not allowed in Windows filenames."""
    unsafe = '<>:"/\\|?*'
    for ch in unsafe:
        s = s.replace(ch, "")
    return s

def reverse_keyword(keyword, reverse=False):
    if reverse:
        keyword = keyword[::-1]

    return keyword

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
        f.write(f"Keywords:  {rkey0}-{rkey1}-{rkey2}-{rkey3}\n")
        f.write(f"Ciphertext: \n{ciphertext}\n")
        f.write("------------------ Matrix 0 ---------------------------\n")
        for row in matrix:
            f.write(" ".join(row) + "\n")
    print(f"\n\nResults saved to: {filename}")

# Reverse scheme is identical regardless of alternating start. 
# The column alphabet direction simply reverses, it's 100% recriprocal. 
# No alternating parameter to switch them is needed. 
A0 = keyword_alphabet(keyword0)
A1 = keyword_alphabet(keyword1, reverse=True)
A2 = keyword_alphabet(keyword2)
A3 = keyword_alphabet(keyword3, reverse=True)
alphabets = [A0, A1, A2, A3]

matrix = build_columnar_hybrid_matrix(ciphertext, alphabets)

# Print to CMD Prompt
print("\nCIPHERTEXT:")
print(" ".join(ciphertext))
print("\nMATRIX:")
print_matrix(matrix)

# Save Results to file
rkey0 = reverse_keyword(keyword0)
rkey1 = reverse_keyword(keyword1, reverse=True)
rkey2 = reverse_keyword(keyword2)
rkey3 = reverse_keyword(keyword3, reverse=True)
 
filename = f"Quagmire Alternating Alphabets Results\{rkey0}-{rkey1}-{rkey2}-{rkey3}_{first_ten}.txt"
save_matrix(matrix, filename)

