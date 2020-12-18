#!/usr/bin/env  python3

class Solution:
#    def uniquePaths(self, m: int, n: int) -> int:
    def uniquePaths(self,m,n):
        #m行 n列
        #将二维列表初始化为1，以便之后用于缓存（目标2）
#        results = [[ 1 for _ in range(n)] for _ in range(m) ]
        results = [[1] * n] * m

        #第0行和第0列的格子路径数显然均取值为1，所以跳过
        for i in range(1,m): #逐行计算
            for j in range(1,n): #逐列计算
                #状态转移方程 缓存并复用结果
                results[i][j] = results[i-1][j] + results[i][j-1]
        
        for i in range(0, m):
            print(results[i])

        return results[m-1][n-1]

def main():
    s = Solution()
    print(s.uniquePaths(3,2));
    print(s.uniquePaths(3,7));

if __name__ == '__main__':
    main();
