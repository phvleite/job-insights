from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    TAGS = ['title', 'salary', 'type']
    result = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    for job in result:
        assert TAGS[0] in job
        assert TAGS[1] in job
        assert TAGS[2] in job
