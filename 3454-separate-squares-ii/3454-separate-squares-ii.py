from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = set()

        # Create events
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs.add(x)
            xs.add(x + l)

        # Coordinate compression
        xs = sorted(xs)
        x_index = {v: i for i, v in enumerate(xs)}

        n = len(xs) - 1
        count = [0] * (4 * n)
        length = [0] * (4 * n)

        def push_up(node, l, r):
            if count[node] > 0:
                length[node] = xs[r + 1] - xs[l]
            elif l == r:
                length[node] = 0
            else:
                length[node] = length[node * 2] + length[node * 2 + 1]

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                count[node] += val
                push_up(node, l, r)
                return
            mid = (l + r) // 2
            if ql <= mid:
                update(node * 2, l, mid, ql, qr, val)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, val)
            push_up(node, l, r)

        # Sort events by y
        events.sort()

        # First pass: total union area
        total_area = 0.0
        prev_y = events[0][0]
        i = 0

        while i < len(events):
            y = events[i][0]
            total_area += length[1] * (y - prev_y)

            while i < len(events) and events[i][0] == y:
                _, typ, xl, xr = events[i]
                update(1, 0, n - 1, x_index[xl], x_index[xr] - 1, typ)
                i += 1

            prev_y = y

        half = total_area / 2

        # Second pass: find y where area reaches half
        count = [0] * (4 * n)
        length = [0] * (4 * n)

        curr_area = 0.0
        prev_y = events[0][0]
        i = 0

        while i < len(events):
            y = events[i][0]
            delta = y - prev_y
            if curr_area + length[1] * delta >= half:
                return prev_y + (half - curr_area) / length[1]

            curr_area += length[1] * delta

            while i < len(events) and events[i][0] == y:
                _, typ, xl, xr = events[i]
                update(1, 0, n - 1, x_index[xl], x_index[xr] - 1, typ)
                i += 1

            prev_y = y

        return prev_y
