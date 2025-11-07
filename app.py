# app.py
from concrete import fhe

@fhe.compiler({"x": "encrypted", "y": "encrypted"})
def encrypted_sum(x, y):
    return x + y

def main():
    inputset = [(5, 7), (10, 3), (2, 8)]
    circuit = encrypted_sum.compile(inputset)
    print("✅ FHE circuit compiled successfully with Zama Concrete.")

    x, y = 12, 4
    encrypted_result = circuit.encrypt_run_decrypt(x, y)
    print(f"🔒 Encrypted addition result: {x} + {y} = {encrypted_result}")

if __name__ == "__main__":
    main()
