Cho file vào exeinfo pe để xem có điều gì bất thường không. Và ohhhhhhhhh đây là file txt chứ không phải exe. Có thể tác giả đã cố tình cho vào để đánh lạc hướng.

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/214dfbaa-a881-4bce-91e6-435b14b1362a)

Đổi đuôi file thành .txt và mở lên ta sẽ được 1 file có nội dung như này

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/9dd009be-0461-408c-9d9b-9758e8ea32df)

Với sự trợ giúp của chatGPT tôi đã xác định được đây là mã bytecode được disassemble từ một chương trình Python. Sau khi viết lại theo logic của bài ta có flag

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/0b17f1a9-1918-49e1-b18f-a6269ca9e755)

Ở đây ta cần chú ý vài điểm như sau:
1. Phải đọc kĩ đoạn key xem nó đang đúng chưa vì khi key sai thì kết quả sẽ là 1 kết quả rất khác.
2. ChatGPT rất tuyệt nhưng chúng ta cần phải chỉnh lại 1 số thứ chứ k phải lệ thuộc vào nó.






