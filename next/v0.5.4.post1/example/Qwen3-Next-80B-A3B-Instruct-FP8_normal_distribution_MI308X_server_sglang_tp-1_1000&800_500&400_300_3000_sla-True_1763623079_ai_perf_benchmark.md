| Targets                                        |                  Values |
|:-----------------------------------------------|------------------------:|
| Framework                                      |                  sglang |
| Model Type (Tokenizer)                         |                     llm |
| Benchmark Scenario                             |          llm_completion |
| Concurrency                                    |                      45 |
| Total Benchmark Time                           |              242.2475 s |
| First Request Send Time                        | 2025_11_20_15_45_08.468 |
| Last Request Send Time                         | 2025_11_20_15_48_41.000 |
| Last Response Recv Time                        | 2025_11_20_15_48_54.000 |
| Time of All Requests Sent                      |              212.5317 s |
| Sum Time of All Requests Get Response          |             9781.1176 s |
| Expect Number of Sent Requests                 |                    3000 |
| Real Number of Sent Requests                   |                     450 |
| Percentage of Sent Requests (Real/Expect)      |                  15.00% |
| Success Requests                               |                     450 |
| Success Requests Percentage                    |                 100.00% |
| Queries Per Second(QPS)(All requests finished) |           1.9953 reqs/s |
| Time of All Prompts Released                   |                0.0663 s |
| Max Content Prompt Token Length                |                     997 |
| Average Content Prompt Token Length            |                  897.67 |
| Max Output Token Length                        |                     499 |
| Average Output Token Length                    |                  447.39 |
| Generate Tokens                                |                  201776 |
| Total    Tokens                                |                  605728 |
| Prefill  Tokens  Per Second(PTPS)              |      1900.6669 tokens/s |
| Generate Tokens  Per Second(GTPS)              |       895.4583 tokens/s |
| Total    Tokens  Per Second(TPS)               |      2685.7775 tokens/s |
| Average  Request Time                          |           21735.8169 ms |
| Lowest   Request Time                          |           13573.2937 ms |
| Highest  Request Time                          |           26590.8680 ms |
| Average  Prefill Time (TTFT)                   |             294.0364 ms |
| Lowest   Prefill Time (TTFT)                   |             194.5348 ms |
| Highest  Prefill Time (TTFT)                   |             714.3836 ms |
| Average  Decode Time (TPOT)                    |              47.9655 ms |
| Lowest   Decode Time (TPOT)                    |              28.1992 ms |
| Highest  Decode Time (TPOT)                    |              53.9964 ms |
| Average  Inter-Token Latency (ITL)             |              47.9080 ms |
| Lowest   Inter-Token Latency (ITL)             |              17.5278 ms |
| Highest  Inter-Token Latency (ITL)             |             637.1319 ms |

| Finish Reason | Count |
|:--------------|------:|
| length        |   450 |
| None          |     0 |

| Targets         |      Request Time |       Prefill Time | Decode Time(excl. 1st token) | Inter-Token Latency |
|:----------------|------------------:|-------------------:|-----------------------------:|--------------------:|
| effective items |               450 |                450 |                          450 |                 450 |
| tp_50           | 21978.27672958374 |  259.7622871398926 |            48.61038632434831 |  34.059762954711914 |
| tp_90           | 24057.65302181244 | 422.70169258117676 |            50.83424718700952 |   46.45004272460947 |
| tp_99           | 25649.76413011551 |  582.2673583030701 |            52.23415989722559 |  227.80798673629764 |