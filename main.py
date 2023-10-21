import argparse
import os

from PIL import Image


def image_to_pdf(image_file, pdf_output):
    img = Image.open(image_file)
    img.save(pdf_output, "PDF")


def images_to_pdf(image_files, pdf_output):
    imgs = []
    for image_file in image_files:
        imgs.append(Image.open(image_file))
    if len(imgs) == 1:
        imgs[0].save(pdf_output, "PDF")
    elif len(imgs) > 1:
        imgs[0].save(pdf_output, "PDF", save_all=True, append_images=imgs[1:])


def generate_pdf(output_type, image_folder):
    image_files = [file for file in os.listdir(image_folder) if file.endswith(('.jpeg', '.tiff'))]
    image_full_paths = [os.path.join(image_folder, filename) for filename in image_files]

    if not image_full_paths:
        print("No image files found in the folder.")
        return

    pdf_folder = image_folder + '/pdf'
    if not os.path.isdir(pdf_folder):
        os.makedirs(pdf_folder)

    if output_type == 'single':
        pdf_output = pdf_folder + '/iscan.pdf'
        images_to_pdf(image_full_paths, pdf_output)
    elif output_type == 'multi':
        for image in image_full_paths:
            base_name = os.path.splitext(os.path.basename(image))[0]
            pdf_output = pdf_folder + '/' + base_name + '.pdf'
            image_to_pdf(image, pdf_output)
    else:
        print('unknown output type!')


def main(args):
    # Access and use the parameters
    action = args.action
    output_type = args.output_type
    path = args.path

    # Perform some action with the parameters
    if action == 'PDF':
        generate_pdf(output_type, path)
    else:
        print('unknown action! program aborts!')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A Python script with different parameters.")

    # Define your parameters here
    parser.add_argument("--action", type=str, required=True, default='PDF', help="choose action: PDF")
    parser.add_argument("--output_type", type=str, required=True,
                        default='single', help="type of action: single of PDF or multi pdfs ")
    parser.add_argument("--path", type=str, required=True, help="the location of images")

    args = parser.parse_args()
    main(args)
