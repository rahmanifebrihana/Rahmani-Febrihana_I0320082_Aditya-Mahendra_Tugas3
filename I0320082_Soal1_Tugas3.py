# List 10 nama teman
list = ['Divana', 'Candrika', 'Funny', 'Ayu', 'Gea', 'Angela', 'Ara', 'Rafli', 'Issa', 'Hani']

# Menampilkan list indeks nomor 4, 6, dan 7
print("List indeks nomor 4, 6, dan 7 adalah", list[4], ",", list[6], ",", "dan", list[7] )

# Menganti nama teman di list 3, 5, dan 9
list[3] = 'Zaneta'
list[5] = 'Sekar'
list[9] = 'Tazkiya'

# Menambahkan 2 nama teman
list.append('Sasa')
list.append('Stefany')

# Menampilkan perulangan semua nama teman
white = 0
for lilac in range (0,12) :
    print (list[white])
    white+=1

# Menampilkan panjang list
print("Panjang list nama teman yaitu", len(list))
