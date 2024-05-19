package gildedrose_test

import (
	"testing"

	"github.com/emilybache/gildedrose-refactoring-kata/gildedrose"
)

func Test_Foo(t *testing.T) {
	var items = []*gildedrose.Item{
		{"foo", 0, 0},
	}

	gildedrose.UpdateQuality(items)

	if items[0].Name != "foo" {
		t.Errorf("Name: Expected %s but got %s ", "fixme", items[0].Name)
	}
}

func Test_ItemDecreasesQuality(t *testing.T) {
	var items = []*gildedrose.Item{
		{"foo", 1, 1},
	}

	gildedrose.UpdateQuality(items)

	if items[0].Quality != 0 {
		t.Errorf("Quality: Expected %d but got %d ", 0, items[0].Quality)
	}
}

func Test_ItemDecreasesSellIn(t *testing.T) {
	var items = []*gildedrose.Item{
		{"foo", 1, 1},
	}

	gildedrose.UpdateQuality(items)

	if items[0].SellIn != 0 {
		t.Errorf("SellIn: Expected %d but got %d ", 0, items[0].SellIn)
	}
}

func Test_ItemDecreasesQualtyTwiceAsFast(t *testing.T) {
	var items = []*gildedrose.Item{
		{"foo", 0, 2},
	}

	gildedrose.UpdateQuality(items)

	if items[0].Quality != 0 {
		t.Errorf("Quality: Expected %d but got %d ", 0, items[0].Quality)
	}
}

func Test_ItemQualityIsNeverNegative(t *testing.T) {
	var items = []*gildedrose.Item{
		{"foo", 0, 0},
	}

	gildedrose.UpdateQuality(items)

	if items[0].Quality != 0 {
		t.Errorf("Quality: Expected %d but got %d ", 0, items[0].Quality)
	}
}

func Test_AgedBrieIncreasesQuality(t *testing.T) {
	var items = []*gildedrose.Item{
		{"Aged Brie", 1, 0},
	}

	gildedrose.UpdateQuality(items)

	if items[0].Quality != 1 {
		t.Errorf("Quality: Expected %d but got %d ", 1, items[0].Quality)
	}
}

func Test_ItemQualityIsNeverMoreThan50(t *testing.T) {
	var items = []*gildedrose.Item{
		{"Test", 1, 100},
	}

	gildedrose.UpdateQuality(items)

	if items[0].Quality <= 50 {
		t.Errorf("Quality: Expected %d but got %d ", 50, items[0].Quality)
	}
}

func Test_SulfurasDoesNotDecreaseQuality(t *testing.T) {
	initialQuality := int8(50)
	var items = []*gildedrose.Item{
		{"Sulfuras, Hand of Ragnaros", 1, initialQuality},
	}

	gildedrose.UpdateQuality(items)

	if items[0].Quality != initialQuality {
		t.Errorf("Quality: Expected %d but got %d ", 80, items[0].Quality)
	}
}

func Test_SulfurasIsNeverSold(t *testing.T) {
	initialSellIn := int8(1)
	var items = []*gildedrose.Item{
		{"Sulfuras, Hand of Ragnaros", initialSellIn, 80},
	}

	gildedrose.UpdateQuality(items)

	if items[0].SellIn != initialSellIn {
		t.Errorf("SellIn: Expected %d but got %d ", 1, items[0].SellIn)
	}
}

func Test_BackstagePassesIncreaseQuality(t *testing.T) {
	var items = []*gildedrose.Item{
		{"Backstage passes to a TAFKAL80ETC concert", 12, 0},
	}

	gildedrose.UpdateQuality(items)

	if items[0].Quality != 1 {
		t.Errorf("Quality: Expected %d but got %d ", 1, items[0].Quality)
	}
}

func Test_BackstagePassesIncreaseQualityBy2When10DaysLeft(t *testing.T) {
	var items = []*gildedrose.Item{
		{"Backstage passes to a TAFKAL80ETC concert", 10, 0},
	}

	gildedrose.UpdateQuality(items)

	if items[0].Quality != 2 {
		t.Errorf("Quality: Expected %d but got %d ", 2, items[0].Quality)
	}
}

func Test_BackstagePassesIncreaseQualityBy3When5DaysLeft(t *testing.T) {
	var items = []*gildedrose.Item{
		{"Backstage passes to a TAFKAL80ETC concert", 5, 0},
	}

	gildedrose.UpdateQuality(items)

	if items[0].Quality != 3 {
		t.Errorf("Quality: Expected %d but got %d ", 3, items[0].Quality)
	}
}

func Test_BackstagePassesQualityIsZeroAfterConcert(t *testing.T) {
	var items = []*gildedrose.Item{
		{"Backstage passes to a TAFKAL80ETC concert", 0, 50},
	}

	gildedrose.UpdateQuality(items)

	if items[0].Quality != 0 {
		t.Errorf("Quality: Expected %d but got %d ", 0, items[0].Quality)
	}
}

func Test_SulfurasHas80Quality(t *testing.T) {
	initialQuality := int8(80)
	var items = []*gildedrose.Item{
		{"Sulfuras, Hand of Ragnaros", 0, initialQuality},
	}

	gildedrose.UpdateQuality(items)

	if items[0].Quality != initialQuality {
		t.Errorf("Quality: Expected %d but got %d ", initialQuality, items[0].Quality)
	}
}

func Test_ConjuredItemsDecreaseQualityTwiceAsFast(t *testing.T) {
	var items = []*gildedrose.Item{
		{"Conjured", 1, 2},
	}

	gildedrose.UpdateQuality(items)

	if items[0].Quality != 0 {
		t.Errorf("Quality: Expected %d but got %d ", 0, items[0].Quality)
	}
}

func Test_ConjuredItemsDecreaseQualityBy4AfterSellIn(t *testing.T) {
	var items = []*gildedrose.Item{
		{"Conjured", 0, 4},
	}

	gildedrose.UpdateQuality(items)

	if items[0].Quality != 0 {
		t.Errorf("Quality: Expected %d but got %d ", 0, items[0].Quality)
	}
}
