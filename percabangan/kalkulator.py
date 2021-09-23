"""
Membuat kalkulator sederhana dengan 2 inputan operand dan 1 operator
yang sudah disiapkan diantaranya (+, -, *, /) dengan memanfaatkan 
fungsi input() bawaan python
"""

nilai1 = int(input("Masukan Nilai :  "))
operator = input("Masukan Operator (-, +, *, /):  ")
nilai2 = int(input("Masukan Nilai :  "))

if (operator not in ["-", "+", "*", "/"]):
    print("Operator yang dimasukan tidak terdaftar")

else:
    if (operator == "+"):
        hasil = nilai1 + nilai2
    
    elif (operator == "-"):
        hasil = nilai1 - nilai2
    
    elif (operator == "*"):
        hasil = nilai1 * nilai2
    
    else:
        hasil = nilai1 / nilai2
    
    print("Hasil %d %s %d : %d" % (nilai1, operator, nilai2, hasil))
