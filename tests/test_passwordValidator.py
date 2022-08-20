from passwordValidator import passwordValidator

def test_should_return_an_error_if_the_password_is_less_than_8_characters():
  assert passwordValidator('sert22') == "A senha deve ter pelo menos 8 caracteres"

def test_should_return_an_error_if_the_password_does_not_contain_two_numbers():
  assert passwordValidator('sert2lus') == "A senha deve conter pelo menos 2 números"

def test_should_return_all_the_missing_requirements():
  assert passwordValidator('sert2lu') == "A senha deve ter pelo menos 8 caracteres\nA senha deve conter pelo menos 2 números"

def test_should_return_an_error_if_the_password_does_not_have_an_uppercase_letter():
  assert passwordValidator('sert22lu') == "A senha deve conter pelo menos uma letra maiúscula"

def test_should_return_an_error_if_the_password_does_not_have_a_special_character():
  assert passwordValidator('aaer22Ad') == "A senha deve conter pelo menos um caractere especial"