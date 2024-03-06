punctuation = '''!()-{};:'"/?@\,#$%^<>[].&*_~'''
empty = ""

text = input("Please enter some text: ")

for char in text:
   if char not in punctuation:
       empty = empty + char
print(empty)
