from random import randint

opponent_occupied_rows = []
opponent_occupied_cols = []
player_occupied_rows = []
player_occupied_cols = []

class Player:
	def __init__(self, player_sign):
		self.sign = player_sign
		self.name = 'example'
	def play(self, opponent_move):
		#if opponent_move == None:
		#	return (7, 7)			# FIRST MOVE
		#ok_move_opponent_occ = 0
		#ok_move_player_occ = 0
		
		row, col = opponent_move
		print (opponent_move)
	"""
		
		opponent_occupied_rows.append(row)
		opponent_occupied_cols.append(col)
		
		dest_row = row + randint(-3,3)
		dest_col = col + randint(-3,3)

		for coord in opponent_occupied_rows:
			if dest_row == coord:
				ok_move_opponent_occ += 0
			else:
				ok_move_opponent_occ += 1
		
		for coord in opponent_occupied_cols:
			if dest_col == coord:
				ok_move_opponent_occ += 0
			else:
				ok_move_opponent_occ += 1
		
		print (opponent_occupied_rows)
		print (opponent_occupied_cols)
		
		for coord in player_occupied_cols:
			if dest_col == coord:
				ok_move_player_occ += 0
			else:
				ok_move_player_occ += 1
		
		for coord in player_occupied_cols:
			if dest_col == coord:
				ok_move_player_occ += 0
			else:
				ok_move_player_occ += 1	
		
		print (player_occupied_rows)
		print (player_occupied_cols)
		print ("opp field score: "+str(ok_move_opponent_occ))
		print ("player field score: "+str(ok_move_player_occ))
		
		
		if ok_move_opponent_occ >= 1 or ok_move_player_occ >= 1:
			if row >= 0 and row <= 15:
				if col >= 0 and col <= 15:
					player_occupied_rows.append(row)
					player_occupied_cols.append(col)
					ok_move_opponent_occ = 0
					ok_move_player_occ = 0
					return (dest_row, dest_col)
				else:
					print("INVALID MOVE - placed outside the grid")
					play(self, opponent_move)
			else:
				print("INVALID MOVE - placed outside the grid")
				play(self, opponent_move)
		else:
			print("INVALID MOVE - placed on an occupied field")
			play(self, opponent_move)
		"""

