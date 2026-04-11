from scipy.stats import expon

lambda_ = 10
prob = 1 - expon.cdf(1, scale=7/lambda_) #mais que
# prob = expon.cdf(1, scale=7/lambda_) #até
print(prob)