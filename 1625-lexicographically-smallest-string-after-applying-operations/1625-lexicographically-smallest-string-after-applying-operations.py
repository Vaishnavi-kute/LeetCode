class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()
        q = deque([s])
        res = s
        n = len(s)

        while q:
            cur = q.popleft()
            if cur in seen:
                continue
            seen.add(cur)
            # Update smallest
            res = min(res, cur)

            # Operation 1: Add a to all digits at odd indices
            arr = list(cur)
            for i in range(1, n, 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            added = "".join(arr)
            if added not in seen:
                q.append(added)

            # Operation 2: Rotate right by b positions
            rotated = cur[-b:] + cur[:-b]
            if rotated not in seen:
                q.append(rotated)

        return res
