from PIL import Image
im=Image.open('google.jpg')
# print(type(im),im)
#提取RGB的颜色通道
r,g,b=im.split()
# print(r)
# print(g)
# print(b)
om=Image.merge('RGB',(g,b,r))
om.save('new_google.jpg')