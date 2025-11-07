from concrete import fhe

@fhe.compiler({"x": "encrypted", "y": "encrypted"})
def encrypted_sum(x, y):
    return x + y


@fhe.compiler({"values": "encrypted"})
def encrypted_sum_list(values):
    total = 0
    for v in values:
        total += v
    return total


def main():
    inputset = [(5, 7), (10, 3), (2, 8)]
    circuit = encrypted_sum.compile(inputset)
    print("✅ FHE circuit compiled successfully with Zama Concrete.")

    x, y = 12, 4
    encrypted_result = circuit.encrypt_run_decrypt(x, y)
    print(f"🔒 Encrypted addition result: {x} + {y} = {encrypted_result}")

    list_inputset = [(list(range(5)),)]
    list_circuit = encrypted_sum_list.compile(list_inputset)
    result_list = list_circuit.encrypt_run_decrypt(list(range(5)))
    print(f"🔐 Encrypted sum of list [0,1,2,3,4] = {result_list}")

if __name__ == "__main__":
    main()
