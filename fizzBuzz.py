def fizzBuzz(value):
    if type(value) == str:
        return "Valor inválido!"
    if value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"