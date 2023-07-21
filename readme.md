# Book Recognition and Organization

This project tackles the issue of an unorganized personal library. It can be used by taking a picture of a book and running it through the code. The code then recognizes what the book is and describes the genre of the book as well as other helpful information.

![add image descrition here](direct image link here)

## The Algorithm

I based my code on the imagenet code we worked on earlier. The algorithm takes an image file, the model is then used to classify the image. The model processes the image and provides a description of the image as well as a confidence score. It then prints this description and score, which gives the user an easy way to classify their book covers.

## Running this project
  
1. Sync the github project at https://github.com/tarajiang/nvidia_project/. (You will need to have the jetson inference libraries properly set up.)
2. Navigagte to the project in your terminal.
3. In the root of the project there is a python script named project.py. Run the model using the following command. Note that you can change the output filename, and which file you want to test the model with.: 
```bash
python3 project.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt --output_filename=output.jpg $DATASET/test/Biography/testfile.jpg
```
4. Use SCP to download the output

### Windows:

```scp <nanousername>@192.168.55.1:/home/<nanousername>/<pathToSyncedProject>/<pathToTestFile C:\Users\<hostusername>\Desktop```

### Mac:
```scp <nanousername>@192.168.55.1:/home/<nanousername>/<pathToSyncedProject>/<pathToTestFile> ./```

[View a video explanation here](video link)
