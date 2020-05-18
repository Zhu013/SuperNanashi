

def printGreen(mess):
    str =  "\033[32m "+mess+" \033[0m"
    print(str)

def printRed(mess):
    str =  "\033[31m "+mess+" \033[0m"
    print(str) 


def printYellow(mess):
    str =  "\033[33m "+mess+" \033[0m"
    print(str)

def printBlue(mess):
    str =  "\033[34m "+mess+" \033[0m"
    print(str)

def printPurple(mess):
    str =  "\033[35m "+mess+" \033[0m"
    print(str)

def printSkyBlue(mess):
    str =  "\033[36m "+mess+" \033[0m"
    print(str)

if __name__ == '__main__':
    mess="hello"
    printBlue(mess)
    printPurple(mess)
    printSkyBlue(mess)

