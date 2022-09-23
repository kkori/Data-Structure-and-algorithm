# 문제1

def bag(capacity, n):
    if capacity == 0 or n == 0:
        return 0
    if thing_w[n-1] > capacity:
        return bag(capacity, n-1)
    else:
        return max(thing_v[n-1] + bag(capacity-thing_w[n-1], n-1), bag(capacity, n-1))

# 문제2

import random
import datetime
import numpy as np


def gen_parent(length):
    genes =[]
    while len(genes)<length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)

def get_fitness(guess):
    return sum(1 for expected, actual in zip(target, guess) if expected==actual)

def mutate(parent):
    index = random.randrange(0,len(parent))
    childGenes=list(parent)
    newGene,alternate=random.sample(geneSet,2)
    if newGene==childGenes[index]:
        childGenes[index]=alternate
    else:
        childGenes[index]=newGene
    return ''.join(childGenes)

def display(guess):
    timeDiff = datetime.datetime.now()-startTime
    fitness = get_fitness(guess)
    print("{}\t{}\t{}".format(guess,fitness,timeDiff))


def s_crossover(a, b, x):
    a_cross = np.append(a[:x], b[x:])
    b_cross = np.append(b[:x], a[x:])
    return a_cross, b_cross

def crossover(parent):
    bestParent_list = list()
    for i in range(0, 10):
        parent = gen_parent(len(target))
        bestParent_list.append(parent)
    sp_Parents = random.sample(bestParent_list, 2)

    A = np.array(list(sp_Parents[0]))
    B = np.array(list(sp_Parents[1]))

    X = random.sample(range(0, len(target)), k=2)
    for i in X:
        A, B = s_crossover(A, B, i)

    A = ''.join(A)
    B = ''.join(B)

    if get_fitness(A) >= get_fitness(B):
        return A
    else:
        return B


if __name__ == "__main__":

    # 문제1
    n = int(input("보석의 수를 입력하시오 >> "))
    capacity = int(input("배낭의 용량을 입력하시오 >> "))
    thing_w = list(map(int, input("보석의 무게를 입력하시오 >> ").split()))
    thing_v = list(map(int, input("보석의 가치를 입력하시오 >> ").split()))
    print(bag(capacity, n))

    # 문제2
    geneSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    target = "Hello World!"

    random.seed()
    startTime = datetime.datetime.now()
    bestParent = gen_parent(len(target)); bestFitness=get_fitness(bestParent)
    display(bestParent)


    # mutate
    num = 0
    while True:
        child = mutate(bestParent)
        num += 1
        if num == 9:
            break
        childFitness = get_fitness(child)
        if bestFitness >= childFitness:
            continue
        display(child)
        if childFitness >= len(bestParent):
            break
        bestFitness = childFitness
        bestParent = child

    # crossover
    while True:
        child = crossover(bestParent)
        childFitness = get_fitness(child)
        if bestFitness >= childFitness:
            continue
        display(child)
        if childFitness >= len(bestParent):
            break
        bestFitness = childFitness
        bestParent = child