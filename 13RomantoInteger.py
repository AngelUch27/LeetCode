class Solution:
    def romanToInt(self, s: str) -> int:
        equivalencias = { 
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,         
        }

        numero = 0

        #Remplaza IV por IIII y a la cadena resultante la vuelve a remplazar
        s = s.replace("IV", "IIII").replace("IX","VIIII").replace("XL","XXXX").replace("XC","LXXXX").replace("CD","CCCC").replace("CM","DCCCC")

        for char in s:
            numero += equivalencias[char]

        return numero

