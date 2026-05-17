class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        q = deque([start])
        
        while q:
            check = q.popleft()
            if check<0 or check>=n or check in visited:
                continue

            if arr[check] == 0:
                return True
            
            q.append(check+arr[check])
            q.append(check-arr[check])
            visited.add(check)
        return False