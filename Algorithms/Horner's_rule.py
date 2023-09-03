# Horner's Rule of Evaluating Polynomials in O(n) Time
def eval(polynomial,a):
    y_val =0
    for i in range(polynomial.degree,-0,-1):
        y_val += polynomial.coeff[i]
        y_val *=a
    y_val +=polynomial.coeff[0]
    return y_val

