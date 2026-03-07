import numpy as np
import pandas as pd

# Store student names and their scores in Math, English, and Science.
students = np.array(['Alice', 'Bob', 'Charlie'])
math=np.array([85, 53, 66])
english=np.array([65, 55, 78])
history=np.array([73, 92, 56])

df = pd.DataFrame({
    'students': students,
    'math': math,
    'history': history,
    'english': english,
})

# Calculate the average score for each student.
# df['average'] = df[['math', 'history', 'english']].mean(axis=1)

# Calculate the average score for each subject.
# averageScores = df[['math', 'history', 'english']].mean()


# Find the top student in each subject.
# without re_indexing
print(df.loc[df['math'].idxmax()]['students'])
print(df.loc[df['history'].idxmax()]['students'])
print(df.loc[df['english'].idxmax()]['students'])
# with re_indexing
df = df.set_index('students')  
print(df[['math', 'history', 'english']].idxmax())

# Add a new student and update their scores.
# df.loc[len(df)] = ['ali',90, 88, 77]
# print(df)

# Remove a student from the dataset.
# df.drop(index = 3, inplace=True)
# print(df)

# Apply a small change to all scores (like adding bonus points).
# print(df[['math', 'history', 'english']] + 5)