#print("hi")
import pandas as pd
import matplotlib.pyplot as plt

course = {'course':["CCIT","CCDM","CCNS"],'courseID':[101,102,103]}

myvar = pd.DataFrame(course)   #accessing Dataframe function (becomes a method when used)
#print(myvar)

#second approach

courselist = ["CCIT","CCDM","CCNS"]
courseIDlist = [101,102,103]
courseDict = {'course':courselist,'courseID':courseIDlist}
myvariable = pd.DataFrame(courseDict)
#print(myvariable)

#pandas series
myvariable2 = pd.Series(courseIDlist)
#print(myvariable2)

#naming index
myvariable3 = pd.DataFrame(courseDict, index = ["C1","C2","C3"])
#print("\n")
#print(myvariable3)

#locating C2
#print("\n")
#print(myvariable3.loc["C2"])

#importing csv file into a dataframe
myvariable4 = pd.read_csv('student.csv')
#print(myvariable4.head(7))  #Analyze dataframes using head method

#Cleaning data
#----------------------------------------------------------------------------------------
pulsedata = pd.read_csv('PulseCopy.csv')
#print(pulsedata.head(20))

#with No empty cell
update1 = pulsedata.dropna()
#print(update1)    #drops empty rows like for date 28th/12/2020

#replace null values
update2 = pd.read_csv('Pulse.csv')
update2['Date'] = pd.to_datetime(update2["Date"])
#print(update2.to_string())    #changes date to format YYYY-MM-DD

#replace emptynull values with 222 --> lines 25,29,33
pulsedata = pd.read_csv('PulseCopy.csv')
pulsedata.fillna(222, inplace=True)
#print(pulsedata)
"""print(pulsedata.duplicated()) SKIP
above line returns true for any duplicate value

removing  duplicates __SKIP
pulsedata.drop_duplicates(inplace=True)
print(pulsedata)"""

#replace Pulse value with 111 for date 16/12/2020
pulsedata.loc[16,'Pulse']=111
#print(pulsedata)

#using mathplot ---------------------------------------------------------------
pulsedata = pd.read_csv('Pulse.csv')
#pulsedata.plot(kind='scatter',x='Duration',y='Calories')
#plt.show()

#histogram
#pulsedata["Duration"].plot(kind='hist')
#plt.show()

#Pie chart
#pulsedata["Pulse"].plot(kind='pie')
#plt.show()


 