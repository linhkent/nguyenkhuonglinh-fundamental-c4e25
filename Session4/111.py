nums = [1, -1, 7, 8, -5, 13]
im = 0
nm = nums[im]
for i, n in enumerate(nums):
    if n<nm:
        im = i
        nm = n
print(im,nm, sep=". ")