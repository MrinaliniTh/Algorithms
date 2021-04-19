class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = 30 * hour + 0.5 * minutes
        min_angle = 6 * minutes
        diff1 = abs(hour_angle - min_angle)
        diff2 = 360 - diff1
        return min(diff1, diff2)