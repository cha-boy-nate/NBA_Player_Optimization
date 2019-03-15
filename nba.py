import csv

#Class creates class data type with their playerID, name. value, and age
class player:
	name = ''
	playerID = ''
	value = 0
	age = 0

	def __init__(self, playerID, name, value, weight):
		self.playerID = playerID
		self.name = name
		self.value = value
		self.weight = weight

def main():
	data = []
	getData("sample-nba-salaries-per.csv", data)
	userSelection = input("Enter your the value from your selected players: ")
	maxWeight = input("Enter your Max Value (Max Budget): ")
	n = len(data)
	optSelection = opt(int(maxWeight), data, n)
	print("------------")
	print("You can inprove your score by "  + str(optSelection - float(userSelection)) + " points for spending " + str(maxWeight))
	print("From: " + str(userSelection))
	print("To: " + str(optSelection))
	print("------------")
	return 0

def opt(maxWeight, players, counter):
	if counter == 0 or maxWeight == 0: return 0
	if (players[counter -1].weight > maxWeight): return opt(maxWeight, players, counter - 1)
	else: return max(players[counter -1].value + opt(maxWeight - players[counter -1].weight, players, counter - 1), opt(maxWeight, players, counter - 1))

def getData(fileLocation, dataset):
	with open(fileLocation, newline='') as data:
		reader = csv.reader(data)
		i = 0
		for row in reader:
			dataset.append(player(i, row[0], float(row[3]), int(row[2])))
			i = i + 1

main()
