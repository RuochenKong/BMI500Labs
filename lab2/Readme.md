## Lecture 3 Quiz

### Problem 1
What is the difference between a pandas Series and a DataFrame?

### Problem 2
Create a sample DataFrame and write a line of code for a quick statistic summary of your data in a DataFrame.

### Problem 3
What are the different ways of selecting elements of a DataFrame?

### Problem4
What is sorting for categorical variables in pandas DataFrame based on?

### Problem 5
Create a pandas DataFrame containing three columns of randomly generated data. Plot the cumulative sum of each column with labels.

### Problem 6
List the age of each gender with the highest weight from the following DataFrame.

```python
df = pd.DataFrame({'Name': 'Alex Tom Steve Clarke Sarah'.split(),
                   'Age': [23, 18, 30, 20, 45],
                   'weight': [151, 140, 180, 124, 120],
                   'Gender': ['Male'] * 3 + ['Female'] * 2})
```

### Problem 7
Replace the weight values higher than 150 with the mean value of weights in the DataFrame from the previous question.

### Problem 8
Create a value counts column and reassign back to the following DataFrame.

```python
df = pd.DataFrame({'Animal': 'cat dog dog dog fish'.split(),
                   'weight': [8, 10, 12, 11, 2]})
```