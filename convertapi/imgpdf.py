import img2pdf 
from PIL import Image 
import os 

def custom_img2pdf(img_path,pdf_path):
    # opening image 
    image = Image.open(img_path) 
    
    # converting into chunks using img2pdf 
    pdf_bytes = img2pdf.convert(image.filename) 
    
    # opening or creating pdf file 
    file = open(pdf_path, "wb") 
    
    # writing pdf files with chunks 
    file.write(pdf_bytes) 
    
    # closing image file 
    image.close() 
    
    # closing pdf file 
    file.close() 
    
    # output 
    print("Successfully made pdf file")

    return 0


def custom_img_png_2pdf(img_path,pdf_path):
    # opening image 
    # image = Image.open(img_path) 
    
    rgba = Image.open(img_path)
    rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
    rgb.paste(rgba, mask=rgba.split()[3])               # paste using alpha channel as mask
    rgb.save(pdf_path, 'PDF', resoultion=100.0)
    # output 
    print("Successfully made pdf file")

    return 0