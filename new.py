from common import ItemInterface
import new_category as ItemCategory

class ItemMaker:
    def make(self, name: str, category: str, days_left: int, value: int) -> ItemInterface | None:
        if category in ItemCategory.CATEGORIES.keys():
            return ItemCategory.CATEGORIES[category](name, days_left, value)
        else:
            return None
