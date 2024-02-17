class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


def add_complex(a, b):
    result_real = a.real + b.real
    result_imag = a.imag + b.imag
    return ComplexNumber(result_real, result_imag)


def multiply_complex(a, b):
    result_real = a.real * b.real - a.imag * b.imag
    result_imag = a.real * b.imag + a.imag * b.real
    return ComplexNumber(result_real, result_imag)


def negate_complex(a):
    return ComplexNumber(-a.real, -a.imag)


def invert_complex(a):
    denominator = a.real**2 + a.imag**2
    result_real = a.real / denominator
    result_imag = -a.imag / denominator
    return ComplexNumber(result_real, result_imag)


def main():

    complex_num1 = ComplexNumber(3, 4)
    complex_num2 = ComplexNumber(1, 2)

    result_addition = add_complex(complex_num1, complex_num2)
    print(
        f"Addition: ({complex_num1.real} + {complex_num1.imag}i) + ({complex_num2.real} + {complex_num2.imag}i) = ({result_addition.real} + {result_addition.imag}i)"
    )

    result_multiplication = multiply_complex(complex_num1, complex_num2)
    print(
        f"Multiplication: ({complex_num1.real} + {complex_num1.imag}i) * ({complex_num2.real} + {complex_num2.imag}i) = ({result_multiplication.real} + {result_multiplication.imag}i)"
    )

    result_negation = negate_complex(complex_num1)
    print(
        f"Negation: -({complex_num1.real} + {complex_num1.imag}i) = ({result_negation.real} + {result_negation.imag}i)"
    )

    result_inversion = invert_complex(complex_num1)
    print(
        f"Inversion: 1 / ({complex_num1.real} + {complex_num1.imag}i) = ({result_inversion.real} + {result_inversion.imag}i)"
    )


if __name__ == "__main__":
    main()
