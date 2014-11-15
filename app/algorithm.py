import math

from pymongo import MongoClient

client1 = MongoClient('mongodb://norfrosh:food@ds051110.mongolab.com:51110/dining')
dbc = client1.dining
collection1 = dbc['dinner']

client2 = MongoClient('mongodb://norfrosh:food@ds051110.mongolab.com:51110/dining')
dbu = client2.users
collection2 = dbu['user']



# Hackathon Algorithm-Dining Hall Picker

#dictionary of dining halls and their coordinates (each a tuple)

def nomnomnom(Fc, d, weightingFactorF, g):
	"""returns the best option for food and dining hall
		inputs: Fc, a list (for a specific cuisine) of lists where each list 
				contains three elements, the food(a string), its user-value(10.0-1.0, 10.0 is best), and its corresponding dining hall coordinates (a tuple);
				d, a float describing the distance one is willing to go;
				weightingFactorF, a float corresponding to the weight FOOD has;
				g, a tuple representing the geographical coordinates of the user
		outputs: Nom, a list with elements food, dining hall, and distance
	"""
	DisList = [["Mudd-Hoch", (.59526, -2.04373)], ["Pomona-Frank", (.59509, -2.05445)], ["Pomona-Frary", (.595165, -2.0544)], ["Pomona-Oldenborg", (.595107, -2.05446)], ["CMC-Collins", (.595185, -2.05441)], ["Scripps-Malott", (.595207, -2.05444)], ["Pitzer-McConnell", (.595214, -2.05435)]]
	DisCalcs = distanceCalcs(Fc, d, g, DisList)
	Fc = DisCalcs[0]
	distances = DisCalcs[1]
	scores = scoreList(Fc, d, weightingFactorF)
	#change code here to change number of results
	results = numResults(Fc, d, weightingFactorF, scores, 3)
	results = changer(results, distances)
	return results

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
		g[0] = math.radians(g[0])
		g[1] = math.radians(g[1])
		deltax = g[0]-diningHallCoord[0]
		meanx = (g[0]+diningHallCoord[0])/2.0
		deltay = g[1]-diningHallCoord[1]
		coordDist=3958.761*math.sqrt((deltax**2)+(math.cos(meanx)*deltay)**2)
		Distances.append([DisLIst[c][0], coordDist])

	#remove any lists in the Fc that have a third element (dining Hall) that corresponds to 
	#the current dining hall's coordinates only if that dining hall is too far away
	
	if coordDist > d:
		filter(lambda x: x[2]!=diningHallCoord, Fc)

	# convert the third element, dining hall coord, to its distance from the user
	if coordDist <= d:
		for i in range(len(Fc)):
			if Fc[i][2]==diningHallCoord:
				Fc[i][2] = d
	return [Fc, distances]

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
	scores = []
	for n in range(len(Fc)):
		#creates a score out of 10 for the distance of the nth element
		if d == 0.0:
			d = 1.0
		distanceScore = (Fc[n][2]/d)*10
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
		top = resultstopResult(scores)
		results.append(top)
		Fc.remove(top)
		scores = scoreList(Fc, d, weightingFactorF)
	return results

def changer(results, distances):
	for i in range(len(results)):
		dis = results[i][2]
		for j in range(len(distances)):
			if dis == distances[j][1]:
				results[i][2] = distances[j][0]
	return results


def main():
	#Fc = 
	#d = 
	#g = 
#	nomnomnom(Fc, d, 0.5, g)


#	if __name__ == "__main__":
#		main()
