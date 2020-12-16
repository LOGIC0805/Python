import numpy as np
from PIL import Image

def PCA(X, percent, X_mean):
    # 去中心化
    X_mat = X - X_mean
    # 计算协方差矩阵的特征值、特征向量
    X_vals, X_vects = np.linalg.eig(np.cov(X_mat))
    # 特征值排序
    X_vals_index = np.argsort(X_vals)[::-1]
    X_vals = X_vals[X_vals_index]
    X_vects = X_vects[:, X_vals_index]
    # 特征值个数选取
    X_vals_sum = np.sum(X_vals)
    X_vals_percent = X_vals_sum * percent
    X_vals_cnt = 0
    vals = 0
    for i in range(np.linalg.matrix_rank(X)):
        vals += X_vals[i]
        if vals > X_vals_percent:
            X_vals_cnt = i
            break
    X_vects = X_vects[:, range(X_vals_cnt)]
    # 投影
    X_new_mat = np.dot(X_vects.T, X_mat)
    # 重建图像
    # 归一化
    X_new = np.dot(X_vects, X_new_mat) + X_mean.T
    # 转化为图像合法取值
    X_new = np.uint8(np.absolute(X_new))
    # 定义压缩值、空间占有值、重构误差
    X_compress = np.size(X_vects) + np.size(X_new_mat)
    X_space = np.size(X)
    X_error = np.linalg.norm(X_new - X)
    return X_new, X_compress, X_space, X_error


if __name__ == '__main__':
    R_mean_total = np.zeros(256*256).reshape((256, 256))
    G_mean_total = np.zeros(256*256).reshape((256, 256))
    B_mean_total = np.zeros(256*256).reshape((256, 256))
    # 获取所有图片的均值
    imgtype = 'agricultural'
    for i in range(100):
        imgname = 'Images/' + imgtype + '/' + imgtype
        if i < 10:
            imgname += '0' + str(i) + '.tif'
        else:
            imgname += str(i) + '.tif'
        # 打开图片
        img = Image.open(imgname)
        # 转换为矩阵
        X = np.array(img)
        # 分成三个通道
        R = X[:, :, 0]
        G = X[:, :, 1]
        B = X[:, :, 2]
        R_mean_total += R
        G_mean_total += G
        B_mean_total += B
    R_mean_total /= 100
    G_mean_total /= 100
    B_mean_total /= 100

    total_sum_compress = 0
    total_sum_space = 0
    total_sum_error = 0
    for i in range(100):
        imgname = 'Images/' + imgtype + '/' + imgtype
        if i < 10:
            imgname += '0' + str(i) + '.tif'
        else:
            imgname += str(i) + '.tif'
        # 打开图片
        img = Image.open(imgname)
        # 转换为矩阵
        X = np.array(img)
        # 分成三个通道
        R = X[:, :, 0]
        G = X[:, :, 1]
        B = X[:, :, 2]
        # 调用PCA
        percent = 0.95
        sum_compress = 0
        sum_space = 0
        sum_error = 0
        R_new, R_compress, R_space, R_error = PCA(R, percent, R_mean_total)
        sum_compress += R_compress
        sum_space += R_space
        sum_error += R_error
        G_new, G_compress, G_space, G_error = PCA(G, percent, G_mean_total)
        sum_compress += G_compress
        sum_space += G_space
        sum_error += G_error
        B_new, B_compress, B_space, B_error = PCA(B, percent, B_mean_total)
        sum_compress += B_compress
        sum_space += B_space
        sum_error += B_error
        print('第' + str(i + 1) + '张图片节省空间: ', sum_space - sum_compress)
        print('第' + str(i + 1) + '张图片压缩率: ', sum_compress / sum_space)
        print('第' + str(i + 1) + '张图片重构误差: ', sum_compress / sum_space)
        total_sum_compress += sum_compress
        total_sum_space += sum_space
        total_sum_error += sum_error
        # 显示新图像
        imgname = 'Images_total_result/' + imgtype + '/' + imgtype
        if i < 10:
            imgname += '0' + str(i) + '.tif'
        else:
            imgname += str(i) + '.tif'
        X_new = np.dstack((R_new, G_new, B_new))
        img_new = Image.fromarray(X_new)
        img_new.save(imgname)
        # img_new.show()
    # 输出压缩图片性能
    print(imgtype + '类图片总节省空间: ', total_sum_space - total_sum_compress)
    print(imgtype + '类图片总压缩率: ', total_sum_compress / total_sum_space)
    print(imgtype + '类图片平均重构误差: ', total_sum_error / 100)
