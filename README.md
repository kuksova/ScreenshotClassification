# ScreenshotFinderbyText
Screenshot Finder by Text (SFT) is an efficient utility for finding screenshots that contain specific text is using EasyOCR library. 

SFT takes word, language and path to the folder with screenshots as input and returns all find screenshots with the found text highlighted and .csv file with name of found screenshots. 
You can search by word, part of word or word combination and multiple languages are supported.

# Usage 
Run ocr_finder_screenshots.py 
```
$ python ocr_finder_screenshots.py word language path_to_images
```

# Update March 2023 
Organization by keywords, create the folder of images of each keyword. 

# How does it work? 
![image](https://user-images.githubusercontent.com/14224692/228294774-cc2f5722-c828-40ce-9121-4d541da88a87.png)

# Update June 2023 
Time and accuracy. 

1)I used EasyOCR engine for inference, no additional image processing. The extracted text are quite accurately. It's imressive! 
But inference time: (7 images) - 55 sec(gpu), 98 sec(cpu). So it means if I want to run the whole folder (435 images), it will take almost 1 hour! 
But at least this is should be done only once. Then I need search for images in the Json file. 

2)I used pytesseract for inference. It works so badly for my images! I knew that it works when to preprocess the image to get the foreground text in black with the background in white.
But my images can't be processed like this. But inference time is impressive (9 sec/ 7 images). 

Conclusions: So I will keep with CRAFT algorithms and easyOCR + GPUs.  
      




