from PIL import Image, ImageOps

# Hàm chèn logo vào ảnh
def add_logo_to_image(frame_image_path, logo_image_path, output_image_path):
    # Mở ảnh nền (test.jpg)
    frame = Image.open(frame_image_path)
    
    # Mở ảnh logo (phukienmoe.jpg)
    logo = Image.open(logo_image_path)
    
    # Loại bỏ viền trắng xung quanh logo
    logo = ImageOps.expand(logo, border=-1, fill='white')
    logo = logo.convert("RGBA")
    datas = logo.getdata()
    newData = []
    for item in datas:
        # Thay thế màu trắng bằng trong suốt
        if item[:3] == (255, 255, 255):
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    logo.putdata(newData)
    
    # Đảm bảo kích thước logo không quá lớn so với ảnh gốc
    max_logo_width = frame.width // 3  # Giới hạn kích thước logo bằng 1/3 chiều rộng của ảnh gốc
    if logo.width > max_logo_width:
        logo_ratio = logo.height / logo.width
        logo = logo.resize((max_logo_width, int(max_logo_width * logo_ratio)))
    
    # Tính toán vị trí đặt logo: căn giữa theo chiều ngang và đặt ở trên cùng
    position = (frame.width // 2 - logo.width // 2, 0)

  # Đặt ở trên cùng
    
    # Dán logo vào ảnh nền
    frame.paste(logo, position, logo)
    
    # Lưu ảnh kết quả
    frame.save(output_image_path)

# Đường dẫn đến file ảnh gốc và logo
frame_image_path = 'test.jpg'  # Ảnh nền gốc (test.jpg)
logo_image_path = 'phukienmoe.jpg'  # Logo (phukienmoe.jpg)
output_image_path = 'output_image_with_logo_fixed.png'  # Ảnh kết quả đầu ra

# Chèn logo vào ảnh nền
add_logo_to_image(frame_image_path, logo_image_path, output_image_path)

print(f"Ảnh với logo đã được lưu tại: {output_image_path}")
