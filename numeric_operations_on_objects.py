class Employee:
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    def __lt__(self, other):
        if self.level>other.level:
            return self.level
        else:
            self.seniority<other.seniority
        return self.seniority


def main():
    # define some employees
    dept = []
    dept.append(Employee("Tim", "Sims", 5, 9))
    dept.append(Employee("John", "Doe", 4, 12))
    dept.append(Employee("Jane", "Smith", 6, 6))
    dept.append(Employee("Rebecca", "Robinson", 5, 13))
    dept.append(Employee("Tyler", "Durden", 5, 12))
    print(bool(dept[0] > dept[2]))
    print(bool(dept[4] < dept[3]))
    # TODO: sort the items


if __name__ == "__main__":
    main()

