| Targets                                        |                  Values |
|:-----------------------------------------------|------------------------:|
| Framework                                      |                  sglang |
| Model Type (Tokenizer)                         |                     llm |
| Benchmark Scenario                             |          llm_completion |
| Concurrency                                    |                      78 |
| Total Benchmark Time                           |              273.5842 s |
| First Request Send Time                        | 2025_11_20_15_36_17.642 |
| Last Request Send Time                         | 2025_11_20_15_40_22.000 |
| Last Response Recv Time                        | 2025_11_20_15_40_34.000 |
| Time of All Requests Sent                      |              244.3578 s |
| Sum Time of All Requests Get Response          |            19261.1221 s |
| Expect Number of Sent Requests                 |                    3000 |
| Real Number of Sent Requests                   |                     780 |
| Percentage of Sent Requests (Real/Expect)      |                  26.00% |
| Success Requests                               |                     780 |
| Success Requests Percentage                    |                 100.00% |
| Queries Per Second(QPS)(All requests finished) |           3.0426 reqs/s |
| Time of All Prompts Released                   |                0.1461 s |
| Max Content Prompt Token Length                |                    1000 |
| Average Content Prompt Token Length            |                  896.83 |
| Max Output Token Length                        |                     499 |
| Average Output Token Length                    |                  447.00 |
| Generate Tokens                                |                  349439 |
| Total    Tokens                                |                 1048964 |
| Prefill  Tokens  Per Second(PTPS)              |      2862.7082 tokens/s |
| Generate Tokens  Per Second(GTPS)              |      1359.6848 tokens/s |
| Total    Tokens  Per Second(TPS)               |      4091.7972 tokens/s |
| Average  Request Time                          |           24693.7463 ms |
| Lowest   Request Time                          |           12136.4393 ms |
| Highest  Request Time                          |           31867.9924 ms |
| Average  Prefill Time (TTFT)                   |             330.2693 ms |
| Lowest   Prefill Time (TTFT)                   |             181.9625 ms |
| Highest  Prefill Time (TTFT)                   |             760.3953 ms |
| Average  Decode Time (TPOT)                    |              54.4969 ms |
| Lowest   Decode Time (TPOT)                    |              27.8892 ms |
| Highest  Decode Time (TPOT)                    |              63.6863 ms |
| Average  Inter-Token Latency (ITL)             |              54.4528 ms |
| Lowest   Inter-Token Latency (ITL)             |               0.0300 ms |
| Highest  Inter-Token Latency (ITL)             |             603.3518 ms |

| Finish Reason | Count |
|:--------------|------:|
| length        |   780 |
| None          |     0 |

| Targets         |       Request Time |       Prefill Time | Decode Time(excl. 1st token) | Inter-Token Latency |
|:----------------|-------------------:|-------------------:|-----------------------------:|--------------------:|
| effective items |                780 |                780 |                          780 |                 780 |
| tp_50           |  24940.93692302704 |  321.3973045349121 |             55.4782836120014 |   34.38997268676758 |
| tp_90           | 27785.810565948486 | 499.14150238037115 |           58.689902467097184 |  153.32622528076172 |
| tp_99           |  30754.83357429505 |   713.507742881775 |           61.674673120856745 |   291.4902782440185 |