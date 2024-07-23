from threading import Thread

# Danh sách các giá trị đầu vào
input_values = [
    0xA8, 0x8A, 0xBF, 0x0A5, 0x2FD, 0x59, 0xDE, 0x24,
    0x65, 0x10F, 0xDE, 0x23, 0x15D, 0x42, 0x2C, 0xDE,
    0x09, 0x65, 0xDE, 0x51, 0xEF, 0x13F, 0x24, 0x53,
    0x15D, 0x48, 0x53, 0xDE, 0x09, 0x53, 0x14B, 0x24,
    0x65, 0xDE, 0x36, 0x53, 0x15D, 0x12, 0x4A, 0x124,
    0x3F, 0x5F, 0x14E, 0xD5, 0x0B
]

# Mảng để theo dõi số lần thực hiện phép toán
operation_counts = [3] * 45

def perform_operations(index):
    for _ in range(3):
        operation_counts[index] -= 1
        operation_type = (operation_counts[index] + index) % 3
        if operation_type == 0:
            input_values[index] //= 3
        elif operation_type == 1:
            input_values[index] -= 5
        else:
            input_values[index] ^= 0x7F

# Tạo và khởi động các thread
threads = [Thread(target=perform_operations, args=(i,)) for i in range(45)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# Chuyển đổi các giá trị thành chuỗi và in ra kết quả
decoded_flag = "".join(chr(item) for item in input_values)
print(decoded_flag)
