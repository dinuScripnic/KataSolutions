from abc import ABC, abstractmethod


class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdater(ABC):

    @staticmethod
    @abstractmethod
    def update_item(item: Item):
        pass


def decrease_item_quality(item: Item, amount: int = 1) -> None:
    item.quality = max(item.quality - amount, 0)


def increase_item_quality(item: Item, amount: int = 1, max_quality: int = 50) -> None:
    item.quality = min(item.quality + amount, max_quality)


class DefaultItem(ItemUpdater):
    @staticmethod
    def _passed_sell_date(item: Item) -> bool:
        return item.sell_in <= 0

    @staticmethod
    def _update_quality(item: Item):
        decrease_item_quality(item)
        if DefaultItem._passed_sell_date(item):
            decrease_item_quality(item)

    @staticmethod
    def _update_sell_in(item: Item):
        item.sell_in = max(0, item.sell_in - 1)

    @staticmethod
    def update_item(item: Item):
        DefaultItem._update_quality(item)
        DefaultItem._update_sell_in(item)


class AgedBrie(ItemUpdater):

    @staticmethod
    def _update_quality(item: Item):
        increase_item_quality(item)

    @staticmethod
    def _update_sell_in(item: Item):
        item.sell_in = max(0, item.sell_in - 1)

    @staticmethod
    def update_item(item: Item):
        AgedBrie._update_quality(item)
        AgedBrie._update_sell_in(item)


class Sulfuras(ItemUpdater):
    @staticmethod
    def _update_quality(item: Item):
        item.quality = min(item.quality, 80)

    @staticmethod
    def _update_sell_in(item: Item):
        item.sell_in = max(0, item.sell_in)

    @staticmethod
    def update_item(item: Item):
        Sulfuras._update_sell_in(item)
        Sulfuras._update_quality(item)


class BackstagePasses(ItemUpdater):
    @staticmethod
    def _update_quality(item: Item):
        increase_item_quality(item)

        if item.sell_in <= 10:
            increase_item_quality(item)

        if item.sell_in <= 5:
            increase_item_quality(item)

        if item.sell_in <= 0:
            item.quality = 0

    @staticmethod
    def _update_sell_in(item: Item):
        item.sell_in = max(0, item.sell_in - 1)

    @staticmethod
    def update_item(item: Item):
        BackstagePasses._update_quality(item)
        BackstagePasses._update_sell_in(item)


class Conjured(ItemUpdater):
    @staticmethod
    def _update_quality(item: Item):
        decrease_item_quality(item, 2)

    @staticmethod
    def _update_sell_in(item: Item):
        item.sell_in = max(0, item.sell_in - 1)

    @staticmethod
    def update_item(item: Item):
        Conjured._update_quality(item)
        Conjured._update_sell_in(item)


item_mapping: dict[str, ItemUpdater] = {
    "Aged Brie": AgedBrie,
    "Sulfuras, Hand of Ragnaros": Sulfuras,
    "Backstage passes to a TAFKAL80ETC concert": BackstagePasses,
    "Conjured": Conjured,
}


class GildedRose:

    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = item_mapping.get(item.name, DefaultItem)
            updater.update_item(item)
