# Sum of Above Average Scores
# Implement a function which takes a List as a parameter and returns the sum of the scores which are above average.
student_scores = [80, 60, 50, 65, 75, 55]


def calculate_avg(student_scores):
  total_sum = 0
  count = 0
  for score in student_scores:
    total_sum += score
    count += 1
  avg = total_sum / count
  return avg


def sum_score_above_average(student_scores):
  avg = calculate_avg(student_scores)
  total_sum = 0
  for score in student_scores:
    if score > avg:
      total_sum += score
  return total_sum


print(
    f"Sum of scores above average is: {sum_score_above_average(student_scores)}"
)
