def solve(filename):
    MOD = 1000001
    
    with open(filename) as f:
        n, k = map(int, f.readline().split())
        nums = [int(f.readline()) for _ in range(n)]
        
        best1 = float('inf')
        best2 = float('inf')
        best3 = float('inf')
        
        prev = []
        
        for i in range(n):
            if i >= k:
                prev.append(nums[i - k])
                prev.sort()
                if len(prev) > 3:
                    prev.pop()
                temp = prev[:3]
                temp.extend([float('inf')] * (3 - len(temp)))
                best1, best2, best3 = temp
                
            if i >= 2 * k and len(prev) >= 2:
                best3 = min(best3, nums[i] * prev[0] * prev[1])
        
        return best3 % MOD
    
print(solve("D:\\1_Univer\\Python\\27-167a.txt"))
print(solve("D:\\1_Univer\\Python\\27-167b.txt"))
