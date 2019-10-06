# Recursion
class Solution(object):
    def minRefuelStopsRec(self, target, startFuel, stations, l):
        """
        Return the min stops with stations[:l] to target with given startFuel
        Or -1 if not possible
        """
        if l == 0 and target <= startFuel: return 0
        if l == 0 and target > startFuel:  return -1

        # case1: fuel up at last station stations[l - 1]
        # startFuel = 1,   station {1, 7}     target = 10
        selected_res = self.minRefuelStopsRec(
            max(target - stations[l - 1][1],
                stations[l - 1][0]),
            startFuel,
            stations,
            l - 1)
        unselected_res = self.minRefuelStopsRec(target, startFuel, stations, l - 1)
        if selected_res == -1:
            return unselected_res
        if unselected_res == -1:
            return selected_res + 1
        return min(unselected_res, selected_res + 1)

    def minRefuelStops(self, target, startFuel, stations):
        """
        stations[i]
                start, startFuel     station       target

        What is the least number of refueling
           stops the car must make in order to reach its destination?
           If it cannot reach the destination, return -1.

        startFuel = 1,              target = 10
        startFuel = 1,   station {2, 8}     target = 10
        startFuel = 1,   station {1, 7}     target = 10
        startFuel = 1,   station {1, 11}    target = 10
        startFuel = 2,   station {2, 4}     station {6, 4}    target = 10
        startFuel = 2,   station {2, 4}     station {6, 2}    target = 10
        """
        return self.minRefuelStopsRec(target, startFuel, stations, len(stations))


# Memorization
class Solution(object):
    """
    source -> stop -> stop -> target

                                   (target, l)
                       /                                  \
             (target, l - 1)                          (target - X, l - 1)
                /            \                        /                     \
    (target - X, l - 2)  (target - X, l - 2)   (target - X, l - 2)      (target - 2X, l - 1)

    Time Complexity Before Mem: O(2 ^ len(stations))

    Time Complexity After Mem: O(len(stations) * target)
      Input: stations, the number target -- takes log16(target) bytes for the input
      Time Complexity based on the input size: O(len(stations) * e^(log16(target)))
    """

    def minRefuelStopsRec(self, target, startFuel, stations, l):
        """
        Return the min stops with stations[:l] to target with given startFuel
        Or -1 if not possible
        """
        if l == 0 and target <= startFuel:
            return 0
        if l == 0 and target > startFuel:
            return -1

        if (target, l) in self.answer_cache:
            return self.answer_cache[(target, l)]

        # case1: fuel up at last station stations[l - 1]
        # startFuel = 1,   station {1, 7}     target = 10
        selected_res = self.minRefuelStopsRec(
            max(target - stations[l - 1][1],
                stations[l - 1][0]),
            startFuel,
            stations,
            l - 1)

        # case2: skip last station stations[l - 1]
        unselected_res = self.minRefuelStopsRec(target, startFuel, stations, l - 1)
        if selected_res == -1:
            return unselected_res
        if unselected_res == -1:
            return selected_res + 1
        ans = min(unselected_res, selected_res + 1)
        self.answer_cache[(target, l)] = ans
        return ans

    def minRefuelStops(self, target, startFuel, stations):
        """
        stations[i]
                start, startFuel     station       target

        What is the least number of refueling
           stops the car must make in order to reach its destination?
           If it cannot reach the destination, return -1.

        startFuel = 1,              target = 10
        startFuel = 1,   station {2, 8}     target = 10
        startFuel = 1,   station {1, 7}     target = 10
        startFuel = 1,   station {1, 11}    target = 10
        startFuel = 2,   station {2, 4}     station {6, 4}    target = 10
        startFuel = 2,   station {2, 4}     station {6, 2}    target = 10
        """
        self.answer_cache = {}
        return self.minRefuelStopsRec(target, startFuel, stations, len(stations))


# DP
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        stations[i]
                start, startFuel     station       target

        What is the least number of refueling
           stops the car must make in order to reach its destination?
           If it cannot reach the destination, return -1.

        startFuel = 1,              target = 10
        startFuel = 1,   station {2, 8}     target = 10
        startFuel = 1,   station {1, 7}     target = 10
        startFuel = 1,   station {1, 11}    target = 10
        startFuel = 2,   station {2, 4}     station {6, 4}    target = 10
        startFuel = 2,   station {2, 4}     station {6, 2}    target = 10
        """
        n = len(stations)
        state = [[0] * (target + 1) for _ in range(n + 1)]
        for t in range(target + 1):
            state[0][t] = -1
        for t in range(min(startFuel, target) + 1):
            state[0][t] = 0
        for station_i in range(1, n + 1):
            for t in range(target + 1):
                # case1: fuel up at last station stations[l - 1]
                # case2: skip last station stations[l - 1]
                fuel_need = max(t - stations[station_i - 1][1], stations[station_i - 1][0])
                if state[station_i - 1][fuel_need] == -1:
                    state[station_i][t] = state[station_i - 1][t]
                elif state[station_i - 1][t] == -1:
                    state[station_i][t] = state[station_i - 1][fuel_need] + 1
                else:
                    state[station_i][t] = min(state[station_i - 1][t], state[station_i - 1][fuel_need] + 1)
        return state[n][target]


# DP with Memory Optimization still exp time
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        stations[i]
                start, startFuel     station       target

        What is the least number of refueling
           stops the car must make in order to reach its destination?
           If it cannot reach the destination, return -1.

        startFuel = 1,              target = 10
        startFuel = 1,   station {2, 8}     target = 10
        startFuel = 1,   station {1, 7}     target = 10
        startFuel = 1,   station {1, 11}    target = 10
        startFuel = 2,   station {2, 4}     station {6, 4}    target = 10
        startFuel = 2,   station {2, 4}     station {6, 2}    target = 10
        """
        n = len(stations)
        state = [0] * (target + 1)
        for t in range(target + 1):
            state[t] = -1
        for t in range(min(startFuel, target) + 1):
            state[t] = 0
        for station_i in range(1, n + 1):
            for t in range(target, -1, -1):
                # case1: fuel up at last station stations[l - 1]
                # case2: skip last station stations[l - 1]
                fuel_need = max(t - stations[station_i - 1][1], stations[station_i - 1][0])
                if state[t] != -1 and state[fuel_need] != -1:
                    state[t] = min(state[t], state[fuel_need] + 1)
                elif state[t] == -1 and state[fuel_need] != -1:
                    state[t] = state[fuel_need] + 1
        return state[target]
