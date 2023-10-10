"""
Given a dictionary of students and their scores, find the average score.
"""

# Sample dictionary of students and their scores
student_scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 88,
    'Eve': 90
}

# Calculate the total sum of scores
total_score = sum(student_scores.values())

# Count the number of students (number of keys)
num_students = len(student_scores)

# Calculate the average score
average_score = total_score / num_students

# Print the average score
print("Average Score:", average_score)
