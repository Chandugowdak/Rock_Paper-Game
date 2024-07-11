Explanation
Variable Initialization:

The strings rock, paper, and scissors (corrected spelling from "seasor") represent the possible choices.
User Input:

a and b prompt players A and B to enter their respective choices.
.strip().lower() ensures that any leading or trailing spaces are removed and the input is converted to lowercase for consistency.
Validation Check:

while a not in [rock, paper, scissors]: checks if a's input is valid and prompts until a valid input is provided.
while b not in [rock, paper, scissors]: checks if b's input is valid and prompts until a valid input is provided.
Game Logic:

The if-elif-else statements determine the winner based on the rules of Rock-Paper-Scissors:
Rock beats scissors.
Paper beats rock.
Scissors beat paper.
If a and b are equal, it is a tie.
The final else case should technically never be reached due to input validation, but it handles any unexpected cases.
