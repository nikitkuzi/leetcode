import bisect


class MyCalendarTwo:
    def __init__(self):
        # Initialize an empty list to store the start and end times along with their frequencies.
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        # Find the insertion points for the start and end times.
        start_index = bisect.bisect_left(self.calendar, [start, 0])
        end_index = bisect.bisect_left(self.calendar, [end, 0])

        # Check for overlaps with existing bookings in the range.
        for _, frequency in self.calendar[start_index:end_index]:
            if abs(frequency) > 1:
                # If any frequency exceeds 1, the booking cannot be made.
                return False

        # Calculate the new frequency for the start and end times.
        start_frequency = 1 if start_index <= 0 else (
            self.calendar[start_index - 1][1] + 1 if self.calendar[start_index - 1][1] > 0 else -
            self.calendar[start_index - 1][1])
        end_frequency = -1 if end_index >= len(self.calendar) else (
            self.calendar[end_index][1] - 1 if self.calendar[end_index][1] < 0 else -self.calendar[end_index][1])

        # Check if the new frequencies would cause a conflict.
        if start_frequency > 2 or -end_frequency > 2:
            return False

        # Update frequencies for all entries that overlap with the new booking.
        for i in range(start_index, end_index):
            self.calendar[i][1] += (1 if self.calendar[i][1] > 0 else -1)

        # Insert the new start and end times with their respective frequencies.
        self.calendar.insert(start_index, [start, start_frequency])
        self.calendar.insert(end_index + 1, [end, end_frequency])

        return True