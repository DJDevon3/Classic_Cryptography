# SPDX-FileCopyrightText: 2026 DJDevon3
# SPDX-License-Identifier: MIT
# Coded for Python 3.10.5
"""Progressive Caesar Matrix 2026-06-01"""

import os

# -------------------------------------------------------------
# Configuration
# To shift in chunks use a keyword like AAAAABBBBCCCC
# -------------------------------------------------------------
ciphertext_mode = "K4"
alphabet_mode = "3"
keyword = "AAABBBCCCDDD"

# This is an additional optional multiplicative progressive process
# This method is much harder to understand or follow by eye
# Recommend keeping this set to False
multiplicative_process = False 

def get_ciphertext(ciphertext_mode):
    """
    Customizable ciphertext mode for manual quick switching
    Can be single or double spaced, lower or upper case.
    """
    ciphertexts = {
        # BEAUFORT:JUDGEYENOTLEASTYEBEJUDGED:KRYPTOSABCDEFGHIJLMNQUVWXZ:EXAMPLEOFABEAUFORTCIPHERINLENGTHFORREVERSEKEYWORDSEARCHESOFANUNKNOWNLENGTHTOAPPROXIMATEFINDINGKEYSANDCLUESANDINABOXOFSALTROCKSMAYBEGYPSUMORCALCITEORMAYBENOT 
        "CUSTOM":
            "QNPNXXYSMWSKPKSPDWNJMZKPJXNKBYCWMZGDZZAAOJYQNJSPUEZTKSZKXZYTLKZBMVOFTYMLRPSSQFDDZSZNPLAVVBMJYKENPEPMLSVJNXAMKSZRPVTKCATGRJOYRCUTYVPXBMFGNVRVHVYIRSODCBEPNECA",

        "K1":
            "EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD",

        "K2":
            "VFPJUDEEHZWETZYVGWHKKQETGFQJNCEGGWHKKDQMCPFQZDQMMIAGPFXHQRLGTIMVMZJANQLVKQEDAGDVFRPJUNGEUNAQZGZLECGYUXUEENJTBJLBQCRTBJDFHRRYIZETKZEMVDUFKSJHKFWHKUWQLSZFTIHHDDDUVHDWKBFUFPWNTDFIYCUQZEREEVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDXFLGGTEZFKZBSFDQVGOGIPUFXHHDRKFFHQNTGPUAECNUVPDJMQCLQUMUNEDFQELZZVRRGKFFVOEEXBDMVPNFQXEZLGREDNQFMPNZGLFLPMRJQYALMGNUVPDXVKPDQUMEBEDMHDAFMJGZNUPLGEWJLLAETG",

        "K4":
            "O B K R U O X O G H U L B S O L I F B B W F L R V Q Q P R N G K S S O T W T Q S J Q S S E K Z Z W A T J K L U D I A W I N F B N Y P V T T M Z F P K W G D K Z X T J C D I G K U H U A U E K C A R",

        "K4_REVERSE":
            "R A C K E U A U H U K G I D C J T X Z K D G W K P F Z M T T V P Y N B F N I W A I D U L K J T A W Z Z K E S S Q J S Q T W T O S S K G N R P Q Q V R L F W B B F I L O S B L U H G O X O U R K B O",

        "K4_SNAKE_REVERSE":
            "V T T M Z F P K W G D K Z X T J C D I G K U H U A U E K C A R P Y N B F N I W A I D U L K J T A W Z Z K E S S Q J S Q T W T U O X O G H U L B S O L I F B B W F L R V Q Q P R N G K S S O R K B O"
            
    }
    return ciphertexts.get(ciphertext_mode)

def custom_alphabet(num):
    """
    Customizable alphabets for manual quick switching
    """
    if (num == "1"):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if (num == "2"):
        alphabet = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    if (num == "3"):
        alphabet = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
    if (num == "4"):
        alphabet = "ZXWVUQNMLJIHGFEDCBASOTPYRK"
    if (num == "5"):
        alphabet = "ABSCIDEFGHJKLMNOPQRTUVWXYZ"
    if (num == "6"):
        alphabet = "PALIMSETBCDFGHJKNOQRUVWXYZ"
    if (num == "7"):
        alphabet = "MEDUSABCFGHIJKLNOPQRTVWXYZ"
    if (num == "8"):
        alphabet = "MAGNETICBDFHJKLOPQRSUVWXYZ"
    if (num == "9"):
        alphabet = "ANTIPODESBCFGHJKLMQRUVWXYZ"
    if (num == "10"):
        alphabet = "ARTICHOKEBDFGJLMNPQSUVWXYZ"
    if (num == "11"):
        alphabet = "HYDRABCEFGIJKLMNOPQSTUVWXZ"
    if (num == "12"):
        alphabet = "HYDRAULICSBEFGJKMNOPQTVWXZ"
    if (num == "13"):
        alphabet = "CENTRALIGYBDFHJKMOPQSUVWXZ"
    if (num == "14"):
        alphabet = "JIMSANBORCDEFGHKLPQTUVWXYZ"
    if (num == "15"):
        alphabet = "PYTHONABCDEFGIJKLMQRSUVWXZ"
    if (num == "16"):
        alphabet = "BDFHJLNPRTVXZACEGIKMOQSUWY" # split in half, equadistant split.
    if (num == "17"):
        alphabet = "ZXVTRPNLJHFDBACEGIKMOQSUWY" # split in half, equadistant from middle. 
        
    # - Attempted Reverse Engineer Plaintext Alphabets 
    if (num == "18"):
        alphabet = "FELARSVTQNPUBCDGHIJKMOYZWX"
    if (num == "19"):
        alphabet = "JKFELARSVTQNOPWBCDGHIMUXYZ"
    if (num == "20"):
        alphabet = "QPORTNHGEKASBCDFIJLMUVWXYZ"
    if (num == "21"):
        alphabet = "NBYEPRVLTIMCZFOADGHJKQSUWX"
    if (num == "22"):
        alphabet = "TIMNZCFLPOWKYBVRADEGHJQSUX"
    return alphabet

# ======== MORSE CODE ================
"""
E E V I R T U A L L Y E
E E E E E E I N V I S I B L E 
D I G E T A L E E E 
I N T E R P R E T A T I T
E E S H A D O W E E 
F O R C E S E E E E 
E L U C I D E E E 
M E M O R Y E 
T I S Y O U R 
P O S I T I O N E
S O S
R Q
"""

# -------------------------------------------------------------
# 1) Utility Functions
# -------------------------------------------------------------
def make_safe_filename(s):
    """Remove characters not allowed in Windows filenames."""
    unsafe = '<>:"/\\|?*'
    for ch in unsafe:
        s = s.replace(ch, "")
    return s

def make_shifts_from_keyword(keyword, alphabet):
    """Convert keyword into a list of numeric shifts based on the custom alphabet."""
    shifts = []
    for c in keyword.upper():
        if c in alphabet:
            shifts.append(alphabet.index(c))
    return shifts if shifts else [0]   # fallback to shift 0 if keyword invalid

def write_line(f, text):
    f.write(text + "\n")
    
# -------------------------------------------------------------
# Brute Caesar Matrix (fixed shift per row)
# -------------------------------------------------------------
def caesar_matrix(text, alphabet, keyword, collector):
    alphabet = alphabet.upper()
    text = text.upper()
    key_shifts = make_shifts_from_keyword(keyword, alphabet)
    key_len = len(key_shifts)
    L = len(alphabet)
    header = f"====================== Brute Caesar Matrix (Alphabet:{alphabet} Keyword:{keyword}) ======================"
    print(header)
    collector.append(header)

    for shift in range(L):
        result = ""
        key_i = 0

        for char in text:
            if char in alphabet:
                base_index = alphabet.index(char)
                total_shift = shift + key_shifts[key_i % key_len]
                decoded = alphabet[(base_index - total_shift) % L]
                result += decoded
                key_i += 1
            else:
                result += char

        line = f"{result}"
        print(line)
        collector.append(line)

# -------------------------------------------------------------
# Progressive Caesar Base Decoder
# -------------------------------------------------------------
def progressive_caesar(text, alphabet, start_shift, keyword=""):
    """
    Progressive Caesar decode. Keyword optional: if empty, only numeric shifting occurs.
    """
    alphabet = alphabet.upper()
    text = text.upper()

    key_shifts = make_shifts_from_keyword(keyword, alphabet)
    key_len = len(key_shifts)
    L = len(alphabet)

    result = ""
    progressive_shift = start_shift
    i = 0

    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)
            total_shift = progressive_shift + key_shifts[i % key_len]
            decoded = alphabet[(idx - total_shift) % L]
            result += decoded

            progressive_shift += 1
            i += 1
        else:
            result += char
    return result

# -------------------------------------------------------------
# 3) Progressive Caesar – Full 26 matrices
# -------------------------------------------------------------
def progressive_caesar_all_matrices(text, alphabet, keyword, iterations, collector):
    alphabet = alphabet.upper()
    text = text.upper()
    current_text = text

    for iter_no in range(iterations):
        header1 = ""
        header2 = f"======================"
        header3 = f" PROGRESSIVE CAESAR MATRIX #{iter_no} (Alphabet:{alphabet} Keyword:{keyword})"
        header4 = f"======================"

        for h in (header1, header2, header3, header4):
            print(h)
            collector.append(h)

        matrix_rows = []

        for start in range(len(alphabet)):
            decoded = progressive_caesar(current_text, alphabet, start, keyword)
            matrix_rows.append(decoded)

            line = f"{matrix_rows}"
            print(line)
            collector.append(line)

        # next iteration uses row 0 from this matrix
        current_text = matrix_rows[0]

# -------------------------------------------------------------
# Pure Progressive Caesar (no keyword)
# -------------------------------------------------------------
def pure_progressive_caesar(text, alphabet, start_shift):
    """
    Pure progressive Caesar: shift sequence = start, start-1, start-2, ...
    """
    alphabet = alphabet.upper()
    text = text.upper()

    L = len(alphabet)
    result = ""

    progressive_shift = start_shift  # first shift
    decrement = 0                    # how much to subtract each step

    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)
            total_shift = progressive_shift - decrement
            decoded = alphabet[(idx - total_shift) % L]
            result += decoded
            decrement += 1
        else:
            result += char

    return result

# -------------------------------------------------------------
# Build matrices using pure progressive (no keyword)
# -------------------------------------------------------------
def pure_progressive_caesar_all_matrices(plaintext, text, alphabet, iterations, collector):
    alphabet = alphabet.upper()
    text = text.upper()

    current_text = text

    for iter_no in range(iterations):
        header1 = ""
        header2 = f"======================"
        header3 = f" PURE PROGRESSIVE MATRIX #{iter_no} (Alphabet:{alphabet} Keyword:{keyword})"
        header4 = f"======================"
        header5 = f"{plaintext}\n"
        
        for h in (header1, header2, header3, header4, header5):
            print(h)
            collector.append(h)

        matrix_rows = []

        for start in range(len(alphabet)):
            decoded = pure_progressive_caesar(current_text, alphabet, start)
            matrix_rows.append(decoded)
            line = f"{decoded}"
            print(line)
            collector.append(line)

        # next iteration uses row 0
        current_text = matrix_rows[0]

def output(text, file_handle=None):
    """
    Print to console and optionally save to file.
    """
    print(text)

    if file_handle:
        file_handle.write(str(text) + "\n")
        
# ========= Alphabet & Ciphertext Mode Switch ============
alphabet = custom_alphabet(alphabet_mode)
ciphertext = get_ciphertext(ciphertext_mode)
ciphertext_R = ciphertext[::-1] # Reverse

# Collector list for file output
strip_spaces_FS = ciphertext.replace(" ", "")
plaintext_FS = " ".join(strip_spaces_FS)
strip_spaces_RS = ciphertext_R.replace(" ", "")
plaintext_RS = " ".join(strip_spaces_RS)
output_lines_F = []
output_lines_R = []

# ========= Run Caesar Run ============ 
caesar_matrix(plaintext_FS, alphabet, keyword, output_lines_F)
caesar_matrix(plaintext_RS, alphabet, keyword, output_lines_R)

if multiplicative_process:
    # Run Multiplicative Progressive Caesar
    progressive_caesar_all_matrices(plaintext_FS, alphabet, keyword, iterations=26, collector=output_lines_F)
    progressive_caesar_all_matrices(plaintext_RS, alphabet, keyword, iterations=26, collector=output_lines_R)
else:
    # Run Pure Progressive Caesar
    brute_row_zero_F = output_lines_F[1].strip()
    pure_progressive_caesar_all_matrices(plaintext_FS, brute_row_zero_F,alphabet,iterations=26,collector=output_lines_F)
    brute_row_zero_R = output_lines_R[1].strip()
    pure_progressive_caesar_all_matrices(plaintext_RS, brute_row_zero_R,alphabet,iterations=26,collector=output_lines_R)

# ========= Save Results to file ============ 
safe_alpha = make_safe_filename(alphabet)
safe_key = make_safe_filename(keyword) if keyword else "NONE"
strip_spaces = ciphertext.replace(" ", "")
first_five = strip_spaces[0:5]

output_dir = "Progressive Caesar Results"
os.makedirs(output_dir, exist_ok=True)
filename = os.path.join(output_dir,f"{ciphertext_mode}-{first_five}-{safe_alpha}-{safe_key}.txt")

with open(filename, "w", encoding="utf-8") as f:
    output(f"Mode: {ciphertext_mode}", f)
    output(f"Alphabet: {alphabet}", f)
    output(f"Keyword:  {keyword}", f)
    output(f"Ciphertext: \n{ciphertext}", f)
    output("\n".join(output_lines_F), f)
    output(f"\n\n", f)
    output("============ REVERSED =================================", f)
    output(f"Mode: {ciphertext_mode}", f)
    output(f"Alphabet: {alphabet}", f)
    output(f"Keyword:  {keyword}", f)
    output(f"Ciphertext: \n{ciphertext_R}", f)
    output("\n".join(output_lines_R), f)

print(f"\nResults saved to: {filename}")
