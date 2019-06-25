import json
import JsonReader as jr
from City import TrafficType
from City import RecreationType
from City import City
from Scalar import DensityType
from Scalar import AreaType
from Scalar import compareValue

class Parser:
	def __init__(self):
		jsonReader = jr.JsonReader()
		self.trafficDetails = "traffic_details"
		self.area = "area"
		self.recreations = "recreations"
		self.populationDensity = "population_density"
		self.listOfCities = jsonReader.combineDataSetsFromJsonFiles()
		
	def parseListOfCities(self):
		cities = []
		for city in self.listOfCities:
			city[self.area] = AreaType("Area", city[self.area])
			city[self.populationDensity] = DensityType("Population density", city[self.populationDensity])
			if self.trafficDetails not in city:
				city[self.trafficDetails] = TrafficType()
			else :
				city[self.trafficDetails] = TrafficType(city[self.trafficDetails])
			if self.recreations not in city:
				city[self.recreations] = RecreationType()
			else :
				city[self.recreations] = RecreationType(city[self.recreations])
			cities.append(City(**city))
		return cities
	
		
	def filterCities(self, cities):
		file = open("files/filter/example_filters.json")
		jsonStr = file.read()
		jsonData = json.loads(jsonStr)
		for city in cities:
			filtered = False
			tmpCity = city
			for filters in jsonData["filters"]:
				city = tmpCity
				filters = (filters["path"].split("/")[1:], filters["op"], filters["value"])
				for attributes in filters[0]:
					city = city.__dict__[attributes]
				if(type(city) == type(int()) or type(city) == type(str())):
					if compareValue(filters[1], city, filters[2]):
						filtered = True
						continue
					else:
						filtered = False
						break
				elif city.compareValue(filters[1], filters[2]):
					filtered = True
					continue
				else:
					filtered = False
					break
			city = tmpCity
			if filtered:
				city.displayCity()
	
	