# Zama FHE Demo — Encrypted Addition

## Description
This repository demonstrates a simple **Fully Homomorphic Encryption (FHE)** example using **Zama's Concrete** framework.  
The script compiles an encrypted function that adds two numbers without ever decrypting them, illustrating how data privacy can be preserved during computation — a core concept behind projects like **Zama**, **ZK-based privacy layers**, and **sound cryptographic computation**.

## Installation
1. Make sure **Python 3.9+** is installed.  
2. Install Zama’s Concrete library:  
   pip install concrete  
3. Add the files `app.py` and `README.md` to your repository.

## Usage
Run with default values:  
python app.py  

Provide custom encrypted inputs:  
python app.py --x 15 --y 8  

Provide a list of numbers for encrypted list summation:  
python app.py --list 1 2 3 4 5  

You can also combine both operations:  
python app.py --x 5 --y 9 --list 2 4 6 8 

## Expected Result
When running with --x 5 --y 9, you will see:  
✅ FHE circuits compiled successfully with Zama Concrete.  
🔒 Encrypted addition result: 5 + 9 = 14  

When running with --list 2 4 6 8, you will see:  
✅ FHE circuits compiled successfully with Zama Concrete.  
🧮 Encrypted list sum result: [2, 4, 6, 8] → 20

## Notes
• All computations are performed using Fully Homomorphic Encryption (FHE) via Zama’s Concrete framework.  
• Results are decrypted only after encrypted evaluation is complete.  
• You can use this example as a minimal template for building secure, privacy-preserving arithmetic pipelines. 
