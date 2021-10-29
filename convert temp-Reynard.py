def convert_temp_c():
    tc = 5/9*(tf - 32)
    return tc


def convert_temp_k():
    tc = 5/9*(tf - 32)
    tk = tc + 273.15
    return tk


tf = int(input("Enter a temperature in Fahrenheit: "))
print("The temperature in Fahrenheit is: ", tf)
print("The temperature in Celsius is: ", convert_temp_c())
print("The temperature in Kelvin is: ", convert_temp_k())
