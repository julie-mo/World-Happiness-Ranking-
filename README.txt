**Overview**

This project aims to find out if there is a strong visual correlation between the happiness score of a country and its respective healthy life expectancy. 

- Data source: 'World Happiness Ranking 2017.csv'
- Point of interest: Does longitivity equal happy life?




**Design Choices**

*Creating data definitions for Country and List[Country]* : 

From systematic progarm design, I have learned that it is imperitive to create data definitions that will properly store the information that will be read from a file. All the data listed in the file is organized by country, and since I need to access the happiness score and healthy life expectancy of each country, a compound data definition that includes information about a country's name, happiness score, and healthy life expectancy was created. In order to analyze the information of multiple countries, a data definition for a list of countries was also created.

*Creating a scatter plot*: 

I have learned that sometimes it is more efficient to represent information in a visual form. Although line plots are also possible for this project, a problem with line plots are that the x-values (healthy life expectancy) needed to be aligned and sorted in ascending order for the line to be visually pleasing and understandable. Since this is not possible when reading from a file, I decided that a scatter plot would be easier to visualize. 

*Using helper functions*:

In systematic program design, it is important to use helper functions in the analysis step of designing functions so that it follows the rule of 'one task per function.'  I decided to use helper functions to 1. plot the graph, 2. get lists of numbers used as x and y values. This is so that instead of accessing individual fields in the Country NamedTuple when creating the plot, I can just call the helper functions to access the x and y values. As well, if I wanted to change what my program produced and for example switch the x and y axis, I can do that easily without changing much code. 


**Problem Solving**

1. extract relevant information from the file "world_happiness_ranking_2017.csv" 
2. store extracted information as a list of countries
3. create 2 helper functions that each access the happiness scores and healthy life expectancies from the list of countries and stores them as list of floats
4. design a function that plots happiness scores over healthy life expectancy
5. call the helper functions in the analyze function
6. calling read and analyze function in the main function so the analyze function can use information extracted in the read function

Below includes a visual of the problem that the program solves


**Most Challenging**

The most difficult parts of the project were centered around helper functions. I did not know how many would be enough or what each of the helper functions should do. As well, it was difficult to come to a decision to create a scatter plot instead of a line plot. It was difficult to sort the list of values obtained in the helper functions in ascending order, and it was nearly impossible for me to match the other list of values to the previous sorted list so that each data point was still the same, just in different order. 

** Future Work**

In the future, I can use concepts learned in systematic programming design to solve other problems regarding the world happiness ranking. For example, a visualization of happiness score over GDP per Capita, or freedom, or even how different factors like trust in government and generosity compare to the happiness score of each country. As well, I can analyze the average happiness score over multiple years for a few select countries to see how they change over time with consideration to poliltical climate, economy, etc. Additionally, I can first find the happiness score difference over a period of time versus the change in healthy life expectancy over the few years, and see if those have any correlation to each other. 


