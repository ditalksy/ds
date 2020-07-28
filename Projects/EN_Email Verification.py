import re

def validate(email):
   #Need to detect only 1 @
    #Detect format in email whether they have @ and . If they do have then we proceed to split the email into 3 parts: username, hosting, and extension
    if (("@" in email) and ("." in email)):
        
        #split the username, hosting and extension by @
        email_split = email.split('@')

        
        username = email_split[0]
        host_ex = email_split[1]

        #split the hosting and extension by .
        host_ex_split = host_ex.split('.')
        hosting = host_ex_split[0]
        extension = host_ex_split[1]

        if re.match(r'^[a-z0-9]+(?:[._][a-z0-9]+)*$',username):
            if re.match(r'^[a-z0-9]',hosting): #.isalnum() for checking
                if (re.match(r'^[a-z]+(?:[.][a-z]+)*$',extension) and (len(extension)<=5)): #.isalpha()
                    print(f"{email} is a VALID email address.")
                else:
                    print(f"{email} is an INVALID email address. Extension should only be alphabet and not longer than 5 characters.")
            else:
                print(f"{email} is an INVALID email address. Only alphabets are allowed in the hosting address.")
        else:
            print(f"{email} is an INVALID email address. Only alphanumeric, underscore, and period allowed in the username.")
    else:
        print(f"{email} is an INVALID email address. Wrong e-mail format. It should be username@hosting.extension")


email = input("Enter a valid email address: ").lower()
validate(email)