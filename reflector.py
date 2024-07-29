class Reflector:
    def __init__(self) -> None:
        self.wiring: dict[str, str] = {
                    "A": "Y",
                    "B": "R",
                    "C": "U",
                    "D": "H",
                    "E": "Q",
                    "F": "S",
                    "G": "L",
                    "I": "P",
                    "J": "X",
                    "K": "N",
                    "M": "O",
                    "T": "Z",
                    "V": "W"
                    }
        
        keys = list(self.wiring.keys())
        vals = list(self.wiring.values())
        for k, v in zip(keys, vals):
            self.wiring[v] = k
        
        del keys
        del vals
        

    def get_char(self, char: str) -> str:
        return self.wiring[char]