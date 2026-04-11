from scipy.stats import norm

mu = 700
sigma = 50
x = 780

prob = 1 - norm.cdf(x, loc=mu, scale=sigma)
print(f"Probabilidade: {prob*100:.2f} %")
