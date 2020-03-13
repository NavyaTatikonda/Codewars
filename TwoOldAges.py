def two_oldest_ages(ages):
    #your code here
    ages.sort()
    age=ages[-2],ages[-1]
    return(list(age))
