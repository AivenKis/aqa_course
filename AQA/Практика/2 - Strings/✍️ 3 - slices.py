#                                                                 Slicing:
#                           from the string “PythonProgramming”, output the first 6 characters,
#                             the last 3 characters, and the string with every other character.


def slices(text:str) -> tuple[str, str, str]:

    first_six = text[:6]
    last_three = text[-3:]
    every_second = text[::2]

    return first_six, last_three, every_second


first, last, every_second = slices("PythonProgramming")

print(first)
print(last)
print(every_second)




