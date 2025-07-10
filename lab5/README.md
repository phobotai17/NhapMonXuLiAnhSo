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

s là structuring element (SE) hình chữ thập 3x3.

Cấu trúc này giúp tập trung xử lý các điểm ảnh ở giữa và lân cận theo 4 hướng chính.

binary_closing: thực hiện dilation rồi erosion giúp lấp các lỗ nhỏ và làm mịn vùng trắng.

iterations=50: lặp lại phép đóng đến 50 lần để làm mờ các chi tiết nhiễu mạnh mẽ hơn.

KQ:

giúp phân biệt vùng trắng và đen dễ hơn.

Bài tập 4:

Chương trình cung cấp hai nhóm công cụ xử lý ảnh:

1.Geometric Transformations:

Tịnh tiến (Translation): Tịnh tiến ảnh theo giá trị x, y nhập từ người dùng.

Xoay ảnh (Rotation): Xoay ảnh với góc angle do người dùng nhập vào.

Phóng to (Zoom) :	Phóng to ảnh với hệ số zoom_factor.

Vẽ lưới tọa độ (Coordinate Mapping): Thêm lưới tọa độ (grid lines) lên ảnh.

2.Image Segmentation:

Ngưỡng hóa thích nghi (Adaptive Threshold): Áp dụng ngưỡng Otsu và hiển thị ảnh nhị phân.

Giãn ảnh nhị phân (Binary Dilation): Áp dụng phép giãn nhị phân với SE hình chữ thập, 50 lần.

Co ảnh nhị phân (Binary Erosion): Áp dụng phép co nhị phân.

Ngưỡng Otsu (Otsu Thresholding): Áp dụng phân ngưỡng bằng phương pháp Otsu.

Người dùng có thể chọn:

Thực hiện 1 trong 2 nhóm thao tác.

Hoặc thực hiện cả hai nhóm: đầu tiên là geometric, sau đó áp dụng segmentation lên ảnh đã biến đổi.

