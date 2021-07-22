# https://www.hackerrank.com/challenges/polar-coordinates/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import cmath

for line in sys.stdin:
    complex_number = complex(line)

    polar_r = abs(complex_number)
    polar_phi = cmath.phase(complex_number)

    print(polar_r)
    print(polar_phi)
