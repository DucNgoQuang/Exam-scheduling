import random
# N classes and m rooms
n , m = list(map(int,input().split()))
# number of students in each class
d = list(map(int,input().split()))
# capacity of each room
c = list(map(int,input().split()))
#number of pairs of classes
k = int(input())
# time slot for class index i 
slot = [None] * n
# room for class index i
r = [None] * n
Conflict_classes = list()
def feasible_class(c):
    class_satisfied = []
    for room in c :
        flag = []
        for i in range (n) :
            if room >= d[i] : #check if whether a class can be in a room
                flag.append(i)
        class_satisfied.append(flag)
    return class_satisfied
class_satisfied = feasible_class(c)
f = [len(i) for i in class_satisfied]
a = min(f)
max_slot = 4
population_size = n
number_of_elite_schedules = 2
tournament_selection_size = 7
mutation_rate = 0.4
for i in range (k):
    Conflict_classes.append(list(map(int,input().split())))
for pair in Conflict_classes :
    pair[0],pair[1] = pair[0] -1 , pair[1] -1 
for i in range (n):
    slot[i] = random.randint(1,max_slot)
    r[i] = random.randint(0,m-1)
def no_of_conflict(slot,r):
    global c ,d , Conflict_classes
    violation = 0 
    for i in range (n):
        if c[r[i]] < d[i] : # capacity constraint
            violation += 1  
    for (i,j) in Conflict_classes: # conflict classes
        if slot[i] == slot[j]:
            violation += 1 
    for i in range (n): # same slot same class
        for j in range (i+1,n):
            if slot[i] == slot[j] and r[i] == r[j]:
                violation += 1
    return violation
def random_schedule():
    flag_slot =  [None] * n
    flag_room = [None] * n
    for j in range (n):
        flag_slot[j] = random.randint(1,max_slot)
        flag_room[j] = random.randint(0,m-1)
    return [flag_slot,flag_room]
def population(population_size):
    population = []
    for i in range (population_size):
        flag_slot =  [None] * n
        flag_room = [None] * n
        for j in range (n):
            flag_slot[j] = random.randint(1,max_slot)
            flag_room[j] = random.randint(0,m-1)
        population.append([flag_slot,flag_room])
    return population
def fitness(slot,room):
    return 1/(1.0 * no_of_conflict(slot,room) +1)
def fitness_popultion(population):
    fit = []
    for (slot,room) in population:
        res = fitness(slot,room)
        fit.append(res)
    fit.sort
    return fit
def fitness_individual(individual):
    return fitness(individual[0],individual[1])
p = population(population_size)
p.sort(key = fitness_individual,reverse=True)
def crossover_shcedule(schedule1,schedule2):
    crossoverSchedule = [[],[]]
    for i in range (n):
        if random.random() > 0.5:
            crossoverSchedule[0].append(schedule1[0][i])
            crossoverSchedule[1].append(schedule1[1][i])
        else:
            crossoverSchedule[0].append(schedule2[0][i])
            crossoverSchedule[1].append(schedule2[1][i])
    return crossoverSchedule
def mutate_schedule(mutate_schedule):
    schedule = random_schedule()
    for i in range (n):
        if mutation_rate > random.random():
            mutate_schedule[0][i] = schedule[0][i]
            mutate_schedule[1][i] = schedule[1][i]
    return mutate_schedule
def select_tournament(population):
    global tournament_selection_size
    tournament_pop = []
    i = 0 
    while i < tournament_selection_size:
        tournament_pop.append(random.choice(population))
        i+= 1
    tournament_pop.sort(key = fitness_individual,reverse=True)
    return tournament_pop
def crossover_population(population):
    global population_size,number_of_elite_schedules
    crossover_pop  = []
    for i in range (number_of_elite_schedules):
        crossover_pop.append(population[i])
    i = number_of_elite_schedules
    while i < population_size:
        schedule_1  = select_tournament(population)[0] #best individual in the tournament 
        schedule_2  =  select_tournament(population)[0]
        crossover_pop.append(crossover_shcedule(schedule_1,schedule_2))
        i += 1
    return crossover_pop
def mutate_population(population):
    global number_of_elite_schedules,population_size
    for i in range (number_of_elite_schedules,population_size):
        population[i] = mutate_schedule(population[i])
    return population
def evolve(population):
    return mutate_population(crossover_population(population))
generation = 0 
print(a)
while fitness_individual(p[0]) != 1 :
    generation +=1
    p = evolve(p)
    p.sort(key=fitness_individual,reverse=True)
    best = p[0]
    print('Generation ' + str(generation) + '  :' , best) 
for i in range (n):
    print(i+1,end=' ')
    print(best[0][i], end=' ')
    print(best[1][i]+1, end =' ')
    print()