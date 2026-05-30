# SPDX-FileCopyrightText: 2026 DJDevon3
# SPDX-License-Identifier: MIT
# Coded for Python 3.10.5
"""
Quagmire III Brute Force Keyword Search with Crib Words
Tests A-Z of a specified character length
How long the script takes depends on how many 
matches it produces, there is no calculable ETA.
"""
import itertools
import string
import time
start_time = time.perf_counter()
ALPHABET = string.ascii_uppercase
STD = string.ascii_uppercase

# ============================================================
# CONFIGURATION: CRIB WORDS AT INDEXED POSITIONS
# INDEX STARTS AT 0! (22 is actually 21) 
# Example for multiple words starting at index position:
# [(21, "EAST"),(25, "NORTH"), (30, "EAST")]
# The more words you index for search the longer it takes
# Doing them individually is orders of magnitude faster 
# ============================================================
ciphertext_mode = "K4"
KEYWORD_LENGTH = 4
ALPHABET_KEYWORD = "KRYPTOS"
# At least 1 crib word required. 
# This script is only for searches with crib words. 
KNOWN_WORDS = [(21, "EAST")] 

if (ciphertext_mode == "CUSTOM"):
    ciphertext = "OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR"
if (ciphertext_mode == "DEMONSTRATION"): 
    # Variable overrides for demonstration mode
    ciphertext = "UNZLSELLXVHVIFYHBJHVWCIWXRZXYXUFYJPQVIUUUSLTWWZLWQIT"
    KEYWORD_LENGTH = 4
    ALPHABET_KEYWORD = "KRYPTOS"
    KNOWN_WORDS = [(11, "EXAM")]
if (ciphertext_mode == "K1"):
    ciphertext = "EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD"
if (ciphertext_mode == "K2"):
    ciphertext = "VFPJUDEEHZWETZYVGWHKKQETGFQJNCEGGWHKKDQMCPFQZDQMMIAGPFXHQRLGTIMVMZJANQLVKQEDAGDVFRPJUNGEUNAQZGZLECGYUXUEENJTBJLBQCRTBJDFHRRYIZETKZEMVDUFKSJHKFWHKUWQLSZFTIHHDDDUVHDWKBFUFPWNTDFIYCUQZEREEVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDXFLGGTEZFKZBSFDQVGOGIPUFXHHDRKFFHQNTGPUAECNUVPDJMQCLQUMUNEDFQELZZVRRGKFFVOEEXBDMVPNFQXEZLGREDNQFMPNZGLFLPMRJQYALMGNUVPDXVKPDQUMEBEDMHDAFMJGZNUPLGEWJLLAETG"
if (ciphertext_mode == "K3"):
    ciphertext = "ENDYAHROHNLSRHEOCPTEOIBIDYSHNAIACHTNREYULDSLLSLLNOHSNOSMRWXMNETPRNGATIHNRARPESLNNELEBLPIIACAEWMTWNDITEENRAHCTENEUDRETNHAEOETFOLSEDTIWENHAEIOYTEYQHEENCTAYCREIFTBRSPAMHHEWENATAMATEGYEERLBTEEFOASFIOTUETUAEOTOARMAEERTNRTIBSEDDNIAAHTTMSTEWPIEROAGRIEWFEBAECTDDHILCEIHSITEGOEAOSDDRYDLORITRKLMLEHAGTDHARDPNEOHMGFMFEUHEECDMRIPFEIMEHNLSSTTRTVDOHW"
if (ciphertext_mode == "K4"):
    ciphertext = "OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR"
if (ciphertext_mode == "K4_SNAKE"):
    ciphertext = "O B K R O S S K G N R P Q Q V R L F W B B F I L O S B L U H G O X O U T W T Q S J Q S S E K Z Z W A T J K L U D I A W I N F B N Y P R A C K E U A U H U K G I D C J T X Z K D G W K P F Z M T T V"

# ============================================================
# UTILITY FUNCTIONS
# ============================================================
def clean_text(text):
    return ''.join(
        c for c in text.upper()
        if c in STD
    )
    
ciphertext_clean = clean_text(ciphertext)
total_keys = 26 ** KEYWORD_LENGTH

def time_calc(input_time):
    """
    Converts seconds into minutes, hours, or days
    """
    if input_time < 60:
        return f"{input_time:.0f} seconds"
    if input_time < 3600:
        return f"{input_time / 60:.0f} minutes"
    if input_time < 86400:
        return f"{input_time / 60 / 60:.0f} hours"
    return f"{input_time / 60 / 60 / 24:.1f} days"
# ============================================================
# BUILD CRIB TABLE
# ============================================================
def build_crib(words):
    """
    Sets crib words into array positions
    If using multiple words it checks for invalid overlap
    """
    crib = {}
    for start_pos, word in words:
        word = word.upper()
        for offset, letter in enumerate(word):
            pos = start_pos + offset
            if pos in crib and crib[pos] != letter:
                raise ValueError(
                    f"Conflicting crib at position {pos}"
                )
            crib[pos] = letter
    return crib
    
CRIB = build_crib(KNOWN_WORDS)

def generate_keywords(length):
    for chars in itertools.product(ALPHABET, repeat=length):
        yield ''.join(chars)

def keyed_alphabet(keyword):
    """
    Create keyed alphabet.
    """
    seen = set()
    result = []

    for ch in keyword.upper():
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            result.append(ch)

    for ch in ALPHABET:
        if ch not in seen:
            result.append(ch)

    return ''.join(result)


def rotate_alphabet(alphabet, start_char):
    """
    Rotate alphabet so start_char becomes position 0
    """
    idx = alphabet.index(start_char)
    return alphabet[idx:] + alphabet[:idx]
    
def double_space(text):
    text = clean_text(text)
    return " ".join(text)

KEYED_ALPHABET = keyed_alphabet(ALPHABET_KEYWORD)
# ============================================================
# CACHE LOOKUP TABLE
# ============================================================
ROW_CACHE = {}
for indicator in ALPHABET:
    row = rotate_alphabet(
        KEYED_ALPHABET,
        indicator
    )
    lookup = {
        cipher: plain
        for cipher, plain in zip(
            row,
            KEYED_ALPHABET
        )
    }
    ROW_CACHE[indicator] = lookup

def decrypt_char(cipher_char, vertical_keyword, index):
    indicator_char = vertical_keyword[
        index % len(vertical_keyword)
    ]
    return ROW_CACHE[indicator_char][cipher_char]

# ============================================================
# EARLY-REJECTION DECRYPTION
# ============================================================
def decrypt_and_check(ciphertext_clean, keyword, crib):
    """
    Decrypt while checking crib positions
    """
    plaintext = []
    for index, cipher_char in enumerate(ciphertext_clean):
        plain_char = decrypt_char(
            cipher_char,
            keyword,
            index
        )
        # Reject immediately if crib position fails
        if index in crib:
            if plain_char != crib[index]:
                return None
        plaintext.append(plain_char)
    return ''.join(plaintext)


# ============================================================
# MAIN BRUTE FORCE LOOP & CONSOLE PRINT
# ============================================================
def brute_force(ciphertext_clean, keyword_length, crib):
    total = 26 ** keyword_length
    print(f"Testing {total:,} keywords...\n")
    matches = []
    for count, keyword in enumerate(
        generate_keywords(keyword_length),
        start=1
    ):
        if count % 100000 == 0:
            print(f"{count:,}/{total:,}")
        plaintext = decrypt_and_check(
            ciphertext_clean,
            keyword,
            crib
        )
        if plaintext:
            matches.append((keyword, plaintext))
            print("\nMATCH FOUND")
            print(f"Keyword:{keyword}\n{double_space(plaintext)}\n")
    return matches

# ============================================================
# SAVE RESULTS TO TEXT FILE
# ============================================================

def save_output(filename, results):
    """
    Save results to text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write("QUAGMIRE III KEYWORD BRUTE FORCE\n")
        f.write(f"Mode: {ciphertext_mode}\n")
        f.write(f"Vigenere Alphabet: {KEYED_ALPHABET}\n")
        f.write(f"Crib Position & Word: {KNOWN_WORDS[0][0]}-{KNOWN_WORDS[0][1]}\n")
        f.write(f"Key Length: {KEYWORD_LENGTH}\n")
        f.write(f"Ciphertext:{' ' * int(KEYWORD_LENGTH+12)}{double_space(ciphertext_clean)}\n")
        f.write(f"Total Matches: {len(results)}\n")
        f.write("=" * 80 + "\n\n")
        for count, (keyword, plaintext) in enumerate(results, start=1):
            f.write(f"Keyword: {keyword} | Plaintext: {double_space(plaintext)}\n\n")
        f.write("=" * 80 + "\n")
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        f.write(f"Keys Processed: {total_keys:,}\n")
        f.write(f"Process Duration: {time_calc(elapsed_time)}")
    
first_ten = ciphertext[0:10]
# ============================================================
# CONSOLE PRINT
# ============================================================
print(f"  Mode: {ciphertext_mode}")
print(f"  Vigenere Alphabet:{KEYED_ALPHABET}")
print(f"  Ciphertext:\n{double_space(ciphertext_clean)}")
print(f"  Crib:{KNOWN_WORDS[0]}")
print(f"  Keyword Length:{KEYWORD_LENGTH}\n")
# ============================================================
# RUN PROGRAM
# ============================================================
if __name__ == "__main__":
    results = brute_force(ciphertext_clean,KEYWORD_LENGTH,CRIB)
    print("\nFINISHED")
    print(f"Matches found: {len(results)}")
    end_time2 = time.perf_counter()
    elapsed_time2 = end_time2 - start_time
    print(f"Keys Processed: {total_keys:,}")
    print(f"Process Duration: {time_calc(elapsed_time2)}")
    print("============================================================")
    
    output_filename = (f"Quagmire Brute Force with Crib Results\{ciphertext_mode}_{KEYWORD_LENGTH}_({KNOWN_WORDS[0][0]}-{KNOWN_WORDS[0][1]})_{first_ten}.txt")
    save_output(output_filename,results)
    print(f"Saved to:{output_filename}")
    