def is_palindrome(text:str)->bool:

    cleaned = ''.join(c.lower() for c in text if c.isalnum())

    if not cleaned:
        return False


    return cleaned == cleaned[::-1]

while True:
    user_input = input("Enter a string to check: ").strip()

    if not user_input:
        print('The string cannot be empty. \n')
        continue


    if is_palindrome(user_input):
        print("Palindrome")
        break

    else:
        print("Not a palindrome")
        break








