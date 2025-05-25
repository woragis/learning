package deck

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
