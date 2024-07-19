# Rev_boxcutter

Đọc thử file bằng exeinfo để xem nó là file gì.

![image](https://github.com/daglongg/EHC/assets/138242812/d2f18020-f89c-41fd-88e8-5e70ad7d0af2)

Sau đó tôi cho vào ghidra để phân tích tĩnh. Ở đây tôi thấy được 1 string tên local_28 và tôi đã đổi thành result khi thấy nó được xor với 55 để tra được string khác.

![image](https://github.com/daglongg/EHC/assets/138242812/fb9c9294-6c9a-428c-9cf5-0b3c391f6885)

 Có 1 vấn là vòng lặp tới 23 lần trong khi cái result đang không có độ dài cố định. Tôi đã thử retype variable thành char [23] và wowwww

 ![image](https://github.com/daglongg/EHC/assets/138242812/5eb47d08-ec33-4d0b-a6d8-de8e70367bae)

 ở đây có thể giải thích rằng biến result đang không xác định đúng định dạng của nó. Và nếu để như ban đầu thì nó đang sai, sau khi tôi retype thì nó đã trở về ban đầu. Tiếp theo là viết lại và ra được flag.

 ![image](https://github.com/daglongg/EHC/assets/138242812/f2debb56-a1db-4eea-8ab2-8ec80efc9e53)

 # Rev_lootstash

 Đọc thử file bằng exeinfo để xem nó là file gì.

 ![image](https://github.com/daglongg/EHC/assets/138242812/78129089-933a-44fa-ba2d-07db0d2c7b69)

Tôi cho vào IDA để đọc chương trình và ta thấy time trong hàm srand() là để tạo ra một giá trị seed duy nhất cho hàm rand(), giúp tạo ra các số ngẫu nhiên khác nhau mỗi khi chạy chương trình. Nếu không có time, chương trình sẽ sử dụng cùng một seed mỗi khi chạy, và sẽ tạo ra các số ngẫu nhiên giống nhau. Bằng cách sử dụng thời gian hiện tại như một giá trị seed, chúng ta đảm bảo rằng các số ngẫu nhiên được tạo ra sẽ thay đổi theo thời gian, và chúng ta có thể nhận được kết quả ngẫu nhiên khác nhau mỗi khi chạy chương trình.

![image](https://github.com/daglongg/EHC/assets/138242812/17100c3b-c594-42ef-ba11-7b7b1b99ef00)


Phần tử (&gear) sẽ được tham chiếu bằng [(v4 % 2040uLL) >> 3]. Ở đây ta thấy gear sẽ lưu rất nhiều các giá trị. Tôi đoán flag sẽ được lưu ở đó và khi srand là đúng số thì sẽ tham chiếu ra được flag. 

![image](https://github.com/daglongg/EHC/assets/138242812/447a4a12-175d-4e4e-8d81-9f6b025a3f1c)

Check từng cái một và tôi đã có flag. 
![image](https://github.com/daglongg/EHC/assets/138242812/43e211d5-b297-41df-b17c-7297b15058cf)




 

 



