import sys
import re

# Baca input dari stdin
for line in sys.stdin:
    # Hapus spasi di awal/akhir dan ubah ke lowercase
    line = line.strip().lower()
    # Pisahkan kata berdasarkan non-alphanumeric characters
    words = re.findall(r'\b\w+\b', line)
    # Emit setiap kata dengan nilai 1
    for word in words:
        print(f"{word}\t1")
