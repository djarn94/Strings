# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Goal scorer variables
player1 = 'Ruud Gullit'
player2 = 'Marco van Basten'
#Time stamps of made goals
goal_0 = 32
goal_1 = 54

scorers = f'{player1} {str(goal_0)}, {player2} {str(goal_1)}'
print(scorers)
report = f'{player1} scored in the {goal_0}nd minute' f'\n{player2} scored in the {goal_1}th minute'

player = 'Jan Wouters'
first_name = player[player.find("Jan"):3]
last_name_len = len(player[4:])
print(last_name_len)

name_short = f'{first_name[0]}. {player[4:]}'


xhant = f'{first_name}! ' * len(first_name)
chant = xhant.rstrip()

good_chant = chant[-1] !=1
print(good_chant)

print(chant)


