package main

import (
	"cards/deck"
)

func main() {
	myCards := deck.NewDeck()

	myCards.SaveToFile("cards")

	cards := deck.NewDeckFromFile("cards")
	cards.Print()
}
