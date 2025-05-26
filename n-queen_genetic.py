import random

def fitness(chromosome):
    n = len(chromosome)
    score = 0
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] != chromosome[j] and abs(chromosome[i] - chromosome[j]) != abs(i - j):
                score += 1
    return score

def create_population(size, n):
    return [random.sample(range(n), n) for _ in range(size)]

def roulette_selection(population, fitnesses):
    total = sum(fitnesses)
    pick = random.uniform(0, total)
    current = 0
    for ind, fit in zip(population, fitnesses):
        current += fit
        if current > pick:
            return ind
    return population[-1]

def crossover(p1, p2):
    n = len(p1)
    point = random.randint(1, n - 2)
    child = p1[:point] + [gene for gene in p2 if gene not in p1[:point]]
    return child

def mutate(chromosome, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

def genetic_n_queens_stage2(n=8, pop_size=50, generations=500, elite_count=1):
    population = create_population(pop_size, n)
    max_fitness = n * (n - 1) // 2

    for gen in range(generations):
        fitnesses = [fitness(ind) for ind in population]
        sorted_pop = [x for _, x in sorted(zip(fitnesses, population), reverse=True)]
        new_population = sorted_pop[:elite_count]

        while len(new_population) < pop_size:
            p1 = roulette_selection(population, fitnesses)
            p2 = roulette_selection(population, fitnesses)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    best = max(population, key=fitness)
    print("Best solution after", generations, "generations:", best, "Fitness:", fitness(best))

if __name__ == "__main__":
    genetic_n_queens_stage2()
