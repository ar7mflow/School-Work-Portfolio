"""
PDA Simulator for L = {wcw^R | w ∈ {0,1}*}
Author: Arham Hassan | 20426387
Language: Python 

This program should (hopefully successfully) simulate the PDA from last question 1 that only 
recognizes strings where a substring w is followed by 'c' and then the reverse of w.
"""



class Stack:
    
    def __init__(self):
        self.items = ['Z0']  # Starting at the bottom
    
    def push(self, symbol):
        self.items.append(symbol)
    
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None
    
    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        return None
    
    def is_bottom(self):
        return len(self.items) == 1 and self.items[0] == 'Z0'
    
    def copy(self):
        new_stack = Stack.__new__(Stack)
        new_stack.items = self.items.copy()
        return new_stack


#ar7m(a small marker I try to put in my code)

class PDASimulator:
    """
    PDA for L = {wcw^R | w ∈ {0,1}*}
    States used: q0 (push w), q1 (pop w^R), q2 (accept)
    """
    
    def __init__(self):
        self.q0 = 'q0'
        self.accept_states = {'q2'}
        self.transitions = self.build_transitions()
    
    def build_transitions(self):
        """
        Format: (state, input, stack_top) -> [(next_state, symbols_to_push)]
        """
        trans = {}
        
        # Phase 1: Pushing w onto stack (in q0)
        trans[('q0', '0', 'Z0')] = [('q0', ['0', 'Z0'])]
        trans[('q0', '1', 'Z0')] = [('q0', ['1', 'Z0'])]
        trans[('q0', '0', '0')] = [('q0', ['0', '0'])]
        trans[('q0', '0', '1')] = [('q0', ['0', '1'])]
        trans[('q0', '1', '0')] = [('q0', ['1', '0'])]
        trans[('q0', '1', '1')] = [('q0', ['1', '1'])]
        
        # Phase 2: Reading 'c' and move to q1
        trans[('q0', 'c', 'Z0')] = [('q1', ['Z0'])]
        trans[('q0', 'c', '0')] = [('q1', ['0'])]
        trans[('q0', 'c', '1')] = [('q1', ['1'])]
        
        # Phase 3: Matching and popping w^R (in q1)
        trans[('q1', '0', '0')] = [('q1', [])]
        trans[('q1', '1', '1')] = [('q1', [])]
        
        # Phase 4: Accepting yay !!!
        trans[('q1', '', 'Z0')] = [('q2', ['Z0'])]
        
        return trans
    


    def simulate(self, input_string):
        """
        Here we'll simulate PDA on input string using a BFS
        Returns True if accepted, False otherwise
        """
        # Checking for invalid inputs/characters here
        valid_chars = {'0', '1', 'c'}
        for char in input_string:
            if char not in valid_chars:
                return False
        
        # BFS: queue stores (state, remaining_input, stack)
        initial_stack = Stack()
        queue = [(self.q0, input_string, initial_stack)]
        visited = set()
        
        while queue:
            state, remaining, stack = queue.pop(0)
            
            # avoiding infinite loops!!! <insert smart meme here> 
            sig = (state, remaining, tuple(stack.items))
            if sig in visited:
                continue
            visited.add(sig)
            
            # Checking if it accepts
            if state in self.accept_states and remaining == '' and stack.is_bottom():
                return True
            
            stack_top = stack.peek()
            if stack_top is None:
                continue
            
            current_char = remaining[0] if remaining else ''
            
            # For trying our epsilon transitions
            key = (state, '', stack_top)
            if key in self.transitions:
                for next_state, push_symbols in self.transitions[key]:
                    new_stack = stack.copy()
                    new_stack.pop()
                    for sym in reversed(push_symbols):
                        new_stack.push(sym)
                    queue.append((next_state, remaining, new_stack))
            
            # for our regular transitions
            if current_char:
                key = (state, current_char, stack_top)
                if key in self.transitions:
                    for next_state, push_symbols in self.transitions[key]:
                        new_stack = stack.copy()
                        new_stack.pop()
                        for sym in reversed(push_symbols):
                            new_stack.push(sym)
                        queue.append((next_state, remaining[1:], new_stack))
        
        return False


#ar7m

def test_runs():
    """Our fancy comprehensive test suite"""
    pda = PDASimulator()
    
    print("="*70)
    print("Running Test Suite...")
    print("="*70)
    
    test_cases = [
        # Cases that should ACCEPT
        ("c", True, "Empty w"),
        ("0c0", True, "w = 0"),
        ("1c1", True, "w = 1"),
        ("01c10", True, "w = 01"),
        ("10c01", True, "w = 10"),
        ("00c00", True, "w = 00"),
        ("11c11", True, "w = 11"),
        ("101c101", True, "w = 101 palindrome"),
        ("110c011", True, "w = 110"),
        ("0110c0110", True, "w = 0110 palindrome"),
        ("001c100", True, "w = 001"),
        ("010c010", True, "w = 010 palindrome"),
    
        # Cases that Should REJECT
        ("", False, "Empty string"),
        ("0", False, "No c"),
        ("01", False, "No c"),
        ("cc", False, "Two c's"),
        ("0c", False, "Missing w^R"),
        ("c0", False, "Missing w"),
        ("01c01", False, "Not reverse"),
        ("10c10", False, "Not reverse"),
        ("01c11", False, "Length mismatch"),
        ("001c10", False, "Length mismatch"),
        ("0c1", False, "Symbol mismatch"),
        ("1c0", False, "Symbol mismatch"),
        ("010c100", False, "Not a reverse"),
        ("abc", False, "Invalid symbols"),
    ]
    
    passed = 0
    failed = 0
    
    for test_input, expected, description in test_cases:
        result = pda.simulate(test_input)
        
        if result == expected:
            passed += 1
            status = "✓"
        else:
            failed += 1
            status = "✗"
        
        result_str = "ACCEPT" if result else "REJECT"
        expected_str = "ACCEPT" if expected else "REJECT"
        print(f"{status} '{test_input:15s}' -> {result_str:6s} (expected {expected_str:6s}) | {description}")
    
    print("="*70)
    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("="*70)
    
    return passed == len(test_cases)


def interactive_mode():
    """A fun little interactive testing mode!! Try your own inputs!! """
    pda = PDASimulator()
    
    print("\n" + "="*70)
    print("Interactive Mode - PDA Simulator")
    print("Language: L = {wcw^R | w ∈ {0,1}*}")
    print("Type 'quit' to exit")
    print("="*70 + "\n")
    
    while True:
        try:
            user_input = input("Enter string to test: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            result = pda.simulate(user_input)
            
            if result:
                print(f"Result: ACCEPTED ✓\n")
            else:
                print(f"Result: REJECTED ✗\n")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}\n")

#ar7m



def main():
    """Our Main function""" 

    print("\nPDA Simulator for L = {wcw^R | w ∈ {0,1}*}")
    print("CISC/CMPE 223 - Problem 2\n")
    
    # First we run the pre-set tests
    all_passed = test_runs()
    
    if all_passed:
        print("\n✓ All tests passed!\n")
    else:
        print("\n⚠ Some tests failed!\n")
    
    # If the user wants interactive mode!
    interactive_mode()


if __name__ == "__main__":
    main()