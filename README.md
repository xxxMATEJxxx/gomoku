# gomoku

## Requirements

python3 with tkinter

## How to start developing your own bot

copy folder martins and rename the copy to your name, for example nabouchodonosor.

copy start_game.py and rename the copy to start_game_custom.py,

in start_game_custom.py replace the word "example" for "nabouchodonosor" on lines 2 and 5

execute start_game_custom.py. Now you are playing against your bot in a window.

Please modify only files in your directory and the file start_game_custom.py. Do not modify any other files.

## Tournament
to start a tournament all vs all:

```
python3 start_game_tournament.py
```

Moves in the individual matches are saved in logs.txt

To save the console output to a file, execute tournament as follows:

```
python3 start_game_tournament.py | tee output.txt
```

## Tips
Make sure that you always play a valid move. If you make an invalid move, you lose your turn.

If opponent makes an invalid move, you receive None in opponent_move. Make sure that your code does not crash in that case.

