# Little Orphan Annie & Captain Midnight Brute Force Decoder:

Decoder rings are quite simple in their method. It's a Caesar cipher decoder with a numerical offset key. The key of 1 for example is a row offset of 1. 
Because there are only 26 possible offsets it is possible to create a Caesar Matrix with every possible solution. Every year a new decoder ring was issued with a different alphabet. 
A decoder ring from 1939 cannot decode a message with a 1940 decoder ring or vice versa. The alphabets used in the decoder wheels are known for every year. 
It is possible to brute force any message, from any decoder year, using any key with this script. If a message was created with a legimate Little Orphan Annie decoder ring or Captain Midnight decoder badge even if the year isn't known, this script will crack it. 

# What is a Little Orphan Annie or Captain Midnight Decoder? 
- The website https://www.mattblaze.org/blog/badges covers this topic far better than I can. You can see all the different makes and models of the decoders as well as their settings. 

![https://raw.githubusercontent.com/DJDevon3/Classic_Cryptography/refs/heads/main/Little_Orphan_Annie_Brute_Force/Example.PNG](https://raw.githubusercontent.com/DJDevon3/Classic_Cryptography/refs/heads/main/Little_Orphan_Annie_Brute_Force/Example.PNG)

# Usage:
- This is a pure python program designed to be run on a PC.

To run the program simply point Windows CMD prompt at the script and run with python:
```py
C:\Users\Devon\Documents\Kryptos Scripts>python Little_Orphan_Annie_Brute_Force.py
```
It will create a text file in a folder named Results. 

```py
C:\Users\Devon\Documents\Kryptos Scripts\Results
```
It will generate 1 file with all possible solutions for every decoder year. 
