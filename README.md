# TBFOPythonCompiler
> Tugas besar IF2124 Teori Bahasa Formal dan Otomata 2021
> by Kelompok 17 K1 (seadanya-sebisanya).

## General Information
Program syntax parsing untuk file python menggunakan algoritma CYK (Cocke–Younger–Kasami) dan Context-free Grammars (CFG) yang telah diubah ke bentuk Chomsky Normal Form (CNF).

## Usage
1. Clone repository ini.
2. Jika ingin mengubah grammar, dapat diubah di `cfg.txt` dan jalankan code di bawah ini untuk memperbaharui `cnf.txt`.
```python
python CFG2CNF.py cfg.txt
```
3. Masukkan file python yang ingin dicek sintaksnya dalam satu directory dengan clone repository dan jalankan salah satu code di bawah ini sesuai input file. Jika program tidak meneriman masukan input file maka akan otomatis mencari file dengan nama "tesInput.py" yang ada pada 1 folder bersama file
```python
python main.py <namainputfile.txt>
python main.py "namainputfile.py"
```

## Future Improvements
* Program belum dapat memberikan lokasi kesalahan sintaks (program dapat mengevaluasi nama variabel yang tidak valid sintaksnya, tetapi tidak dengan sintaks lainnya).
* Pembacaan string program masih belum bisa menangkap banyak isi yang bertabrakan dengan nama terminal di cfg.txt

## Contributors
- [Fransiskus Davin Anwari | 13520025](https://github.com/fdavin)
- [Taufan Fajarama Putrawansyah R | 13520031](https://github.com/roastland)
- [Tri Sulton Adila | 13520033](https://github.com/3sulton)
