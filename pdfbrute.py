from PyPDF2 import PdfFileReader


def getPDFFileName():
    return input("Enter path to PDF File: ")

def getPasswordList():
    print("Enter path to a password list  or leave black to use default rockyou.txt")
    return input("Enter path to password list: ")


def main():
    pdfFileName=getPDFFileName()

    #get password list or use default
    passwFile = getPasswordList() or "rockyou.txt"

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