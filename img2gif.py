import imageio

gif_images = []
for i in range(0, 500):
    gif_images.append(imageio.imread("./DSTA_TSP_python_version/picture/"+str(i)+".png"))   # 读取多张图片
imageio.mimsave("result.gif", gif_images)   # 转化为gif动画
