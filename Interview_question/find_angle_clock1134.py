class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """
        mins has to convert into hour and convert it in degree. (0.5)
        is nothing but 30(min)//60 * 30(degree)
        minute to hour conversion
        60 min = 1hr
        1 min = 1/60 hr
        30 min = 30/60 hr = 0..5 hr
        =================
        12 hr = 360 degree => 1 hr = 360/12 = 30 degree
        60 min = 360 degree => 1min = 360/60 = 6 degree
        """
        hour_angle = 30 * hour + 30 * minutes//60
        min_angle = 6 * minutes
        diff1 = abs(hour_angle - min_angle)
        diff2 = 360 - diff1
        return min(diff1, diff2)