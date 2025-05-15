class square():


    def genratesquare(self,*nums):
         for num in nums:
            print(f"{num} squared is {num ** 2}")


data=square()

data.genratesquare(10)
data.genratesquare(10,30)
data.genratesquare(10,30,40)
