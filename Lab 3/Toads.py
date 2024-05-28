import random


class Toad:
    def __init__(self, is_trustworthy):
        self.truthful: bool = (int(is_trustworthy))

    def is_trustworthy(self):
        return self.truthful

    def tell_about(self, toad):
        b_trustworthy = toad.is_trustworthy()
        if (self.is_trustworthy()):
            return b_trustworthy
        else:
            r = random.random()
            if (r < 0.5):
                return True
            else:
                return False

def getPopulation(n):
    toadList = []
    for i in range(n):
        trust = input("Enter your trust issues: ")
        toad = Toad(trust)
        toadList.append(toad)
    return toadList

def TruthFulToadsA(population):
    truthfulToads = []
    for i in range(len(population)):
        check = True
        for j in range(len(population)):
            if population[i].tell_about(population[j]) != population[j].is_trustworthy():
                check = False
                break
        if(check == True):
            truthfulToads.append(i)

    return truthfulToads

def TruthFulToadsB(population):
    truthfulToads = []
    for i in range(len(population)):
        check = True
        for j in range(len(population)):
            if population[i].tell_about(population[j]) != population[j].is_trustworthy():
                check = False
                break
        if(check == True):
            truthfulToads.append(i)

    return truthfulToads

n = input("Enter number of Toads ")
population = getPopulation(int(n))

print(TruthFulToadsA(population))
