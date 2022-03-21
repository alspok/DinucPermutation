import copy
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
    
    for item in result:
        dinucFull = copy.deepcopy(iv.dinucDictFull)
        diDictionary, _ = DinucCalc().dinucCalc(item)
        for key in diDictionary.keys():
            dinucFull[key][0] += diDictionary[key][0]
            dinucFull[key][1] += diDictionary[key][1]
            dinucFull[key][2] += abs(diDictionary[key][0] - diDictionary[key][1])
            dinucFull[key][3] = diDictionary[key][0] / dinuc_list_length
            dinucFull[key][4] = diDictionary[key][1] / dinuc_list_length
            dinucFull[key][5] = abs(dinucFull[key][3] - dinucFull[key][4])

        dinucSeq = ''.join(item)
        dinucSeq1st = dinucSeq
        dinucSeq2nd = dinucSeq[1:] + dinucSeq[0]
        print(f"{dinucSeq1st}")
        print(f" {dinucSeq2nd}")
        
        for key, value in dinucFull.items():
            print(f"{key}\t{dinucFull[key][0]}\t{dinucFull[key][1]}\t{dinucFull[key][2]}\t{dinucFull[key][3]:.6f}\t{dinucFull[key][4]:.6f}\t{dinucFull[key][5]:.6f}")
        pass
    # for key, value in dinucFull.items():
    #     if any(value):
    #         print(f"{key}\t{value[0]}\t{value[1]}\t{value[2]}\t{value[3]:.6f}\t{value[4]:.6f}\t{value[5]:.6f}")
    # print (f"\n{math.factorial(int(len(nuc_list)))} permutations")
            
    pass
         
if __name__ == '__main__':
    # dinucPermut()
    dinucPermutCalc()