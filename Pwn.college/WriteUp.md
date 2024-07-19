# Challenges 
## Level 1: 

### Cách 1: 

Chạy thử file babyrev_level1.0 và nó hiện lên là

![image](https://github.com/daglongg/EHC/assets/138242812/388bd2bd-bb92-4ae1-8191-f32057a4e974)

Ở đây ta có thể thấy nó đăng bắt chúng ta nhập 1 cái gì đó. Mình đã nghĩ nhau nếu nhập thì nó cần phải có 1 hàm để so sánh. 

![image](https://github.com/daglongg/EHC/assets/138242812/571e2dff-17a4-4b3b-acc6-0da744f76265)

Ohhhhh. Sau khi mình nhập vào thì nó chuyển qua thành số. Và mình nhận ra đây là bảng mã ASCII. Đọc ở dưới thì có dòng nó mong muốn mình nhập. Sau khi đổi thì mình đã ra được input là WYAFN. Và ta đã ra tìm ra đc flag ...

![image](https://github.com/daglongg/EHC/assets/138242812/c2773973-3b5a-4bf9-b027-24939a01169f)

### Cách 2: 

Mở ghidra lên và tìm ra cái hàm so sánh ấy

![image](https://github.com/daglongg/EHC/assets/138242812/0b1b58eb-3566-40fd-93ca-11edbdb6b693)

Sau đó mình đã tìm đã String 

![image](https://github.com/daglongg/EHC/assets/138242812/f2321b3b-b8d2-4b01-a4ed-58293f3bfc72)

Và ta tìm ra được Input
Sau đó nhập vào là ra flag **pwn.college{MhqbLGcAid8_XTVURWssRLeru2y.0VM1IDL5ATN3QzW}**

## Level 1.1: 

Chạy thử babyrev_level1.1 và nó hiện lên là

![image](https://github.com/daglongg/EHC/assets/138242812/0673055e-f454-4586-8c9a-ea707cb73fd3)

Khi mình lên nhập bừa 1 cái thì nó hiện ra là không đúng.

Mình vẫn đoán là nó dùng 1 hàm để so sánh

Sau đó mình tìm ra được cái hàm so sánh

![image](https://github.com/daglongg/EHC/assets/138242812/5dbcc500-4cea-415a-a967-14a2fa74c5e5)

Và cái đó là 

![image](https://github.com/daglongg/EHC/assets/138242812/5d1e1b52-d329-47a1-b1aa-b9ca36e91b83)

![image](https://github.com/daglongg/EHC/assets/138242812/a9b4cee5-f050-4fa0-b14b-ff18c5aec6c8)

Sau đó mình nhập vào và tìm ra flag **pwn.college{ceOn_wGu44loJAp0UNmuPn9U9wq.0lM1IDL5ATN3QzW}**

## Level 2:

Cho vào Ghira để tìm được kết quả và khi nhập lại ta thấy index 0 và 1 phải swap cho nhau

Sau khi swap ta được flag

![Screenshot 2024-02-20 104241](https://github.com/daglongg/EHC/assets/138242812/cf91ebcc-b410-443f-ab58-ea7f365880cd)

## level 2.1:

Ở đây ta thấy hàm 

![Screenshot 2024-02-20 122605](https://github.com/daglongg/EHC/assets/138242812/9ea8d47f-7b7c-4729-9dfb-5a893ab5d4c4)

Vậy là nó swap index 0 và 3 cho nhau. 

Sau khi swap ta được flag

![Screenshot 2024-02-20 233943](https://github.com/daglongg/EHC/assets/138242812/3faa31f9-094f-463b-9181-b82d63c85ecf)

## Level 3.0:

Ở đây ta làm tương tự như các phân trên nhưng có 1 điều đặc biệt là input ta nhập vào đã được đỏi lại từ phải qua trái

![Screenshot 2024-02-20 235247](https://github.com/daglongg/EHC/assets/138242812/0340e08c-619a-4e5a-9bbe-1fe403eab680)

Vậy ta chỉ cần nhập từ phải qua trái là ra flag

![Screenshot 2024-02-20 235401](https://github.com/daglongg/EHC/assets/138242812/61f13949-d2f9-46d8-90bb-f6251d38b79a)

## Level 3.1:

Ở đây ta làm tương tự như các phân trên và ta thấy có 1 hàm nó đổi giá trị đầu và cuối và cứ thế đổi

![Screenshot 2024-02-21 003730](https://github.com/daglongg/EHC/assets/138242812/898ab259-84a2-475c-b569-b617d7c11bb3)

Ta có thể code lại hàm này cho nhanh nhưng mình đã làm ra luôn tại nó dễ

![Screenshot 2024-02-21 003908](https://github.com/daglongg/EHC/assets/138242812/2adc8d8b-736b-477c-9650-d9229c0c65df)

## Level 4.0:

Ở bài này mình lấy được result và mình thử thì wow :>

Ra luôn flag :>

![Screenshot 2024-02-21 004452](https://github.com/daglongg/EHC/assets/138242812/03c72adc-a346-4cf3-bc79-a357d7ab5d82)

## Level 4.1:

Mình cũng làm tương tự vài 4.0. Mình đọc code thì thấy nó sắp xếp theo bảng chữ cái mà cái result nó đã sắp xếp rồi nên ra luôn flag

![Screenshot 2024-02-21 230208](https://github.com/daglongg/EHC/assets/138242812/280d0509-64d1-4bcf-9a0c-f229461a6c5f)

## Level 5.0:

Sau khi decompile ra ta thấy được bài này sẽ xor với 7

Mình đã viết 1 đoạn code để thực thi hộ mình

![image](https://github.com/daglongg/EHC/assets/138242812/7b468df8-092f-4ec4-9264-f88714a24f5a)

Và mình ra được flag

![Screenshot 2024-02-22 011120](https://github.com/daglongg/EHC/assets/138242812/94dd8f20-37ef-411f-a8c6-5ac6eb2fe2fa)

## Level 5.1:

Bài này mình làm tương tự bài trên 
 
![Screenshot 2024-02-22 012530](https://github.com/daglongg/EHC/assets/138242812/9dfa0d3d-8313-4f6e-9036-82ec1cd2cb1f)

và mình ra được lag 

![Screenshot 2024-02-22 012628](https://github.com/daglongg/EHC/assets/138242812/79685b10-7d08-439d-bb5f-480f2efda9ba)

## Level 6.0:

Với bài này có tổng cộng 18 kí tự và kí tự thứ 3 đổi chỗ cho kí tự thứ 16 và kí tự 9 đổi chỗ cho 17. 

![image](https://github.com/daglongg/EHC/assets/138242812/97711aa3-f450-4ccb-8f5d-084fe58754b7)


MÌnh đã code lại và thực thi và đổi số thì mình ra được flag

![Screenshot 2024-02-22 133123](https://github.com/daglongg/EHC/assets/138242812/37c682e0-f582-4fb0-845b-2ac202baaffe)

## level 6.1:

Cho vào ghidra nhập result và thế là ta cố flag

![image](https://github.com/daglongg/EHC/assets/138242812/9c6b149c-e8c1-43cc-bba7-4ab882bb0c05)

## Level 7.0:

Ở bài này sau khi mình cho file vào Ghidra để Decompile. Chúng ta thấy khi ta nhập input thì chương trình sẽ hiển thị một số nguyên dạng thập lục phân bằng câu lệnh **%02x** với ít nhất 2 chữ số,  và sử dụng ký tự '0' để điền vào các vị trí trống nếu cần thiết.

Các câu lệnh tiếp theo với chức năng là đảo ngược chuỗi, XOR, Swap, Sort, Swap, và hiển thị result sau kkhi thực hiện tất cả các công việc ấy.

Điều chúng ta cần làm ở đây là đảo ngược quá trình. Ở đây tôi dùng DEV C++.

![image](https://github.com/daglongg/EHC/assets/138242812/5cfcef44-e17c-4460-8712-55a7db4b914c)

Và tôi đã có đoạn mã lúc đầu là **PvSu\zEeMhOntQwTrUeLlKoOg**

Nhập vào và ra flag 
![image](https://github.com/daglongg/EHC/assets/138242812/7e4b5fbd-dff3-441a-a478-d697e2c76a7f)

## Level 7.1:

Ở đây ta làm tương tự các phần trước. Ta có thể thấy được các đoạn code này đang thực hiện XOR, Sort, và XOR

![image](https://github.com/daglongg/EHC/assets/138242812/957b0f83-b5e0-4322-9f39-f1d904d1cd10)

![image](https://github.com/daglongg/EHC/assets/138242812/6c8a0a5c-cf97-4cff-905d-671fcaeaee79)

Sau khi code lại đoạn code và chạy ta được input ban đầu

![image](https://github.com/daglongg/EHC/assets/138242812/07bc7701-f4b4-4aea-818a-9b991e9c5aed)

và ta có input **aaagfeedkjjhhhhnmrpwvuzyxx**. Khi ta nhập vào và ra flag

![image](https://github.com/daglongg/EHC/assets/138242812/be3a8f99-ce81-47c6-b8e6-02754946d6ea)






## Level 8.0:

Cùng ý tưởng với bài 7.0. Tôi đã viết lại các câu lệnh vào cho kết quả vào để ra input
![image](https://github.com/daglongg/EHC/assets/138242812/589bbdcd-231c-4669-8956-6d046fa38940)
![image](https://github.com/daglongg/EHC/assets/138242812/0f902ef5-2d47-483b-b497-6a1f09846fdc)

và tôi đã có được input **mggesejlvrqtyxvyvgntvdfsfdonjttqzbd**
![image](https://github.com/daglongg/EHC/assets/138242812/6d385a89-f9fe-4636-9854-3ec79e615a02)

## Level 8.1:
 Ở đây tôi đã được em Vũ Nam và em Hoàng Quý Khánh và em Trí và em Vũ Anh chỉ cho hint là thay đổi type của mảng sau đó tôi đã code lại và chạy ra input

 ![image](https://github.com/daglongg/EHC/assets/138242812/1930ce85-cfcd-4738-a42c-1ef79ac28814)

![image](https://github.com/daglongg/EHC/assets/138242812/83ebbff4-b378-4529-995e-3857b32ea09e)

Tôi đã có input là **vwwwtsspzzxxyyyyffggdeecannoolllmmmkh**
và tôi đã có flag là
![image](https://github.com/daglongg/EHC/assets/138242812/c794e842-4fa8-4933-8ede-8bcca4853066)

## Level 9.0

Ở đây ta có thấy được nó đang đổi byte và sử dụng MD5. Tiếc là MD5 sau khi băm sẽ không đảo ngược được. Vậy chỉ còn đổi byte. Ý tường là đổi byte mà khi mình nhập sai thì nó sẽ trả về flag cho mình. Và tôi sẽ đổi hàm so sánh

Ở đây là offset vậy nên ta cần tìm đia chỉ cần đổi và địa chỉ base. Sau khi tìm ra cả 2 thì ta tiến hành lấy địa chỉ cần đổi trừ đi  địa chỉ base.

Địa chỉ cần đổi ở đây là ![image](https://github.com/daglongg/EHC/assets/138242812/b3df69aa-8827-4594-bf15-5ca02dc9af02)
Còn địa chỉ base là ![image](https://github.com/daglongg/EHC/assets/138242812/a8c6ce23-2451-44b4-9e91-e9cef344221e)
Sau đó trừ đi ta có offset là 225B.
Vậy ta cần đổi gì?
Ta cần đổi giá trị so sánh từ 75 về 74. Tại sao vậy thì mn có thể tra byte của jnz và jz.
Sau đó nhập vào là ra flag 
![image](https://github.com/daglongg/EHC/assets/138242812/1bb374c7-66a5-410b-810e-bf7dfb8b6be7)


## level 9.1
Làm tương tự câu 9.0. 

![image](https://github.com/daglongg/EHC/assets/138242812/2d1e2d83-b131-4755-80fa-2cb21cf358f6)

 và ta ra flag


## Level 10.0:

Solutionn vẫn giống ở bài 9.0. 

![image](https://github.com/daglongg/EHC/assets/138242812/bd890413-09d9-4e3a-ae8c-db02dbd9cf3f)

và ta ra flag

## Level 10.1:

Vẫn cái solution ấy 

![image](https://github.com/daglongg/EHC/assets/138242812/76f599b7-4472-4c9a-9252-80bc9e725158)
