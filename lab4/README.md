Bài 1:

Đọc ảnh "fruit.jpg" và chuyển sang dạng ảnh xám (mode='L').

Kết quả là một mảng NumPy 2 chiều với giá trị độ sáng từ 0–255.

Sử dụng scipy.ndimage.shift để dịch ảnh theo trục X và Y:

shift=(0, 30) nghĩa là:

0 pixel theo trục Y (chiều dọc)

30 pixel theo trục X (chiều ngang)

Các pixel bị đẩy ra ngoài sẽ được làm trống bằng giá trị mặc định 0

Bài 2:

Cắt chính xác từng vùng ảnh bằng slicing img[y1:y2, x1:x2]

[:, :, ::-1] đảo thứ tự màu biến RGB thành BGR

Kết quả là màu sắc của vùng ảnh bị thay đổi

Đu đủ được gán lại vào vị trí cũ

Dưa hấu được gán vào vị trí mới hơn

Bài 3:

mountain và boat là vùng ảnh lấy theo tọa độ (y1:y2, x1:x2)

Mỗi vùng có kích thước 100x150 pixel

Hàm nd.rotate thực hiện xoay vùng ảnh 45 độ

reshape=True giúp mở rộng khung ảnh để không bị cắt mất góc

Bài 4:

Cắt vùng có chiều cao 100 pixels và chiều rộng 100 pixels từ vị trí (y=100:200, x=150:250) đây là vùng cần phóng to

Hàm nd.zoom dùng để nội suy đa chiều

(5, 5, 1) là hệ số phóng đại theo từng chiều:

5 lần theo chiều cao

5 lần theo chiều rộng

1 giữ nguyên số kênh màu RGB

Bài 5: 

tinhtien(list)

Dịch chuyển ảnh theo trục hoành 30 pixels

shift=(0, 30) nghĩa là không theo chiều dọc, chỉ dịch 30 pixel sang phải

Ảnh kết quả bị lệch phải, phần bên trái được điền mặc định màu đen

xoay(list)

Xoay ảnh một góc 20° theo chiều ngược kim đồng hồ

reshape=False giúp giữ nguyên kích thước ảnh gốc

Các pixel ở góc có thể bị cắt nếu nằm ngoài khung gốc

phongTo(list)

Phóng to ảnh gấp 2 lần

thuNho(list)

Thu nhỏ ảnh xuống 10% kích thước ban đầu

cooridnate_map(list)

Chèn lưới tọa độ lên ảnh RGB

Các dòng và cột xen kẽ được tô màu đen [0,0,0], chia ảnh thành ô vuông 100x100 pixel

random_transform()

Tự động chọn ngẫu nhiên 1 phép biến đổi trong danh sách:

"T": tinhtien

"X": xoay

"P": phongTo

"H": thuNho

"C": cooridnate_map

Biến list_of_images chứa các đường dẫn đến ảnh
