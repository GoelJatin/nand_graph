Output
======

Input String: !(3.5).!(!(1.2).3)


	14.!(!(1.2).3)

	14.!(15.3)

	14.12

	 12 

Graph Instance: 
Instance of the Graph class with nodes: [{Node: [3], Node: [1], Node: [2], Node: [5], Node: [12], Node: [15], Node: [14]}]

Edges:
	Node: [3]	-->	Node: [5]
	Node: [5]	-->	No Edges
	Node: [14]	-->	No Edges
	Node: [1]	-->	Node: [2]
	Node: [2]	-->	No Edges
	Node: [15]	-->	Node: [3]
	Node: [12]	-->	No Edges

Output:  12 


Input String: !(!(3.5).10).!(!(102.256).335)


	!(14.10).!(!(102.256).335)

	5.!(!(102.256).335)

	5.!(15.335)

	5.240

	 0 

Graph Instance: 
Instance of the Graph class with nodes: [{Node: [15], Node: [10], Node: [14], Node: [102], Node: [256], Node: [3], Node: [5], Node: [335], Node: [240]}]

Edges:
	Node: [3]	-->	Node: [5]
	Node: [5]	-->	No Edges
	Node: [14]	-->	Node: [10]
	Node: [10]	-->	No Edges
	Node: [102]	-->	Node: [256]
	Node: [256]	-->	No Edges
	Node: [15]	-->	Node: [335]
	Node: [335]	-->	No Edges
	Node: [240]	-->	No Edges

Output:  0 


