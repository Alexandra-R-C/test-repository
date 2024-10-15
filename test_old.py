from common import ItemMakingMapper
from old import OldItemMaker


ITEM_MAKER = ItemMakingMapper({
    'Observer Ward': '1',
    'Old Card Album': '2',
    'Silksong Preorder Key': '3',
    'Sol Blade': '4',
}, OldItemMaker())


# Ensure item instantiation is always done through `ITEM_MAKER`

def test_invalid():
    item = ITEM_MAKER.make('Invalid', 10, 10)
    assert item is None
