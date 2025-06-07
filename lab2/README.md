Các thư viện sử dụng:

Thư viện PIL (Pillow): Đọc/ghi ảnh, xử lý ảnh cơ bản

Numpy: Tính toán ma trận ảnh

Matplotlib: hiển thị ảnh

ImageIO: để lưu lại ảnh đã xử lý

Giải thích các câu lệnh:

1. Image inverse transformation – iit()

   im_2 = 255 - im_1

   Vì ảnh xám có giá trị từ 0 đến 255, nên việc lấy 255 trừ đi giá trị hiện tại sẽ làm ảnh trở thành âm bản của chính nó


2. Gamma correction – gc()

   Điều chỉnh độ sáng ảnh theo hàm mũ

   Giúp làm sáng ảnh tối hoặc làm tối ảnh sáng một cách phi tuyến tính

   Tham số gamma:

    Nếu gamma < 1: ảnh sáng lên

    Nếu gamma > 1: ảnh tối đi

3. Log transformation – lt()

   Dùng hàm log để làm nổi bật các chi tiết ở vùng tối (nơi có giá trị nhỏ)

   Logarit làm cho khoảng cách giữa các giá trị nhỏ dãn ra, nên các chi tiết vùng tối được tăng cường rõ hơn

4.Histogram equalization – he()

  Cân bằng lại độ phân bố sáng của ảnh để ảnh không bị quá tối hoặc quá sáng. Rất hữu ích với ảnh có độ tương phản thấp

  Nếu ảnh quá nhiều điểm tối, thì histogram sẽ dồn về bên trái. Sau khi equalization, histogram được trải đều thì ảnh nhìn rõ ràng và cân bằng hơn

5. Contrast Stretching – cs()

   Kéo dãn độ tương phản ảnh ra hết mức từ min đến max

   Nếu ảnh ban đầu chỉ có giá trị nằm trong khoảng nhỏ (ví dụ từ 50 đến 150), thì ảnh sẽ hơi xám xám, không rõ nét

Sau khi giãn, các giá trị được map lại để nằm trọn vẹn trong [0, 255] thì ảnh nét và rõ hơn

6. List_of_images

list_of_images = [r"exercise\ha-long-bay-in-vietnam.jpg",

                  r"exercise\pagoda.jpg",
                  
                  r"exercise\quang_ninh.jpg",]
                  
                 
   Danh sách ảnh
