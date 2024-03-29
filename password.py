def encode(x):
    enc_pw = ""
    for item in password:
        if item == "0":
            enc_pw += "3"
        elif item == "1":
            enc_pw += "4"
        elif item == "2":
            enc_pw += "5"
        elif item == "3":
            enc_pw += "6"
        elif item == "4":
            enc_pw += "7"
        elif item == "5":
            enc_pw += "8"
        elif item == "6":
            enc_pw += "9"
        elif item == "7":
            enc_pw += "0"
        elif item == "8":
            enc_pw += "1"
        elif item == "9":
            enc_pw += "2"
    return enc_pw


# Rachel decode function: takes in encoded password and returns the original password
def decode(encoded_password):
    decoded_password = ""

    for char in encoded_password:
        decoded_char = int(char) - 3

        if decoded_char < 0:
            decoded_char += 10

        decoded_password += str(decoded_char)

    return decoded_password


while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    user_input = int(input("Please enter an option: "))
    if user_input == 1:
        password = input("Please enter your password to encode: ")
        password = encode(password)
        print("Your password has been encoded and stored!\n")
    elif user_input == 2:
        print(f"The encoded password is {password}, and the original password is {decode(password)}.")
    elif user_input == 3:
        break
