### **Repository 9: Image Resizer**
```python
# Repository: python-image-resizer
# Description: Resize images using Pillow.

from PIL import Image

def resize_image(input_path, output_path, width=None, height=None):
    img = Image.open(input_path)
    original_width, original_height = img.size

    if width and not height:
        height = int((original_height / original_width) * width)
    elif height and not width:
        width = int((original_width / original_height) * height)

    img_resized = img.resize((width, height))
    img_resized.save(output_path)
    print(f"Resized image saved to {output_path}")

# Example usage
resize_image("input.jpg", "output.jpg", width=300)

from PIL import Image
import os

def bulk_resize_images(directory, size):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(os.path.join(directory, filename))
            img_resized = img.resize(size)
            img_resized.save(os.path.join(directory, f"resized_{filename}"))
    print("All images resized successfully.")

# Example usage
bulk_resize_images("/path/to/images", (300, 300))
