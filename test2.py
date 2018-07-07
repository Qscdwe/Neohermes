
import gym
import gym_token
from baselines import deepq
import numpy as np 

def callback(lcl, _glb):
    # stop training if reward exceeds 199
    # is_solved = np.mean(lcl['episode_rewards'][-101:-1]) > -0.03
    # Manually save pickle later
    # Check out other parameters
    # auto push log to cloud
    is_solved = False
    return is_solved

def main():
    env = gym.make("token-v1")
    model = deepq.models.mlp([128,64,64,128])
    act = deepq.learn(
        env,
        q_func=model,
        lr=1e-3,
        max_timesteps=300000,
        buffer_size=50000,
        exploration_fraction=0.3,
        exploration_final_eps=0,
        print_freq=1,
        callback=callback,
        checkpoint_freq=3,
        gamma=0.9,
        param_noise=True
    )
    print("Saving model to runtime_model.pkl")
    act.save("runtime_model.pkl")

if __name__ == '__main__':
    main()
