# Book Recognition and Organization

This project tackles the issue of an unorganized personal library. It can be used by taking a picture of a book and running it through the code. The code then recognizes what the book is and describes the genre of the book as well as other helpful information.

![add image descrition here](direct image link here)

## The Algorithm

I based my code on the imagenet code we worked on earlier. The algorithm takes an image file, the model is then used to classify the image. The model processes the image and provides a description of the image as well as a confidence score. It then prints this description and score, which gives the user an easy way to classify their book covers.

## Running this project

1. Add steps for running this project.
2. Make sure to include any required libraries that need to be installed for your project to run.

1. Run the model using the following command. Note that you should not be in the docker. 
 imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt $DATASET/test/Biography/[fileName].jpg [resultFileName].jpg
2. Once the inference is done, you can fetch the file from the Jetson using scp. 


[View a video explanation here](video link)
