# moe: Minimum Openended Environment

Under construction...

```python
from moe.moe_limited_env import MOELimitedEnv, Action

env = MOELimitedEnv(size=100)
obs = env.reset()

for _ in range(1000):
    a = np.random.choice(Action)

    obs = env.step(a)
```
