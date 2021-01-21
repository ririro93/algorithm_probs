def compute(n):
  if n == 0: return []
  if dp[n]:
    return dp[n]
  dp[n] = compute(n-1) + [[0, 2]] + transpose(compute(n-1), '0->1,1->2,2->0')
  return dp[n]

print(compute(2))