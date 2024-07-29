class Plugboard:
    def __init__(self, is_military = False) -> None:
        self.configuration: dict[str, str] = {
            "A": "B",
            "C": "D",
            "E": "F",
            "G": "H",
            "I": "J",
            "K": "L",
            "M": "N",
            "O": "P",
            "Q": "R",
            "S": "T",
            "U": "V"
            }
        self.make_complementary()
        self.is_military: bool = is_military


    def make_complementary(self) -> None:
        self.complementary = {}
        for k, v in self.configuration.items():
            self.complementary[v] = k


    def get_char(self, s: str, forward: bool) -> str:
        if self.is_military:
            if s in self.configuration.keys() and forward:
                return self.configuration[s]
            elif not forward and s in self.complementary.keys():
                return self.complementary[s]
            else:
                return s
        else:
            return s
    

    def get_config(self) -> tuple[bool, dict[str, str]]:
        return self.is_military, self.configuration