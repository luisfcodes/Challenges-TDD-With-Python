def passwordValidator(password):
  listOfSpecialCharacters = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '.', ',', '?']
  numbers = 0
  capitalLetters = 0
  specialCharacters = 0

  for i in range(len(password)):
    try:
      int(password[i])
      numbers += 1
    except:
      if password[i].upper() == password[i]:
        capitalLetters += 1
      for x in listOfSpecialCharacters:
        if password[i] == x:
          specialCharacters += 1
  
  if len(password) < 8 and numbers < 2:
    return "A senha deve ter pelo menos 8 caracteres\nA senha deve conter pelo menos 2 números"
  
  if len(password) < 8:
    return "A senha deve ter pelo menos 8 caracteres"

  if numbers < 2:
    return "A senha deve conter pelo menos 2 números"

  if capitalLetters < 1:
    return "A senha deve conter pelo menos uma letra maiúscula"

  if specialCharacters < 1:
    return "A senha deve conter pelo menos um caractere especial"