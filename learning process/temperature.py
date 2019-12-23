t=input()
if t[0] in ['C']:
    F=1.8*eval(t[1:])+32
    print("F{:.2f}".format(F))
else:
    C=(eval(t[1:])-32)/1.8
    print("C{:.2f}".format(C))
