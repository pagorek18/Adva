import re

def compareValue(operator, value, value2):
	if operator == "eq":
		return value == value2
	elif operator == "gt":
		return value > value2
	elif operator == "lt":
		return value < value2
	elif operator == "ge":
		return value >= value2
	elif operator == "le":
		return value <= value2
	elif operator == "in":
		return value >= value2[0] and value <= value2[1]
	elif operator == "re":
		result = re.search(value2, value)
		if result:
			return True
		else:
			return False
	return False

class Scalar:
	def __init__(self, name, value, unit = ""):
		self.name = name
		self.value = value
		self.unit = unit
		
	def compareValue(self, operator, value):
		return compareValue(operator, self.value, value)
		
	def displayScalar(self):
		scalarOutput = "\t{}: {} {}"
		print(scalarOutput.format(self.name, self.value, self.unit))
		
class AreaType(Scalar):
	def __init__(self, name, value, unit = "km^2"):
		Scalar.__init__(self, name, value, unit)
		
class DensityType(Scalar):
	def __init__(self, name, value, unit = "person/km^2"):
		Scalar.__init__(self, name, value, unit)
		
class PercentageType(Scalar):
	def __init__(self, name, value, unit = "%"):
		Scalar.__init__(self, name, value, unit)
		
class SpeedType(Scalar):
	def __init__(self, name, value, unit = "km/h"):
		Scalar.__init__(self, name, value, unit)
		
class TimeType(Scalar):
	def __init__(self, name, value):
		Scalar.__init__(self, name, value)