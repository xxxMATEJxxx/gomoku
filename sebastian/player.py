from random import randint

opponent_moves_rows = []
opponent_moves_cols = []
player_moves_rows = []
player_moves_cols = []

class Player:
	def __init__(self, player_sign):
		self.sign = player_sign
		self.name = 'example'
	def play(self, opponent_move):
		#if opponent_move == None:
		#	return (7, 7)			# FIRST MOVE
		row, col = opponent_move
		print (opponent_move)
		
		opponent_moves_rows.append(row)
		opponent_moves_cols.append(col)
		
		dest_row = row + randint(-3,3)
		dest_col = col + randint(-3,3)

		ok_move_opponent_occ = 0
		ok_move_player_occ = 0
		
		for coord in opponent_moves_rows:
			if dest_row == coord:
				ok_move_opponent_occ += 0
			else:
				ok_move_opponent_occ += 1
		
		for coord in opponent_moves_cols:
			if dest_col == coord:
				ok_move_opponent_occ += 0
			else:
				ok_move_opponent_occ += 1
		
		print (opponent_moves_rows)
		print (opponent_moves_cols)
		
		for coord in player_moves_cols:
			if dest_col == coord:
				ok_move_player_occ += 0
			else:
				ok_move_player_occ += 1
		
		for coord in player_moves_cols:
			if dest_col == coord:
				ok_move_player_occ += 0
			else:
				ok_move_player_occ += 1	
		
		print (player_moves_rows)
		print (player_moves_cols)
		print (ok_move_opponent_occ)
		print (ok_move_player_occ)
		
		# TODO:
		# ochrana proti tahu mimo pole (<0, >15)
		
		if ok_move_opponent_occ >= 1 or ok_move_player_occ >= 1:
			player_moves_rows.append(row)
			player_moves_cols.append(col)
			
			return (dest_row, dest_col)
		else:
			print("INVALID MOVE")
			play(self, opponent_move)
		

