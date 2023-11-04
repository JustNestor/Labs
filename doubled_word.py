string = input()
result = ""
for char in string:
    if char == " ": result += char
    else: result += char*2
print(result)
