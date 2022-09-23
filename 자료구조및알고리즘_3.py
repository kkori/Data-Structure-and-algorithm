import random

#1번
def ice(graph, i, j):
    if i > n-1 or i <= -1 or j <= -1 or j> m-1:
        return
    if graph[i][j] == 1:
        return
    graph[i][j] = 1
    ice(graph, i-1, j)
    ice(graph, i+1, j)
    ice(graph, i, j-1)
    ice(graph, i, j+1)

#2번
def budget(depart, price):
    result_2 = 0
    depart.sort()
    for i in range(len(depart)):
        if depart[i] <= price:
            price -= depart[i]
            result_2 += 1
        else:
            break
    return print(result_2)




if __name__ == "__main__":
    #1번
    n,m = map(int,input("enter size >> ").split())
    map_ice = []
    for i in range(n):
        map_ice.append(list(map(int,input("0 or 1 >> "))))

    result = 0
    for i in range(n):
        for j in range(m):
            if map_ice[i][j] == 0:
                result += 1
                ice(map_ice, i, j)
    print(result)

    #2번
    depart = [random.randint(1, 20) for i in range(random.randint(1, 10))]
    price = random.randint(1, 40)
    print(f'{depart},{price},', end='')
    budget(depart, price)
