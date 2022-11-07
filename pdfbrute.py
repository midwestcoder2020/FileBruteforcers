from PyPDF2 import PdfFileReader
import os

def getPDFFileName():
    return input("Enter path to PDF File: ").strip()

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
    pdfFileName=getPDFFileName()

    #get password list or use default
    passwFile = getPasswordList() or assembleFiles()


    if type(passwFile).__name__ == "list":
        for p in passwFile:
            print(p.strip())
            file = PdfFileReader(pdfFileName)
            file.decrypt(p.strip().encode())
            try:
                file.getNumPages()
            except:
                continue
            else:
                print("Password found:", p)
                exit(0)
    else:
        #load passwords
        #opens handle to password file to minimize memory overhead
        with open(passwFile) as passwords:
            for p in passwords:
                print(p.strip())
                file = PdfFileReader(pdfFileName)
                file.decrypt(p.strip().encode())
                try:
                    file.getNumPages()
                except:
                    continue
                else:
                    print("Password found:", p)
                    exit(0)

        passwords.close()

if __name__ == '__main__':
    main()
