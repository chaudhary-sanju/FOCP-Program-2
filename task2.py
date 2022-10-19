def temp_convert():
    cel = float(input("Enter a temperature in Celsius: "))
    feh = ( cel * 1.8 ) + 32
    return(f"{cel}C is equivalent to {feh}F")

print(temp_convert())