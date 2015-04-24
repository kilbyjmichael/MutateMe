#!/usr/bin/python

'''Uses a basic Genitic Algorithm to find a string,
but this time includes the number of children parents will have'''

import random

TARGET      = "Michael Kilby"
DNA_SIZE    = len(TARGET)
POP_SIZE    = 200
GENERATIONS = 500
KINDER_NUM  = 4
MUTATE_CHANCE = [1,200] # 1 in 100

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
    fittest_fitness = 0

    for generation in range(GENERATIONS):
        weighted_population = []

        # copy from pop to wpop
        for individual in population:
            fitness_num = fitness(individual)
            pair = (individual, fitness_num)
            weighted_population.append(pair)

        pos_winner, score = weighted_population[0]

        # To deal with not fidning one:
        if score >= fittest_fitness:
            fittest_fitness = score
            almost_fit = pos_winner

        # To check for a winner and stop:
        if score is 100:
            print("TARGET found in Gen %s:  %s" % (generation, pos_winner))
            quit(0)
        else:
            print("Generation %s... Random sample: %s : %s" % (generation, pos_winner, score))

        population = [] # Empty the houses for the kids

        # Now parents can have 4 kids
        for _ in range(int(POP_SIZE/KINDER_NUM)):
            # Selection
            for kid in range(KINDER_NUM):
                person1 = weighted_choice(weighted_population)
                person2 = weighted_choice(weighted_population)
                # Mate
                kid = mate(person1, person2)
                # Mutate and add back into the population.
                population.append(mutate(kid))

    # If no other is found:
    print("TARGET not found:")
    print("Fittest String: '%s' at a fitness of %s" % (almost_fit, fittest_fitness))

if __name__ == "__main__": main()
