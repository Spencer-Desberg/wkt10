import matplotlib.pyplot as plt
import pandas as pd
import random as rand

class Chooser:
    def __init__(self, vals = None):
        self.vals = [1,2,3,4,5,6] if vals is None else vals
        self.currentVal = rand.choice(self.vals)
        
    def select(self):
        self.currentVal = rand.choice(self.vals)
        return self.currentVal
        
    def get_value(self):
        return self.currentVal
    
def solveAt(func = None, x = None):
    if func is None: 
        return x
    else: return func(x)

def printCsvVals(csvName = None, colName = None, rows= None):
    if csvName is None: return 'please provide a file name'
    if colName is None: return 'please provide column name(s)'
    try:
        csv = pd.read_csv(csvName)
    except FileNotFoundError:
        return 'The file was not found.'
    vals = csv[colName]
    if rows is not None:
        vals = vals.iloc[rows]
    return vals

if __name__ == '__main__':
    #Chooser
    zoo_animals = Chooser(["tiger","elephant","gorilla","giraffe"])
    print(zoo_animals.get_value())
    #solveAt
    def f1(x): return x**2 + (3*2)
    print(solveAt(f1, 3))
    #printCsvVals
    print(printCsvVals('Homework\worksheet10\SwedishMotorInsurance.csv', ['Claims','Payment'], range(10)))