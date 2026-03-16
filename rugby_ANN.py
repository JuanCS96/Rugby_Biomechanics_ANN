
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import LSTM
import matplotlib.pyplot as plt

@tf.keras.utils.register_keras_serializable()
class LSTM_Compat(LSTM):
    def __init__(self, *args, **kwargs):
        kwargs.pop("time_major", None)
        super().__init__(*args, **kwargs)

model = load_model("rugby_model.keras", custom_objects={'LSTM': LSTM_Compat}, safe_mode=False, compile=False)

velData = pd.read_csv('velTestData.csv', header=None)
forceData = pd.read_csv('forceTestData.csv', header=None)

vels = velData.to_numpy().T
forces = forceData.to_numpy().T

x_test = vels.reshape(len(vels), len(vels[0]), 1)
y_test = forces.reshape(len(forces), len(vels[0]), 1)

pred_forces = model.predict(x_test)

for i in range(0, len(pred_forces)):
    plt.plot(pred_forces[i], color="blue")
    plt.plot(forces[i], color="red")
    plt.show()




