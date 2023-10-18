from temp_converter_7 import celsius_to_fahrenheit, fahrenheit_to_celsius

temperature = input("Enter a temperature: ")

conversion_choice = input("Convert to (Celsius or Fahrenheit): ").strip().lower()

if conversion_choice == "celsius":
    result = celsius_to_fahrenheit(int(temperature))
    print(f"{temperature} °C is approximately {result} °F")
elif conversion_choice == "fahrenheit":
    result = fahrenheit_to_celsius(int(temperature))
    print(f"{temperature} °F is approximately {result} °C")
else:
    print("Invalid conversion choice. Please enter 'Celsius' or 'Fahrenheit'.")
