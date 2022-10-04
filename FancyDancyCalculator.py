from time import sleep
import math
import pyfiglet


input1 = 0
input2 = 0
mathop = ""
wholeinput = ""
parsedinput = ""
output = 0

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
        output = int(input1) * int(input2)
        print(pyfiglet.figlet_format(wholeinput + " is " + str(output)))

    def divide(input1, input2):
        print("dividing")
        output = int(input1) / int(input2)
        print(pyfiglet.figlet_format(wholeinput + " is " + str(output)))

    def add(input1, input2):
        print("adding")
        output = int(input1) + int(input2)
        print(pyfiglet.figlet_format(wholeinput + " is " + str(output)))

    def subtract(input1, input2):
        print("subtracting")
        output = int(input1) - int(input2)
        print(pyfiglet.figlet_format(wholeinput + " is " + str(output)))

    def exp(input1, input2):
        print("exping")
        output = math.pow(int(input1), int(input2))
        print(pyfiglet.figlet_format(wholeinput + " is " + str(output)))

    def squarert(input1):
        print("sqrting")
        output = math.sqrt(int(input1))
        print(pyfiglet.figlet_format("The sqrt of " + str(input1) + " is " + str(output)))

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
