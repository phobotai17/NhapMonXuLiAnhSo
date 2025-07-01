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

Bài tập thêm 1:

Ảnh gốc được dịch sang phải 50 pixel, xuống dưới 30 pixel

Một canvas trống (đen) được tạo để chứa ảnh sau khi tịnh tiến

Áp dụng biến dạng hình sin cho trục x để ảnh gợn sóng theo chiều ngang

Hàm sin() giúp tạo hiệu ứng sóng mượt, tự nhiên

Dùng np.mgrid để tạo ma trận chỉ số cho từng pixel

Các tọa độ được biến đổi theo sóng để áp dụng cho từng pixel

map_coordinates nhận lưới tọa độ mới và nội suy lại ảnh tương ứng, lặp cho từng kênh màu (R, G, B).

Kq:

Ảnh kiwi bị gợn sóng nhẹ theo trục ngang và tịnh tiến về phía dưới và bên phải

Bài tập thêm 2:

Ảnh được đưa về chế độ RGBA, cho phép kiểm tra và giữ vùng trong suốt

Tạo một dải giá trị từ 0 đến 1 theo chiều ngang ảnh x

Dùng để tính trọng số tuyến tính cho nội suy giữa 2 màu

Chỉ áp dụng gradient cho những pixel có độ trong suốt alpha > 0

Mỗi kênh màu (R, G, B) được tính bằng cách nội suy tuyến tính từ color1 đến color2 cho hiệu ứng chuyển màu mượt mà từ trái sang phải

canvas là một tấm nền có kênh alpha (RGBA), nên vẫn giữ được vùng trong suốt

Ảnh được ghép kèm mặt nạ chính nó (giữ alpha), nên hiệu ứng trong suốt không bị mất

kq:

Trái đu đủ chuyển màu từ đỏ sang xanh lá

Dưa hấu chuyển màu từ vàng sang tím

Giữ lại vùng trong suốt

Bài tập thêm 3:

Ảnh gốc được chuyển sang NumPy array để xử lý pixel-level

reshape=False: không mở rộng ảnh sau xoay

mode='constant', cval=255: nền trắng

flipud lật ảnh theo trục dọc

Tạo ảnh trắng mới đủ lớn để chứa cả hai ảnh đã xử lý

Dán ảnh vào vị trí, canh chỉnh khoảng cách 25px, 50px

kq:

thay đổi góc xoay, áp dụng mirror theo chiều ngang

Bài tập thêm 4:

(5, 5, 1): tăng chiều cao & rộng gấp 5 lần, giữ nguyên số kênh màu

order=1: dùng nội suy tuyến tính, tránh răng cưa

Tạo hiệu ứng lượn sóng nhẹ bằng sin & cos

warp_factor * dx * r: tạo hiệu ứng uốn cong từ tâm ảnh

Duyệt từng kênh màu (R, G, B) và ánh xạ lại giá trị pixel theo tọa độ mới

mode='reflect': xử lý vùng ảnh ngoài biên bằng phản chiếu

Kq:

Ảnh ngôi chùa sau khi zoom được uốn cong nhẹ
