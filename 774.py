class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def possible(dist):
            stations_added = 0

            for i in range(len(stations) - 1):
                diff = stations[i + 1] - stations[i]
                add_stations = int(diff / dist)
                stations_added += add_stations

            return stations_added <= k

        left, right = 0, stations[-1] - stations[0]

        while right - left > 10**(-6):
            mid = (left + right) / 2

            if possible(mid):
                right = mid
            else:
                left = mid

        return left