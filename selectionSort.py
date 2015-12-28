def selectionSort(alist):
	a = alist
	for times in range(len(a)-1, 0, -1):
		largest_num_pos = 0
		for place in range(1, times + 1):
			
			if(a[place] > a[largest_num_pos]):
				largest_num_pos = place

		holder = a[times]
		a[times] = a[largest_num_pos]
		a[largest_num_pos] = holder
		
	return a

test = []
for var in range(1, 100):
	number = random.randint(0, 10000)
	test.append(number)


current = int(round(time.time() * 1000))

toPrint = selectionSort(test)
print toPrint


current2 = int(round(time.time() * 1000))


totalTime = current2 - current
print "The code took %d milliseconds to complete" % (totalTime)