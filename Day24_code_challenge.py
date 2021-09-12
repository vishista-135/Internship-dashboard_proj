import re
from glob import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
filenames = glob('baby_names/*.txt')    
ssa_df_list = []
for file in filenames:
    temp_df = pd.read_csv(file, names = ['names','sex','count'])
    year = int(re.findall('\d\d\d\d', file)[0])
    
    if year > 2010:
        break   
    temp_df['year'] = year
    ssa_df_list.append(temp_df)
finaldf = pd.concat(ssa_df_list, axis = 0, ignore_index = True)

#task 02: Display the top 5 male and female baby names of 2010.

df_2010 = finaldf[finaldf['year'] ==  2010]
female_names = df_2010[df_2010['sex'] == 'F']
female_names_sort_by_count = female_names.sort_values('count', ascending = False, ignore_index = True)

print (female_names_sort_by_count['names'][0:5]) 

male_names = df_2010[df_2010['sex'] == 'M']
male_names_sort_by_count = male_names.sort_values('count', ascending = False, ignore_index = True)

#top five female names of 2010
print (male_names_sort_by_count['names'][0:5]) 

#task 03:     Calculate sum of the births column by sex as the total number of births  
#in that year(use pandas groupby method).

grouped_multiple = finaldf.groupby(['year', 'sex']).agg({'count': ['sum']})
print(grouped_multiple)

#task 04: Plot the results of the above activity to show total births  by sex and year.

grouped_multiple.plot(kind='bar')
grouped_multiple[0:10].plot(kind='bar')

