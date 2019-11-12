class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        state = [(0, 1)]  # (pos, speed)
        dist = 0
        visited = set()  # visited (pos, speed)
        visited.add((0, 1))
        while state:
            # print(state)
            n = len(state)
            for _ in range(n):
                pos, speed = state.pop(0)
                if pos == target:
                    return dist
                else:
                    new_states = [(pos + speed, speed * 2), (pos, -1 if speed > 0 else 1)]
                    for new_state in new_states:
                        if new_state not in visited:
                            visited.add(new_state)
                            state.append(new_state)
            dist += 1
