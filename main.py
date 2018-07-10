import gym
import gym_token
from baselines import deepq
import numpy as np 

def callback(lcl, _glb):
    # if lcl['model_saved'] and lcl['num_episodes']%20==0:
    #     print('***',lcl)

    is_solved = False
    return is_solved

def main():
    import time
    saving_folder = f'./Model/{time.ctime()}' 
    # Maybe we can restore tmp model using the function in this link:
    # https://github.com/openai/baselines/blob/24fe3d6576dd8f4cdd5f017805be689d6fa6be8c/baselines/deepq/simple.py#L45

    print(f'Will save tmp model at {saving_folder}')

    # 50000 timesteps is about 10 min
    # We will run model in about 1 day
    env = gym.make("Token-v1")
    model = deepq.models.mlp([64,64,64])
    act = deepq.learn(
        env,
        q_func=model,
        lr=1e-3,
        max_timesteps=50000 * 6 * 24,
        buffer_size=50000,
        exploration_fraction=0.4,
        exploration_final_eps=0,
        print_freq=10,
        checkpoint_freq=10,
        checkpoint_path=saving_folder,
        callback=callback,
        gamma=0.9,
        param_noise=True
    )

    print(f"Saving model to {saving_folder}/runtime_model.pkl")
    act.save(f"{saving_folder}/runtime_model.pkl")

if __name__ == '__main__':
    # import sys,time


    # old_stdout = sys.stdout
    # file_name = f"TokenLog_{time.ctime()}.log"
    # log_file = open(file_name,"w")
    # print(f"Logging to {file_name}")
    # sys.stdout = log_file

    np.warnings.filterwarnings('ignore')
    main()

    # sys.stdout = old_stdout
    # log_file.close()
