from time import sleep
import math
import pyfiglet
from colorama import Fore, Back, Back, Style
from colorama import init
from termcolor import colored


input1 = 0
input2 = 0
mathop = ""
wholeinput = ""
parsedinput = ""
output = 0

init()

print('''
,--.   ,--.         ,--.                                         ,--.
|  |   |  |  ,---.  |  |  ,---.  ,---.  ,--,--,--.  ,---.      ,-'  '-.  ,---.
|  |.'.|  | | .-. : |  | | .--' | .-. | |        | | .-. :     '-.  .-' | .-. |
|   ,'.   | \   --. |  | \ `--. ' '-' ' |  |  |  | \   --.       |  |   ' '-' '
'--'   '--'  `----' `--'  `---'  `---'  `--`--`--'  `----'       `--'    `---'
''')
sleep(2)
print('''


        CCCCCCCCCCCCC               AAA               LLLLLLLLLLL                    CCCCCCCCCCCCC
     CCC::::::::::::C              A:::A              L:::::::::L                 CCC::::::::::::C
   CC:::::::::::::::C             A:::::A             L:::::::::L               CC:::::::::::::::C
  C:::::CCCCCCCC::::C            A:::::::A            LL:::::::LL              C:::::CCCCCCCC::::C
 C:::::C       CCCCCC           A:::::::::A             L:::::L               C:::::C       CCCCCC
C:::::C                        A:::::A:::::A            L:::::L              C:::::C
C:::::C                       A:::::A A:::::A           L:::::L              C:::::C
C:::::C                      A:::::A   A:::::A          L:::::L              C:::::C
C:::::C                     A:::::A     A:::::A         L:::::L              C:::::C
C:::::C                    A:::::AAAAAAAAA:::::A        L:::::L              C:::::C
C:::::C                   A:::::::::::::::::::::A       L:::::L              C:::::C
 C:::::C       CCCCCC    A:::::AAAAAAAAAAAAA:::::A      L:::::L         LLLLLLC:::::C       CCCCCC
  C:::::CCCCCCCC::::C   A:::::A             A:::::A   LL:::::::LLLLLLLLL:::::L C:::::CCCCCCCC::::C
   CC:::::::::::::::C  A:::::A               A:::::A  L::::::::::::::::::::::L  CC:::::::::::::::C
     CCC::::::::::::C A:::::A                 A:::::A L::::::::::::::::::::::L    CCC::::::::::::C
        CCCCCCCCCCCCCAAAAAAA                   AAAAAAALLLLLLLLLLLLLLLLLLLLLLLL       CCCCCCCCCCCCC

''')
sleep(1)
while True:
    wholeinput = input("Enter your equation: ")
    print(wholeinput)
    parsedinput = wholeinput.split(" ")
    print(parsedinput)

    input1 = parsedinput[0]
    mathop = parsedinput[1]
    input2 = parsedinput[2]

    print("Input 1: " + input1)
    print("Input op: " + mathop)
    print("Input 2: " + input2)

    def multiply(input1, input2):
        print("multiplying")
        output = float(input1) * float(input2)
        output = round(output, 3)
        print(pyfiglet.figlet_format(wholeinput + " is " + str(output)))

    def divide(input1, input2):
        print("dividing")
        output = float(input1) / float(input2)
        output = round(output, 3)
        print(pyfiglet.figlet_format(wholeinput + " is " + str(output)))

    def add(input1, input2):
        print("adding")
        output = float(input1) + float(input2)
        print(pyfiglet.figlet_format(wholeinput + " is " + str(output)))

    def subtract(input1, input2):
        print("subtracting")
        output = float(input1) - float(input2)
        print(pyfiglet.figlet_format(wholeinput + " is " + str(output)))

    def exp(input1, input2):
        print("exping")
        output = math.pow(float(input1), float(input2))
        pyfiglet.print_figlet(input1, colors="RED")
        print(" to the power of " +
              str(input2) + " is " + str(output))

    def squarert(input1):
        print("sqrting")
        output = math.sqrt(float(input1))
        output = round(output, 3)
        print(pyfiglet.figlet_format("The sqrt of " +
              str(input1) + " is " + str(output)))

    if mathop == "/":
        print("division selected")
        divide(input1, input2)

    elif mathop == "+":
        print("plus selected")
        add(input1, input2)

    elif mathop == "-":
        print("minus selected")
        subtract(input1, input2)

    elif mathop == "*":
        print("multiply selected")
        multiply(input1, input2)

    elif mathop == "sqrt":
        print("sqrt selected")
        squarert(input1)

    elif mathop == "**" or "xx":
        print("exp selected")
        exp(input1, input2)
