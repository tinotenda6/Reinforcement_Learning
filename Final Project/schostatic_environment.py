import random
import numpy as np
import matplotlib.pyplot as plt

from agent import Agent

NUM_OF_EPISODE = 500
NUM_OF_SIMULATION = 100

environment_partially_stochastic = [[11,-30,0],[-30,[14,0],5],[0,0,5]]
environment_fully_stochastic = [[[10, 12], [5, -65], [8, -8]], [[5, -65], [14, 0], [12, 0]], [[8, -8], [12, 0], [10, 0]]]


def partial_stochastic_climb(grid, alpha, gamma, ex):
    reward_arr = []
    percentage_arr = []
    reinforcement_val_arr = []
    max_reward = 14

    action_arr = ['a', 'b', 'c']

    # make agents and 2 q tables for each agent
    for simulation in range(NUM_OF_SIMULATION):
        q_a1 = [0, 0, 0]
        q_b1 = [0, 0, 0]
        q_a2 = [0, 0, 0]
        q_b2 = [0, 0, 0]

        reward = 0
        agent1 = Agent(q_a1, q_b1, action_arr, reward, alpha, gamma)
        agent2 = Agent(q_a2, q_b2, action_arr, reward, alpha, gamma)

        count = 0
        T = 1
        for episode in range(NUM_OF_EPISODE):
            if episode == 0:
                ex = 1
            else:
                ex = 1 / T

            reward = 0

            action1 = agent1.choose_action(ex)
            action2 = agent2.choose_action(ex)

            #index 1 is where action is
            if(action1[1]==0 and action2[1]==0):
                reward = grid[0][0]

            if(action1[1]==0 and action2[1]==1):
                reward = grid[0][1]

            if(action1[1]==0 and action2[1]==2):
                reward = grid[0][2]

            if(action1[1]==1 and action2[1]==0):
                reward = grid[1][0]

            if(action1[1]==1 and action2[1]==1):
                index = random.randint(0, 1)
                reward = grid[1][1][index]

            if(action1[1]==1 and action2[1]==2):
                reward = grid[1][2]

            if(action1[1]==2 and action2[1]==0):
                reward = grid[2][0]

            if(action1[1]==2 and action2[1]==1):
                reward = grid[2][1]

            if(action1[1]==2 and action2[1]==2):
                reward = grid[2][2]

            next_q_a1 = q_a1
            next_q_b1 = q_b1

            next_q_a2 = q_a2
            next_q_b2 = q_b2

            reinforcement_val_arr[episode] += reward

            agent1.update_Qtable(action1[0],action1[1],action1[2],reward, alpha, gamma, q_a1, q_b1, next_q_a1, next_q_b1)
            agent2.update_Qtable(action2[0],action2[1],action2[2],reward, alpha, gamma, q_a2, q_b2, next_q_a2, next_q_b2)

            reward_arr.append(reward)


            # Count max reward numbers
            #print("max reward is:", max_reward, "reward is: ", reward)
            if reward == max_reward:
                count += 1

            T += 1
        percentage = (count / NUM_OF_EPISODE) * 100
        percentage_arr.append(percentage)

    mean_per = np.mean(percentage_arr)
    # print(percentage_arr)
    # return proportion
    # print("q_a1:", q_a1, "q_b1:", q_a2, "max:", max_reward)

    for episode in range(NUM_OF_EPISODE):
       reinforcement_val_arr[episode] /= NUM_OF_SIMULATION

    x = np.arange(NUM_OF_EPISODE)
    y = np.array(reinforcement_val_arr)
    plt.plot(x, y, color="green")
    plt.show()

    print("partially stochastic:", mean_per)
    return mean_per


def fully_stochastic_climb(grid, alpha, gamma, ex):

    reward_arr = []
    percentage_arr = []
    reinforcement_val_arr = [0 for _ in range(NUM_OF_EPISODE)]
    max_reward = 14

    action_arr = ['a','b','c']



    # make agents and 2 q tables for each agent
    for simulation in range(NUM_OF_SIMULATION):

        q_a1 = [0, 0, 0]
        q_b1 = [0, 0, 0]
        q_a2 = [0, 0, 0]
        q_b2 = [0, 0, 0]
        reward = 0

        agent1 = Agent(q_a1, q_b1, action_arr, reward, alpha, gamma)
        agent2 = Agent(q_a2, q_b2, action_arr, reward, alpha, gamma)

        count = 0
        T = 1
        for episode in range(NUM_OF_EPISODE):

            if episode == 0:
                ex = 1
            else:
                ex = 1 / T
            reward = 0

            # choose action
            action1 = agent1.choose_action(ex)
            action2 = agent2.choose_action(ex)

            #index 1 is where action is
            if(action1[1]==0 and action2[1]==0):
                index = random.randint(0, 1)
                reward = grid[0][0][index]

            if(action1[1]==0 and action2[1]==1):
                index = random.randint(0, 1)
                reward = grid[0][1][index]
            if(action1[1]==0 and action2[1]==2):
                index = random.randint(0, 1)
                reward = grid[0][2][index]

            if(action1[1]==1 and action2[1]==0):
                index = random.randint(0, 1)
                reward = grid[1][0][index]

            if(action1[1]==1 and action2[1]==1):
                index = random.randint(0, 1)
                reward = grid[1][1][index]

            if(action1[1]==1 and action2[1]==2):
                index = random.randint(0, 1)
                reward = grid[1][2][index]

            if(action1[1]==2 and action2[1]==0):
                index = random.randint(0, 1)
                reward = grid[2][0][index]

            if(action1[1]==2 and action2[1]==1):
                index = random.randint(0, 1)
                reward = grid[2][1][index]

            if(action1[1]==2 and action2[1]==2):
                index = random.randint(0, 1)
                reward = grid[2][2][index]

            # reinforcement_val += reward
            # reinforcement_val_arr[episode] += reinforcement_val

            # Update Q value
            ## QUESTION: since there is only one policy, is next state current state?
            # Q[cur_row][cur_col][action] = val + (alpha * (reward + (gamma * max(Q[next_row][next_col])) - val))
            next_q_a1 = q_a1
            next_q_b1 = q_b1

            next_q_a2 = q_a2
            next_q_b2 = q_b2

            agent1.update_Qtable(
                action1[0], action1[1], action1[2], reward, alpha, gamma, q_a1, q_b1, next_q_a1, next_q_b1)
            agent2.update_Qtable(
                action2[0], action2[1], action2[2], reward, alpha, gamma, q_a2, q_b2, next_q_a2, next_q_b2)
            ## add reward in array
            reward_arr.append(reward)
            reinforcement_val_arr[episode] += reward
            # Count max reward numbers
            #print("max reward is:", max_reward, "reward is: ", reward)
            if reward == max_reward:
                count += 1
            T += 1

        percentage = (count / NUM_OF_EPISODE) * 100
        percentage_arr.append(percentage)
        #print(percentage_arr)
    mean_per = np.mean(percentage_arr)


    # print(percentage_arr)
    # return proportion
    # print("q_a1:", q_a1, "q_b1:", q_a2, "max:", max_reward)
    for episode in range(NUM_OF_EPISODE):
       reinforcement_val_arr[episode] /= NUM_OF_SIMULATION

    x = np.arange(NUM_OF_EPISODE)
    y = np.array(reinforcement_val_arr)
    plt.plot(x, y, color="green")
    plt.show()

    print("fully stochastic:", mean_per)
    return mean_per

# def climb_and_penalty(grid, alpha, gamma, ex):


# partial_stochastic_climb(environment_partially_stochastic, 0.1, 0, 1)
fully_stochastic_climb(environment_fully_stochastic, 0.1, 0, 1)

# set reward based on action ,reward
# return
#  make new agent
# action_a = agent.chooseAction()
