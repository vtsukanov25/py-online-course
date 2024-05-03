from typing import Dict


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: Dict[str, str]) -> "OnlineCourse":
        weeks = cls.days_to_weeks(int(course_dict["days"]))
        return cls(course_dict["name"], course_dict["description"], weeks)
