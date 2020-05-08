import gym
import gym_snake

from pynput.keyboard import Key, Listener

env = gym.make("snake-v0")
env.reset()
env.render()

action = None 
def on_release(key): 
    global action      
    if key==Key.left:
        action=gym_snake.envs.snake.Snake.LEFT
    elif key==Key.right:
        action=gym_snake.envs.snake.Snake.RIGHT
    elif key==Key.up:
        action=gym_snake.envs.snake.Snake.UP
    elif key==Key.down:
        action=gym_snake.envs.snake.Snake.DOWN
    elif key==Key.esc:
        return False

#print(env.obs)
listener=Listener(on_press=on_release)
listener.start()
is_debug = True
while True:    
    if action is not None:    
        #observation contains RGB array of screen
        observation, reward, done, info = env.step(action)
        if done:
            print(f"Restart {reward}")
            env.reset()
        print(f"State: {observation}, Reward: {reward}, Are we done: {done}, {info}")        
        env.render()
        if is_debug:
            action=None


