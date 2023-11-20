# gaussian_blur

1. Giới thiệu về Gaussian Blur:
- Là một loại bộ lọc làm mờ hình ảnh sử dụng hàm Gaussian (cũng được sử dụng cho phân bố chuẩn trong thống kê) để tính toán phép biến đổi áp dụng cho từng pixel trong hình ảnh.
2. Gaussian Blur trong OpenCV:
  - Để thực hiện Gaussian Blur trong OpenCV, bạn có thể sử dụng hàm GaussianBlur của thư viện OpenCV. Hàm này nhận vào ảnh đầu vào và các tham số như kích thước của bộ lọc và độ đơn điệu của Gaussian. Kết quả là ảnh đã được làm mờ bằng cách áp dụng bộ lọc Gaussian.
3. Tính năng của ứng dụng :
 - Chọn hình ảnh từ file người dùng.
<img width="1507" alt="Ảnh màn hình 2023-11-20 lúc 15 50 48" src="https://github.com/pinniheo211/gaussian_blur/assets/84260434/547a6b0b-f58d-44d0-9a40-4019940668a5">
 - Upload ảnh lên và thực hiện chỉnh đồ mờ của ảnh.
   <img width="1505" alt="Ảnh màn hình 2023-11-20 lúc 15 53 24" src="https://github.com/pinniheo211/gaussian_blur/assets/84260434/e447b5a5-f8fd-46e7-9258-2275809b235a">
 - Sau khi đã làm mờ ảnh và tiến hành download ảnh đã làm mờ về.
DEMO (hướng dẫn chạy ứng dụng):
B1: vào pycharm và create new project với flask.
<img style="display:block" width="811" alt="Ảnh màn hình 2023-11-20 lúc 15 54 57" src="https://github.com/pinniheo211/gaussian_blur/assets/84260434/af9fceac-472c-485b-a874-09f66bd3ab52">

B2: mở terminal vào thư mục project clone dự án về:

git clone https://github.com/pinniheo211/gaussian_blur.git 
<img width="962" alt="Ảnh màn hình 2023-11-20 lúc 15 56 00" src="https://github.com/pinniheo211/gaussian_blur/assets/84260434/96a82b03-7a42-45da-9d7d-8737a0c0a644">

sau khi clone xong cd vào thư mục gaussian_blur : cd gaussian_blur
<img width="630" alt="Ảnh màn hình 2023-11-20 lúc 15 57 14" src="https://github.com/pinniheo211/gaussian_blur/assets/84260434/0e873fba-e92c-42fc-b75f-88e1a66140aa">


B3: cài đặt opencv: pip(pip3) install opencv-python
 <img width="713" alt="Ảnh màn hình 2023-11-20 lúc 15 57 46" src="https://github.com/pinniheo211/gaussian_blur/assets/84260434/a127fa19-79d8-4b0a-8fa4-a53ce5d16985">

B4: chạy chương trình : python app.py
<img width="966" alt="Ảnh màn hình 2023-11-20 lúc 15 58 16" src="https://github.com/pinniheo211/gaussian_blur/assets/84260434/092ca9f2-d881-49f4-9c0e-429fe9ac5283">

-> Giao diện trang chủ của trang web:
<img width="1507" alt="Ảnh màn hình 2023-11-20 lúc 15 58 50" src="https://github.com/pinniheo211/gaussian_blur/assets/84260434/db62504e-59c7-4590-8962-bcdd918b1d21">


 
