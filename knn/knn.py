import tensorflow as tf
import numpy as np

def load_mnist_data(filename,isbatch=0,train_nums=1000,test_nums=200):
    from tensorflow.examples.tutorials.mnist import input_data
    mnist = input_data.read_data_sets(filename, one_hot=True)
       #2、批量获取样本
    if isbatch==1:
        X_train,Y_train = mnist.train.next_batch(train_nums)
        X_test,Y_test = mnist.test.next_batch(test_nums)
        return X_train,Y_train,X_test,Y_test
    else:
        #1、获取全部样本
        X_train = mnist.train.images[0:60000]   #[1:10]
        X_test = mnist.test.images[0:1000] 
        Y_train = mnist.train.labels[0:60000] 
        Y_test = mnist.test.labels[0:1000] 
        return X_train,Y_train,X_test,Y_test

def KNN_Classifier(X_train,Y_train,X_test,Y_test,K=5,dims=784,dist_metric='L1'):
    # 计算图输入占位符
    xs = tf.placeholder(tf.float32,[None,dims])
    xst  = tf.placeholder(tf.float32,[dims])  
    # 使用 L1 距离进行最近邻计算
    # L1：dist = sum(|X1-X2|)  或 L2：dist=sqrt(sum(|X1-X2|^2))
    dist = tf.reduce_sum(tf.abs(tf.add(xs,tf.negative(xst))),
                         reduction_indices=1)
    #或dist = tf.reduce_sum(tf.abs(tf.subtract(xtrain, xtest))), axis=1)

    # 预测: 获得前K个最小距离的索引，用于与正确标签比较
    #index = tf.arg_min(dist,0)
    if K is None:
        dim = tf.size(tf.shape(dist))   #矩阵元素的个数
        if dim==1:
            K = tf.shape(dist)[0]
        elif dim==2:
            K = tf.shape(dist)[1]
        else:
            K = tf.shape(dist)[-1]
    # 从小到大排序，取前K个最小的
    value,index = tf.nn.top_k(-dist,k=K)
    value = -value


    # 初始化所有变量
    init = tf.global_variables_initializer()    

    #定义一个正确率计算器
    Accuracy = 0 

    #执行会话
    with tf.Session() as sess:
        sess.run(init) 
        # 只能循环地对测试样本进行预测
        for i in range(len(X_test)):    
            idx = sess.run(index,feed_dict={xs:X_train,xst:X_test[i,:]})

            # 计算预测标签和正确标签用于比较
            Klabels = np.argmax(Y_train[idx],axis=1)   #统计K行01标签中为1的下标
            Predict_label = np.argmax(np.bincount(Klabels)) #统计下标数组中出现次数最多的值
            #print(Y_train[idx],'\n',Klabels,'\n',Predict_label)

            True_label = np.argmax(Y_test[i])

            print("Test Sample",i,"Prediction label:",Predict_label,
                  "True Class label:",True_label)

            # 计算精确度
            if Predict_label == True_label:
                Accuracy +=1
        print("Accuracy=",Accuracy/len(X_test))    

    return Accuracy    

if __name__ == '__main__':  
    X_train,Y_train,X_test,Y_test = load_mnist_data("MNIST_data",isbatch=0,train_nums=1000,test_nums=200)    
    Accuracy =  KNN_Classifier(X_train,Y_train,X_test,Y_test,K=5,dims=784,dist_metric='L1') 
