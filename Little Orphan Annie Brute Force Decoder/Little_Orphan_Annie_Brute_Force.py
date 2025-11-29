import os

# ----------------------------------------------
# CIPHERTEXT INPUT AND KEY (KEYS ARE NUMERIC 0-25)
# It will attempt all possible keys anyway.
# Included example is a real Little Orphan Annie code from 1936
# Even if you don't know the year or key this will brute force all possible solutions
# using every possible Little Orphan Annie & Captain Midnight decoder ring/badge. 
# ----------------------------------------------
key = 14
cipher = "19 05 21 15 02 09 06 10 08 21 13 20 20 06 23 02 01 15 13 15 17 09 06 23 14 02"
# ----------------------------------------------

def make_safe_filename(s):
    unsafe = '<>:"/\\|?*'
    for ch in unsafe:
        s = s.replace(ch, "")
    return s
    

def normalize_alphabet(alphabet):
    if isinstance(alphabet, str):
        return list(alphabet)
    return alphabet


def encode_number_string(num_string, alphabet):
    alphabet = normalize_alphabet(alphabet)
    output = ""
    nums = []

    # Accept both "190522 or 19 05 22"
    if " " not in num_string:
        nums = [num_string[i:i+2] for i in range(0, len(num_string), 2)]
    else:
        nums = num_string.split()

    for n in nums:
        idx = int(n) - 1
        output += alphabet[idx]

    return output


def caesar_key(text, key, alphabet):
    alphabet = normalize_alphabet(alphabet)
    size = len(alphabet)
    transformed = ""

    for ch in text:
        if ch in alphabet:
            old = alphabet.index(ch)
            new = (old + key) % size
            transformed += alphabet[new]
        else:
            transformed += ch
    return transformed


def decode_number_caesar(num_string, key, alphabet):
    letters = encode_number_string(num_string, alphabet)
    return caesar_key(letters, key, alphabet)


def build_caesar_matrix(text, alphabet, double_space=True):
    alphabet = alphabet.upper()
    text = text.upper()
    L = len(alphabet)
    matrix = []

    for key in range(L):
        decoded = ""
        for char in text:
            if char in alphabet:
                old_idx = alphabet.index(char)
                new_idx = (old_idx + key) % L
                decoded += alphabet[new_idx]
            else:
                decoded += char

        if double_space:
            decoded = " ".join(decoded)

        row = f"{key:02d}: {decoded}"
        matrix.append(row)

    return matrix


def generate_all_in_one_file(cipher, key, alphabets):
    os.makedirs("Results", exist_ok=True)

    strip_spaces = cipher.replace(" ", "")
    first_five = strip_spaces[0:5]

    # Build one combined output filename
    combined_filename = f"Results/LittleOrphanAnnie-{first_five}-ALL-{key}.txt"

    with open(combined_filename, "w", encoding="utf-8") as out:

        # Header for file
        out.write("============== Little Orphan Annie Brute Caesar Matrix File ==============\n")
        out.write(f"Ciphertext Numbers: {cipher}\n")
        out.write(f"Preferred Offset Key: {key}\n")
        out.write("==========================================================================\n\n")

        # Process each alphabet
        for year, alphabet in alphabets.items():

            # Decode using numeric Caesar
            decoded = decode_number_caesar(cipher, key, alphabet)

            # Write header for this alphabet
            out.write(f"Alphabet ({year}): {alphabet}\n")
            out.write(f"Decoded Text: {decoded}\n\n")
            out.write("----- Caesar Matrix -----\n\n")

            # Build and write matrix
            matrix = build_caesar_matrix(decoded, alphabet, double_space=True)
            out.write("\n".join(matrix))
            out.write("\n\n============================================================\n\n")

    print(f"\nAll matrices saved into one file:\n{combined_filename}\n")
    return combined_filename


# ----------------------------------------------
# ALPHABETS & INPUT
# ----------------------------------------------

alphabets = {
    1935: "AMZNBLYOKCQXJDRWIESVHGTFUP",
    1936: "AGTPBHMCSQDFZLNEVJYIWUROKX",
    1937: "AOIPBNMDSQCFXEHLVJYTWURGKX",
    1938: "ALVYUTXZWJSNQIBMGPFCKRODHE",
    1939: "ACEBFDGPMNLKQRWVXUYSHJTIZO",
    1940: "ACEBGHFDJILMKWNORPQSUTVYZX",
    1941: "AXNQEGMKFWZHIOBLTDSRCJVUPY",
    1942: "AEXDTZKNYCJWSGUMBOQHRIVFPL",
    1945: "AFXDTZKNYCJWSGUMPOQHRIVEBL",
    1946: "AGHTVQSEOYJIFLXKDCWRBONZMU",
    1947: "ATMPQUOVFYBHJNCIXSDKRGWLEZ",
    1948: "ALVYUTXZWJSNQIBMGPFCKRODHE",
    1949: "AEHDORKCFPGMBIQNSJWZXTUYVL"
}

# Generate unified file
generate_all_in_one_file(cipher, key, alphabets)
