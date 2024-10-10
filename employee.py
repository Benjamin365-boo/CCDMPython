import pandas as pd
import matplotlib.pyplot as plt

#exercises
#q1- create new object call Empdata to read employees.csv file
Empdata = pd.read_csv('employees.csv')
#print('employees.csv')

#q2- create new object called nonull to remove empty/null space Use dropna()
nonull = Empdata.dropna()
#print(nonull)
#qst how many rows was dropped? '764 rows'

#q3 create new object EmpStartDate to format date to YYYY-MM-DD
EmpStartDate = pd.read_csv('employees.csv')
EmpStartDate['Start Date'] = pd.to_datetime(EmpStartDate["Start Date"])
#print(EmpStartDate)

#q4
Salary = pd.read_csv('employees.csv')
Salary["Salary"].plot(kind='hist')
plt.show()
#answer 12000 to 14000
