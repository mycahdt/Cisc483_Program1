import pandas as pan
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# NOTE: To look at the next histogram, you must X out
# of the first histogram that pops up.

def subsetDataFunc():

    # Reads the csv file
    myDataFrame = pan.read_csv('subset_census-income_data.csv',na_values='?')

    # Mean, median, range, variance for the Age attribute
    mean = myDataFrame['age'].mean()
    median = myDataFrame['age'].median()
    range = myDataFrame['age'].max() - myDataFrame['age'].min()
    variance = myDataFrame['age'].var()
    
    # Prints the mean, median, range, variance for the Age attribute
    print("Mean: " + str(mean))
    print("Median: " + str(median))
    print("Range: " + str(range))
    print("Variance: " + str(variance))
    
    # Histogram for Age
    plt.hist(myDataFrame['age'], edgecolor='black', bins=10)
    plt.title('Frequency of Ages')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    
    
    # Creates a new dataframe for a given set of columns in the data 
    df2 = myDataFrame.loc[:, ["age", "education-num", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "class "]]
    df2["race"] = pan.factorize(df2["race"])[0]
    df2["sex"] = pan.factorize(df2["sex"])[0]
    df2["class "] = pan.factorize(df2["class "])[0]
    
    # Covariance
    covMatrix = df2.cov()
    print(covMatrix.to_string())
    
    # Correlation
    corrMatrix = df2.corr()
    print(corrMatrix.to_string())
    
    
    # Plots the Histogram
    plt.show()
    
    

def adultDataFunc():
    
    # Reads the csv file
    myDataFrame = pan.read_csv('adultData.csv',na_values='?')
   
    # Creates a column called BUCKET which
    # Discretizes the AGE attribute by binning it into 4 equi-width intervals
    myDataFrame['BUCKET']=pan.cut(myDataFrame['AGE'],4)
    print(myDataFrame)
    
    # Histogram for Age
    plt.hist(myDataFrame['AGE'], edgecolor='black', bins=[20, 30, 40, 50, 60])
    plt.title('Frequency of Ages')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    
    # Creates a column called 2ndBucket which 
    # Discretizes the AGE attribute by binning it into 4 equi-depth (= equal-frequency) intervals
    myDataFrame['2ndBucket']=pan.qcut(myDataFrame['AGE'],q=4,precision=0)
    print(myDataFrame)
    
    # Plots the Histogram
    plt.show()
    

def main():
    subsetDataFunc()
    adultDataFunc()
    


if __name__ == '__main__':
    main()
