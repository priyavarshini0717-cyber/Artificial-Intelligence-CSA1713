import random
def fitness(x):
    return x * x
population = [random.randint(0, 31) for _ in range(6)]
generations = 20
mutation_rate = 0.1
for generation in range(generations):
    population.sort(key=fitness, reverse=True)

    new_population = population[:2]

    while len(new_population) < 6:

        parent1 = random.choice(population[:3])
        parent2 = random.choice(population[:3])

        child = (parent1 + parent2) // 2

        if random.random() < mutation_rate:
            child = random.randint(0, 31)

        new_population.append(child)

    population = new_population

best = max(population, key=fitness)

print("GENETIC ALGORITHM OPTIMIZATION")
print("--------------------------------")
print("Best Solution (x):", best)
print("Maximum Fitness:", fitness(best))
