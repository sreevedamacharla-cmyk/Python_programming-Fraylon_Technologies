class GradeTracker:
    def __init__(self):
        # name -> {subject: mark}
        self.students = {}
        # every subject ever recorded (unique) -> a SET
        self.subjects = set()

    # --------- CREATE / UPDATE ---------
    def add_student(self, name):
        if name in self.students:
            raise ValueError(f"'{name}' already exists")
        self.students[name] = {}  # dict of subject -> mark

    def record_mark(self, name, subject, mark):
        if name not in self.students:  # guard: unknown student
            raise KeyError(f"No student named '{name}'")
        if not 0 <= mark <= 100:  # guard: valid range
            raise ValueError("mark must be 0..100")
        self.students[name][subject] = mark  # add OR overwrite
        self.subjects.add(subject)  # set ignores duplicates

    # --------- READ ---------
    def average(self, name):
        marks = self.students[name].values()
        return sum(marks) / len(marks) if marks else 0.0

    def topper(self):
        # tuple (name, avg) chosen by highest average
        if not self.students:
            return None
        return max(((n, self.average(n)) for n in self.students), key=lambda t: t[1])

    def ranking(self):
        # list of (name, avg) tuples, best first; tie-break by name
        board = [(n, round(self.average(n), 2)) for n in self.students]
        board.sort(key=lambda t: (-t[1], t[0]))
        return board

    def subject_toppers(self):
        # for each subject, who scored highest?
        best = {}
        for sub in self.subjects:
            scorers = [(n, self.students[n][sub]) for n in self.students if sub in self.students[n]]
            if scorers:
                best[sub] = max(scorers, key=lambda t: t[1])
        return best

    # --------- DELETE ---------
    def remove_student(self, name):
        self.students.pop(name, None)  # safe delete, no KeyError


# --------- DEMO ---------
if __name__ == "__main__":
    gt = GradeTracker()

    # Add students
    for name in ["Asha", "Ravi", "Kiran"]:
        gt.add_student(name)

    # Record marks
    gt.record_mark("Asha", "math", 92);  gt.record_mark("Asha", "cs", 88)
    gt.record_mark("Ravi", "math", 75);  gt.record_mark("Ravi", "cs", 95)
    gt.record_mark("Kiran", "math", 88); gt.record_mark("Kiran", "cs", 90)

    # Display results
    print("Averages :", {n: round(gt.average(n), 2) for n in gt.students})
    print("Topper   :", gt.topper())
    print("Ranking  :", gt.ranking())
    print("Subjects :", gt.subjects)
    print("Per-sub  :", gt.subject_toppers())