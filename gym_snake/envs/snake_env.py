import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_snake.envs.snake_game.snake_game import Grid, Snake, PlayGame
import matplotlib.pyplot as plt

class SnakeEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    
    def __init__(self, grid_width=40, grid_height=40, snake_length=3):
        self.width = grid_width
        self.height = grid_height
        self.snake_starting_length = snake_length
        self.action_space = spaces.Discrete(4)
       
    def reset(self, width, height):
        self.width = width
        self.height = height
        self.game = PlayGame(self.width, self.height, self.snake_starting_length)
        self.last_state = self.game.get_current_state()
        return self.last_state
    
    def step(self, action):
        self.last_state, action, next_state, reward = self.game.step(action)
#         assert(reward >= 0), 'YOU DIED'
        return self.last_state, action, next_state, reward
        
    def render(self, mode='human'):
        try:
            self.game.render()
        except:
            self.reset()
            self.game.render()