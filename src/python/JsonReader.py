import json
import os
from itertools import groupby
from collections import ChainMap

class JsonReader:
	def __init__(self):
		self.dir = "files"
		self.key = "cities"
		
	def getValidJson(self, jsonString):
		try:
			jsonData = json.loads(jsonString)
		except ValueError:
			return None
		return jsonData
		
	def readJsonFiles(self):
		try:
			dataSet = []
			for filename in os.listdir(self.dir):
				if filename.endswith(".json"):
					with open(os.path.join(self.dir, filename), encoding = "utf8") as file:
						jsonString = file.read()
						jsonData = self.getValidJson(jsonString)
						if jsonData != None:
							dataSet.extend(jsonData[self.key])
						else:
							raise ValueError
			return dataSet
		except KeyError:
			print("Key \'", self.key, "\' doesn't exist")
			return []
		except ValueError:
			print("File has incorrect format")
			return []
			
	def combineDataSetsFromJsonFiles(self):
		dataSet = self.readJsonFiles()
		if len(dataSet) == 0:
			return []
		else:
			try:
				key = "city"
				citiesKey = lambda cityDict : cityDict[key].lower()
				res = map(lambda dicts : dict(ChainMap(*dicts[1])),
					groupby(sorted(dataSet, key = citiesKey), key = citiesKey))	
				return list(res)
			except KeyError:
				print("The invalid format of \'", key, "\' key")
				return []
		
		