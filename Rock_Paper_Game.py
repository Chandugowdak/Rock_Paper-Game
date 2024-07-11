rock = 'rock'  # DEFINE VARIABLE 'rock' WITH VALUE 'rock'
paper = 'paper'  # DEFINE VARIABLE 'paper' WITH VALUE 'paper'
seasor = 'seasor'  # DEFINE VARIABLE 'seasor' WITH VALUE 'seasor'

a = input("Enter the Value (rock, paper, seasor): ")  # PROMPT PLAYER A TO ENTER THEIR CHOICE
b = input("Enter the Value (rock, paper, seasor): ")  # PROMPT PLAYER B TO ENTER THEIR CHOICE

# CHECK IF PLAYER A'S INPUT IS VALID
while a != rock and a != paper and a != seasor:
    a = input("Enter a Valid Input (rock, paper, seasor): ")  # PROMPT PLAYER A TO ENTER A VALID INPUT

# CHECK IF PLAYER B'S INPUT IS VALID
while b != rock and b != paper and b != seasor:
    b = input("Enter a Valid Input (rock, paper, seasor): ")  # PROMPT PLAYER B TO ENTER A VALID INPUT

# DETERMINE THE WINNER BASED ON PLAYER A AND PLAYER B'S CHOICES
if a == rock and b == paper:
    print("B Won The Match")  # PLAYER B WINS IF A IS ROCK AND B IS PAPER
elif a == rock and b == seasor:
    print("A Won The Match")  # PLAYER A WINS IF A IS ROCK AND B IS SEASOR
elif a == paper and b == rock:
    print("A Won The Match")  # PLAYER A WINS IF A IS PAPER AND B IS ROCK
elif a == seasor and b == paper:
    print("A Won")  # PLAYER A WINS IF A IS SEASOR AND B IS PAPER
elif a == paper and b == seasor:
    print("B Won")  # PLAYER B WINS IF A IS PAPER AND B IS SEASOR
else:
    print("It Is a Tie")  # IT'S A TIE IF BOTH CHOICES ARE THE SAME
