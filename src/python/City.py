import re
import datetime
import JsonReader as jr
from Scalar import TimeType
from Scalar import SpeedType
from Scalar import PercentageType

class City:
	def __init__(self, **cities):
		self.__dict__.update(cities)
		
	def displayCity(self):
		print("City: {}, Country: {}, Voivodeship: {}".format(self.city, self.country, self.voivodeship))
		self.area.displayScalar()
		print("\tPopulation: ", self.population)
		self.population_density.displayScalar()
		self.recreations.displayRecreationInfo()
		self.traffic_details.displayTrafficInfo()
		print(66 * "-")
		
class RecreationType:
	def __init__(self, recreations = dict()):
		try:
			self.parks = PercentageType("Parks", int(recreations["parks"]))
			self.woods = PercentageType("Woods", int(recreations["woods"]))
		except (KeyError, ValueError):
			self.parks = PercentageType("Parks", "no info", "")
			self.woods = PercentageType("Woods", "no info", "")
			
	def displayRecreationInfo(self):
		print("RecreationInfo")
		self.parks.displayScalar()
		self.woods.displayScalar()

class TrafficType:
	peakTime = "traffic_peak_time"
	averageSpeed = "average_speed"
	def __init__(self, traffics = dict()):
		try:
			startTime = str(traffics[self.peakTime]["start"])
			endTime = str(traffics[self.peakTime]["end"])
			self.averageSpeed = SpeedType("Speed", int(traffics[self.averageSpeed]))
			if self.checkIfTimesAreCorrect(startTime, endTime):
				self.timeSpan = TimeSpanType(startTime, endTime)
			else:
				self.timeSpan = TimeSpanType("no info", "no info")
		except (KeyError, ValueError):
			self.timeSpan = TimeSpanType("no info", "no info")
			self.averageSpeed = SpeedType("Speed", "no info", "")

	def checkIfTimesAreCorrect(self, startTime, endTime):
		start = re.search("^((\\d\\d)|\\d):\\d\\d$", startTime)
		if start:
			end = re.search("^((\\d\\d)|\\d):\\d\\d$", endTime)
			if end:
				dStart = datetime.datetime.strptime(startTime,'%H:%M')
				dEnd = datetime.datetime.strptime(endTime,'%H:%M')
				if dStart < dEnd:
					return True
		return False
			
	def displayTrafficInfo(self):
		print("Traffic info")
		self.timeSpan.displayTime()
		self.averageSpeed.displayScalar()
		
		
class TimeSpanType:
	def __init__(self, startTime, endTime):
		self.start = TimeType("From", startTime)
		self.end = TimeType("To", endTime)
		
	def displayTime(self):
		self.start.displayScalar()
		self.end.displayScalar()
	