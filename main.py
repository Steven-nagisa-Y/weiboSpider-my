import os, time
import weibo, autoEmail

def again():
    time.sleep(3)
    clr()
    main()
    

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
        autoEmail.email('JWC post new Weibo!' ,time.ctime())
    else:
        print("\nIt says %s"%isOK)
        again()

if __name__ == '__main__':
    main()