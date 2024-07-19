Trước khi bắt đầu thì tôi sẽ dùng tool `Exeinfo PE` để có thể biết được các thông tin cơ bản của file.

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/17c4bf60-2047-4e4f-92f6-d51c2bd6d896)

Tôi sẽ cho vào IDA để phân tích động nó. Ở đây tác giả đã chia ra làm 2 level, ở đây ta có thể thấy rất nhiều các hàm antidbg như
`OutputDebugStringW` và `IsDebuggerPresent`. 2 hàm này tôi đã đề cập trong phần trước.

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/7213883b-b993-4f85-b6d9-02d8d14b4afd)

Điều cần làm là chúng ta sẽ vượt qua các hàm này và tôi có flag là `picoCTF{0x200_debug_f0r_Win_ce2f78e8}`

