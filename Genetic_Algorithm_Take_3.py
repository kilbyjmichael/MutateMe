#!/usr/bin/python

'''Mates colors!'''

import random
from PIL import Image

IMG_SIZE = (250,250)
IMG_MODE = 'RGB'
WHITE = '#FFFFFF'
BLACK = '#000000'
MAX_RGB = 255

TARGET      = [137,22,88]
DNA_SIZE    = 3
POP_SIZE    = 200
GENERATIONS = 500
MUTATE_CHANCE = [1,200] # 1 in 100

def random_color():
  # Return a random color value
  color = int(random.randrange(0, MAX_RGB, 1))
  return color

def make_population():
    # Returns a list of POP_SIZE strings.
    population = []
    for x in range(POP_SIZE):
        dna = [0,0,0]
        for x in range(DNA_SIZE):
            dna[x] = random_color()
        population.append(dna)
    return population

def mutate(dna_sample):
    # Use MUTATE_CHANCE to create randomness in population
    dna = []
    for color in dna_sample:
        if int(random.random()*(MUTATE_CHANCE[1]/MUTATE_CHANCE[0])) == 1:
            dna.append(random_color())
        else:
            dna.append(color)
    return dna

def fitness(dna):
    # Calculate the difference between a character in the same position in the TARGET string.
     fitness = 0
     for i in range(3):
         fitness += (abs(dna[i] + TARGET[i]) / TARGET[i]) * 10
     return fitness

def mate(mother, father):
    zygote = list(zip(mother, father))
    child = []
    for dna in zygote:
        child.append(dna[random.randrange(2)])
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
        if pos_winner is TARGET:
            print("TARGET found in Gen %s:  %s" % (generation, pos_winner))
            quit(0)
        else:
            print("Generation %s... Random sample: %s : %s" % (generation, pos_winner, score))

        population = [] # Empty the houses for the kids

        # fill pop back up by mating all of them
        for _ in range(int(POP_SIZE/2)):
          # Selection
          person1 = weighted_choice(weighted_population)
          person2 = weighted_choice(weighted_population)

          # Mate
          kid1 = mate(person1, person2)

          # Mutate and add back into the population.
          population.append(mutate(kid1))

    # If no other is found:
    print("TARGET not found:")
    print("Fittest String: '%s' at a fitness of %s" % (almost_fit, fittest_fitness))

if __name__ == "__main__": main()
