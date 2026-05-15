from PIL import Image
import numpy as np

img = Image.open("input.png").convert("RGBA")
arr = np.array(img)

# 目标颜色：近白色
new_color = np.array([245, 245, 245, 255])  # #F7F3EA

# 判断接近白色的像素
r, g, b, a = arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3]
mask = (r > 245) & (g > 245) & (b > 245) & (a > 0)

arr[mask] = new_color

out = Image.fromarray(arr)
out.save("output.png")