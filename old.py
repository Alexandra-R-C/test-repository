from common import ItemInterface


class OldItemMaker:
    def make(self, name: str, category: str, days_left: int, value: int) -> ItemInterface | None:
        if category != '':
            return OldItemImpl(name, days_left, value)


class OldItemImpl:
    def __init__(self, name: str, days_left: int, value: int):
        self.name = name
        self.days_left = days_left
        self.value = value

    def next_day(self):
        if self.name != "Old Card Album" and self.name != "Silksong Preorder Key":
            if self.value > 0:
                if self.name != "Sol Blade":
                    self.value = self.value - 1
        else:
            if self.value < 50:
                self.value = self.value + 1
                if self.name == "Silksong Preorder Key":
                    if self.days_left < 11:
                        if self.value < 50:
                            self.value = self.value + 1
                    if self.days_left < 6:
                        if self.value < 50:
                            self.value = self.value + 1
        if self.name != "Sol Blade":
            self.days_left = self.days_left - 1
        if self.days_left < 0:
            if self.name != "Old Card Album":
                if self.name != "Silksong Preorder Key":
                    if self.value > 0:
                        if self.name != "Sol Blade":
                            self.value = self.value - 1
                else:
                    self.value = self.value - self.value
            else:
                if self.value < 50:
                    self.value = self.value + 1
