__author__ = "Andrew M. Silva and Estela M. Vilas Boas"
from ReadGraph import *
from GreedyGoThrough import *
from GreedyFindVert import *

Adj, Inc, Init, Dest = ReadGraph()
GreedyGoThrough(Adj, Init)
GreedyFindVert(Inc, Init, Dest)
