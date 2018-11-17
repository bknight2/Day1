import tensorflow as tf

a = tf.placeholder("float")                 # float a = 3.0f
b = tf.placeholder("float")                 # float b = 3.0f
c = tf.multiply(a, b)
sess = tf.Session()                         # 생성자, class
print(sess.run(c, feed_dict={a:3, b:3}))
