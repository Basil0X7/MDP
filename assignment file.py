import numpy as np

s1= 0
s2= 0
s3= 0

A1 = [[0.001,0,0.999],[0.001,0.999,0],[0,0,0]]
A2 = [[0,0,0],[0,0,0],[0.001,0,0.999]]
A3 = [[0,0,0],[0,0,0],[0,0,0]]
R1 = 100
R2 = 90
R3 = 11
discount = 1
discount2 = 0.9

print("_______________________________________")
print("t 0 for the ss1a1 is :", s1)
print("t 0 for the ss1a2 is :", s2)
print("t 0 for the ss1a3 is :", s3)
print("_______________________________________")
for i in range(5):

    s1a1 = ((A1[0][0] * (R1 + discount * s1)) + (A1[0][1] * (R1 + discount * s2)) + (A1[0][2] * (R1 + discount * s3)))
    s1a2 = ((A1[1][0] * (R2 + discount * s1)) + (A1[1][1] * (R2 + discount * s2)) + (A1[1][2] * (R2 + discount * s3)))
    s1a3 = ((A1[2][0] * (R3 + discount * s1)) + (A1[2][1] * (R3 + discount * s2)) + (A1[2][2] * (R3 + discount * s3)))

    s2a1 = ((A2[0][0] * (R1 + discount * s1)) + (A2[0][1] * (R1 + discount * s2)) + (A2[0][2] * (R1 + discount * s3)))
    s2a2 = ((A2[1][0] * (R2 + discount * s1)) + (A2[1][1] * (R2 + discount * s2)) + (A2[1][2] * (R2 + discount * s3)))
    s2a3 = ((A2[2][0] * (R3 + discount * s1)) + (A2[2][1] * (R3 + discount * s2)) + (A2[2][2] * (R3 + discount * s3)))

    s3a1 = ((A3[0][0] * (R1 + discount * s1)) + (A3[0][1] * (R1 + discount * s2)) + (A3[0][2] * (R1 + discount * s3)))
    s3a2 = ((A3[1][0] * (R2 + discount * s1)) + (A3[1][1] * (R2 + discount * s2)) + (A3[1][2] * (R2 + discount * s3)))
    s3a3 = ((A3[2][0] * (R3 + discount * s1)) + (A3[2][1] * (R3 + discount * s2)) + (A3[2][2] * (R3 + discount * s3)))


    print("t", i ,"for s1 when take a1 :",s1a1)
    print("t", i ,"for s1 when take a2 :",s1a2)
    print("t", i ,"for s2 when take a3 :",s2a3)



    s1 = max(s1a1,s1a2,s1a3)
    s2 = max(s2a1,s2a2,s2a3)
    s3 = max(s3a1,s3a2,s3a3)
    print("t", i, "for s3 when take any a", s3)
    print("_______________________________________")

s1= 0
s2= 0
s3= 0

for i in range(5):

    s1a1 = ((A1[0][0] * (R1 + discount2 * s1)) + (A1[0][1] * (R1 + discount2 * s2)) + (A1[0][2] * (R1 + discount2 * s3)))
    s1a2 = ((A1[1][0] * (R2 + discount2 * s1)) + (A1[1][1] * (R2 + discount2 * s2)) + (A1[1][2] * (R2 + discount2 * s3)))
    s1a3 = ((A1[2][0] * (R3 + discount2 * s1)) + (A1[2][1] * (R3 + discount2 * s2)) + (A1[2][2] * (R3 + discount2 * s3)))

    s2a1 = ((A2[0][0] * (R1 + discount2 * s1)) + (A2[0][1] * (R1 + discount2 * s2)) + (A2[0][2] * (R1 + discount2 * s3)))
    s2a2 = ((A2[1][0] * (R2 + discount2 * s1)) + (A2[1][1] * (R2 + discount2 * s2)) + (A2[1][2] * (R2 + discount2 * s3)))
    s2a3 = ((A2[2][0] * (R3 + discount2 * s1)) + (A2[2][1] * (R3 + discount2 * s2)) + (A2[2][2] * (R3 + discount2 * s3)))

    s3a1 = ((A3[0][0] * (R1 + discount2 * s1)) + (A3[0][1] * (R1 + discount2 * s2)) + (A3[0][2] * (R1 + discount2 * s3)))
    s3a2 = ((A3[1][0] * (R2 + discount2 * s1)) + (A3[1][1] * (R2 + discount2 * s2)) + (A3[1][2] * (R2 + discount2 * s3)))
    s3a3 = ((A3[2][0] * (R3 + discount2 * s1)) + (A3[2][1] * (R3 + discount2 * s2)) + (A3[2][2] * (R3 + discount2 * s3)))


    print("t", i ,"for s1 when take a1 and discount = 0.9 :",s1a1)
    print("t", i ,"for s1 when take a2 and discount = 0.9 :",s1a2)
    print("t", i ,"for s2 when take a3 and discount = 0.9 :",s2a3)



    s1 = max(s1a1,s1a2,s1a3)
    s2 = max(s2a1,s2a2,s2a3)
    s3 = max(s3a1,s3a2,s3a3)
    print("t", i, "for s3 when take any a  and discount = 0.9 :", s3)
    print("_______________________________________")




