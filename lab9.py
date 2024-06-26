# Lucas Di Campli

def main():
    encoded_password = None
    original_password = None

    while True:
        print_menu()
        option = input("Please enter an option: ")

        if option == "1":
            original_password = input("Please enter your password to encode: ")
            encoded_password = encode_password(original_password)
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            if encoded_password:
                decoded_password = decode_password(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
            else:
                print("No password has been encoded yet!\n")
        elif option == "3":
            break


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode_password(password):
    encoded = ''
    for char in password:
        new_digit = (int(char) + 3) % 10
        encoded += str(new_digit)
    return encoded

def decode_password(encoded):
    # Code explained:
    # encoded_password_list is a list of ints
    # First, we map the above list (ie, iterate through each element in the list and modify them)
    # by setting each element to |x - 3| (makes it an absolute value)
    # Now this new list of ints is then converted to a single int
    # by using a mixture of int(), join(), and list comprehension
    encoded_password_list = [int(x) for x in str(encoded)]
    return int(
        "".join(str(i) for i in map(lambda x: abs(x - 3), encoded_password_list))
    )


if __name__ == "__main__":
    main()
