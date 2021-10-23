user_input = str(input("Enter the words to convert to acronym: "))
text = user_input.split()
a = ' '
for i in text:
    a = a + str(i[0]).upper()
print(a)


# OUTPUT:
# Enter the words to convert to acronym: Vaibhav Nath
# VN