import os, time
import weibo

def again():
    time.sleep(3)
    clr()
    main()

def letMeKnow():
    for i in range(10):
        print('* ' * i+'\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def main():
    weibo.main()
    try:
        files = open("iKnow.txt", "r")
    except:
        print('error')
    isOK = files.read()
    if isOK == "OK":
        print("\nIt says %s"%isOK)
        letMeKnow()
    else:
        print("\nIt says %s"%isOK)
        again()

if __name__ == '__main__':
    main()