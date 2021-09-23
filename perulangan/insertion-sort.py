"""
INSERTION SORT
Algoritma insertion sort pada dasarnya memilah data yang akan diurutkan menjadi dua bagian,
yang belum diurutkan dan yang sudah diurutkan. Elemen pertama diambil dari bagian array yang
belum diurutkan dan kemudian diletakkan sesuai posisinya pada bagian lain dari array yang telah 
diurutkan. Langkah ini dilakukan secara berulang hingga tidak ada lagi elemen yang tersisa pada 
bagian array yang belum diurutkan.
"""

element = [1, 9, 8, 4, 7, 5, 6, 2, 3]

for n in range(len(element) - 1):
    while (n >= 0):
        if (element[n] > element[n+1]):
            tmp = element[n]
            element[n] = element[n+1]
            element[n+1] = tmp
        n -= 1

print(element)

# Cara gampangnya
element = [1, 9, 8, 4, 7, 5, 6, 2, 3]
print(sorted(element))

# Buatlah proses untuk memballik pengurutan dimana nilai
# sebelah kiri ke kenan dari yang terbesar ke terkecil.?