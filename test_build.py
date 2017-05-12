import sys
from build import power_of_two

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
test(power_of_two(8) == True) # number is power of 2
test(power_of_two(15) == False) # number is not power of 2

