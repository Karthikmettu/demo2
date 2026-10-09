class PositiveNumber:
    def __new__(cls, value):
        if value < 0:
            print("Negative value not allowed!")
            return None   # No object created
        return super().__new__(cls)

    def __init__(self, value):
        self.value = value
        print("hello")


p1 = PositiveNumber(10)
print(p1.value)   # 10
p2 = PositiveNumber(-5)
print(p2)         # None