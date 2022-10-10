# Conversion of 'Decimal Number' to 'Binary Number'
def decimalToBinary(n):
    # Here we are using built-in python function
    # converting decimal to binary and removing the prefix(0b)
    return (bin(n).replace("0b", "")) 
   