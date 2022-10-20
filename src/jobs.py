from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    if not path.endswith('.csv'):
        raise ValueError('Formato inválido!')
    with open(path, encoding='utf-8') as file:
        read_file = csv.reader(file, delimiter=',')
        header, *data = read_file
    result_list = []
    for row in data:
        dict_result = {}
        for ind, elem in enumerate(row):
            dict_result[header[ind]] = elem
        result_list.append(dict_result)

    return result_list
