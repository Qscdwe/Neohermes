import gym
import gym_token

from baselines import deepq
import numpy as np

np.warnings.filterwarnings('ignore')

def main():
    env = gym.make("Token-v1")
    act = deepq.load("runtime_model.pkl")

    while True:
        obs, done = env.reset(), False
        episode_rew = 0
        while not done:
            env.render()
            obs, rew, done, _ = env.step(act(obs[None])[0])
            episode_rew += rew
        print("Episode reward", episode_rew)
        env.close()

if __name__ == '__main__':
    main()