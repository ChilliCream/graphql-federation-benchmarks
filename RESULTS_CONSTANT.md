## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.16 | 5,426 | 5,445 | 5,406 | 0.3% | 382 MB | 72.1 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.16 | 5,390 | 5,409 | 5,387 | 0.2% | 396 MB | 75.3 KB |  |
| fusion-net-11 | 16.7.6 | 5,353 | 5,435 | 5,307 | 0.9% | 383 MB | 73.4 KB |  |
| fusion-fed-aot-11 | 16.7.6 | 5,319 | 5,325 | 5,293 | 0.3% | 124 MB | 23.9 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.16 | 5,309 | 5,318 | 5,299 | 0.1% | 133 MB | 25.7 KB |  |
| fusion-aot-11 | 16.7.6 | 5,307 | 5,313 | 5,295 | 0.1% | 119 MB | 23.0 KB |  |
| fusion-fed-net-11 | 16.7.6 | 5,295 | 5,345 | 5,232 | 0.9% | 373 MB | 72.1 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.16 | 5,142 | 5,181 | 5,132 | 0.4% | 130 MB | 25.8 KB |  |
| feddi-gateway | 2026-11-03-0517 | 4,881 | 4,901 | 4,784 | 0.9% | 2,296 MB | 481.7 KB |  |
| hive-router | v0.3.16 | 4,417 | 4,431 | 4,380 | 0.5% | 94 MB | 21.8 KB |  |
| grafbase | 0.53.5 | 1,878 | 1,887 | 1,846 | 0.9% | 108 MB | 58.7 KB |  |
| caliban | 3.2.1 | 1,465 | 1,467 | 1,449 | 0.5% | 5,085 MB | 3,554.0 KB |  |
| cosmo | 0.373.0 | 1,453 | 1,454 | 1,450 | 0.1% | 164 MB | 115.8 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 610 | 613 | 609 | 0.3% | 2,598 MB | 4,360.4 KB |  |
| apollo-router | v2.19.1 | 488 | 493 | 487 | 0.5% | 177 MB | 370.9 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 429 | 431 | 429 | 0.2% | 204 MB | 487.3 KB |  |
| hive-gateway | 2.15.10 | 289 | 290 | 287 | 0.4% | 3,393 MB | 12,022.2 KB |  |
| apollo-gateway | 2.14.4 | 277 | 278 | 276 | 0.3% | 2,146 MB | 7,934.0 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1955040    ✗ 0     
     data_received..................: 57 GB   475 MB/s
     data_sent......................: 783 MB  6.5 MB/s
     http_req_blocked...............: avg=2.48µs  min=792ns    med=1.93µs  max=6.85ms   p(90)=3.02µs  p(95)=3.6µs    p(99.9)=27.48µs
     http_req_connecting............: avg=131ns   min=0s       med=0s      max=3.39ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9ms     min=802.51µs med=8.09ms  max=266.43ms p(90)=14.44ms p(95)=17.59ms  p(99.9)=29.83ms
       { expected_response:true }...: avg=9ms     min=802.51µs med=8.09ms  max=266.43ms p(90)=14.44ms p(95)=17.59ms  p(99.9)=29.83ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 651780
     http_req_receiving.............: avg=91.33µs min=25.82µs  med=46.21µs max=63.37ms  p(90)=85.94µs p(95)=186.56µs p(99.9)=5.82ms 
     http_req_sending...............: avg=42.62µs min=4.31µs   med=8.02µs  max=192.9ms  p(90)=13.55µs p(95)=98.53µs  p(99.9)=4.87ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.87ms  min=742.95µs med=7.99ms  max=265.79ms p(90)=14.22ms p(95)=17.34ms  p(99.9)=29.46ms
     http_reqs......................: 651780  5426.58986/s
     iteration_duration.............: avg=9.19ms  min=1.04ms   med=8.28ms  max=279.6ms  p(90)=14.64ms p(95)=17.81ms  p(99.9)=30.07ms
     iterations.....................: 651680  5425.75728/s
     success_rate...................: 100.00% ✓ 651680     ✗ 0     
     vus............................: 50      min=50       max=50  
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1942149     ✗ 0     
     data_received..................: 57 GB   472 MB/s
     data_sent......................: 778 MB  6.5 MB/s
     http_req_blocked...............: avg=2.5µs   min=782ns    med=1.92µs max=6.74ms   p(90)=3.01µs  p(95)=3.6µs    p(99.9)=26.77µs
     http_req_connecting............: avg=141ns   min=0s       med=0s     max=3.57ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.06ms  min=805.24µs med=8.13ms max=262.77ms p(90)=14.47ms p(95)=17.65ms  p(99.9)=30.34ms
       { expected_response:true }...: avg=9.06ms  min=805.24µs med=8.13ms max=262.77ms p(90)=14.47ms p(95)=17.65ms  p(99.9)=30.34ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 647483
     http_req_receiving.............: avg=93.72µs min=24.77µs  med=46.2µs max=172.77ms p(90)=86.7µs  p(95)=189.76µs p(99.9)=6.08ms 
     http_req_sending...............: avg=42.07µs min=4.25µs   med=8.14µs max=198.66ms p(90)=13.72µs p(95)=99.77µs  p(99.9)=4.73ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.92ms  min=741.56µs med=8.02ms max=262.38ms p(90)=14.24ms p(95)=17.37ms  p(99.9)=29.95ms
     http_reqs......................: 647483  5390.739666/s
     iteration_duration.............: avg=9.25ms  min=975.57µs med=8.31ms max=290.48ms p(90)=14.67ms p(95)=17.86ms  p(99.9)=30.65ms
     iterations.....................: 647383  5389.907097/s
     success_rate...................: 100.00% ✓ 647383      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1928715     ✗ 0     
     data_received..................: 56 GB   468 MB/s
     data_sent......................: 773 MB  6.4 MB/s
     http_req_blocked...............: avg=2.86µs  min=892ns    med=2.3µs   max=6.03ms   p(90)=3.52µs  p(95)=4.17µs   p(99.9)=31.41µs
     http_req_connecting............: avg=133ns   min=0s       med=0s      max=3.46ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.12ms  min=785.57µs med=8.14ms  max=286.2ms  p(90)=14.81ms p(95)=18.17ms  p(99.9)=31.45ms
       { expected_response:true }...: avg=9.12ms  min=785.57µs med=8.14ms  max=286.2ms  p(90)=14.81ms p(95)=18.17ms  p(99.9)=31.45ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 643005
     http_req_receiving.............: avg=97.93µs min=25.17µs  med=47.65µs max=100.62ms p(90)=90.35µs p(95)=198.69µs p(99.9)=6.48ms 
     http_req_sending...............: avg=44.3µs  min=4.4µs    med=8.59µs  max=149.59ms p(90)=14.47µs p(95)=102.95µs p(99.9)=5.06ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.98ms  min=730.29µs med=8.03ms  max=285.64ms p(90)=14.56ms p(95)=17.88ms  p(99.9)=31.04ms
     http_reqs......................: 643005  5353.323/s
     iteration_duration.............: avg=9.32ms  min=1.21ms   med=8.33ms  max=296.17ms p(90)=15.02ms p(95)=18.39ms  p(99.9)=31.73ms
     iterations.....................: 642905  5352.490453/s
     success_rate...................: 100.00% ✓ 642905      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1916352     ✗ 0     
     data_received..................: 56 GB   465 MB/s
     data_sent......................: 768 MB  6.4 MB/s
     http_req_blocked...............: avg=2.49µs  min=821ns    med=1.93µs  max=5.66ms   p(90)=3.03µs  p(95)=3.6µs    p(99.9)=26.9µs 
     http_req_connecting............: avg=161ns   min=0s       med=0s      max=3.76ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.19ms  min=836.25µs med=8.3ms   max=296.56ms p(90)=14.62ms p(95)=17.7ms   p(99.9)=30.09ms
       { expected_response:true }...: avg=9.19ms  min=836.25µs med=8.3ms   max=296.56ms p(90)=14.62ms p(95)=17.7ms   p(99.9)=30.09ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 638884
     http_req_receiving.............: avg=96.22µs min=24.63µs  med=45.07µs max=241.64ms p(90)=85.8µs  p(95)=191.15µs p(99.9)=5.77ms 
     http_req_sending...............: avg=41.35µs min=4.42µs   med=8.15µs  max=118.32ms p(90)=13.92µs p(95)=100.29µs p(99.9)=4.69ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.05ms  min=757.11µs med=8.2ms   max=133.94ms p(90)=14.4ms  p(95)=17.43ms  p(99.9)=29.59ms
     http_reqs......................: 638884  5319.192319/s
     iteration_duration.............: avg=9.38ms  min=1.26ms   med=8.49ms  max=306.59ms p(90)=14.82ms p(95)=17.92ms  p(99.9)=30.38ms
     iterations.....................: 638784  5318.359744/s
     success_rate...................: 100.00% ✓ 638784      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1912770     ✗ 0     
     data_received..................: 56 GB   465 MB/s
     data_sent......................: 767 MB  6.4 MB/s
     http_req_blocked...............: avg=2.79µs  min=871ns    med=2.26µs  max=5.59ms   p(90)=3.55µs  p(95)=4.21µs   p(99.9)=33.64µs
     http_req_connecting............: avg=137ns   min=0s       med=0s      max=3.85ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.2ms   min=836.24µs med=8.22ms  max=280.59ms p(90)=14.92ms p(95)=18.33ms  p(99.9)=31.25ms
       { expected_response:true }...: avg=9.2ms   min=836.24µs med=8.22ms  max=280.59ms p(90)=14.92ms p(95)=18.33ms  p(99.9)=31.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 637690
     http_req_receiving.............: avg=97.89µs min=24.35µs  med=45.94µs max=219.2ms  p(90)=89.49µs p(95)=198.14µs p(99.9)=6.41ms 
     http_req_sending...............: avg=43.76µs min=4.45µs   med=8.68µs  max=125.26ms p(90)=14.75µs p(95)=104.93µs p(99.9)=4.96ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.06ms  min=758.15µs med=8.11ms  max=227.7ms  p(90)=14.69ms p(95)=18.04ms  p(99.9)=30.78ms
     http_reqs......................: 637690  5309.070231/s
     iteration_duration.............: avg=9.4ms   min=1.19ms   med=8.41ms  max=290.13ms p(90)=15.13ms p(95)=18.55ms  p(99.9)=31.55ms
     iterations.....................: 637590  5308.237684/s
     success_rate...................: 100.00% ✓ 637590      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1912074     ✗ 0     
     data_received..................: 56 GB   464 MB/s
     data_sent......................: 766 MB  6.4 MB/s
     http_req_blocked...............: avg=2.92µs  min=832ns    med=2.01µs  max=9.71ms   p(90)=3.18µs  p(95)=3.78µs   p(99.9)=28.92µs
     http_req_connecting............: avg=468ns   min=0s       med=0s      max=8.54ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.2ms   min=810.04µs med=8.27ms  max=270.23ms p(90)=14.79ms p(95)=18.04ms  p(99.9)=30.68ms
       { expected_response:true }...: avg=9.2ms   min=810.04µs med=8.27ms  max=270.23ms p(90)=14.79ms p(95)=18.04ms  p(99.9)=30.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 637458
     http_req_receiving.............: avg=91.41µs min=23.22µs  med=45.13µs max=34.39ms  p(90)=86.47µs p(95)=190.17µs p(99.9)=5.95ms 
     http_req_sending...............: avg=45.72µs min=4.48µs   med=8.26µs  max=181.57ms p(90)=14.11µs p(95)=102.02µs p(99.9)=5.09ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.07ms  min=769.42µs med=8.17ms  max=188.85ms p(90)=14.56ms p(95)=17.77ms  p(99.9)=30.33ms
     http_reqs......................: 637458  5307.237727/s
     iteration_duration.............: avg=9.4ms   min=1.28ms   med=8.46ms  max=298.42ms p(90)=15ms    p(95)=18.27ms  p(99.9)=30.93ms
     iterations.....................: 637358  5306.405164/s
     success_rate...................: 100.00% ✓ 637358      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1907910     ✗ 0     
     data_received..................: 56 GB   463 MB/s
     data_sent......................: 765 MB  6.4 MB/s
     http_req_blocked...............: avg=3.03µs  min=941ns    med=2.42µs  max=6.5ms    p(90)=3.67µs  p(95)=4.32µs   p(99.9)=35.41µs
     http_req_connecting............: avg=146ns   min=0s       med=0s      max=4.1ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.22ms  min=807.42µs med=8.23ms  max=236.53ms p(90)=14.91ms p(95)=18.26ms  p(99.9)=30.99ms
       { expected_response:true }...: avg=9.22ms  min=807.42µs med=8.23ms  max=236.53ms p(90)=14.91ms p(95)=18.26ms  p(99.9)=30.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 636070
     http_req_receiving.............: avg=96.36µs min=25.35µs  med=47.59µs max=62.72ms  p(90)=90.16µs p(95)=198.24µs p(99.9)=6.17ms 
     http_req_sending...............: avg=43.83µs min=4.23µs   med=8.69µs  max=20.09ms  p(90)=14.56µs p(95)=105.05µs p(99.9)=5.02ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.08ms  min=746.18µs med=8.12ms  max=235.73ms p(90)=14.66ms p(95)=17.99ms  p(99.9)=30.59ms
     http_reqs......................: 636070  5295.698799/s
     iteration_duration.............: avg=9.42ms  min=1.02ms   med=8.42ms  max=340.48ms p(90)=15.13ms p(95)=18.49ms  p(99.9)=31.47ms
     iterations.....................: 635970  5294.866234/s
     success_rate...................: 100.00% ✓ 635970      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1852686     ✗ 0     
     data_received..................: 54 GB   450 MB/s
     data_sent......................: 742 MB  6.2 MB/s
     http_req_blocked...............: avg=2.94µs  min=941ns    med=2.39µs  max=6.41ms   p(90)=3.62µs  p(95)=4.26µs   p(99.9)=30.86µs
     http_req_connecting............: avg=150ns   min=0s       med=0s      max=3.97ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.5ms   min=859.37µs med=8.54ms  max=291.15ms p(90)=15.29ms p(95)=18.65ms  p(99.9)=31.73ms
       { expected_response:true }...: avg=9.5ms   min=859.37µs med=8.54ms  max=291.15ms p(90)=15.29ms p(95)=18.65ms  p(99.9)=31.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 617662
     http_req_receiving.............: avg=99.43µs min=25.56µs  med=48.34µs max=34.15ms  p(90)=93.17µs p(95)=212.83µs p(99.9)=6.28ms 
     http_req_sending...............: avg=44.27µs min=4.5µs    med=8.6µs   max=259.62ms p(90)=14.67µs p(95)=108.64µs p(99.9)=4.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.36ms  min=804.83µs med=8.43ms  max=288.04ms p(90)=15.05ms p(95)=18.37ms  p(99.9)=31.32ms
     http_reqs......................: 617662  5142.301993/s
     iteration_duration.............: avg=9.7ms   min=1.22ms   med=8.73ms  max=307.17ms p(90)=15.5ms  p(95)=18.87ms  p(99.9)=32.03ms
     iterations.....................: 617562  5141.46945/s
     success_rate...................: 100.00% ✓ 617562      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-11-03-0517)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1758723     ✗ 0     
     data_received..................: 51 GB   427 MB/s
     data_sent......................: 705 MB  5.9 MB/s
     http_req_blocked...............: avg=2.49µs  min=801ns    med=1.96µs  max=5.56ms   p(90)=3.06µs  p(95)=3.63µs   p(99.9)=25.48µs
     http_req_connecting............: avg=150ns   min=0s       med=0s      max=3.92ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.03ms min=716.8µs  med=9.39ms  max=280.04ms p(90)=14.76ms p(95)=17.99ms  p(99.9)=28.54ms
       { expected_response:true }...: avg=10.03ms min=716.8µs  med=9.39ms  max=280.04ms p(90)=14.76ms p(95)=17.99ms  p(99.9)=28.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 586341
     http_req_receiving.............: avg=89.66µs min=24.13µs  med=45.55µs max=146.62ms p(90)=85.75µs p(95)=194.92µs p(99.9)=6.19ms 
     http_req_sending...............: avg=40.79µs min=4.41µs   med=8.37µs  max=210.56ms p(90)=14.64µs p(95)=103.61µs p(99.9)=4.23ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.9ms   min=640.75µs med=9.3ms   max=279.54ms p(90)=14.51ms p(95)=17.75ms  p(99.9)=28.14ms
     http_reqs......................: 586341  4881.972046/s
     iteration_duration.............: avg=10.22ms min=1.18ms   med=9.57ms  max=295.61ms p(90)=14.97ms p(95)=18.19ms  p(99.9)=28.79ms
     iterations.....................: 586241  4881.13943/s
     success_rate...................: 100.00% ✓ 586241      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1591842     ✗ 0     
     data_received..................: 46 GB   386 MB/s
     data_sent......................: 638 MB  5.3 MB/s
     http_req_blocked...............: avg=3.04µs  min=802ns    med=2.47µs  max=5.48ms   p(90)=3.86µs  p(95)=4.56µs   p(99.9)=34.23µs
     http_req_connecting............: avg=171ns   min=0s       med=0s      max=3.52ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.1ms  min=955.81µs med=10.79ms max=292.5ms  p(90)=15.43ms p(95)=18.55ms  p(99.9)=29.47ms
       { expected_response:true }...: avg=11.1ms  min=955.81µs med=10.79ms max=292.5ms  p(90)=15.43ms p(95)=18.55ms  p(99.9)=29.47ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 530714
     http_req_receiving.............: avg=92.81µs min=25.11µs  med=49.26µs max=132.01ms p(90)=96.92µs p(95)=211.45µs p(99.9)=5.29ms 
     http_req_sending...............: avg=42.37µs min=4.53µs   med=9.23µs  max=132.57ms p(90)=16.2µs  p(95)=113.25µs p(99.9)=4.16ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.96ms min=875.61µs med=10.67ms max=282.14ms p(90)=15.19ms p(95)=18.27ms  p(99.9)=29.07ms
     http_reqs......................: 530714  4417.957343/s
     iteration_duration.............: avg=11.29ms min=1.42ms   med=10.98ms max=302.73ms p(90)=15.64ms p(95)=18.78ms  p(99.9)=29.72ms
     iterations.....................: 530614  4417.124887/s
     success_rate...................: 100.00% ✓ 530614      ✗ 0     
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

     checks.........................: 100.00% ✓ 677565      ✗ 0     
     data_received..................: 20 GB   165 MB/s
     data_sent......................: 272 MB  2.3 MB/s
     http_req_blocked...............: avg=4.11µs  min=842ns   med=2.27µs  max=10.26ms  p(90)=4.38µs   p(95)=5.36µs   p(99.9)=38.96µs
     http_req_connecting............: avg=1.29µs  min=0s      med=0s      max=10.22ms  p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.32ms min=1.82ms  med=25.79ms max=280.66ms p(90)=34.01ms  p(95)=36.7ms   p(99.9)=50.62ms
       { expected_response:true }...: avg=26.32ms min=1.82ms  med=25.79ms max=280.66ms p(90)=34.01ms  p(95)=36.7ms   p(99.9)=50.62ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 225955
     http_req_receiving.............: avg=93.24µs min=27.47µs med=57.39µs max=172.54ms p(90)=117.69µs p(95)=182.1µs  p(99.9)=1.64ms 
     http_req_sending...............: avg=33.05µs min=4.54µs  med=9.83µs  max=138.6ms  p(90)=22.13µs  p(95)=100.48µs p(99.9)=1.45ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.19ms min=1.72ms  med=25.68ms max=257.27ms p(90)=33.89ms  p(95)=36.57ms  p(99.9)=50.36ms
     http_reqs......................: 225955  1878.849696/s
     iteration_duration.............: avg=26.55ms min=7.69ms  med=26.01ms max=303.8ms  p(90)=34.22ms  p(95)=36.92ms  p(99.9)=50.97ms
     iterations.....................: 225855  1878.018181/s
     success_rate...................: 100.00% ✓ 225855      ✗ 0     
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

     checks.........................: 100.00% ✓ 528489      ✗ 0     
     data_received..................: 15 GB   128 MB/s
     data_sent......................: 212 MB  1.8 MB/s
     http_req_blocked...............: avg=3.68µs  min=1.08µs  med=2.85µs  max=4.06ms   p(90)=4.39µs  p(95)=5.08µs   p(99.9)=35.29µs 
     http_req_connecting............: avg=544ns   min=0s      med=0s      max=4.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.81ms min=2ms     med=32.82ms max=298.81ms p(90)=48.15ms p(95)=53.28ms  p(99.9)=82.19ms 
       { expected_response:true }...: avg=33.81ms min=2ms     med=32.82ms max=298.81ms p(90)=48.15ms p(95)=53.28ms  p(99.9)=82.19ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 176263
     http_req_receiving.............: avg=71.86µs min=27.89µs med=60.43µs max=65.97ms  p(90)=95.77µs p(95)=111.26µs p(99.9)=834.04µs
     http_req_sending...............: avg=25.01µs min=5.34µs  med=12.18µs max=172.48ms p(90)=17.79µs p(95)=21.39µs  p(99.9)=779.56µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.71ms min=1.9ms   med=32.72ms max=298.31ms p(90)=48.06ms p(95)=53.18ms  p(99.9)=82.1ms  
     http_reqs......................: 176263  1465.657444/s
     iteration_duration.............: avg=34.05ms min=5.21ms  med=33.04ms max=308.31ms p(90)=48.37ms p(95)=53.5ms   p(99.9)=82.75ms 
     iterations.....................: 176163  1464.825926/s
     success_rate...................: 100.00% ✓ 176163      ✗ 0     
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

     checks.........................: 100.00% ✓ 524247      ✗ 0     
     data_received..................: 15 GB   127 MB/s
     data_sent......................: 210 MB  1.7 MB/s
     http_req_blocked...............: avg=3.47µs  min=1.16µs  med=2.61µs  max=4.01ms   p(90)=4.06µs  p(95)=4.72µs   p(99.9)=34.44µs 
     http_req_connecting............: avg=555ns   min=0s      med=0s      max=3.97ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.1ms  min=2.02ms  med=33.2ms  max=320.15ms p(90)=49.28ms p(95)=54.44ms  p(99.9)=77.54ms 
       { expected_response:true }...: avg=34.1ms  min=2.02ms  med=33.2ms  max=320.15ms p(90)=49.28ms p(95)=54.44ms  p(99.9)=77.54ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 174849
     http_req_receiving.............: avg=74.36µs min=26.73µs med=60.85µs max=217.41ms p(90)=96.95µs p(95)=113.57µs p(99.9)=738.39µs
     http_req_sending...............: avg=23.2µs  min=4.95µs  med=11.2µs  max=89.18ms  p(90)=16.56µs p(95)=20.23µs  p(99.9)=800.36µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34ms    min=1.97ms  med=33.11ms max=319.92ms p(90)=49.17ms p(95)=54.34ms  p(99.9)=77.05ms 
     http_reqs......................: 174849  1453.759208/s
     iteration_duration.............: avg=34.32ms min=3.84ms  med=33.41ms max=328.58ms p(90)=49.48ms p(95)=54.65ms  p(99.9)=77.86ms 
     iterations.....................: 174749  1452.927771/s
     success_rate...................: 100.00% ✓ 174749      ✗ 0     
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

     checks.........................: 100.00% ✓ 220218     ✗ 0    
     data_received..................: 6.4 GB  53 MB/s
     data_sent......................: 88 MB   733 kB/s
     http_req_blocked...............: avg=4.64µs  min=1.16µs  med=3.06µs  max=4.37ms   p(90)=4.55µs  p(95)=5.19µs   p(99.9)=41.43µs 
     http_req_connecting............: avg=1.34µs  min=0s      med=0s      max=4.33ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=81.4ms  min=3.46ms  med=78.56ms max=330.29ms p(90)=98.34ms p(95)=108.65ms p(99.9)=200.85ms
       { expected_response:true }...: avg=81.4ms  min=3.46ms  med=78.56ms max=330.29ms p(90)=98.34ms p(95)=108.65ms p(99.9)=200.85ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 73506
     http_req_receiving.............: avg=79.37µs min=27.97µs med=70.23µs max=43.87ms  p(90)=103.2µs p(95)=115.42µs p(99.9)=602.64µs
     http_req_sending...............: avg=18.85µs min=5.45µs  med=13.67µs max=34.18ms  p(90)=19.28µs p(95)=21.43µs  p(99.9)=607.81µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=81.3ms  min=3.4ms   med=78.46ms max=329.39ms p(90)=98.23ms p(95)=108.55ms p(99.9)=200.76ms
     http_reqs......................: 73506   610.116548/s
     iteration_duration.............: avg=81.74ms min=13.49ms med=78.79ms max=338.09ms p(90)=98.58ms p(95)=108.89ms p(99.9)=202.67ms
     iterations.....................: 73406   609.286525/s
     success_rate...................: 100.00% ✓ 73406      ✗ 0    
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

     checks.........................: 100.00% ✓ 176388     ✗ 0    
     data_received..................: 5.2 GB  43 MB/s
     data_sent......................: 71 MB   587 kB/s
     http_req_blocked...............: avg=4.83µs   min=1.24µs  med=3.06µs  max=3.53ms   p(90)=4.5µs    p(95)=5.09µs   p(99.9)=52.85µs 
     http_req_connecting............: avg=1.56µs   min=0s      med=0s      max=3.5ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=101.66ms min=4.41ms  med=99.52ms max=321.21ms p(90)=137.27ms p(95)=149.02ms p(99.9)=193.02ms
       { expected_response:true }...: avg=101.66ms min=4.41ms  med=99.52ms max=321.21ms p(90)=137.27ms p(95)=149.02ms p(99.9)=193.02ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 58896
     http_req_receiving.............: avg=80.41µs  min=30.37µs med=71.17µs max=83.56ms  p(90)=101.52µs p(95)=113.77µs p(99.9)=532.69µs
     http_req_sending...............: avg=21.33µs  min=5.19µs  med=13.88µs max=98.32ms  p(90)=19.13µs  p(95)=21.1µs   p(99.9)=548.75µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=101.56ms min=4.28ms  med=99.42ms max=319.85ms p(90)=137.17ms p(95)=148.9ms  p(99.9)=192.83ms
     http_reqs......................: 58896   488.447403/s
     iteration_duration.............: avg=102.07ms min=18.91ms med=99.82ms max=342.67ms p(90)=137.53ms p(95)=149.32ms p(99.9)=194.46ms
     iterations.....................: 58796   487.618065/s
     success_rate...................: 100.00% ✓ 58796      ✗ 0    
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

     checks.........................: 100.00% ✓ 155319     ✗ 0    
     data_received..................: 4.5 GB  38 MB/s
     data_sent......................: 62 MB   516 kB/s
     http_req_blocked...............: avg=4.26µs   min=1.07µs  med=3.15µs   max=2.77ms   p(90)=4.57µs   p(95)=5.13µs  p(99.9)=84.26µs 
     http_req_connecting............: avg=922ns    min=0s      med=0s       max=2.75ms   p(90)=0s       p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=115.45ms min=5.36ms  med=113.09ms max=327.77ms p(90)=150.8ms  p(95)=162.7ms p(99.9)=211.32ms
       { expected_response:true }...: avg=115.45ms min=5.36ms  med=113.09ms max=327.77ms p(90)=150.8ms  p(95)=162.7ms p(99.9)=211.32ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51873
     http_req_receiving.............: avg=83.73µs  min=29.67µs med=78.85µs  max=97.25ms  p(90)=107.71µs p(95)=119.7µs p(99.9)=461.18µs
     http_req_sending...............: avg=21.54µs  min=4.84µs  med=16.01µs  max=49.52ms  p(90)=20.53µs  p(95)=22.26µs p(99.9)=452.38µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=115.34ms min=5.25ms  med=112.99ms max=327.63ms p(90)=150.68ms p(95)=162.6ms p(99.9)=211.03ms
     http_reqs......................: 51873   429.852221/s
     iteration_duration.............: avg=115.92ms min=34.22ms med=113.39ms max=349.41ms p(90)=151.09ms p(95)=163ms   p(99.9)=213.39ms
     iterations.....................: 51773   429.023558/s
     success_rate...................: 100.00% ✓ 51773      ✗ 0    
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

     checks.........................: 100.00% ✓ 104505     ✗ 0    
     data_received..................: 3.1 GB  25 MB/s
     data_sent......................: 42 MB   347 kB/s
     http_req_blocked...............: avg=6.5µs    min=1.34µs  med=3.49µs   max=3.94ms   p(90)=4.89µs   p(95)=5.52µs   p(99.9)=1.46ms  
     http_req_connecting............: avg=2.76µs   min=0s      med=0s       max=3.9ms    p(90)=0s       p(95)=0s       p(99.9)=1.37ms  
     http_req_duration..............: avg=171.6ms  min=5.64ms  med=154.03ms max=834.24ms p(90)=196.49ms p(95)=221.32ms p(99.9)=717.01ms
       { expected_response:true }...: avg=171.6ms  min=5.64ms  med=154.03ms max=834.24ms p(90)=196.49ms p(95)=221.32ms p(99.9)=717.01ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 34935
     http_req_receiving.............: avg=88.97µs  min=33.33µs med=84.4µs   max=8.22ms   p(90)=113.78µs p(95)=125.29µs p(99.9)=635.31µs
     http_req_sending...............: avg=20.85µs  min=6.45µs  med=16.96µs  max=19.86ms  p(90)=21.49µs  p(95)=23.08µs  p(99.9)=457.49µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=171.49ms min=5.57ms  med=153.93ms max=834.15ms p(90)=196.39ms p(95)=221.19ms p(99.9)=716.91ms
     http_reqs......................: 34935   289.184349/s
     iteration_duration.............: avg=172.33ms min=79.96ms med=154.33ms max=834.49ms p(90)=196.92ms p(95)=221.92ms p(99.9)=717.35ms
     iterations.....................: 34835   288.356571/s
     success_rate...................: 100.00% ✓ 34835      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 100458     ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   333 kB/s
     http_req_blocked...............: avg=6.66µs   min=1.39µs  med=3.43µs   max=4.14ms   p(90)=4.83µs   p(95)=5.44µs   p(99.9)=1.4ms   
     http_req_connecting............: avg=2.99µs   min=0s      med=0s       max=4.1ms    p(90)=0s       p(95)=0s       p(99.9)=1.38ms  
     http_req_duration..............: avg=178.45ms min=7.41ms  med=171.21ms max=408.94ms p(90)=215.06ms p(95)=220.75ms p(99.9)=292.1ms 
       { expected_response:true }...: avg=178.45ms min=7.41ms  med=171.21ms max=408.94ms p(90)=215.06ms p(95)=220.75ms p(99.9)=292.1ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 33586
     http_req_receiving.............: avg=92.2µs   min=35.86µs med=86.23µs  max=45.08ms  p(90)=116.47µs p(95)=127.87µs p(99.9)=475.87µs
     http_req_sending...............: avg=26.81µs  min=6.22µs  med=17.33µs  max=62.2ms   p(90)=21.86µs  p(95)=23.76µs  p(99.9)=503.41µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=178.33ms min=7.33ms  med=171.1ms  max=408.57ms p(90)=214.97ms p(95)=220.64ms p(99.9)=291.99ms
     http_reqs......................: 33586   277.701282/s
     iteration_duration.............: avg=179.26ms min=46.39ms med=171.49ms max=418.41ms p(90)=215.38ms p(95)=221.07ms p(99.9)=292.78ms
     iterations.....................: 33486   276.874446/s
     success_rate...................: 100.00% ✓ 33486      ✗ 0    
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

