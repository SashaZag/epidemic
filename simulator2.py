import random
def simulate(nodes_number,iterations, x=4):
	success = 0
	

	for n in range(iterations):
		node_list = [0] * nodes_number
		node_list[0] = 1

		for a in range(nodes_number):
			#if node_list[a] == 1:
			for i in random.sample(range(nodes_number), x):
				#print(node_list)
				if node_list[i] <= 1:
					node_list[i] += 1


		#print(node_list)
		if all(node_list):
			success += 1


	result = "{percents}%".format(percents=100*success/iterations)
	print(result)

simulate(20, 1000)