import os
import pyAesCrypt


def getFileName():
    return input("Enter path to aescrypt file: ").strip()

def getPasswordList():
    print("Enter path to a password list  or leave black to use default rockyou.txt")
    return input("Enter path to password list: ").strip()

def assembleFiles():
    print("Getting passwords...")
    data=[]
    if not os.path.exists("./rockyou.txt"):
        for x in os.listdir("./"):
            if "rockyou_" in x:
                data.extend(open(x,"rt",encoding="utf-8",errors='ignore').readlines())
                print(len(data))
    else:
        data.extend(open('rockyou.txt', "rt", encoding="utf-8", errors='ignore').readlines())

    return data

def main():
    fName=getFileName()

    if not os.path.exists(fName):
        print("File Name Found")
        exit(0)

    fNameF = fName.replace(".aes","")

    #get password list or use default
    passwFile = getPasswordList() or assembleFiles()

    #load passwords
    #opens handle to password file to minimize memory overhead
    if type(passwFile).__name__ == "list":
        for p in passwFile:
            print(p.strip())  # REMOVE FOR INCREASED PERFORMANCE
            try:
                pyAesCrypt.decryptFile(fName,fNameF,p.strip())
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
                    pyAesCrypt.decryptFile(fName, fNameF, p.strip())
                except:
                    continue
                else:
                    print("Password found:", p)
                    exit(0)
        passwords.close()

if __name__ == '__main__':
    main()