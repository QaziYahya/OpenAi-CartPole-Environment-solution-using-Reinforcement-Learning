# OpenAi-CartPole-Environment-solution-using-Reinforcement-Learning
Reinforcement Learning DQN - using OpenAI Cart Pole environment 

<li>Tensorflow</li>
<li>Keras</li>
<li>gym</li>
</br>

The OpenAI Cart Pole consists of a pole placed upright ontop of a cart which moves along a frictionless track. The goal is to balance the pole by applying forces in the left and right direction on the cart. The cart can be controlled by using 2 discrete actions which are repersented by 0 and 1. They are described as follows:

<li>0: Push cart to the left</li>
<li>1: Push cart to the right</li>
</br>

![Screenshot from 2022-09-25 16-10-56](https://user-images.githubusercontent.com/74414105/192140577-231ffa78-287a-4600-a091-dea3b7d5dfc0.png)

The agent was trained using Deep-Q-Learning. It took a total of 2651 episodes for the model to train with an avarage score of 402.17. The time taken was about 7 minutes. 

# Preview:

https://user-images.githubusercontent.com/74414105/192140702-4556cef7-4258-48a1-8a58-fa7f29d7c1a4.mp4

# Training & Testing
The agent can be trained by running the "train.py" file keep in mind that it takes some time for the agent to train. The model can be tested by running the
"test.py" file it'll create and save a video of the agent playing the game. 
