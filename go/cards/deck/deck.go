package deck

import (
	"fmt"
	"math/rand"
	"time"
)

type Deck []string

func NewDeck() Deck {
	d := Deck{}
	values := []string{"Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"}
	suits := []string{"Spades", "Diamonds", "Hearts", "Clubs"}

	for _, value := range values {
		for _, suit := range suits {
			d = append(d, value+" of "+suit)
		}
	}

	return d
}

func (d Deck) Print() {
	for i, card := range d {
		fmt.Println(i, card)
	}
}

func Deal(d Deck, handSize int) (Deck, Deck) {
	return d[:handSize], d[handSize:]
}

func (d Deck) Shuffle() {
	source := rand.NewSource(time.Now().UnixNano())
	r := rand.New(source)

	length := len(d) - 1
	for i := range d {
		newPosition := r.Intn(length)
		d[i], d[newPosition] = d[newPosition], d[i]
	}
}
