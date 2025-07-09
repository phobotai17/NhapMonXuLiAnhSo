bài tập 1:

Cắt phần ảnh từ tọa độ (10, 10) đến (350, 480)

Lưu vùng ảnh đã cắt vào file LangBiang.jpg

convert('L'): chuyển ảnh sang ảnh xám 8-bit (0–255)

Biến đổi thành mảng số để tính toán ngưỡng.

Tự động tìm ngưỡng tách nền và đối tượng (Otsu) để rồi nhân với 0.3 để hạ thấp ngưỡng làm cho ảnh sáng hơn sẽ bị chuyển thành đen

Tạo ảnh nhị phân bằng cách so sánh từng pixel với ngưỡng

Sau đó Chuyển mảng Boolean thành ảnh để hiển thị và lưu

KQ:

Ảnh nhị phân sau xử lý sẽ có vùng màu trắng hiện các chi tiết sáng hơn ngưỡng.

Do giảm ngưỡng Otsu xuống còn 30% nên ảnh dễ bị chuyển thành trắng hơn, giúp nổi bật các chi tiết đậm hoặc bóng đổ.

Bài tập 2:

mode='L': đọc ảnh ở dạng grayscale (1 kênh độ sáng)

Cắt ảnh từ tọa độ (y: 10, 680, x: 500, 1000)

Xoay ảnh 45 độ nhưng không thay đổi kích thước gốc (reshape=False).

Các vùng ngoài ảnh sẽ được điền mặc định bằng màu đen.

threshold_local(a, offset=60) chia ảnh thành nhiều ô nhỏ, sau đó xác định ngưỡng riêng cho từng ô.

offset=60: giảm ngưỡng cục bộ xuống 60 đơn vị giúp làm nổi bật các chi tiết tối.

a > thres: tạo ảnh nhị phân (pixel > ngưỡng thì là True, màu trắng).

Chuyển mảng nhị phân thành ảnh PIL.

KQ:

Màn hình hiển thị ảnh xoay góc 45 độ

bài tập 3:

Cắt ảnh từ tọa độ (y: 10, 350, x: 1000, 1450)

mode='L': đọc ảnh ở dạng grayscale (1 kênh độ sáng)


