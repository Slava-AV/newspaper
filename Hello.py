import sys

def say_hello(names):
	listOfnames=""
	i =0
	while i < len(names):
		listOfnames=listOfnames+names[i]
		i=i+1

	print("Hi " + listOfnames)

if __name__ == "__main__":
	names = input("What are your names, guys: ")
	names = names.split(",")
	# say_hello(sys.argv[1],sys.argv[2])
	say_hello(names)
	# Hi!!!