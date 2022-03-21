inputText = input("Enter your wrongdoing: ")
for element in inputText:
  if element.isupper() == True:
    print (element.lower(),end="")
  else:
    print (element.upper(),end="")
input("\nPress Enter to leave")