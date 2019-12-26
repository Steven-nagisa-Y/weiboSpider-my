import os, time
import weibo, autoEmail

def again():
    time.sleep(600)
    clr()
    main()
    
def delete(file):
    if os.name == 'nt':
        os.system('del /f /q '+file)
    elif os.name == 'posix':
        os.system('rm -f '+file)

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
    lines = files.readlines()
    i = 0
    for line in lines:
        foo[i] = line
    if isOK == "OK":
        print("\nIt says %s"%isOK)
        autoEmail.email('JWC has just posted new Weibo!' ,time.ctime())
    else:
        print("\nIt says %s"%isOK)
        again()

if __name__ == '__main__':
    main()