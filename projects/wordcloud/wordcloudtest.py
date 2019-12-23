import wordcloud
from scipy.misc import imread
mask = imread("heart.jpg")
f = open("wordcloud.txt", "r")
t = f.read()
f.close()
w = wordcloud.WordCloud( font_path="msyh.ttc", mask = mask, width=1000, height=700, background_color="white")
w.generate(t)
w.to_file("grwordcloud.jpg")
