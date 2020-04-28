# Fermat's Latest Theorem: x^2+y^2=z^2
import math
def fermat(limit,n):

    ('\n'
     '        if n <= 2:\n'
     '        return\n')
    for x in range(1, limit+1):
        for y in range(x, limit+1):
            pow_sum = pow(x,n)+pow(y,n)
            z = pow(pow_sum,1/n)
            z_pow = pow(int(z),n)
            if pow_sum == z_pow:
                print("God! Fermat was wrong!")
            else:
                print(f"pow_sum={pow_sum},pow_z={z_pow}. No, that's not right!")


fermat(10,2)
