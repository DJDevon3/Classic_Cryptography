# SPDX-FileCopyrightText: 2026 DJDevon3
# SPDX-License-Identifier: MIT
# Coded for Python 3.10.5
"""
ACA Quagmire III & IV Encrypt & Decrypt 2026-05-29
"""

import string
from pathlib import Path
STD = string.ascii_uppercase

"""
=========================================================
CONFIGURATION PARAMETERS
=========================================================
top keyworded alphabet is row keyword in mode 3
top keyword only used in mode 4
"""
cryptography_mode = "DECRYPT" # Valid modes: ENCRYPT or DECRYPT
QUAGMIRE_MODE = "3" # Valid modes: 3 or 4
row_keyword = "KRYPTOS"
vertical_keyword = "PALIMPSEST"
top_keyword = "ABC" # Only used with Quagmire 4
ciphertext_mode = "K1"

# For adding custom variations that can be switched to with ciphertext mode switch
# Either single or double spaced works
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

def tableau_to_string(
    mode,
    top_alphabet,
    top_keyword,
    row_alphabet,
    row_keyword,
    vertical_keyword,
    matrix,
    ciphertext,
    plaintext
):

    lines = []
    ciphertext_clean = clean_text(ciphertext)
    repeated_keyword = repeat_keyword(vertical_keyword,len(ciphertext_clean))

    # =====================================================
    # Quagmire III
    # =====================================================

    if mode == "3":
        lines.append("    Quagmire III Table")
        lines.append(f"    Keyworded Alphabet: {row_alphabet}")
        lines.append(f"    Vertical Keyword: {vertical_keyword}")
        lines.append("    -  " + " ".join(row_alphabet))

    # =====================================================
    # Quagmire IV
    # =====================================================

    elif mode == "4":
        lines.append("    Quagmire IV Table")
        lines.append(f"    Top Alphabet: {top_alphabet} ({top_keyword})")
        lines.append(f"    Row Alphabet: {row_alphabet} ({row_keyword})")
        lines.append(f"    Vertical Keyword: {vertical_keyword}")
        lines.append("    -  " + " ".join(top_alphabet))
    else:
        raise ValueError("INVALID QUAGMIRE MODE MUST BE 3 OR 4")

    # =====================================================
    # Matrix Rows
    # =====================================================

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

def save_output(filename, text):
    Path(filename).write_text(text,encoding="utf-8")

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
        
        # Build tableau row
        row = rotate_alphabet(row_alphabet,indicator_char)

        # Find plaintext letter position
        col = top_alphabet.index(pt_char)

        # Ciphertext from tableau row
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
    
# build matrix and decrypt
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
print(f"\n{tableau_output}\n")

# save to txt file
# Quagmire Results folder does not automatically create itself
first_ten = ciphertext[0:10]
output_filename = (f"Quagmire Results\{cryptography_mode}_Q{QUAGMIRE_MODE.replace(' ', '_')}_({row_keyword}-{vertical_keyword})_{first_ten}.txt")
save_output(output_filename,tableau_output)
print(f"Saved to:{output_filename}")