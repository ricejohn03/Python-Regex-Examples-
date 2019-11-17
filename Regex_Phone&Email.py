import re

# sample data to test on
phoneEmailData = 'My Name is Cole my email is Cole33@gmail.com and number is 123-665-9565 \n' \
                 'My Name is Sally my email is sally@gmail.com and number is 123-665-9555 \n' \
                 'My Name is Brad my email is Brad@gmail.com and number is 663-665-9565 \n' \
                 'My Name is Mac my email is mac@gmail.com and number is 523-665-9565 \n' \
                 'My Name is Kal my email is Kal@gmail.com and number is 123-665-9565 \n' \
                 'My Name is Tina my email is Tina@gmail.com and number is 183-665-9565'

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
for groups in phoneRegex.findall(phoneEmailData):
    phone_list.append(groups[0])
for groups in emailRegex.findall(phoneEmailData):
    email_list.append(groups)

# consolidate the list and print
for i in range(0,len(phone_list) -1):
    info_list.append(phone_list[i])
    info_list.append((email_list[i]))

    
#loop and print out data with the number first and email second
it = iter(info_list)
for i in it:
    print("Number: " + i + " - Email: " + next(it))
