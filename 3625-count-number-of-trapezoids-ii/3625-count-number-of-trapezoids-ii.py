from collections import defaultdict

class Solution(object):

    # Custom gcd function (because Python2 has no math.gcd)
    def mygcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def countTrapezoids(self, points):
        n = len(points)
        lines_by_slope = defaultdict(list)

        # -------- STEP 1: Build all segments with normalized slope ----------
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                # Normalize slope
                if dx == 0:
                    slope = (1, 0)     # vertical
                elif dy == 0:
                    slope = (0, 1)     # horizontal
                else:
                    g = self.mygcd(dx, dy)
                    dx //= g
                    dy //= g
                    # Fix sign for uniqueness
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    slope = (dy, dx)

                lines_by_slope[slope].append((i, j))

        result = 0

        # -------- STEP 2: Count valid pairs of segments ----------
        for slope, segments in lines_by_slope.items():
            k = len(segments)
            if k < 2:
                continue

            total_pairs = k * (k - 1) // 2

            endpoint_count = defaultdict(int)
            for a, b in segments:
                endpoint_count[a] += 1
                endpoint_count[b] += 1

            invalid = 0
            for cnt in endpoint_count.values():
                if cnt > 1:
                    invalid += cnt * (cnt - 1) // 2

            result += total_pairs - invalid

        return result
