#Problem 3-1 Trikon
#Name- Prakhar Singhania


#==================== A =============================

print('Following is the output for A')

z = 4
for i in range (0,5):
    for j in range(0, z): 
        print(" ", end = "")
    for k in range(i, -1, -1):
        print(k, end = "")
    z = z - 1
    print(" ")

#I have replaced i and z in range.
#put z because i need z times space before element that 4 in first, 3 in second and so on...
# put i bin k range because i need elements from small to big. 0,1,2,,,,


#==================== B ===========================

print('') #just to have extra line between 2 outputs for clarity
print('Following is the output for B')

z = 0
for i in range (0,5):
    for j in range(0, z):
        print(" ", end = "")
    for k in range(0, i+1): #reversed direction of numbers as i want increasing array from left side..k will print 0 first time, 01 second and so on..
        print(k, end = "")
    z = z - 1
    print(" ")

#reason to interchange same as in A

#===================== C ===========================
print('') #just to have extra line between 2 outputs for clarity
print('Follwing is the output for C')
z = 4
for i in range (0,5):
    for j in range(0,-i): #called negative integers in range to get the spacing and line break on right side.
        print(" ", end = "")
    for k in range(0, z+1): #changed range from 0,z+1 as we want 0 near straight line and increasing thereatfer with stepsize 1 
        print(k, end = "")
    z = z - 1
    print(" ")


#(b) Follwoing is code for output D

#=================== D ============================

print('') #just to have extra line between 2 outputs for clarity
print('Follwoing is the output for D')
z = 4
for i in range (0,5):
    for j in range(z, -1, -1):
        print(" ", end = " ")
    z= z-1
    print(i)
    print(" ")

   
