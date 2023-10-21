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


def generate_pdf(input_files, output_type, output_path):
    if not input_files:
        print("No image files found in the folder.")
        return

    if output_type == 'single':
        pdf_output = output_path + '/iscan.pdf'
        images_to_pdf(input_files, pdf_output)
    elif output_type == 'multi':
        for image in input_files:
            base_name = os.path.splitext(os.path.basename(image))[0]
            pdf_output = output_path + '/' + base_name + '.pdf'
            image_to_pdf(image, pdf_output)
    else:
        print('unknown output type!')


def main(args):
    # Access and use the parameters
    action = args.action
    output_type = args.output_type
    input_files = args.input_files
    output_path = args.output_path

    # Perform some action with the parameters
    if action == 'PDF':
        generate_pdf(input_files, output_type, output_path)
    else:
        print('unknown action! program aborts!')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A Python script with different parameters.")

    # Define your parameters here
    parser.add_argument("--action", type=str, required=True, default='PDF', help="choose action: PDF")
    parser.add_argument("--input_files", type=str, required=True, nargs='+', help="choose action: PDF")
    parser.add_argument("--output_type", type=str, required=True,
                        default='single', help="type of action: single of PDF or multi pdfs ")
    parser.add_argument("--output_path", type=str, required=True, help="the location of images")

    args = parser.parse_args()
    main(args)
