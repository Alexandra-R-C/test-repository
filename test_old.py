from common import ItemMakingMapper
from old import OldItemMaker

ITEM_MAKER = ItemMakingMapper({
    'Observer Ward': '1',
    'Old Card Album': '2',
    'Silksong Preorder Key': '3',
    'Sol Blade': '4',
}, OldItemMaker())

# stockAge, stockValue, daysToPass
CASES = (
    (3, 3, 1),
    (0, 3, 10),
    (3, 3, 4),
    (3, 9, 5),
    (3, 9, 9),
    (1, 0, 1),
    (1, 51, 1),
    (-1, 51, 1),
    (1, 51, 1),
    (3, 49, 6),
    (69, 420, 69),
    (30, 0, 30),
    (30, 0, 29),
)

# Test to make an invalid item; item must be none
def test_invalid():
    item = ITEM_MAKER.make('Invalid', 10, 10)
    assert item is None

# Test to make a valid item; item must have correct values
def test_valid():
    item = ITEM_MAKER.make('Observer Ward', 10, 10)
    assert item is not None
    assert item.name == 'Observer Ward'
    assert item.days_left == 10
    assert item.value == 10

# Tests for depreciating items whose value decreases as time passes
def test_depreciating():
    for case in CASES:
        stockAge, stockValue, daysToPass = case
        item = ITEM_MAKER.make('Observer Ward', stockAge, stockValue)
        for i in range(daysToPass):
            item.next_day()
        assert item.days_left == stockAge - daysToPass
        if stockAge < 0:
            assert item.value == max(0, stockValue - 2 * daysToPass)
        else:
            assert item.value == max(0, stockValue - daysToPass - max(0, daysToPass - stockAge))

# Test for appreciating items whose value increases as time passes
def test_appreciating():
    for case in CASES:
        stockAge, stockValue, daysToPass = case
        item = ITEM_MAKER.make('Old Card Album', stockAge, stockValue)
        for i in range(daysToPass):
            item.next_day()
        assert item.days_left == stockAge - daysToPass
        assert item.value == min(max(50, stockValue), stockValue + daysToPass + max(0, daysToPass - stockAge))

# Test for expiring items whose value increases as time passes, but becomes worthless once it's reached its age
def test_expiring():
    for case in CASES:
        stockAge, stockValue, daysToPass = case
        item = ITEM_MAKER.make('Silksong Preorder Key', stockAge, stockValue)
        finalValue = stockValue
        for i in range(daysToPass):
            item.next_day()
            if item.value < 50:
                finalValue += 1
                if item.days_left < 5 and item.value < 50:
                    finalValue += 1
                if item.days_left < 10 and item.value < 50:
                    finalValue += 1

        
        assert item.days_left == stockAge - daysToPass
        
        if item.days_left < 0:
            assert item.value == 0
        else:
            if item.value != finalValue:
                print(stockAge, stockValue, daysToPass)
            assert item.value == finalValue


def test_evergreen():
    for case in CASES:
        stockAge, stockValue, daysToPass = case
        item = ITEM_MAKER.make('Sol Blade', stockAge, stockValue)
        for i in range(daysToPass):
            item.next_day()
        assert item.days_left == stockAge
        assert item.value == stockValue
