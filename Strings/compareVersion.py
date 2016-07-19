class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        list1=A.split(".")
        list2=B.split(".")
        #print list1
        #print list2
        len1=len(list1)
        len2=len(list2)
        
        i=0
        while i<len1 and i<len2:
            if int(list1[i])<int(list2[i]):
                return -1
            elif int(list1[i])>int(list2[i]):
                return 1
            else:
                i+=1
        if len1>len2:
            for i in range(len2,len1):
                if int(list1[i])>0:
                    return 1
            return 0
        elif len2>len1:
            for i in range(len1,len2):
                if int(list2[i])>0:
                    return -1
            return 0
        return 0

