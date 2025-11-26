# Progressive Caesar Matrix Encrypt/Decrypt:
- This is a pure python program designed to be run on a PC.

To run the program simply point Windows CMD prompt at the script and run with python:
```py
C:\Users\Devon\Documents\Kryptos Scripts>python Progressive_Caesar_Matrix.py
```
It will create text files in a folder named Results. It does not create the folder for you. Either create the folder or change the file save location at the bottom of the script. 

```py
C:\Users\Devon\Documents\Kryptos Scripts\Results
```
It will generate 2 files. Each file is your plaintext in both forward and reverse. 
The first matrix is a normal Brute Force Caesar matrix from which all 26 possible progressive Caesar matrices are created.
If you use a keyword it will translate it to a numerical offset and offset the results. This is how Kryptos K1 & K2 are solved. Examples of K1 and K2 are included (hard coded). 

What is a progressive Caesar? 
- It reads each consecutive previous matrix diagonally and produces the results horizontally. It iterates through 26 times, once for each letter of the English alphabet. No more trying to read matrices diagonally is needed. The script makes all 26 possible diagonal permutations visible horizontally both forward and reversed. 

![https://raw.githubusercontent.com/DJDevon3/Classic_Cryptography/refs/heads/main/Progressive_Caesar_Matrix/Example.PNG](https://raw.githubusercontent.com/DJDevon3/Classic_Cryptography/refs/heads/main/Progressive_Caesar_Matrix/Example.PNG)

## Progressive Caesar Incrementing (0, 1, 2, 3 OR 0,-1,-2,-3):

One of the really neat aspects of a full printout of the entirety of every possible progressive matrix is it naturally shifts from positive increments to negative increments halfway through beginning at Matrix #13. So +13 also becomes -13. In fact 0 to +25 is also 0 to -25. There is no need to specify an increment because it covers every possible sequential increment as a natural course of the method. A progressive Caesar is one of the most beautifully symetrical cryptography methods.

## Progressive Caesar plus Scytale:

To view a sequential skipping pattern (Scytale) simply resize your window to be smaller. Each row is intentionally double spaced to make viewing Scytales within the matrices easier. 

## Keyworded Caesar Matrix also known as Vigenere or Quagmire III:

A Keyworded Caesar Matrix with a custom alphabet works in exactly the same way as Vigenere. In fact, Vigenere and most substitution ciphers at their core... are actually Caesar in a different format. The main difference is a Vigenere tableu isn't used. With the right alphabet and keyword you can crack a Vigenere cipher using a keyworded Caesar cipher.
