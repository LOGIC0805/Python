# PCA压缩图片

崔鹏宇 10185101165 数据科学与工程算法实践课项目一

### 项目内容

> 主成分分析（PCA）可用于减小矩阵（图像）的尺寸并投影这些新尺寸以重新形成保留其品质但k权重较小的图像。从给定数据集中的选择某个类别的100张图像，然后使用PCA压缩图像。最终输出图像压缩的性能，即节省空间、压缩率和重建错误。
> 
> Principal component analysis (PCA) can be used to reduce the size of the matrix (image) and project these new sizes to reform an image that retains its quality but has a smaller k weight. Select 100 images of a certain category from a given data set, and then use PCA to compress the images. The final output image compression performance, namely saving space, compression rate and reconstruction error.

### 注意事项

- 项目结构目录为本文件夹目录，数据集在Images文件夹下，输出在Images_total_result文件夹下
- 本项目选择agricultural类图片，共100张，编号00-99，即第一张图片是00号图片，输入和输出图片编号一致
- 对彩色图片的处理方法是分成R G B三个通道分解进行PCA降维，之后再合并投影
- 会打印每张图片的压缩性能和该类别下所有100张图片整体的压缩性能
