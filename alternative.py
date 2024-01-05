text = "Now here's a little story of a man named Jed. \nA poor mountaineer, barely kept his family fed" # original sentence, split into 2 lines with \n

print ("Here is the original: \n" + text) # print of original text

print()
uplow = ""  # create for loop
for i in range(len(text)):
    if not i % 2: # defines that very 2nd character (first letter) is identified
        uplow = uplow + text[i].upper()  # above retrned in upper case
    else:
       uplow = uplow + text[i].lower() # if not made upper, then the character will be lower case
print ("Every other letter of our sentence is a capital: \n" + uplow) # print text and output on a new line

print()

altuplow = "" # create for loop
altuplow = text.split() # split string or original text
altuplow[1::2] = map(str.upper, altuplow[1::2]) # defines that every 2nd word will be upper
altuplow = " " .join(altuplow) # joins the string 
print  ("Every other word is now made up of capitals: \n" + altuplow) # prints text and output on new line


