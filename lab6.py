#Original File: Yiqiao (Emily) Huang

def encode(original):
    encoded = []
    for letter in original:
        encoded.append(str((int(letter) + 3) % 10))
    return "".join(encoded)


def main():
    is_running = True
    while is_running:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")

        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode:")
            enc = encode(password)
            print("Your password has been encoded and stored!\n")
        if option == 3:
            is_running = False


if __name__ == "__main__":
    main()