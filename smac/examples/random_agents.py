from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from smac.env import StarCraft2Env
import numpy as np


def main():
    env = StarCraft2Env(map_name="door1")
    env_info = env.get_env_info()

    n_actions = env_info["n_actions"]
    n_agents = env_info["n_agents"]

    n_episodes = 10

    for e in range(n_episodes):
        env.reset()
        terminated = False
        episode_reward = 0

        i = 0
        while not terminated:
            obs = env.get_obs()
            state = env.get_state()

            actions = []
            for agent_id in range(n_agents):
                avail_actions = env.get_avail_agent_actions(agent_id)
                avail_actions_ind = np.nonzero(avail_actions)[0]
                action = np.random.choice(avail_actions_ind)
                if i < 6 and avail_actions[4] == 1:
                    action = 4
                elif i < 21 and avail_actions[3] == 1:
                    action = 3
                elif i < 23 and avail_actions[4] == 1:
                    action = 4
                else:
                    action = 6
                actions.append(action)

            reward, terminated, _ = env.step(actions)
            episode_reward += reward
            i += 1

        print("Total reward in episode {} = {}".format(e, episode_reward))

    env.close()


if __name__ == "__main__":
    main()
