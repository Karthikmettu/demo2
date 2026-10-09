class Test:
    def __init__(self,x):
        print("Default constructor")
        self.x=x

t = Test("Hii")
g=Test("Hello world")
print(t.x)
print(g.x)