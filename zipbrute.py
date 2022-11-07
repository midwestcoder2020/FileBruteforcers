import zipfile

def getZipFileName():
    return input("Enter path to zipfile: ")

def getPasswordList():
    print("Enter path to a password list  or leave black to use default rockyou.txt")
    return input("Enter path to password list: ")

def main():
    zipName=getZipFileName()
    #init zip file object
    zF = zipfile.ZipFile(zipName)

    #get password list or use default
    passwFile = getPasswordList() or "rockyou.txt"

    #load passwords
    #opens handle to password file to minimize memory overhead
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