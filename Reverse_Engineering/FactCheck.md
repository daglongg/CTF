Mình cho cho file này vào exeinfo pe để xem nó là file gì

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/3a3c15e5-76ac-48e6-9a9a-8ed6296d60d8)

Mình sẽ đọc file này với IDA để xem chương trình này hoạt động như nào. Ta thấy được rằng tác giả đã cho 1 nửa của flag và muốn ta hoàn thành nửa con lại.


![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/4b99f7aa-f95b-444b-b382-8a32b6727be9)

Tại dòng 91 đến dòng 109 ta thấy được các câu lệnh if. Nếu đúng với điều kiện thì ta sẽ ra được flag

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/0bd007b0-e0f5-435c-b8eb-d1ac8574c113)

Tôi đã viết 1 đoạn script bằng python để mô phỏng lại cách hoạt động của các câu lệnh if và tôi có flag

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/7501a3dd-55f8-4b5e-90fd-dd41b4df0d1f)


