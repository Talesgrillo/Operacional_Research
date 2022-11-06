from pulp import *
import pandas as pd
import numpy as np

#Defining the variables in the problem
radiation = 2

#Defining objective fuction
obj_func = np.array([0.4,0.5])

#Create constrains arrays
area_1 = np.array([[0.3,0.1],[0.5,0.5],[0.6,0.4]])
dosagem = np.array([[2.7],[6],[6]])
print(area_1)
print(dosagem)

#Objective for the model problem
model = LpProblem('Fration of dose',LpMinimize)

#Defining the matrix for the variables
variable_names = [str(j) for j in range(1,radiation+1)]
variable_names.sort()
print ('Valores das Variaveis',variable_names)

#Defining non-negativity constrains
DV_variables = LpVariable.matrix("X", variable_names, cat = "Integer", lowBound= 0 )
allocation = np.array(DV_variables).reshape(1,2)
print("Decision Variable Matrix: ")
print(allocation)


obj_func = lpSum(allocation*obj_func)
print(obj_func)
model +=  obj_func
print(model)

# Constraints
constasdfva = lpSum(allocation*area_1[0]) <= dosagem[0]
print(constasdfva)

model += constasdfva

constasdfvr = lpSum(allocation*area_1[1]) == dosagem[1]
print(constasdfvr)

model += constasdfvr

constasdfvt = lpSum(allocation*area_1[2]) >= dosagem[2]
print(constasdfvt)

model += constasdfvt

# Solving
model.solve(PULP_CBC_CMD())
status =  LpStatus[model.status]
print(status)

print('Valor: %.3f'%model.objective.value())