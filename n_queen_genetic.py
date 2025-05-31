
import random

def fitness(chromosome):
    n = len(chromosome)
    non_attacking = 0
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] != chromosome[j] and abs(chromosome[i] - chromosome[j]) != abs(i - j):
                non_attacking += 1
    return non_attacking

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

def adaptive_mutation(generation, max_generations):
    return max(0.01, 0.2 * (1 - generation / max_generations))

def evolve_population(population, fitnesses, generation, max_generations, elite_count=2):
    sorted_pop = [x for _, x in sorted(zip(fitnesses, population), reverse=True)]
    elites = sorted_pop[:elite_count]

    new_population = elites.copy()
    while len(new_population) < len(population):
        p1 = tournament_selection(population, fitnesses)
        p2 = tournament_selection(population, fitnesses)
        child = crossover(p1, p2)
        mutation_rate = adaptive_mutation(generation, max_generations)
        mutate(child, mutation_rate)
        new_population.append(child)
    return new_population

def solve_n_queens_genetic(n, max_generations=1000, population_size=100):
    population = create_population(population_size, n)
    max_fitness = n * (n - 1) // 2

    for generation in range(max_generations):
        fitnesses = [fitness(ind) for ind in population]
        if max(fitnesses) == max_fitness:
            best = population[fitnesses.index(max(fitnesses))]
            print(f"Solution found at generation {generation}: {best}")
            return best

        population = evolve_population(population, fitnesses, generation, max_generations)

    print("No solution found.")
    return None

# Test mode
if __name__ == "__main__":
    solve_n_queens_genetic(8)
