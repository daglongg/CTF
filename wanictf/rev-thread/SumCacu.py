#!/usr/bin/env python3

from pwn import *
from z3 import *

# Số lượng ký tự trong flag
FLAG_LENGTH = 45

# Kết quả đầu ra mong muốn
expected_output = [
    0xa8, 0x8a, 0xbf, 0xa5, 0x2fd, 0x59, 0xde, 0x24,
    0x65, 0x10f, 0xde, 0x23, 0x15d, 0x42, 0x2c, 0xde,
    0x09, 0x65, 0xde, 0x51, 0xef, 0x13f, 0x24, 0x53,
    0x15d, 0x48, 0x53, 0xde, 0x09, 0x53, 0x14b, 0x24,
    0x65, 0xde, 0x36, 0x53, 0x15d, 0x12, 0x4a, 0x124,
    0x3f, 0x5f, 0x14e, 0xd5, 0x0b
]

# Tạo danh sách các biến ký tự cho đầu vào
input_vars = [BitVec(f"char_{i}", 32) for i in range(FLAG_LENGTH)]

# Tạo solver Z3
solver = Solver()

# Thêm các ràng buộc vào solver
for i in range(FLAG_LENGTH):
    char = input_vars[i]
    transformed_char = char
    for op in range(3):
        transformed_char = (transformed_char * 3 if op == 0 else
                            transformed_char + 5 if op == 1 else
                            transformed_char ^ 0x7f)
    solver.add(transformed_char == expected_output[i])

# Kiểm tra và lấy model
if solver.check() == sat:
    model = solver.model()
    flag = ""
    for i in range(FLAG_LENGTH):
        char_value = model[input_vars[i]].as_long()
        # Lấy phần thấp của giá trị nếu giá trị quá lớn để trở thành ký tự ASCII
        flag += chr(char_value & 0xff)
    print(f"Flag: {flag}")

    # Gửi flag đến process
    p = process("./thread")
    p.sendline(flag.encode())
    print(p.readline().decode())
else:
    print("No solution found")
