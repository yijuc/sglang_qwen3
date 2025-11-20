## Run Qwen3-Next-80B-A3B-Instruct-FP8 and Qwen3-Next-80B-A3B-Instruct
```bash
# qwen3_next.py plugin
cp /sgl-workspace/sglang/python/sglang/srt/models/qwen3_next.py /sgl-workspace/sglang/python/sglang/srt/models/qwen3_next.py.bk
cp qwen3_next.py /sgl-workspace/sglang/python/sglang/srt/models/qwen3_next.py
```

```bash
# kunlun benchmark python version conflict
pip install prettytable==3.9.0
```

```bash
# Run benchmark
## Run server
./run_server.sh
## Run client
./run_client.sh
```