class BMW:
    car1="BMW1"
    car2="BMW2"

    def start(self):
        print(f"id: {self}")
        print("start")
    
    def stop(self):
        print("stop")

    def drive(self):
        print("drive")


p1=BMW()
p2=BMW()



print(p1.car1)
print(p1.car2)

p1.start()
p2.start()