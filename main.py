punctuations = '''!()-{};:'"/?@\,#$%^<>[].&*_~'''
no_punct = ""

my_str = input("Enter a string: ")

for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char
print(no_punct)
