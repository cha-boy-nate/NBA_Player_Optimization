import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from sklearn import datasets, linear_model

from matplotlib.ticker import NullFormatter

#Class creates class data type with their playerID, name. value, and age
class player:
	name = ''
	playerID = ''
	value = 0
	age = 0

	def __init__(self, playerID, name, value, age):
		self.playerID = playerID
		self.name = name
		self.value = value
		self.age = age

def main():
	#create arrays for players sorted into positions
	shootingGuard = []
	powerForward = []
	center = []
	pointGuard = []
	
	#get data from csv and sort players into arrays
	getData('nba.csv', shootingGuard, powerForward, center, pointGuard)
	
	#shows some sample scatterplots using matplotlib and numpy. X-axis is age (weight). Y-axis is player efficiency (value)
	makeGraph(shootingGuard, "Shooting Guard Statistics")
	makeGraph(powerForward, "Power Forward Statistics")
	makeGraph(center, "Center Statistics")
	makeGraph(pointGuard, "Point Guard Statistics")

	return 0

#Function takes a set of data and title as parameters and uses them to construct a scatterplot with a line of linear regression (line of best fit)
def makeGraph(dataset, titleString):
	value = []
	age = []
	for person in dataset:
		value.append(float(person.value))
		age.append(int(person.age))
	fig, ax = plt.subplots(1,1)
	ax.plot(np.unique(age), np.poly1d(np.polyfit(age, value, 1))(np.unique(age)), color='red')
	plt.xlabel('Age')
	plt.ylabel('Value (player efficency)')
	plt.title(titleString)
	ax.scatter(age,value)
	ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
	ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
	plt.show()
	return

#Function reads data from a csv file and sorts players by position into one of 4 position arrays
def getData(fileLocation, shootingGuard, powerForward, center, pointGuard):
	with open(fileLocation, newline='') as data:
		reader = csv.reader(data)
		for row in reader:
			if(row[2] == "SG"):
				shootingGuard.append(player(row[0], row[1], row[4], row[3]))
			elif(row[2] == "PF"):
				powerForward.append(player(row[0], row[1], row[4], row[3]))
			elif(row[2] == "PG"):
				pointGuard.append(player(row[0], row[1], row[4], row[3]))	
			elif(row[2] == "C"):
				center.append(player(row[0], row[1], row[4], row[3]))	

main()
