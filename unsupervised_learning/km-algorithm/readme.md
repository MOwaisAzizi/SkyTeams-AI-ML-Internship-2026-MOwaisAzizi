K-Means algorithm

One of the main ways to reduce the size of an image is to reduce the number of pixels in the image, which makes the image lower quality.

Is there another way to reduce the image size without reducing its quality?

Yes, one way is using the K-Means algorithm, which is one of the clustering algorithms in machine learning. This algorithm reduces the number of bits used for colors, which helps reduce the image size.


These days, I was working on a practical project to learn the K-Means algorithm deeply, and the goal of the project was to take an image made up of hundreds of colors and thousands of pixels, break it down into pixels, and rebuild the image using the K-Means algorithm and only 16 colors to color the pixels again, in a way that both reduces its size and keeps the image quality the same as the original image.


The images you see have not lost their quality at all. However, in the top image, the original image has many colors (hundreds of different colors), so the model could not rebuild the compressed image using only 16 colors while keeping exactly the same colors as the original image. But in the bottom image, because fewer colors are used in the original image, the algorithm was able to rebuild the image very well using the 16 available colors, with almost 6 times smaller size and without reducing the image quality.

This can be done using the K-Means algorithm. Each pixel gets its color from the closest color among the 16 colors selected by the K-Means algorithm. Therefore, the image can be rebuilt well using fewer colors and with a smaller file size. This reduction in size is possible because fewer bits are used for the colors in the image.


As a result, using this model, not only was the image rebuilt with the same quality as the original image, with the same number of pixels and without reducing its quality, but the size of the new image was also reduced by almost 6 times compared to the original image.


This algorithm has different uses, but it is not used very often for image compression (when many different colors are used in the image) because of the small changes it makes to the colors of the image pixels. However, it can be used to reduce the size of images with simple colors and icons.