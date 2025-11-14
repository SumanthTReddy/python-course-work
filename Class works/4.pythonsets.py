#sets

s=set() #nullset
print(s)

s={1,2,3,4,5,}
print(s)

s={1,1,1,2,2,3,3,3,4,5,7,7,8,10}
print(s)

s={4000,100,2,340,55,79}
print(s)

s.add(90)
print(s)

s.remove(4000)
print(s)

s.add(12.23)
print(s)

s.add("1234")
print(s)

s.add(12+7j)
print(s)

s.add(False)
print(s)

s.add((1,2,3,4))
print(s)

girls={'tejaswini','fareen','pooja'}
print(girls)

guys={'sumanth','hemanth','gopi','prasad'}
print(guys)

online={'prasad'}
print(online)

print(girls.union(guys))
print(girls.intersection(guys))
print(guys.intersection(online))
print



a={1,2,3,4,5}
b={4,5,6,7,8}

print(a.symmetric_difference(b))
print(a.difference(b))

a={1,2,3,4}
b={3,4}

print(a.issubset(b))
print(b.issubset(a))
print(a.issuperset(b))

print(girls.isdisjoint(guys))
print(guys.isdisjoint(online))


print(girls.add('teju'))
print(girls.remove('teju'))
print(girls.discard('teju'))
print(girls.pop())
print(girls.clear())
print(guys.update({'shiva','shekar','shankar'}))
print(guys.add('teju'))

a={1,2,3,4,5}
b={1,2,3,4}

print(a.intersection(b))
print(a)
print(b)
print(a.intersection_update(b))
print(a)
print(b)




c=a.copy()
print(c)

c.add(12)
print(c)
max(c)
min(c)
sum(c)
