# SPDX-FileCopyrightText: 2026 DJDevon3
# SPDX-License-Identifier: MIT
# Coded for Python 3.10.5
"""
ACA Quagmire III & IV Encrypt & Decrypt 2026-06-02
"""

import os
import string
import math
from pathlib import Path
STD = string.ascii_uppercase

"""
=========================================================
CONFIGURATION PARAMETERS
top keyworded alphabet is row keyword in mode 3
top keyword only used in mode 4
"""
QUAGMIRE_MODE = "4" # Valid modes: 3 or 4
cryptography_mode = "DECRYPT" # Valid modes: ENCRYPT or DECRYPT
row_keyword = "KRYPTOS"
vertical_keyword = "PALIMPSEST"
top_keyword = "KRYPTOS" # Only used with Quagmire 4
ciphertext_mode = "K1"

# Optional Additional Scytale Post-Processing
enable_scytale = False
scytale_rod_sizes = list(range(1, 15))

# Optional Additional Skip Transposition Post-Processing
enable_skip = False
skip_sizes = list(range(1, 15))
 
if (ciphertext_mode == "CUSTOM"):
    ciphertext = "UNZLSELLXVHVIFYHBJHVWCIWXRZXYXUFYJPQVIUUUSLTWWZLWQITW"
if (ciphertext_mode == "DEMONSTRATION"):
    ciphertext = "W L Y N P A E K A R B A B P N A E Z K X T E E C Y B K A L M L R D M S R S F D B R W Q B S H H F C U W K I K A F K R B O D K I S F Z L O J U T V X K S B U G W C Q B D"
    cryptography_mode = "DECRYPT"
    QUAGMIRE_MODE = "4"
    row_keyword = "KRYPTOS"
    vertical_keyword = "PALIMPSEST"
    top_keyword = "MEDUSA"
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
if (ciphertext_mode == "K4_CRIB"):
    ciphertext = "x x x x x x x x x x x x x x x x x x x x x E A S T N O R T H E A S T x x x x x x x x x x x x x x x x x x x x x x x x x x x x x B E R L I N C L O C K x x x x x x x x x x x x x x x x x x x x x x x"
if (ciphertext_mode == "K1_ENCRYPT"):
    ciphertext = "BETWEENSUBTLESHADINGANDTHEABSENCEOFLIGHTLIESTHENUANCEOFIQLUSION"
if (ciphertext_mode == "K2_ENCRYPT"):
    ciphertext = "I T W A S T O T A L L Y I N V I S I B L E H O W S T H A T P O S S I B L E T H E Y U S E D T H E E A R T H S M A G N E T I C F I E L D X T H E I N F O R M A T I O N W A S G A T H E R E D A N D T R A N S M I T T E D U N D E R G R U U N D T O A N U N K N O W N L O C A T I O N X D O E S L A N G L E Y K N O W A B O U T T H I S T H E Y S H O U L D I T S B U R I E D O U T T H E R E S O M E W H E R E X W H O K N O W S T H E E X A C T L O C A T I O N O N L Y W W T H I S W A S H I S L A S T M E S S A G E X T H I R T Y E I G H T D E G R E E S F I F T Y S E V E N M I N U T E S S I X P O I N T F I V E S E C O N D S N O R T H S E V E N T Y S E V E N D E G R E E S E I G H T M I N U T E S F O R T Y F O U R S E C O N D S W E S T I D B Y R O W S"
    
# =========================================================
# Utility Functions
# =========================================================
def clean_text(text):
    return ''.join(
        c for c in text.upper()
        if c in STD
    )

def keyed_alphabet(keyword):
    keyword = clean_text(keyword)
    seen = set()
    result = []
    for ch in keyword + STD:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return ''.join(result)

def rotate_alphabet(alphabet, start_char):
    idx = alphabet.index(start_char)
    return alphabet[idx:] + alphabet[:idx]

def double_space(text):
    text = clean_text(text)
    return " ".join(text)

def repeat_keyword(keyword, length):
    keyword = clean_text(keyword)
    repeated = ""
    while len(repeated) < length:
        repeated += keyword
    repeated = repeated[:length]
    return repeated

def output(text, file_handle=None):
    """
    Print to console and optionally save to file.
    """
    print(text)

    if file_handle:
        file_handle.write(str(text) + "\n")

# =========================================================
# Build Tableau
# =========================================================
def build_tableau(row_alphabet, vertical_keyword):
    vertical_alpha = keyed_alphabet(
        vertical_keyword
    )
    matrix = []
    for ch in vertical_alpha:
        row = rotate_alphabet(
            row_alphabet,
            ch
        )
        matrix.append(row)
    return matrix

# =========================================================
# Format Output
# =========================================================
def tableau_to_string(mode, top_alphabet, top_keyword, row_alphabet, row_keyword, vertical_keyword, matrix, ciphertext, plaintext):
    lines = []
    ciphertext_clean = clean_text(ciphertext)
    repeated_keyword = repeat_keyword(vertical_keyword,len(ciphertext_clean))
    
    # Quagmire III
    if mode == "3":
        lines.append("    Quagmire III Table")
        lines.append("    -  " + " ".join(row_alphabet))
        
    # Quagmire IV
    elif mode == "4":
        lines.append("    Quagmire IV Table")
        lines.append("    -  " + " ".join(top_alphabet))
    else:
        raise ValueError("INVALID QUAGMIRE MODE MUST BE 3 OR 4")
    for i, row in enumerate(matrix):
        row_string = " ".join(row)
        lines.append(f"    {i+1:02d} {row_string}")
        
    lines.append("\nKeyword")
    lines.append(double_space(repeated_keyword))
    if (cryptography_mode == "DECRYPT"):
        lines.append("\nCiphertext")
        lines.append(double_space(ciphertext_clean))
        lines.append("\nPlaintext (Decrypted)")
        lines.append(double_space(plaintext))
    if (cryptography_mode == "ENCRYPT"):
        lines.append("\nPlaintext")
        lines.append(double_space(ciphertext_clean))
        lines.append("\nCiphertext (Encrypted)")
        lines.append(double_space(plaintext))
    return "\n".join(lines)

# =========================================================
# Save Output
# =========================================================
def decrypt_quagmire(ciphertext,top_alphabet,row_alphabet,vertical_keyword):
    ciphertext = clean_text(ciphertext)
    vertical_keyword = clean_text(vertical_keyword)
    plaintext = []
    repeated_keyword = repeat_keyword(vertical_keyword,len(ciphertext))
    for i, ct_char in enumerate(ciphertext):
        indicator_char = repeated_keyword[i]

        # Build tableau row
        row = rotate_alphabet(
            row_alphabet,
            indicator_char
        )

        # Find ciphertext letter position
        col = row.index(ct_char)

        # Plaintext from top alphabet
        pt_char = top_alphabet[col]
        plaintext.append(pt_char)
    return ''.join(plaintext)
    
def encrypt_quagmire(plaintext,top_alphabet,row_alphabet,vertical_keyword):
    plaintext = clean_text(plaintext)
    vertical_keyword = clean_text(vertical_keyword)
    ciphertext = []
    repeated_keyword = repeat_keyword(vertical_keyword,len(plaintext))
    for i, pt_char in enumerate(plaintext):
        indicator_char = repeated_keyword[i]
        
        # Build tableau
        row = rotate_alphabet(row_alphabet,indicator_char)
        col = top_alphabet.index(pt_char)
        ct_char = row[col]
        ciphertext.append(ct_char)
    return ''.join(ciphertext)

if QUAGMIRE_MODE == "3":
    row_alphabet = keyed_alphabet(row_keyword)
    top_alphabet = row_alphabet
elif QUAGMIRE_MODE == "4":
    top_alphabet = keyed_alphabet(top_keyword)
    row_alphabet = keyed_alphabet(row_keyword)
else:
    raise ValueError(
        "INVALID QUAGMIRE MODE MUST BE 3 OR 4"
    )

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

def get_scytale_results(text, rod_sizes):
    lines = []
    lines.append("\n=============== Scytale Results ===============")
    for rod in rod_sizes:
        result = scytale_decrypt(text, rod)
        spaced = " ".join(result)
        lines.append(f"\nSkip:{rod:02} | {spaced}")
    return "\n".join(lines)
 
# ==========================================
# SKIP CIPHER FUNCTIONS
# ========================================== 
def skip_transposition(text, skip):
    """
    Skip transposition
    """
    step = skip + 1
    result = []
    for start in range(step):
        result.append(text[start::step])
    return ''.join(result)
    
def get_skip_results(text, skip_sizes):
    lines = []
    lines.append("\n=============== Skip Transposition Results ===============")

    for skip in skip_sizes:
        result = skip_transposition(text, skip)
        spaced = " ".join(result)
        lines.append(f"\nSkip:{skip:02} | {spaced}")
    return "\n".join(lines)
    
# ==========================================
# RUN PROGRAM
# ========================================== 
matrix = build_tableau(row_alphabet,vertical_keyword)
if (cryptography_mode=="DECRYPT"):
    plaintext = decrypt_quagmire(ciphertext,top_alphabet,row_alphabet,vertical_keyword)
if (cryptography_mode=="ENCRYPT"):
    plaintext = encrypt_quagmire(ciphertext,top_alphabet,row_alphabet,vertical_keyword)

# console print format
tableau_output = tableau_to_string(
    mode=QUAGMIRE_MODE,
    top_alphabet=top_alphabet,
    top_keyword=top_keyword,
    row_alphabet=row_alphabet,
    row_keyword=row_keyword,
    vertical_keyword=vertical_keyword,
    matrix=matrix,
    ciphertext=ciphertext,
    plaintext=plaintext
)

# save to txt file
first_ten = ciphertext[0:10]
output_dir = "Quagmire III IV Results"
os.makedirs(output_dir, exist_ok=True)
filename = os.path.join(output_dir,f"{cryptography_mode}_Q{QUAGMIRE_MODE.replace(' ', '_')}_({row_keyword}-{vertical_keyword})_{first_ten}.txt")

with open(filename, "w", encoding="utf-8") as f:
    output("=" * 45, f)
    output(f"Method: {cryptography_mode}", f)
    output(f"Top Alphabet: {top_alphabet}", f)
    output(f"Row Alphabet: {row_alphabet}", f)
    output(f"Vertical Keyword: {vertical_keyword}", f)
    output(f"Custom Mode: {QUAGMIRE_MODE.replace(' ', '_')}", f)
    output(f"Ciphertext: {ciphertext}", f)
    output(f"Ciphertext Length: {len(ciphertext)}\n", f)
    output(f"{tableau_output}", f)
    if enable_scytale:
        scytale_output = get_scytale_results(plaintext, scytale_rod_sizes)
        output(scytale_output, f)
    if enable_skip:
        skip_output = get_skip_results(plaintext, skip_sizes)
        output(skip_output, f)
    
print(f"\nResults saved to: {filename}")
