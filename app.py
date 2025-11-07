import argparse
from concrete import fhe


# === Encrypted FHE operations ===
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
    # --- Parse command-line arguments ---
    parser = argparse.ArgumentParser(description="Encrypted addition using Zama Concrete.")
    parser.add_argument("--x", type=int, default=12, help="First encrypted number")
    parser.add_argument("--y", type=int, default=4, help="Second encrypted number")
    parser.add_argument("--list", nargs="*", type=int, help="Optional list of integers for encrypted_sum_list")
    args = parser.parse_args()

    # --- Compile FHE circuits ---
    inputset_add = [(5, 7), (10, 3), (2, 8)]
    circuit_add = encrypted_sum.compile(inputset_add)

    inputset_list = [(1, 2, 3), (4, 5, 6)]
    circuit_list = encrypted_sum_list.compile(inputset_list)

    print("✅ FHE circuits compiled successfully with Zama Concrete.")

    # --- Encrypted addition ---
    encrypted_result = circuit_add.encrypt_run_decrypt(args.x, args.y)
    print(f"🔒 Encrypted addition result: {args.x} + {args.y} = {encrypted_result}")

    # --- Encrypted list sum (if provided) ---
    if args.list:
        encrypted_list_result = circuit_list.encrypt_run_decrypt(tuple(args.list))
        print(f"🧮 Encrypted list sum result: {args.list} → {encrypted_list_result}")


if __name__ == "__main__":
    main()
