from PIL import Image

# Tạo logo từ ảnh vuông với viền trắng
def create_logo_with_border(input_image_path, output_image_path, border_size):
    # Mở ảnh gốc
    img = Image.open(input_image_path)
    
    # Tạo một ảnh mới với kích thước lớn hơn để thêm viền trắng
    new_size = (img.size[0] + border_size * 2, img.size[1] + border_size * 2)
    bordered_img = Image.new('RGB', new_size, 'white')  # Nền trắng
    
    # Dán ảnh gốc vào giữa ảnh có viền
    bordered_img.paste(img, (border_size, border_size))
    
    # Lưu ảnh ra file
    bordered_img.save(output_image_path)

# Đường dẫn đến file ảnh gốc và file ảnh đầu ra
input_image_path = 'test.jpg'  # Thay đổi đường dẫn đến ảnh gốc của bạn
output_image_path = 'logo_with_white_border.png'  # Đường dẫn để lưu logo mới
border_size = 50  # Kích thước viền trắng

# Gọi hàm tạo logo
create_logo_with_border(input_image_path, output_image_path, border_size)

print(f"Logo đã được lưu tại: {output_image_path}")
