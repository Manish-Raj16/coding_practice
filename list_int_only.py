'''Create a function that takes a list of strings and integers, and filters out the list so
that it returns a list of integers only.

Examples
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
filter_list(["A", 0, "Edabit", 1729, "Python", 1729]) ➞ [0, 1729]'''

inp = list(input().split())

conv = []
for i in inp:
    try:
        conv.append(int(i))
    except ValueError:
        conv.append(i)
result=[]
#main program:
for i in conv:
    if type(i) == int:
        result.append(i)
print(result)
