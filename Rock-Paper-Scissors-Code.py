import random

options = ['rock', 'paper', 'scissors']
comp_turn = ''
user_turn = ''
comp_score = 0
user_score = 0
total_games = 0
draw_score = 0

print('\nWelcome to Rock, Paper, Scissors Game!\n')

while True:
    user_turn = input("Type 'rock', 'paper' or 'scissors' to take turn or Type 'q' to quit: ").lower()
    comp_turn = options[random.randint(0, 2)]

    if user_turn == "q":
        print('\n\n\n\n\n\n\nYou have chosen to quit!')
        break

    if user_turn not in options:
        print('Kindly input correctly!')
        continue

    total_games = total_games + 1

    if user_turn == 'rock' and comp_turn == 'scissors':
        user_score = user_score + 1
        print('You Win')
        continue
    elif user_turn == 'paper' and comp_turn == 'rock':
        user_score = user_score + 1
        print('You Win')
        continue
    elif user_turn == 'scissors' and comp_turn == 'paper':
        user_score = user_score + 1
        print('You Win')
        continue
    elif user_turn == comp_turn:
        print('It\'s a Draw!!')
        draw_score = draw_score + 1
    else:
        print('Computer Wins')
        comp_score = comp_score + 1

print('Final Scores are as follows:-')
print(f'                User Wins : {user_score}')
print(f'            Computer Wins : {comp_score}')
print(f'                    Draws : {draw_score}')
print(f'              Total Games : {total_games}')
print('\nSee You Next Time, Goodbye!')
