import dis

def mindist(sptSet, dist):
    min_index = 0
    d_min = 1000000
    for n in range(nodes):
        if((not sptSet) and dist[n] <= d_min):
            d_min = dist[n]
            min_index = n
    return min_index

def printdistance(dist):
    for i in range(nodes):
        print i, ' ', dist[i]
        return

def dijkstralgo(src):
    dist = [1000000]*nodes
    sptSet = [False]*nodes
    dist[src] = 0
    for i in range(1, nodes):
        u = mindist()
        sptSet[u] = True
        for v in range(nodes):
            if(not sptSet[v]):
                if(graph[u][v] != 0 and dist[i] != 1000000 and dist[u]+graph[u][v] < dist[v]):
                    dist[v] = dist[u] + graph[u][v]

        printdistance()           
    return


def main():
    global nodes
    nodes=raw_input('Enter the number of nodes')
    global graph
    graph = [[0 for x in range(nodes)] for y in range(nodes)]
    print 'Enter the distance between nodes\t Enter 0 if not connected\n'

    for i in range(nodes):
        for j in range(nodes):
            if( i == j):
                graph[i][j] = 0
                continue
            else:
                print i, '->', j, ': '
                graph[i][j] = int(raw_input())
    src = raw_input('Enter the source vertex')
    dijkstralgo(src)
    return

if __name__ == "__main__":
    main()
