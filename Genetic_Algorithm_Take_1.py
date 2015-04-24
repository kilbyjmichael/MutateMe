#!/usr/bin/python

import random

TARGET      = "Michael Kilby"
DNA_SIZE    = len(TARGET)
POP_SIZE    = 1000
GENERATIONS = 1000
MUTATE_CHANCE = [1,100] # 1 in 100

def random_char():
  # Return a random character between ASCII 32 and 126
  return chr(int(random.randrange(32, 126, 1)))

def make_population():
    # Returns a list of POP_SIZE strings.
    population = []
    for x in range(POP_SIZE):
        dna = ''
        for char in range(DNA_SIZE):
            dna += random_char()
        population.append(dna)
    return population

def mutate(dna_sample):
    dna_sample = str(dna_sample)
    # Use MUTATE_CHANCE to create randomness in population
    dna = ''
    for char in dna_sample:
        if int(random.random()*(MUTATE_CHANCE[1]/MUTATE_CHANCE[0])) == 1:
            dna += random_char()
        else:
            dna += char
    return dna

def fitness(dna):
    # Calculate the difference between a character in the same position in the TARGET string.
    # fitness = 0
    correct_chars = 0
    for dna_chr, tar_chr in zip(dna, TARGET):
        if dna_chr is tar_chr:
            correct_chars += 1
        else:
            pass
    correct_chars = correct_chars * 100
    return correct_chars/DNA_SIZE

def mate(mother, father):
    zygote = list(zip(mother, father))
    child = ''
    for dna in zygote:
        child += dna[random.randrange(2)]
    return child

def weighted_choice(items):
    """
    Chooses a random element from items, where items is a list of tuples in
    the form (item, weight). weight determines the probability of choosing its
    respective item. Note: this function is borrowed from ActiveState Recipes.
    """
    weight_total = sum((item[1] for item in items))
    n = random.uniform(0, weight_total)
    for item, weight in items:
      if n < weight:
        return item
      n = n - weight
    return item

def main():
    # Make an initial population
    population = make_population()

    for generation in range(GENERATIONS):
        weighted_population = []

        # copy from pop to wpop
        for individual in population:
            fitness_num = fitness(individual)
            pair = (individual, fitness_num)
            weighted_population.append(pair)

        print("Generation %s... Random sample: %s" % (generation, weighted_population[0]))

        population = [] # Empty the houses for the kids

        # fill pop back up by mating all of them
        for _ in range(int(POP_SIZE)):
          # Selection
          person1 = weighted_choice(weighted_population)
          person2 = weighted_choice(weighted_population)
          person3 = weighted_choice(weighted_population)
          person4 = weighted_choice(weighted_population)

          # Crossover
          kid1 = mate(person1, person2)
          kid2 = mate(person3, person4)
          # Mutate and add back into the population.
          population.append(mutate(kid1))
          population.append(mutate(kid2))
          #print (person1)
          #print (person2 + ":")
          #print (kid + "\n")

    fittest_string = population[0]
    minimum_fitness = fitness(population[0])

    for individual in population:
        ind_fitness = fitness(individual)
        if ind_fitness <= minimum_fitness:
            fittest_string = individual
            minimum_fitness = ind_fitness
    print("Fittest String: %s" % fittest_string)

if __name__ == "__main__": main()
