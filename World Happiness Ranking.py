#!/usr/bin/env python
# coding: utf-8

# 1a. Information in File
# - Country name
# - Happiness Rank
# - Happiness Score
# - Whisker High
# - Whisker Low
# - Economy GDP per Capita
# - Family
# - Healthy Life Expectancy
# - Freedom
# - Generosity
# - Trust of Government Corruption
# - Dystopia Residual
# 
# 

# 1b. Description of Program Product
# 
# This program will output a visualization in the form of a scatter plot graph that shows the Happiness Score of all the listed countries plotted over its Healthy Life Expectancy in 2017.
#     
# Other possible outputs include:
# - a line graph visualization of the difference between whiskers compared to the happiness score
# - a bar graph visualization of all the happiness scores of each country
# - a bar graph visualization percentage of family contributing to the happiness score for every country in 2017
# - a line graph visualization of the correlation of Economy GDP per Capita and Happiness Score
# 

# 1c. Example of Program Product
# ![image.png](attachment:image.png)

# 2a. Data Definitions
# 
# I chose to document the columns "Country", "Happiness Score", and "Healthy Life Expectancy". By gathering a list of countries with its respective data on  happiness score and heathy life expectancy, I can then analyze that data for a possible trend or correlation between happiness score and healthy life expectancy in the analyze function in 2c. I think this is meaningful as the notion that longitivity equals a happy life is widespread.

# In[90]:


#2a.
from cs103 import *
from typing import List, NamedTuple
import matplotlib.pyplot as plt

Country = NamedTuple('Country', [('name', str),
                                 ('happiness_score', float), #in range [0,8] 
                                 ('healthy_life_expectancy', float)]) #in range [0,1]
#interp. a country with its name, happiness score and healthy life expectancy in 2017 

C1 = Country('Canada', 7.316, 0.834557652)
C2 = Country('Mexico', 6.578, 0.709978998)

def fn_for_country(c: Country) -> ...: #template based on compound
    return ...(c.name, 
              c.happiness_score, 
              c.healthy_life_expectancy)

#List[Country]
#interp. a list of countries

L0 = []
L1 = [C1]
L2 = [C1, C2]
L3 = [('United States', 6.993000031, 0.774286628), ('Paraguay', 5.493000031, 0.579250693), ('Haiti', 3.602999926, 0.27732113)]
L4 = [('Norway', 7.537000179, 0.796666503), ('Japan', 5.920000076, 0.913475871), ('South Africa', 4.828999996, 0.18708007), ('Rwanda', 3.470999956, 0.326424807)]

def fn_for_loc(loc: List[Country]) -> ...: #template based on arbitrary sized and reference rule
    #description of accumulator
    acc = ... #type: ...
    for c in loc:
        ... (acc, fn_for_country(c))
    return ... (acc)


# In[91]:


#2b.
import csv 

def main(filename: str) -> None:
    '''
    reads the file from given filename, analyzes the data, and returns None
    '''
    #return None #stub
    #template based on function composition
    return analyze(read(filename))

    
def read(filename: str) -> List[Country]:
    '''
    reads information from the specified file and returns a list of countries
    '''
    #template based on read template of function composition 
    #loc contains the result so far
    loc = [] #type: List[Country]
    
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader) #skip header line for row in reader
    
        for row in reader: 
            name = row[0]
            happiness_score = parse_float(row[2])
            healthy_life_expectancy = parse_float(row[7])
            c = Country(name,
                        happiness_score,
                        healthy_life_expectancy)
            loc.append(c)
    
    return loc


#2c.

def analyze(loc: List[Country]) -> None:
    '''
    displays a plot that shows the happiness score of a list of countries over their respective healthy life expectancies
    and returns None
    '''
    return plot_happiness_over_life_expectancy(list_of_happiness_score(loc), list_of_life_expectancy(loc))
    

def plot_happiness_over_life_expectancy(happiness_score: List[float], life_expectancy: List[float]) -> None:
    """
    display a plot of the happiness score over healthy life expectancy, where happiness is a list of all 
    the happiness score from countries, and life_expectancy is a list of all the healthy life expectancies from countries
    """
    #return None #stub
        
    #x-axis label, y-axis label, and plot title
    plt.xlabel('Healthy Life Expectancy')
    plt.ylabel('Happiness Score')
    plt.title('Happiness Score vs Healthy Life Expectancy')

    # axes range
    plt.axis([0,1,0,8])

    # data plotting and setting properties
    plt.scatter(life_expectancy, happiness_score, color = 'g', alpha = 0.5)

    # show plot
    plt.show()
    
    return None


def list_of_happiness_score(loc: List[Country]) -> List[float]:
    '''
    returns a list of happiness score from a given list of countries
    '''
    #return [] #stub
    #template from List[Country]
    
    #holds the happiness score from each country so far
    lohs = [] #type: List[float]
    
    for c in loc:
        lohs.append(c[1])
    return lohs


def list_of_life_expectancy(loc: List[Country]) -> List[float]:
    '''
    returns a list of healthy life expectancy from a given list of countries
    '''
    #return [] #stub
    #template from List[Country]
    
    #holds the healthy life expectancy from each country so far
    lole = [] #type: List[float]
    
    for c in loc:
        lole.append(c[2])
    return lole


start_testing()
#examples and tests for main
expect(main('world_happiness_ranking_2017_test1.csv'), None)
expect(main('world_happiness_ranking_2017_test2.csv'), None)

#examples and tests for read
expect(read('world_happiness_ranking_2017_test1.csv'), [('United States', 6.993000031, 0.774286628), ('Paraguay', 5.493000031, 0.579250693), ('Haiti', 3.602999926, 0.27732113)])
expect(read('world_happiness_ranking_2017_test2.csv'), [('Norway', 7.537000179, 0.796666503), ('Japan', 5.920000076, 0.913475871), ('South Africa', 4.828999996, 0.18708007), ('Rwanda', 3.470999956, 0.326424807)])

#examples and tests for analyze
expect(analyze(L3), None)
expect(analyze(L4), None)

#examples and tests for plot_happiness_over_life_expectancy
LOHS1 = list_of_happiness_score(L3)
LOHS2 = list_of_happiness_score(L4)
LOLE1 = list_of_life_expectancy(L3)
LOLE2 = list_of_life_expectancy(L4)
expect(plot_happiness_over_life_expectancy(LOHS1, LOLE1), None)
expect(plot_happiness_over_life_expectancy(LOHS2, LOLE2), None)


#examples and tests for list_of_happiness_score
expect(list_of_happiness_score(L3), [6.993000031, 5.493000031, 3.602999926])
expect(list_of_happiness_score(L4), [7.537000179, 5.920000076, 4.828999996, 3.470999956])

#examples and tests for list_of_life_expectancy
expect(list_of_life_expectancy(L3), [0.774286628, 0.579250693, 0.27732113])
expect(list_of_life_expectancy(L4), [0.796666503, 0.913475871, 0.18708007, 0.326424807])

summary()

main('world_happiness_ranking_2017.csv')




