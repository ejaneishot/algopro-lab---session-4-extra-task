def unify_lists(a, b):
    #returns a new list which is the result of the unification of two lists A and B (A U B)
    return list(set(a + b))

def duplicate_string(t, s):
   
    #returns a modified version of the string, where each character is duplicated according to the corresponding integer in the tuple
   
    result = ""
    for i, c in enumerate(s):
        result += c * t[i]
    return result

def factorial(n):
    #calculates the factorial of a given integer n using recursion
    #base case: 0! = 1
    if n == 0:
        return 1
    #recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)
    
    #ezdub extra points plzplzplz i need to play games im tired thank