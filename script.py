import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)

score_mean = students.score.mean()
#print(score_mean)

students.score = students.score.fillna(value = 0)

print(students.score)

score_mean_2 = students.score.mean()
print(score_mean)




