from agent import Agent

<<<<<<< HEAD
#
enviroment_grid = [[11,-30,0],[-30,0,5],[0,0,5]]


def climb(alpha, gamma,ex):
#create q_b and q_b
    q_a1 = [0,0,0]
    q_b1 = [0,0,0]
    q_a2 = [0,0,0]
    q_b2 = [0,0,0]
    action_arr = ['a','b','c']
    reward = 0
    


    # make agents
    agent1 = Agent(q_a1, q_b1, action_arr,ex,reward,alpha,gamma)
    agent2 = Agent(q_a1, q_b1, action_arr,ex,reward,alpha,gamma)
=======

def climb(grid, alpha, gamma, ex):

    action_arr = ['a', 'b', 'c']
    reward = 0

    # make agents and q tables
    agent1 = Agent(q_a1, q_b1, action_arr, ex, reward, alpha, gamma)
    q_a1 = [0, 0, 0]
    q_b1 = [0, 0, 0]

    agent2 = Agent(q_a1, q_b1, action_arr, ex, reward, alpha, gamma)
    q_a2 = [0, 0, 0]
    q_b2 = [0, 0, 0]
>>>>>>> edited environmet

    action1 = Agent.choose_action()
    action2 = Agent.choose_action()

    #index 1 is where action is
<<<<<<< HEAD
    if(action1[1]==0 and action2[1]==0):
        reward = enviroment_grid[0][0]
    if(action1[1]==0 and action2[1]==1):
        reward = enviroment_grid[0][1]
    if(action1[1]==0 and action2[1]==2):
        reward = enviroment_grid[0][2]

    if(action1[1]==1 and action2[1]==0):
        reward = enviroment_grid[1][0]

    if(action1[1]==1 and action2[1]==1):
        reward = enviroment_grid[1][1]

    if(action1[1]==1 and action2[1]==2):
        reward = enviroment_grid[1][2]

    if(action1[1]==2 and action2[1]==0):
        reward = enviroment_grid[2][0]

    if(action1[1]==2 and action2[1]==1):
        reward = enviroment_grid[2][1]
    
    if(action1[1]==2 and action2[1]==2):
        reward = enviroment_grid[2][2]
    
    agent1.update_Qtable(action1[0],action1[1],action1[2],reward, alpha,gamma, q_a1,q_b1)
    agent2.update_Qtable(action2[0],action2[1],action2[2],reward, alpha,gamma, q_a2,q_b2)


=======
    if(action1[1] == 0 and action2[1] == 0):
        reward = grid[0][0]

    if(action1[1] == 0 and action2[1] == 1):
        reward = grid[0][1]

    if(action1[1] == 0 and action2[1] == 2):
        reward = grid[0][2]

    if(action1[1] == 1 and action2[1] == 0):
        reward = grid[1][0]

    if(action1[1] == 1 and action2[1] == 1):
        reward = grid[1][1]

    if(action1[1] == 1 and action2[1] == 2):
        reward = grid[1][2]

    if(action1[1] == 2 and action2[1] == 0):
        reward = grid[2][0]

    if(action1[1] == 2 and action2[1] == 1):
        reward = grid[2][1]

    if(action1[1] == 2 and action2[1] == 2):
        reward = grid[2][2]

    agent1.update_Qtable(action1[0], action1[1],
                         action1[2], reward, alpha, gamma, q_a1, q_b1)
    agent2.update_Qtable(action2[0], action2[1],
                         action2[2], reward, alpha, gamma, q_a2, q_b2)
>>>>>>> edited environmet


# set reward based on action ,reward
# return
<<<<<<< HEAD
#  make new agent 
# action_a = agent.chooseAction()


=======
#  make new agent
# action_a = agent.chooseAction()
environment_grid = [[11, -30, 0], [-30, 0, 5], [0, 0, 5]]
>>>>>>> edited environmet
