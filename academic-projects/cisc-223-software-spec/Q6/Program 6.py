"""
Computing x^n for non-negative integer n
Author: That one student who had too much coffee, jk, Arham Hassan | 20426387
Date: Probably past midnight
"""


def power_iterative(x, n):
    """
    Attempting to compute x^n iteratively.
    
    Pre-Condition we're using: 
        n >= 0 
        x is a number (int or float, we don't judge)
    
    Post-Condition:
        Returns x^n 
        If n=0, returns 1 (because math)
    
    Loop Invariant:
        After k iterations: result == x^k AND 0 <= k <= n
    
    Args:
        x: the base (any number)
        n: the exponent (must be >= 0)
    
    Returns:
        x raised to the power n
    """
    
    # --- Pre-Condition checlks ---
    # (optional but good practice, comment out if you trust your inputs 100%!!)
    assert n >= 0, f"Bruh, n={n} is negative. Read the spec: n >= 0 only!"
    assert isinstance(n, int), f"n should be an int, you passed in {type(n)}"
 
    
    # --- Initialization ---
    result = 1  
    k = 0       
    
    #ar7m
    # --- Main Loop ---
    while k < n:
        
        
        result = result * x  
        k = k + 1            
      
    
    # --- TERMINATION ---
    # Loop should exit when k == n
    # By invariant: result == x^k == x^n
    # Hence our Post-Condition is satisfied!! yayy!! 
    
    return result




def power_recursive(x, n):
    """
    This one should compute x^n recursively (bascially using the elegant, "trust the math" approach).
    
    Pre-Condition:
        n >= 0
        x is a number
    
    Post-Condition:
        Returns x^n
    
        power(x, 0) = 1                    (base case)
        power(x, n) = x * power(x, n-1)    (recursive case for n > 0)
    
    Args:
        x: base
        n: exponent (non-negative int)
    
    Returns:
        x^n
    """
    
    # --- Pre-Condition CHECK (just once at entry) ---
    assert n >= 0, f"Recursive power needs n >= 0, got n={n}"
   #ar7m 
    # --- BASE CASE ---
    if n == 0:
        
        return 1  
    
    # --- RECURSIVE CASE ---
    else:
    
        recursive_result = power_recursive(x, n - 1)
        
        return x * recursive_result  # POST: returns x^n yayyy!!




def power(x, n):
    """
    Just a wrapper function: computes x^n.
    Defaults to iterative version (because stack overflow is real for large n).
    Fun Fact: Feel free to swap to power_recursive(x, n) if you're feeling like it ;)
    
    Args:
        x: base
        n: exponent (non-negative int)
    
    Returns:
        x^n
    """
    return power_iterative(x, n)  # You can change this to power_recursive if you want




# ============================================
#             HOLY TESTING ZONE 
# ============================================

def test_power():
 

    print("Running tests...\n")
    
    # Test 1: Basic cases
    assert power(2, 3) == 8, "2^3 should be 8"
    print("✓ Test 1 passed: power(2, 3) = 8")

    assert power(5, 0) == 1, "5^0 should be 1"
    print("✓ Test 2 passed: power(5, 0) = 1")
    
    assert power(3, 1) == 3, "3^1 should be 3"
    print("✓ Test 3 passed: power(3, 1) = 3")
    
    # Test 2: Larger exponent
    assert power(2, 10) == 1024, "2^10 should be 1024"
    print("✓ Test 4 passed: power(2, 10) = 1024")
    
    # Test 3: x = 0
    assert power(0, 5) == 0, "0^5 should be 0"
    print("✓ Test 5 passed: power(0, 5) = 0")
    
    # Test 4: x = 1
    assert power(1, 100) == 1, "1^100 should be 1"
    print("✓ Test 6 passed: power(1, 100) = 1")
    
    # Test 5: Negative base
    assert power(-2, 3) == -8, "(-2)^3 should be -8"
    print("✓ Test 7 passed: power(-2, 3) = -8")
    
    assert power(-2, 4) == 16, "(-2)^4 should be 16"
    print("✓ Test 8 passed: power(-2, 4) = 16")
    
    # Test 6: Float base
    result = power(2.5, 2)
    assert abs(result - 6.25) < 0.0001, "2.5^2 should be 6.25"
    print(f"✓ Test 9 passed: power(2.5, 2) = {result}")
    
    # Test 7: Edge case - 0^0 (mathematically debated, we just return 1 lmao)
    assert power(0, 0) == 1, "0^0 is defined as 1 in this implementation"
    print("✓ Test 10 passed: power(0, 0) = 1 (by convention)")
    
    print("\n🎉 All tests passed! Code is solid.")




def test_both_versions():
    """
    Verifying if both iterative and recursive give the same results, cuz why not for the love of coding.
    """
    print("\n Comparing iterative vs recursive...\n")
    
    test_cases = [(2, 3), (5, 0), (3, 1), (2, 10), (-2, 4), (7, 2)]
    
    for x, n in test_cases:
        iter_result = power_iterative(x, n)
        rec_result = power_recursive(x, n)
        assert iter_result == rec_result, f"Mismatch for ({x}, {n})"
        print(f"✓ power({x}, {n}): iterative={iter_result}, recursive={rec_result} (match!)")
    
    print("\n Both versions produce identical results!")


# ============================================
#                    MAIN 
# ============================================



if __name__ == "__main__":
    print("=" * 50)
    print("  POWER(x, n) IMPLEMENTATION - CISC223 Problem 6")
    print("=" * 50)
    print()
    
    # To run basic tests
    test_power()
    
    # For comparing iterative vs recursive
    test_both_versions()
    
    print("\n" + "=" * 50)
    print("Demo: Try it yourself!")
    print("=" * 50)
    
    # A lil interactive demo :))
    x_demo = 3
    n_demo = 4
    result = power(x_demo, n_demo)
    print(f"\npower({x_demo}, {n_demo}) = {result}")
    print(f"Verification: {x_demo}^{n_demo} = {x_demo**n_demo} (using Python's ** operator)")
    print(f"Match: {result == x_demo**n_demo}\n")