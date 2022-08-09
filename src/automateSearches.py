"""
    Author: Diego A. Santiago Uriarte 
    
    Summary: Automate google searches related to politics, 
    social customs, social issues, ecoconomic status, status quo, and
    store the top three results of each subject in  a text file
    
"""
from io import TextIOWrapper
from googlesearch import search
from pandas import read_csv
from os import getcwd


def writeTitle(file: TextIOWrapper, country: str):

    file.write(' '*25 + '\n')
    file.write(' '*25 + country.upper() + ':\n')
    file.write(' '*25 + '\n')


def automateSearchOffline():
    """
    Summary: main function to be executed.
    """
    df = read_csv(getcwd() + '\\Data\\countries of world.csv')
    _COUNTRIES: list = df.Country
    _SUBJECTS: list = ['Culture', 'Social Issues', 'Economic Status',
                       'Sovreignty', 'Status Quo', 'Civil Rights Issues',
                       'Meals', 'History', 'gamers', 'Art', 'Music']
    output_file: TextIOWrapper = open(
        getcwd() + '\\links\\Result Study Guide.txt', 'w+')

    for country in _COUNTRIES:
        writeTitle(output_file, country)

        for subject in _SUBJECTS:
            # establish certain filters for the search
            minus = '-britannica -.gov  '
            query: str = f'{country}  {subject} {minus}'

            # always gonna be just 3 therefore its O(1)
            for result in search(query=query, num=1, stop=3, pause=6):
                line: str = f'--{subject}: {result}\n'
                output_file.write(line)
                output_file.flush()

    output_file.close()


def automateSearchOnline(country: str = 'Puerto Rico') -> list:

    _SUBJECTS: list = ['Culture', 'Social Issues', 'Economic Status',
                       'Sovreignty', 'Status Quo', 'Civil Rights Issues',
                       'Meals', 'History', 'gamers', 'Art', 'Music']
    result = []

    for subject in _SUBJECTS:
        # establish certain filters for the search
        minus = '-britannica -.gov  '
        query: str = f'{country}  {subject} {minus}'

        result.append(' '*25 + '\n')
        result.append(' '*20 + country.upper() + '\n')
        result.append(' '*25 + '\n')
        # always gonna be just 3 therefore its O(1)
        for link in search(query=query, num=1, stop=3, pause=6):
            line: str = f'--{subject}: {link}\n'
            result.append(line)
            print(line)

    return result

if __name__ == '__main__':
    automateSearchOnline()
