seq=(145,"abcd",'a',168) 
data=list(seq) 
print( "List formed is : ",data ) 


data = [786,'abc','a',123.5] 
print( "Index of 123.5:", data.index(123.5) ) 
print( "Index of a is", data.index('a') ) 

data = [786,'abc','a',123.5,786,'rahul','b',786] 
print( "Number of times 123.5 occured is", data.count(123.5) ) 
print( "Number of times 786 occured is", data.count(786) )  


data1=['abc',123,10.5,'a'] 
data2=['ram',541] 
data1.extend(data2) 
print( data1 ) 
print( data2 ) 
