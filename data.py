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

def get_lottery_numbers(URL):
	"""takes in URL, uses parse_data to return a list (size 1000) of list of winning numbers"""
	# """Returns an array of the frequency of each number in the lottery"""
	thelist = get_lottery_data(URL)
	win_numbers = []
	for element in thelist:
		win_numbers.append(element['winning_numbers'])
	finallst = parse_data(win_numbers)
	return finallst

def how_many_entries(URL):
	"""should always return 1000, for number of entries"""
	return len(get_lottery_numbers(URL))

def get_mega_numbers(URL):
	"""Returns an array of mega numbers"""
	result=[];
	data=get_lottery_data(URL)
	for e in data:
		result.append(int (e["mega_ball"]))
	return result

def parse_string_to_listint(string):
	"""takes in string and converts to int (hardcoded) This is the helper method for parse_data."""
	length = len(string)
	newlist = []
	first = int (string[0] + string[1])
	second = int (string[3] + string[4])
	third = int (string[6] + string[7])
	forth = int (string[9] + string[10])
	fifth = int (string[12] + string[13])
	newlist.append(first)
	newlist.append(second)
	newlist.append(third)
	newlist.append(forth)
	newlist.append(fifth)
	return newlist

def parse_data(lst):
	"""takes in list of strings (result from get_lottery_numbers),
		returns list of list of integers."""
	finallist = []
	for element in lst:
		finallist.append(parse_string_to_listint(element))
	return finallist


def probability(lottery_array):
	"""Takes in a tuple where lottery_array[0] is an array of 5 get_array_of_numbers
		and lottery_array[1] is the mega number"""
	return 0

def random_lottery():
	"""Retursn a tuple of which the first element is an array of 5 random,
		non duplicate numbers, and the second element is a mega number"""
	return 0



