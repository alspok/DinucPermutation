from Classes.InitVar import InitVar as iv
from Classes.Permutarion import Permutation as pm
from Classes.DinucCalc import DinucCalc

def dinucPermut():
                
    result = pm.permutations(iv.dinucList)
    i = 1
    for item in result:
        diCalc = DinucCalc()
        dinucDiffSum = diCalc.dinucCalc(item)
        if dinucDiffSum == 0:
            print(f"{i}\t{list(item)}")
        else:
            print(i, end='\r')
        i += 1
        
if __name__ == '__main__':
    dinucPermut()