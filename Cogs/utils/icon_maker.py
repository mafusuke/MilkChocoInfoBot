"""Tool to crop each of icons for costume"""
from PIL import Image
from tqdm import tqdm
HOME = "./"
im = Image.open(HOME+'image0.png')
# bar = tqdm(total=12*8)  # COSTUMES
# count = 1
# for tate in range(8):
#     for yoko in range(12):
#         bar.update(1)
#
#         # head:
#         # im_crop = im.crop((yoko * 80, tate * 80 + 5, yoko * 80 + 80, tate * 80 + 75))
#         # body, back:
#         im_crop = im.crop((yoko*80, tate*110+10, yoko*80+80, tate*110+100))
#
#         im_crop.save(HOME + f'res\\{count}.png')
#         count += 1

bar = tqdm(total=4*5)  # CHARACTER ICONS
count = 1
for tate in range(4):
    for yoko in range(5):
        bar.update(1)
        x = 90
        y = 90
        im_crop = im.crop((yoko * y, tate * x, yoko * x+x, tate * y+y))
        im_crop.save(HOME + f'res/{count}.png')
        count += 1


