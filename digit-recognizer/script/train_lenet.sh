#!/usr/bin/env sh

caffe train --solver=lenet_solver.prototxt --gpu=1
#caffe train --solver=lenet_solver_adam.prototxt --gpu=1
