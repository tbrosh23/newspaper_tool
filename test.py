import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

cifar10 = tf.keras.datasets.cifar10
(tdata, tlabels), (vdata, vlabels) = cifar10.load_data()