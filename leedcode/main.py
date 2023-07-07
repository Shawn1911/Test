# sentences = [
#     "alice and bob love leetcode",
#     "i think so too",
#     "this is great thanks very much"]

# max_=float("-inf")
#
# for i in sentences:
#     max_=max_(max_,len(i.split()))
# return max_
#
# print(max([len(i.split())for i in sentences]))
# print(max(map(lambda x : len(x.split()) , sentences)))
# print()

nums=[1,2,3,1,1,3]
c=0
for i ,v in enumerate(nums):
    c+=nums[i+1:].count(v)
print (c)


