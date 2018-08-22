def GreedyFindVert(Inc, Init, Dest, Sum=0, k=None): # Find a vert with the best way
	# First execution
	if(k == None):
		print("\nGreedy Find Vert")
		k = Init

	if(Dest == k):
		print("Vert founded!")
		return

	# Searching for de minimal edge
	l = Inc[k]
	Min = 0
	i = None
	for j in range(0,len(l)):
		if(l[j] > 0):
			if(Min == 0):
				Min = l[j]
				i = j
			elif(Min > 0 and l[j] < Min):
				Min = l[j]
				i = j

	# Don't have edges to go
	if(i == None):
		print("End of line!")
		return

	# Searching for the next vert
	for j in range(0,len(Inc)):
		if(Inc[j][i] < Min and Inc[j][i] < 0):
			break
			
	Sum += Min
	print("Vert:", k+1, "Next vert:", j+1, "Lowest edge:", Min, "Edges sum:", Sum)
	GreedyFindVert(Inc, Init, Dest, Sum, j)
