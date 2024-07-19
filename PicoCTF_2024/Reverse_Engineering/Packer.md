Điều đầu tiên là tôi sẽ xác định file này thật chất là file gì thông qua 1 tool tên là Exeinfo PE

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/0aac5ad4-1363-4c88-9e70-9c0c0b90bcf5)

Ở đây nó đã giúp ta phát hiện ra là file này đã được UPX. Vậy UPX là gì ?
UPX - Untimate Packer for eXecutables: Là một công cụ nén và giải nén các file thực thi máy tính (executable files) trong hệ điều hành. Công dụng chính là giảm dung lương file, che dấu mã nguồn, bảo vệ chống phân tích ngược.
 => Vậy ta suy ra rằng tác giả đã sử dụng UPX để có thể che dấu mã nguồn của hệ thống.
 
Tôi sẽ show cho các bạn để các bạn thấy được sự khác nhau của chúng:

Đây là chương trình khi được UPX, chúng ta có thể nhận ra rằng chương trình này không có main và đang được rút gọn

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/4a1e7843-b9d6-4c4f-b9fb-66fc77cf0315)

Còn đây là chương trình sau khi được giải nén UPX, có đầy đủ main và các hàm khác

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/97366083-7be8-479d-9f82-7ea19b68bbbc)

Đến đây việc chúng ta cần làm là xem chương trình này hoạt động như nào. Ta thấy được ở dòng 23 có 1 string và có vẻ khi chương trình yêu cầu ta nhập từ bàn phím vào thì nó sẽ so sánh với string ấy. Nếu đúng thì nó hiển thị ra string ấy. Còn nếu sai thì sẽ hiện ra là Access denied.

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/512c93c7-ced3-4920-84ef-612d292f3304)

Cho string ấy vào Cipher Identifier để xác định định dạng gốc và ta có flag là : 

![image](https://github.com/daglongg/PicoCTF_2024/assets/138242812/c07bef1b-bf3c-425b-94cb-c5094d7c2c12)



