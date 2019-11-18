import re


# ---Matching Multiple Groups with the Pipe
heroRegex = re.compile(r'(Batman|Superman)')
hero = heroRegex.search('My favorite super hero is Superman and Batman is second')
print(hero.group())

hero2 = heroRegex.search('My favorite super hero is Batman and Superman is second')
print(hero2.group())


# ---Optional Matching with the Question Mark
print("\nOptional Matching with the Question Mark")
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())


# ---Zero or More with the Star
print("\nZero or More with the Star")
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())


mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())


# ---Matching One or More with the plus
print("\nMatching One or More with the plus ")
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search(' the Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search(' The  Adventure of Batwowowowoman')
print(mo2.group())
