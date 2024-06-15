conversion_table = [
    ("M",1000),
    ("CM",900),
    ("D",500),
    ("CD",400),
    ("C",100),
    ("XC",90),
    ("L",50),
    ("XL",40),
    ("X",10),
    ("IX",9),
    ("V",5),
    ("IV",4),
    ("I",1)
]

def to_roman(n):
    final_string = ""
    for i in conversion_table:
        final_string += i[0]*(n//i[1])
        n -= n//i[1]*i[1]
    return final_string

def from_roman(string):
    final_number = 0
    for i in string:
        #TO BE IMPLEMENTED
        pass
    return final_number

print(from_roman('MCMLXXXIV'))