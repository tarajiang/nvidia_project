import sys
import argparse
import logging  

from jetson_inference import imageNet
from jetson_utils import loadImage, saveImage, cudaFont

logging.basicConfig(level=logging.DEBUG)  

parser = argparse.ArgumentParser(description="Classify an image using an image recognition DNN.") 

parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--model", type=str, default="resnet18.onnx", help="model to use")
parser.add_argument("--input_blob", type=str, default="input_0", help="input blob name")
parser.add_argument("--output_blob", type=str, default="output_0", help="output blob name")
parser.add_argument("--labels", type=str, default="labels.txt", help="path to the labels file")
parser.add_argument("--output_filename", type=str, default="output.jpg", help="filename of the output image")

args = parser.parse_known_args()[0]

net = imageNet(model=args.model, labels=args.labels, input_blob=args.input_blob, output_blob=args.output_blob, argv=sys.argv)
img = loadImage(args.filename)

class_idx, confidence = net.Classify(img)
class_desc = net.GetClassDesc(class_idx)

font = cudaFont()
font.OverlayText(img, text=f"{class_desc} {confidence * 100.0:.2f}%", x=5, y=5, color=font.White, background=font.Gray40)

saveImage(args.output_filename, img)

print(f"Image is recognized as '{class_desc}' (class #{class_idx}) with {confidence * 100:.2f}% confidence")
print(f"Output image saved to {args.output_filename}")
