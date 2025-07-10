Bài 2.1:
threshold_otsu: Tự động tìm ngưỡng phân cách nền và vật.

label:	Gán nhãn cho từng vùng trắng.

regionprops:	Tính các thuộc tính hình học, ví dụ như diện tích, tâm, bbox,...

mpatches.Rectangle:	Vẽ bounding box quanh mỗi vùng có nhãn.

KQ:

phân vùng đối tượng (object labeling) trên ảnh đen trắng bird.png bằng Otsu threshold và hiển thị các hộp giới hạn (bounding boxes) quanh từng đối tượng.

Bài 2.2:

Màu ban đầu được chuyển về ảnh đen trắng (grayscale)

Ảnh được dịch xuống 1 pixel để giúp tạo ra sự khác biệt giữa ảnh gốc và ảnh dịch.

Mỗi pixel được so sánh với pixel phía trên nó.

Nếu có sự thay đổi mạnh: giá trị lớn thì biểu hiện biên.

KQ:

phát hiện biên ảnh bằng cách so sánh ảnh gốc và ảnh đã tịnh tiến. 

bài 2.3:

axis=0: Tính đạo hàm theo hàng ngang

axis=1: Tính đạo hàm theo cột dọc

abs(a) và abs(b) lấy trị tuyệt đối của gradient theo hai trục.

Tổng lại để tạo ảnh thể hiện mức độ mạnh của biên tại mỗi điểm.

KQ:

Dùng bộ lọc Sobel để phát hiện đường biên trong ảnh

Bài 2.4:

axis=0: Tính đạo hàm theo hàng ngang

axis=1: Tính đạo hàm theo cột dọc

Tạo các phần tử của ma trận tự tương quan

Làm mượt giúp ổn định kết quả và giảm nhiễu cục bộ.

Tính ma trận đặc trưng và chỉ số góc (R) 

R = detC - α trC^2

R càng lớn thì điểm đó càng có khả năng là góc.

alpha là hệ số nhạy cảm nên chọn từ 0.04 đến 0.2.

KQ: Phát hiện các góc trong ảnh như những điểm mà độ sáng thay đổi theo nhiều hướng

Bài 2.5:

data:	Ảnh nhị phân

lineHough(data, γ):	Trả về ảnh Hough với ngưỡng γ để bỏ qua điểm quá yếu

Ma trận ho[rho, theta] dùng để tích lũy phiếu.

theta chia đều từ 0° đến 89° (0–89 độ, bước 1°).

rho = x cosθ + y sinθ:	Công thức biến đổi Hough

Tìm điểm có giá trị cao nhất trong ảnh W.

(v, h) là tọa độ điểm đang xét.

ho[rho, theta]:	Ma trận lưu số phiếu, càng sáng càng có khả năng là đường thẳng

Với mỗi góc theta, tính toán tương ứng giá trị rho của điểm đang xét.

Với mỗi giá trị  (p,0), cộng thêm giá trị pixel vào ma trận ho.

Sau khi xử lý một điểm, đặt nó về 0 để không xét lại.

KQ:

Hàm lineHough(indata, gamma) thực hiện biến đổi Hough để phát hiện các đường thẳng trong ảnh đầu vào indata
