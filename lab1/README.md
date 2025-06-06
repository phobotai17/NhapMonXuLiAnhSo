Các thư viện sử dụng:

- Thư viện PIL (Pillow): Đọc/ghi ảnh, xử lý ảnh cơ bản
- OpenCV (cv2):	Đọc, xử lý, và lưu ảnh
- Numpy:	Tính toán ma trận ảnh
- colorsys:	Chuyển đổi RGB sang HSV và ngược lại
- os:	Quản lý file/thư mục
- random:	Cho giá trị ngẫu nhiên để đổi màu

Giải thích các câu lệnh:

1) SỬ DỤNG MÀU RGB
  image = Image.open("excercise/baby.jpeg")
  r, g, b = image.split()

  Ảnh được chia thành 3 kênh: Đỏ (R), Xanh lá (G), Lam (B)
  Mỗi kênh được lưu lại thành ảnh đơn sắc chứa thông tin kênh tương ứng

2) HOÁN ĐỔI VỊ TRÍ CÁC MÀU RGB
  swapped_image = Image.merge("RGB", (b,g,r))

  Đổi vị trí kênh R và B → tạo hiệu ứng màu mới (ví dụ: ảnh sẽ nghiêng về màu xanh nhiều hơn)

3) CHUYỂN MÀU SANG HSV RỒI THAY ĐỔI MÀU SẮC
  hue_shifts = [0.0, 0.333, 0.667]

  Đọc ảnh xong chuyển sang HSV, sau đó thay đổi hoàn toàn giá trị hue (màu)
  Tạo ra 3 ảnh với các tông màu khác nhau: đỏ, xanh lá, xanh dương

4) ĐIỂU CHỈNH MÀU HSV BẰNG HỆ SỐ
  h_new = (1/3) * h
  v_new = (3/4) * v

  Giảm hue về 1/3 để ảnh có màu lệch nhẹ (vàng hoặc xanh)
  Giảm độ sáng (value) xuống còn 75%

5) LỌC NHIỄU BẰNG BỘ LỌC TRUNG BÌNH(MEAN FILTER)
  filtered_image = image.filter(ImageFilter.BoxBlur(1))

  Dùng bộ lọc trung bình (như làm mờ nhẹ) → khử nhiễu salt & pepper nhẹ

6) SO SÁNH CÁC BỘ LỌC KHỬ NHIỄU(MEAN, MEDIAN, GAUSSIAN)
  cv2.blur, cv2.medianBlur, cv2.GaussianBlur
  
  Mean: trung bình điểm ảnh
  Median: giữ cạnh tốt, khử nhiễu dạng đốm
  Gaussian: làm mịn ảnh, giữ chi tiết mượt hơn

7) XÁC ĐỊNH BIÊN TRƯỚC KHI KHỬ NHIỄU
  sobelx = cv2.Sobel(...)
  sobely = cv2.Sobel(...)

  Ảnh được làm mượt trước (Gaussian)
  Sau đó, dùng Sobel để phát hiện biên ngang/dọc
  Tính độ lớn vector biên để tạo ảnh chỉ hiển thị đường biên

8) ĐỔI MÀU RGB NGẪU NHIÊN SAU KHI KHỬ NHIỄU
  r_scale = random.uniform(0.5, 1.5)

  Tạo hiệu ứng màu ngẫu nhiên bằng cách nhân kênh R, G, B với hệ số ngẫu nhiên

9) ĐỔI MÀU HSV NGẪU NHIÊN SAU KHI KHỬ NHIỄU
  unique_hues = np.linspace(0, 179, num_images)

  Chuyển ảnh sang HSV: thay toàn bộ hue bằng giá trị khác nhau cho mỗi ảnh


