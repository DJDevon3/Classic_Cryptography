# SPDX-FileCopyrightText: 2025 DJDevon3
# SPDX-License-Identifier: MIT
# Coded for Python 3.10.5
"""Progressive Caesar Matrix 2025-11-27"""

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
    
# -------------------------------------------------------------
# Pattern Checking (no highlighting)
# -------------------------------------------------------------
def check_pattern_both(text, pattern):
    """Return match flags and the original text (no highlighting)."""
    t = text.upper()
    p = pattern.upper().strip()

    if not p:
        return False, False, text

    forward = p in t
    reverse = p[::-1] in t

    return forward, reverse, text


def pattern_label(forward, reverse):
    if forward and reverse:
        return "   <-- MATCH (FWD & REV)"
    if forward:
        return "   <-- MATCH (FWD)"
    if reverse:
        return "   <-- MATCH (REV)"
    return ""

def write_line(f, text):
    f.write(text + "\n")
# -------------------------------------------------------------
# 1) Brute Caesar Matrix (fixed shift per row)
# -------------------------------------------------------------
def caesar_matrix(text, alphabet, keyword, pattern, collector):
    alphabet = alphabet.upper()
    text = text.upper()

    key_shifts = make_shifts_from_keyword(keyword, alphabet)
    key_len = len(key_shifts)
    L = len(alphabet)

    header = f"=== Brute Caesar Matrix (alphabet='{alphabet}', keyword='{keyword}') ==="
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

        forward, reverse, raw = check_pattern_both(result, pattern)
        label = pattern_label(forward, reverse)

        line = f"{raw}{label}"
        print(line)
        collector.append(line)


# -------------------------------------------------------------
# 2) Progressive Caesar Decode
# -------------------------------------------------------------
def progressive_caesar(text, alphabet, start_shift, keyword=""):
    """Progressive Caesar decode. Keyword optional: if empty, only numeric shifting occurs."""
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
def progressive_caesar_all_matrices(text, alphabet, keyword, pattern, iterations, collector):
    alphabet = alphabet.upper()
    text = text.upper()

    current_text = text  # initial input

    for iter_no in range(iterations):
        header1 = ""
        header2 = f"======================"
        header3 = f" PROGRESSIVE CAESAR MATRIX #{iter_no}"
        header4 = f"======================"

        for h in (header1, header2, header3, header4):
            print(h)
            collector.append(h)

        matrix_rows = []

        for start in range(len(alphabet)):
            decoded = progressive_caesar(current_text, alphabet, start, keyword)
            matrix_rows.append(decoded)

            forward, reverse, raw = check_pattern_both(decoded, pattern)
            label = pattern_label(forward, reverse)

            line = f"{raw}{label}"
            print(line)
            collector.append(line)

        # next iteration uses row 0 from this matrix
        current_text = matrix_rows[0]

# -------------------------------------------------------------
# Pure Progressive Caesar (no keyword)
# -------------------------------------------------------------
def pure_progressive_caesar(text, alphabet, start_shift):
    """Pure progressive Caesar: shift sequence = start, start-1, start-2, ..."""
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
def pure_progressive_caesar_all_matrices(text, alphabet, pattern, iterations, collector):
    alphabet = alphabet.upper()
    text = text.upper()

    current_text = text

    for iter_no in range(iterations):
        header1 = ""
        header2 = f"======================"
        header3 = f" PURE PROGRESSIVE MATRIX #{iter_no}"
        header4 = f"======================"

        for h in (header1, header2, header3, header4):
            print(h)
            collector.append(h)

        matrix_rows = []

        for start in range(len(alphabet)):
            decoded = pure_progressive_caesar(current_text, alphabet, start)
            matrix_rows.append(decoded)

            forward, reverse, raw = check_pattern_both(decoded, pattern)
            label = pattern_label(forward, reverse)

            line = f"{raw}{label}"
            print(line)
            collector.append(line)

        # next iteration uses row 0
        current_text = matrix_rows[0]

        
# -------------------------------------------------------------
# Configuration
# -------------------------------------------------------------
plaintext_mode = "K1"
alphabet = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
keyword = ""
pattern = ""
# To include keyword shift in progressive matrix set TRUE
progressive_keyword = False 

#alphabet = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#alphabet = "ZYXWVUTSRQPONMABCDEFGHIJKL"
#alphabet = "ABSCIDEFGHJKLMNOPQRTUVWXYZ"
#alphabet = "PALIMSETBCDFGHJKNOQRUVWXYZ"
#alphabet = "MAGNETICBDFHJKLOPQRSUVWXYZ"
#alphabet = "ANTIPODESBCFGHJKLMQRUVWXYZ"
#alphabet = "ARTICHOKEBDFGJLMNPQSUVWXYZ"
#alphabet = "HYDRAULICBEFGJKMNOPQSTVWXZ"
#alphabet = "HYDRABCEFGIJKLMNOPQSTUVWXZ"
#alphabet = "CENTRALIGYBDFHJKMOPQSUVWXZ"
#alphabet = "JIMSANBORCDEFGHKLPQTUVWXYZ"
#alphabet = "BDFHJLNPRTVXZACEGIKMOQSUWY"

# - Attempted Reverse Engineer Plaintext Alphabets 
#alphabet = "FELARSVTQNPUBCDGHIJKMOYZWX"
#alphabet = "JKFELARSVTQNOPWBCDGHIMUXYZ"
#alphabet = "QPORTNHGEKASBCDFIJLMUVWXYZ"
#alphabet = "NBYEPRVLTIMCZFOADGHJKQSUWX"
#alphabet = "TIMNZCFLPOWKYBVRADEGHJQSUX"

# ========= HARDCODED MODES ============
#------K4
if (plaintext_mode == "K4"):
    plaintext_F = "O B K R U O X O G H U L B S O L I F B B W F L R V Q Q P R N G K S S O T W T Q S J Q S S E K Z Z W A T J K L U D I A W I N F B N Y P V T T M Z F P K W G D K Z X T J C D I G K U H U A U E K C A R"
#------K4 PLAINTEXT CRIB WORDS
if (plaintext_mode == "K4_CRIB"):
    plaintext_F = "X X X X X X X X X X X X X X X X X X X X X E A S T N O R T H E A S T X X X X X X X X X X X X X X X X X X X X X X X X X X X X X B E R L I N C L O C K X X X X X X X X X X X X X X X X X X X X X X X"
#------K4 PLAINTEXT X'S
if (plaintext_mode == "K4_X"):
    plaintext_F = "X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X"
#------K4 Snake Route Transposition
if (plaintext_mode == "K4_SNAKE"):
    plaintext_F = "R O B K R O S S K G N R P Q Q V R L F W B B F I L O S B L U H G O X O U T W T Q S J Q S S E K Z Z W A T J K L U D I A W I N F B N Y P R A C K E U A U H U K G I D C J T X Z K D G W K P F Z M T T V"
#------K1 Keyword: PALIMPSEST
if (plaintext_mode == "K1"):
    plaintext_F = "EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD" 
    alphabet = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
    keyword = "PALIMPSEST"
#------K2 Keyword: ABSCISSA
if (plaintext_mode == "K2"): 
    plaintext_F = "VFPJUDEEHZWETZYVGWHKKQETGFQJNCEGGWHKKDQMCPFQZDQMMIAGPFXHQRLGTIMVMZJANQLVKQEDAGDVFRPJUNGEUNAQZGZLECGYUXUEENJTBJLBQCRTBJDFHRRYIZETKZEMVDUFKSJHKFWHKUWQLSZFTIHHDDDUVHDWKBFUFPWNTDFIYCUQZEREEVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDXFLGGTEZFKZBSFDQVGOGIPUFXHHDRKFFHQNTGPUAECNUVPDJMQCLQUMUNEDFQELZZVRRGKFFVOEEXBDMVPNFQXEZLGREDNQFMPNZGLFLPMRJQYALMGNUVPDXVKPDQUMEBEDMHDAFMJGZNUPLGEWJLLAETG"
    alphabet = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
    keyword = "ABSCISSA"

#------Reverse of all forward plaintext
plaintext_R = plaintext_F[::-1]

# Collector list for file output
strip_spaces_FS = plaintext_F.replace(" ", "")
plaintext_FS = " ".join(strip_spaces_FS)
strip_spaces_RS = plaintext_R.replace(" ", "")
plaintext_RS = " ".join(strip_spaces_RS)
output_lines_F = []
output_lines_R = []

# Run 2 modes Forwards
caesar_matrix(plaintext_FS, alphabet, keyword, pattern, output_lines_F)
caesar_matrix(plaintext_RS, alphabet, keyword, pattern, output_lines_R)
if progressive_keyword:
    progressive_caesar_all_matrices(plaintext_FS, alphabet, keyword, pattern, iterations=26, collector=output_lines_F)
    progressive_caesar_all_matrices(plaintext_RS, alphabet, keyword, pattern, iterations=26, collector=output_lines_R)
else:
    # Run pure progressive
    brute_row_zero_F = output_lines_F[1].strip()  # adjust if needed
    pure_progressive_caesar_all_matrices(brute_row_zero_F,alphabet,pattern,iterations=26,collector=output_lines_F)
    brute_row_zero_R = output_lines_R[1].strip()
    pure_progressive_caesar_all_matrices(brute_row_zero_R,alphabet,pattern,iterations=26,collector=output_lines_R)

# Save Alphabet & Key
safe_alpha = make_safe_filename(alphabet)
safe_key = make_safe_filename(keyword) if keyword else "NONE"

# FORWARD Strip Spaces and Truncate
strip_spaces = plaintext_F.replace(" ", "")
first_five = strip_spaces[0:5]

# Save FORWARD Results
if (plaintext_mode == "K4"):
    filename = f"Results\K4-{first_five}-{safe_alpha}-{safe_key}.txt"
if (plaintext_mode == "K4_CRIB"):
    filename = f"Results\K4_CRIB-{first_five}-{safe_alpha}-{safe_key}.txt"
if (plaintext_mode == "K4_X"):
    filename = f"Results\K4_X-{first_five}-{safe_alpha}-{safe_key}.txt"
if (plaintext_mode == "K4_CRIB"):
    filename = f"Results\K4_CRIB-{first_five}-{safe_alpha}-{safe_key}.txt"
if (plaintext_mode == "K4_SNAKE"):
    filename = f"Results\K4_SNAKE-{first_five}-{safe_alpha}-{safe_key}.txt"
if (plaintext_mode == "K1"):
    filename = f"Results\K1-{first_five}-{safe_alpha}-{safe_key}.txt"
if (plaintext_mode == "K2"):
    filename = f"Results\K2-{first_five}-{safe_alpha}-{safe_key}.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"Alphabet: {alphabet}\n")
    f.write(f"Keyword:  {keyword}\n")
    f.write(f"Plaintext:  {plaintext_F}\n")
    f.write(f"Search For:  {pattern}\n")
    f.write("============ FORWARD =================================\n\n")
    f.write("\n".join(output_lines_F))
    f.write(f"\n\n")
    f.write("============ REVERSE =================================\n\n")
    f.write(f"Alphabet: {alphabet}\n")
    f.write(f"Keyword:  {keyword}\n")
    f.write(f"Plaintext:  {plaintext_R}\n")
    f.write(f"Search For:  {pattern}\n")
    f.write("---------------------------------------------\n\n")
    f.write("\n".join(output_lines_R))

print(f"\n\nResults saved to: {filename}")
