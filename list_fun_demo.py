list1=[10,20] 
list2=[30,40] 
list3=list1+list2 
print( list3 ) 


list1=[10,20] 
print( list1*2 )


list1=[1,2,4,5,7] 
print( list1[0:2] ) 
print( list1[4] ) 
list1[1]=9 
print( list1 )


data1=[5,10,15,20,25] 
print( "Values of list are: " ) 
print( data1 ) 
data1[2]="Multiple of 5" 
print( "Values of list are: " ) 
print( data1 )


list1=[10,"rahul",'z'] 
print( "Elements of List are: " ) 
print( list1 ) 
list1.append(10.45) 
print( "List after appending: " ) 
print( list1 ) 


list1=[10,'rahul',50.8,'a',20,30] 
print( list1 ) 
del list1[0] 
print( list1 ) 
del list1[0:3] 
print( list1 ) 

list1=[101,981,'abcd','xyz','m'] 
list2=['aman','shekhar',100.45,98.2] 
print( "No. of elements in List1: ",len(list1)) 
print( "No. of elements in List2: ",len(list2) )
