class Subject {
  constructor(name, grade, weightedGrade) {
    this.name = name;
    this.grade = grade;
    this.weightedGrade = weightedGrade;
  }
}

class AverageResult {
  constructor(average, subjects) {
    this.average = average;
    this.subjects = subjects;
  }
}

function calculateAverage(subjects, gradeNumber) {
  let totalWeightedGrade = 0.0;
  let totalWeight = 0.0;
  let processedSubjects = [];

  for (let subject of subjects) {
    let grade = parseFloat(subject.grade) || 0;
    let weight = parseFloat(subject.weight) || 0;
    if (weight === 0) continue;

    let weightedGrade = grade * weight;

    processedSubjects.push(new Subject(
      subject.name ?? null,
      grade,
      weightedGrade
    ));

    totalWeightedGrade += weightedGrade;
    totalWeight += weight;
  }

  if (gradeNumber < 10) {
    totalWeightedGrade += 100 * 2;
    totalWeight += 2;
  }

  let average = totalWeight > 0 ? (totalWeightedGrade / totalWeight).toFixed(2) : "0.00";
  return new AverageResult(average, processedSubjects);
}

// Example
const subjects = [
  { name: "القران الكريم والدراسات الاسلامية", weight: 5, grade: 100 },
  { name: "اللغة العربية", weight: 4, grade: 100 },
  { name: "الدراسات الاجتماعية", weight: 2, grade: 100 },
  { name: "الرياضيات", weight: 6, grade: 100 },
  { name: "العلوم", weight: 4, grade: 100 },
  { name: "اللغة الانجليزية", weight: 4, grade: 100 },
  { name: "المهارات الرقمية", weight: 2, grade: 100 },
  { name: "التربية الفنية", weight: 2, grade: 100 },
  { name: "التربية بدنية", weight: 2, grade: 100 },
  { name: "التفكير الناقد", weight: 2, grade: 100 },
  { name: "المهارات الحياتية و الاسرية", weight: 1, grade: 99 }
];

const result = calculateAverage(subjects, 9);
console.log(result);
