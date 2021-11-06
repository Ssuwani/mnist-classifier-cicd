from tensorflow.keras.models import load_model
from bento_service import MnistService


model = load_model("gs://suwan/mnist_model_demo2/")

mnist_svc = MnistService()
mnist_svc.pack('model', model)

saved_path = mnist_svc.save()
print(f"saved_path : {saved_path}")

