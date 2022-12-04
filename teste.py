from src.sorting import sort_by
from src.jobs import read
from datetime import datetime
# import time

CRITERIA = ['min_salary', 'max_salary', 'date_posted']
jobs = read('src/jobs.csv')
sort_by(jobs, CRITERIA[2])

for ind in range(len(jobs)):
    data_time = datetime.strptime(jobs[ind][CRITERIA[2]], "%Y-%m-%d")
    # data = datetime(data_time)
    print(data_time)
