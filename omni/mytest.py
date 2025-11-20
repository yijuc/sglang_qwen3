
import os
import torch
from transformers import Qwen3OmniMoeProcessor
import time

import sglang as sgl

os.environ['SGLANG_USE_AITER'] = '1'
#os.environ['HIP_VISIBLE_DEVICES'] = '6'
os.environ['SGLANG_TORCH_PROFILER_DIR']='/dockerx/sglang_qwen3/omni/profile_log'

def gen(llm, text, audio, image, sampling_params):
    ttft = 0
    st = time.perf_counter()
    generated_text = ''
    for output in llm.generate(prompt=text,
                               image_data=image,
                               audio_data=audio,
                               sampling_params=sampling_params,
                               stream=True):
        timestamp = time.perf_counter()
        if ttft == 0:
            ttft = timestamp - st
    latency = time.perf_counter() - st
    generated_text = output['text']
    
    return ttft, latency, generated_text, output['meta_info']['completion_tokens']

if __name__ == '__main__':

    text = '\nAnalyze this audio and generate a reasoning chain to deduce the content of the audio. The specific steps are as follows:\n\n1. Generate a reasoning chain for the description of the audio:\n* Determine which type the audio belongs to (Music / Sound / Speech / Song). The distinction between speech and sound is whether or not it contains intelligible human voice content. The difference between music and a song lies in that a song contains vocal content, while music does not.\n* If the audio is **Speech**, then analyze the following aspects of the audio: (1) Spoken Language Characteristic, including language, number of speakers, speaker gender, speaker emotion, and sentiment; (2) Speech Transcript, which refers to the textual content of the speech; (3) Sound Caption, which is a description of this audio, with particular emphasis on describing the background sounds of the speech.\n* If the audio is **Music**, then analyze the following aspects of the audio: (1) Music Reasoning, including Genre and Style, Mood and Expression; (2) Music Knowledge, including types of instruments, sound texture, melody and rhythm, harmony, and chords; (3) Historical and Cultural Context, which involves analyzing the style of the audio, its background, and information about the author\'s style.\n* If the audio is **Sound**, then analyze the following aspects of the audio: (1) Acoustic Sounds analysis, which means analyzing the conditions of the audio, such as weather phenomena, wild environments, non-verbal vocalizations etc.; (2) Acoustic Scene Reasoning, which involves describing the scene of the sound and inferring the sound events and activities reflected by the related audio; (3) Sound-Based Event Reasoning, which involves describing repeated sounds, fixed frequency sounds, and regular sound phenomena. \n* If the audio is **Song**, then analyze the following aspects of the audio: (1) Song Reasoning, including Genre and Style, Mood and Expression, a summary of the lyrics, specific lyrics; (2) Song Knowledge, including types of instruments, sound texture, melody and rhythm, harmony, and chords; (3) Historical and Cultural Context, which involves analyzing the style of the audio, its background, and information about the author\'s style.\n\n2. Please integrate all of the above results in JSON format. Below is a sample:\n```json\n{{\n    "type": "",\n    "content_dict": {{ // follow the various items for different types\n    //...\n    }}\n}}\n'
    image = "/dockerx/sglang_qwen3/omni/1280x853.jpg"
    audio = "/dockerx/sglang_qwen3/omni/caption2.mp3"

    MODEL_PATH = "/SHARE/Qwen3-Omni-30B-A3B-Instruct/"

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "audio", 
                    "audio": audio
                },
                {
                    "text": 'Hi ' * (24 * 1024), # text,
                    "type": "text",
                },
            ], 
        }
    ]
    image_num = 20
    messages[0]['content'] += [{"type": "image", "image": image} for _ in range(image_num)]
    processor = Qwen3OmniMoeProcessor.from_pretrained(MODEL_PATH)

    text_template = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    audios = [audio]
    images = [image] * image_num

    # https://docs.sglang.ai/basic_usage/offline_engine_api.html
    llm = sgl.Engine(model_path=MODEL_PATH,
                     #disable_cuda_graph=True,
                     #disable_radix_cache=True,
                     mm_attention_backend="triton_attn")
    sampling_params = {"temperature": 0.001,
                       #"top_p": 0.95,
                       "max_new_tokens": 300}
    # warmup
    ttft, latency, gen_text, gen_len = gen(llm, text_template, audios, images, sampling_params)
    print(f'warmup={latency:.2f}s, ttft={ttft:.2f}s, tpots={(latency-ttft)/(gen_len-1)*1000:.2f}ms, {gen_len=}')

    if 0:
        llm.flush_cache()
        llm.start_profile()
        ttft, latency, gen_text, gen_len = gen(llm, text_template, audios, images, sampling_params)
        llm.stop_profile()
        print(f'profile={latency:.2f}s, ttft={ttft:.2f}s, tpots={(latency-ttft)/(gen_len-1)*1000:.2f}ms, {gen_len=}')
    else:
        for i in range(10):
            llm.flush_cache()
            ttft, latency, gen_text, gen_len = gen(llm, text_template, audios, images, sampling_params)
            print(f'e2e[{i}]={latency:.2f}s, ttft={ttft:.2f}s, tpots={(latency-ttft)/(gen_len-1)*1000:.2f}ms, {gen_len=}')

    print("===============================")
    print(f"Generated text: {gen_text}")
    llm.shutdown()
