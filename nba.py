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
	data = []
	getData("sample-nba-salaries-per.csv", data)
	sum = 0
	for i in data:
		
		sum = i.value + sum
	#maxWeight = 1000000
	#n = len(data)
	#knapSack(maxWeight, getWeights(test), getValues(test), n)
	#print(test(maxWeight, getWeights(data), getValues(data), n))
	return 0


def test(W, wt, val, n):
	# Base Case
	if n == 0 or W == 0:
		return 0

	# If weight of the nth item is more than Knapsack of capacity
	# W, then this item cannot be included in the optimal solution
	if (wt[n - 1] > W):
		return test(W, wt, val, n - 1)

	# return the maximum of two cases:
	# (1) nth item included
	# (2) not included
	else:
		return max(val[n - 1] + test(W - wt[n - 1], wt, val, n - 1), test(W, wt, val, n - 1))


def knapSack(maxWeight, weight, value, counter):
	table = [[0 for runningWeight in range(maxWeight + 1)] for index in range(counter + 1)]
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
		i = 0
		for row in reader:
			dataset.append(player(i, row[0], float(row[3]), int(row[2])))
			i = i + 1

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
