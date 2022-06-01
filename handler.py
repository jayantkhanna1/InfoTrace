# sherlock - check all features
# email spoof
# location from image
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

from sherlock import Sherlock_Module
from metadata import MetaDataExtractor
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
            if subcommand == "exit PhotoInfo" or subcommand == 'PhotoInfo exit' or subcommand == "exit" or subcommand == "cd ..":
                break

            elif subcommand == "pwd":
                print("""
                PhotoInfo Module
                """)
            
            elif subcommand == "PhotoInfo --help" or subcommand == "PhotoInfo -h" or subcommand == "--help" or subcommand == "-h" or subcommand == "help" or subcommand == "h" or subcommand == "?":
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
            
            else:
                print(
                    """
                    Invalid Command
                    """
                )


    else:
        print("Command not found") 
