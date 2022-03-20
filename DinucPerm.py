import math
from ntpath import join
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
        _, dinucDiffSum = diCalc.dinucCalc(item)
        if dinucDiffSum == 0:
            print(f"{i}\t{list(item)}")
        elif i % 10000 == 0:
            print(f"{i} of {fact_nuc_list} {(i/fact_nuc_list) * 100:2.6f} %", end='\r')
        i += 1
    print()
    pass

def dinucPermutCalc():
    nuc_list = iv.dinucList
    dinuc_list_length = len(''.join(nuc_list)) // 2
    result = pm.permutations(nuc_list)
    
    dinucDictSum = iv.dinucDictSum
    for item in result:
        diDictionary, _ = DinucCalc().dinucCalc(item)
        for key in diDictionary.keys():
            dinucDictSum[key][0] += diDictionary[key][0]
            dinucDictSum[key][1] += diDictionary[key][1]
            dinucDictSum[key][2] += abs(diDictionary[key][0] - diDictionary[key][1])
            dinucDictSum[key][3] = diDictionary[key][0] / dinuc_list_length
            dinucDictSum[key][4] = diDictionary[key][1] / dinuc_list_length 
            dinucDictSum[key][5] = abs(dinucDictSum[key][3] - dinucDictSum[key][4])
    
    for key, value in dinucDictSum.items():
        if any(value):
            print(f"{key}\t{value[0]}\t{value[1]}\t{value[2]}\t{value[3]:.6f}\t{value[4]:.6f}\t{value[5]:.6f}")
    print (f"\n{math.factorial(int(len(nuc_list)))} permutations")
            
    pass
         
if __name__ == '__main__':
    # dinucPermut()
    dinucPermutCalc()