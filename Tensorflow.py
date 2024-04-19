import sys
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

a = tf.Variable([[1,2],[3,4]], name='a')
b = tf.Variable([[5,6],[7,8]] , name='b')

f = a + b
init = tf.global_variables_initializer()

with tf.Session() as s:
    init.run()
    print(f.eval())