package deck

import (
	"fmt"
	"math/rand"
	"os"
	"strings"
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

func (d Deck) ToString() string {
	return strings.Join([]string(d), ",")
}

func (d Deck) SaveToFile(filename string) error {
	return os.WriteFile(filename, []byte(d.ToString()), 0666)
}

func NewDeckFromFile(filename string) Deck {
	bs, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println("Error:",err)
		os.Exit(1)
	}
	s := strings.Split(string(bs), ",")

	return Deck(s)
}
