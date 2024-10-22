#Original File: Yiqiao (Emily) Huang

def encode(original):
    encoded = []
    for letter in original:
        encoded.append(str((int(letter) + 3) % 10))
    return "".join(encoded)

# decode function added by Christian Domingo
def decode(enc):
    decoded = ""
    temp_list = list(enc)
    for i in range(len(enc)):
        if temp_list[i] == "0":
            decoded += "7"
        elif temp_list[i] == "1":
            decoded += "8"
        elif temp_list[i] == "2":
            decoded += "9"
        else:
            decoded += str(int(temp_list[i]) - 3)
    return decoded

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
        # menu option 2 added by Christian Domingo
        elif option == 2:
            dec = decode(enc)
            print(f"The encoded password is {enc}, and the original password is {dec}")
        if option == 3:
            is_running = False


if __name__ == "__main__":
    main()