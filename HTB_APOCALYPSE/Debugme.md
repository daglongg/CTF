# Debugme:


Trước khi làm gì với file này tôi phải xem nó là file gì đã
![image](https://github.com/daglongg/EHC/assets/138242812/c81f0387-df3d-41c6-a592-921b6876e829)

Ở đây có 1 số thông tin cơ bản của file. Tôi sẽ phân tích động file này xem nó làm gì. Cho vào IDA và tôi thấy có vẻ họ sử dụng TLScallback (Đây là 1 hàm nếu phát hiện ta debug động thì nó có thể thực hiện các biện pháp như chấm dứt hoặc thay đổi hành vi của chương trình).

![image](https://github.com/daglongg/EHC/assets/138242812/6ebabd58-34eb-4ee7-98bd-abc4da1d48a6)

Trước khi làm gì tôi sẽ phân tích tĩnh hàm main để biết sơ sơ chương trình này làm gì. Ta thấy có 1 đoạn ở dòng 24 nếu chúng làm gì đó thì main có thể đc xor với 5Ch đây là **Self-modifying code**. Đây là cách antidebug bằng cách thay đổi mã máy liên tục.
![image](https://github.com/daglongg/EHC/assets/138242812/24e8764a-5d10-42e7-b075-1a004db45c80).

Tôi sẽ  bắt đầu debug động nó. Ở đây ta thấy được 1 câu lệnh lạ đó là **mov eax, fs:[0x30]**. Đây là 1 cái antidebug nữa và nó có tên gọi là PEB. Bằng cách di chuyển giá trị của PEB vào thanh ghi eax, chương trình có thể kiểm tra và thay đổi các cờ gỡ lỗi, từ đó gây khó khăn hoặc ngăn chặn việc gỡ lỗi từ các công cụ ngoại vi. Tôi đặt 1 breakpint ở hàm so sánh để xem nó sẽ rẽ nhánh đi đâu và có vẻ nó break chương trình. Tôi sẽ điều chỉnh cờ cho đi đúng hướng
![image](https://github.com/daglongg/EHC/assets/138242812/201a8d77-6403-4423-8cdb-e824044ca761)


Tại đây tôi sẽ chạy qua hàm xor 5CH và có vẻ main đã xor với 5CH. Có vẻ khi so với 5CH thì chương trình đã trở về chương trình gốc. Tôi đã kiểm tra 2 funtion **security_init_cookie** nó đang tính thời gian và nếu lâu quá có thể chương trình có thể dừng. Tôi sẽ vào hàm **___tmainCRTStartup** ở đây tôi thấy được 2 chỗ antidebug mà tôi đã đề cập. Tôi sẽ điều hướng qua nó. Ở cuối hàm này có 2 hàm main. Ở hàm main đầu tiên thì không có gì đặc biệt. Cho tới hàm số 2

![image](https://github.com/daglongg/EHC/assets/138242812/e7491b69-83e5-4155-8f5e-d67a539b134d)

![image](https://github.com/daglongg/EHC/assets/138242812/e9201e4b-01e8-4403-8381-0d11e6e2ea3f)

Các chức năng ở đây làm tôi nhớ tới chương trình đầu tiên. Vượt qua các hàm sau break bằng cách đổi cờ tôi đã tới được hàm cuối. 

![image](https://github.com/daglongg/EHC/assets/138242812/c70ab6ba-be02-4ad6-9bb1-48bc7b20f78a)
![image](https://github.com/daglongg/EHC/assets/138242812/c4b11b08-3704-42fc-a3bd-1db4305ed258)
Tôi đã nghĩ là tôi đã gần chạm tới nó. Nhưng vẫn k ra, tôi cứ nghĩ tôi đi sai hướng nhưng sau khi hỏi hint em Khánh thì tôi được biết là flag sẽ nằm ở Hex View. và tôi đã lặp lại 21 lần và tôi đã tìm ra iem. 
![image](https://github.com/daglongg/EHC/assets/138242812/0ec19c93-0cd2-48e9-879e-0d22996552f6)
