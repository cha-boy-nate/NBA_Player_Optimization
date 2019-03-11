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

	def __init__(self, playerID, name, value, weight):
		self.playerID = playerID
		self.name = name
		self.value = value
		self.weight = weight

def main():
	test = []
	getData("nba-sorted.csv", test)
	W = 200
	n = len(test)
	knapSack(W, getWeights(test), getValues(test), n)
	return 0

def knapSack(maxWeight, weight, value, counter):
	table = [[0 for runningWeight in range(maxWeight + 1)]
		 for index in range(counter + 1)]
	for index in range(counter + 1):
		for runningWeight in range(maxWeight + 1):
			if index == 0 or runningWeight == 0:
				table[index][runningWeight] = 0
			elif weight[index - 1] <= runningWeight:
				table[index][runningWeight] = max(value[index - 1] + table[index - 1][runningWeight - weight[index - 1]], table[index - 1][runningWeight])
			else:
				table[index][runningWeight] = table[index - 1][runningWeight]
	final = table[counter][maxWeight]
	print("Max skill is " + str(final))
	w = maxWeight
	for index in range(counter, 0, -1):
		if final <= 0:
			return 0
		if final == table[index - 1][runningWeight]:
			continue
		else:
			print("weight - " + str(weight[index - 1]) + " value - " + str(value[index - 1]))
			final = final - value[index - 1]
			runningWeight = runningWeight - weight[index - 1]

def getData(fileLocation, dataset):
	with open(fileLocation, newline='') as data:
		reader = csv.reader(data)
		for row in reader:
			dataset.append(player(row[0], row[1], float(row[4]), int(row[3])))

def getWeights(players):
	output = []
	for i in players:
		output.append(i.weight)
	return output

def getValues(players):
	output = []
	for i in players:
		output.append(i.value)
	return output

main()
