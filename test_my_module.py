import my_module as mod
import pytest
def f1(x): return x**2 + (3*2)

def test_solveAt():
    assert mod.solveAt(f1, 3) == 15
    
def test_printCsvVals():
    assert int(mod.printCsvVals('SwedishMotorInsurance.csv', ['Claims'], 10)) == 10
    
 
def test___init__():
    choose = mod.Chooser()   
    assert choose.vals == [1,2,3,4,5,6]