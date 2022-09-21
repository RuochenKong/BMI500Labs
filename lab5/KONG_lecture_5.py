# Problem 1
# b) Yes, the 'UserDict' class under 'collections' allows user to implement more functions based on original 'dict'.
#    There's also 'OrderedDict' under 'collections'.
#    'defaultdict' is a subclass of 'dict', which allows users to specify the default value of keys.


# Problem 2
def check_palindrome(string):
    reversed_string = string[::-1]
    res = True if reversed_string == string else False
    return res


# Test Results:
#     String: 1234321 is palindrome
#     String: 123421 is non-palindrome

test_str = '1234321'
is_palindrome = 'palindrome' if check_palindrome(test_str) else 'non-palindrome'
print('String: %s is %s' % (test_str, is_palindrome))

test_str = '123421'
is_palindrome = 'palindrome' if check_palindrome(test_str) else 'non-palindrome'
print('String: %s is %s' % (test_str, is_palindrome))

# Problem 3
s = ' The quick brown fox jumped over the lazy dog '

# a)
# Results:
#     Function "find('the')": 33
#     Function "rfind('the')": 33
print('Function "find(\'the\')":', s.find('the'))
print('Function "rfind(\'the\')":', s.rfind('the'))

# b)
# Results:
#     Function "find('dog')": 42
#     Function "find('cat')": -1
print('Function "find(\'dog\')":', s.find('dog'))
print('Function "find(\'cat\')":', s.find('cat'))

# c)
# Results:
#     Function "s.split(' ')": ['', 'The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog', '']
#     Function "'$$'.join(s)": $$The$$quick$$brown$$fox$$jumped$$over$$the$$lazy$$dog$$
new_s = s.split(' ')
print('Function "s.split(\' \')":', new_s)
new_s = '$$'.join(new_s)
print('Function "\'$$\'.join(s)":', new_s)

# d)
# Results:
#     Function "s.lower()":  the quick brown fox jumped over the lazy dog
#     Function "s.upper":  THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG
#     Function "s.title()":  The Quick Brown Fox Jumped Over The Lazy Dog
print('Function "s.lower()":', s.lower())
print('Function "s.upper":', s.upper())
print('Function "s.title()":', s.title())

# e)
# Results:
#     Function "s.strip()": The quick brown fox jumped over the lazy dog
print('Function "s.strip()":', s.strip())

# f)
# Results:
# Function "s.replace('jumped', 'flew')":  The quick brown fox flew over the lazy dog
print('Function "s.replace(\'jumped\', \'flew\')":', s.replace('jumped', 'flew'))

# Problem 4

# a) Results:
#    ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
s = s.lower().strip().split(' ')
print(s)

# b) & c) Results:
#    dict_items([('the', 2), ('quick', 1), ('brown', 1), ('fox', 1),
#                ('jumped', 1), ('over', 1), ('lazy', 1), ('dog', 1)])
from nltk import FreqDist
freq_distribution = FreqDist(s)
print(freq_distribution.items())

# d)
# Without split(), the whole sentence would be considered as a single word.
# Without strip(), we would expect a extra distribution that "('',2)"
# Without lower(), we would expect "('The',1),('the',1)" instead of "('the',2)"
