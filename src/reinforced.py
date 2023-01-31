# -*- coding: utf-8 -*-

from board import Board
import random

class Agent():

    def __init__(self, directions:dict):
        self.directions = directions

    def rl(self, state:Board, max_moves:int=100000):
        
        game_state = state.generate()
        total_reward = 0
    
        n = 0
        while game_state and n < max_moves:
            action = random.choice(list(self.directions.keys()))
            moved, score = state.step(self.directions.get(action))
            reward = moved*score

            print(f"{n:<4} action:{self.directions.get(action)[0]:<3} state:{str(state.board):<80}  reward:{reward:<6}")
            total_reward += reward
            n += 1

            game_state = state.generate()

        return {
            "total_iterations": n,
            "total_reward": total_reward,
            "game_state": game_state,
        }

directions = dict(zip([0,1,2,3,4],["up","down","left","right"]))

agent = Agent(directions=directions)
board = Board(row_size=4, col_size=4)
result = agent.rl(board)

print("-"*120)
print(result)
print("-"*120)