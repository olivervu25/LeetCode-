class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        i = 1
        if len(flowerbed)>=2: 
            if flowerbed[0]==0 and flowerbed[1]==0: 
                flowerbed[0]=1
                n-=1
            if flowerbed[-1]==0 and flowerbed[-2]==0: 
                flowerbed[-1]=1
                n-=1
        else: 
            if flowerbed[0]==0: 
                n-=1 
        while i < len(flowerbed)-1 and n>0: 
            if flowerbed[i]==0: 
                if flowerbed[i+1] == 0 and flowerbed[i-1]==0: 
                    flowerbed[i]=1
                    n-=1 
                    i+=1 
                else: 
                    i+=1
            else:
                i+=1 
        if n<=0: 
            return True
        else: 
            return False 

            
        