#!/bin/bash
unset HIP_VISIBLE_DEVICES
export HIP_VISIBLE_DEVICES=4,5,6,7
## Model Path
MODEL_DIR="/SHARE"
RESULT_DIR="/dockerx/sglang_qwen3/next"
KUNLUN_DIR="/dockerx/sglang_qwen3/kunlun-benchmark"

# model="Qwen3-Next-80B-A3B-Instruct-FP8" # FP8
model="Qwen3-Next-80B-A3B-Instruct" # FP16

# FP8
if [[ "$model" == *"FP8"* ]]; then
    port=30001
# FP16
else
    port=30002
fi

max_concurrency=300
num_prompts=$((10 * max_concurrency))

${KUNLUN_DIR}/kunlun-benchmark sglang server \
 --port $port \
 --work_mode manual \
 --max_input_len 1000 \
 --min_input_len 800 \
 --max_output_len 500 \
 --min_output_len 400 \
 --concurrency ${max_concurrency} \
 --query_num ${num_prompts} \
 --result_dir $RESULT_DIR \
 --model_path $MODEL_DIR/$model \
 --is_sla True \
 --sla_decode 50 \