import numpy as np
img = np.zeros((8, 8), dtype=int)

# print(img)

# # *** Tasks ***
# 1. Draw a white border around the image (set first/last row and column to 255)
print("\n Task 1")
img[0, :] = 255    # top row
img[-1, :] = 255   # bottom row
img[:, 0] = 255    # left column
img[:, -1] = 255   # right column
print(f"White border around the image: \n {img}\n")

# 2. Create a checkerboard pattern (hint: use slicing with a step like [::2])
print("\n Task 2")
board = np.zeros((8, 8), dtype=int)   # separate array, keeps img untouched
board[::2, 1::2] = 1                  # even rows, odd columns
board[1::2, ::2] = 1                  # odd rows, even columns
print(f"Checkerboard pattern: \n {board}\n")


# 3. Make a diagonal line using np.eye()
print("\n Task 3")
diag = np.eye(8, dtype=int)   # 1s on the diagonal, int to match the other arrays
print(f"Diagonal line: \n {diag}\n")

# 4. Crop the middle 4x4 region out of the image
print("\n Task 4")
middle_region = img[2:6, 2:6]
print(f"Middle 4x4 region out of the image: \n {middle_region}\n")

# 5. Flip the image upside down, then left to right
print("\n Task 5")
flipped_image_ud = np.flipud(img)
print(f"Upside Down: \n {flipped_image_ud}\n")
flipped_image_lr = np.fliplr(flipped_image_ud)
print(f"Left Right: \n {flipped_image_lr}\n")

# 6. Rotate the image by 90 degrees
print("\n Task 6")
rotated_image = np.rot90(img)   # counter-clockwise by default
print(f"Rotated 90 degrees: \n {rotated_image}\n")

# 7. Invert the colors (255 - img)
print("\n Task 7")
print(f"Inverted image: \n {255 - img}\n")


# 8. Stack 3 different 2D arrays into one (8, 8, 3) RGB image and print its shape
print("\n Task 8")
# each 8x8 array becomes one colour channel: img = red, board = green, diag = blue
# axis=2 adds the new axis at the end, so every pixel holds its own [R, G, B] triple
rgb = np.stack([img, board, diag], axis=2)
print(f"RGB image: {rgb}\n")           # (8, 8, 3) -> 8 rows, 8 cols, 3 channels
print(f"RGB image shape: {rgb.shape}\n")           # (8, 8, 3) -> 8 rows, 8 cols, 3 channels
print(f"Top-left pixel [R, G, B]: {rgb[0, 0]}\n")  # one pixel = 3 numbers, one per channel