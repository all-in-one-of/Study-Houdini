from PIL import Image

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2, (img_height - crop_height) // 2, (img_width + crop_width) // 2, (img_height + crop_height) // 2))


def crop_top_left(pil_img, crop_width, crop_height):
    return pil_img.crop((0,0, crop_width, crop_height))



for i in range(0,142):

    # num = "%05d" % i
    num = str(i)
    in_path = "JPG/img-" + num + ".jpg"
    out_path = "src_cropped/img-" + num + ".jpg"
    img = Image.open(in_path)
    # img_new = crop_center(img, 720, 720)
    img_new = crop_top_left(img, 720, 720)
    img_new.save(out_path, quality=100)

    print("cropped", i)


print("Finish!!")