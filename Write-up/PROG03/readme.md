# Báo cáo bài tập số 3
***
### Cách hoạt động của sshtrojan1:
1. Tìm kiếm process có người đăng nhập sudo `ps aux | grep "\[priv\]"`
2. Từ lệnh này, lấy tên Username và id của tiến trình
3. Hàm check có chức năng kiểm tra xem đã có mật khẩu nhập đúng hay chưa
4. Nếu có mật khẩu đúng, tiến hành truy vết input và lấy mật khẩu
