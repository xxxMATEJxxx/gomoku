# gomoku

## Requirements

python3 with tkinter

## How to run

to play against a bot in a window, copy start_game.py to start_game_custom.py,
modify as needed and execute:

```
python3 start_game_custom.py
```

to start a tournament all vs all:

```
python3 start_game_tournament.py
```

Moves in the individual matches are saved in logs.txt

To save the console output to a file, execute tournament as follows:

```
python3 start_game_tournament.py | tee output.txt
```
