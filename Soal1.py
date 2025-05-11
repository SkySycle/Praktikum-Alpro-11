def tiga_bilangan_terbaik(data):
    if len(data) < 3:
        raise ValueError("List harus memiliki minimal 3 bilangan.")
    
    data_terurut = sorted(data, reverse=True)
    
    return data_terurut[:3]

angka = [12, 45, 23, 67, 89, 34, 10]
hasil = tiga_bilangan_terbaik(angka)
print("Tiga bilangan terbaik:", hasil)
