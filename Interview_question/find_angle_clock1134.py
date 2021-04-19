class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = 30 * hour + 0.5 * minutes # mins has to convert into hour and convert it in degree. (0.5)
        #is nothing but 30(min)//60 * 30(degree)
        min_angle = 6 * minutes
        diff1 = abs(hour_angle - min_angle)
        diff2 = 360 - diff1
        return min(diff1, diff2)