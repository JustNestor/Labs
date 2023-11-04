# # while True:
# # 	try:
# # 		a, b, c = input().split()
# # 		a, c = int(a), int(c)
# #
# # 		match b:
# # 			case "+": print(f"{a+c}")
# # 			case "-": print(f"{a-c}")
# # 			case "*": print(f"{a*c}")
# # 			case "/": print(f"{a/c}")
# #
# # 	except ZeroDivisionError: print("Не можливо поділити на 0!")
# # 	except Exception as e: print(e)
#
#

while True:
	a, b, c = input().split()
	a, c = int(a), int(c)
	if c == 0:
		print("Не можливо поділити на 0!")
		continue

	if b == "+": print(f"{a+c}")
	elif b == "-": print(f"{a-c}")
	elif b == "*": print(f"{a*c}")
	elif b == "/": print(f"{a/c}")
	elif b == "**": print(f"{a**c}")
	elif b == "//": print(f"{a//c}")
	elif b == "%": print(f"{a%c}")
	else: print("Не відома операція!")




