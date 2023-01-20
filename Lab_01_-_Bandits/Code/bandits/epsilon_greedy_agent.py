'''
Created on 14 Jan 2022

@author: ucacsjj
'''

import numpy as np
import random
from .agent import Agent

class EpsilonGreedyAgent(Agent):
    
    def __init__(self, environment, epsilon):
        super().__init__(environment)
        self._epsilon = epsilon

    # Q5a:
    # Change the implementation to use the epsilon greedy algorithm
    def _choose_action(self):
        c = random.uniform(0, 1)
        if self._epsilon < c:
            return self._environment.optimal_action()[0]
        return self._environment.action_space.sample()

        
    
            
        
