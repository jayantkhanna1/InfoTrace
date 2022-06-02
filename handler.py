
# email spoof
# Name search
# phone number lookup
# email lookup
# ip lookup
# domain lookup
# url lookup
# hash lookup
# social media lookup
# wifi cracking
# password cracking md5,sha256,sha512 etc.

from Modules.sherlock import Sherlock_Module
from Modules.metadata import MetaDataExtractor
from Modules.iptogeo import IpLookup
from Modules.email_spoof import EmailSpoof

print("Type help to see help menu")
while(True):
    command = input(">> ")
    command=command.lower().strip()




    if command == "help" or command == "h" or command == "?" or command == "--help" or command == "-h":
        print("""
        help:
            help : show help menu
            h : show help menu
            --help : show help menu
            ? : show help menu
            -h : show help menu

        Modules:
            1. sherlock : to get inside sherlock module and search for a username accross social media sites
            2. photoinfo : to get information such as gps coordinates etc. about the image
            3. ipinfo : to get information regarding an ip address
            4. emailspoof : to Spoof an Email
        
        Get Current Directory Commands:
            pwd : to get current module
        
        Exiting command:
            exit : exit the program
        """)





    elif command == "exit":
        print("""
        Goodbye! 
        """)
        break
    



    elif command == 'pwd':
        print("""
                Main Menu
                """)





    elif command == "sherlock" or command == "1":
        print("""
        sherlock - A module to search for a user on multiple websites
        Enter Sherlock --help to see complete help menu for sherlock
        """)
        sherlock = Sherlock_Module()
        while(True):
            subcommand = input(">> Sherlock >> ")
            subcommand = subcommand.lower().strip()
            subcommandarr = subcommand.split(' ')
            if subcommand == "exit sherlock" or subcommand == 'sherlock exit' or subcommand == "exit" or subcommand == "cd ..":
                break

            elif subcommand == "pwd":
                print("""
                sherlock Module
                """)
 
            elif subcommand == "sherlock --help" or subcommand == "sherlock -h" or subcommand == "--help" or subcommand == "-h" or subcommand == "help" or subcommand == "h" or subcommand == "?": 
                print("""
                Details:
                    You are inside sherlock module. A module to search for a user on multiple websites
                
                Help Menu:
                    sherlock --help : show help menu for sherlock
                    sherlock -h : show help menu for sherlock
                    --help : show help menu for sherlock
                    -h : show help menu for sherlock
                    help : show help menu for sherlock
                    h : show help menu for sherlock
                    ? : show help menu for sherlock

                Exit sherlock:
                    exit sherlock : exit sherlock module
                    sherlock exit : exit sherlock module
                    exit : exit sherlock module
                    cd .. : exit sherlock module
                
                Use Sherlock
                    sherlock USERNAME : to search for a user 
                    sherlock USERNAME --timeout TIME_IN_SECONDS : to specify time for each website to be searched for default is 1 second
                """)
            
            elif subcommandarr[0] == "sherlock":
                if len(subcommandarr) == 1:
                    print("""
                    Please enter a username
                    """)
                else:
                    if len(subcommandarr) == 2: 
                        print(
                            """
                            Spider is running please Wait...
                            """
                        )
                        lst=sherlock.findUser(name = subcommandarr[1])
                        for x in lst:
                            print(x)
                    if len(subcommandarr) == 4 and subcommandarr[2] == "--timeout":
                        print(
                            """
                            Spider is running please Wait...
                            """
                        )
                        lst=sherlock.findUserTimeout(name = subcommandarr[1],time = subcommandarr[3])
                        for x in lst:
                            print(x)

            else:
                print(
                    """
                    Invalid Command
                    """
                )
    




    elif command == "photoinfo" or command == "2":
        meta = MetaDataExtractor()
        while(True):
            subcommand = input(">> PhotoInfo >> ")
            subcommand = subcommand.lower().strip()
            subcommandarr = subcommand.split(' ')
            if subcommand == "exit photoinfo" or subcommand == 'photoinfo exit' or subcommand == "exit" or subcommand == "cd ..":
                break

            elif subcommand == "pwd":
                print("""
                PhotoInfo Module
                """)
            
            elif subcommand == "photoinfo --help" or subcommand == "photoinfo -h" or subcommand == "--help" or subcommand == "-h" or subcommand == "help" or subcommand == "h" or subcommand == "?":
                print("""
                Details:
                    You are inside PhotoInfo module. A module to extract PhotoInfo from an image
                
                Help Menu:
                    PhotoInfo --help : show help menu for PhotoInfo
                    PhotoInfo -h : show help menu for PhotoInfo
                    --help : show help menu for PhotoInfo
                    -h : show help menu for PhotoInfo
                    help : show help menu for PhotoInfo
                    h : show help menu for PhotoInfo
                    ? : show help menu for PhotoInfo

                Exit PhotoInfo:
                    exit PhotoInfo : exit PhotoInfo module
                    PhotoInfo exit : exit PhotoInfo module
                    exit : exit PhotoInfo module
                    cd .. : exit PhotoInfo module
                
                Use PhotoInfo
                    PhotoInfo IMAGE_PATH : to extract PhotoInfo from an image
                """)

            elif subcommandarr[0] == "photoinfo":
                if len(subcommandarr) == 1:
                    print("""
                    Please enter an image path
                    """)
                else:
                    if len(subcommandarr) == 2:
                        print(
                            """
                            Extracting Information from image
                            """
                        )
                        print(meta.extract(subcommandarr[1]))
            




    elif command == 'iplookup' or command == '3':
        iplookup = IpLookup()
        while(True):
            subcommand = input(">> Ip Lookup >> ")
            subcommand = subcommand.lower().strip()
            subcommandarr = subcommand.split(' ')
            if subcommand == "exit iplookup" or subcommand == 'iplookup exit' or subcommand == "exit" or subcommand == "cd ..":
                break

            elif subcommand == "pwd":
                print("""
                Ip Lookup Module
                """)
            
            elif subcommand == "iplookup --help" or subcommand == "iplookup -h" or subcommand == "--help" or subcommand == "-h" or subcommand == "help" or subcommand == "h" or subcommand == "?":
                print("""
                Details:
                    You are inside Ip Lookup module. A module to get information relating to an ip address
                
                Help Menu:
                    iplookup --help : show help menu for iplookup
                    iplookup -h : show help menu for iplookup
                    --help : show help menu for iplookup
                    -h : show help menu for iplookup
                    help : show help menu for iplookup
                    h : show help menu for iplookup
                    ? : show help menu for iplookup

                Exit Ip Lookup:
                    exit iplookup : exit iplookup module
                    iplookup exit : exit iplookup module
                    exit : exit iplookup module
                    cd .. : exit iplookup module
                
                Use iplookup
                    Ip_Address : to information relating to an ip address
                """)


            else:
                from IPy import IP
                try:
                    IP(subcommand)
                    result = iplookup.lookup(ip_address = subcommand)
                    print(result)
                except:
                    print(
                        """
                        Invalid IP Address
                        """
                    )




    elif command == "emailspoof" or command == "4":
        emailspoof = EmailSpoof()
        while(True):
            subcommand = input(">> Email Spoof >> ")
            subcommand = subcommand.lower().strip()
            subcommandarr = subcommand.split(' ')
            if subcommand == "exit emailspoof" or subcommand == 'emailspoof exit' or subcommand == "exit" or subcommand == "cd ..":
                break

            elif subcommand == "pwd":
                print("""
                Ip Lookup Module
                """)
            
            elif subcommand == "emailspoof --help" or subcommand == "emailspoof -h" or subcommand == "--help" or subcommand == "-h" or subcommand == "help" or subcommand == "h" or subcommand == "?":
                print("""
                Details:
                    You are inside Email Spoofing module. You can spoof any email with help of this module
                
                Help Menu:
                    emailspoof --help : show help menu for emailspoof
                    emailspoof -h : show help menu for emailspoof
                    --help : show help menu for emailspoof
                    -h : show help menu for emailspoof
                    help : show help menu for emailspoof
                    h : show help menu for emailspoof
                    ? : show help menu for emailspoof

                Exit Ip Lookup:
                    exit emailspoof : exit emailspoof module
                    emailspoof exit : exit emailspoof module
                    exit : exit emailspoof module
                    cd .. : exit emailspoof module
                
                Use emailspoof
                    emailspoof --password PASSWORD_OF_REAL_EMAIL --realemail EMAIL_OF_PERSON_ACTUALLY_SENDING --sendername SENDER_NAME --senderemail SENDER_EMAIL --toemail RECIEVER_EMAIL --toname RECIEVER_NAME --subject SUBJECT --message MESSAGE : to information relating to an ip address
                """)


            elif subcommandarr[0] == "emailspoof":
                if len(subcommandarr) > 2:
                    try:
                        sendername = subcommandarr[subcommandarr.index("--sendername")+1]
                    except:
                        sendername = None

                    try:
                        senderemail = subcommandarr[subcommandarr.index("--senderemail")+1]
                    except:
                        senderemail = None

                    try:
                        toemail = subcommandarr[subcommandarr.index("--toemail")+1]
                    except:
                        toemail = None
                    
                    try:
                        subject = subcommandarr[subcommandarr.index("--subject")+1]
                    except:
                        subject = None

                    try:
                        message = subcommandarr[subcommandarr.index("--message")+1]
                    except:
                        message = None

                    try:
                        realemail = subcommandarr[subcommandarr.index("--realemail")+1]
                    except:
                        realemail = None

                    try:
                        realpassword = subcommandarr[subcommandarr.index("--password")+1]
                    except:
                        realpassword = None

                    try:
                        toname = subcommandarr[subcommandarr.index("--toname")+1]
                    except:
                        toname = None
                    if senderemail == None :
                        print("""
                        Please enter Sender email
                        """)
                    elif sendername == None :
                        print("""
                        Please enter Sender name
                        """)
                    elif toemail == None :
                        print("""
                        Please enter Reciever email
                        """)
                    elif subject == None :
                        print("""
                        Please enter Subject
                        """)
                    elif message == None :
                        print("""
                        Please enter Message
                        """)
                    elif realemail == None :
                        print("""
                        Please enter Real Email
                        """)
                    elif realpassword == None :
                        print("""
                        Please enter Real Email Password
                        """)
                    elif toname == None :
                        print("""
                        Please enter correct Reciever name
                        """)
                    else:
                        emailspoof.spoof(toname=toname,realemail= realemail,realemailpassword= realpassword ,senderemail=senderemail, sendername= sendername, toemail = toemail, subject = subject, message = message)

            else:
                print(
                        """
                        Invalid Command
                        """
                    )



    else:
        print("Command not found") 


#emailspoof --toemail jayantkhanna3105@gmail.com --toname Jayant_Khanna --sendername Jayant_Khanna --senderemail jayantkhanna31052002@gmail.com --message Hello_There_Mate --subject Subject --realemail jayantkhannaofficial@gmail.com --password icdgjxokvhtsvfex