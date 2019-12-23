c=input()
if c[0] in ['R']:
    U=eval(c[3:])/6.78
    print("USD{:.2f}".format(U))
else:
    R=eval(c[3:])*6.78
    print("RMB{:.2f}".format(R))
