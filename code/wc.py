def linecount(filename):
	count = 0
	for line in open(filename):
		count += 1
	return count

# Below is how to stop a module running on import
if __name__ == '__main__':
	print linecount('wc.py')
	
