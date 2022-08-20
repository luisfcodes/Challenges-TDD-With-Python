from fizzBuzz import fizzBuzz

def test_should_return_an_error_when_receiving_string():
    assert fizzBuzz('2') == "Valor inválido!"

def test_should_return_fizz_for_multiples_of_three():
    assert fizzBuzz(9) == 'Fizz'

def test_should_return_buzz_for_multiples_of_five():
    assert fizzBuzz(20) == 'Buzz'

def test_should_return_fizzbuzz_for_multiples_of_three_and_five():
    assert fizzBuzz(15) == 'FizzBuzz'