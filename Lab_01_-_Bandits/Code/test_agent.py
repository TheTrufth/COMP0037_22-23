#!/usr/bin/env python3

'''
Created on 13 Jan 2022

@author: ucacsjj
'''

import matplotlib.pyplot as plt
import numpy as np

from bandits.bandit import Bandit
from bandits.bandit import BanditEnvironment
from bandits.random_action_agent import RandomActionAgent

if __name__ == '__main__':
    # Create bandit
    environment = BanditEnvironment(4)
    
    # Add some bandits
    environment.set_bandit(0, Bandit(1, 1))    
    environment.set_bandit(1, Bandit(1, 2))
    environment.set_bandit(2, Bandit(2, 1))
    environment.set_bandit(3, Bandit(2, 2))
    
    # Create the agent
    agent = RandomActionAgent(environment)
    
    number_of_steps = 100
    
    # Step-by-step store of rewards
    reward_history = np.zeros(number_of_steps)
    action_history = np.zeros(number_of_steps)
    
    # Step through the agent and let it do its business
    for p in range(0, number_of_steps):
        action_history[p], reward_history[p] = agent.step()
        
    # Q3b:
    # Plot the actions and rewards
    # Generate the reward plot
    for s in range(number_of_steps):
        action_history[s], reward_history[s] = agent.step()

    plt.xlabel('Sample number')
    plt.ylabel('Reward')
    plt.plot(reward_history, color = 'red', label = 'Reward')
    plt.figure(1)

    plt.figure(2)   
    plt.xlabel('Sample number')
    plt.ylabel('Action')
    print(action_history[:20])
    plt.scatter(np.arange(number_of_steps), action_history, color = 'blue', label = 'Reward', marker='o')

    
    plt.ion()
    plt.show()
    plt.pause(0.001)
    input()
