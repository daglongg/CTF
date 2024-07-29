![image](https://github.com/user-attachments/assets/be17e695-d071-4bb6-86a0-a05e09499491)

Bài này ta sẽ nhận được 1 file `its_a_mess.bin`. Kiểm tra file tôi thấy rằng đây là 1 file txt và nội dung trong đó có vẻ là 1 đoạn mã đã được compiler.

![image](https://github.com/user-attachments/assets/e0c5a620-0675-4108-a1ec-178dd31c8887)

Nếu đọc kĩ thì chúng ta thấy rằng các kí tự của đoạn mã này đã được tác giả modify đi. Cụ thể nếu nhìn xuống dòng cuối cùng ta có thể thấy tác giả đã đảo các 2 byte cạnh nhau.

Ví dụ ta có đoạn code minh họa:
* Tôi có đoạn mã là:  `1,2,3,4,5`. Và ta có đoạn code sau khi đảo là `2,1,4,3,5`

![image](https://github.com/user-attachments/assets/64deef7d-b506-4b53-8fd1-da2d8846f9b8)

Ta sẽ modify lại và ta có 1 file ELF

![image](https://github.com/user-attachments/assets/32a9bb78-18a8-4c50-a6df-daf4933f5edd)

Sử dụng IDA và ta thấy rằng file đã được tác giả đóng gói bằng `PyInstaller`. 

![image](https://github.com/user-attachments/assets/8ae9e71d-29ea-46a6-934c-6401b7634a29)

Tại đây tôi sẽ sử dụng `pyinstxtractor` để giải nén tệp thực thi được tạo ra bằng `PyInstaller`. Sau khi giải nén và ta có được 


![image](https://github.com/user-attachments/assets/d6cefcc6-5297-4f63-8f27-e0ad101ebe52)

Tại đây có rất nhiều các file python. Sử dụng web `PyLingual` để decompiled từng file

![image](https://github.com/user-attachments/assets/c0d78e93-fff7-49a1-8db2-87bfbcada3b9)

Và ta có flag là: `FLAG:472092DC7BABB7EA4B0ABC682C7D922DF9E4E0D5958624CCD`
