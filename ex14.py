# converts a Celsius temperature to Fahrenheit
celsius = float(input('Enter the temperature in Celsius: '))
fahrenheit = (celsius * (9/5)) + 32
print('The temperature of {:.2f}°C in Fahrenheit is {:.2f}°F'.format(celsius, fahrenheit))
