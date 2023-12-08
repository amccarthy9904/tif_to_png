from pathlib import Path
from PIL import Image, ImageSequence
import imageio


def convert_tif_to_png(folder_path):
    # Convert folder path to a Path object
    folder_path = Path(folder_path)

    # Iterate through each file in the folder
    for file_path in folder_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() == ".tif":
            # Load the TIFF image using Pillow
            # img = Image.open(file_path)
            img = imageio.imread(file_path, format='tiff')
    
            new_file_path = folder_path.with_name(f"{file_path.stem}{str(1)}.png") 
            imageio.imwrite(new_file_path, img)

            # if img.mode != 'RGB':
            #     img = img.convert('RGB')
            # for i, page in enumerate(ImageSequence.Iterator(img)):
                
            #     new_file_path = folder_path.with_name(f"{file_path.stem}{str(i+1)}.png") 
            #     img.save(new_file_path, "PNG")

            print(f"Converted {file_path.name} to {new_file_path.name}")

if __name__ == "__main__":
    # Replace 'your_folder_path' with the actual folder path containing the TIFF images
    folder_path = input("Enter the folder path: ")
    convert_tif_to_png(folder_path)
