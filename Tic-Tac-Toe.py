import random, os, time

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.human = 'X'
        self.ai = 'O'
        self.current = self.human
        self.stats = {'Wins': 0, 'Losses': 0, 'Draws': 0}

    def show_board(self):
        print("\n" + "\n".join([
            " | ".join(self.board[i:i+3]) for i in range(0, 9, 3)
        ]).replace(' ', '_'))

    def valid_moves(self): return [i for i, v in enumerate(self.board) if v == ' ']

    def winner(self, b):
        combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for i, j, k in combos:
            if b[i] == b[j] == b[k] != ' ': return b[i]
        return None

    def minimax(self, board, depth, maxing):
        win = self.winner(board)
        if win == self.ai: return 10 - depth
        if win == self.human: return depth - 10
        if ' ' not in board: return 0

        if maxing:
            best = -float('inf')
            for move in self.valid_moves():
                board[move] = self.ai
                best = max(best, self.minimax(board, depth+1, False))
                board[move] = ' '
            return best
        else:
            best = float('inf')
            for move in self.valid_moves():
                board[move] = self.human
                best = min(best, self.minimax(board, depth+1, True))
                board[move] = ' '
            return best

    def ai_move(self):
        print("🤖 Thinking...")
        time.sleep(0.3)
        best_score, move = -float('inf'), None
        for i in self.valid_moves():
            self.board[i] = self.ai
            score = self.minimax(self.board, 0, False)
            self.board[i] = ' '
            if score > best_score:
                best_score, move = score, i
        return move

    def play(self):
        print("🎮 You vs AI | X: You, O: AI")
        while True:
            self.show_board()
            if self.winner(self.board):
                win = self.winner(self.board)
                print("🎉 You Win!" if win == self.human else "😈 AI Wins!")
                self.stats['Wins' if win == self.human else 'Losses'] += 1
                break
            if ' ' not in self.board:
                print("🤝 It's a draw!")
                self.stats['Draws'] += 1
                break
            if self.current == self.human:
                try:
                    move = int(input("Enter (1-9): ")) - 1
                    if move in self.valid_moves():
                        self.board[move] = self.human
                        self.current = self.ai
                    else: print("❌ Invalid move")
                except: print("❌ Enter a number")
            else:
                self.board[self.ai_move()] = self.ai
                self.current = self.human

if __name__ == "__main__":
    while True:
        game = TicTacToe()
        game.play()
        print(f"📊 Stats: {game.stats}")
        if input("Play again? (y/n): ").lower() != 'y': break