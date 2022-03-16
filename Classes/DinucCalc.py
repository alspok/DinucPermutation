from Classes.InitVar import InitVar as iv

class DinucCalc():
        
    def dinucCalc(self, diList: list) -> float:
        diDict = iv.dinucDict
        diString = ''.join(diList)
        if len(diString) % 2 == 0:
            diString = diString + diString[0]
        diLength = len(diString) // 2
            
        for key, value in diDict.items():
            indices = [index for index in range(len(diString)) if diString.startswith(key, index)]
            for index in indices:
                if index % 2 == 0:
                    diDict[key][0] += 1
                else:
                    diDict[key][1] += 1
            diDict[key][0] = diDict[key][0] / diLength
            diDict[key][1] = diDict[key][1] / diLength
            diDict[key][2] = abs(diDict[key][0] - diDict[key][1])
            
        diDiffSum = 0
        for value in diDict.values():
            diDiffSum += value[2]
        # diDict = {}
        
        return diDiffSum