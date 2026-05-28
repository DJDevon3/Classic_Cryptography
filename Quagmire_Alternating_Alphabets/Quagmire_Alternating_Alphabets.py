# SPDX-FileCopyrightText: 2026 DJDevon3
# SPDX-License-Identifier: MIT
# Coded for Python 3.10.5
"""
Quagmire Alternating Alphabets + Scytale Decryption 2026-05-28
"""

import string
import math

STD = string.ascii_uppercase

"""
Script Configuration Options
You can make a standard Caesar matrix by setting 
alternating to false & number of alphabets to 1
You can make a fully custom alphabet by inputting your
entire 26 character alphabet instead of a keyword
"""
ciphertext_mode = "K4"
number_of_alphabets = "4" # 1 to 4 optional
alternating_direction = True  # True or False
keyword0 = "ABC"
keyword1 = "ABC"
keyword2 = "ABC"
keyword3 = "ABC"

# Optional Additional Scytale Post-Processing
enable_scytale = True
scytale_rod_sizes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# For adding custom variations that can be switched to with ciphertext mode switch
if (ciphertext_mode == "CUSTOM"):
    ciphertext = ("T H I S I S A T E S T C I P H E R O F A N O V E L A L T E R N A T I N G K E Y W O R D E D C A E S A R M A T R I X E N C R Y P T I O N B Y R E D D I T U S E R B L O W N G U S T")
if (ciphertext_mode == "K4_SNAKE"):
    ciphertext = ("O B K R O S S K G N R P Q Q V R L F W B B F I L O S B L U H G O X O U T W T Q S J Q S S E K Z Z W A T J K L U D I A W I N F B N Y P R A C K E U A U H U K G I D C J T X Z K D G W K P F Z M T T V")
if (ciphertext_mode == "K4"):
    ciphertext = ("OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR")
if (ciphertext_mode == "K4_SCYTALE_3"):
    ciphertext = ("O R X H B L B F V P G S W S S K W J U A N N V M P G Z J I U A K R B U O U S I B L Q R K O T J S Z A K D W F Y T Z K D X C G H U C K O G L O F W R Q N S T Q Q E Z T L I I B P T F W K T D K U E A")
if (ciphertext_mode == "K4_CRIB"):
    ciphertext = ("x x x x x x x x x x x x x x x x x x x x x E A S T N O R T H E A S T x x x x x x x x x x x x x x x x x x x x x x x x x x x x x B E R L I N C L O C K x x x x x x x x x x x x x x x x x x x x x x x")
if (ciphertext_mode == "K1"):
    ciphertext = ("EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD")
ciphertext = ciphertext.upper()
ciphertext = ciphertext.replace(" ", "")
first_ten = ciphertext[0:10]

# ==========================================
# FUNCTIONS
# ==========================================

def make_safe_filename(s):
    """
    Remove characters not allowed in Windows filenames.
    """
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

def print_matrix_reverse(matrix):
    """
    Reversed double-spaced console print
    """
    for row in matrix:
        print(" ".join(row[::-1]))

# ==========================================
# SCYTALE FUNCTIONS
# ==========================================

def scytale_decrypt(text, rod_size):
    """
    Standard scytale decryption
    """
    length = len(text)
    cols = math.ceil(length / rod_size)
    grid = [['' for _ in range(cols)] for _ in range(rod_size)]
    idx = 0
    for r in range(rod_size):
        for c in range(cols):

            if idx < length:
                grid[r][c] = text[idx]
                idx += 1
    plaintext = ""
    for c in range(cols):
        for r in range(rod_size):

            if grid[r][c]:
                plaintext += grid[r][c]
    return plaintext


def scytale_decrypt_from_rows(rows, rod_size):
    """
    Apply scytale decryption to matrix row results
    """
    decrypted_rows = []
    for row in rows:
        text = ''.join(row)
        decrypted = scytale_decrypt(text, rod_size)
        decrypted_rows.append(decrypted)
    return decrypted_rows


def print_scytale_results(rows, rod_sizes):
    print(f"\n=============== Forward Matrix Results processed into Scytale Skip ===============")
    for rod in rod_sizes:
        print(f"\n------------------ Scytale Rod Size {rod} ------------------")
        results = scytale_decrypt_from_rows(rows, rod)
        for i, result in enumerate(results):
            spaced = " ".join(result)
            print(spaced)

# ==========================================
# SAVE RESULTS TO TXT FILE
# ==========================================
def save_matrix(matrix, filename):
    """
    Header with processes used 
    makes backtracking, file searching, or sharing results easier
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"MULTIPLE ALTERNATING ALPHABETS MATRIX\n")
        f.write(f"Mode:  {ciphertext_mode}\n")
        f.write(f"Alternating:  {alternating_direction}\n")
        f.write(f"Alphabets:{number_of_alphabets} {alphabets}\n")
        if (number_of_alphabets == "1"):    
            f.write(f"Keywords:  {rkey0}\n")
        if (number_of_alphabets == "2"):
            f.write(f"Keywords:  {rkey0}-{rkey1}\n")
        if (number_of_alphabets == "3"):
            f.write(f"Keywords:  {rkey0}-{rkey1}-{rkey2}\n")
        if (number_of_alphabets == "4"):
            f.write(f"Keywords:  {rkey0}-{rkey1}-{rkey2}-{rkey3}\n")
        f.write(f"Ciphertext: \n{ciphertext}\n")
        f.write("\n------------------ Matrix Result Forward ------------------\n")
        for row in matrix:
            f.write(" ".join(row) + "\n")
        f.write("\n------------------ Matrix Result Reverse ------------------\n")
        for row in matrix:
            f.write(" ".join(row[::-1]) + "\n")
            
        #Optional: Forward results only are then processed with Scytale
        if enable_scytale:
            f.write(f"\n=============== Forward Matrix Results processed into Scytale Skip ===============\n")
            for rod in scytale_rod_sizes:
                f.write(f"\n------------------ Scytale Rod Size {rod} ------------------\n")
                results = scytale_decrypt_from_rows(matrix, rod)
                for i, result in enumerate(results):
                    spaced = " ".join(result)
                    f.write(spaced + "\n")
                    
    print(f"\n\nResults saved to: {filename}")

# ==========================================
# BUILD ALPHABETS
# ==========================================

if (alternating_direction):

    A0 = keyword_alphabet(keyword0)
    A1 = keyword_alphabet(keyword1, reverse=True)
    A2 = keyword_alphabet(keyword2)
    A3 = keyword_alphabet(keyword3, reverse=True)

else:

    A0 = keyword_alphabet(keyword0)
    A1 = keyword_alphabet(keyword1)
    A2 = keyword_alphabet(keyword2)
    A3 = keyword_alphabet(keyword3)

# Current hardcoded limit is 4

if (number_of_alphabets == "1"):
    alphabets = [A0]

if (number_of_alphabets == "2"):
    alphabets = [A0, A1]

if (number_of_alphabets == "3"):
    alphabets = [A0, A1, A2]

if (number_of_alphabets == "4"):
    alphabets = [A0, A1, A2, A3]

# ==========================================
# BUILD MATRIX
# ==========================================
matrix = build_columnar_hybrid_matrix(ciphertext, alphabets)

# Print to CMD Prompt
print("\nCIPHERTEXT:")
print(" ".join(ciphertext))
print("\nMATRIX FORWARD:")
print_matrix(matrix)
print("\nMATRIX REVERSE:")
print_matrix_reverse(matrix)
if enable_scytale:
    print_scytale_results(matrix, scytale_rod_sizes)
    
# Save Results to file
if (alternating_direction):
    rkey0 = reverse_keyword(keyword0)
    rkey1 = reverse_keyword(keyword1, reverse=True)
    rkey2 = reverse_keyword(keyword2)
    rkey3 = reverse_keyword(keyword3, reverse=True)
    alt = "_ALT"
if not (alternating_direction):
    rkey0 = reverse_keyword(keyword0)
    rkey1 = reverse_keyword(keyword1)
    rkey2 = reverse_keyword(keyword2)
    rkey3 = reverse_keyword(keyword3)
    alt = ""

if (number_of_alphabets == "1"):    
    filename = f"Quagmire Alternating Alphabets Results\{ciphertext_mode}_({rkey0})_{first_ten}{alt}.txt"
if (number_of_alphabets == "2"):
    filename = f"Quagmire Alternating Alphabets Results\{ciphertext_mode}_({rkey0}-{rkey1})_{first_ten}{alt}.txt"
if (number_of_alphabets == "3"):
    filename = f"Quagmire Alternating Alphabets Results\{ciphertext_mode}_({rkey0}-{rkey1}-{rkey2})_{first_ten}{alt}.txt"
if (number_of_alphabets == "4"):
    filename = f"Quagmire Alternating Alphabets Results\{ciphertext_mode}_({rkey0}-{rkey1}-{rkey2}-{rkey3})_{first_ten}{alt}.txt"

save_matrix(matrix, filename)