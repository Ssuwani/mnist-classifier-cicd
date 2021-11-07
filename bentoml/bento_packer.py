from tensorflow.keras.models import load_model
from bento_service import MnistService
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--model_path", required=True, type=str)
args = parser.parse_args()

model = load_model(args.model_path)

mnist_svc = MnistService()
mnist_svc.pack("model", model)

saved_path = mnist_svc.save()
print(f"saved_path : {saved_path}")
