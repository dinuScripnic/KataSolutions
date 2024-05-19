package gildedrose

type Item struct {
	Name    string
	SellIn  int8
	Quality int8
}

const DEFAULT_MAX_QUALITY = 50
const DEFAULT_MIN_QUALITY = 0
const SULFURAS_MAX_QUALITY = 80

func decreaseItemQuality(item *Item, minValue int8) {
	if item.Quality > minValue {
		item.Quality = item.Quality - 1
	}
}
func increaseItemQuality(item *Item, maxValue int8) {
	if item.Quality < maxValue {
		item.Quality = item.Quality + 1
	}
}

type ItemUpdater interface {
	uptadeItem(item *Item)
}

type DefaultUpdater struct {
}

func (DefaultUpdater) uptadeItem(item *Item) {
	item.SellIn = item.SellIn - 1
	decreaseItemQuality(item, DEFAULT_MIN_QUALITY)
	if item.SellIn < 0 {
		decreaseItemQuality(item, DEFAULT_MIN_QUALITY)
	}
}

type AgedBrieUpdater struct {
}

func (AgedBrieUpdater) uptadeItem(item *Item) {
	item.SellIn = item.SellIn - 1
	increaseItemQuality(item, DEFAULT_MAX_QUALITY)
}

type SulfurasUpdater struct {
}

func (SulfurasUpdater) uptadeItem(item *Item) {
	if item.Quality > SULFURAS_MAX_QUALITY {
		item.Quality = SULFURAS_MAX_QUALITY
	}
}

type BackstagePassesUpdater struct {
}

func (BackstagePassesUpdater) uptadeItem(item *Item) {
	item.SellIn = item.SellIn - 1
	increaseItemQuality(item, DEFAULT_MAX_QUALITY)
	if item.SellIn < 10 {
		increaseItemQuality(item, DEFAULT_MAX_QUALITY)
	}
	if item.SellIn < 5 {
		increaseItemQuality(item, DEFAULT_MAX_QUALITY)
	}
	if item.SellIn < 0 {
		item.Quality = 0
	}
}

type ConjuredUpdater struct {
}

func (ConjuredUpdater) uptadeItem(item *Item) {
	item.SellIn = item.SellIn - 1
	decreaseItemQuality(item, DEFAULT_MIN_QUALITY)
	decreaseItemQuality(item, DEFAULT_MIN_QUALITY)
	if item.SellIn < 0 {
		decreaseItemQuality(item, DEFAULT_MIN_QUALITY)
		decreaseItemQuality(item, DEFAULT_MIN_QUALITY)
	}
}

type UpdaterFactory struct {
	updaterMap map[string]ItemUpdater
}

func NewUpdaterFactory() UpdaterFactory {
	updaterMap := make(map[string]ItemUpdater)
	updaterMap["Aged Brie"] = AgedBrieUpdater{}
	updaterMap["Sulfuras, Hand of Ragnaros"] = SulfurasUpdater{}
	updaterMap["Backstage passes to a TAFKAL80ETC concert"] = BackstagePassesUpdater{}
	updaterMap["Conjured"] = ConjuredUpdater{}
	return UpdaterFactory{updaterMap}
}

func (factory *UpdaterFactory) get(item *Item) ItemUpdater {
	updater, ok := factory.updaterMap[item.Name]
	if ok {
		return updater
	}
	return DefaultUpdater{}
}

func UpdateQuality(items []*Item) {
	factory := NewUpdaterFactory()
	for _, item := range items {
		updater := factory.get(item)
		updater.uptadeItem(item)
	}
}
