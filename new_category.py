from new import DepreciatingItem

class ItemImplementation:
    def __init__(self, name: str, days_left: int, value: int):
        self.name = name
        self.days_left = days_left
        self.value = value

    def next_day(self):
        ...

class DepreciatingItem(ItemImplementation):
    def next_day(self):
        self.days_left -= 1
        self.value = max(0, self.value - (2 if self.days_left < 0 else 1))

class PerishableItem(DepreciatingItem):
    def next_day(self):
      self.days_left -= 1
      self.value = max(0, self.value - 3)

class AppreciatingItem(ItemImplementation):
    def next_day(self):
        self.days_left -= 1
        if self.value < 50:
          self.value += 1
          if self.days_left < 0:
            self.value += 1

class ExpiringItem(ItemImplementation):
    def next_day(self):
        self.days_left -= 1
        if self.days_left < 0:
            self.value = 0
        elif self.value < 50:
            self.value += 1
            if self.days_left < 5:
                self.value += 1
            if self.days_left < 10:
                self.value += 1

class EvergreenItem(ItemImplementation):
    ...

CATEGORIES = {
  '1': DepreciatingItem,
  '2': AppreciatingItem,
  '3': ExpiringItem,
  '4': EvergreenItem,
  '5': PerishableItem
}
