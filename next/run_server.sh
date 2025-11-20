#!/bin/bash

## Model Path
export MODEL_DIR="/SHARE" # hjbog-1
# export MODEL_DIR="/mnt/md0/models" # hjbog-2

## Env
unset HIP_VISIBLE_DEVICES
export HIP_VISIBLE_DEVICES=4,5,6,7
export SGLANG_USE_AITER=1

# model="Qwen3-Next-80B-A3B-Instruct-FP8" # FP8
model="Qwen3-Next-80B-A3B-Instruct" # FP16

# FP8
if [[ "$model" == *"FP8"* ]]; then
    cuda_graph_max_bs=128
    port=30001
# FP16
else
    cuda_graph_max_bs=256
    port=30002
fi
TP=4
EP=1

echo "launching ${model}"
echo "TP=${TP}"
echo "EP=${EP}"

python3 -m sglang.launch_server \
 --model-path $MODEL_DIR/$model \
 --host localhost \
 --port $port \
 --tp-size ${TP} \
 --ep-size ${EP} \
 --trust-remote-code \
 --chunked-prefill-size 32768 \
 --mem-fraction-static 0.85 \
 --disable-radix-cache \
 --max-prefill-tokens 32768 \
 --cuda-graph-max-bs $cuda_graph_max_bs \
 --max-running-requests 128 \
 --page-size 64 \
 --attention-backend triton \