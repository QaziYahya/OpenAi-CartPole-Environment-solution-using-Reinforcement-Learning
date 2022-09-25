import logging
import imageio
import gym
import numpy as np
import tensorflow as tf

logging.getLogger().setLevel(logging.ERROR)

env = gym.make("CartPole-v1")

q_network = tf.keras.models.load_model('Cart_Pole_model.h5')

def create_video(filename, env, q_network, fps=30):
  video = imageio.get_writer(filename, fps=fps)
  done = False
  state = env.reset()
  frame = env.render(mode="rgb_array")
  video.append_data(frame)
  while not done:
    state = np.expand_dims(state, axis=0)
    q_values = q_network(state)
    action = np.argmax(q_values.numpy()[0])
    state, _, done, _ = env.step(action)
    frame = env.render(mode="rgb_array")
    video.append_data(frame)

filename = "./Cart_Pole.mp4"

create_video(filename, env, q_network)