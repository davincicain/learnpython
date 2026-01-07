"""
https://pypi.python.org

CMD command
upgrade pip: python -m pip install --upgrade pip
install: pip install module name
install form mirror site URL: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple module name
uninstall: pip uninstall module name
view the installed list: pip list
view the module information: pip show module name

pillow: process image
"""

from PIL import Image

def main():
    a = Image.open(r"D:\shaojun3\Desktop\py\reference1\whitecat1.jpg")
    b = a.convert("L") #convert into black and white photos
    b.save(r"D:\shaojun3\Desktop\py\reference1\whitecat3.jpg")

if __name__ == '__main__':
    main()