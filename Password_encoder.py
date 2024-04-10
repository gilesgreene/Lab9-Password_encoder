#Giles Greene
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(unencoded_password):
    encoded_password = ""
    for char in unencoded_password:
        old_digit = int(char)
        new_digit = (int(char) + 3) % 10
        encoded_password += str(new_digit)
    return encoded_password


def decode(encoded_passwd):
    """Decodes password by shifting numbers
    3 times back"""

    passwd = ''

    for num in encoded_passwd:
        num = int(num)
        new_num = (num - 3) % 10
        passwd += new_num

    return passwd


def main():
    while True:
        menu()
        option = int(input("\nPlease enter an option:"))
        if option == 1:
            password = input("Please enter your password to encode:")
            encode(password)
            print("Your password has been encoded and stored!\n")
        #if option == 2:

        if option == 3:
            break
if __name__ == "__main__":
    main()
