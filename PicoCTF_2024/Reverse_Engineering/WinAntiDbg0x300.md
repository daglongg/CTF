Trước hết tôi vẫn sẽ dùng tool `Exeinfo Pe` để check xem các thông tin cơ bản của file. File này đã được nén lại (UPX). Tác dụng của UPX thì như tôi đã để cập trước đó là dùng để ẩn đi chương trình gốc

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/481971cd-8420-4a17-b671-e006d47d1646)

 Đây là chương trình lúc chưa được UPX, 1 chương trình mà chỉ có 1 funtion duy nhất, đây cũng là dấu hiệu cho thấy chương trình đã được nén, hay được can thiệp

 ![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/84dc3a2c-0b0f-4a15-a986-e6e9acd00ca2)

 Tôi sẽ dùng câu lệnh `upx -d WinAntiDbg0x300.exe` để giải né UPX. Chương trình sau khi giải nén thì rất rõ ràng. 

 ![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/410e087a-2099-4d37-bb6a-400f6a74a23a)

Tại bài này tác giả đã không gợi ý rõ ràng cho chúng ta biết flag đang nằm ở đâu. Việc chúng ta cần làm là xem từng funtion 1 chức năng là gì và làm như nào. Ở đây ta thấy được funtion `offset StartAddress`. Ở đây tác giả đã khéo léo khi giấu flag ở đây. 
![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/7aea0a8a-b28b-44c4-9277-bfa5b64b3f1d)

Vượt qua mọi thứ và ta có flag



