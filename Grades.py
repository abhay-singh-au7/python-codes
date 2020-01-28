s1=int( input("enter the value of subject1: "))
s2= int(input("enter the value of subject2: "))
s3= int(input("enter the value of subject3: "))
s4= int(input("enter the value of subject4: "))
s5= int(input("enter the value of subject5: "))
perc = int(s1+s2+s3+s4+s5)/5
print(perc)

if (perc >=90):
    print ("Grade A")
elif (perc >70 or perc <90):    
     print("Grade B")
elif (perc >50 or perc <70):
    print("Grade C")
elif (perc >30 or perc <50):
    print("Grade D")
else:
        print("Grade E")


        
