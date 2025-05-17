# String methods

#1. upper(): To print characters in upper case
x = "united states of america"
print(x.upper())

#2. lower(): To print characters in lower case
x = "UNITED STATES OF AMERICA"
print(x.lower())

#3. capitalize(): To capitalize the 1st character of the string
x = "united states of america"
print(x.capitalize())

#4. title(): To capitalize the 1st character of each word in a string
x = "united states of america"
print(x.title())

#5. swapcase(): It swaps the case
x = "uNITED sSTATES oF aMERICA"
print(x.swapcase())

#6. replace(): It is used to replace a portion of a string
x = "Java is easy and Java is an object oriented programming"
print(x.replace("Java", "Python"))

#7. count(): To count the number of occurances of a sub-string or a character
x = "hello hello hello how are you?"
print(x.count("hello"))
print(x.count("h"))

#8. strip(): It is used to remove the blankspaces before and after the string
x = "        Python Programming        "
print(x)
print(x.strip())

#9. format(): It is used to substitue the string
x = "{} is object oriented programming"
print(x.format("Python"))

x = "My name is {} and I live in {}"
print(x.format("Prateek", "USA"))

x = "{},{},{} are the trending technologies"
print(x.format("Python", "Java","AWS"))

#10. find(): It is used to check whether a substring is available or not, If found, it returns the 1st character index position else it returns -1
x = "Python is easier than Java sdfsdhf Java"
print(x.find("is"))

#11. split(): To split the string based on the delimiter
x = "Good Evening USA"
y = x.split(" ")
print(y, type(y))

x = "101,Nagarjun,102,Prateek,1003,Geetha"
print(x.split(","))

#12. startswith():
x = "Python is easier than Java"
print(x.startswith("Java"))

#13. endswith():
x = "Python is easier than Java"
print(x.endswith("Java"))

#14. join(): To join the string within a collection
x = ["08","05","2025"]
result = "-".join(x)
print(result)

emps = ["Nag","Prateek","Geetha"]
print(" ".join(emps))

#15. isalpha(): It returns True if all the characters with in the string are alphabets else it returns False
x = "UnitedStates"
print(x.isalpha())

#16. isdecimal(): It returns True if all the characters within the string are numeric
pi = "3141"
print(pi.isdecimal())

#17. isalnum(): It returns True if all characters within the string are either alphabets or numerics or combination of both
x = "121 2121"
print(x.isalnum())

