def add(string):
    if len(string) < 1:
        return 0
    
    if string[len(string) - 1] == "," or string[len(string) - 1] == "\n":
        return 'Entrada Inválida!'

    result = 0
    delimiter = ""
    newString = string

    for z in string[0::2]:
        print(z)

    if len(string) > 4:
        if string[0:4] == f"//{string[2]}\n":
            delimiter = string[2]
            newString = string[4:]
            for index, y  in enumerate(newString):
                try:
                    number = int(y)
                    result = result + number
                except:
                    
                    if y != delimiter:
                        return f"'{delimiter}' esperado mas '{y}' encontrado na posição {index}."
            return result

    for x in newString:
        try:
            number = int(x)
            result = result + number
        except:
            print('')
    
    print(result)
    return result
    
add("2,-4,-9")