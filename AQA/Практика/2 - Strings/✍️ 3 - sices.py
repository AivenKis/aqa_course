def sices(text:str)->str:
    text = "PythonProgramming"
    print(text[:6])
    print(text[-3:])
    print(text[::2])
    return text[:6], text[-3:], text[::2]

sices("PythonProgramming")


