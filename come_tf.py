# coding=utf-8
import tensorflow as tf
# tf对数据类型要求比python高许多，就要定义 清楚才行
v_one = tf.Variable(3)
# 这个是变量
c_two = tf.constant([1, 2])
# 这个里面还可以加字符串，字符串 只有加法 运算，就是拼接
print(c_two)
# 这个是常量，而且 这个变量必须要给值，不行的话就给placeholder并且给出类型,这个也可以给多维矩阵
input1 = tf.placeholder(tf.int32)
input2 = tf.placeholder(tf.int32)
print(v_one)
# tf里面的都是张量，可以打印出来看看
# tf读多维的从外往里面 读，然后shape显示是从左到右

output = tf.matmul(input1, input2)
# 两个tensor叉乘，tensorflow里面一切都是tensor
# 叉乘是行乘列
# 矩阵有叉乘和点乘两种
# 点乘就是对应位置相乘 ，要求两个矩阵必须大小相同
sess = tf.Session()
# 加入会话之后才会 开始运算
# print(sess.run(v_one.initializer.run()))

rst = sess.run(output, feed_dict={input1:[[1, 2]], input2:[[3], [1]]})
print(rst)
# 这样子就能显示出来结果5
# sess.close()
# 或者用with来打开session,不关也无所谓了
# g = tf.Graph()
# # 这个就是图，只认识图里面的数据，不认识图外面的数据，当然图外面也不认识图里面的数据
# with g.as_default():
#     sess = tf.Session()
#     print(sess.run(v_one))
# #     这个是会报错显示不出来的

sess.run(tf.global_variables_initializer())
print(sess.run(v_one))
# 这个就不会显示shape这些了，只显示数值
