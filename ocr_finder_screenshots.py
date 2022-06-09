import matplotlib.pyplot as plt


import cv2
import easyocr
import re
import os
import time
import csv


def CorrectWord(word):
	a = []
	charac_of_word = list(word)
	len_of_word = len(charac_of_word)
	for i in range(0, int(0.8*len_of_word)):
		a.append(charac_of_word[i])
	b= ''.join(a)
	return b

def WordsinSentence(word,sentence):
    pattern = re.compile(word)
    found = re.findall(pattern,sentence.lower())

    if found:
        return True
    else:
        return False

def ParserEasyOCR(result, img, word, word1):
	fl = False
	for (bbox, text, prob) in result:
		if WordsinSentence(word, text) or WordsinSentence(word1, text):
			(tl, tr, br, bl) = bbox
			tl = (int(tl[0]), int(tl[1]))
			tr = (int(tr[0]), int(tr[1]))
			br = (int(br[0]), int(br[1]))
			bl = (int(bl[0]), int(bl[1]))

			cv2.rectangle(img, tl, br, (0, 255, 0), 2)
			fl = True

	return fl, img



def ReadImagesFromFolder(path_images, word, lang):

	word1 = CorrectWord(word)
	count1 = 0

	arr_id_images = []
	foundImgs = [] 

	reader = easyocr.Reader([lang], gpu=False)
	for name in os.listdir(path_images):
		name1 = os.path.join(path_images, name)
		img = cv2.imread(name1)
		# each item represents lists of text box coordinates [x,y], text and model confident level
		result = reader.readtext(img) 

		exist_img, img1 = ParserEasyOCR(result, img, word, word1) # true, false

		if exist_img:
			arr_id_images.append(name)
			foundImgs.append(img1)

		count1 += 1

	if arr_id_images:

		saveData(arr_id_images, foundImgs)


def saveData(arr_id_images, foundImgs):
	fig = plt.figure(figsize=(10, 10))
	rows, cols = 1, len(arr_id_images)

	for j in range(0, cols * rows):
		fig.add_subplot(rows, cols, j + 1)
		plt.imshow(foundImgs[j])
		plt.axis('off')
	plt.savefig("These screenshots have the word.png")

	# 2. Save id screenshots that contain the word
	f = open('./id_found_images.csv', 'w')
	writer = csv.writer(f)  # create the csv writer
	writer.writerow(arr_id_images)
	f.close()




if __name__ == "__main__":

	print("Word Language[en,ru] Path_to_images")
	word = input("Word ")
	lang = input("Language[en,ru]  ")
	path_images = input("Path_to_images  ")

	predict_time = 0
	before_time = time.time()
	ReadImagesFromFolder(path_images, word, lang)
	predict_time += time.time() - before_time
	print(predict_time)
