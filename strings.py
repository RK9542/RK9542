# this file runs throught the concepts of Strings
name = "Ravi"
print ("Hello, " + name)
#Using Multi line strings
Sentence = """Hi Ravi, How are you?
My Name is Python.
Hope everything is going well wuth Python programming."""
print(Sentence)
#Looping through the strings
for character in name:
    print(character)

fruit = "Mango"
len1 = len(fruit)
print ("Mango is a", len1, "character word")


pie = "Applepie"
print (pie[0:5])
print (pie[0:4])
print (pie[0:-4])
print (pie[-4:-2])
print (pie[6]) #returns character at speciefied index

nm = "Harry"
print (nm[-4:-2])

str1 = "AbcdEFGHij"
print (str1.upper())
print (str1.lower())

str1 = " Hello Ravi "
print (str1.strip())

str2 = "Hello !!!"
print (str2.rstrip("!"))
str3 = "Hello |||"
print (str3.rstrip("|"))

str4 = "Silver spoon in Mars"
print (str4.replace("sp" , "M"))
print (str4.split(" "))

str5 = "hello"
print (str5.capitalize())
str6 = "hello WorlD"
print (str6.capitalize())

str7 = "!!!Welcome to the Console!!!"
print (str7.center(100))
print (str7.center(100 , "."))

countstr = str7.count("o")
print (countstr)

print (str7.endswith("!!!"))
print (str7.endswith("to" , 8, 13))
print (str7.find("to"))
print (str7.find("Ravi"))
print (str7.index("to"))
#print (str7.index("Ravi"))

str8 = "welcometopythonprogramming"
print (str8.isalnum())


str9 ="WelcometoPythonProgramming"
print (str9.isalpha())
str10 ="Welcome2PythonProgramming"
print (str10.isalpha())

str11 = "welcome to python programming"
print (str11.islower())
print (str11.isupper())

str12 = "Welcome to python programming"
print (str12.islower())
print (str12.isupper())

str13 = "WELCOME TO PYTHON PROGRAMMING\n"
print (str13.islower())
print (str13.isupper())
print (str13)
print (str13.isprintable())

str14 = "WELCOME TO PYTHON PROGRAMMING"
print (str14.isprintable())
print (str9.isspace())
print (str14.isspace())

str15 = "           "
print (str15.isspace())

str16 = "Welcome To Python Programming"
print (str16.istitle())
print (str15.istitle())

print (str16.swapcase())
print (str12.title())









