from pulp import *
import pandas as pd
import numpy as np


#Defining the problem variables
products = 2

#Objective function
Objectivea = np.array([3,-3])

#Defining the constrains
problem_constrains = np.array([[-6,3],[9,5],[-4,7],[5,10]])
respo = np.array([18,45,-28,50])
print(problem_constrains)

#Defining the objective for the problem model
model = LpProblem("Exercise_2",LpMaximize)

#Defining the matrix for the variables
variable_names = [str(j) for j in range(1,products+1)]
variable_names.sort()
print("Variable Indices:", variable_names)

#Defining non-negativity constrains
DV_variables = LpVariable.matrix("X", variable_names[0], cat = "Integer", lowBound= 0)
DV_variables1 = LpVariable.matrix("X", variable_names[1], cat = "Integer", upBound= 4)
allocation = np.array([DV_variables,DV_variables1]).reshape(1,2)
print("Decision Variable/Allocation Matrix: ")
print(allocation)

obj_func = lpSum(allocation*Objectivea)
print(obj_func)
model +=  obj_func
print(model)

# Constraints
constasdfva = lpSum(allocation*problem_constrains[0]) <= respo[0]
print(constasdfva)

model += constasdfva

constasdfvr = lpSum(allocation*problem_constrains[1]) >= respo[1]
print(constasdfvr)

model += constasdfvr

constasdfvt = lpSum(allocation*problem_constrains[2]) >= respo[2]
print(constasdfvt)

model += constasdfvt

constasdfavt = lpSum(allocation*problem_constrains[3]) >= respo[3]
print(constasdfavt)

model += constasdfavt

# Solving
model.solve(PULP_CBC_CMD())
status =  LpStatus[model.status]
print(status)

print("Valor:",model.objective.value())


for v in model.variables():
    try:
        print(v.name,"=", v.value())
    except:
        print("error couldnt find value")