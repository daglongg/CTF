Tải file `wget https://artifacts.picoctf.net/c_rhea/10/challenge.zip` và mình câu lệnh tree để xem file ấy như nào.

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/17ac14a4-1766-49d7-b5ea-325a12a61a37) 

Dạo qua 1 lượt các file nào các file ấy có gì. Trong file `decrypt.sh` ta thấy nó đang được thiết kế để giải mã các tệp tin bằng cách sử dụng mã hóa AES-256-CBC với phương pháp bảo mật PBKDF2 và việc sử dụng hàm băm với 100,000 vòng lặp. Còn file `checksum.txt` thì nó đang lưu trữ 1 đoạn mã SHA256. CÒn `files` là thư mục và bên trong nó sẽ lưu trữ các file. Tôi nghĩ tôi sẽ mã hóa các file trong file `files` để so sánh với file `checksum.txt`. Cái nào đúng thì tôi sẽ cho chạy nó với file `decrypt.sh`

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/13769fc3-a151-4247-a494-26d9a9571aa0)

Và tôi có flag là `picoCTF{trust_but_verify_c6c8b911}`
