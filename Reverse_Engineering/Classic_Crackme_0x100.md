Sử dụng công cụ exeinfo pe để xem file này file gì

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/83a1a6e3-a5b3-4eec-9761-ba74733b3fc4)

Có vẻ đây là 1 file bình thường. K có dấu hiệu của việc bị nén. Nên tôi sẽ cho vào IDA để phân tích tĩnh

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/f619f2bc-d194-4c49-8a03-961bfc0c9832)

Hmmm. Chương trình sẽ yêu cầu ta nhập mật khẩu, sẽ mật khẩu của ta sẽ được tính toán và kết quả sẽ được so sánh với string ban đầu. Và chúng ta sẽ nc vào server của pico và nếu đúng thì ta sẽ được trả ra 1 cái flag. Vì bài này tôi làm sau giải nên ng ta đã đóng cổng kết nối. Nhưng tôi vẫn sẽ cung cấp cho các bạn đoạn script bằng python.

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/9eab987c-c34f-4f53-a52d-53098d0c6c7d)

Lúc này tôi đã nhập pass và tôi đã có flag







