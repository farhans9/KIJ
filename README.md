Dalam menerapkan algoritma caesar cipher dibutuhkan proses enkripsi dan dekripsi. Proses enkripsi dilakukan sebelum data disimpan kedalam database. Untuk menerapkan algoritma caesar cipher digunakan persamaan . C = C mod 26  dimana C adalah nilai pergeseran karakter, dalam penelitian ini digunakan pergeseran 3 sehingga nilai awal C adalah 3. Selanjutnya dilakukan proses enkripsi dengan melakukan konversi setiap karakter ke kode ASCII. Perintah ord digunakan untuk mengambil nilai ASCII dari karakter, perintah chr digunakan untuk mengubah kode ASCII ke karakter. Untuk memudahkan perhitungan nilai ASCII maka setiap karakter akan diubah menjadi huruf besar atau uppercase. Kemudian dilakukan perulangan hingga seluruh karakter dikonversi. Seluruh proses tersebut dapat dilihat pada Gambar 1.  
Proses dekripsi terhadap data dilakukan pada saat pembacaan hasil voting oleh sistem. Alur proses dekripsi memiliki kesamaan dengan proses enkripsi yang membedakan adalah pada proses dekripsi dilakukan pengurangan nilai C. 


![alt text](https://github.com/farhans9/KIJ/assets/149062286/3d4eebbc-760c-43ed-b297-3e5e230df62f?raw=true)



Proses enkripsi dilakukan sebelum data disimpan kedalam database. Salah satu contoh hasil penerapan proses enkripsi pada Gambar 1 dapat dilihat pada Gambar 2. 


![Screenshot (440)](https://github.com/farhans9/KIJ/assets/149062286/fab0823b-ead1-481d-a7c1-8483388063c6)

Hasil enkripsi data mahasiswa pada Gambar 2 merupakan data yang tersimpan dalam database. Proses dekripsi dilakukan pada saat sistem membaca data mahasiswa melalui sistem. Penerapan proses dekripsi pada diperlihatkan pada Gambar 3. 

![Screenshot (442)](https://github.com/farhans9/KIJ/assets/149062286/ad2d919e-4b79-4b52-ac92-2d5a271aed74)

Pada Gambar 3 diperlihatkan data mahasiswa yang dapat dilihat melalui sistem. Sedangkan pada Gambar 2 diperlihatkan data mahasiswa yang berada dalam database yang telah terenkripsi. Salah satu contoh proses enkripsi nama mahasiswa PERMANA menjadi SHUPDQD dengan menerapkan algoritma caesar cipher pergeseran 3. 
