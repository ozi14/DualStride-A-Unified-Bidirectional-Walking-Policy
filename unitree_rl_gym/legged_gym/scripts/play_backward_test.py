import sys
from legged_gym import LEGGED_GYM_ROOT_DIR
import os
import time 
import sys
from legged_gym import LEGGED_GYM_ROOT_DIR

import isaacgym
from legged_gym.envs import *
from legged_gym.utils import  get_args, export_policy_as_jit, task_registry, Logger

import numpy as np
import torch

def play(args):
    env_cfg, train_cfg = task_registry.get_cfgs(name=args.task)
    
    # Override environment settings for testing (from original play.py)
    env_cfg.env.num_envs = min(env_cfg.env.num_envs, 100)
    env_cfg.terrain.num_rows = 5
    env_cfg.terrain.num_cols = 5
    env_cfg.terrain.curriculum = False
    env_cfg.noise.add_noise = False
    env_cfg.domain_rand.randomize_friction = False
    env_cfg.domain_rand.push_robots = False
    env_cfg.env.test = True
    
    # Override command ranges for testing
    env_cfg.commands.ranges.lin_vel_x = [-0.8, -0.3]  # Backward only
    env_cfg.commands.ranges.lin_vel_y = [0.0, 0.0]    # No lateral movement
    
    # Create environment and load policy (using the framework's approach)
    env, _ = task_registry.make_env(name=args.task, args=args, env_cfg=env_cfg)
    
    # Load policy the same way as in play.py
    train_cfg.runner.resume = True
    train_cfg.runner.load_run = args.load_run
    train_cfg.runner.checkpoint = args.checkpoint
    train_cfg.runner.experiment_name = args.experiment_name
    ppo_runner, train_cfg = task_registry.make_alg_runner(env=env, name=args.task, args=args, train_cfg=train_cfg)
    policy = ppo_runner.get_inference_policy(device=env.device)
    
    # Test cycle - alternate between commands
    obs = env.get_observations()
    for i in range(10000):
        # Every 500 steps, change the command
        if i % 500 == 0:
            # Test different backward speeds
            speed = -0.7 if (i // 500) % 2 == 0 else -1.2 
            print(f"Setting command: x_vel={speed}, y_vel=0.0")
            env.commands[:, 0] = speed  # x velocity
            env.commands[:, 1] = 0.0    # y velocity
            
        actions = policy(obs.detach())
        obs, _, _, dones, infos = env.step(actions.detach())
        
        # Optional: Reset if done
        if dones.any():
            print("Episode finished. Resetting.")
        
        time.sleep(0.01)  # slow down for visualization

if __name__ == '__main__':
    args = get_args()
    play(args)