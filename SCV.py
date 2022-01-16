try:
    import requests
except ModuleNotFound:
    print(red + "module \"requests\" not found\nrequests will be installed automatically" + white)
    t.sleep(4)
    os.system("pip install requests")
import os, time as t
t.sleep(4)
os.system("""apt install toilet""")
os.system("clear")
#color
plus = "[+] "
greenpurple= '\033[1;32;45m'
red = '\033[1;31;40m'
blue = '\033[1;34;40m'
redyellow = '\033[1;33;41m'
white = '\033[0;37;40m'
yellow = '\033[1;33;40m'
green = '\033[1;32;40m'
def loop():
    os.system("clear")
    print(yellow)
    os.system("toilet SourceCode-Viewer")
    print(white)
    print(red + "version1.0".center(58))
    print(yellow + plus + green + "Tool Name:Source Code Viewer\n" + yellow + plus + green + "Author:Spider Anongreyhat (Anonspidey)\n" + yellow + plus + green + "Team:TermuxHackz Society\n" + yellow + plus + green + "Github:https://github.com/spider863644\n" + yellow + plus + green + "WhatsApp:+2349052863644\n" + yellow + plus + green + "Instagram:https://instagram.com/spider863644")
    print(white)
    print(yellow + "============================================================\n============================================================" + white)
    print(green + "Note:Do not use (www.)\n use https://\n\n" + red + "http://site not supported!")
    update = input (redyellow + "Do you wanna update?[y/n] " + white)
    if update == "y" or update == "Y":
        os.system(" clear")
        print(redyellow + "Updating..." + white)
        t.sleep(5)
        os.system("""
        rm -f -r SourceCode-Viewer
        git clone https://github.com/spider863644/SourceCode-Viewer
        """)
        print(blue +"""
        Now type the following commands
        cd $HOME
        cd SourceCode-Viewer
        python3 SCV.py
        """ + white)
        exit()
    else:
        pass
    print(white +"Nice 👍👏" + white)
    url = input(redyellow + "Enter the URL of the webpage you wanna get its source code " + white)
    if "https://" not in url:
        print(red + "Invalid URL!\n" + url + " is not a valid URL!")
        t.sleep(4)
        loop()
    #raise ConnectionError(red + "No internet connection\nConnect to internet and try again" + white)
    x = requests.get(url)
    os.system("clear")
    print(redyellow + "Getting source code of " + url + "..." + white)
    t.sleep(5)
    print(blue)
    print(x.text)
    print(white)
    cont = input(greenpurple + "Do you wanna get another webpage source code? [y/n]" + white)
    if cont == "y" or cont == "Y":
        loop()
    else:
        print(green + "Thanks for using my script, kindly follow me on Instagram\nhttps://instagram.com/spider863644" + white)
loop()