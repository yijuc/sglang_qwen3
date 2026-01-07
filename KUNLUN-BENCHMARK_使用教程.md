## 使用示例
### 大语言模型
当前示例使用vllm/vllm-openai:v0.6.4 镜像

阿里最新测试镜像: [https://sinian-metrics-platform.oss-cn-hangzhou.aliyuncs.com/home/hxn/vllm/vllm0.9.1.tar](https://sinian-metrics-platform.oss-cn-hangzhou.aliyuncs.com/home/hxn/vllm/vllm0.9.1.tar)

```shell
# 改镜像运行在5090 机器需要升级nccl
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt install libnccl2=2.26.2-1+cuda12.8 libnccl-dev=2.26.2-1+cuda12.8
```

1. 运行容器

```shell
docker run -it --gpus all --entrypoint=/bin/bash vllm/vllm-openai:v0.6.4，注意：该镜像要修改entrypoint
```

2. 安装Benchmark

```shell
# 查看环境信息
# OS: cat /etc/os-release
# Py: python3 -V
# 当前系统为 Ubuntu 22.04 / Python为 3.12

# 下载对应的安装包
# apt install wget
##### 下载链接获取: 可以找ali的同事获取, 需提供上一步获取环境信息
wget https://sinian-metrics-platform.oss-cn-hangzhou.aliyuncs.com/ai_perf/pack/kunlun_benchmark/main/ubuntu22.04/py3.12.0/kunlun-benchmark.tar.gz
# 解压
tar -zxf ./kunlun-benchmark.tar.gz
# 安装依赖
cd kunlun-benchmark
bash ./build.sh
```

3. 准备模型
    - 用户可以选择自己的模型
    - 本示例使用 Qwen/Qwen2.5-0.5B-Instruct

```shell
# modelscope 模型下载工具可以 pip安装
modelscope download Qwen/Qwen2.5-0.5B-Instruct --local_dir /model/Qwen2.5-0.5B-Instruct
```

4. 启动服务

```shell
# 可以更具设备自行添加其他参数 非必要情况不要开启缓存
python3 -m vllm.entrypoints.openai.api_server --port 30001 --model /model/Qwen2.5-0.5B-Instruct

# 服务运行起来的LOG
INFO 12-04 20:16:08 launcher.py:27] Route: /v1/embeddings, Methods: POST
INFO:     Started server process [156]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:30001 (Press CTRL+C to quit)
```

5. 执行测试

```shell
./kunlun-benchmark vllm server \
    --port 30001 \  # 端口要和启动的服务端口保持一致
    --work_mode manual \  # 如果要远程测试 work_mode 改为 platform 增加一个参数--url填写请求的url eg: https://www.xxx.com/v1/complations --port 可以不设置
    --max_input_len 1000 \
    --min_input_len 800 \
    --max_output_len 500 \
    --min_output_len 400  \
    --concurrency 20 \
    --query_num 200 \
    --result_dir /home/admin/work_dir/result/ \ 测试结果保存路径, 可自行指定
    --model_path /model/Qwen2.5-0.5B-Instruct \
    # 开启后回去自动调整并发 让结果decode/prefill 符合我们设置sla_decode/prfill
    # 如需要单独验证某一个并发的性能 可以设为False
    --is_sla True \ 
    --sla_decode 50 \
    --sla_prefill 3000  # 0 表示不作限制
```

6. 常用测试场景

| 输入 | 输出 | SLA标准(ms) |
| --- | --- | --- |
| 0.8-1k | 300-500 | decode:50 prefill: 3000 |
| 1.6-2k | 300-500 | decode:50 prefill: 3000 |
| 3-3.6k | 300-500 | decode:50 prefill: 3000 |
| 16-20k | 300-500 | decode:50 prefill: 不作限制 |
| 0.8-1k | 1.6-2k | decode:50 prefill: 3000 |
| 0.1-0.2k | 3.6-4k | decode:50 prefill: 3000 |


针对不同的测试场景 只需要在执行测试给的测试案例的命令基础上, 修改max/min_input/output_len 这四个参数即可



### 文生图模型
镜像: 一个可以运行diffusers的镜像

阿里最新测试镜像: [https://sinian-metrics-platform.oss-cn-hangzhou.aliyuncs.com/home/hxn/vllm/t2i.cu128.tar](https://sinian-metrics-platform.oss-cn-hangzhou.aliyuncs.com/home/hxn/vllm/t2i.cu128.tar)

1. 运行容器

和大语言模型一致

2. 安装Benchmark

和大语言模型一致

3. 准备模型
    - 本示例使用 [SDXL](https://www.modelscope.cn/models/AI-ModelScope/stable-diffusion-xl-base-1.0)
    - 下载方式和大语言模型一致
4. 启动服务

```shell
cd kunlun-benchmark
# 这里以nvidia的为例
CUDA_VISIBLE_DEVICES=0 python lit_web.py --model_path /path/to/model/sdxl 
```

5. 测试

```shell
# 测试需要用到指定的数据集 下载地址 https://huggingface.co/datasets/Gustavosta/Stable-Diffusion-Prompts
./kunlun_benchmark diffusers server --query_num 30 \
--model_path /path/to/model/sdxl \
--dataset_dir /fuzirui/Stable-Diffsion-Prompt \ # 设置为本地数据集路径
--num_inference_steps 20 \
--guidance_scale 7.0 \
--width 1024 --height 1024 \
--batch_size 2
```

6. 常用测试场景

| width/height | num_inference_steps | batch_size |
| --- | --- | --- |
| 1024 | 10/20 | 1/2 |
| 2048 | 10/20 | 1/2 |










