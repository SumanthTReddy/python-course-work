#dictionaries
'orderd mutable key-value pairs'
'keys must be immutable,unique'
d={}
print(d)
d=dict()
print(d)
d={'name':'sumanth','course':'PFS','batchno':41}
print(d)
d={'name':'sumanth','course':'PFS','batchno':41,'name':'ajay'}
print(d)
d={1:'val',12.3:'val','string':'val',(1,2,3):'val',False:'val'}
print(d)
d['name']='sumanth'
print(d)
d={'name':'sumanth','course':'PFS','batchno':41}
print(d)
print(d['course'])
print(d['batchno'])
print(d.get('name'))
print(d.get('age'))
d={'name':'sumanth','course':'PFS','batchno':41}
print(d)

print(d.update({'phoneno':123,'email':'suma@gmail.com'}))
print(d)


print(d.keys)
print(d.values)
print(len(d))
print(max(d)) 
print(min(d))
print(sorted(d))
print(d.setdefault('age',22))
