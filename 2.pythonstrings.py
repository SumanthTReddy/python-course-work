1.# Empty strings
s = ''
s = ""
s = ''' '''
s = "' '"

# String concatenation
name = 'Ajay'
name1 = "Krishna"
print(name + name1)           # Output: AjayKrishna
print(name + ' ' + name1)     # Output: Ajay Krishna

# Repetition
print(name * 10)              # Output: Ajay repeated 10 times
print('*' * 100)
print('-' * 10)

# String indexing
name = 'Ajay Kumar'
print(name[3])    # y
print(name[-2])   # a
print(name[-5])   # K
print(name[1])    # j

# Long string
names = 'AjayKrishnaSatishNishithaPreethiRuchitha'
print(names)

# Slicing
print(names[0:4])     # Ajay
print(names[:4])      # Ajay
print(names[4:11])    # Krishna
print(names[11:17])   # Satish
print(names[17:25])   # Nishitha
print(names[25:32])   # Preethi
print(names[32:40])   # Ruchitha
print(names[32:])     # Ruchitha

# Step slicing
print(names[0:4:2])   # Aa
print(names[::3])     # A simplified pattern
print(names[::-1])    # Reverse string

# Reverse partial
print(names[10:3:-1]) # anhsirK

# Membership operators
print('Ajay' in names)     # True
print('nithin' in names)   # False
print('sahithi' not in names)  # True

# Case functions
print(names.upper())
print(names.lower())
print(names.swapcase())

# Capitalize and Title
l = 'python programming language'
print(l.capitalize())
print(l.title())

# Casefold
print("ß".casefold())  # ss

# Center, Ljust, Rjust
print(l.center(50, '*'))
print(l.center(50, '-'))
print(l.center(50, '_'))
print(l.ljust(50, '-') + ':')
print(l.rjust(50, '-'))

# Zfill examples
print('2'.zfill(6))
print('202'.zfill(6))
print('202123'.zfill(6))

# Find and Index methods
print(names.find('j'))
print(names.find('a'))
print(names.find('Ajay'))
print(names.find('z'))      # -1 (not found)
print(names.rfind('a'))
print(names.index('K'))
print(names.rindex('a'))
# Avoid using index() for not-found characters, as it raises an error

# Count occurrences
print(names.count('a'))
print(names.count('e'))
print(names.count('i'))

# Replace examples
print(names.replace('a', '*'))
print(names.replace('sh', '00'))
print(names.replace('Ajay', 'Anirudh'))

# maketrans and translate
trans_table = str.maketrans('AEIOUaeiou', '1234500000')
print(names.translate(trans_table))
