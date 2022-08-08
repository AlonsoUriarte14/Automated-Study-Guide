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
def writeTitle(file : TextIOWrapper, country: str):
    
    file.write(' '*25 + '\n')
    file.write(' '*25 + country.upper() + ':\n')
    file.write(' '*25 + '\n')
    
def main():
    """
    Summary: main function to be executed.
    """
    df = read_csv(getcwd() + '\\Data\\countries of world.csv')
    COUNTRIES : list = df.Country
    SUBJECTS : list = ['Social Customs', 'Social Issues', 'Economic Status', 
                       'Sovreignty', 'Status Quo', 'Civil Rights Issues'] 
    output_file : TextIOWrapper = open(getcwd()  + '\\links\\Result Study Guide.txt', 'w+')
    
    for country in COUNTRIES:
        writeTitle(output_file, country)
        
        for subject in SUBJECTS:
            query : str = f'{country}  {subject}'

            #always gonna be just 3 therefre its O(1)
            for result in search(query=query, num=1, stop=3):
                line : str = f'--{subject}: {result}\n' 
                output_file.write(line)
                output_file.flush()
    
    output_file.close()
if __name__ == '__main__':
    main()

    
