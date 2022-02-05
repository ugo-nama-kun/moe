from enum import Enum, auto
from collections import deque

import numpy as np

from moe.const import Action


class EnvComponent(Enum):
    white = auto()
    black = auto()


class MOEnvironment:
    def __init__(self):
        self._world = deque([])
        self._world_origin = 0
        self._agent_pos = 0

    def reset(self):
        self._world.clear()
        self._world.append(EnvComponent.white)
        self._world_origin = 0
        self._agent_pos = 0
        return self.get_obs()

    def step(self, action: Action):
        if action is Action.right:
            self._agent_pos += 1
            if self._pos_to_index(self._agent_pos) > len(self._world) - 1:
                self._world.append(EnvComponent.white)

        elif action is Action.left:
            self._agent_pos -= 1
            if self._pos_to_index(self._agent_pos) < 0:
                self._world_origin += 1
                self._world.appendleft(EnvComponent.white)

        elif action is Action.write:
            index = self._pos_to_index(self._agent_pos)
            self._world[index] = EnvComponent.black

        elif action is Action.delete:
            index = self._pos_to_index(self._agent_pos)
            self._world[index] = EnvComponent.white

        else:
            raise ValueError("Action must be one of Agent class component")

        return self.get_obs()

    def _pos_to_index(self, pos):
        return pos + self._world_origin

    def get_obs(self):
        return self._world[self._pos_to_index(self._agent_pos)]

    def render(self, mode="text"):
        if mode == "text":
            env = [int(c is EnvComponent.black) for c in self._world]
            pos = self._agent_pos + self._world_origin
            s = "["
            for k in range(len(env)):
                s += str(env[k])
                if k == pos:
                    s += "*"

                if k != len(env) - 1:
                    s += ", "

            s += "]"

            print()
            print(s)

        elif mode == "nparray":
            return np.array([bool(k == EnvComponent.black) for k in self._world])


if __name__ == '__main__':
    n_steps = 1000
    img = []

    env = MOEnvironment()
    obs = env.reset()

    print("obs: ", obs)
    env.render()

    for _ in range(10):
        a = np.random.choice(Action)
        print("action: ", a)

        obs = env.step(a)

        img.append(env.render(mode="nparray"))



