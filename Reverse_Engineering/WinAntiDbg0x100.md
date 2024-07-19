Với bài này thì ngay từ cái tên tác giả đã gợi ý cho chúng ta biết được rằng tác giả sẽ sử dụng antidebug. Vậy antidebug là gì ?

"Antidbg" là một khái niệm trong lĩnh vực phân tích động của phần mềm và kỹ thuật phòng thủ chống lại việc phát hiện và phân tích bởi các công cụ gỡ lỗi (debugging tools) như gdb, lldb, hay WinDbg. Các kỹ thuật antidbg thường được sử dụng trong phần mềm độc hại (malware) hoặc các ứng dụng yêu cầu bảo mật cao để gây khó khăn hoặc ngăn chặn quá trình phân tích, phát hiện và ngăn chặn bởi các công cụ gỡ lỗi.

Trước khi phân tích mình sẽ dùng tool `Exeinfo PE` để xem nó là file gì. Đây là file 32 bit, tôi sẽ phân tích tĩnh nó với IDA

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/eba45589-57e3-4379-96c0-a9868cb36e28)

Đây là file 32 bit, tôi sẽ phân tích tĩnh nó với IDA. Nhìn qua đây tôi có thể nhìn thấy funtion `OutputDebugStringW`. Hàm này có trách nhiệm ghi lại thông tin quan trọng, cảnh báo hoặc dữ liệu debug trong quá trình chạy của ứng dụng. Khi được gọi, nội dung của chuỗi được truyền vào hàm sẽ được gửi đến bảng điều khiển gỡ lỗi. 
Và `IsDebuggerPresent` là một hàm API trong Windows API được sử dụng để kiểm tra xem một ứng dụng đang chạy có đang được gỡ lỗi hay không. Hàm này trả về TRUE nếu ứng dụng đang chạy dưới chế độ gỡ lỗi và FALSE nếu không.

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/723d54f9-a2b6-462e-9bed-08f9f1ff9fd1)

Chúng ta nhìn xuống thì thấy tác giả đã chú thích rõ flag nằm ở đâu. Việc của chúng ta chỉ cần vượt qua các hàm debug. Và ta có flag là `picoCTF{d3bug_f0r_th3_Win_0x100_17712291}`

