package main

import (
	"cards/deck"
	"fmt"
)

func main() {
	myCards := deck.NewDeck()

	for i, card := range myCards {
		fmt.Println("My card:", i, card)
	}
}
