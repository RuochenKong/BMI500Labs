## Homework of Week 5: Natural Language Processing

#### Problem 1 
1. Look up the documentation for lists, dictionaries and strings in python. (Nothing to submit for this)
2. Are there more sophisticated dictionaries? What is a defaultdict?
#### Problem 2
A palindrome is a string that reads the same backwards and forwards. 
1. Write and run some code that checks if a given string is palindrome and prints the result on the screen. Provide 2 outputs in the homework answer--one for a palindrome and one for a non-palindrome.
#### Problem 3
For strings, run the following functions and test their utilities.

The input string (s) is:\
s = ' The quick brown fox jumped over the lazy dog '

You can find more information in section 3.2 of the NLTK book: [http://www.nltk.org/book_1ed/ch03.html](http://www.nltk.org/book_1ed/ch03.html). 

1. Search for the word 'the' using the following functions
```python
s.find(t)	
s.rfind(t)	
```
2. What is the output for 'dog'? What is the output for 'cat' for the following functions?
```python
s.index(t)	
s.rindex(t)
```

3. Split the string and join it via the marker '$$' (using the $$ as 'glue')
```python
s.split(t)	
s.join(text)
```

4. Show the outputs of the following 3 functions.
```python
s.lower()	
s.upper()	
s.title()
```

5. What does the strip function do to the string s?
```python
s.strip()
```

6.  Replace 'jumped' with 'flew'
```python
s.replace(t, u)	
```

#### Problem 4
Generating frequency distributions:

1. Preprocess the string s by lowercasing it and tokenizing it using the split() function. Remove extra whitespace using the strip() function.
2. Run the command provided by nltk for generating frequency distributions (FreqDist()).
3. Output the distribution.
4. How does preprocessing affect the generation of frequency distributions?

