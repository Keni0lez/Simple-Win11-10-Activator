import os
import time 

print(" ")
print("""
1. Windows 10 
2. Windows 11
3. Other (old)
""")
inputwin = int(input("Choose Windows: "))

if inputwin == 3:
    os.system('cls')
    print("Coming soon...")
    time.sleep(5)
    
if inputwin == 1:
        os.system('cls')
        print(" ")
        print("""
        Windows 10

        1. Pro
        2. Home
        3. LTSC
        4. Home N
        5. Home Single Language
        6. Home Country Specific
        7. Pro N
        8. Education
        9. Education N
        10. Enterprise
        11. Enterprise N


        """)
        inputusr = int (input("                                                  Choose edition: "))

        if inputusr == 1:
            os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
            os.system("slmgr /skms kms8.msguides.com")
            os.system("slmgr /ato")

        if inputusr == 2:
            os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
            os.system("slmgr /skms kms8.msguides.com")
            os.system("slmgr /ato")


        if inputusr == 3:
            os.system("slmgr.vbs /ipk M7XTQ-FN8P6-TTKYV-9D4CC-J462D")
            os.system("slmgr.vbs /skms kms.msgang.com")
            os.system("slmgr.vbs /ato")


        if inputusr == 4:
            os.system("slmgr.vbs /ipk 3KHY7-WNT83-DGQKR-F7HPR-844BM")
            os.system("slmgr.vbs /skms kms.msgang.com")
            os.system("slmgr.vbs /ato")


        if inputusr == 5:
            os.system("slmgr.vbs /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH")
            os.system("slmgr.vbs /skms kms.msgang.com")
            os.system("slmgr.vbs /ato")


        if inputusr == 6:
            os.system("slmgr.vbs /ipk PVMJN-6DFY6–9CCP6–7BKTT-D3WVR")
            os.system("slmgr.vbs /skms kms.msgang.com")
            os.system("slmgr.vbs /ato")


        if inputusr == 7:
            os.system("slmgr.vbs /ipk MH37W-N47XK-V7XM9-C7227-GCQG9")
            os.system("slmgr.vbs /skms kms.msgang.com")
            os.system("slmgr.vbs /ato")


        if inputusr == 8:
            os.system("slmgr.vbs /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")
            os.system("slmgr.vbs /skms kms.msgang.com")
            os.system("slmgr.vbs /ato")


        if inputusr == 9:
            os.system("slmgr.vbs /ipk 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ")
            os.system("slmgr.vbs /skms kms.msgang.com")
            os.system("slmgr.vbs /ato")


        if inputusr == 10:
            os.system("slmgr.vbs /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
            os.system("slmgr.vbs /skms kms.msgang.com")
            os.system("slmgr.vbs /ato")


        if inputusr == 11:
            os.system("slmgr.vbs /ipk DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4")
            os.system("slmgr.vbs /skms kms.msgang.com")
            os.system("slmgr.vbs /ato")




        print("Please wait 10 seconds")
        print("1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("5")
        time.sleep(1)
        print("6")
        time.sleep(1)
        print("7")
        time.sleep(1)
        print("8")
        time.sleep(1)
        print("9")
        time.sleep(1)
        print("10")
        time.sleep(2)


if inputwin == 2:
        os.system('cls')
        print(" ")
        print("""
        Windows 11

        1. Pro
        2. Home
        3. Education
        4. Enterprise
        5. For Workstations
        """)
        inputusr11 = int (input("                                                  Choose edition: "))
        
if inputusr11 == 1:
    os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
    os.system("slmgr /skms kms8.msguides.com")
    os.system("slmgr /ato")

if inputusr11 == 2:
    os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
    os.system("slmgr /skms kms8.msguides.com")
    os.system("slmgr /ato")

if inputusr11 == 3:
    os.system("slmgr.vbs /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")
    os.system("slmgr.vbs /skms kms.msgang.com")
    os.system("slmgr.vbs /ato")

if inputusr11 == 4:
    os.system("slmgr.vbs /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
    os.system("slmgr.vbs /skms kms.msgang.com")
    os.system("slmgr.vbs /ato")

if inputusr11 == 5:
    os.system("slmgr /ipk NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J")
    os.system("slmgr /skms kms8.msguides.com")
    os.system("slmgr /ato")