import gym
import gym_snake
env = gym.make("snake-v0")
env.reset()
env.render()

for _ in range(500):
    env.render()
    env.step(1)