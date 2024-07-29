class Rotor:
    def __init__(self, 
                 number: int, 
                 offset: int, 
                 neighbour = None, 
                 has_neighbour: bool = False) -> None:
        self.number = number
        self.neighbour = neighbour
        self.has_neighbour = has_neighbour
        self.complementary = {}
        self.offset = min(25, abs(offset))

        match self.number:
            case 1:
                self.wiring = {"A": "P", "B": "E", "C": "Z", "D": "U", "E": "O", "F": "H", "G": "X", "H": "S", "I": "C", "J": "V", "K": "F", "L": "M", "M": "T", "N": "B", "O": "G", "P": "L", "Q": "R", "R": "I", "S": "N", "T": "Q", "U": "J", "V": "W", "W": "A", "X": "Y", "Y": "D", "Z": "K"}
                self.trigger = "Q"
            case 2:
                self.wiring = {"A": "Z", "B": "O", "C": "U", "D": "E", "E": "S", "F": "Y", "G": "D", "H": "K", "I": "F", "J": "W", "K": "P", "L": "C", "M": "I", "N": "Q", "O": "X", "P": "H", "Q": "M", "R": "V", "S": "B", "T": "L", "U": "G", "V": "N", "W": "J", "X": "R", "Y": "A", "Z": "T"}
                self.trigger = "E"
            case 3:
                self.wiring = {"A": "E", "B": "H", "C": "R", "D": "V", "E": "X", "F": "G", "G": "A", "H": "O", "I": "B", "J": "Q", "K": "U", "L": "S", "M": "I", "N": "M", "O": "Z", "P": "F", "Q": "L", "R": "Y", "S": "N", "T": "W", "U": "K", "V": "T", "W": "P", "X": "D", "Y": "J", "Z": "C"}
                self.trigger = "V"
            case 4:
                self.wiring = {"A": "I", "B": "M", "C": "E", "D": "T", "E": "C", "F": "G", "G": "F", "H": "R", "I": "A", "J": "Y", "K": "S", "L": "Q", "M": "B", "N": "Z", "O": "X", "P": "W", "Q": "L", "R": "H", "S": "K", "T": "D", "U": "V", "V": "U", "W": "P", "X": "O", "Y": "J", "Z": "N"}
                self.trigger = "J"
            case 5:
                self.wiring = {"A": "Q", "B": "W", "C": "E", "D": "R", "E": "T", "F": "Z", "G": "U", "H": "I", "I": "O", "J": "A", "K": "S", "L": "D", "M": "F", "N": "G", "O": "H", "P": "J", "Q": "K", "R": "P", "S": "Y", "T": "X", "U": "C", "V": "V", "W": "B", "X": "N", "Y": "M", "Z": "L"}
                self.trigger = "Z"

        if self.offset > 0:
            keys = list(self.wiring.keys())
            values = list(self.wiring.values())
            keys_prev = keys[:-self.offset]
            keys_aft = keys[self.offset:]
            keys_aft.extend(keys_prev)
            self.wiring = {}
            for k, v in zip(keys_aft, values):
                self.wiring[k] = v            

        self.make_complementary()


    def turn(self) -> None:
        letters = list(self.wiring.keys())
        last = letters[-1]
        prev = letters[:-1]
        letters = [last]
        letters.extend(prev)
        vals = list(self.wiring.values())
        self.wiring = {}
        for k, v in zip(letters, vals):
            self.wiring[k] = v

        self.make_complementary()

        if list(self.wiring.keys())[0] == self.trigger:
            if self.has_neighbour:
                self.neighbour.turn()
            

    def make_complementary(self) -> None:
        self.complementary = {}
        for k, v in self.wiring.items():
            self.complementary[v] = k


    def get_char(self, letter: str, forward: bool) -> str:
        self.turn()
        if forward:
            return self.wiring[letter]
        if not forward:
            return self.complementary[letter]
    

    def get_config(self) -> tuple[int, int]:
        return self.number, self.offset