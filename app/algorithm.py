import math

import pymongo

from pymongo import MongoClient

client1 = MongoClient('mongodb://norfrosh:food@ds051110.mongolab.com:51110/dining')
db = client1.dining
dinner = db['dinner']

client2 = MongoClient('mongodb://norfrosh:food@ds051110.mongolab.com:51110/users')
db = client2.users
user = db.user



def nomnomnom(Fc, d, weightingFactorF, g):
	"""returns the best option for food and dining hall
		inputs: Fc, a list (for a specific cuisine) of lists where each list 
				contains three elements, the food(a string), its user-value(10.0-1.0, 10.0 is best), 
				and its corresponding dining hall name (a string), which will be converted to coordinates;
				d, a float describing the distance one is willing to go;
				weightingFactorF, a float corresponding to the weight FOOD has;
				g, a tuple representing the geographical coordinates of the user
		outputs: Nom, a list with elements food, dining hall, and distance
	"""
	DisList = [["hmc", (.59526, -2.04373)], ["frary", (.595165, -2.0544)], ["cmc", (.595185, -2.05441)],["pitzer",(.595214,-2.05435)]]
	for i in range(len(Fc)):
		for j in range(len(DisList)):
			if DisList[j][0] == str(Fc[j][2]):
				Fc[j][2] = DisList[j][1]
	DisCalcs = distanceCalcs(Fc, d, g, DisList)
	Fc = DisCalcs[0]
	distances = DisCalcs[1]
	scores = scoreList(Fc, d, weightingFactorF)
	#change code here to change number of results
	results = numResults(Fc, d, weightingFactorF, scores, 1)
	results = changer(results, distances)
	dHall = None
	print results
	for hall in DisList:
		if results[0][2] == hall[1]:
			dHall = hall[0]
	return results[0][0], dHall

def distanceCalcs(Fc, d, g, DisList):
	""" deals with distance stuff
		inputs: Fc, the user's food list described above;
				d, a float for the user's distance described above
				g, a tuple desribed above
		outputs: list of updated Fc and list of distances of each dining hall
	"""

	#calculate the dining halls' distances from the user
	Distances = []
	#INSERT COORDINATE CALCULATIONS HERE, replace coordDist
	for c in range(len(DisList)):
		#coordDist = DIST CALCULATIONS USING TUPLE d AND THE COORD TUPLE OF ELEMENT C IN THE DICT
		diningHallCoord=DisList[c][1]
		#calc distance
		x = math.radians(g[0])
		y = math.radians(g[1])
		deltax = x-diningHallCoord[0]
		meanx = (x+diningHallCoord[0])/2.0
		deltay = y-diningHallCoord[1]
		coordDist=3958.761*math.sqrt((deltax**2)+(math.cos(meanx)*deltay)**2)
		Distances.append([DisList[c][0], coordDist])

	#remove any lists in the Fc that have a third element (dining Hall) that corresponds to 
	#the current dining hall's coordinates only if that dining hall is too far away
	
	if coordDist > d:
		filter(lambda x: x[2]!=diningHallCoord, Fc)

	# convert the third element, dining hall coord, to its distance from the user
	if coordDist <= d:
		for i in range(len(Fc)):
			if Fc[i][2]==diningHallCoord:
				Fc[i][2] = d
	return [Fc, Distances]

def scoreList(Fc, d, weightingFactorF):
	"""creates a list that scores each food list, with matching indices to Fc
		inputs: Fc, the food list of the user, described above;
				d, the distance float, as described above;
				weightingFactorF, the float determining importance of food for user, escribed above
		outputs: the list of scores for each food
	"""
	#create a list with the "score" of each list within Fc, where the indices of the new list match the indices of Fc 
	#determine the weighting factor for distance, since we are given the one for walking
	weightingFactorD = 1 - weightingFactorF
	scores = [0]*len(Fc)
	for n in range(len(Fc)):
		#creates a score out of 10 for the distance of the nth element
		if d == 0.0:
			d = 1.0
		print Fc[n][1]
		print Fc
		#Fc[n][1]=math.sqrt(int((Fc[n][1][1]))**2 + int((Fc[n][1][2]))**2)
		distanceScore = (Fc[n][1]/d)*10
		#weight the distanceScore according to the user's preference
		distanceScore = distanceScore*weightingFactorD
		#weight the food's score, which is given in each food list's element 2
		foodScore = Fc[n][1]*weightingFactorF
		score = distanceScore + foodScore
		scores[n] = score
	return scores

def topResult(Fc, scores):
	"""find the index of the top highest rated food
		inputs: scores, a list of the scores of each food element in the same order as the foods were in Fc;
				Fc, the original food list, described above
		outputs: the top rated element of Fc
	"""
	topScore = scores[0]
	topIndex = 0
	for s in range(1,len(scores)):
		if scores[s]>topScore:
			topScore = scores[s]
			topIndex = s
	return Fc[topIndex]

def numResults(Fc, d, weightingFactor, scores, n):
	if n >= len(Fc):
		print "There aren't that many options for this cuisine today. Here are those available:"
		n = len(Fc)-1
	results = []
	for i in range(n):
		top = topResult(Fc, scores)
		results.append(top)
		Fc.remove(top)
		scores = scoreList(Fc, d, weightingFactor)
	return results

def changer(results, distances):
	for i in range(len(results)):
		dis = results[i][2]
		for j in range(len(distances)):
			if dis == distances[j][1]:
				results[i][2] = distances[j][0]
	return results


def taggedcuisine(meal):
	tags = meal[2]
	#if preferredTag in tags:
	return True
	#else:
	#	return False


def tagFinder(keyName):
	print keyName
	print type(keyName)
	food = dinner.find_one({"name": keyName})
	if food:
		tagList = food["tags"]
		return tagList
	else:
		return None

def makeChoice(g, foodListDict):
	Fc = []
	# list of lists with three elements, name, value, list of tags, dininghall name
	favMeals = []
	for key in foodListDict:
		key = str(key)
		tagList = tagFinder(key)
		if tagList:
			hallName = tagList[0]
			favMeals.append([key, foodListDict[key], tagList, hallName])
	preferredTag = ""
	filter(taggedcuisine, favMeals)
	if len(favMeals) == 0:
		print "No options for you. Try to be more exciting!"
	print favMeals
	for f in range(len(favMeals)):
		hallName = favMeals[f][3]
		Fc.append([favMeals[f][0], favMeals[f][1], hallName])
	d = 1000000
	return nomnomnom(Fc, d, 0.5, g)



