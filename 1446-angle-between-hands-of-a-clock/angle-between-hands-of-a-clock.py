class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle = 6.0 * minutes
        hour_angle = 30.0 * (hour % 12) + 0.5 * minutes
        diff = abs(hour_angle - min_angle)
        return min(diff, 360.0 - diff)