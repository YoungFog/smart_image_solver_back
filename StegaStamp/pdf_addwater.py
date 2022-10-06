import PyPDF2
import argparse
def get_writer(water_file,page_pdf):
    """
    将水印pdf与pdf的一页进行合并
    :param water_file:
    :param page_pdf:
    :return:
    """
    pdfReader = PyPDF2.PdfFileReader(water_file)
    page_pdf.mergePage(pdfReader.getPage(0))
    return page_pdf

# 遍历pdf的每一页,添加水印

def add_watermark(origin_file,water_file,target_file):
    pdfWriter = PyPDF2.PdfFileWriter()  # 用于写pdf
    pdfReader = PyPDF2.PdfFileReader(origin_file)  # 读取pdf内容
    for page in range(pdfReader.numPages):
        page_pdf = get_writer(water_file, pdfReader.getPage(page))
        pdfWriter.addPage(page_pdf)
    pdfReader = PyPDF2.PdfFileReader(water_file)
    page_pdf.mergePage(pdfReader.getPage(0))
    with open(target_file, 'wb') as t:
        pdfWriter.write(t)
    # return page_pdf
def parse_args():
    """Get user command line parameters"""
    parser = argparse.ArgumentParser(description="These options are available")
    parser.add_argument("--input_file", help="Input PDF file you want to add watermark", type=str)
    parser.add_argument("--water_file", help="Input watermark file",type=str)
    parser.add_argument("--new_file",help="new file_s name",type=str)

    args = vars(parser.parse_args())
    # To Display Command Arguments Except Password
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i, j)
          for i, j in args.items() if i != 'password'))
    print("######################################################################")
    return args

if __name__=='__main__':
    args = parse_args()
    # Encrypting or Decrypting File
    add_watermark(
        origin_file=args['input_file'],
        water_file=args['water_file'],
        target_file=args['new_file']
    )