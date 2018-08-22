def ReadGraph(): # Read a graph like a adjacency and incidency
	n = int(input()) # Number of verts
	a = int(input()) # Number of edges

	Init = int(input())
	Dest = int(input())

	# Read adjacency matrix
	Adj = []
	for i in range(0,n):
		l = [int(x) for x in input().split()] # Read line
		if(len(l) != n): # Matrix need to be n*n
			print("Wrong input!")
			exit()
		Adj.append(l)

	# Read incidency matrix
	Inc = []
	for i in range(0,n):
		l = [int(x) for x in input().split()] # Read line
		if(len(l) != a): # Matriz need to be n*a
			print("Wrong input!")
			exit()
		Inc.append(l)

	return Adj, Inc, Init, Dest
