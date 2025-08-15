### **Repository 9: Image Resizer**
```python
# Repository: python-image-resizer
# Description: Resize images using Pillow.

from PIL import Image

def resize_image(input_path, output_path, size, watermark=None):
    img = Image.open(input_path)
    img_resized = img.resize(size)
    if watermark:
        draw = ImageDraw.Draw(img_resized)
        draw.text((10, 10), watermark, fill=(255, 255, 255))
    img_resized.save(output_path)
    print(f"Resized image saved to {output_path}")

# Example usage
resize_image("input.jpg", "output.jpg", (300, 300))
