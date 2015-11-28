import re

#Takes a beautiful soup string str and an int n, and returns the top n names in str as an array of strings sorted by the number of times each name appears
def names(str, n):
    possibleNames = re.findall('(Mr. |Ms. |Mrs. |Dr. )?([A-Z][a-z]+ )([A-Z] |[A-Z]. |[A-Z][a-z]+ )?([A-Z][a-z]+)',txt) #gets all possible names
    
    doc = open("names.csv", 'r')
    fN = doc.read().split("\n") #list of well-known first names
    doc.close()
    
    occurences = {} #will be a dict consisting of names as keys, and number of occurences as values
    for(name in possibleNames):
        nameParts = name.split(' ')
        if((nameParts[0] in fN) || (nameParts[0] in ["Mr.","Ms.","Mrs.","Dr."] && nameParts[1] in fN)): #checks if possible names are actual names
            if(name in occurences.keys()):
                occurences[name] += 1
            else:
                occurences[name] = 1
    
    i=occurences.values()[0]
    for(j in occurences.values()):
        if(j>i):i=j
    
    out = []
    while(n && i):
        for(NOT in occurences.items()): #NOT is a Name,Occurences Tuple
            if(NOT[1]==i && n):
                out.append(NOT[0])
                n-=1
        i-=1

    return out
