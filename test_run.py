def start(nice=0,mean=0,name=""):
	name = describe_name(name)
	nice,mean,name = nice_mean(nice,mean,name)

def describe_name(name):
	if name != "":
		print("\nThank you for playing again, {}!".format(name))
	else:
		stop = True
		while stop:
			if name == "":
				name = input("\nWhat is your name? ").capitalize()
			if name != "":
				print("\nWelcome, {}!".format(name))
				stop = False
	return name

def nice_mean(nice,mean,name):
	stop = True
	while stop:
		show_score(name,nice,mean)
		pick = input("\nA stranger approaches you for a \n conversation. Will you be nice \nor mean? (N/M) ").lower()
		if pick == "n":
			print("\nThe stranger walks away smiling...")
			nice = (nice + 1)
			stop = False
		if pick == "m":
			print("\nThe stranger glares at you \nmenaciously and storms off...")
			mean = (mean + 1)
			stop = False
	score(nice,mean,name)

def show_score(name,nice,mean):
	print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
	if nice > 2:
		win(nice,mean,name)
	if mean > 2:
		mean(nice,mean,name)
	else:
		nice_mean(nice,mean,name)

def win(nice,mean,name):
	print("\nNice job {}, you win! \n Everyone loves you".format(name))
	again(nice,mean,name)

def lose(nice,mean,name):
	print("\nGame over {}".format(name))
	again(nice,mean,name)

def again(nice,mean,name):
	stop = True
	while stop:
		choice = input("\nDo you want to play gain?").lower()
		if choice == "y":
			stop = False
			reset(nice,mean,name)
		if choice == "n":
			print("Sorry to let you go")
			stop = False
			quit()
		else:
			print("\nEnter ( Y ) for 'Yes', ( N ) for 'No': ")

def reset(nice,mean,name):
	nice = 0
	mean = 0
	start(nice,mean,name)

if __name__ == "__main__":
	start()