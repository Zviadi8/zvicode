#!/usr/bin/python
import sys
import base64


BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)

DESCRIPTION = '''

+===========================================================================+
|General:-------zvicode is a simple text encoder in three different bases---|
|Developer:-----Zviad Gabroshvili-------------------------------------------|
|Country:-------Georgia-----------------------------------------------------|
|Year:----------2015--------------------------------------------------------|
|Mail:----------zviadgabroshvili@gmail.com----------------------------------|
|Price:---------This program is Free and Open Source------------------------|
|Website:-------http://zneweasy.com-----------------------------------------|
|And Last:------Happy hacking-----------------------------------------------|
+---------------------------------------------------------------------------+
|   _________________________                    _________________________  |
|  |Chat                     |                  |Chat                     | |
|  |($)I need to encode text |                  |($)Encode it using simple| |
|  |   to bases: 16; 32; 64  |-----Internet-----|   zvicode.py in bases:  | |
|  |                         |                  |   16; 32; 64            | |
|  |                         |                  |                         | |
|  |_________________________|                  |_________________________| |
|            |      |                                     |      |          |
|           /________\                                   /________\         |
|                                                                           |
|Program doesn't need Internet.                                             |
|                                                                           |
|Usage:                                                                     |
| -u------user friendly interface                                           |
| -e------encode                                                            |
| -d------decode                                                            |
| 16------base16                                                            |
| 32------base32                                                            |
| 64------base64                                                            |
| example1: python zvicode.py -e 16 simple_text                             |
| example2: python zvicode.py -d 64 base64_string                           |
| example3: python zvicode.py -u                                            |
+===========================================================================+

'''

def instructions():
    printout(DESCRIPTION, GREEN)
    print'\n'

def default():
    try:
        printout(DESCRIPTION, GREEN)
        print'\n'
        filename=raw_input("Enter full filename to open: ")
        txt=open(filename)
        full=txt.read()
    except IOError:
        print "\nOh please enter valid filename \n"
        sys.exit(1)
    except KeyboardInterrupt:
       printout("\nGoodbye\n", RED)
       sys.exit(1)
    print '\n'
    try:
        printout("For encoding type encode for decoding type decode(encode/decode): ", BLUE)
        selection=raw_input()
    except KeyboardInterrupt:
       printout("\nGoodbye\n", RED)
       sys.exit(1)
    if selection=="encode":
        try:
            base=raw_input("Select base to encode(16; 32; 64): ")
            if base =="16":
                coded=base64.b16encode(full)
                printout("\nYour base16 encoded text is under the line\n", RED)
                print("\t--------------------------------------------------\n")
                print(coded)
                print"\n"
                sys.exit(0)
            elif base=="32":
                coded=base64.b32encode(full)
                printout("\nYour base32 encoded text is under the line\n", RED)
                print("\t--------------------------------------------------\n")
                print(coded)
                print"\n"
                sys.exit(0)
            elif base=="64":
                coded=base64.b64encode(full)
                printout("\nYour base64 encoded text is under the line\n", RED)
                print("\t--------------------------------------------------\n")
                print(coded)
                print"\n"
                sys.exit(0)
        except KeyboardInterrupt:
           printout("\nGoodbye\n", RED)
           sys.exit(1)
    elif selection=="decode":
        try:
            base2=raw_input("Select base to encode(16; 32; 64): ")
            if base2=="16":
                decoded=base64.b16decode(full)
                printout("\nYour base16 decoded text is under the line\n", RED)
                print("\t--------------------------------------------------\n")
                print(decoded)
                print"\n"
                sys.exit(0)
            elif base2=="32":
                decoded=base64.b32decode(full)
                printout("\nYour base32 decoded text is under the line\n", RED)
                print("\t--------------------------------------------------\n")
                print(decoded)
                print"\n"
                sys.exit(0)
            elif base2=="64":
                decoded=base64.b64decode(full)
                printout("\nYour base64 decoded text is under the line\n", RED)
                print("\t--------------------------------------------------\n")
                print(decoded)
                print"\n"
                sys.exit(0)

        except KeyboardInterrupt:
           printout("\nGoodbye\n", RED)
           sys.exit(1)
    else:
        printout("Please enter valid selection(16/32/64)\n", YELLOW)
        default()

if len(sys.argv) >4 or len(sys.argv)==3 or len(sys.argv) ==1:
    instructions()
    print'\n'
    sys.exit(0)
if len(sys.argv)==2 and sys.argv[1] =="-u":
    default()

else:
    string=sys.argv[3]
    if sys.argv[1] == "-e":
        if sys.argv[2] == "16":
            coded = base64.b16encode(string)
            printout("You encoded string: "+ coded, RED)
            print'\n'
            sys.exit(0)
        elif sys.argv[2] == "32":
            coded = base64.b32encode(string)
            printout("Your encoded string: "+ coded, RED)
            print'\n'
            sys.exit(0)
        elif sys.argv[2] == "64":
            coded = base64.b64encode(string)
            printout("Your encoded string: "+ coded, RED)
            print'\n'
            sys.exit(0)
        else:
            default()
            print'\n'
    elif sys.argv[1] == "-d":
        if sys.argv[2] == "16":
            data = base64.b16decode(string)
            printout("You decoded string: "+ data, RED)
            print'\n'
            sys.exit(0)
        elif sys.argv[2] == "32":
            data = base64.b32decode(string)
            printout("Your decoded string: "+ data, RED)
            print'\n'
            sys.exit(0)
        elif sys.argv[2] == "64":
            data = base64.b64decode(string)
            printout("Your decoded string: "+ data, RED)
            print'\n'
            sys.exit(0)
        else:
            default()
            print'\n'
            sys.exit(0)
    else:
        default()
        print'\n'
        sys.exit(0)
