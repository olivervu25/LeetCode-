class Solution:
    def generate(self,numRows):
        a=[]
        for i in range(numRows):
            list1 = [1]*(i+1)
            a.append(list1)
            if i>=2: 
                for j in range(1,i,1): 
                    list1[j] = a[i-1][j]+a[i-1][j-1]
                    a[i]= list1 
        return a
