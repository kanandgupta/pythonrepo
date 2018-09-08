tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "abc", 'b', 'c', 'd' ;

print tup1 [0:3]
print tup1 [1:3]
print tup1 [-4:0]

print tup1 [::-1]
for tup4 in reversed(tup1):
    print tup4,
    
del tup3 [0:1]

print tup3    

#print tup2 [0:4]
    
#tuple does not allow to insert new values 