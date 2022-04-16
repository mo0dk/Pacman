class Achievement():
    def __init__(self, id, name, desc, need, isCountable = False):
        self.id = id
        self.name = name
        self.description = desc
        self.done = False
        self.current = 0
        self.goal = need
        self.countable = isCountable

    def progress(self):
        return self.current / self.goal
    def Get(self):
        self.done = True
        self.current = self.goal
    def changeName(self, newName):
        self.name = newName
    def changeDescription(self, newDesc):
        self.description = newDesc

achievements = [
    Achievement(1, "Убийца", "Съешьте 10 привидений", 10, True),
    Achievement(2, "Опытный", "Выиграйте 2 раза", 2, True),
    Achievement(3, "Играю в Пакмана 10 часов", "Ну, вы поняли :)", 36000, True),
    Achievement(4, "Спидран по Пакману, поехали!", "Съешьте все зёрна за минуту", 1),
    Achievement(5, "Секретная ачивка!", "???", 1)
]

def achievements_save_to_file():
    file = open('saves/ach.txt', 'w')
    for ach in achievements:
        file.write(str(ach.current) + '\n')
    file.close()

def achievements_load_from_file():
    saved = open('saves/ach.txt')
    lst = list(saved)
    for i in range(len(achievements)):
        achievements[i].current = int(lst[i][:-1])
    if (achievements[4].current == achievements[4].goal):
        achievements[4].done = True
        achievements[4].changeName("[СЕКРЕТ] Высокие технологии")
        achievements[4].changeDescription("Пройдите сквозь портал")
    saved.close()
