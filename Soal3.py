def ambil_kata_unik(file_path):
    try:
        with open(file_path, 'r') as file:
            artikel = file.read()

        artikel = artikel.lower()
        for char in artikel:
            if char in ",.!?;":
                artikel = artikel.replace(char, " ")

        kata_kata = artikel.split()

        kata_unik = set(kata_kata)

        print("Kata-kata unik dalam artikel:")
        for kata in kata_unik:
            print(kata)

    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan file path yang dimasukkan benar.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

file_path = input("Masukkan path file teks: ")
ambil_kata_unik(file_path)
