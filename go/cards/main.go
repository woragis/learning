package main

import (
	"cards/deck"
)

func main() {
	myCards := deck.NewDeck()

	cards, remaining := deck.Deal(myCards, 8)
	cards.Print()
	remaining.Print()
}
