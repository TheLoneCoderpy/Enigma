from io import TextIOWrapper
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector

class Enigma:
    def __init__(self, 
                 num1: int = 1, 
                 num2: int = 2, num3: int = 3, 
                 rotor_1_offset=1, 
                 rotor_2_offset=0, 
                 rotor_3_offset=0, 
                 military = True) -> None:
        self.alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.plugboard = Plugboard(is_military=military)
        self.third_rotor = Rotor(number=num3, has_neighbour=False, offset=rotor_3_offset) # left
        self.second_rotor = Rotor(number=num2, neighbour=self.third_rotor, has_neighbour=True, offset=rotor_2_offset) # middle
        self.first_rotor = Rotor(number=num1, neighbour=self.second_rotor, has_neighbour=True, offset=rotor_1_offset) # right
        
        self.reflector = Reflector()


    def init(self) -> None:
        while 1:
            in_str = input("Text: ")
            if in_str == "q":
                break
            enigma_string = self.enigma_str(in_str)
            result = self.encode(enigma_string)
            print(result)


    def encode(self, text: str) -> str:
        result = ""
        for c in text:
            c_plugboard = self.plugboard.get_char(c, forward=True)
            c_first = self.first_rotor.get_char(c_plugboard, forward=True)
            c_second = self.second_rotor.get_char(c_first, forward=True)
            c_third = self.third_rotor.get_char(c_second, forward=True)
            c_middle = self.reflector.get_char(c_third)
            c_third_back = self.third_rotor.get_char(c_middle, forward=False)
            c_second_back = self.second_rotor.get_char(c_third_back, forward=False)
            c_first_back = self.first_rotor.get_char(c_second_back, forward=False)
            c_final = self.plugboard.get_char(c_first_back, forward=False)
            result += c_final
        return result


    def enigma_str(self, text: str) -> str:
        nogo_chars: list[str] = ["!", '"', "§", "$", "%", "&", "/", "(", ")", "=", "?", "`", "{", "[", "]", "}", "\\", "°", "^", "+", "*", "~", "'", "#", ",", ";", ".", ":", "-", "_", "@", " "]
        multi_chars: dict[str, str] = {"Ü": "UE", "Ö": "OE", "Ä": "AE"}
        text = text.upper()
        s = ""
        for c in text:
            if c not in nogo_chars:
                if c in list(multi_chars.keys()):
                    c = multi_chars[c]
                s += c
        return s
    

    def get_config(self) -> str:
        pl_mil, pl_config = self.plugboard.get_config()
        r1_num, r1_off = self.first_rotor.get_config()
        r2_num, r2_off = self.second_rotor.get_config()
        r3_num, r3_off = self.third_rotor.get_config()
        return f"plugboard;{pl_mil};{pl_config};rotor1;{r1_num};{r1_off};rotor2;{r2_num};{r2_off};rotor3;{r3_num};{r3_off}"


    def configuration_from_file(self, path: str) -> None:
        try:
            file: TextIOWrapper = open(path, "r")
            cont: list[str] = file.read().split(";")
            print(cont)

            r3 = Rotor(number=int(cont[10]), offset=int(cont[11]), has_neighbour=False)
            r2 = Rotor(number=int(cont[7]), offset=int(cont[8]), neighbour=r3, has_neighbour=True)
            r1 = Rotor(number=int(cont[4]), offset=int(cont[5]), neighbour=r2, has_neighbour=True)
            
            plugboard = Plugboard(is_military=bool(cont[1]))
            dict_raw: list[str] = cont[2].replace(" ", "").replace("'", "").rstrip("}").lstrip("{").split(",")
            dict_clean: dict[str, str] = {e[0]: e[2] for e in dict_raw}
            plugboard.configuration = dict_clean

            self.first_rotor = r1
            self.second_rotor = r2
            self.third_rotor = r3
          
        except Exception as e:
            print("Error loading File:", e)


    def configuration_to_file(self, path: str) -> None:
        c = self.get_config()
        try:
            file = open(path, "w")
            file.write(c)
            file.close()
        except Exception as e:
            print("Error writing File:", e)