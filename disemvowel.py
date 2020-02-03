#SOLUTION 1-
def disemvowel(string):
    for i in 'aeiouAEIOU':
        string=string.replace(i,"")
    
    return string



#SOLUTION 2-

def disemvowel(string):
    vowels=('a','e','i','o','u','A','E','I','O','U')
    for i in string:
        if i in vowels:
            string=string.replace(i,"")
    
    return string
