import math
from Classes.InitVar import InitVar as iv
from Classes.Permutarion import Permutation as pm
from Classes.DinucCalc import DinucCalc 

def dinucPermut():
 
    nuc_list = iv.dinucList
    fact_nuc_list = math.factorial(int(len(nuc_list)))
       
    result = pm.permutations(nuc_list)
    i = 1
    for item in result:
        diCalc = DinucCalc()
        dinucDiffSum = diCalc.dinucCalc(item)
        if dinucDiffSum == 0:
            print(f"{i}\t{list(item)}")
        elif i % 10000 == 0:
            print(f"{i} of {fact_nuc_list} {(i/fact_nuc_list) * 100:2.6f} %", end='\r')
        i += 1
    
    input("\nPress any key to exit")
             
if __name__ == '__main__':
    dinucPermut()