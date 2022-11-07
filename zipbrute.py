import zipfile
import os

def getZipFileName():
    return input("Enter path to zipfile: ").strip()

def getPasswordList():
    print("Enter path to a password list  or leave black to use default rockyou.txt")
    return input("Enter path to password list: ").strip()

def assembleFiles():
    print("Getting passwords...")
    data=[]
    if not os.path.exists("./rockyou.txt"):
        for x in os.listdir("./"):
            if "rockyou_" in x:
                data.extend(open(x,"r",encoding="utf-8",errors='ignore').readlines())
                print(len(data))
    else:
        data.extend(open('rockyou.txt', "r", encoding="utf-8", errors='ignore').readlines())

    return data


def main():
    zipName=getZipFileName()
    #init zip file object
    zF = zipfile.ZipFile(zipName)

    #get password list or use default
    passwFile = getPasswordList() or assembleFiles()

    #load passwords
    #opens handle to password file to minimize memory overhead
    if type(passwFile).__name__ == "list":
        for p in passwFile:
            print(p.strip())  # REMOVE FOR INCREASED PERFORMANCE
            try:
                zF.extractall(pwd=p.strip().encode())
            except:
                continue
            else:
                print("Password found:", p)
                exit(0)
    else:
        with open(passwFile) as passwords:
            for p in passwords:
                print(p.strip()) # REMOVE FOR INCREASED PERFORMANCE
                try:
                    zF.extractall(pwd=p.strip().encode())
                except:
                    continue
                else:
                    print("Password found:", p)
                    exit(0)
        passwords.close()

if __name__ == '__main__':
    main()
