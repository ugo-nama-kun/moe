# moe: Minimum Openended Environment

Under construction...

```python
env = MOELimitedEnv(size=100)
obs = env.reset()

for _ in range(1000):
    a = np.random.choice(Action)

    obs = env.step(a)
```
