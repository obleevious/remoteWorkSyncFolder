#
# @lc app=leetcode id=675 lang=python3
#
# [675] Cut Off Trees for Golf Event
#
# https://leetcode.com/problems/cut-off-trees-for-golf-event/description/
#
# algorithms
# Hard (30.14%)
# Total Accepted:    12.8K
# Total Submissions: 41.9K
# Testcase Example:  '[[1,2,3],[0,0,4],[7,6,5]]'
#
# You are asked to cut off trees in a forest for a golf event. The forest is
# represented as a non-negative 2D map, in this map:
# 
# 
# 0 represents the obstacle can't be reached.
# 1 represents the ground can be walked through.
# The place with number bigger than 1 represents a tree can be walked through,
# and this positive number represents the tree's height.
# 
# 
# 
# 
# You are asked to cut off all the trees in this forest in the order of tree's
# height - always cut off the tree with lowest height first. And after cutting,
# the original place has the tree will become a grass (value 1).
# 
# You will start from the point (0, 0) and you should output the minimum steps
# you need to walk to cut off all the trees. If you can't cut off all the
# trees, output -1 in that situation.
# 
# You are guaranteed that no two trees have the same height and there is at
# least one tree needs to be cut off.
# 
# Example 1:
# 
# 
# Input: 
# [
# ⁠[1,2,3],
# ⁠[0,0,4],
# ⁠[7,6,5]
# ]
# Output: 6
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# ⁠[1,2,3],
# ⁠[0,0,0],
# ⁠[7,6,5]
# ]
# Output: -1
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: 
# [
# ⁠[2,3,4],
# ⁠[0,0,5],
# ⁠[8,7,6]
# ]
# Output: 6
# Explanation: You started from the point (0,0) and you can cut off the tree in
# (0,0) directly without walking.
# 
# 
# 
# 
# Hint: size of the given matrix will not exceed 50x50.
# 
#
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if len(forest) < 1 or len(forest[0]) < 0:
            return 0
        cands = []
        
        #for i, row in enumerate(forest):
        #    for j, n in enumerate(row):
        #        if n > 1:
        #            cands.append((n, (i, j)))
        #cands.sort()

        cands = sorted((x, (i, j)) for i in range(len(forest)) 
                                    for j, x in enumerate(forest[i]) if x > 1)

        ans = 0

        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        dq = collections.deque()

        def bfs(start, end):
            if start == end:
                return 0
            nonlocal forest, dirs, dq
            hm = collections.defaultdict(int)
            dq.append(start)
            hm[start] = 0
            while len(dq) > 0:
                cur = dq.popleft()
                i, j = cur[0], cur[1]
                for dir in dirs:
                    ni, nj = i+dir[0], j+dir[1]
                    if 0<=ni<len(forest) and 0<=nj<len(forest[0]) and forest[ni][nj] > 0 and (ni, nj) not in hm:
                        hm[(ni,nj)] = hm[(i,j)] + 1
                        dq.append((ni, nj))
            if end not in hm:
                return -1
            return hm[end]
            
        curpos = (0, 0)

        for tree in cands:
            tans = bfs(curpos, tree[1])
            if tans == -1:
                return -1
            else:
                ans += tans
            curpos = tree[1]
        
        return ans
