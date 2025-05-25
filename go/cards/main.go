package main

import (
	"cards/deck"
)

func main() {
	myCards := deck.NewDeck()

	myCards.Shuffle()
	myCards.Print()
}
