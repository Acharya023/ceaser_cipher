def encryption(text,shift):
    encrypted = ""
    for val in text:
        if (val.isupper()):
            encrypted += chr((ord(val) -65 + shift) % 26 + 65)
        elif (val.isspace()):
            encrypted += chr((ord(val)) % 26 )
        elif (val.isnumeric()):
            encrypted += chr((ord(val) -48 + shift) % 10 + 48 )
        else:
            encrypted += chr((ord(val) - 97 + shift ) % 26 + 97)
    return encrypted

text = input("type text here:")
shift = int(input("shift by number:"))
print( "input text : " + text)
print("shift by     :" + str(shift))
print( "Encrypted text:" + encryption(text,shift))