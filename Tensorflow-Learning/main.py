__author__ = "Marco Marson"
__version__ = "1.0"
__maintainer__ = "Marco Marson"
__email__ = "vollet.marson@gmail.com"
__status__ = "Development"

import tensorflow as tf




if __name__=='__main__':
    print(tf.test.is_built_with_cuda())
    print(tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None))