import os
from PIL import Image


def create_manga_pdf(base_dir, output_pdf_name):
    chapters = sorted(
        [folder for folder in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, folder))])

    all_pages = []

    for chapter in chapters:
        chapter_path = os.path.join(base_dir, chapter)

        images = sorted(
            [os.path.join(chapter_path, img) for img in os.listdir(chapter_path) if img.endswith('.png')],
            key=lambda x: int(os.path.splitext(os.path.basename(x))[0])
        )

        for img_path in images:
            img = Image.open(img_path).convert('RGB')
            all_pages.append(img)

    if all_pages:
        all_pages[0].save(output_pdf_name, save_all=True, append_images=all_pages[1:])
        print(f"Created PDF successfully: {output_pdf_name}")
    else:
        print("No images found")


base_directory = "path/to/your/chapters/"
output_pdf = "output.pdf"

if __name__ == '__main__':
    create_manga_pdf(base_directory, output_pdf)
