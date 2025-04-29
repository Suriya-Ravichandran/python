class Sum:
    def add(self, *args):
        return sum(args)

s1 = Sum()

print(s1.add(10))             # 10
print(s1.add(20, 40))         # 60
print(s1.add(30, 40, 50))     # 120
