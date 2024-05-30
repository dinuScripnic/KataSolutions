from gilded_rose import Item, GildedRose


class Test_DefaultItem:

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert "foo" == items[0].name

    def test_item(self):
        item = Item("TestName", 10, 10)
        assert item is not None

    def test_decrease_quality(self):
        NAME = "Test"
        INITIAL_QUALITY = 50
        INITIAL_SELL_IN = 10
        items = [Item(NAME, INITIAL_SELL_IN, INITIAL_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == INITIAL_QUALITY - 1
        assert gilded_rose.items[0].sell_in == INITIAL_SELL_IN - 1

    def test_sell_date_passed_quality_decreases_twice_as_fast(self):
        INITIAL_QUALITY = 50
        INITIAL_SELL_IN = 0
        items = [Item("Test", INITIAL_SELL_IN, INITIAL_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == INITIAL_QUALITY - 2

    def test_quality_is_never_more_than_50(self):
        NAME = "Test"
        INITIAL_QUALITY = 100
        INITIAL_SELL_IN = 10
        items = [Item(NAME, INITIAL_SELL_IN, INITIAL_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality <= 50

    def test_quality_is_never_negative(self):
        NAME = "Test"
        INITIAL_QUALITY = 0
        INITIAL_SELL_IN = 10
        item = Item(NAME, INITIAL_SELL_IN, INITIAL_QUALITY)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 0


class Test_AgedBrie:
    NAME = "Aged Brie"

    def test_aged_brie_quality_increases(self):
        INITIAL_QUALITY = 10
        INITIAL_SELL_IN = 10
        items = [Item(self.NAME, INITIAL_SELL_IN, INITIAL_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == INITIAL_QUALITY + 1

    def test_aged_brie_decrease_sell_in(self):
        INITIAL_QUALITY = 10
        INITIAL_SELL_IN = 10
        items = [Item(self.NAME, INITIAL_SELL_IN, INITIAL_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].sell_in == INITIAL_SELL_IN - 1


class Test_Sulfuras:
    NAME = "Sulfuras, Hand of Ragnaros"

    def test_sulfuras_never_decreases_in_quality(self):
        INITIAL_QUALITY = 10
        INITIAL_SELL_IN = 10
        items = [Item(self.NAME, INITIAL_SELL_IN, INITIAL_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == INITIAL_QUALITY

    def test_sulfuras_is_never_sold(self):
        INITIAL_QUALITY = 10
        INITIAL_SELL_IN = 10
        items = [Item(self.NAME, INITIAL_SELL_IN, INITIAL_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].sell_in == INITIAL_SELL_IN

    def test_sulfuras_quality_is_80(self):
        INITIAL_QUALITY = 80
        INITIAL_SELL_IN = 10
        items = [Item(self.NAME, INITIAL_SELL_IN, INITIAL_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == INITIAL_QUALITY


class Test_BackstagePasses:
    NAME = "Backstage passes to a TAFKAL80ETC concert"

    def test_backstage_passes_quality_increases(self):
        INITIAL_QUALITY = 10
        INITIAL_SELL_IN = 15
        items = [Item(self.NAME, INITIAL_SELL_IN, INITIAL_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == INITIAL_QUALITY + 1

    def test_backstage_passes_quality_increase_by_2_when_10_days_or_less_left(self):
        INITIAL_QUALITY = 10
        INITIAL_SELL_IN = 10
        items = [Item(self.NAME, INITIAL_SELL_IN, INITIAL_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == INITIAL_QUALITY + 2

    def test_backstage_passes_quality_increase_by_3_when_5_days_or_less_left(self):
        INITIAL_QUALITY = 10
        INITIAL_SELL_IN = 5
        items = [Item(self.NAME, INITIAL_SELL_IN, INITIAL_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == INITIAL_QUALITY + 3

    def test_backstage_passes_quality_drops_to_0_after_concert(self):
        INITIAL_QUALITY = 10
        INITIAL_SELL_IN = 0
        items = [Item(self.NAME, INITIAL_SELL_IN, INITIAL_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == 0


class Test_Conjured:
    NAME = "Conjured"

    def test_conjured_decrease_quality_twice_fast(self):
        INITIAL_QUALITY = 10
        INITIAL_SELL_IN = 10
        items = [Item(self.NAME, INITIAL_SELL_IN, INITIAL_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality == INITIAL_QUALITY - 2
