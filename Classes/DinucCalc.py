from Classes.InitVar import InitVar as iv

class DinucCalc():
        
    def dinucCalc(self, diList: list) -> float:
        diString = ''.join(diList)
        if len(diString) % 2 == 0:
            diString = diString + diString[0]
        
        diDict = {'aa': [0, 0, 0], 'ac': [0, 0, 0], 'ag': [0, 0, 0], 'at': [0, 0, 0],
                  'ca': [0, 0, 0], 'cc': [0, 0, 0], 'cg': [0, 0, 0], 'ct': [0, 0, 0],
                  'ga': [0, 0, 0], 'gc': [0, 0, 0], 'gg': [0, 0, 0], 'gt': [0, 0, 0],
                  'ta': [0, 0, 0], 'tc': [0, 0, 0], 'tg': [0, 0, 0], 'tt': [0, 0, 0]
        }
        
        for key in diDict.keys():
            indices = [index for index in range(len(diString)) if diString.startswith(key, index)]
            for index in indices:
                if index % 2 == 0:
                    diDict[key][0] += 1
                else:
                    diDict[key][1] += 1
            diDict[key][2] = abs(diDict[key][0] - diDict[key][1])
            
        diDiffSum = 0
        for value in diDict.values():
            diDiffSum += value[2]
            
        return diDict, diDiffSum