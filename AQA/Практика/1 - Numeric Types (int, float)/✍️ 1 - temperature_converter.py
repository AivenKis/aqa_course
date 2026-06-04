def celsius_user_input():

    while True:
        try:
            value = float(input("Enter temperature in Celsius:"))
            return value
        except ValueError:
            print("ERROR: Please enter a numeric value\n")

def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32


celsius = celsius_user_input()
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius:g}°C = {fahrenheit:g}°F")














