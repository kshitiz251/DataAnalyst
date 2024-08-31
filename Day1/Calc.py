from functools import reduce

ls = [1,45,89,78,56]

st = list(filter(lambda a : a%2 , ls))

print(st)

m = list(map(lambda a: a*a ,st))

print(m)

r = reduce(lambda a,b : a+b , ls)

print(r)