import random
import time
  ### Input read and handle

t0 = time.time()
# N classes and m rooms
n , m = list(map(int,input().split()))
# number of students in each class
d = list(map(int,input().split()))
# capacity of each room
c = list(map(int,input().split()))
#number of pairs of classes
k = int(input())
# time slot for class index i 
s = [None] * n
# room for class index i
r = [None] * n
# sort the rooms based on their capacities
l = sorted(c)
classes = [i for i in range (n)]
index_reverse = {}
for i in range (m):
    for j in range (m):
        if l[i] == c[j]:
            if j+1 not in index_reverse.values():
                index_reverse[i+1] = j+1 # sorted order : original order
            continue
dummy_1 = list()
Conflict_classes = set()
for i in range (k):
    dummy_1.append(list(map(int,input().split())))
for pair in dummy_1 :
    Conflict_classes.add((pair[0]-1,pair[1]-1))
    Conflict_classes.add((pair[1]-1,pair[0]-1))

    ###
    
def objective_value(slots):
    a = len(slots)
    return a
#select the course for this slot

def Greedy(slots,assigned):
    global Conflict_classes,c,d,l,classes
    def candidate_course(this_slot):
        candidate = []
        room = len(this_slot)
        room_cap = l[room]
        for i in classes:
            if assigned[i] == False: #course i hasnt been assigned yet
                if d[i] <= room_cap:
                        flag = True
                        for assigned_course in this_slot:
                            if (assigned_course,i) in Conflict_classes:
                                flag = False
                        if flag == True:
                            candidate.append(i)
        return candidate

    def select_course(this_slot):
        if len(this_slot) == m : # this slot is full
            return None
        else :
            candidate = candidate_course(this_slot)
            if len(candidate) == 0 :
                return None #no course satisfy this room
            else:
                if len(candidate) > 5:
                    candidate = candidate[:5]
                course = random.choice(candidate)
                return course
    def construct_solution(slots,assigned):
        this_slot = []
        while True:
            dummy = [0 if i == True else 1 for i in assigned]
            course = select_course(this_slot)
            if course == None :
                if len(this_slot) == m : # this slot is  full
                    slots.append(this_slot)
                    this_slot = []
                    continue
                else : # no course satisfy this room
                    this_slot.append(None) # move to the next room 
                    continue
            this_slot.append(course)
            if sum(dummy) == 1 :
                assigned[course] =True
                slots.append(this_slot)
                break
            assigned[course] = True # mark as assigned
        return slots
    sol = construct_solution(slots,assigned)
    return sol

def Local_Search(slots):
    candidates = []
    for l in slots:
        count = 0
        for cl in l :
            if cl != None:
                count += 1
        candidates.append([l,count])
    candidates.sort(key= lambda x : x[1],reverse=True)
    new_slots = [random.choice(candidates[:2])[0]]
    assigned = [False if i not in new_slots[0] else True for i in range (n)]
    random.shuffle(classes)
    new_sol = Greedy(new_slots,assigned)
    return new_sol



def greedy_ls():
    best_slots = None
    value_best = n
    while True:
        t = time.time()
        if t - t0 >= 240 : 
            break
        slots = Greedy([],[False for i in range (n)])
        value_cur = objective_value(slots)
        if value_cur < value_best:
            best_slots = slots
            value_best = value_cur
        for j in range (5):
            neighbor = Local_Search(slots)
            value_cur = objective_value(neighbor)
            if value_cur < value_best:
                best_slots = neighbor
                value_best = value_cur
    return best_slots

best_slots = greedy_ls()

def solution_converter(best_slots):
    for i in range (len(best_slots)):
        slot = best_slots[i]
        for j in range (len(slot)):
            clas = slot[j]
            if clas != None:
                s[clas] = i+1
                r[clas] = j+1
    for i in range (n):
        print(i+1,end=' ')
        print(s[i],end=' ')
        print(index_reverse[r[i]])
    return

solution_converter(best_slots)