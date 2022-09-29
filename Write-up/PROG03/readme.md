# Báo cáo bài tập số 3
***
### Cách hoạt động của sshtrojan1:
1. Tìm kiếm process có người đăng nhập `sudo ps aux | grep "\[priv\]"`
2. Từ lệnh này, lấy tên Username và id của tiến trình
3. Tiến hành đọc thông tin trao đổi từ tiến trình vào file foo `sudo strace -p [ppid] 2> foo`
4. Hàm check có chức năng kiểm tra xem đã có mật khẩu nhập đúng hay chưa
5. Nếu có mật khẩu đúng, tiến hành truy vết input và lấy mật khẩu

###### **Lưu ý: ** trong sshd_config để 2 dòng sau ở trạng thái uncommented `PubkeyAuthentication no` và `PasswordAuthentication yes`

### Cách hoạt động của sshtrojan2:
1. 
2. 
3. 
4. 
5. 