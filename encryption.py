
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

KEY_FILE = Path("key.key")


def load_or_create_key():
    if KEY_FILE.exists():
        return KEY_FILE.read_bytes()

    key = Fernet.generate_key()
    KEY_FILE.write_bytes(key)
    return key


def main():
    key = load_or_create_key()
    cipher = Fernet(key)

    print("=== Data Encryption and Decryption ===")
    print("1. Encrypt text")
    print("2. Decrypt text")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        text = input("Enter text to encrypt: ")
        encrypted = cipher.encrypt(text.encode("utf-8"))
        print("\nEncrypted text:")
        print(encrypted.decode("utf-8"))

    elif choice == "2":
        encrypted_text = input("Enter encrypted text: ")

        try:
            decrypted = cipher.decrypt(
                encrypted_text.encode("utf-8")
            )
            print("\nDecrypted text:")
            print(decrypted.decode("utf-8"))
        except (InvalidToken, ValueError):
            print("Decryption failed. Check the text and key.")

    else:
        print("Invalid option. Choose 1 or 2.")


if __name__ == "__main__":
    main()
