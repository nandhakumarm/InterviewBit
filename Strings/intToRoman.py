class Solution(object):
    def intToRoman(self, num):
        myList=[["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
        myStr=""
        
        
        while num>0:
            for i in range(len(myList)):
                #print myStr,myList[i][1]
                if i+1<len(myList) and num==myList[i+1][1]:
                    myStr+=myList[i+1][0]
                    num-=myList[i+1][1]
                    break
                elif i+1<len(myList) and num>=myList[i][1] and num<myList[i+1][1]:
                    myStr+=myList[i][0]
                    num-=myList[i][1]
                    break
                elif i+1==len(myList):
                    myStr+=myList[i][0]
                    num-=myList[i][1]
                    break
                    
        return myStr

