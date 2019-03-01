def getInfo():
	var1 = input("input your first value: ")
	var2 = input("input your second value: ")
	return var1,var2

def compute():
	go = True
	while go:
		var1,var2 = getInfo()
		try:
			var3 = int(var1) + int(var2)
			go = False
		except ValueError as e:
			print("{}: You did not provide a numeric value!".format(e))
		except:
			print("You provided invalid input")

	print("{} + {} = {}".format(var1,var2,var3))

if __name__ == "__main__":
	compute()