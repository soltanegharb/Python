#Python project1 writing a code that get a string ( in any size but only letters ), and a number, then  move forward the letters by the given number. if number is greater than 26 start over from letter a.

#make the dictionary of English letters by their index starting from 1

engAlphLetter = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,
                 "r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

engAlphNumber = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",
                 18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
#input the string

usrStr = (input("please input your string to be forwarded then press Enter button\n")).lower()
test=0
while test==0:
    testChar = None
    for testChar in usrStr:
        if testChar not in engAlphLetter:
            usrStr = (input("please input your string alphabetical letters from a-z\n")).lower()
            test = 0
            break

        else:
            test = 1

#input the number

while True:
    try:
        usrNum = int(input("please input your number, numerical from 0-9\n"))
        break
    except ValueError:
        pass
usrNum = int(usrNum)

#process the user input and solve the problem

new_usrStr = []
usrStr_listed = list(usrStr)
for c in usrStr_listed:
    new_var = engAlphLetter[c] + usrNum
    if new_var>26:
        new_var_edited = new_var%26
        new_c = engAlphNumber[new_var_edited]
    else:
        new_c = engAlphNumber[new_var]
    new_usrStr.append(new_c)

output = "".join(new_usrStr)
print(output)
