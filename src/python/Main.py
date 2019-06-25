from Parser import Parser

def printMenu():
    print(30 * "-", "MENU", 30 * "-")
    print("1. Get all cities")
    print("2. Display cities")
    print("3. Display filter cities")
    print("0. Exit")
    print(67 * "-")

def main():
	loop = True
	cities = []
	while loop:
		printMenu()
		choice = input("Enter your choice [0-3]: ")
		 
		if choice == "1":
			parser = Parser()
			cities = parser.parseListOfCities()
			print("Cities collected")
		elif choice == "2":
			if len(cities) == 0:
				print("Fill list of cities with option 1")
			else:
				for city in cities:
					city.displayCity()
		elif choice == "3":
			if len(cities) == 0:
				print("Fill list of cities with option 1")
			else:
				parser.filterCities(cities)
		elif choice == "0":
			loop = False
		else:
			input("Wrong option selection. Enter any key to try again")
			
if __name__ == "__main__":
	main()