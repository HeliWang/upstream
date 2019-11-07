"""
Find target number by * 2 or // 3 (lower bound) starting from 1
"""


def dfs(cur, target, visited):
    if cur == target:
        return True
    if cur in visited:
        return False
    visited.add(cur)
    return dfs(cur // 3, target, visited) or dfs(cur * 2, target, visited)
    # if a recursion is True, end the whole recursion,
    #  else, try another branch


def find_target(target):
    visited = set()
    return dfs(1, target, visited)


for i in range(200):
    if find_target(i) == False:
        print(i)

"""
Find all ways to reach the target
"""


def dfs(cur, target, visited, trace):
    if cur == target:
        print(trace)
    if cur in visited:
        return False
    visited.add(cur)
    return dfs(cur // 3, target, visited) or dfs(cur * 2, target, visited)
    # if a recursion is True, end the whole recursion,
    #  else, try another branch


def find_target(target):
    visited = set()
    return dfs(1, target, visited)


for i in range(200):
    if find_target(i) == False:
        print(i)

"""
# Find the shortest way to reach the target number by * 2 or // 3 (lower bound) starting from 1
Analysis: A graph problem, with cycle
  2 * 2 * 2 * 2 // 3 == 5
  2 * 2 * 2 * 2 * 2 * 2 // 3 // 3 == 5
"""


def dfs(cur, target, visited):
    if cur == target:
        return True
    if cur in visited:
        return False
    visited.add(cur)
    return dfs(cur // 3, target, visited) or dfs(cur * 2, target, visited)


def find_target(target):
    visited = set()
    return dfs(1, target, visited)


for i in range(100):
    print(find_target(i))


def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))
