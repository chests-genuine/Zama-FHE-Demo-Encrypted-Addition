# Zama FHE Demo — Encrypted Addition

## Description
This repository demonstrates a simple **Fully Homomorphic Encryption (FHE)** example using **Zama's Concrete** framework.  
The script compiles an encrypted function that adds two numbers without ever decrypting them, illustrating how data privacy can be preserved during computation — a core concept behind projects like **Zama**, **ZK-based privacy layers**, and **sound cryptographic computation**.

## Installation
1. Make sure **Python 3.9+** is installed.  
2. Install Zama’s Concrete library:  
   pip install concrete  
3. Add the files `app.py` and `README.md` to your repository.

## Run with Docker
To run this project in a Docker container:

1. Build the image:
   docker build -t zama-fhe-demo .

2. Run the container:
   docker run --rm zama-fhe-demo


## Usage
Run the script with:  
python app.py  

The script will:
- Compile an encrypted addition circuit.
- Perform an encrypted computation (`x + y`) using FHE.
- Decrypt and display the result securely.

## Expected Output
If successful, you will see output similar to:  
✅ FHE circuit compiled successfully with Zama Concrete.  
🔒 Encrypted addition result: 12 + 4 = 16  

## Notes
- The example shows the essence of privacy-preserving computation — the data remains encrypted throughout processing.  
- You can modify the function to implement subtraction, multiplication, or more complex operations.  
- Zama’s FHE technology enables secure computations in fields like AI, blockchain privacy, and confidential data analytics.
