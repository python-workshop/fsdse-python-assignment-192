#Determine if a number is a power of two
def power_of_two(n):
    if (n & (n - 1)) == 0:
        return True
        print("Power of 2")
        
    else:
        return False
        print("Wrong No")


#power_of_two(8)