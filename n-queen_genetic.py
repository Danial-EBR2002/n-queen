import random

def fitness(chromosome):
    score = 0
    n = len(chromosome)
    for i in range(n):
        for j in range(i+1, n):
            if chromosome[i] != chromosome[j] and abs(chromosome[i] - chromosome[j]) != abs(i - j):
                score += 1
    return score

def random_chromosome(n):
    return random.sample(range(n), n)

def mutate(chromosome):
    i, j = random.sample(range(len(chromosome)), 2)
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

def crossover(p1, p2):
    cut = random.randint(1, len(p1)-1)
    return p1[:cut] + p2[cut:]

def very_simple_genetic(n=8, pop_size=20, generations=100):
    population = [random_chromosome(n) for _ in range(pop_size)]

    for _ in range(generations):
        new_population = []
        for _ in range(pop_size):
            p1 = random.choice(population)
            p2 = random.choice(population)
            child = crossover(p1, p2)
            if random.random() < 0.5:
                child = mutate(child)
            new_population.append(child)
        population = new_population

    # Print best
    best = max(population, key=fitness)
    print("Best:", best)

if __name__ == "__main__":
    very_simple_genetic()
