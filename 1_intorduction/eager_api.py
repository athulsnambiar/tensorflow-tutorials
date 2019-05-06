import numpy as np
import tensorflow as tf

print("Setting Eager mode...")
tf.enable_eager_execution()
print("eager execution turned on :", tf.executing_eagerly())