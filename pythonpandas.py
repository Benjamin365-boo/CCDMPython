import pandas as pd
import matplotlib.pyplot as plt
courselist = ("CCIT,CCDM,CCNS")
courseID = (101,102,103)

#to use pandas dataframe functions
#create a dictionary
courseDict = {'course':courselist,'ID':courseID}

#use function -->DATAFRAME
myvariable = pd.DataFrame(courseDict)
#print(myvariable)

#Panda Series
myvariable2 = pd.Series(courseDict)
#print(myvariable2)

#reading csv files
pulsedata = pd.read_csv('pulse.csv')
#print(myvariable3)

#to remove empty cells or null values
update1 = pulsedata.dropna() 
#print(update1)

#changing date format
update2 = pd.read_csv('pulse.csv')
update2['Date'] = pd.to_datetime(update2["Date"])
#YYY-MM-DD
#print(update2)

#change values
pulsedata.loc[10,'pulse'] = 111
#print(pulsedata)

#using MatPlot and pandas
pulsedata = pd.read_csv('Pulse.csv')
#pulsedata. plot(kind='scatter', x = 'Duration', y='Calories')
#plt.show()

#histrogram
#pulsedata["Duration"].plot(kind='hist')
#plt.show()
pulsedata["Duration"].plot(kind='pie')
plt.show()

