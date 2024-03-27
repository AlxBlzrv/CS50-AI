import math
import random
import time


class NimGame:

    def __init__(self, initial=[1, 3, 5, 7]):
        self.piles = initial.copy()
        self.current_player = 0
        self.winner = None

    @classmethod
    def available_moves(cls, piles):
        moves = set()
        for i, pile in enumerate(piles):
            for j in range(1, pile + 1):
                moves.add((i, j))
        return moves

    @classmethod
    def other_player(cls, player):
        return 0 if player == 1 else 1

    def switch_player(self):
        self.current_player = NimGame.other_player(self.current_player)

    def make_move(self, action):
        pile, count = action

        if self.winner is not None:
            raise Exception("Game already won")
        elif pile < 0 or pile >= len(self.piles):
            raise Exception("Invalid pile")
        elif count < 1 or count > self.piles[pile]:
            raise Exception("Invalid number of objects")

        self.piles[pile] -= count
        self.switch_player()

        if all(pile == 0 for pile in self.piles):
            self.winner = self.current_player


class NimAI:

    def __init__(self, alpha=0.5, epsilon=0.1):
        self.q_values = dict()
        self.alpha = alpha
        self.epsilon = epsilon

    def update_q_values(self, old_state, action, new_state, reward):
        old_q = self.get_q_value(old_state, action)
        best_future_reward = self.best_future_reward(new_state)
        new_q = old_q + self.alpha * ((reward + best_future_reward) - old_q)
        self.q_values[tuple(old_state), action] = new_q

    def get_q_value(self, state, action):
        try:
            return self.q_values[tuple(state), action]
        except KeyError:
            return 0

    def best_future_reward(self, state):
        max_reward = 0
        for sta, q in self.q_values.items():
            if sta[0] == state and q > max_reward:
                max_reward = q
        return max_reward

    def choose_action(self, state, epsilon=True):
        max_reward = 0
        best_action = None
        available_moves = NimGame.available_moves(state)

        for move in available_moves:
            try:
                q = self.q_values[tuple(state), move]
            except KeyError:
                q = 0

            if q > max_reward:
                max_reward = q
                best_action = move

        if max_reward == 0:
            return random.choice(tuple(available_moves))

        if not epsilon:
            return best_action
        else:
            if random.random() < self.epsilon:
                return random.choice(tuple(available_moves))
            else:
                return best_action


def train_ai(n):
    player = NimAI()

    for i in range(n):
        print(f"Training game {i + 1}")
        game = NimGame()
        last = {
            0: {"state": None, "action": None},
            1: {"state": None, "action": None}
        }

        while True:
            state = game.piles.copy()
            action = player.choose_action(game.piles)
            last[game.current_player]["state"] = state
            last[game.current_player]["action"] = action
            game.make_move(action)
            new_state = game.piles.copy()

            if game.winner is not None:
                player.update_q_values(state, action, new_state, -1)
                player.update_q_values(
                    last[game.current_player]["state"],
                    last[game.current_player]["action"],
                    new_state,
                    1
                )
                break

            elif last[game.current_player]["state"] is not None:
                player.update_q_values(
                    last[game.current_player]["state"],
                    last[game.current_player]["action"],
                    new_state,
                    0
                )

    print("Training completed")
    return player


def play_game(ai, human_player=None):
    if human_player is None:
        human_player = random.randint(0, 1)

    game = NimGame()

    while True:
        print()
        print("Piles:")
        for i, pile in enumerate(game.piles):
            print(f"Pile {i}: {pile}")
        print()

        available_moves = NimGame.available_moves(game.piles)
        time.sleep(1)

        if game.current_player == human_player:
            print("Your Turn")
            while True:
                pile = int(input("Choose Pile: "))
                count = int(input("Choose Count: "))
                if (pile, count) in available_moves:
                    break
                print("Invalid move, try again.")

        else:
            print("AI's Turn")
            pile, count = ai.choose_action(game.piles, epsilon=False)
            print(f"AI chose to take {count} from pile {pile}.")

        game.make_move((pile, count))

        if game.winner is not None:
            print()
            print("GAME OVER")
            winner = "Human" if game.winner == human_player else "AI"
            print(f"Winner is {winner}")
            return
