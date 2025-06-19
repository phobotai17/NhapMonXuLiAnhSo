Các thư viện sử dụng:

  Thư viện PIL (Pillow): Đọc/ghi ảnh, xử lý ảnh cơ bản
  
  Numpy: Tính toán ma trận ảnh
  
  Matplotlib: hiển thị ảnh
  
  ImageIO: để lưu lại ảnh đã xử lý
  
  SciPy (fftpack): Biến đổi Fourier 2D
  
  OS: duyệt thư mục ảnh  

Giải thích các câu lệnh:

Bài 2:

  Fast Fourier (FF): biểu diễn ảnh trong miền tần số
  
  Butterworth Lowpass Filter (BLF): làm mờ, giữ chi tiết lớn, loại bỏ nhiễu/tần số cao
  
  Butterworth Highpass Filter (BHF): làm sắc nét, giữ chi tiết nhỏ, loại bỏ vùng mịn

Cách hoạt động của Fast Fourier

  Mỗi ảnh đầu vào được chuyển sang ảnh xám (convert("L"))
  
  Dùng fft2 để biến đổi từ miền không gian ảnh gốc sang miền tần số
  
  Dùng fftshift để dịch tâm tần số ra giữa (để dễ nhìn)
  
  Lấy log (log(1 + |F|)) để hiển thị tần số rõ hơn
  
  Ảnh hiển thị là biểu đồ tần số, vùng trung tâm là tần số thấp, vùng rìa là chi tiết nhỏ.

Butterworth Lowpass Filter

  Tạo bộ lọc H(u,v) theo công thức:
  ​
  H(u,v) = 1 / 1 + (D(u,v) / D0)^2n 
  
  Trong đó:
  
  D(u,v): khoảng cách tới tâm ảnh trong miền tần số
  
  D0 = 30: ngưỡng cắt
  
  n = 1: bậc lọc
  
  Nhân bộ lọc H(u,v) với phổ tần số F(u,v) rồi biến đổi ngược về không gian bằng ifft2
  
  Anh đã được làm mờ nhẹ, giữ cấu trúc lớn, lọc bỏ nhiễu.

BHF – Butterworth Highpass Filter

  Giống BLF nhưng công thức đảo ngược:
  
  H(u,v) = 1 / 1 + (D0 / D(u,v))^2n
  
  Dùng bậc n = 2 để làm sắc nét ảnh rõ hơn
  
  Bộ lọc này giúp tăng chi tiết
  
  Sau khi lọc biến đổi ngược về không gian và lưu ảnh.

Bài 3:

  Hoán đổi ngẫu nhiên thứ tự kênh màu (R, G, B) để tạo hiệu ứng màu mới

  1.Dùng Image.open().convert("RGB") để đảm bảo ảnh có 3 kênh màu
  
  2.Tạo một hoán vị ngẫu nhiên của [0, 1, 2] tương ứng (R, G, B)
  
    perm = np.random.permutation(3)
    img_array[:, :, perm]

  3.Biến đổi từng kênh màu bằng 1 trong 5 phép biến đổi:

    Inverse: Ảnh âm bản

    Gamma correction: Điều chỉnh độ sáng

    Log transform: Nhấn mạnh vùng tối, nén vùng sáng

    Histogram equalization: Cân bằng phân bố độ sáng, làm nổi chi tiết

    Contrast stretching: Kéo giãn cường độ từ [min, max] về [0, 255]

  4.Sau khi xử lý xong từng kênh 
  
    gộp lại bằng Image.fromarray()
  
    Dùng matplotlib để hiển thị ảnh
    
    Lưu lại bằng iio.imwrite()

  Khi sử dụng các phép biến đổi trên từng kênh riêng biệt, ta có thể thấy rõ tác động của mỗi phép lên màu sắc tổng thể.

Bài 4:

  1.Tạo một hoán vị ngẫu nhiên của [0, 1, 2] tương ứng (R, G, B)
  
    perm = np.random.permutation(3)
    img_array[:, :, perm
    
  2.Biến đổi Fourier và lọc Butterworth
  
  Chuyển sang ảnh xám vì Fourier hoạt động trên ảnh đơn kênh nên cần chuyển ảnh sang grayscale.

  Biến đổi Fourier:
  
    F = fft2(im_array)             
    F_shifted = fftshift(F)        

  Tạo mặt nạ lọc Butterworth cho lowpass và highpass

  Nhân với phổ tần số và biến đổi ngược

    G = F_shifted * H              
    
    img_back = ifft2(ifftshift(G))

  3. Sử dụng Min và Max filter(Theo công thức ở bài 2):
     
    MinFilter làm ảnh mịn hơn, giảm nhiễu sau lọc lowpass
    
    MaxFilter làm ảnh nét mạnh hơn, tăng chi tiết khi lọc highpass

    
    

  
