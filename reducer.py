import sys

current_word = None
current_count = 0
word = None

# Baca input dari stdin
for line in sys.stdin:
    # Hapus spasi di awal/akhir
    line = line.strip()
    # Pisahkan menjadi kata dan count
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        # Abaikan jika count bukan angka
        continue

    # Jika kata saat ini sama dengan yang sebelumnya
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Emit kata sebelumnya beserta total count
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# Emit kata terakhir beserta total count
if current_word == word:
    print(f"{current_word}\t{current_count}")
