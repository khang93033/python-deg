# New Feature: Resize multiple images at once

from PIL import Image
import os

def bulk_resize_images(directory, size):
    """Resize all images in a directory."""
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(os.path.join(directory, filename))
            img_resized = img.resize(size)
            img_resized.save(os.path.join(directory, f"resized_{filename}"))
    print("All images resized successfully.")

# Example usage
bulk_resize_images("/path/to/images", (300, 300))
