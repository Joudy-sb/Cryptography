class polynomial:
    def __init__(self, fx, gx):
        self.f = fx
        self.g = gx
        self.pow_f = self.polypow_f()
        self.pow_g = self.polypow_g()

    def polypow_f(self):
        counter=0
        pow_x = list()
        for i in reversed(self.f):
            if i == "1":
                pow_x.append(counter)
                counter+=1
            if i == "0":
                counter+=1
        return pow_x[::-1]
    
    def polypow_g(self):
        counter=0
        pow_x = list()
        for i in reversed(self.g):
            if i == "1":
                pow_x.append(counter)
                counter+=1
            if i == "0":
                counter+=1
        return pow_x[::-1]
    
    def addition(self):
        result = list()
        temp = list()
        temp.extend(self.pow_f)
        temp.extend(self.pow_g)
        for i in temp:
            if temp.count(i)==1:
                result.append(i)

        return result
    
    def multiplication(self):
        result = list()
        temp = list()
        for i in self.pow_f:
            for j in self.pow_g:
                temp.append(i+j)
        for i in temp:
            if temp.count(i)==1:
                result.append(i)

        return result
                
def main():
    obj = polynomial(str(101), str(111))
    print(obj.polypow_f())
    print(obj.polypow_g())
    print(obj.addition())
    print(obj.multiplication())

if __name__ == "__main__":
    main()