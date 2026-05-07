# Конвертер температур
# Напишите программу, которая принимает от пользователя число (градусы Цельсия) и переводит его в Фаренгейты.

def temperature_converter():
    celsius = float(input("Введите температуру в °C:"))
    fahrenheit = (celsius * 1.8) + 32
    return celsius, fahrenheit
celsius, fahrenheit = temperature_converter()
print(f"{celsius}°C = {fahrenheit:.1f} °F")



