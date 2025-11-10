def avg(nums: [int]) -> int:
    if not nums:
      return None
    return float(sum(nums)/ len(nums))
