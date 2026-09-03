# M1.1 — Expressions and Values

## Objective

## Notes
What is an expression?
An expression is a combination of values, variables , operators and function calls that python evaluates to produce a value/result.

What is a Value?
A value is the result obtained when Python evaluates an expression. Values are represented by objects in Python.

What does it mean to evaluate an expression?
To evaluate an expression means producing a result or value ex 10 + 5, 10 * 2 , x = 10 +2 etc
An expression can be as simple as a literal/name or more complex using operators and function calls


## Examples
Three examples of expressions are:
1 0 + 2 , 11 * 2 , x , x + 10,  x = 10 + 5
x = 10 + 5 is a expression evaluated by python interpreter to produce value / result 15 where 
x is bound to the resulting object value 

## Experiments
In x = 10 + 5, 10 + 5 is evaluated first. The resulting object is then bound to x

What is the result of 10 + 2 * 3?
ans - 16

What is the result of (10 + 2) * 3?
ans -36

What is the result of 20 - 8 / 2?
ans -16

What is the result of 20 - 8 // 2?
ans -16

What is the result of 2 ** 3 * 2? 
ans -16

## Debugging

## Practice Questions
x = 10
y = x + 5
x = 20

print(x)
print(y)
-- My prediction is x= 20 and y= 15. Let me run this and check.
Result:
x= 20 as python  interpret and execute code line by line in ln 3 x is declared 20 so it will print 20, but in ln 1 x is declared 10, and when python evaluates expression x + 5 in ln 2 where y is bound to result of the expression it given result 15 when we use print(y)
y= 15
in y = x + 5, x + 5 is evaluated as a expression as python sees values and operators, and produce result/ value

after evaluating the expression python obtains  value 15 a new object which is bound to variable y.

after x = 20 , no python does not automatically update the value of y with x value, it just rebinds the object reference 20 to x variable.


## Reflection
