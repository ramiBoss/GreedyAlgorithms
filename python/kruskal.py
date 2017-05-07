#!/usr/bin/python

# Kruskal's algorithm for finding MST which uses Greedy Technique
import random
class edge:
    def __init__(self, src, des, weight):
        self.src = src
        self.des = des
        self.weight = weight
        return

def checkCycle(edg):
    src = edg.src
    des = edg.des
    while(path[src] > 0):
        src = path[src]

    while(path[des] > 0):
        des = path[des]

    if(src != des):
        path[src] = des
        return 0
    return 1

def kruskal():
    global path
    path = [None]*len(edges)
    edges.sort(key = lambda edge: edge.weight)
    for i in range(len(edges)-1):
        print 'Edge ', edges[i].src, '->', edges[i].des, ' is'
        if(not checkCycle(edges[i])):
            print ' selected'
        else:
            print ' not selected'
    return

def makeGraph():
    global edges
    edges = []
    for i in range(vertex):
        for j in range(vertex):
            if(graph[i][j]):
                newEdge = edge(i, j, graph[i][j])
                edges.append(newEdge)            
    return

def main():
    global graph
    global vertex
    print '1: Enter manually\n 2: Randomize\n'
    choice = raw_input()

    if(int(choice) == 1):
        vertex = raw_input('Number of vertex: ')
        graph = [[0 for x in range(vertex)] for y in range(vertex)]
        print 'Enter the graph matrix: '
        for i in range(vertex):
            for j in range(vertex):
                graph[i][j] = raw_input()
    elif(int(choice) == 2):
        vertex = random.randint(2,3)
        graph = [[0 for x in range(vertex)] for y in range(vertex)]
        for i in range(vertex):
            for j in range(vertex):
                if(i == j):
                    graph[i][j] = 0
                elif(graph[j][i]):
                    graph[i][j] = graph[j][i]                          
                else:
                    graph[i][j] = random.randint(4,20)
    else:
        print 'Wrong Input...............'
        print 'Terminating...............'

    print 'Graph Info: '
    print 'Number of Vertices: ', vertex
    print 'Graph'
    print graph 
    makeGraph()
    kruskal()          
    return

if __name__ == '__main__':
    main()
