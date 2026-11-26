## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-fed-net-11 | 16.7.7 | 5,480 | 5,495 | 5,465 | 0.2% | 376 MB | 70.3 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.21 | 5,443 | 5,471 | 5,428 | 0.3% | 348 MB | 65.5 KB |  |
| fusion-net-11 | 16.7.7 | 5,415 | 5,441 | 5,410 | 0.2% | 370 MB | 69.9 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.21 | 5,379 | 5,395 | 5,362 | 0.2% | 100 MB | 19.1 KB |  |
| fusion-aot-11 | 16.7.7 | 5,350 | 5,381 | 5,324 | 0.4% | 130 MB | 24.9 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.21 | 5,339 | 5,393 | 5,326 | 0.6% | 350 MB | 67.0 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.21 | 5,337 | 5,361 | 5,335 | 0.2% | 102 MB | 19.5 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 5,241 | 5,281 | 5,229 | 0.5% | 125 MB | 24.4 KB |  |
| feddi-gateway | 2026-11-22-1912 | 5,142 | 5,151 | 5,136 | 0.1% | 2,333 MB | 464.5 KB |  |
| hive-router-nightly | v0.3.20-nightly.2b115870 | 4,549 | 4,579 | 4,505 | 0.7% | 92 MB | 20.7 KB |  |
| hive-router | v0.3.17 | 4,492 | 4,508 | 4,481 | 0.2% | 93 MB | 21.3 KB |  |
| grafbase | 0.53.5 | 1,899 | 1,902 | 1,889 | 0.3% | 109 MB | 59.0 KB |  |
| caliban | 3.2.1 | 1,507 | 1,530 | 1,504 | 0.7% | 6,639 MB | 4,511.4 KB |  |
| cosmo | 0.373.0 | 1,495 | 1,499 | 1,495 | 0.1% | 167 MB | 114.2 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 611 | 612 | 607 | 0.3% | 2,610 MB | 4,374.2 KB |  |
| apollo-router | v2.19.1 | 534 | 534 | 533 | 0.1% | 173 MB | 332.1 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.36cc3633 | 515 | 516 | 514 | 0.2% | 192 MB | 382.1 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 402 | 402 | 401 | 0.1% | 199 MB | 506.0 KB |  |
| hive-gateway | 2.15.10 | 302 | 303 | 300 | 0.4% | 3,220 MB | 10,919.0 KB |  |
| apollo-gateway | 2.14.4 | 275 | 275 | 274 | 0.2% | 2,152 MB | 8,013.6 KB |  |


### Details

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1974510     ✗ 0     
     data_received..................: 58 GB   480 MB/s
     data_sent......................: 791 MB  6.6 MB/s
     http_req_blocked...............: avg=2.72µs  min=771ns    med=1.91µs  max=9.29ms   p(90)=3.05µs  p(95)=3.68µs   p(99.9)=28.61µs
     http_req_connecting............: avg=337ns   min=0s       med=0s      max=9.15ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.91ms  min=790.45µs med=7.98ms  max=246.38ms p(90)=14.29ms p(95)=17.43ms  p(99.9)=29.98ms
       { expected_response:true }...: avg=8.91ms  min=790.45µs med=7.98ms  max=246.38ms p(90)=14.29ms p(95)=17.43ms  p(99.9)=29.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 658270
     http_req_receiving.............: avg=92.74µs min=25µs     med=46.07µs max=172.64ms p(90)=87.44µs p(95)=186.95µs p(99.9)=6.22ms 
     http_req_sending...............: avg=42.41µs min=3.91µs   med=7.97µs  max=182.94ms p(90)=13.7µs  p(95)=98.35µs  p(99.9)=4.96ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.77ms  min=739.15µs med=7.87ms  max=244.8ms  p(90)=14.06ms p(95)=17.15ms  p(99.9)=29.47ms
     http_reqs......................: 658270  5480.744883/s
     iteration_duration.............: avg=9.1ms   min=1.12ms   med=8.16ms  max=285.18ms p(90)=14.49ms p(95)=17.65ms  p(99.9)=30.28ms
     iterations.....................: 658170  5479.912285/s
     success_rate...................: 100.00% ✓ 658170      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1961037     ✗ 0     
     data_received..................: 57 GB   476 MB/s
     data_sent......................: 786 MB  6.5 MB/s
     http_req_blocked...............: avg=2.94µs  min=931ns    med=2.3µs   max=8.08ms   p(90)=3.48µs  p(95)=4.11µs   p(99.9)=33.38µs
     http_req_connecting............: avg=151ns   min=0s       med=0s      max=3.72ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.97ms  min=785.58µs med=7.98ms  max=292.23ms p(90)=14.59ms p(95)=18ms     p(99.9)=30.9ms 
       { expected_response:true }...: avg=8.97ms  min=785.58µs med=7.98ms  max=292.23ms p(90)=14.59ms p(95)=18ms     p(99.9)=30.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 653779
     http_req_receiving.............: avg=96.65µs min=25.72µs  med=47.22µs max=71.37ms  p(90)=88.62µs p(95)=194.1µs  p(99.9)=6.34ms 
     http_req_sending...............: avg=43.42µs min=4.34µs   med=8.3µs   max=153.54ms p(90)=13.95µs p(95)=101.38µs p(99.9)=4.98ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.83ms  min=725.91µs med=7.87ms  max=291.73ms p(90)=14.35ms p(95)=17.7ms   p(99.9)=30.41ms
     http_reqs......................: 653779  5443.320407/s
     iteration_duration.............: avg=9.16ms  min=959.93µs med=8.17ms  max=302.67ms p(90)=14.81ms p(95)=18.22ms  p(99.9)=31.22ms
     iterations.....................: 653679  5442.487814/s
     success_rate...................: 100.00% ✓ 653679      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1951128     ✗ 0     
     data_received..................: 57 GB   474 MB/s
     data_sent......................: 782 MB  6.5 MB/s
     http_req_blocked...............: avg=2.53µs  min=771ns    med=1.94µs  max=5.84ms   p(90)=3.07µs  p(95)=3.67µs   p(99.9)=27.73µs
     http_req_connecting............: avg=141ns   min=0s       med=0s      max=4.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.02ms  min=798.07µs med=8.08ms  max=269.91ms p(90)=14.53ms p(95)=17.76ms  p(99.9)=30.48ms
       { expected_response:true }...: avg=9.02ms  min=798.07µs med=8.08ms  max=269.91ms p(90)=14.53ms p(95)=17.76ms  p(99.9)=30.48ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 650476
     http_req_receiving.............: avg=93.85µs min=25.67µs  med=46.22µs max=119.79ms p(90)=88.25µs p(95)=189.55µs p(99.9)=6.12ms 
     http_req_sending...............: avg=41.88µs min=4.23µs   med=8.04µs  max=113.47ms p(90)=13.65µs p(95)=99.87µs  p(99.9)=4.69ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.88ms  min=750.76µs med=7.97ms  max=269.36ms p(90)=14.3ms  p(95)=17.5ms   p(99.9)=30.06ms
     http_reqs......................: 650476  5415.784309/s
     iteration_duration.............: avg=9.21ms  min=953.34µs med=8.26ms  max=284.64ms p(90)=14.73ms p(95)=17.98ms  p(99.9)=30.77ms
     iterations.....................: 650376  5414.951722/s
     success_rate...................: 100.00% ✓ 650376      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1938102     ✗ 0     
     data_received..................: 57 GB   471 MB/s
     data_sent......................: 777 MB  6.5 MB/s
     http_req_blocked...............: avg=4.87µs  min=812ns    med=1.9µs   max=198.1ms  p(90)=3.05µs  p(95)=3.66µs   p(99.9)=28.92µs
     http_req_connecting............: avg=2.43µs  min=0s       med=0s      max=197.97ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.08ms  min=811.9µs  med=8.18ms  max=249.5ms  p(90)=14.54ms p(95)=17.62ms  p(99.9)=30.06ms
       { expected_response:true }...: avg=9.08ms  min=811.9µs  med=8.18ms  max=249.5ms  p(90)=14.54ms p(95)=17.62ms  p(99.9)=30.06ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 646134
     http_req_receiving.............: avg=88.29µs min=24.46µs  med=44.53µs max=88.62ms  p(90)=83.87µs p(95)=187.25µs p(99.9)=5.51ms 
     http_req_sending...............: avg=42.87µs min=4.34µs   med=8.08µs  max=104.35ms p(90)=13.75µs p(95)=100.01µs p(99.9)=4.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.95ms  min=753.69µs med=8.07ms  max=165.21ms p(90)=14.32ms p(95)=17.36ms  p(99.9)=29.65ms
     http_reqs......................: 646134  5379.637998/s
     iteration_duration.............: avg=9.27ms  min=1.19ms   med=8.36ms  max=312.9ms  p(90)=14.74ms p(95)=17.85ms  p(99.9)=30.39ms
     iterations.....................: 646034  5378.805409/s
     success_rate...................: 100.00% ✓ 646034      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1927761     ✗ 0     
     data_received..................: 56 GB   468 MB/s
     data_sent......................: 773 MB  6.4 MB/s
     http_req_blocked...............: avg=2.94µs  min=912ns    med=2.33µs  max=7.46ms   p(90)=3.56µs  p(95)=4.17µs   p(99.9)=30.93µs
     http_req_connecting............: avg=151ns   min=0s       med=0s      max=4.03ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.13ms  min=823.35µs med=8.16ms  max=276.7ms  p(90)=14.82ms p(95)=18.2ms   p(99.9)=31.16ms
       { expected_response:true }...: avg=9.13ms  min=823.35µs med=8.16ms  max=276.7ms  p(90)=14.82ms p(95)=18.2ms   p(99.9)=31.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 642687
     http_req_receiving.............: avg=96.48µs min=23.49µs  med=45.79µs max=178.03ms p(90)=87.81µs p(95)=198.85µs p(99.9)=6.52ms 
     http_req_sending...............: avg=43.6µs  min=4.58µs   med=8.7µs   max=99.38ms  p(90)=14.52µs p(95)=104.74µs p(99.9)=4.91ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.99ms  min=759.88µs med=8.05ms  max=276.58ms p(90)=14.57ms p(95)=17.92ms  p(99.9)=30.69ms
     http_reqs......................: 642687  5350.934957/s
     iteration_duration.............: avg=9.32ms  min=1.19ms   med=8.35ms  max=285.94ms p(90)=15.04ms p(95)=18.42ms  p(99.9)=31.4ms 
     iterations.....................: 642587  5350.102368/s
     success_rate...................: 100.00% ✓ 642587      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1923681     ✗ 0     
     data_received..................: 56 GB   467 MB/s
     data_sent......................: 771 MB  6.4 MB/s
     http_req_blocked...............: avg=3.11µs   min=822ns    med=2.39µs  max=7.25ms   p(90)=3.65µs  p(95)=4.31µs   p(99.9)=34.24µs
     http_req_connecting............: avg=224ns    min=0s       med=0s      max=5.17ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.14ms   min=793.7µs  med=8.15ms  max=273.85ms p(90)=14.79ms p(95)=18.12ms  p(99.9)=31.42ms
       { expected_response:true }...: avg=9.14ms   min=793.7µs  med=8.15ms  max=273.85ms p(90)=14.79ms p(95)=18.12ms  p(99.9)=31.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 641327
     http_req_receiving.............: avg=101.77µs min=25.7µs   med=47.85µs max=109.99ms p(90)=91.89µs p(95)=197.64µs p(99.9)=7.16ms 
     http_req_sending...............: avg=44.55µs  min=4.52µs   med=8.76µs  max=159.05ms p(90)=14.89µs p(95)=103.18µs p(99.9)=5.12ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9ms      min=731.58µs med=8.03ms  max=273.26ms p(90)=14.52ms p(95)=17.81ms  p(99.9)=30.83ms
     http_reqs......................: 641327  5339.59637/s
     iteration_duration.............: avg=9.34ms   min=1.09ms   med=8.34ms  max=283.69ms p(90)=15ms    p(95)=18.35ms  p(99.9)=31.72ms
     iterations.....................: 641227  5338.763784/s
     success_rate...................: 100.00% ✓ 641227      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1922829     ✗ 0     
     data_received..................: 56 GB   467 MB/s
     data_sent......................: 771 MB  6.4 MB/s
     http_req_blocked...............: avg=2.59µs  min=771ns    med=1.92µs  max=7.54ms   p(90)=3.03µs  p(95)=3.63µs   p(99.9)=28.01µs
     http_req_connecting............: avg=248ns   min=0s       med=0s      max=6.38ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.15ms  min=844.28µs med=8.24ms  max=264.28ms p(90)=14.62ms p(95)=17.75ms  p(99.9)=30.11ms
       { expected_response:true }...: avg=9.15ms  min=844.28µs med=8.24ms  max=264.28ms p(90)=14.62ms p(95)=17.75ms  p(99.9)=30.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 641043
     http_req_receiving.............: avg=92.54µs min=25.73µs  med=46.15µs max=189.96ms p(90)=87.18µs p(95)=188.71µs p(99.9)=5.97ms 
     http_req_sending...............: avg=42.13µs min=4.19µs   med=8.04µs  max=217.94ms p(90)=13.69µs p(95)=99.89µs  p(99.9)=4.86ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.02ms  min=773.58µs med=8.13ms  max=258.37ms p(90)=14.4ms  p(95)=17.48ms  p(99.9)=29.68ms
     http_reqs......................: 641043  5337.281169/s
     iteration_duration.............: avg=9.35ms  min=1.07ms   med=8.42ms  max=277.94ms p(90)=14.83ms p(95)=17.97ms  p(99.9)=30.41ms
     iterations.....................: 640943  5336.448576/s
     success_rate...................: 100.00% ✓ 640943      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1888491     ✗ 0     
     data_received..................: 55 GB   459 MB/s
     data_sent......................: 757 MB  6.3 MB/s
     http_req_blocked...............: avg=2.98µs  min=841ns    med=2.36µs max=6.8ms    p(90)=3.6µs   p(95)=4.22µs   p(99.9)=32.03µs
     http_req_connecting............: avg=138ns   min=0s       med=0s     max=3.49ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.32ms  min=838.62µs med=8.37ms max=269.62ms p(90)=14.97ms p(95)=18.28ms  p(99.9)=30.93ms
       { expected_response:true }...: avg=9.32ms  min=838.62µs med=8.37ms max=269.62ms p(90)=14.97ms p(95)=18.28ms  p(99.9)=30.93ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 629597
     http_req_receiving.............: avg=93.53µs min=23.88µs  med=47.2µs max=77.25ms  p(90)=88.02µs p(95)=199.25µs p(99.9)=5.78ms 
     http_req_sending...............: avg=42.92µs min=4.48µs   med=8.82µs max=139.17ms p(90)=14.52µs p(95)=104.17µs p(99.9)=4.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.18ms  min=792.98µs med=8.26ms max=266.63ms p(90)=14.74ms p(95)=18.02ms  p(99.9)=30.45ms
     http_reqs......................: 629597  5241.71705/s
     iteration_duration.............: avg=9.52ms  min=1.18ms   med=8.56ms max=286.58ms p(90)=15.17ms p(95)=18.51ms  p(99.9)=31.26ms
     iterations.....................: 629497  5240.884498/s
     success_rate...................: 100.00% ✓ 629497      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-11-22-1912)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1852881     ✗ 0     
     data_received..................: 54 GB   450 MB/s
     data_sent......................: 743 MB  6.2 MB/s
     http_req_blocked...............: avg=2.97µs  min=782ns    med=2.06µs  max=15.24ms  p(90)=3.43µs  p(95)=4.15µs   p(99.9)=30.06µs
     http_req_connecting............: avg=423ns   min=0s       med=0s      max=15.05ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.5ms   min=813.1µs  med=8.53ms  max=306.13ms p(90)=15.29ms p(95)=18.61ms  p(99.9)=31.79ms
       { expected_response:true }...: avg=9.5ms   min=813.1µs  med=8.53ms  max=306.13ms p(90)=15.29ms p(95)=18.61ms  p(99.9)=31.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 617727
     http_req_receiving.............: avg=99.43µs min=22.86µs  med=46.33µs max=22.76ms  p(90)=92.68µs p(95)=205.18µs p(99.9)=6.71ms 
     http_req_sending...............: avg=44.25µs min=4.14µs   med=8.59µs  max=149.06ms p(90)=15.39µs p(95)=108.9µs  p(99.9)=4.92ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.36ms  min=741.49µs med=8.41ms  max=305.24ms p(90)=15.04ms p(95)=18.34ms  p(99.9)=31.27ms
     http_reqs......................: 617727  5142.9149/s
     iteration_duration.............: avg=9.7ms   min=1.12ms   med=8.72ms  max=325.02ms p(90)=15.5ms  p(95)=18.84ms  p(99.9)=32.09ms
     iterations.....................: 617627  5142.082345/s
     success_rate...................: 100.00% ✓ 617627      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.20-nightly.2b115870)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1639242     ✗ 0     
     data_received..................: 48 GB   398 MB/s
     data_sent......................: 657 MB  5.5 MB/s
     http_req_blocked...............: avg=2.58µs  min=821ns    med=2.06µs  max=4.28ms   p(90)=3.28µs  p(95)=3.91µs   p(99.9)=30.86µs
     http_req_connecting............: avg=159ns   min=0s       med=0s      max=3.38ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.77ms min=958.47µs med=10.26ms max=277.52ms p(90)=14.86ms p(95)=17.97ms  p(99.9)=28.42ms
       { expected_response:true }...: avg=10.77ms min=958.47µs med=10.26ms max=277.52ms p(90)=14.86ms p(95)=17.97ms  p(99.9)=28.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 546514
     http_req_receiving.............: avg=94.69µs min=25.18µs  med=50.49µs max=187.02ms p(90)=97.39µs p(95)=208.09µs p(99.9)=5.74ms 
     http_req_sending...............: avg=43.01µs min=4.39µs   med=8.73µs  max=209.52ms p(90)=15.29µs p(95)=110.07µs p(99.9)=4.34ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.63ms min=867.35µs med=10.16ms max=276.93ms p(90)=14.6ms  p(95)=17.69ms  p(99.9)=28.05ms
     http_reqs......................: 546514  4549.669423/s
     iteration_duration.............: avg=10.97ms min=1.69ms   med=10.44ms max=288.24ms p(90)=15.07ms p(95)=18.19ms  p(99.9)=28.72ms
     iterations.....................: 546414  4548.836933/s
     success_rate...................: 100.00% ✓ 546414      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1618599     ✗ 0     
     data_received..................: 47 GB   393 MB/s
     data_sent......................: 649 MB  5.4 MB/s
     http_req_blocked...............: avg=2.73µs  min=842ns    med=2.13µs  max=6.47ms   p(90)=3.47µs  p(95)=4.16µs   p(99.9)=31.81µs
     http_req_connecting............: avg=173ns   min=0s       med=0s      max=3.84ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.91ms min=954.7µs  med=10.4ms  max=275.02ms p(90)=15.02ms p(95)=18.21ms  p(99.9)=28.74ms
       { expected_response:true }...: avg=10.91ms min=954.7µs  med=10.4ms  max=275.02ms p(90)=15.02ms p(95)=18.21ms  p(99.9)=28.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 539633
     http_req_receiving.............: avg=93.67µs min=24.98µs  med=50.33µs max=198.95ms p(90)=98.31µs p(95)=209.59µs p(99.9)=5.37ms 
     http_req_sending...............: avg=43.13µs min=4.51µs   med=8.88µs  max=167.12ms p(90)=15.92µs p(95)=111.83µs p(99.9)=4.41ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.77ms min=874.71µs med=10.3ms  max=274.5ms  p(90)=14.76ms p(95)=17.95ms  p(99.9)=28.28ms
     http_reqs......................: 539633  4492.040354/s
     iteration_duration.............: avg=11.11ms min=1.69ms   med=10.58ms max=284.32ms p(90)=15.23ms p(95)=18.44ms  p(99.9)=29.03ms
     iterations.....................: 539533  4491.207929/s
     success_rate...................: 100.00% ✓ 539533      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: grafbase (HotChocolate subgraphs) (0.53.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 684930      ✗ 0     
     data_received..................: 20 GB   166 MB/s
     data_sent......................: 275 MB  2.3 MB/s
     http_req_blocked...............: avg=3.96µs  min=1.02µs  med=3.04µs  max=7.1ms    p(90)=5.17µs   p(95)=6.22µs   p(99.9)=43.09µs
     http_req_connecting............: avg=394ns   min=0s      med=0s      max=3.96ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.02ms min=1.93ms  med=25.48ms max=284.42ms p(90)=33.85ms  p(95)=36.55ms  p(99.9)=50.83ms
       { expected_response:true }...: avg=26.02ms min=1.93ms  med=25.48ms max=284.42ms p(90)=33.85ms  p(95)=36.55ms  p(99.9)=50.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 228410
     http_req_receiving.............: avg=93.79µs min=26.68µs med=61.64µs max=230.27ms p(90)=126.87µs p(95)=213.35µs p(99.9)=1.93ms 
     http_req_sending...............: avg=37.68µs min=4.68µs  med=11.39µs max=116.25ms p(90)=24.21µs  p(95)=115.8µs  p(99.9)=1.74ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=25.89ms min=1.83ms  med=25.36ms max=283.88ms p(90)=33.72ms  p(95)=36.4ms   p(99.9)=50.6ms 
     http_reqs......................: 228410  1899.248356/s
     iteration_duration.............: avg=26.27ms min=3.71ms  med=25.71ms max=309.19ms p(90)=34.08ms  p(95)=36.78ms  p(99.9)=51.2ms 
     iterations.....................: 228310  1898.416848/s
     success_rate...................: 100.00% ✓ 228310      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: caliban (HotChocolate subgraphs) (3.2.1)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 543537      ✗ 0     
     data_received..................: 16 GB   132 MB/s
     data_sent......................: 218 MB  1.8 MB/s
     http_req_blocked...............: avg=3.14µs  min=912ns   med=2.34µs  max=3.97ms   p(90)=3.83µs  p(95)=4.49µs  p(99.9)=30.16µs 
     http_req_connecting............: avg=518ns   min=0s      med=0s      max=3.93ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=32.88ms min=1.96ms  med=31.96ms max=271.78ms p(90)=46.6ms  p(95)=51.46ms p(99.9)=78.21ms 
       { expected_response:true }...: avg=32.88ms min=1.96ms  med=31.96ms max=271.78ms p(90)=46.6ms  p(95)=51.46ms p(99.9)=78.21ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 181279
     http_req_receiving.............: avg=68.27µs min=26.81µs med=56.57µs max=127.2ms  p(90)=91.22µs p(95)=106.7µs p(99.9)=770.58µs
     http_req_sending...............: avg=22µs    min=4.61µs  med=10.57µs max=178.54ms p(90)=16.8µs  p(95)=20.51µs p(99.9)=722.45µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=32.79ms min=1.9ms   med=31.87ms max=270.7ms  p(90)=46.51ms p(95)=51.36ms p(99.9)=77.87ms 
     http_reqs......................: 181279  1507.271563/s
     iteration_duration.............: avg=33.1ms  min=5.49ms  med=32.16ms max=300.12ms p(90)=46.81ms p(95)=51.66ms p(99.9)=78.68ms 
     iterations.....................: 181179  1506.440098/s
     success_rate...................: 100.00% ✓ 181179      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.373.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 539430      ✗ 0     
     data_received..................: 16 GB   131 MB/s
     data_sent......................: 216 MB  1.8 MB/s
     http_req_blocked...............: avg=2.94µs  min=911ns  med=2.14µs  max=3.44ms   p(90)=3.62µs  p(95)=4.29µs   p(99.9)=25.58µs 
     http_req_connecting............: avg=492ns   min=0s     med=0s      max=3.41ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.14ms min=2ms    med=32.28ms max=278.57ms p(90)=47.76ms p(95)=52.58ms  p(99.9)=75.62ms 
       { expected_response:true }...: avg=33.14ms min=2ms    med=32.28ms max=278.57ms p(90)=47.76ms p(95)=52.58ms  p(99.9)=75.62ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 179910
     http_req_receiving.............: avg=68.4µs  min=25.7µs med=58.25µs max=34.8ms   p(90)=94.31µs p(95)=109.34µs p(99.9)=684.48µs
     http_req_sending...............: avg=21.01µs min=4.54µs med=9.94µs  max=212.24ms p(90)=16.32µs p(95)=20.01µs  p(99.9)=750.67µs
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.05ms min=1.94ms med=32.19ms max=278.02ms p(90)=47.67ms p(95)=52.5ms   p(99.9)=75.45ms 
     http_reqs......................: 179910  1495.918405/s
     iteration_duration.............: avg=33.36ms min=4.26ms med=32.48ms max=293.93ms p(90)=47.95ms p(95)=52.78ms  p(99.9)=75.95ms 
     iterations.....................: 179810  1495.086924/s
     success_rate...................: 100.00% ✓ 179810      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 220734     ✗ 0    
     data_received..................: 6.5 GB  54 MB/s
     data_sent......................: 89 MB   735 kB/s
     http_req_blocked...............: avg=4.02µs  min=1µs     med=2.51µs  max=3.92ms   p(90)=3.92µs  p(95)=4.48µs   p(99.9)=42.51µs 
     http_req_connecting............: avg=1.24µs  min=0s      med=0s      max=3.88ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=81.22ms min=3.49ms  med=78.38ms max=316.33ms p(90)=98.4ms  p(95)=108.77ms p(99.9)=208.9ms 
       { expected_response:true }...: avg=81.22ms min=3.49ms  med=78.38ms max=316.33ms p(90)=98.4ms  p(95)=108.77ms p(99.9)=208.9ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 73678
     http_req_receiving.............: avg=73.07µs min=27.8µs  med=63.78µs max=89.88ms  p(90)=97.96µs p(95)=110.64µs p(99.9)=527.09µs
     http_req_sending...............: avg=18.58µs min=5µs     med=12.64µs max=73.7ms   p(90)=18.64µs p(95)=20.47µs  p(99.9)=545.2µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=81.12ms min=3.39ms  med=78.29ms max=316.16ms p(90)=98.3ms  p(95)=108.67ms p(99.9)=208.67ms
     http_reqs......................: 73678   611.606037/s
     iteration_duration.............: avg=81.55ms min=23.44ms med=78.61ms max=323.4ms  p(90)=98.63ms p(95)=109.04ms p(99.9)=210.67ms
     iterations.....................: 73578   610.775931/s
     success_rate...................: 100.00% ✓ 73578      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.19.1)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 193182     ✗ 0    
     data_received..................: 5.6 GB  47 MB/s
     data_sent......................: 78 MB   642 kB/s
     http_req_blocked...............: avg=4.44µs  min=1.07µs  med=2.71µs  max=4.09ms   p(90)=4.18µs   p(95)=4.76µs   p(99.9)=48.02µs 
     http_req_connecting............: avg=1.51µs  min=0s      med=0s      max=4.05ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.8ms  min=4.37ms  med=90.8ms  max=302.11ms p(90)=125.15ms p(95)=135.39ms p(99.9)=177.86ms
       { expected_response:true }...: avg=92.8ms  min=4.37ms  med=90.8ms  max=302.11ms p(90)=125.15ms p(95)=135.39ms p(99.9)=177.86ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64494
     http_req_receiving.............: avg=75.48µs min=27.59µs med=70.04µs max=44.68ms  p(90)=101.28µs p(95)=114.17µs p(99.9)=500.39µs
     http_req_sending...............: avg=22.6µs  min=4.86µs  med=13.29µs max=107.83ms p(90)=18.86µs  p(95)=20.71µs  p(99.9)=530.51µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.7ms  min=4.25ms  med=90.71ms max=301.94ms p(90)=125.04ms p(95)=135.3ms  p(99.9)=177.56ms
     http_reqs......................: 64494   534.931792/s
     iteration_duration.............: avg=93.19ms min=18.9ms  med=91.07ms max=310.79ms p(90)=125.42ms p(95)=135.65ms p(99.9)=179.44ms
     iterations.....................: 64394   534.102364/s
     success_rate...................: 100.00% ✓ 64394      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-nightly (HotChocolate subgraphs) (v3.0.0-preview.0-nightly.36cc3633)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 186345     ✗ 0    
     data_received..................: 5.4 GB  45 MB/s
     data_sent......................: 75 MB   620 kB/s
     http_req_blocked...............: avg=4.95µs  min=1.22µs  med=3.29µs  max=3.94ms   p(90)=4.75µs   p(95)=5.34µs   p(99.9)=55.34µs 
     http_req_connecting............: avg=1.44µs  min=0s      med=0s      max=3.91ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=96.19ms min=4.6ms   med=94.13ms max=319.69ms p(90)=127.67ms p(95)=138.09ms p(99.9)=182.63ms
       { expected_response:true }...: avg=96.19ms min=4.6ms   med=94.13ms max=319.69ms p(90)=127.67ms p(95)=138.09ms p(99.9)=182.63ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 62215
     http_req_receiving.............: avg=85.24µs min=27.69µs med=72.44µs max=157.81ms p(90)=102.9µs  p(95)=115.19µs p(99.9)=581.69µs
     http_req_sending...............: avg=28.68µs min=5.29µs  med=14.84µs max=118.03ms p(90)=20.44µs  p(95)=22.51µs  p(99.9)=552.27µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=96.08ms min=4.48ms  med=94.02ms max=319.53ms p(90)=127.57ms p(95)=137.96ms p(99.9)=182.07ms
     http_reqs......................: 62215   515.888847/s
     iteration_duration.............: avg=96.6ms  min=13.04ms med=94.41ms max=329.91ms p(90)=127.98ms p(95)=138.36ms p(99.9)=184.55ms
     iterations.....................: 62115   515.059644/s
     success_rate...................: 100.00% ✓ 62115      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-v3 (HotChocolate subgraphs) (v3.0.0-preview.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 145362     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   483 kB/s
     http_req_blocked...............: avg=5.45µs   min=1.25µs  med=3.19µs   max=4.12ms   p(90)=4.55µs   p(95)=5.11µs   p(99.9)=736.82µs
     http_req_connecting............: avg=2.04µs   min=0s      med=0s       max=4.08ms   p(90)=0s       p(95)=0s       p(99.9)=713.24µs
     http_req_duration..............: avg=123.36ms min=5.32ms  med=120.82ms max=340.43ms p(90)=161.79ms p(95)=174.8ms  p(99.9)=227.12ms
       { expected_response:true }...: avg=123.36ms min=5.32ms  med=120.82ms max=340.43ms p(90)=161.79ms p(95)=174.8ms  p(99.9)=227.12ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48554
     http_req_receiving.............: avg=79.18µs  min=30.55µs med=72.62µs  max=53.83ms  p(90)=102.19µs p(95)=113.83µs p(99.9)=472.82µs
     http_req_sending...............: avg=25µs     min=5.62µs  med=14.73µs  max=81.8ms   p(90)=19.74µs  p(95)=21.58µs  p(99.9)=449.79µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=123.26ms min=5.21ms  med=120.73ms max=340.23ms p(90)=161.68ms p(95)=174.67ms p(99.9)=226.26ms
     http_reqs......................: 48554   402.336486/s
     iteration_duration.............: avg=123.85ms min=24.56ms med=121.14ms max=350.85ms p(90)=162.1ms  p(95)=175.18ms p(99.9)=229.55ms
     iterations.....................: 48454   401.507849/s
     success_rate...................: 100.00% ✓ 48454      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 109608     ✗ 0    
     data_received..................: 3.2 GB  27 MB/s
     data_sent......................: 44 MB   364 kB/s
     http_req_blocked...............: avg=6.29µs   min=1.12µs  med=3.41µs   max=3.62ms   p(90)=4.84µs   p(95)=5.45µs   p(99.9)=1.55ms  
     http_req_connecting............: avg=2.65µs   min=0s      med=0s       max=3.57ms   p(90)=0s       p(95)=0s       p(99.9)=1.52ms  
     http_req_duration..............: avg=163.74ms min=5.24ms  med=146.44ms max=757.8ms  p(90)=186.43ms p(95)=209.84ms p(99.9)=688.31ms
       { expected_response:true }...: avg=163.74ms min=5.24ms  med=146.44ms max=757.8ms  p(90)=186.43ms p(95)=209.84ms p(99.9)=688.31ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 36636
     http_req_receiving.............: avg=97.51µs  min=35.01µs med=86.93µs  max=91.76ms  p(90)=116.95µs p(95)=127.91µs p(99.9)=881.21µs
     http_req_sending...............: avg=30.57µs  min=5.96µs  med=17.31µs  max=97.26ms  p(90)=22.15µs  p(95)=23.95µs  p(99.9)=543.73µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=163.61ms min=5.11ms  med=146.33ms max=757.68ms p(90)=186.31ms p(95)=209.71ms p(99.9)=688.18ms
     http_reqs......................: 36636   302.773809/s
     iteration_duration.............: avg=164.46ms min=29.29ms med=146.8ms  max=758.05ms p(90)=186.76ms p(95)=210.38ms p(99.9)=688.63ms
     iterations.....................: 36536   301.947371/s
     success_rate...................: 100.00% ✓ 36536      ✗ 0    
     vus............................: 5       min=5        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-gateway (HotChocolate subgraphs) (2.14.4)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 99513      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   330 kB/s
     http_req_blocked...............: avg=8µs      min=1.2µs   med=3.42µs   max=7.95ms   p(90)=4.82µs   p(95)=5.39µs   p(99.9)=1ms     
     http_req_connecting............: avg=3.96µs   min=0s      med=0s       max=5.79ms   p(90)=0s       p(95)=0s       p(99.9)=948.15µs
     http_req_duration..............: avg=180.18ms min=7.41ms  med=179.6ms  max=455.13ms p(90)=210.59ms p(95)=216.74ms p(99.9)=277.76ms
       { expected_response:true }...: avg=180.18ms min=7.41ms  med=179.6ms  max=455.13ms p(90)=210.59ms p(95)=216.74ms p(99.9)=277.76ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33271
     http_req_receiving.............: avg=87.84µs  min=33.2µs  med=85.49µs  max=3.06ms   p(90)=114.25µs p(95)=124.71µs p(99.9)=465.1µs 
     http_req_sending...............: avg=21.43µs  min=5.9µs   med=16.84µs  max=14.03ms  p(90)=21.16µs  p(95)=22.86µs  p(99.9)=1.05ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=180.07ms min=7.27ms  med=179.49ms max=453.9ms  p(90)=210.49ms p(95)=216.63ms p(99.9)=277.66ms
     http_reqs......................: 33271   275.03561/s
     iteration_duration.............: avg=180.97ms min=43.14ms med=180.13ms max=461.95ms p(90)=210.86ms p(95)=217ms    p(99.9)=279.22ms
     iterations.....................: 33171   274.208957/s
     success_rate...................: 100.00% ✓ 33171      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

