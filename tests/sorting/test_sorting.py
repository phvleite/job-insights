from src.sorting import sort_by
from src.jobs import read
from datetime import datetime


def test_sort_by_criteria_min_salary():
    CRITERIA = ['min_salary', 'max_salary', 'date_posted']
    jobs = read('src/jobs.csv')
    sort_by(jobs, CRITERIA[0])
    try:
        for ind in range(5):
            assert jobs[ind][CRITERIA[0]] <= jobs[ind + 1][CRITERIA[0]]
    except Exception:
        assert False

    assert jobs[len(jobs) - 1][CRITERIA[0]] == ''


def test_sort_by_criteria_max_salary():
    CRITERIA = ['min_salary', 'max_salary', 'date_posted']
    jobs = read('src/jobs.csv')
    sort_by(jobs, CRITERIA[1])
    try:
        for ind in range(5):
            assert jobs[ind][CRITERIA[0]] > jobs[ind + 1][CRITERIA[0]]
    except Exception:
        assert False

    assert jobs[len(jobs) - 1][CRITERIA[0]] == ''


def test_sort_by_criteria_date_posted():
    CRITERIA = ['min_salary', 'max_salary', 'date_posted']
    jobs = read('src/jobs.csv')
    sort_by(jobs, CRITERIA[2])
    try:
        for ind in range(len(jobs) - 1):
            data1 = datetime.strptime(jobs[ind][CRITERIA[2]], "%Y-%m-%d")
            data2 = datetime.strptime(jobs[ind + 1][CRITERIA[2]], "%Y-%m-%d")
            assert data1 > data2
    except Exception:
        assert False
