from pulp import *
import pandas as pd
import numpy as np


#Defining the problem variables
products = 2

#Objective function
Objectivea = np.array([3,-3])

#Defining the constrains
problem_constrains = np.array([[-5,-6],[-8,5],[-2,3]])
respo = np.array([-30,40,6])
print(problem_constrains)

#Defining the objective for the problem model
model = LpProblem("Wyndor Glass CO",LpMinimize)

#Defining the matrix for the variables
variable_names = [str(j) for j in range(1,products+1)]
variable_names.sort()
print("Variable Indices:", variable_names)

#Defining non-negativity constrains
DV_variables = LpVariable.matrix("X", variable_names[0], cat = "Integer", lowBound= -6,upBound=7)
DV_variables1 = LpVariable.matrix("X", variable_names[1], cat = "Integer", lowBound= 0,upBound=10)
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

constasdfvr = lpSum(allocation*problem_constrains[1]) <= respo[1]
print(constasdfvr)

model += constasdfvr

constasdfvt = lpSum(allocation*problem_constrains[2]) >= respo[2]
print(constasdfvt)

model += constasdfvt

# Solving
model.solve(PULP_CBC_CMD())
status =  LpStatus[model.status]
print(status)

print("Valor:",model.objective.value())