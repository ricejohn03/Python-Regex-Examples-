import re
import os

#To Display Your Current Directpry
print("This is you current DIR= " + os.getcwd() + "\n")


# open data file and store into a variable
phoneEmailDatafile = open('youtextfile.txt')
pedData = phoneEmailDatafile.read()
phoneEmailDatafile.close()

# defining the parameters to find phone numbers in text
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
(\d{3}) # first 3 digits
(\s|-|\.) # separator
(\d{4}) # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

# defining the parameters to find email addresses in text
emailRegex = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

# Create list to store each piece of the extracted data.
info_list = []
phone_list = []
email_list = []

# loop over all groups in the data and append them to the list for both numbers and email
for groups in phoneRegex.findall(pedData):
    phone_list.append(groups[0])
for groups in emailRegex.findall(pedData):
    email_list.append(groups)

# consolidate the list and print
for i in range(0, len(phone_list) - 1):
    info_list.append(phone_list[i])
    info_list.append((email_list[i]))

# loop and store sorted data into a string to pass to the write function later()
it = iter(info_list)
finaldata = ''
for i in it:
    finaldata = finaldata + ("Number: " + i + " - Email: " + next(it) + "\n")

# save newly sorted data to txt file
sorted_data = open("sorted-data.txt", 'w')
for line in finaldata.splitlines():
    print(line)
    sorted_data.write(line + '\n')

sorted_data.close()