# codenames

(日本語は下にあります)

## how to run:
- install `requirements.txt`
- run it with `python util/gameplay.py`

## how to play:

1. when the program is first run, `prompt.png` will show
2. pick 1 word from `prompt.png` and input it to the terminal
3. it will tell you which color it is
4. whichever color team has all of its colored cards picked wins
5. if black card is picked then the team will immediately lose
6. if you pick a card with color the same as your team you get up to 3 consecutive picks
7. if your pick is the other team or neutral then your turn will end
8. every card can only be picked once per round
9. `answer.png` will show at game over

my code is a mess and the words are taken from https://github.com/jacksun007/codenames

## 実行する方法
- `requirements.txt` をインストール
- `python util/gameplay.py` を実行すると遊べる

## 遊び方

1. プログラムを実行すると、`prompt.png`がすべてのカードを表示する
2. `prompt.png`から1単語を選んでターミナルに入力する
3. プログラムが入力した単語の色を表示する
4. 自分のチームの色のカードをすべて選んだチームが勝ち
5. 黒いカードを選んだらチームは即負けになる
6. 自分のチームの色のカードを選んだ場合、最大3回まで連続で選べる
7. 間違った色を選んだ場合はチーム交代する
8. 一度選んだカードは二度と選べない
9. ゲームオーバーに正解が乗っている`answer.png`が出てくる