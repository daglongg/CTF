Sử dụng Exeinfo để xác định thông tin cơ bản của file

![image](https://github.com/user-attachments/assets/f98c064d-51e2-4fd8-9be0-004ea563ed4a)

Ở đây ta dễ dàng nhận ra rằng chương trình yêu cầu ta nhập vào 1 đoạn `Input Name` và 1 đoạn `Input Serial`. Chương trình sẽ mã hóa cái `Name` và so sánh với `Serial`. Tác giả đã cho ta sẵn 1 file chứa `Serial` và yêu cầu ta tìm Name

![image](https://github.com/user-attachments/assets/3ff6ac0d-5de2-4163-96d5-91f849642c9d)

Ở đây khi tôi debug thì tôi phát hiện ra rằng giá trị `v8[v3++]` nó sẽ chỉ nằm trong khoảng từ 0x10 tới 0x30 và sẽ lặp lại.

```
def xor_decrypt(hex_str, xor_values):
    # Chuyển đổi chuỗi hex thành byte
    data = bytes.fromhex(hex_str)
    
    # Tạo buffer cho kết quả
    result = bytearray()
    
    # Lặp qua dữ liệu và thực hiện phép XOR
    xor_index = 0
    for byte in data:
        # XOR với giá trị tương ứng từ xor_values
        xor_value = xor_values[xor_index]
        result.append(byte ^ xor_value)
        
        # Cập nhật chỉ số xor_value, lặp lại khi cần
        xor_index = (xor_index + 1) % len(xor_values)
    
    return result


hex_str = "5B134977135E7D13"

# Các giá trị XOR lặp lại (10, 20, 30)
xor_values = [0x10, 0x20, 0x30]

# Giải mã
decoded_bytes = xor_decrypt(hex_str, xor_values)

# Chuyển đổi kết quả thành chuỗi ASCII
decoded_str = decoded_bytes.decode('ascii', errors='ignore')

print("Decoded bytes:", decoded_bytes)
print("Decoded string:", decoded_str)
```
Và ta có flag là `K3yg3nm3`
