class AgeGroup:
    def __init__(self, start, end, last=False):
        self.start = start
        self.end = end
        self.last = last

    def contains(self, age):
        """Функция проверяет, входит ли возраст в данную возрастную группу"""
        return self.start < age <= self.end

    def str(self):
        """Функция возвращает строку с границами возрастной группы"""
        if self.last:
            return f"{self.start}+"

        return f"{self.start}-{self.end}"


class Respondent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def str(self):
        """Функция возвращает строку с именем и возрастом респондента"""
        return f"{self.name} ({self.age})"


class AgeGroupDivider:
    def __init__(self, age_groups):
        self.age_groups = age_groups
        self.grouped_respondents = {group: [] for group in self.age_groups}

    def add_respondent(self, respondent):
        """Функция добавляет респондента в нужную возрастную группу"""
        for group in self.age_groups:
            if group.contains(respondent.age):
                self.grouped_respondents[group].append(respondent)
                break

    def display_groups(self):
        """Функция выводит в корректном формате возрастные группы и респондентов"""
        for group in reversed(self.age_groups):
            if self.grouped_respondents[group]:
                print(f"{group.str()}: ", end="")
                print(
                    ", ".join(
                        respondent.str()
                        for respondent in sorted(self.grouped_respondents[group], key=lambda x: (-x.age, x.name))
                    )
                )


def parse_age_groups(args):
    """Функция возвращает список возрастных групп, определяемых последовательностью возрастов"""
    ages = [-1] + [int(arg) for arg in args]
    age_groups = []
    for i in range(len(ages)):
        if i == len(ages) - 1:
            age_groups.append(AgeGroup(ages[i] + 1, 123, last=True))
        else:
            age_groups.append(AgeGroup(ages[i] + 1, ages[i + 1]))
    return age_groups


if __name__ == "__main__":
    with open("age_groups.txt", "r", encoding="UTF-8") as f:
        age_groups = parse_age_groups(map(int, f.readline().split()))

    divider = AgeGroupDivider(age_groups)

    with open("respondents.txt", "r", encoding="UTF-8") as f:
        for line in f.readlines():
            if line == "END":
                break
            name, age = line.split(",")
            respondent = Respondent(name.strip(), int(age.strip()))
            divider.add_respondent(respondent)

    divider.display_groups()
