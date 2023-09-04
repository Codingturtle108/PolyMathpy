class Polynomials:
    def __init__(self,coeff,degree,symb):
        if len(coeff) != degree +1:
            print("Error ,Coefficient Requirement Not Satisfied")
            return
        self.coeff = coeff
        self.x = symb
        self.degree  =degree
    def genPoly(self): # Function To Generate Polynomial Expression
        self.Polynomial = f'{self.coeff[0]}'
        for i in range(1,len(self.coeff)):
            if self.coeff[i]:
                if self.coeff[i] ==1:
                    self.Polynomial += f'+{self.x}**{i}'
                else:
                    self.Polynomial += f'+{self.coeff[i]}{self.x}**{i}'
        return self.Polynomial
    def __add__(p1, p2): #Adding Add Operation In Polynomial Class
        # Assuming Degree to Be Same
        degree_res = max(p1.degree, p2.degree)
        print(degree_res)
        coeff_res = [0]*(degree_res+1)
        for i in range(degree_res+1):
            coeff_res[i] += p1.coeff[i] + p2.coeff[i]
        print(coeff_res)
        # For now Assuming The Polynomials consist of the same variable
        Poly_res = Polynomials(coeff_res,degree_res,p1.x)
        return Poly_res

    def eval(self, a):
        y_val = 0
        for i in range(self.degree, -0, -1):
            y_val += self.coeff[i]
            y_val *= a
        y_val += self.coeff[0]
        return y_val
    def __mul__(self,other):
        degree_res = self.degree + other.degree
        coeff_res = [0]*(degree_res+1)
        i =0
        while  i <= self.degree:
            j =0
            while j <= other.degree:
                coeff_res[i+j]+=self.coeff[i]*other.coeff[j]
                j +=1
            i +=1
        Poly =  Polynomials(coeff_res,degree_res,'x')
        return POly


