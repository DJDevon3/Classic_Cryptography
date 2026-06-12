import os
from collections import Counter

# Colski Keyword Length Finder Script
ciphertext_mode = "PK1"
alphabet_mode = "2"
key_length = 26
alphabet_length = 26

automate_frequency_order = False # True runs frequency test
frequency_order = "LIONHEARTS" # False use manual order

def get_ciphertext(ciphertext_mode):
    """
    Customizable ciphertext for manual quick switching
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
            "O B K R U O X O G H U L B S O L I F B B W F L R V Q Q P R N G K S S "
            "O T W T Q S J Q S S E K Z Z W A T J K L U D I A W I N F B N Y P V T "
            "T M Z F P K W G D K Z X T J C D I G K U H U A U E K C A R",

        "K4_REVERSE":
            "K R A C K E U A U H U K G I D C J T X Z K D G W K P F Z M T T V P Y N "
            "B F N I W A I D U L K J T A W Z Z K E S S Q J S Q T W T O S S K G "
            "N R P Q Q V R L F W B B F I L O S B L U H G O X O U R K B O",

        "K4_SNAKE_REVERSE":
            "V T T M Z F P K W G D K Z X T J C D I G K U H U A U E K C A R P Y N "
            "B F N I W A I D U L K J T A W Z Z K E S S Q J S Q T W T U O X O G "
            "H U L B S O L I F B B W F L R V Q Q P R N G K S S O R K B O",
            
        "K4_GROUP5":
            "O B K R U"
            "O X O G H"
            "U L B S O"
            "L I F B B"
            "W F L R V"
            "Q Q P R N"
            "G K S S O"
            "T W T Q S"
            "J Q S S E"
            "K Z Z W A"
            "T J K L U"
            "D I A W I"
            "N F B N Y"
            "P V T T M"
            "Z F P K W"
            "G D K Z X"
            "T J C D I"
            "G K U H U"
            "A U E K C"
            "A R",
            
        "PK1":
            "MQRALWVSJIMSXGJSVWQPHJMDINKXGIMHNKYUTXTTGJCYIABTJUMQEOFBITNBMONGVWETDLAIJPQYMZIKBQVRXZHUIJVDJLTQHIQYHEQKFTPTJYCONAFXYWQIBONAYXGWJFFIQMVXNVQYQFMWKFEJQYZFBWKXBKDQLJRELWGWDKHECRSFBKOVQJCPYDNKXYHE"
            
    }
    return ciphertexts.get(ciphertext_mode)

def custom_alphabet(num):
    """
    Customizable alphabets for manual quick switching
    """
    if (num == "1"):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if (num == "2"):
        alphabet = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
    if (num == "3"):
        alphabet = "ZXWVUQNMLJIHGFEDCBASOTPYRK"
    return alphabet

def output(text, file_handle=None):
    """
    Print to console and optionally save to file.
    """
    print(text)

    if file_handle:
        file_handle.write(str(text) + "\n")

def get_frequency_order(ciphertext, alphabet, top_n=10):
    counts = Counter(c for c in ciphertext if c in alphabet)
    return ''.join(letter for letter, count in counts.most_common(top_n))
    
# ===== MAIN =======        
alphabet = custom_alphabet(alphabet_mode)
ciphertext = get_ciphertext(ciphertext_mode)
if ciphertext is None:
    raise ValueError(f"Invalid ciphertext_mode --> {ciphertext_mode}")
 
if (automate_frequency_order):
    frequency_order = get_frequency_order(ciphertext,alphabet,15)
lion_order = [alphabet.index(k)for k in frequency_order]
ciphertext_order = [alphabet.index(k) for k in ciphertext if k in alphabet]
all_counts = {}
for x in range(1, key_length):
    all_counts[x] = [[ciphertext_order[i::x].count(j) for j in range(alphabet_length)]for i in range(x)]

output_dir = "Colski Keyword Length Finder Results"
os.makedirs(output_dir, exist_ok=True)
filename = os.path.join(output_dir,f"{ciphertext_mode}-{alphabet}.txt")

with open(filename, "w", encoding="utf-8") as f:
    output("=" * 45, f)
    output(f"Mode: {ciphertext_mode}", f)
    output(f"Alphabet: {alphabet}", f)
    output(f"Frequency Order: {frequency_order}", f)
    output(f"Ciphertext: {ciphertext}", f)
    output(f"Ciphertext Length = {len(ciphertext_order)}", f)
    output("Potential Keywords:", f)

    for x in range(1, key_length):
        K2_count = all_counts[x]
        key = ''.join(
            max((sum(K2_count[i][(k+j) % alphabet_length]for k in lion_order),alphabet[j])for j in range(alphabet_length))[1]
            for i in range(x)
        )
        output(f"{x:02}:{key}", f)
print(f"\nResults saved to: {filename}")
    
""" Prints all iterations from 1 to specified key_length   
01:S
02:SS
03:SSS
04:SSPA
05:ZSHSA
06:SSOSSS
07:OSSSSOS
08:BSCISSAA
09:SSSSSPSEN
10:PSHSAZSABS
11:OSSIZSASPPS
12:SWAASSSYUSPI
13:SZSDUCSDZSSSO
14:OSBSWNSEJVZSTA
15:OSSSSZEDSAZCHJA
16:BSIISSAAFSCNSSPA
17:ZHSSSSOJAXYSSZWOS
18:UAOEVSOYBASVSSGSPN
19:XPDASUSSPEVOOSOHSQS
20:YSCAWDSQUSPAHSAZTUBV
21:ASXSSGSODUZSSUUUDAATS
22:OSLNYWSYGSJAVSKZPASEPS
23:VSABIWXEEEACGSOSOSPESSB
"""
