#Importing necessary modules

import random
import array
from this import d


#Setting maxium length for pass
max_len=6

#Arrays for chracters being used in the pass
DIGITS = ['0', '1', '2', '3', '4','5','6','7','8','9']
lowcase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
upcase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

#combining list
combined_list = DIGITS + lowcase + upcase

#randomly selecting one chracter 
random_digit = random.choice(DIGITS)
random_lower = random.choice(lowcase)
random_upper = random.choice(upcase)    

#now we have 3 random digits, but we need 6 
temp_password = random_digit + random_lower + random_upper

#so we again select randomly from the arrays
for i in range(max_len - 3):
    temp_password = temp_password + random.choice(combined_list)


#shuffling pass
temp_password_list = array.array('u', temp_password)
random.shuffle(temp_password_list)

#forming password
password = ""
for x in temp_password_list:
    password = password + x


#finally printing password
print("Password generated successfully! Your password is:", password)
