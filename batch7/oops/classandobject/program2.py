import time
class con:


    def serverSetup(self):
        time.sleep(3)
        print("Server creation Started")
    
    def memorySetup(self):
        time.sleep(3)
        print("Server Memory Allocated Sucessfully")
    
    def serverReady(self):
        time.sleep(3)
        print("Server is ready to use !!")

    def __init__(self):
        self.serverSetup()
        self.memorySetup()
        self.serverReady()

    def __end__(self):
        pass


c1=con()

    