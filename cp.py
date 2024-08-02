from ortools.sat.python import cp_model
import math
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
max_days = math.ceil(n/4)
max_slots = 4 * max_days
Conflict_classes = list()
for i in range (k):
    Conflict_classes.append(list(map(int,input().split())))
for pair in Conflict_classes :
    pair[0],pair[1] = pair[0] -1 , pair[1] -1 
model = cp_model.CpModel()
H = 200
s = [model.NewIntVar(1,max_slots,'s[' + str(i) + ']') for i in range (n)]
r = [model.NewIntVar(1,m,'r[' + str(i) + ']') for i in range (n) ]
z = model.NewIntVar(1,10**6,'z')

for (i,j) in Conflict_classes :
    model.Add(s[i] != s[j]) #no conflict class

for i in range (n):
    for j in range (n):
        if i != j :
            b1=model.NewBoolVar("b1")
            model.Add(r[i]==r[j]).OnlyEnforceIf(b1)
            model.Add(r[i]!=r[j]).OnlyEnforceIf(b1.Not())
            model.Add(s[i]!=s[j]).OnlyEnforceIf(b1)
            b2=model.NewBoolVar("b2")
            model.Add(s[i]==s[j]).OnlyEnforceIf(b2)
            model.Add(s[i]!=s[j]).OnlyEnforceIf(b2.Not())
            model.Add(r[i]!=r[j]).OnlyEnforceIf(b2)        
            
for i in range(n):
    for j in range(m):
        b=model.NewBoolVar("b")
        model.Add(r[i]==j+1).OnlyEnforceIf(b)
        model.Add(r[i]!=j+1).OnlyEnforceIf(b.Not())
        model.Add(c[j]>=d[i]).OnlyEnforceIf(b)



for i in range (n):
    model.Add(z >= s[i]) #max value

model.Minimize(z)
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE :
    for i in range (n):
        print(i+1,end=' ')
        print(solver.Value(s[i]),end=' ')
        print(solver.Value(r[i]), end = ' ')
        print()
else :
    print('NO SOLUTION')