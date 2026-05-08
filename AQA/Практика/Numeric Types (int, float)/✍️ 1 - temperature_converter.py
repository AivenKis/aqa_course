def temperature_converter():

    while True:
        try:
            value = float(input("Enter temperature in Celsius:"))
            return value
        except ValueError:
            print("ERROR: Please enter a numeric value\n")



celsius = temperature_converter()
fahrenheit = (celsius * 1.8) + 32

print(f"{celsius:g}°C = {fahrenheit:g}°F")



