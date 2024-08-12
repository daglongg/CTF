# Rev 2

Sử dụng ExeInfo để xác định các thông tin cơ bản của file

![image](https://github.com/user-attachments/assets/747bd8ae-ff0e-4843-bf53-d126751ee4eb)

Chúng ta thấy ở đây chương trình đã yêu cầu chúng ta nhập 1 đoạn input đầu vào và chương trình sẽ encryp đoạn input đó. Sau đó sẽ so sánh với chuỗi `encryptedFlag`.

![image](https://github.com/user-attachments/assets/a14ecae2-0538-429a-b4bc-072786d69cfd)

Tôi sẽ viết 1 đoạn giải mã bằng python để decryp:
```
encrpFlag = [
    0x4D, 0x47, 0x52, 0x4C, 0x38, 0x83, 0x83, 0x4E, 0x7B, 0x4D, 0x81, 0x7C,
    0x51, 0x7F, 0x7B, 0x80, 0x7F, 0x83, 0x50, 0x7B, 0x50, 0x51, 0x7D, 0x7D,
    0x7F, 0x51, 0x7F, 0x51, 0x4F, 0x82, 0x4D, 0x7F, 0x51, 0x7C, 0x7E, 0x7F,
    0x7A, 0x36
]

# Giải mã
def decrypt_flag(encrypted):
    flag = ""
    for byte in encrypted:
        # Quá trình giải mã: (byte - 20) ^ 0x5F
        decoded_byte = (byte - 20) ^ 0x5F
        flag += chr(decoded_byte)
    return flag

# Giải mã và in ra kết quả
flag = decrypt_flag(encrpFlag)
print("Flag:", flag)

```

`flag{00e8f27b48340c8cb664b4bd1f4b7549}`
