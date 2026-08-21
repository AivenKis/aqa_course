#                                                                   Palindrome:
#                                          Write a function that checks whether the entered string is a palindrome (reads the same in both directions).



def is_palindrome(text:str) -> bool:

   cleaned = text.lower().replace(" ", "")

   reversed_text = cleaned[::-1]


   if cleaned == reversed_text:
       return True
   else:
       return False

while True:
    user_input = input("Enter a string check: ").strip()

    if not user_input:
        print("The string cannot be empty. \n")
        continue

    result = is_palindrome(user_input)

    if result:
        print("The string is palindrome. \n")

    else:
        print("The string is not palindrome. \n")

    break








