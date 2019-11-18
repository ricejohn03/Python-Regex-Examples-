import re


# ---Matching Specific Repetitions with Curly Brackets
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2 == None)


# ---Greedy and Nongreedy Matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())


# ---The findall() Method
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
pho_num = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(pho_num)

# ---Making Your own Charater Classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelsfound = vowelRegex.findall('The Big Man is crazy about patatos')
print(vowelsfound)