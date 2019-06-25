def consecutive_combo(lst1, lst2):
    """ Checks whether 2 lists of unique integer elements combine to make a 
    consecutive list. If the list is continous, last element - first + 1 is 
    the number of elements. """
	combined = lst1
	combined.extend(lst2)
	combined.sort()
	return combined[-1] - combined[0] + 1 == len(lst1)
