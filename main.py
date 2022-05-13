from rock_paper_scissors import  full_process



if __name__ == '__main__':
    import tensorflow as tf

    if tf.test.gpu_device_name():
        print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
    else:
        print("Please install GPU version of TF")

    full_process()


