def temperature_converter():
    celsius = float(input("Введите значение в °C:"))
    fahrenheit = (celsius * 1.8) + 32
    return celsius, fahrenheit

celsius, fahrenheit = temperature_converter()
print(f"{celsius:g}°C = {fahrenheit:g}°F")



