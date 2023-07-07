for i in range(1, 101):
    
    output = ""

    if i % 3 == 0:
        output = output + "Fizz"
    
    if i % 5 == 0:
        output = output + "Buzz"
    
    if i % 7 == 0:
        output = output + "Rizz"
    
    if i % 11 == 0:
        output = output + "Jazz"
    
    if 120 % i == 0:
        output = output + "Dizz"
    
    if output == "":
        output = i
    
    print(output)