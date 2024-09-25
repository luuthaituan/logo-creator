from PIL import Image, ImageOps
import os

# Hàm chèn logo vào ảnh
def add_logo_to_image(frame_image_path, logo_image_path, output_image_path, target_width=None, target_height=None):
    # Mở ảnh nền (frame_image_path)
    frame = Image.open(frame_image_path)
    
    # Mở ảnh logo (logo_image_path)
    logo = Image.open(logo_image_path)
    
    # Chuyển đổi logo sang RGBA để có thể xử lý trong suốt
    logo = logo.convert("RGBA")
    datas = logo.getdata()
    newData = []
    
    for item in datas:
        # Thay thế màu trắng bằng trong suốt
        if item[:3] == (255, 255, 255):  # Nếu pixel là trắng
            newData.append((255, 255, 255, 0))  # Làm trong suốt
        else:
            newData.append(item)  # Giữ nguyên
    logo.putdata(newData)

    # Thay đổi kích thước logo nếu có target_width và target_height
    if target_width and target_height:
        logo = logo.resize((target_width, target_height))
    
    # Đảm bảo kích thước logo không quá lớn so với ảnh gốc (giới hạn 1/3 chiều rộng của ảnh nền)
    max_logo_width = frame.width // 3
    if logo.width > max_logo_width:
        logo_ratio = logo.height / logo.width
        logo = logo.resize((max_logo_width, int(max_logo_width * logo_ratio)))
    
    # Tính toán vị trí để chèn logo (ở giữa phía trên)
    position = (frame.width // 2 - logo.width // 2, 0)  # Căn giữa theo chiều ngang và đặt ở trên cùng
    
    # Dán logo vào ảnh nền
    frame.paste(logo, position, logo)
    
    # Lưu ảnh kết quả ra file
    frame.save(output_image_path, quality=95)
    print(f"Ảnh với logo đã được lưu tại: {output_image_path}")

# Hàm tạo logo từ ảnh vuông với viền trắng
def create_logo_with_border(input_image_path, output_image_path, border_size):
    # Mở ảnh gốc
    img = Image.open(input_image_path)
    
    # Tạo ảnh mới với kích thước lớn hơn để thêm viền trắng
    new_size = (img.size[0] + border_size * 2, img.size[1] + border_size * 2)
    bordered_img = Image.new('RGB', new_size, 'white')  # Nền trắng
    
    # Dán ảnh gốc vào giữa ảnh có viền
    bordered_img.paste(img, (border_size, border_size))
    
    # Lưu ảnh ra file
    bordered_img.save(output_image_path, quality=95)
    print(f"Ảnh với viền trắng đã được lưu tại: {output_image_path}")

# Đường dẫn đến thư mục chứa ảnh nền và thư mục lưu ảnh kết quả
input_folder = 'input_logo'  # Thư mục chứa ảnh nền
logo_image_path = 'phukienmoe.jpg'  # Logo
output_folder = 'output_logo'  # Thư mục lưu ảnh kết quả

# Kiểm tra và tạo thư mục đầu ra nếu chưa tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Kích thước mong muốn của logo
target_width = 600  # Chiều rộng mong muốn
target_height = 120  # Chiều cao mong muốn
border_size = 50  # Kích thước viền trắng

# Lặp qua từng file ảnh trong thư mục đầu vào
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Kiểm tra định dạng file
        frame_image_path = os.path.join(input_folder, filename)  # Đường dẫn đầy đủ tới ảnh nền
        output_image_with_logo = os.path.join(output_folder, f'output_{filename}')  # Tạo tên file đầu ra cho ảnh có logo
        output_image_with_border = os.path.join(output_folder, f'bordered_{filename}')  # Tạo tên file đầu ra cho ảnh có viền

        # Chèn logo vào ảnh nền
        add_logo_to_image(frame_image_path, logo_image_path, output_image_with_logo, target_width, target_height)

        # Thêm viền trắng vào ảnh đã có logo
        create_logo_with_border(output_image_with_logo, output_image_with_border, border_size)

        # Xóa file trung gian sau khi hoàn tất
        if os.path.exists(output_image_with_logo):
            os.remove(output_image_with_logo)
            # print(f"File trung gian {output_image_with_logo} đã bị xóa.")
        else:
            print(f"File {output_image_with_logo} không tồn tại.")
