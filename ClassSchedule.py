class ClassSchedule:
    start_time = "9:15"
    end_time = "3:00"

    def __init__(self, start_time, end_time):
        self.schedule = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []
        }
        self.start_time = start_time
        self.end_time = end_time

    def add_class(self, day, start_time, end_time, subject):
        if day not in self.schedule:
            raise ValueError(f"Invalid day: {day}")

        if start_time < self.start_time or end_time > self.end_time:
            raise ValueError(
                f"Error: Class '{subject}' is outside of school hours.")

        for block in self.schedule[day]:
            if start_time < block[1] and end_time > block[0]:
                raise ValueError(
                    f"Error: Class '{subject}' overlaps with class '{block[2]}'."
                )

        self.schedule[day].append((start_time, end_time, subject))

    def remove_class(self, day, subject):
        if day not in self.schedule:
            raise ValueError(f"Invalid day: {day}")

        self.schedule[day] = [
            block for block in self.schedule[day] if block[2] != subject
        ]

    def add_lunch(self, time, day):
        if time < self.start_time or time > self.end_time:
            raise ValueError(
                f"Error: Lunch time '{time}' is outside of school hours.")

        self.schedule[day].append((time, day, "Lunch"))

        # Sort the schedule based on start time
        self.schedule[day] = sorted(self.schedule[day], key=lambda x: x[0])

    def view_schedule(self):
        for day, blocks in self.schedule.items():
            print(f"\n{day}:")
            for block in sorted(blocks, key=lambda x: x[0]):
                print(f"{block[0]}-{block[1]}: {block[2]}")

    def get_ordered_classes(self, day):
        """
        Returns a list of classes ordered based on the schedule for a given day.
        """
        classes = []
        blocks = self.schedule.get(day)

        if not blocks:
            return classes

        for block in sorted(blocks, key=lambda x: x[0]):
            classes.append(block[2])

        return classes
