import numpy as np
import matplotlib.pyplot as plt

from moe.moe_limited_env import MOELimitedEnv, Action


n_steps = 1000
img = []

env = MOELimitedEnv(size=100)
obs = env.reset()

for _ in range(1000):
    a = np.random.choice(Action)

    obs = env.step(a)

    img.append(env.render(mode="nparray"))

img = np.array(img)

plt.figure(figsize=(5, 1))
plt.imshow(img.transpose(), "gray")
plt.show()
