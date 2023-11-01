Dalam menerapkan algoritma caesar cipher dibutuhkan proses enkripsi dan dekripsi. Proses enkripsi dilakukan sebelum data disimpan kedalam database. Untuk menerapkan algoritma caesar cipher digunakan persamaan . C = C mod 26  dimana C adalah nilai pergeseran karakter, dalam penelitian ini digunakan pergeseran 3 sehingga nilai awal C adalah 3. Selanjutnya dilakukan proses enkripsi dengan melakukan konversi setiap karakter ke kode ASCII. Perintah ord digunakan untuk mengambil nilai ASCII dari karakter, perintah chr digunakan untuk mengubah kode ASCII ke karakter. Untuk memudahkan perhitungan nilai ASCII maka setiap karakter akan diubah menjadi huruf besar atau uppercase. Kemudian dilakukan perulangan hingga seluruh karakter dikonversi. Seluruh proses tersebut dapat dilihat pada Gambar 1.  
Proses dekripsi terhadap data dilakukan pada saat pembacaan hasil voting oleh sistem. Alur proses dekripsi memiliki kesamaan dengan proses enkripsi yang membedakan adalah pada proses dekripsi dilakukan pengurangan nilai C. 


![alt text](https://github.com/farhans9/KIJ/assets/149062286/3d4eebbc-760c-43ed-b297-3e5e230df62f?raw=true)



Proses enkripsi dilakukan sebelum data disimpan kedalam database. Salah satu contoh hasil penerapan proses enkripsi pada Gambar 1 dapat dilihat pada Gambar 2. 


![Screenshot (440)](https://github.com/farhans9/KIJ/assets/149062286/fab0823b-ead1-481d-a7c1-8483388063c6)
