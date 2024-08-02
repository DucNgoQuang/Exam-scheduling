# N classes and m rooms
import time
t0 = time.time()
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
l = sorted(c)
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
slots = []
courses = [False for i in range (n)]
def select_course(this_slot):
    global Conflict_classes,c,d,courses,l
    if len(this_slot) == m : # this slot is full
        return None
    else :
        for i in range (n):
            if courses[i] == False: #course hasnt been assigned yet
                if d[i] <= l[len(this_slot)]:
                    flag = True
                    for assigned_course in this_slot:
                        if (assigned_course,i) in Conflict_classes:
                            flag = False
                    if flag == True:
                        return i 
this_slot = []
while True:
    dummy = [0 if i == True else 1 for i in courses]
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
        courses[course] =True
        slots.append(this_slot)
        break
    courses[course] = True # mark as assigned
t = time.time()
for i in range (len(slots)):
    slot = slots[i]
    for j in range (len(slot)):
        clas = slot[j]
        if clas != None:
            s[clas] = i+1
            r[clas] = j+1
for i in range (n):
    print(i+1,end=' ')
    print(s[i],end=' ')
    print(index_reverse[r[i]])