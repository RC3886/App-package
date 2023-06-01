import img2pdf
import os


class ImageConverter:
    def convert_images_to_pdf(self):
        image_folder = "E:\\Downloads\\Picturestoconvert"
        output_pdf_path = "E:\\Downloads\\Picturestoconvert\\convertedfile.pdf"

        image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

        if os.path.exists(output_pdf_path):         # checks if the output PDF file already exists, fixed crashing
            print("Output PDF file already exists. Skipping conversion.")
            print()
            return

        with open(output_pdf_path, "wb") as pdf_file:
            image_pdf_bytes = img2pdf.convert([os.path.join(image_folder, f) for f in image_files])
            pdf_file.write(image_pdf_bytes)
            print("Conversion completed.")
            print()

        converter = ImageConverter()                     # instance of the ImageConverter class
        converter.convert_images_to_pdf()               # call the method on the instance
