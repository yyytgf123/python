class square:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def pow(self):
        result = self.first ** self.second
        return result
    def sum(self):
        result = self.first + self.second
        return result


a = square()
b = square()
a.setdata(3,4)
b.setdata(5,5)


print(a.pow())
print(b.sum())

