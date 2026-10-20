#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path
import pandas as pd

ROOT = Path.cwd().parent if Path.cwd().name == 'notebooks' else Path.cwd()
departments = pd.read_csv(ROOT / 'data' / 'departments.csv')
employees = pd.read_csv(ROOT / 'data' / 'employees.csv')

display(departments)
display(employees.head())


# In[2]:


print('Number of departments:', len(departments))
print('Total department budget:', departments['budget'].sum())
display(departments.sort_values('budget', ascending=False))


# In[3]:


get_ipython().run_line_magic('timeit', "departments['budget'].sum()")


# In[4]:


if 'department' in employees.columns:
    display(employees.groupby('department').size().rename('employee_count'))
else:
    print('No department column in employees.csv. Columns:', employees.columns.tolist())

if 'city' in employees.columns:
    display(employees.groupby('city').size().rename('employee_count'))

