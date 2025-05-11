def hitung_rata_rata():
    angka = []

    while True:
        masukan = input("Masukkan bilangan (atau ketik 'done' untuk selesai): ")

        if masukan.lower() == "done":
            break
        try:
            bilangan = float(masukan)
            angka.append(bilangan)
        except ValueError:
            print("Input tidak valid. Masukkan angka atau 'done'.")

    if angka:
        rata_rata = sum(angka) / len(angka)
        print(f"Rata-rata dari bilangan yang dimasukkan adalah: {rata_rata}")
    else:
        print("Tidak ada bilangan yang dimasukkan.")

hitung_rata_rata()
