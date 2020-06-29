"""
Stitcher.py
Author: Yashkir Ramsamy
Purpose: Stitch multiple pdf files together to create a single file

"""

import PyPDF2
import os


def fileName(file_path):
    return file_path[file_path.rfind("/") + 1:]


def stitch(file_list, output_name):
    stitcher = PyPDF2.PdfFileMerger()  # Merger object which handles stitches

    for file in file_list:
        print("Stitching:", file)
        stitcher.append(file, fileName(file))

    with open(output_name, 'wb') as output_pdf:
        stitcher.write(output_pdf)


def main():
    stitch_mode = input("Stitch mode: Automatic/Manual\n")

    if stitch_mode.lower() == "automatic":
        dir = input("Enter directory of PDFs: ")
        output_name = input("Enter name of output file: ") + ".pdf"
        file_list = []
        for file in os.listdir(dir):
            if file.endswith(".pdf"):
                file_list.append(dir + "/" + file)
        stitch(file_list, output_name)
    elif stitch_mode.lower() == "manual":
        file_path = ''
        file_list = []
        print("Enter file path of PDFs to stitch in order. \nEnter \"done\" when complete.")
        while file_path != "done":
            file_path = input()
            file_list.append(file_path)
        output_name = input("Enter name of output file: ") + ".pdf"
        stitch(sorted(file_list), output_name)

    else:
        print("Not a valid mode.")
    print("Exiting")


if __name__ == "__main__":
    try:
        main()
    except:
        print("Something went wrong. Exiting.")
