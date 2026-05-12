def slices(text:str):

    firs_six = text[:6]
    last_three = text[-3:]
    every_second = text[::2]

    return firs_six, last_three, every_second

result = slices("PythonProgramming")
first, last, every_second = result

print(first)
print(last)
print(every_second)



