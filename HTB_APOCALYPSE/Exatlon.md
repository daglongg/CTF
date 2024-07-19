## Exatlon:

Tải bài trên hackthebox về. Ta dùng câu lệnh file exatlon_v1 để xác định loại thông tin của  file.

Loại tệp: ELF (Executable and Linkable Format), đây là định dạng tiêu chuẩn cho các tệp thực thi và thư viện trên hệ điều hành UNIX và UNIX-like.

Kiến trúc: 64-bit (ELF 64-bit LSB executable), có nghĩa là tệp này được biên dịch để chạy trên kiến trúc x86-64 (còn được gọi là AMD64 hoặc Intel 64), mà là một phiên bản mở rộng của kiến trúc x86.

Phiên bản: Phiên bản 1 (version 1).

Nền tảng: GNU/Linux, cho biết rằng tệp này được biên dịch để chạy trên hệ điều hành Linux.

Liên kết tĩnh (Statically linked): Đây là một ứng dụng đã liên kết tĩnh, có nghĩa là tất cả các thư viện cần thiết đã được liên kết vào tệp thực thi, do đó không cần phải phụ thuộc vào các thư viện hệ thống khác khi chạy.

![image](https://github.com/daglongg/EHC/assets/138242812/53c4515f-a8ae-4b15-b2af-97ae730e0d7b)

Chạy thử chương trình ta thấy được chương trình yêu cầu nhập mật khẩu. Nếu ta nhập sai thì tiếp tục nhập lại. Tôi xác định đây là 1 vòng lặp vô tận và khi nhập đúng pass sẽ dừng chương trình. Tác giả đã cho ta hint trong chương trình. Chương trình gốc của chúng ta đã được nén bởi **UPX** nhằm che dấu mã nguồn, thông tin gốc. Nhăm làm chậm quá trình Reverse. Dùng câu lệnh **upx -d -o exatlon exatlon_v1** để giải nén.

![image](https://github.com/daglongg/EHC/assets/138242812/c03ec4dc-c54d-44d5-a77f-8ed70be706a9)

Sau khi giải nén ta cho vào Ghidra để đọc chương trình. Ở đây ta có thể thấy được vài điều như sau:

    - Input của chúng ta không hề được mã hóa như tôi đã lầm tưởng mà nó được so sánh với 1 string trong chương trình. Nếu đúng thì chương trình sẽ thông báo là Look_Good còn nếu sai thì thông báo là ;(. Vậy có khả năng cao là Input chính là cái flag chúng ta cần tìm.
    - String trong chương trình sẽ được dịch trái 4 bit trong hàm exatlon để cmp với Input.
    - Nếu ta muốn đảo ngược String ấy ta cần dịch phải 4 bit
    
![image](https://github.com/daglongg/EHC/assets/138242812/a53180e9-6cde-4e30-a967-98323ec9d377)

Dịch sang phải 4 bit ta có Input (flag).


![image](https://github.com/daglongg/EHC/assets/138242812/aa537a0d-b0a9-4359-85b8-5b7432058179)

Thử lại và ta có 

![image](https://github.com/daglongg/EHC/assets/138242812/cf9f307f-cf0b-43af-8da9-eba80528c70a)
