import unittest
import json
from JsonReader import JsonReader

class TestJsonReader(unittest.TestCase):
	def setUp(self):
		self.jsonReader = JsonReader()
		self.jsonReader.dir = "testFiles"

	def test_getValidJson(self):
		str = '{key}'
		self.assertEqual(self.jsonReader.getValidJson(str), None)
		str = '{"key": 2}'
		self.assertEqual(self.jsonReader.getValidJson(str), json.loads(str))
		
	def test_readJsonFiles(self):
		self.jsonReader.dir = "testFiles/1"
		self.assertEqual(self.jsonReader.readJsonFiles(), [])
		self.jsonReader.dir = "testFiles/2"
		self.assertEqual(self.jsonReader.readJsonFiles(), [])
		self.jsonReader.dir = "testFiles/3"
		self.assertEqual(self.jsonReader.readJsonFiles(), [{"key" : 2}])
		
	def test_combineDataSetsFromJsonFiles(self):
		self.jsonReader.dir = "testFiles/3"
		self.assertEqual(self.jsonReader.combineDataSetsFromJsonFiles(), [])
		self.jsonReader.dir = "testFiles/4"
		self.assertEqual(self.jsonReader.combineDataSetsFromJsonFiles(), [{"city" : "Gdańsk"}, {"city" : "Gdynia"}, {"city" : "Warszawa"}])
	
if __name__ == "__main__":
	unittest.main()