#!/bin/bash
set -x

convert=/home/resys/var/caffe/bin/convert_imageset
caffe=/home/resys/var/caffe/bin/caffe
compute_image_mean=/home/resys/var/caffe/bin/compute_image_mean
model_dir=/data/resys/xuqiang/dogs-vs-cats/model
classification=/home/resys/var/caffe/bin/classification 

python file_list.py

rm -fr data/train_lmdb data/valid_lmdb
${convert}  --resize_height=227 --resize_width=227 data/train/ data/train_list.txt data/train_lmdb
${convert}  --resize_height=227 --resize_width=227 data/train/ data/valid_list.txt data/valid_lmdb

${compute_image_mean} data/train_lmdb/ data/mean.binaryproto
${caffe} train --gpu=1 --solver=${model_dir}/solver.prototxt \
	--weights ${model_dir}/bvlc_reference_caffenet.caffemodel 2>&1 | tee train.log

# predict
./classification  model/deploy.prototxt \
	model/_iter_200.caffemodel  \
	./data/mean.binaryproto \
	./labels.txt \
	./data/test_list.txt | tee result.txt
