def karatsuba_algorithm(f_num, s_num):
    """
    An Algorithmic function that returns the multiplication between two numbers
    
    Parameters:
        f_num : int
                The first number
        s_num : int
                The second number
    Returns:
        product : int
                  The product between two numbers
    See Also:
    
        https://en.wikipedia.org/wiki/Karatsuba_algorithm
        
        This algorithm was developed to get the multiplication between two numbers using only
        3 multiplication instead of the ordinary 4 time multiplication concept.
        
        It uses Divide and Conquer Algorithm with complexity = O(n)
    """
    if f_num < 10 or s_num < 10:
        return f_num * s_num
    else:
        n = max(len(str(f_num)), len(str(s_num))) // 2
        a = f_num // 10 ** n
        b = f_num % 10 ** n
        c = s_num // 10 ** n
        d = s_num % 10 ** n
        
        ac = karatsuba_algorithm(a, c)
        bd = karatsuba_algorithm(b, d)
        a_plus_b_multi_c_plus_d = karatsuba_algorithm(a+b, c+d) - ac - bd
        
        product = (ac * 10**(2 * n)) + (a_plus_b_multi_c_plus_d * 10**(n)) + bd
        return product

x = 5678
y = 1234
print("The product of\n {} * {} = {}\n".format(x, y, karatsuba_algorithm(x, y)))
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
print("The product of\n {} * {} = {}\n".format(x, y, karatsuba_algorithm(x, y)))