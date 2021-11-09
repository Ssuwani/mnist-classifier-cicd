import tensorflow as tf
import argparse
from utils import trigger_dispatch


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ACCESS_TOKEN",
        type=str,
        required=True,
        help="Github Access Token for trigger 'cd' vai dispatch",
    )
    parser.add_argument(
        "--num_neurons",
        type=int,
        required=True,
        help="number of units in last hidden layer",
    )
    parser.add_argument(
        "--learning_rate", type=float, required=True, help="learning rate"
    )
    parser.add_argument(
        "--output_model_path",
        type=str,
        required=True,
        help="Model output path ex) 'gs://suwan/mnist_saved_model'",
    )
    args = parser.parse_args()
    return args


def training(num_neurons, learning_rate, output_model_path):
    mnist = tf.keras.datasets.mnist
    (train_x, train_y), (test_x, test_y) = mnist.load_data()
    train_x = train_x / 255.0
    test_x = test_x / 255.0

    model = tf.keras.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(num_neurons, activation="relu"),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )
    model.compile(
        loss="sparse_categorical_crossentropy",
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        metrics=["acc"],
    )

    model.fit(train_x, train_y, epochs=10)

    loss, acc = model.evaluate(test_x, test_y)
    print(f"model loss: {loss:.4f} acc: {acc*100:.4f}")

    print("demo")

    model.save(output_model_path)

    trigger_dispatch(args.ACCESS_TOKEN)


if __name__ == "__main__":
    args = get_args()
    training(args.num_neurons, args.learning_rate, args.output_model_path)
