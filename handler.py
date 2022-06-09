# phone number lookup
# email lookup
# domain lookup
# url lookup
# hash lookup
# Social Media find all posts comments relating to a keyword (Twitter Discord Reddit 4chan Facebook Instagram)
# password cracking md5,sha256,sha512 etc.
# File malicious or not
# Get a remote connection
# Image similarity
# Search a keyword on tor

from Modules.sherlock import Sherlock_Module
from Modules.metadata import MetaDataExtractor
from Modules.iptogeo import IpLookup
from Modules.phonenumberlookup import PhoneNumber

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
            1. personinfo : to get inside personinfo module and search for a username accross social media sites
            2. photoinfo : to get information such as gps coordinates etc. about the image
            3. ipinfo : to get information regarding an ip address
            4. phoneinfo : to get information regarding phonen number
        
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





    elif command == "personinfo" or command == "1":
        print("""
        personinfo - A module to search for a user on multiple websites
        Enter personinfo --help to see complete help menu for personinfo
        """)
        personinfo = Sherlock_Module()
        while(True):
            subcommand = input(">> personinfo >> ")
            subcommand = subcommand.lower().strip()
            subcommandarr = subcommand.split(' ')
            if subcommand == "exit personinfo" or subcommand == 'personinfo exit' or subcommand == "exit" or subcommand == "cd ..":
                break

            elif subcommand == "pwd":
                print("""
                personinfo Module
                """)
 
            elif subcommand == "personinfo --help" or subcommand == "personinfo -h" or subcommand == "--help" or subcommand == "-h" or subcommand == "help" or subcommand == "h" or subcommand == "?": 
                print("""
                Details:
                    You are inside personinfo module. A module to search for a user on multiple websites
                
                Help Menu:
                    personinfo --help : show help menu for personinfo
                    personinfo -h : show help menu for personinfo
                    --help : show help menu for personinfo
                    -h : show help menu for personinfo
                    help : show help menu for personinfo
                    h : show help menu for personinfo
                    ? : show help menu for personinfo

                Exit personinfo:
                    exit personinfo : exit personinfo module
                    personinfo exit : exit personinfo module
                    exit : exit personinfo module
                    cd .. : exit personinfo module
                
                Use personinfo
                    personinfo USERNAME : to search for a user 
                    personinfo USERNAME --timeout TIME_IN_SECONDS : to specify time for each website to be searched for default is 1 second
                """)
            
            elif subcommandarr[0] == "personinfo":
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
                        lst=personinfo.findUser(name = subcommandarr[1])
                        for x in lst:
                            print(x)
                    if len(subcommandarr) == 4 and subcommandarr[2] == "--timeout":
                        print(
                            """
                            Spider is running please Wait...
                            """
                        )
                        lst=personinfo.findUserTimeout(name = subcommandarr[1],time = subcommandarr[3])
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




    
    elif command == "phoneinfo" or command == "4":
        while(True):
            subcommand = input(">> Phone Info >> ")
            subcommand = subcommand.lower().strip()
            subcommandarr = subcommand.split(' ')
            if subcommand == "exit phoneinfo" or subcommand == 'phoneinfo exit' or subcommand == "exit" or subcommand == "cd ..":
                break

            elif subcommand == "pwd":
                print("""
                 Phone Number Informa Module
                """)
            
            elif subcommand == "phoneinfo --help" or subcommand == "phoneinfo -h" or subcommand == "--help" or subcommand == "-h" or subcommand == "help" or subcommand == "h" or subcommand == "?":
                print("""
                Details:
                    You are inside Phone Number Information module. You can find information about any phonenumber with help of this module
                
                Help Menu:
                    phoneinfo --help : show help menu for phoneinfo
                    phoneinfo -h : show help menu for phoneinfo
                    --help : show help menu for phoneinfo
                    -h : show help menu for phoneinfo
                    help : show help menu for phoneinfo
                    h : show help menu for phoneinfo
                    ? : show help menu for phoneinfo

                Exit Ip Lookup:
                    exit phoneinfo : exit phoneinfo module
                    phoneinfo exit : exit phoneinfo module
                    exit : exit phoneinfo module
                    cd .. : exit phoneinfo module
                
                Use phoneinfo
                    phoneinfo PHONE_NUMBER : to get information about a phone number
                """)


            elif subcommandarr[0] == "phoneinfo":
                phoninfo = PhoneNumber()
                if len(subcommandarr) == 1:
                    print("""
                    Please enter a phone number
                    """)
                else:
                    if len(subcommandarr) == 2:
                        print(
                            """
                            Extracting Information from phone number
                            """
                        )
                        data = phoninfo.subhandler(subcommandarr[1])
                        res = []
                        for i in data:
                                if i not in res:
                                    res.append(i)
                        for x in res:  
                            print(x)
            else:
                print(
                        """
                        Invalid Command
                        """
                    )
    
    else:
        print("Command not found") 

