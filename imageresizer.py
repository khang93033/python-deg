### **Repository 9: Image Resizer**
```python
# Repository: python-image-resizer
# Description: Resize images using Pillow.

from PIL import Image

def resize_image(input_path, output_path, size):
    """Resize an image."""
    img = Image.open(input_path)
    img_resized = img.resize(size)
    img_resized.save(output_path)
    print(f"Resized image saved to {output_path}")

# Example usage
resize_image("input.jpg", "output.jpg", (300, 300))
