class Adder:
    def __init__(self, nbr1: str, nbr2: str) -> None:
        self.nbr1 = nbr1
        self.nbr2 = nbr2
    
    def sum(self) -> int:
        return self.nbr1 + self.nbr2

    def mult(self) -> int:
        return self.nbr1 * self.nbr2
