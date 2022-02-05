from enum import Enum, auto

import numpy as np

from .moe_env import Action


class EnvComponent(Enum):
    white = auto()
    black = auto()


class MOELimitedEnv:
    def __init__(self, size=10):
        self._size = size
        self._world = np.zeros(self._size, dtype=np.bool8)
        self._agent_pos = int(self._size / 2.)

    def reset(self):
        self._world = np.zeros(self._size, dtype=np.bool8)
        self._agent_pos = int(self._size / 2.)
        return self.get_obs()

    def step(self, action: Action):
        if action is Action.right:
            if self._agent_pos < self._world.size - 1:
                self._agent_pos += 1

        elif action is Action.left:
            if self._agent_pos > 1:
                self._agent_pos -= 1

        elif action is Action.write:
            self._world[self._agent_pos] = True

        elif action is Action.delete:
            self._world[self._agent_pos] = False

        else:
            raise ValueError("Action must be one of Agent class component")

        return self.get_obs()

    def get_obs(self):
        return self._world[self._agent_pos]

    def render(self, mode="text"):
        if mode == "text":
            env = self._world
            pos = self._agent_pos
            s = "["
            for k in range(len(env)):
                s += str(int(env[k]))
                if k == pos:
                    s += "*"

                if k != len(env) - 1:
                    s += ", "

            s += "]"

            print()
            print(s)

        elif mode == "nparray":
            return self._world.copy()


if __name__ == '__main__':
    n_steps = 1000
    img = []

    env = MOELimitedEnv()
    obs = env.reset()

    print("obs: ", obs)
    env.render()

    for _ in range(1000):
        a = np.random.choice(Action)
        print("action: ", a)

        obs = env.step(a)

        env.render()

        img.append(env.render(mode="nparray"))



