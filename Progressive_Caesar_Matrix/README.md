# Progressive Caesar Matrix Encrypt/Decrypt
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
