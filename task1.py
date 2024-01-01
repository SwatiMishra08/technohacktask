#tic tac toe game
block_dict = []

for i in range(9):
  block_dict.append(' ')


def print_board(block_dict):
  board = f"""

   {block_dict[0]} | {block_dict[1]} | {block_dict[2]}
  ---|---|---
   {block_dict[3]} | {block_dict[4]} | {block_dict[5]}
  ---|---|---
   {block_dict[6]} | {block_dict[7]} | {block_dict[8]}

  """
  print(board)


index_list = []
def take_input(player_name):
  while True:
    x = int(input(f'{player_name}: '))
    x -= 1
    if 0 <= x < 10:
      if x in index_list:
        print('This spot is blocked.')
        continue
      index_list.append(x)  
      return x
    print('Please Enter number between 1-9')


def result_calculation(block_dict, player_one, player_two):
  if block_dict[0] == block_dict[1] == block_dict[2] == 'X' or block_dict[1] == block_dict[4] == block_dict[7] == 'X' or block_dict[0] == block_dict[4] == block_dict[8] == 'X' or block_dict[2] == block_dict[5] == block_dict[8] == 'X' or block_dict[3] == block_dict[4] == block_dict[5] == 'X' or block_dict[2] == block_dict[4] == block_dict[6] == 'X' or block_dict[6] == block_dict[7] == block_dict[8] == 'X' or block_dict[0] == block_dict[3] == block_dict[6] == 'X' :
    print(f'Congratulations {player_one}. You WON.!!')
    quit('Thank you both for joining')
  elif block_dict[0] == block_dict[1] == block_dict[2] == 'O' or block_dict[1] == block_dict[4] == block_dict[7] == 'O' or block_dict[0] == block_dict[4] == block_dict[8] == 'O' or block_dict[2] == block_dict[5] == block_dict[8] == 'O' or block_dict[3] == block_dict[4] == block_dict[5] == 'O' or block_dict[2] == block_dict[4] == block_dict[6] == 'O' or block_dict[6] == block_dict[7] == block_dict[8] == 'O' or block_dict[0] == block_dict[3] == block_dict[6] == 'O' :
    print(f'Congratulations {player_two}. You WON.!!')
    quit('Thank you both for joining')
  else:
    return


def main():
  print("Welcome to tic tac toe game.!!")
  player_one = input("Enter player 1 name: ")
  player_two = input("Enter player 2 name: ")
  print(f"Thank you for joining Mr./Mrs. {player_one} and Mr./Mrs. {player_two}")
 
  print(f"Mr. {player_one}'s sign is - X")
  print(f"Mr. {player_two}'s sign is - O")
  input("Enter any key to start the game: ")
  print_board(block_dict)
  for i in range(0,9):
    if i%2 == 0:
      index = take_input(player_one)
      block_dict[index] = 'X'
    else:
      index = take_input(player_two)
      block_dict[index] = 'O'

    print_board(block_dict)
    result_calculation(block_dict, player_one, player_two)
    
  
  print("This is a tie.")
    
    
    
main()