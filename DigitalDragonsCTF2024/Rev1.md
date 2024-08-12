# Rev1.md

Sử dụng Exeinfo PE để xác định các thông tin cơ bản của file

![image](https://github.com/user-attachments/assets/41352508-7296-4742-87fc-e5048e33cd51)

Sử dụng IDA để dịch ngược chương trình này. Ở đây ta thấy rằng chương trình đơn giản in ra các thông báo...


![image](https://github.com/user-attachments/assets/0ed32191-71de-4882-a48b-8f3bf60f8f90)

Ở đây tác giả khả năng đã giấu flag ở đâu đó trong chương trình. Dùng `Strings` và tôi đã tìm ra flag của bài

![image](https://github.com/user-attachments/assets/d8b1776b-5efb-4843-8ca4-9b028477c5a3)

`flag{833450aafcf1a802422ac2bf6c42a304}`



