# получение данных от пользователя и разделение на имя и фамилию

def data_input(prompt:str):
    full_name = input("Please enter your name and surname: ")

    first_name = full_name.split()[0]
    last_name = full_name.split()[1]

    return full_name



