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
        exit(-1)
    lines = files.readlines()
    foo = []
    for line in lines:
        foo.append(line)
    files.close()
    isOK = foo[0]
    ls2 = [str(i) for i in foo]
    ls3 = ''.join(ls2)
    print('已经存储的内容：\n'+ls3)
    if isOK == "OK\n":
        print("\nIt says %s"% isOK)
        autoEmail.email('JWC has just posted new Weibo!' ,time.ctime()+'\nRecent posts:\n'+ls3)
        time.sleep(10800)
        delete("iKnow.txt")
        again()
    else:
        print("\nIt says %s"% isOK)
        again()

if __name__ == '__main__':
    main()