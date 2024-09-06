![image](https://github.com/user-attachments/assets/d3478b67-ad31-46a2-9c1b-0f2143cbce96)

Sử dụng exeinfo để biết được các thông tin cơ bản của file này

![image](https://github.com/user-attachments/assets/e3861336-12bd-4150-b2f4-a80c190e591d)

Thử chạy thử và đây là 1 con game rắn với yêu cầu là nếu chơi được 16525 điểm thì bạn sẽ có flag :))

![image](https://github.com/user-attachments/assets/6e02ad93-b0b9-4758-b888-50cdb0049a65)

Thử nghĩ tới crack thì tôi đã dùng IDA nhưng nó khá là rối, sau 1 hồi tìm kiếm thì tôi đã tìm thấy tool là `gameconqueror`. Một tool cho phép tôi biết có thể vị trí của biến và cho phép tôi sửa đổi giá trị của nó.

Cách tải tool: `sudo apt-get install gameconqueror`

Chạy tool và thêm `prosecc` 

![image](https://github.com/user-attachments/assets/a79df655-5c73-42a0-8086-3a24b2d210ac)

Sửa giá trị và ta có flag là: `CSCTF{Y0u_b34T_My_Sl1th3r_G4m3!}`
