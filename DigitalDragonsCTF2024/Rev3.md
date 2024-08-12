# Rev 3

Dùng `Exeinfo` để xác định thông tin cơ bản của file

![image](https://github.com/user-attachments/assets/e4b6a1bb-99f1-4942-82d7-8c0c95b0fa6a)


Ở đây ta thấy rằng chương trình yêu cầu ta nhập đầu vào và sử dụng các phương trình để tính toán các giá trị 

![image](https://github.com/user-attachments/assets/ad90947a-9ca5-4d21-bd59-f4ee32e57ebb)

Ở đây ta sẽ sử dụng z3 để tính, cái quan trọn nhất là các giá trị `v[i]` sẽ nằm trong khoảng nào. Tôi sẽ thử luôn với bảng mã ascii.

```
from z3 import *

solver = Solver()
v = {i: Int(f'v{i}') for i in range(5, 43)}

for i in range(5, 43):
    solver.add(v[i] >= 0x20, v[i] <= 0x7F)

solver.add(v[22] + v[23] + v[5] + v[15] - v[39] == 208)
solver.add(v[12] + v[36] + v[26] - v[27] + v[32] == 197)
solver.add(v[10] + v[16] - v[28] - v[14] + v[6] == 150)
solver.add(v[28] + v[22] + v[24] - v[17] - v[9] == -61)
solver.add(v[27] + v[13] + v[33] - v[28] - v[10] == 139)
solver.add(v[24] + v[39] + v[17] - v[33] + v[42] == 330)
solver.add(v[34] + v[15] + v[26] + v[27] - v[12] == 153)
solver.add(v[21] + v[35] + v[31] - v[8] - v[18] == 91)
solver.add(v[37] + v[17] + v[25] + v[19] + v[15] == 408)
solver.add(v[30] + v[20] - v[33] - v[17] - v[21] == -46)
solver.add(v[13] + v[6] - v[11] - v[8] + v[32] == 154)
solver.add(v[32] + v[8] - v[40] - v[6] - v[34] == -18)
solver.add(v[31] + v[37] + v[7] - v[13] - v[35] == 50)
solver.add(v[34] + v[31] + v[17] - v[13] - v[36] == 58)
solver.add(v[24] + v[18] + v[20] - v[37] + v[32] == 203)
solver.add(v[10] + v[25] - v[42] - v[9] + v[12] == -44)
solver.add(v[24] + v[37] + v[39] - v[19] + v[6] == 259)
solver.add(v[27] + v[42] + v[39] - v[40] - v[13] == 163)
solver.add(v[37] + v[22] + v[19] + v[30] + v[40] == 414)
solver.add(v[15] + v[11] + v[26] + v[10] + v[9] == 327)
solver.add(v[34] + v[30] + v[41] - v[20] - v[27] == 12)
solver.add(v[16] + v[29] - v[40] - v[22] - v[13] == -51)
solver.add(v[13] + v[5] - v[40] - v[41] - v[24] == 38)
solver.add(v[36] + v[32] + v[9] + v[39] - v[7] == 268)
solver.add(v[30] + v[14] - v[23] - v[39] + v[29] == 22)
solver.add(v[8] + v[23] + v[39] - v[25] - v[7] == 150)
solver.add(v[14] + v[24] - v[27] - v[40] + v[22] == 11)
solver.add(v[6] + v[9] - v[34] - v[16] + v[29] == 132)
solver.add(v[5] + v[15] - v[17] - v[10] - v[34] == -54)
solver.add(v[20] + v[18] - v[25] - v[40] - v[13] == -55)
solver.add(v[39] + v[8] - v[42] - v[38] + v[34] == 72)
solver.add(v[20] + v[41] + v[17] - v[18] - v[27] == 106)
solver.add(v[17] + v[39] - v[36] - v[34] - v[26] == 48)
solver.add(v[12] + v[33] - v[13] - v[11] + v[9] == 123)
solver.add(v[42] == ord('}'))

if solver.check() == sat:
    model = solver.model()
    v_values = [model[v[i]].as_long() for i in range(5, 43)]
    print("Values of v5 to v42:", v_values)

    print("Values of v5 to v42:", v_values)
else:
    print("No solution found.")

```

`flag{51ee95ff4fda5a721b89f3a16b0e9a86}`

