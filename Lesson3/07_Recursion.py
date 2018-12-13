"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position >= 0:
        if position == 0 or position == 1:
            return position
        else:
            return get_fib(position - 1) + get_fib(position - 2)
    else:
        return -1

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)


"""
Fibonacci sequence without recursion
def get_fib(position):
	if position == 0 or position == 1:
        return position
    else:
        first = 0
        second = 1
        next = first + second
        for i in range(2, position):
        	first = second
            second = next
            next = first + second
        return next
"""
