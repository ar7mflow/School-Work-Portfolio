# CISC 360 Haskell Exam Solutions - Quick Reference

## Question 2 (2.5 points) - Lambda Calculus Stepping

### First Expression: `(\u -> 1 + u 7)`
**CANNOT BE STEPPED**
- Reason: Lambda abstraction without argument applied
- `u` needs to be a function but no value is supplied

### Second Expression: `(\t -> t 7) (\x -> 9 - 1)`
**STEPS TO: 8**
```
    (\t -> t 7) (\x -> 9 - 1)
 => (\x -> 9 - 1) 7                [β-reduction: substitute (\x -> 9 - 1) for t]
 => 9 - 1                          [β-reduction: substitute 7 for x]
 => 8                              [by arithmetic]
```

---

## Question 3 (2.5 points) - Lambda Calculus Stepping

### First Expression: `(\u -> 2 + u 10)`
**CANNOT BE STEPPED**
- Reason: Lambda abstraction without argument applied
- `u` needs to be a function but no value is supplied

### Second Expression: `(\t -> t 7) (\x -> 9 - 5)`
**STEPS TO: 4**
```
    (\t -> t 7) (\x -> 9 - 5)
 => (\x -> 9 - 5) 7                [β-reduction: substitute (\x -> 9 - 5) for t]
 => 9 - 5                          [β-reduction: substitute 7 for x]
 => 4                              [by arithmetic]
```

---

## Question 4 (5 points) - Recursive Trace

### Given:
```haskell
mySum [] = 0
mySum (x:xs) = x + mySum xs
```

### Trace: `mySum [1,2,3]`

```
    mySum [1,2,3]
 => 1 + mySum [2,3]                         [match (x:xs) with x=1, xs=[2,3]]
 => 1 + (2 + mySum [3])                     [match (x:xs) with x=2, xs=[3]]
 => 1 + (2 + (3 + mySum []))                [match (x:xs) with x=3, xs=[]]
 => 1 + (2 + (3 + 0))                       [base case: [] = 0]
 => 1 + (2 + 3)                             [3 + 0 = 3]
 => 1 + 5                                   [2 + 3 = 5]
 => 6                                       [1 + 5 = 6]
```

**ANSWER: 6**

---

## Question 5 (5 points) - Fill in the Blanks

### Complete the function:
```haskell
removeLastTwo :: [a] -> [a]
removeLastTwo [x,y] = []
removeLastTwo (x:xs) = x : removeLastTwo xs
```

**ANSWER:** `x : removeLastTwo xs`

### How it works:
- Base case: When exactly 2 elements left, return []
- Recursive case: Keep first element (x), recurse on rest (xs)
- Naturally stops when reaching the last two elements

### Example:
```
removeLastTwo [1,2,3,4,5]
=> [1,2,3]
```

---

## Question 6 (5 points) - Design Your Own

### Task: Count even numbers in a list (recursion only)

```haskell
myEvenCount :: [Int] -> Int
myEvenCount [] = 0
myEvenCount (x:xs)
    | x `mod` 2 == 0 = 1 + myEvenCount xs
    | otherwise      = myEvenCount xs
```

### How it works:
- Base case: Empty list has 0 even numbers
- Recursive case: If x is even, add 1 to count; otherwise don't add
- Uses guards with `mod` to check evenness

### Example:
```
myEvenCount [1,2,3,4]
=> 2  (counts 2 and 4)
```

---

## Question 7 (5 points) - Fix Infinite Recursion

### Given (BROKEN):
```haskell
myReverse :: [a] -> [a]
myReverse (x:xs) = myReverse xs ++ [x]
```

### Problem:
**Input that causes issue:** `[]` (empty list)

**Why:** No base case to stop recursion

### FIXED VERSION:
```haskell
myReverse :: [a] -> [a]
myReverse [] = []                    -- MISSING PIECE
myReverse (x:xs) = myReverse xs ++ [x]
```

**ANSWER:** Add base case `myReverse [] = []`

### Example with fix:
```
myReverse [1,2,3]
=> [3,2,1]
```

---

## Summary of Answers

| Question | Answer |
|----------|--------|
| Q2.1 | Cannot be stepped (no argument) |
| Q2.2 | 8 |
| Q3.1 | Cannot be stepped (no argument) |
| Q3.2 | 4 |
| Q4 | 6 (with full trace shown) |
| Q5 | `x : removeLastTwo xs` |
| Q6 | myEvenCount function (shown above) |
| Q7 | Add: `myReverse [] = []` |

---

## Key Course Patterns Used

✓ **β-reduction** for lambda calculus steps  
✓ **Pattern matching** with `(x:xs)` notation  
✓ **Guards** for conditional logic  
✓ **Structural recursion** on lists  
✓ **Base cases** for termination  
✓ **No built-in functions** where restricted  
✓ **Clear step-by-step justification**  

All solutions follow CISC 360 course standards and conventions.
