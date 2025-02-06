class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(self.MEOWS):
            print('meow')


if __name__ == '__main__':
    cat = Cat()
    cat.meow()
