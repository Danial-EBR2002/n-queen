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

def tournament_selection(population, fitnesses, k=5):
    selected = random.sample(list(zip(population, fitnesses)), k)
    selected.sort(key=lambda x: x[1], reverse=True)
    return selected[0][0]

def crossover(p1, p2):
    n = len(p1)
    point = random.randint(1, n - 2)
    child = p1[:point] + [gene for gene in p2 if gene not in p1[:point]]
    return child

def mutate(chromosome, mutation_rate=0.05):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

def adaptive_mutation(generation, max_generations):
    return max(0.01, 0.2 * (1 - generation / max_generations))

def evolve_population(population, fitnesses, generation, max_generations, elite_count=2):
    # Sort by fitness descending
    sorted_pop = [x for _, x in sorted(zip(fitnesses, population), reverse=True)]
    elites = sorted_pop[:elite_count]

    new_population = elites.copy()
    while len(new_population) < len(population):
        p1 = tournament_selection(population, fitnesses)
        p2 = tournament_selection(population, fitnesses)
        child = crossover(p1, p2)
        mutation_rate = adaptive_mutation(generation, max_generations)
        child = mutate(child, mutation_rate)
        new_population.append(child)
    return new_population

def genetic_n_queens_stage3(n=8, generations=1000, pop_size=100):
    population = create_population(pop_size, n)
    max_fitness = n * (n - 1) // 2

    for gen in range(generations):
        fitnesses = [fitness(ind) for ind in population]
        if max(fitnesses) == max_fitness:
            best = population[fitnesses.index(max_fitness)]
            print(f"Solution found at generation {gen}: {best}")
            return best

        population = evolve_population(population, fitnesses, gen, generations)

    best = max(population, key=fitness)
    print("Best solution after", generations, "generations:", best, "Fitness:", fitness(best))
    return best

if __name__ == "__main__":
    genetic_n_queens_stage3()
