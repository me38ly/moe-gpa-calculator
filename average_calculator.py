from dataclasses import dataclass
from typing import List, Union

@dataclass
class Subject:
    name: str
    grade: float
    weighted_grade: float

@dataclass
class AverageResult:
    average: str
    subjects: List[Subject]

def calculate_average(subjects: List[dict], grade_number: int) -> AverageResult:
    total_weighted_grade = 0.0
    total_weight = 0.0
    processed_subjects: List[Subject] = []

    for subject in subjects:
        try:
            grade = float(subject.get("grade", 0))
            weight = float(subject.get("weight", 0))
        except (ValueError, TypeError):
            continue

        if weight == 0:
            continue

        weighted_grade = grade * weight
        processed_subjects.append(
            Subject(
                name=subject.get("name", None),
                grade=grade,
                weighted_grade=weighted_grade
            )
        )

        total_weighted_grade += weighted_grade
        total_weight += weight

    if grade_number < 10:
        total_weighted_grade += 100 * 2
        total_weight += 2

    average = round(total_weighted_grade / total_weight, 2) if total_weight else 0.0

    return AverageResult(
        average=f"{average:.2f}",
        subjects=processed_subjects
    )
    
# Example   
subjects = [
    {"name": "القران الكريم والدراسات الاسلامية", "weight": 5, "grade": 100},
    {"name": "اللغة العربية", "weight": 4, "grade": 100},
    {"name": "الدراسات الاجتماعية", "weight": 2, "grade": 100},
    {"name": "الرياضيات", "weight": 6, "grade": 100},
    {"name": "العلوم", "weight": 4, "grade": 100},
    {"name": "اللغة الانجليزية", "weight": 4, "grade": 100},
    {"name": "المهارات الرقمية", "weight": 2, "grade": 100},
    {"name": "التربية الفنية", "weight": 2, "grade": 100},
    {"name": "التربية بدنية", "weight": 2, "grade": 100},
    {"name": "التفكير الناقد", "weight": 2, "grade": 100},
    {"name": "المهارات الحياتية و الاسرية", "weight": 1, "grade": 99}
]

print(calculate_average(subjects, 9))
