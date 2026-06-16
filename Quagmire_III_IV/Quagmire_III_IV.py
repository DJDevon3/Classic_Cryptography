# SPDX-FileCopyrightText: 2026 DJDevon3
# SPDX-License-Identifier: MIT
# Coded for Python 3.10.5
"""
ACA Quagmire II, III & IV Encrypt & Decrypt 2026-06-16
"""

import os
import string
import math
from pathlib import Path
from collections import Counter
STD = string.ascii_uppercase

"""
=========================================================
CONFIGURATION PARAMETERS
top keyworded alphabet = row keyword in mode 3
top keyword only unique in mode 4
"""
QUAGMIRE_MODE = "3" # Valid modes: 3 or 4
cryptography_mode = "DECRYPT" # Valid modes: ENCRYPT or DECRYPT

ciphertext_mode = "Quagmire_III_Decrypt_Demo"
row_keyword = "KRYPTOS" # Alphabet generated from keyword
vertical_keyword = "ABSCISSA" # Repeated vigenere style keyword

# Hard coded lower in script as ABC for QUAGMIRE_MODE 2 
# Top Keyword only ever customizable with QUAGMIRE_MODE 4
top_keyword = "CUSTOMKEYWORD"

# Check for enough character counts in K4 result
enable_minimum_K4_characters = False
minimum_characters="EASTNORTHEASTBERLINCLOCK"

# Optional Additional Scytale Post-Processing
enable_scytale = False
scytale_rod_sizes = list(range(1, 15))

# Optional Additional Skip Transposition Post-Processing
enable_skip = False
skip_sizes = list(range(1, 25))
#=========================================================

if (ciphertext_mode == "CUSTOM"):
    ciphertext = "UNZLSELLXVHVIFYHBJHVWCIWXRZXYXUFYJPQVIUUUSLTWWZLWQITW"
if (ciphertext_mode == "K1"):
    # Use row_keyword: KRYPTOS & vertical_keyword: PALIMPSEST
    ciphertext = "EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD"
if (ciphertext_mode == "K2"):
    # Use row_keyword: KRYPTOS & vertical_keyword: ABSCISSA
    ciphertext = "VFPJUDEEHZWETZYVGWHKKQETGFQJNCEGGWHKKDQMCPFQZDQMMIAGPFXHQRLGTIMVMZJANQLVKQEDAGDVFRPJUNGEUNAQZGZLECGYUXUEENJTBJLBQCRTBJDFHRRYIZETKZEMVDUFKSJHKFWHKUWQLSZFTIHHDDDUVHDWKBFUFPWNTDFIYCUQZEREEVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDXFLGGTEZFKZBSFDQVGOGIPUFXHHDRKFFHQNTGPUAECNUVPDJMQCLQUMUNEDFQELZZVRRGKFFVOEEXBDMVPNFQXEZLGREDNQFMPNZGLFLPMRJQYALMGNUVPDXVKPDQUMEBEDMHDAFMJGZNUPLGEWJLLAETG"
if (ciphertext_mode == "K3"):
    ciphertext = "ENDYAHROHNLSRHEOCPTEOIBIDYSHNAIACHTNREYULDSLLSLLNOHSNOSMRWXMNETPRNGATIHNRARPESLNNELEBLPIIACAEWMTWNDITEENRAHCTENEUDRETNHAEOETFOLSEDTIWENHAEIOYTEYQHEENCTAYCREIFTBRSPAMHHEWENATAMATEGYEERLBTEEFOASFIOTUETUAEOTOARMAEERTNRTIBSEDDNIAAHTTMSTEWPIEROAGRIEWFEBAECTDDHILCEIHSITEGOEAOSDDRYDLORITRKLMLEHAGTDHARDPNEOHMGFMFEUHEECDMRIPFEIMEHNLSSTTRTVDOHW"
if (ciphertext_mode == "K4"):
    ciphertext = "OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR"
if (ciphertext_mode == "K4_REVERSE"):
    ciphertext = "RACKEUAUHUKGIDCJTXZKDGWKPFZMTTVPYNBFNIWAIDULKJTAWZZKESSQJSQTWTOSSKGNRPQQVRLFWBBFILOSBLUHGOXOURKBO"
if (ciphertext_mode == "K4_SNAKE"):
    ciphertext = "O B K R O S S K G N R P Q Q V R L F W B B F I L O S B L U H G O X O U T W T Q S J Q S S E K Z Z W A T J K L U D I A W I N F B N Y P R A C K E U A U H U K G I D C J T X Z K D G W K P F Z M T T V"
if (ciphertext_mode == "K4_SNAKE_REVERSE"):
    ciphertext = "V T T M Z F P K W G D K Z X T J C D I G K U H U A U E K C A R P Y N B F N I W A I D U L K J T A W Z Z K E S S Q J S Q T W T U O X O G H U L B S O L I F B B W F L R V Q Q P R N G K S S O R K B O"
if (ciphertext_mode == "K4_CRIB"):
    ciphertext = "x x x x x x x x x x x x x x x x x x x x x E A S T N O R T H E A S T x x x x x x x x x x x x x x x x x x x x x x x x x x x x x B E R L I N C L O C K x x x x x x x x x x x x x x x x x x x x x x x"
if (ciphertext_mode == "PK1"):
    # Use row_keyword: KRYPTOS & vertical_keyword: PROVENANCE
    ciphertext = "MQRALWVSJIMSXGJSVWQPHJMDINKXGIMHNKYUTXTTGJCYIABTJUMQEOFBITNBMONGVWETDLAIJPQYMZIKBQVRXZHUIJVDJLTQHIQYHEQKFTPTJYCONAFXYWQIBONAYXGWJFFIQMVXNVQYQFMWKFEJQYZFBWKXBKDQLJRELWGWDKHECRSFBKOVQJCPYDNKXYHE"
if (ciphertext_mode == "PK3"):
    ciphertext = "HWZTRPPVHZLHRBQBQOMZBACNOTHLYGBATBTKHERQHRVZWWXCTZLRRVZCROHCIOTBVJKCALNKFJHEIMKUHJPFNVBCGQYNZMOHGBUTDPTJTDSUBOLYPLSKIEMANXMFNDBCTNRTLLVQOXUBPAXQUVDNXUMCIFOGETZWHJDIWDBWQFXAOMWBBCQXYZFZBTRIQMYOFFMVWSFLPTHFFQUINGLAMSQJOPUESPIQGZZCTJVRLQMIIRROOGBWNPQMXFQDVFTCVGNRIXQKUYYKBRTWPCDHLAWC"
    
# ======= Demonstration Modes below override configuration parameters =======
# Decryption Demonstrations
if (ciphertext_mode == "Quagmire_II_Decrypt_Demo"): # Quagmire II Decrypt Demo
    QUAGMIRE_MODE = "2"
    row_keyword = "SPRINGFEVER"
    vertical_keyword = "FLOWER"
    ciphertext = "JICIC OSLYK ILFVC HEBDX CCORJ IOEWA FMWKK TXBGW HRJIB KEDBJ WZABU XWHEH UXOXC U"
if (ciphertext_mode == "Quagmire_III_Decrypt_Demo"): # Quagmire III Decrypt Demo
    QUAGMIRE_MODE = "3"
    row_keyword = "AUTOMOBILE"
    vertical_keyword = "HIGHWAY"
    ciphertext = "KRSLW MITJD VIABM RGQMT MLLIV IFUIX RHTNY ONVRH HIIIR MCAOV EI"
if (ciphertext_mode == "Quagmire_IV_Decrypt_Demo"): # Quagmire IV Decrypt Demo
    ciphertext = "VBMRF CYISP MPBRR HEICX RREIG DX"
    cryptography_mode = "DECRYPT"
    QUAGMIRE_MODE = "4"
    row_keyword = "PERCEPTION"
    vertical_keyword = "EXTRA"
    top_keyword = "SENSORY"
    
# Encryption Demonstrations
if (ciphertext_mode == "K1_Encrypt_Encrypt_Demo"): # Kryptos K1 Encrypt Demo
    cryptography_mode = "ENCRYPT"
    QUAGMIRE_MODE = "3"
    row_keyword = "KRYPTOS"
    vertical_keyword = "PALIMPSEST"
    ciphertext = "BETWEENSUBTLESHADINGANDTHEABSENCEOFLIGHTLIESTHENUANCEOFIQLUSION"
if (ciphertext_mode == "K2_Encrypt_Encrypt_Demo"): # Kryptos K2 Encrypt Demo
    cryptography_mode = "ENCRYPT"
    QUAGMIRE_MODE = "3"
    row_keyword = "KRYPTOS"
    vertical_keyword = "ABSCISSA"
    ciphertext = "ITWASTOTALLYINVISIBLEHOWSTHATPOSSIBLETHEYUSEDTHEEARTHSMAGNETICFIELDXTHEINFORMATIONWASGATHEREDANDTRANSMITTEDUNDERGRUUNDTOANUNKNOWNLOCATIONXDOESLANGLEYKNOWABOUTTHISTHEYSHOULDITSBURIEDOUTTHERESOMEWHEREXWHOKNOWSTHEEXACTLOCATIONONLYWWTHISWASHISLASTMESSAGEXTHIRTYEIGHTDEGREESFIFTYSEVENMINUTESSIXPOINTFIVESECONDSNORTHSEVENTYSEVENDEGREESEIGHTMINUTESFORTYFOURSECONDSWESTIDBYROWS"
# =======Demonstration Modes above override configuration parameters =======

# =========================================================
# Utility Functions
# =========================================================
def clean_text(text):
    return ''.join(c for c in text.upper()if c in STD)

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
    Print to console and save to file
    """
    print(text)
    if file_handle:
        file_handle.write(str(text) + "\n")

def phrase_deficit(text, phrase=minimum_characters):
    """
    Checks if enough characters are present in ciphertext
    """
    text_counts = Counter(text.upper())
    phrase_counts = Counter(phrase.upper())
    missing = {}
    for letter, needed in phrase_counts.items():
        have = text_counts.get(letter, 0)
        if have < needed:
            missing[letter] = needed - have

    return missing


def build_tableau(row_alphabet, vertical_keyword):
    """ Build Tableau Output """
    vertical_alpha = keyed_alphabet(vertical_keyword)
    matrix = []
    for ch in vertical_alpha:
        row = rotate_alphabet(row_alphabet,ch)
        matrix.append(row)
    return matrix


def tableau_to_string(mode, top_alphabet, top_keyword, row_alphabet, row_keyword, vertical_keyword, matrix, ciphertext, plaintext):
    """ Different modes require different formatting """
    lines = []
    ciphertext_clean = clean_text(ciphertext)
    repeated_keyword = repeat_keyword(vertical_keyword,len(ciphertext_clean))
    
    # Quagmire III
    if mode == "2":
        top_keyword = "ABC"
        lines.append("    Quagmire II Table")
        lines.append("    -  " + " ".join(top_alphabet))
        
    elif mode == "3":
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
        
        # Check for minimum crib character count
        if enable_minimum_K4_characters:
            missing = phrase_deficit(plaintext)
            if missing:
                lines.append(f"\nPlaintext (Decrypted) Minimum Characters: Fail ({minimum_characters}) {missing}")
            else:
                lines.append(f"\nPlaintext (Decrypted) Minimum Characters: Pass ({minimum_characters})")
        else:
                lines.append(f"\nPlaintext (Decrypted):")
            
        lines.append(double_space(plaintext))
    if (cryptography_mode == "ENCRYPT"):
        lines.append("\nPlaintext")
        lines.append(double_space(ciphertext_clean))
        lines.append("\nCiphertext (Encrypted)")
        lines.append(double_space(plaintext))
    return "\n".join(lines)


def decrypt_quagmire(ciphertext,top_alphabet,row_alphabet,vertical_keyword):
    """ Quagmire Decryption Function"""
    ciphertext = clean_text(ciphertext)
    vertical_keyword = clean_text(vertical_keyword)
    plaintext = []
    repeated_keyword = repeat_keyword(vertical_keyword,len(ciphertext))
    for i, ct_char in enumerate(ciphertext):
        indicator_char = repeated_keyword[i]
        row = rotate_alphabet(row_alphabet,indicator_char)
        col = row.index(ct_char)
        pt_char = top_alphabet[col]
        plaintext.append(pt_char)
    return ''.join(plaintext)
    
def encrypt_quagmire(plaintext,top_alphabet,row_alphabet,vertical_keyword):
    """ Quagmire Encryption Function"""
    plaintext = clean_text(plaintext)
    vertical_keyword = clean_text(vertical_keyword)
    ciphertext = []
    repeated_keyword = repeat_keyword(vertical_keyword,len(plaintext))
    for i, pt_char in enumerate(plaintext):
        indicator_char = repeated_keyword[i]
        row = rotate_alphabet(row_alphabet,indicator_char)
        col = top_alphabet.index(pt_char)
        ct_char = row[col]
        ciphertext.append(ct_char)
    return ''.join(ciphertext)
    
# Quagmire II, III, or IV Mode switch globals
if QUAGMIRE_MODE == "2":
    row_alphabet = keyed_alphabet(row_keyword)
    top_alphabet = keyed_alphabet("ABC")
    vertical_alphabet = keyed_alphabet(vertical_keyword)
elif QUAGMIRE_MODE == "3":
    row_alphabet = keyed_alphabet(row_keyword)
    top_alphabet = row_alphabet
    vertical_alphabet = keyed_alphabet(vertical_keyword)
elif QUAGMIRE_MODE == "4":
    top_alphabet = keyed_alphabet(top_keyword)
    row_alphabet = keyed_alphabet(row_keyword)
    vertical_alphabet = keyed_alphabet(vertical_keyword)
else:
    raise ValueError("INVALID QUAGMIRE MODE MUST BE 2, 3, OR 4")

# ==========================================
# SCYTALE FUNCTIONS
# ==========================================
def scytale_decrypt(text, rod_size):
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
        lines.append(f"\nSkip:{skip:02}\n{spaced}")
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

# Text file output formatting
first_ten = ciphertext[0:10]
output_dir = "Quagmire III IV Results"
os.makedirs(output_dir, exist_ok=True)
filename = os.path.join(output_dir,f"{cryptography_mode}_Q{QUAGMIRE_MODE.replace(' ', '_')}_({row_keyword}-{vertical_keyword})_{first_ten}.txt")

# Open text file and append method headers & results to file
with open(filename, "w", encoding="utf-8") as f:
    output("=" * 45, f)
    output(f"Method: {cryptography_mode}", f)
    output(f"Quagmire Mode: {QUAGMIRE_MODE.replace(' ', '_')}", f)
    output(f"Top Alphabet: {top_alphabet}", f)
    output(f"Row Keyword: {row_keyword}", f)
    output(f"Row Alphabet: {row_alphabet}", f)
    output(f"Vertical Keyword: {vertical_keyword}", f)
    output(f"Vertical Alphabet: {vertical_alphabet}", f)
    output(f"Ciphertext Mode Name: {ciphertext_mode}", f)
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
