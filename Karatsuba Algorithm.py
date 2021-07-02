#!/usr/bin/env python
# coding: utf-8

# In[83]:


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
        a = f_num // 10**(n)
        #print(a)
        b = f_num % 10**(n)
        #print(b)
        c = s_num // 10**(n)
        #print(c)
        d = s_num % 10**(n)
        #print(d)
        
        ac = karatsuba_algorithm(a, c)
        bd = karatsuba_algorithm(b,d)
        a_plus_b_multi_c_plus_d = karatsuba_algorithm(a+b, c+d) - ac - bd
        
        product = (ac * 10**(2 * n)) + (a_plus_b_multi_c_plus_d * 10**(n)) + bd
        return product


# In[84]:


karatsuba_algorithm(5678,1234)


# In[79]:


x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
karatsuba_algorithm(x, y)


# In[80]:


karatsuba_algorithm(123,345)

