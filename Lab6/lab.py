from Crypto.Cipher import AES
from PIL import Image
from math import ceil, sqrt
from collections import Counter
import os


BLOCK_SIZE = 16

def is_16_byte(file_data):
    if len(file_data) % 16 !=0:
        return False
    return True


def read_header(file):
    with open(file, "rb") as f:
        return f.read()[:54]

def read_body(file):
    with open(file, "rb") as f:
        # Skip header of 54 bytes to only have the image data
        return f.read()[54:]
    

def create_16_byte_blocks(data):
    blocks = []
    for i in range(0, len(data), BLOCK_SIZE):
        block = data[i : i + BLOCK_SIZE]
        blocks.append(block)
    return blocks

def map_blocks_canvas(blocks, block_counts , total):
    pixel_values = []
    for block in blocks:
        freq = block_counts[block]
        # Normalize frequency to range 0–255
        value = min(int((freq / total) * 255), 255)
        pixel_values.append(value)
        
    return pixel_values


def pixel_2_image(pixel_values):
    num_pixels = len(pixel_values)
    side = int(ceil(sqrt(num_pixels)))
    pixel_values += [0] * (side * side - num_pixels)
    
    img = Image.new('L', (side, side))
    img.putdata(pixel_values)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img.save('result.png')

def main():
    src_file = 'aes.bmp.enc'
    
    # Male sense of header
    enc_header_data = read_header(src_file)
    print(enc_header_data)
    
    enc_body_data = read_body(src_file)

    print(f"File is 16 bytes? {is_16_byte(enc_body_data)}")
    
    # Taking advantage of ECB weekness
    blocks = create_16_byte_blocks(enc_body_data)
    
    block_counts = Counter(blocks)
    max_count = max(block_counts.values()) if block_counts else 1
    
    # Create grayscale mapping on the frequency of each block present
    pixel_values = map_blocks_canvas(blocks , block_counts, max_count)
    # print(pixel_values)
    
    # Create Image from the pixel mapping
    pixel_2_image(pixel_values)



if __name__ == "__main__":
    main()