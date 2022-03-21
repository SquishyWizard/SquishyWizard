# This is a small simple program I created for myself. 
# I use caps lock when typing long lines of text and on occasions 
# finding myself in the predicament of a reverse caps lock situation. 

#This was my quick solution to the issue. 

inputText = input("Enter your wrongdoing: ")
for element in inputText:
  if element.isupper() == True:
    print (element.lower(),end="")
  else:
    print (element.upper(),end="")
input("\nPress Enter to leave")
