#!/usr/bin/env  python3

def fib(n):
    # 用于缓存以往结果，以便复用（目标2）
    #results = list(range(n+1)) 
    results = [ 0 for _ in range(n+1)]

    for i in range(n+1):  # 按顺序从小往大算（目标3）
        if i < 2:
            results[i] = i
        else:
            # 使用状态转移方程（目标1），同时复用以往结果（目标1）
            results[i] = results[i-1] + results[i-2] 
     
    print(results)
    return results[-1]

'''
目标1，建立状态转移方程（完成）。
目标2，缓存并复用以往结果（完成）。在线性规划解法中，我们把结果缓存在results列表，同时在results[i] = results[i-1] + results[i-2] 中进行了复用。这相当于我们只需完成图2中红色部分的计算任务即可，时间复杂度瞬间降为O(n)
目标3，按顺序从小往大算（完成）。for循环实现了从0到n 的顺序求解，让问题按着从小规模往大规模求解的顺序走。]
'''

def main():
    print(fib(6))
    print(fib(10))
    print(fib(100))

if __name__ == '__main__':
    main()

