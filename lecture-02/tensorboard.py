# -*- coding: utf-8 -*-
import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)
writer = tf.summary.FileWriter('./graphs', tf.get_default_graph())
with tf.Session() as sess:
    print(sess.run(x))
writer.close()

# go to Terminal, run the program:
# $ python tensorboard.py
# $ tensorboard --logdir="./graphs" --port 6006
