from PIL import Image
import sys
import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()

# OCRツールをインストールされているか確認
if len(tools) == 0:
  print("No OCR tool found")
  sys.exit(1)

# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name())) # インストールされているOCRツールを表示

# そのOCRツールで使用できる言語を確認
langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))

# 使用する言語を選択
lang = langs[1]
print("Will use lang '%s'" % (lang))

im1 = Image.open('0194.jpg')
txt = tool.image_to_string(
  im1,
  lang=lang,
  builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
print(txt)