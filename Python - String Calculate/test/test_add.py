from add import add

def test_should_return_zero_for_empty_string():
    assert add("") == 0

def test_should_return_the_number_itself_in_case_of_an_argument():
    assert add("5") == 5

def test_should_return_the_sum_of_two_comma_separated_numbers():
    assert add("3,3") == 6

def test_should_return_the_sum_of_the_numbers_regardless_of_the_arguments():
    assert add("//;\n1;3") == 4

def test_should_return_an_error_if_there_is_a_separator_at_the_end():
    assert add("3,4\n") == "Entrada Inválida!"

def test_should_return_the_sum_accepting_new_delimiters():
    assert add("//;\n1;3") == 4

def test_should_return_an_error_if_the_delimiter_is_different_from_the_one_informed():
    assert add("//|\n1|2,3") == "'|' esperado mas ',' encontrado na posição 3."