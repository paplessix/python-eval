import numpy as np
from colorama import Fore, Style

def red_text(text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}"

def simil(carac1,carac2):
    if carac1 == carac2:
        return 0
    else :
        return -1
class Ruler:
    def __init__(self,string1,string2):
        self.string1 = string1
        self.string2 = string2
        self.d = -1
    def Mat_F(self) : 
        
        string1 = self.string1
        string2 = self.string2
        d = self.d

        F = np.zeros((len(string1),len(string2)))
        for i in range(len(string1)):
            F[i,0] = d*i
        for j in range(len(string2)):
            F[0,j] = d*j
        for i in range(1,len(string1)):
            for j in range (1,len(string2)):
                choice1 = F[i-1,j-1]+simil(string1[i],string2[j])
                choice2 = F[i-1,j]+d
                choice3 = F[i,j-1] + d
                F[i,j] = max(choice1,choice2,choice3)
        setattr(Ruler,'mat_F',F)
    
    def dist(self):
        string1 = self.string1
        string2 = self.string2
        d = self.d
        mat_F = self.mat_F

        distance = 0

        align1 = ""
        align2 = ""
        i = len(string1)-1
        j = len(string2)-1
        while j > 0 and i > 0  : 
            score = mat_F[i,j]
            scorediag = mat_F[i-1,j-1]
            scoreUp = mat_F[i,j-1]
            scoreLeft = mat_F[i-1,j]
            if score  == scorediag + simil(string1[i],string2[j]):
                if simil(string1[i],string2[j]) != 0:
                    distance+=1
                align1 = string1[i] + align1
                align2 = string2[j] + align2
                i = i-1
                j = j-1
            elif score == scoreLeft +d :
                distance += 1
                align1 = string1[i] + align1
                align2 = '=' + align2
                i = i-1
            elif score == scoreUp +d :
                distance += 1
                align1 = '=' + align1
                align2 = string2[j] + align2
                j = j-1

        if i == j :
            if simil(string1[i],string2[j]) != 0:
                distance+=1            
            align1 = string1[i] + align1
            align2 = string2[j] + align2
        else : 
            while i>=0:
                distance+=1
                align1 = string1[i] + align1
                align2 = '=' + align2
                i=i-1
            while j>=0:
                distance+=1
                align1 = '='+align1
                align2 = string2[j] + align2
                j = j-1
        setattr(Ruler,'align1',align1)
        setattr(Ruler,'align2',align2)
        setattr(Ruler,'distance',distance)


    def compute(self):
        self.Mat_F()
        self.dist()

    def report(self): 
        top =""
        bottom = ""
        for a,b in zip(self.align1,self.align2):
            if a == '=':
                top += red_text(a)
                bottom += b
            elif b == '=':
                top += a
                bottom += red_text(b)
            elif a!=b:
                top += red_text(a)
                bottom += red_text(b)
            else:
                top += a
                bottom += b

        return top , bottom
    