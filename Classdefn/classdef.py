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
