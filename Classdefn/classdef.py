class Polynomials:
    def __init__(self,coeff,degree,symb):
        if len(coeff) != degree +1:
            print("Error ,Coefficient Requirement Not Satisfied")
            return
        self.coeff = coeff
        self.x = symb
        self.degree  =degree
    def genPoly(self):
        self.Polynomial = f'{self.coeff[0]}'
        for i in range(1,len(self.coeff)):
            if self.coeff[i]:
                if self.coeff[i] ==1:
                    self.Polynomial += f'+{self.x}**{i}'
                else:
                    self.Polynomial += f'+{self.coeff[i]}{self.x}**{i}'
        return self.Polynomial
p1 = Polynomials([1,2,1],2,'x')
print(p1.genPoly())
