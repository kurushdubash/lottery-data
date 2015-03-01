import requests

# api ask a server for data and it will give you that data.
# api's are usually URLs. 

#URL : https://data.ny.gov/resource/d6yy-54nr.json

nysixnum = "https://data.ny.gov/resource/d6yy-54nr.json"
nyfivemeg = "https://data.ny.gov/resource/5xaw-6ayf.json"



def get_lottery_data(URL):
	"""Returns data (which is list of dictionaries) for Lottery"""
	data = requests.get(URL) #one bigass list where each item is a dictionary. 
	data = data.json() #from object to dictionary
	return data

def get_lottery_numbers():
	"""Returns an array of the frequency of each number in the lottery"""
	return 0

def get_mega_numbers():
	"""Returns an array of mega numbers"""
	return 0

def parse_data(data):
	return 0

def probability(lottery_array):
	"""Takes in a tuple where lottery_array[0] is an array of 5 get_array_of_numbers
		and lottery_array[1] is the mega number"""
	return 0

def random_lottery():
	"""Retursn a tuple of which the first element is an array of 5 random,
		non duplicate numbers, and the second element is a mega number"""
	return 0



