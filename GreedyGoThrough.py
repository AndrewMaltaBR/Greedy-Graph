def GreedyGoThrough(Adj, Init, Sum=0, k=None, S=[]): # Go through the graph completely
	# First execution
	if(k == None):
		print("\nGreedy Go Through")
		k = Init

	S.append(k)
	if(len(S) == len(Adj)): # "This vert is done!"
		print("Done!")
		return

	# Searching for de minimal edge
	l = Adj[k]
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

	Sum += Min
	print("Vert:", k+1, "Next vert:", i+1, "Lowest edge:", Min, "Edges sum:", Sum)
	GreedyGoThrough(Adj, Init, Sum, i, S)
