#Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
 #This is the 'nester.py' module and it provides one function called print_lol() which prints lists that may or maynot include nested lists."""
#This is the 'nester.py' module and it provides one function called print_lol() which prints lists that may or may not include nested lists."
def print_lol(the_list, level=0):
	#"""This funtion takes one positional argument called "the_list", which is any Python list (of, possibly, nested lists). Each data item in the provided list is (recursively) printed to the screen on its own line."""
		for each_item in the_list:
			if isinstance(each_item, list):
				print_lol(each_item, level+1)
		else:
			for tab_stop in range(level):
				print("\t", end='')
			print(each_item)


# https://python-forum.io/thread-117.html
# https://python-forum.io/thread-5596.html
# http://www.pas.rochester.edu/~rsarkis/csc161/python/execution.html

import nester

movies = [ "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 
			91, ["Graham Chapman", ["Michael Palin", 
			"John Cleese", "Terry Gilliam", "Eric Idle", 
			"Terry Jones"]]]

nester.print_lol(movies, 0)

