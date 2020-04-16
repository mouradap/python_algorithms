"""

Dijkstra is a Shortest Path First (SPF) algorithm that iterates through every
node in a graph, storing where its been and the weight for each connection.
It retrieves useful information about the shortest path by linking a node to its
minimum weight predecessor. So it becomes possible to calculate the shortest path from
node X to node Y.

"""

#First we create a template graph to test our algorithm.

graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},
'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}

#Then we define the dijkstra function that receives the graph,
#a start and an end position (or node).

def dijkstra(graph,start,end):
    #We are storing the shortest distance in a separate dictionary
    shortest_distance = {}

    #And each nodes' predecessor in a separate dictionary
    predecessor = {}

    #Stacking the unseen nodes in the graph
    unseenNodes = graph

    #Setting an infinity value for unvisited nodes
    infinity = float('inf')

    #And creating a list for the resulting shortest path.
    path = []

    #Setting the value of unseen nodes to infinity.
    #Any visited node will have a value lesser than unvisited nodes.
    for node in unseenNodes:
        shortest_distance[node] = infinity
        #print(node)

    #Dijkstra always starts at a position, so the start position weight must be 0.
    shortest_distance[start] = 0

    #Creating a loop for every unseen node.
    while unseenNodes:
    #We do not know what node has a minimal value yet, so we set it to none.
        minNode = None
        
        for node in unseenNodes:
            if minNode is None:
                minNode = node
                #Now we visited the node and we know its weight.

            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

                #If our new node has a lesser value than our previous one, we have a new
                #minimal node.
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
                #print(predecessor)

        #And then we remove the minNode from the stack.
        unseenNodes.pop(minNode)


#Now we're finished with visiting nodes.
#We will start retrieving our path from our end-point to the start-point.
#We need to do this backwards because we will traverse through the predecessors
#with lessr weights.

    currentNode = end
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        #If impossible to traverse the nodes, we raise an error.
        except KeyError:
            print('Path not reachable')
            break

    #Do not forget to include a start node to your path.
    path.insert(0,start)

    if shortest_distance[end] != infinity:
        print('Shortest distance is {}'.format(str(shortest_distance[end])))
        print('And the path is {}'.format(str(path)))


dijkstra(graph, 'a', 'b')