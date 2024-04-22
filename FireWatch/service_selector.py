import os

# ASCII art
ascii_art = r"""
                               (                               
 )\ )                            )\ )     (            )         
(()/(   (  (    )  (        (   (()/(   ( )\  (     ( /(    (    
 /(_)) ))\ )(  /(( )\  (   ))\   /(_)) ))((_)))\ (  )\())(  )(   
(_))  /((_|()\(_))((_) )\ /((_) (_))  /((_) /((_))\(_))/ )\(()\  
/ __|(_))  ((_))((_|_)((_|_))   / __|(_))| (_)) ((_) |_ ((_)((_) 
\__ \/ -_)| '_\ V /| / _|/ -_)  \__ \/ -_) / -_) _||  _/ _ \ '_| 
|___/\___||_|  \_/ |_\__|\___|  |___/\___|_\___\__| \__\___/_|  
"""

def select_service():
    while True:
        print("Select a service:")
        print("1. FireWatch (Host Enumeration and Data)")
        print("2. Intel Extinguisher(Documents and Enumeration)")
        print("3. Shodan Module (Less powerful Alternative to FireWatch)")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            print("It's time to burn...")
            print("All ready.")
            os.system('python FireWatch.py')
            print("Exiting...")
            break

        elif choice == '4':
            print("Exiting...")
            break

        elif choice in ['2', '3']:
            print(f"Executing {'intelx_scan.py' if choice == '2' else 'shodan_scan2.py'}...")
            os.system('python intelx_scan.py' if choice == '2' else 'python shodan_scan2.py')

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    # Print the ASCII art in orange
    print("\033[33m" + ascii_art + "\033[0m")
    select_service()
    # Print creator's name in orange
    print("\033[33m" + "Created by Zachary Longo" + "\033[0m")
