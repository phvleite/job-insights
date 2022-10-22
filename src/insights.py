from src.jobs import read
# from jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    result = read(path)
    unique_jobs = set()

    for job_type in result:
        if job_type['job_type'] != '':
            unique_jobs.add(job_type['job_type'])

    unique_jobs_list = [job for job in unique_jobs]

    return unique_jobs_list


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """

    jobs_list = [job for job in jobs if job['job_type'] == job_type]
    return jobs_list


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    result = read(path)
    unique_industries = set()

    for industry in result:
        if industry['industry'] != '':
            unique_industries.add(industry['industry'])

    unique_industries_list = [industry for industry in unique_industries]

    return unique_industries_list


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    jobs_list = [job for job in jobs if job['industry'] == industry]
    return jobs_list


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    result = read(path)
    unique_max_salary = set()

    for reg in result:
        if reg['max_salary'] != '' and reg['max_salary'] != 'invalid':
            unique_max_salary.add(int(reg['max_salary']))

    maximo_max_salary = max(unique_max_salary)

    return maximo_max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    result = read(path)
    unique_min_salary = set()

    for reg in result:
        if reg['min_salary'] != '' and reg['min_salary'] != 'invalid':
            unique_min_salary.add(int(reg['min_salary']))

    minimo_min_salary = min(unique_min_salary)

    return minimo_min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if 'max_salary' not in job or 'min_salary' not in job:
        raise ValueError('Chave inexistente!')
    elif not isinstance(
            job['min_salary'], int) or not isinstance(
                job['max_salary'], int):
        raise ValueError('Tipo inválidos!')
    elif job['min_salary'] > job['max_salary']:
        raise ValueError('Dados inválidos!')
    if not isinstance(salary, int):
        raise ValueError("Tipo inválido!")

    result = job['min_salary'] <= salary <= job['max_salary']
    return result


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except Exception:
            continue
    return jobs_list
