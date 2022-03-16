import math

"""Init var for project"""
class InitVar():
    nucList = ['a', 'c', 'g', 't']
    fact_nucList = math.factorial(int(len(nucList)))

    dinucList = ['tt', 'ac', 'ag', 'at',
                 'ca', 'cc', 'cg', 'ct',
                 'ga', 'gc', 'gg', 'gt',
                 'ta', 'tc', 'tg', 'aa'
    ]
    fact_dinucList = math.factorial(int(len(dinucList)))
    
    dinucList_aa = ['aa', 'aa', 'aa', 'aa', 'aa', 'aa', ]
    fact_dinucList_aa = math.factorial(len(dinucList_aa))
    
    dinucDict = {'aa': [0, 0, 0], 'ac': [0, 0, 0], 'ag': [0, 0, 0], 'at': [0, 0, 0],
                 'ca': [0, 0, 0], 'cc': [0, 0, 0], 'cg': [0, 0, 0], 'ct': [0, 0, 0],
                 'ga': [0, 0, 0], 'gc': [0, 0, 0], 'gg': [0, 0, 0], 'gt': [0, 0, 0],
                 'ta': [0, 0, 0], 'tc': [0, 0, 0], 'tg': [0, 0, 0], 'tt': [0, 0, 0]
    }
