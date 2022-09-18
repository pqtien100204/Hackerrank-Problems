def print_formatted(number):
    # your code goes here
    w = len(str(bin(number)).replace('0b',''))
    results = []
    for i in range(1, number+1):
        deci = str(round(i)).rjust(w, " ")
        octal = oct(i)[2:].rjust(w, " ")
        hexa = hex(i)[2:].upper().rjust(w, " ")
        bina = bin(i)[2:].rjust(w, " ")
        print(deci, octal, hexa, bina)
print(print_formatted(17))