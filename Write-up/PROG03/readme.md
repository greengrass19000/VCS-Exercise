# Báo cáo bài tập số 3
***
### Cách hoạt động của sshtrojan1:
1. Tìm kiếm process có người đăng nhập `sudo ps aux | grep "\[priv\]"`
2. Từ lệnh này, lấy tên Username và id của tiến trình
3. Tiến hành đọc thông tin trao đổi từ tiến trình vào file foo `sudo strace -p [ppid] 2> foo`
4. Hàm check có chức năng kiểm tra xem đã có mật khẩu nhập đúng hay chưa
5. Nếu có mật khẩu đúng, tiến hành truy vết input và lấy mật khẩu

###### **Lưu ý:** trong sshd_config để 2 dòng sau ở trạng thái uncommented `PubkeyAuthentication no` và `PasswordAuthentication yes`

### Cách hoạt động của sshtrojan2:
1. Phát hiện process được dùng để đăng nhập nơi khác `pgrep -a -f '^ssh '`
2. Tại bước này ta lấy được username và pid
3. Tiến hành đọc thông tin trao đổi từ tiến trình vào file foo `sudo strace -p [ppid] 2> foo`
4. Dựa trên trạng thái trong reply message của máy tính kết nối (=28 cho password đúng)
5. Khi có tín hiệu mất khẩu đúng, truy vết file  và lấy mật khẩu

## Kiến thức nắm được sau bài tập
- Cài đặt SSH trên Windows và Linux, thiết lập config SSH server thông qua file 'sshd_config'
- Lấy thông tin từ tiến trình
- Đọc dữ liệu từ file lưu trữ nội dung tương tác giữa client và server của SSH
- Chạy lệnh song song để thu thập thông tin mà không ảnh hưởng đến trạng thái hoạt động của tiến trình
- Thực hiện code và compile trên và cấp quyền root cho Sublime-Text