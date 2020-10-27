# Test DuckDuckGo
# 
# test_duckduckgo.py
# 
# ***
# 
# By Jeremiah Thomas
# 
# ***
# 
# Created 2020-10-26
# 
# +++
# Description
# 
# A standalone pytest module for directly testing the instant answers feature of DuckDuckGo.
# 
# +++
# Dedication
# 
# CSC 256-0001
# 

# 
# +++
# Imports
# 
import pytest
import requests
# 
# +++
# Assignments
# 
# ===
# Constants
# 
PRESIDENTS = \
	[ # Last names only, excluding duplicates; it is a list instead of a set to preserve the order
	'Washington',
	'Adams',
	'Jefferson',
	'Madison',
	'Monroe',
	'Jackson',
	'Van Buren',
	'Harrison',
	'Tyler',
	'Polk',
	'Taylor',
	'Fillmore',
	'Pierce',
	'Buchanan',
	'Lincoln',
	'Johnson',
	'Grant',
	'Hayes',
	'Garfield',
	'Arthur',
	'Cleveland',
	'McKinley',
	'Roosevelt',
	'Taft',
	'Wilson',
	'Harding',
	'Coolidge',
	'Hoover',
	'Truman',
	'Eisenhower',
	'Kennedy',
	'Nixon',
	'Ford',
	'Carter',
	'Reagan',
	'Bush',
	'Clinton',
	'Obama',
	'Trump',
	]
# 
# +++
# Functions
# 
# ===
# Definitions
# 
# ---
# Create President Sublist
# 
def create_president_sublist(president_list):
	'''
	Create a list of president names found in a DuckDuckGo search.

	**president_list**: list of str (full list of president names for comparison)

	Return president_sublist: list of str (subset of president names found in the search results)
	'''

	SEARCH = 'presidents+of+the+united+states'
	president_sublist = []

	for name in president_list:
		for object in read_duckduckgo(SEARCH)['RelatedTopics']:
			if name in object['Text']:
				president_sublist.append(name)
				break # Prevent duplicates

	return president_sublist
# 
# ---
# Read DuckDuckGo
# 
def read_duckduckgo(search):
	'''
	Read the JSON-formatted results of an arbitrary DuckDuckGo search.

	**search**: str (percent-encoded, plus-sign-separated search terms)

	Return dict (JSON object of results)
	'''

	return requests.get(f'https://duckduckgo.com/?q={search}&format=json').json()
# 
# ---
# President Sublist
# 
@pytest.fixture(scope = 'session')
def president_sublist():
	'''
	Wrap """create_president_sublist()""" for pytest fixturization.

	Return func (called only once per test session)
	'''

	return create_president_sublist(PRESIDENTS)
# 
# ---
# Test Create President Sublist
# 
@pytest.mark.parametrize('args', PRESIDENTS)
def test_create_president_sublist(president_sublist, args):
	'''
	Test function to ensure all president names are captured.

	**president_sublist**: func (fixture calling """create_president_sublist()""")
	**args**: list of str (list of president names passes as parameters)

	No returns
	'''

	for name in PRESIDENTS:
		assert name in president_sublist
# 
# +++
# Output
# 
# ===
# Main
# 
def main():

	print(create_president_sublist(PRESIDENTS))
# 
# ===
# Init
# 
if __name__ == '__main__': 
	main()