
s1=90; s2=80; s3=40; s4=40;s5=40

tot = s1+s2+s3+s4+s5
print("TOTAL: ", tot)
per = (tot/500)*100
print("PERCENTAGE: ", per, "%")

if s1>=40 and s2>=40 and s3>=40 and s4>=40 and s5>=40:
    print("RESULT: PASS")
    if per>=70:
        print("FIRST CLASS WITH DISTINCTION")
    elif per>=60:
        print("FIRST CLASS")
    elif per>=50:
        print("SECOND CLASS")
    elif per>=40:
        print("THIRD CLASS")
else:
    print("RESULT: FAIL")
