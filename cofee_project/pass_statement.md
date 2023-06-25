
# What is Pass in Python?
In Python, the pass statement is considered as no operation statement,
means it consumes the execution cycle like a valid python statement but **nothing happens actually when the pass is executed**.


# What are the uses of pass statements and How it Works

- Pass work like when the condition is true it goes in the pass and executes code of pass block after that it continues with the main program code.
- It can be used when a statement is required syntactically but the program requires no action.
- In python, if you use an if, elif, else, functions, class, for loops, while loops you need to define their body or block of code correspond to them, if you don’t the python interpreter will throw an error. So, to overcome this error you can use the pass keyword as a body of the corresponding statement and the statement do nothing and throw no error.

# Example:
## 1. What if we do not use the pass keyword?
```python
number = 20
if number == 19:
else:
    print("this is else block")
```

Output:
```shell
  File "c:/Users/PythonPool/Desktop/test.py", line 3
    else:
       ^
IndentationError: expected an indented block
```

In the above python program, We haven’t declared the body of if statement. So when the python interpreter reaches at the if statement. Python interpreter didn’t find any code for if block.


## 2. Using the pass keyword/statement and solving the error
```python
number = 20
if number == 19:
    pass
else:
    print("this is else block")
```

# IMPORTANT: Pass Statement for an Empty Function
Python doesn’t have the concept of *abstract functions*. So if we have to define an empty function:

```python
def foo():
    pass
```