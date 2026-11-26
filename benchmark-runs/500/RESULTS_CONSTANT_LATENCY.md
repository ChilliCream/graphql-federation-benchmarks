## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.7 | 3,607 | 3,625 | 3,600 | 0.3% | 363 MB | 102.9 KB |  |
| fusion-aot-11 | 16.7.7 | 3,580 | 3,606 | 3,558 | 0.5% | 117 MB | 33.5 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 3,579 | 3,587 | 3,570 | 0.2% | 117 MB | 33.6 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.21 | 3,579 | 3,587 | 3,564 | 0.3% | 107 MB | 30.5 KB |  |
| fusion-fed-net-11 | 16.7.7 | 3,578 | 3,601 | 3,556 | 0.4% | 373 MB | 106.7 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.21 | 3,576 | 3,605 | 3,565 | 0.4% | 353 MB | 101.2 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.21 | 3,571 | 3,572 | 3,558 | 0.2% | 348 MB | 99.9 KB |  |
| feddi-gateway | 2026-11-22-1912 | 3,557 | 3,568 | 3,547 | 0.2% | 2,309 MB | 664.7 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.21 | 3,554 | 3,570 | 3,538 | 0.3% | 107 MB | 30.8 KB |  |
| hive-router-nightly | v0.3.20-nightly.2b115870 | 3,385 | 3,399 | 3,376 | 0.2% | 89 MB | 26.9 KB |  |
| hive-router | v0.3.17 | 3,358 | 3,378 | 3,349 | 0.3% | 92 MB | 27.9 KB |  |
| caliban | 3.2.1 | 1,464 | 1,469 | 1,455 | 0.4% | 6,121 MB | 4,281.2 KB |  |
| grafbase | 0.53.5 | 1,459 | 1,465 | 1,449 | 0.4% | 100 MB | 70.4 KB |  |
| cosmo | 0.373.0 | 1,439 | 1,441 | 1,438 | 0.1% | 151 MB | 107.2 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 594 | 597 | 594 | 0.2% | 2,612 MB | 4,503.0 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.36cc3633 | 517 | 517 | 516 | 0.1% | 197 MB | 389.5 KB |  |
| apollo-router | v2.19.1 | 515 | 525 | 514 | 0.9% | 181 MB | 360.9 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 420 | 421 | 419 | 0.2% | 205 MB | 498.9 KB |  |
| hive-gateway | 2.15.10 | 288 | 289 | 286 | 0.4% | 3,232 MB | 11,491.2 KB |  |
| apollo-gateway | 2.14.4 | 266 | 267 | 265 | 0.4% | 2,164 MB | 8,330.7 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1308696     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 524 MB  4.3 MB/s
     http_req_blocked...............: avg=2.41µs  min=781ns   med=1.84µs  max=3.99ms   p(90)=3.11µs  p(95)=3.89µs   p(99.9)=24.61µs
     http_req_connecting............: avg=197ns   min=0s      med=0s      max=3.95ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.55ms min=8.05ms  med=13.13ms max=295.49ms p(90)=16.65ms p(95)=17.89ms  p(99.9)=25.2ms 
       { expected_response:true }...: avg=13.55ms min=8.05ms  med=13.13ms max=295.49ms p(90)=16.65ms p(95)=17.89ms  p(99.9)=25.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 436332
     http_req_receiving.............: avg=72.81µs min=23.66µs med=43.38µs max=184.51ms p(90)=92.67µs p(95)=172.94µs p(99.9)=1.83ms 
     http_req_sending...............: avg=32.09µs min=4.19µs  med=7.89µs  max=167.32ms p(90)=16.74µs p(95)=94.03µs  p(99.9)=1.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.44ms min=7.99ms  med=13.04ms max=295.28ms p(90)=16.54ms p(95)=17.77ms  p(99.9)=24.96ms
     http_reqs......................: 436332  3607.35837/s
     iteration_duration.............: avg=13.74ms min=8.22ms  med=13.32ms max=305.33ms p(90)=16.84ms p(95)=18.08ms  p(99.9)=25.39ms
     iterations.....................: 436232  3606.531624/s
     success_rate...................: 100.00% ✓ 436232      ✗ 0     
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

     checks.........................: 100.00% ✓ 1298889     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 520 MB  4.3 MB/s
     http_req_blocked...............: avg=2.84µs  min=922ns   med=2.26µs  max=3.7ms    p(90)=3.59µs  p(95)=4.3µs    p(99.9)=30µs   
     http_req_connecting............: avg=237ns   min=0s      med=0s      max=3.66ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.65ms min=8.09ms  med=13.2ms  max=284.19ms p(90)=16.81ms p(95)=18.14ms  p(99.9)=25.88ms
       { expected_response:true }...: avg=13.65ms min=8.09ms  med=13.2ms  max=284.19ms p(90)=16.81ms p(95)=18.14ms  p(99.9)=25.88ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 433063
     http_req_receiving.............: avg=71.59µs min=24.11µs med=44.26µs max=101.84ms p(90)=93.04µs p(95)=186.65µs p(99.9)=1.83ms 
     http_req_sending...............: avg=34.98µs min=4.46µs  med=8.54µs  max=239.16ms p(90)=16.66µs p(95)=101.59µs p(99.9)=1.85ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.54ms min=8.03ms  med=13.1ms  max=283.69ms p(90)=16.69ms p(95)=18ms     p(99.9)=25.64ms
     http_reqs......................: 433063  3580.156005/s
     iteration_duration.............: avg=13.84ms min=8.26ms  med=13.39ms max=306.1ms  p(90)=17.01ms p(95)=18.33ms  p(99.9)=26.08ms
     iterations.....................: 432963  3579.3293/s
     success_rate...................: 100.00% ✓ 432963      ✗ 0     
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

     checks.........................: 100.00% ✓ 1298400     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 520 MB  4.3 MB/s
     http_req_blocked...............: avg=2.83µs  min=902ns   med=2.3µs   max=4.14ms   p(90)=3.65µs  p(95)=4.41µs   p(99.9)=30.89µs
     http_req_connecting............: avg=160ns   min=0s      med=0s      max=3.71ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.65ms min=8.14ms  med=13.21ms max=263.5ms  p(90)=16.8ms  p(95)=18.11ms  p(99.9)=25.7ms 
       { expected_response:true }...: avg=13.65ms min=8.14ms  med=13.21ms max=263.5ms  p(90)=16.8ms  p(95)=18.11ms  p(99.9)=25.7ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 432900
     http_req_receiving.............: avg=74.81µs min=25.82µs med=47.76µs max=19.43ms  p(90)=98.3µs  p(95)=190.47µs p(99.9)=1.97ms 
     http_req_sending...............: avg=34.41µs min=4.42µs  med=8.7µs   max=136.57ms p(90)=17.35µs p(95)=102.67µs p(99.9)=1.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.54ms min=8.08ms  med=13.11ms max=263.16ms p(90)=16.67ms p(95)=17.98ms  p(99.9)=25.42ms
     http_reqs......................: 432900  3579.072382/s
     iteration_duration.............: avg=13.85ms min=8.34ms  med=13.4ms  max=284.98ms p(90)=16.99ms p(95)=18.31ms  p(99.9)=25.93ms
     iterations.....................: 432800  3578.245616/s
     success_rate...................: 100.00% ✓ 432800      ✗ 0     
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

     checks.........................: 100.00% ✓ 1298484     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 520 MB  4.3 MB/s
     http_req_blocked...............: avg=2.4µs   min=821ns   med=1.86µs  max=3.9ms    p(90)=2.96µs  p(95)=3.59µs   p(99.9)=24.65µs
     http_req_connecting............: avg=217ns   min=0s      med=0s      max=3.87ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.66ms min=8.2ms   med=13.24ms max=281.75ms p(90)=16.77ms p(95)=18.02ms  p(99.9)=25.45ms
       { expected_response:true }...: avg=13.66ms min=8.2ms   med=13.24ms max=281.75ms p(90)=16.77ms p(95)=18.02ms  p(99.9)=25.45ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 432928
     http_req_receiving.............: avg=66.75µs min=23.27µs med=43.4µs  max=205.45ms p(90)=87.51µs p(95)=166.22µs p(99.9)=1.56ms 
     http_req_sending...............: avg=32µs    min=4.03µs  med=7.95µs  max=154.73ms p(90)=15.14µs p(95)=92.46µs  p(99.9)=1.82ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.56ms min=8.1ms   med=13.14ms max=281.25ms p(90)=16.66ms p(95)=17.91ms  p(99.9)=25.21ms
     http_reqs......................: 432928  3579.144698/s
     iteration_duration.............: avg=13.85ms min=8.4ms   med=13.43ms max=304.1ms  p(90)=16.96ms p(95)=18.21ms  p(99.9)=25.67ms
     iterations.....................: 432828  3578.317969/s
     success_rate...................: 100.00% ✓ 432828      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1298301     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 520 MB  4.3 MB/s
     http_req_blocked...............: avg=2.4µs   min=782ns   med=1.84µs  max=3.59ms   p(90)=3.09µs  p(95)=3.9µs    p(99.9)=24.22µs
     http_req_connecting............: avg=207ns   min=0s      med=0s      max=3.56ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.66ms min=8.26ms  med=13.26ms max=280.96ms p(90)=16.77ms p(95)=18.03ms  p(99.9)=25.5ms 
       { expected_response:true }...: avg=13.66ms min=8.26ms  med=13.26ms max=280.96ms p(90)=16.77ms p(95)=18.03ms  p(99.9)=25.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 432867
     http_req_receiving.............: avg=68.86µs min=23.92µs med=43.86µs max=154.36ms p(90)=92.93µs p(95)=168.52µs p(99.9)=1.75ms 
     http_req_sending...............: avg=31.13µs min=4.19µs  med=7.86µs  max=154.78ms p(90)=16.18µs p(95)=92.13µs  p(99.9)=1.74ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.56ms min=8.21ms  med=13.16ms max=280.46ms p(90)=16.65ms p(95)=17.91ms  p(99.9)=25.27ms
     http_reqs......................: 432867  3578.82175/s
     iteration_duration.............: avg=13.85ms min=8.44ms  med=13.45ms max=290.45ms p(90)=16.95ms p(95)=18.22ms  p(99.9)=25.72ms
     iterations.....................: 432767  3577.994978/s
     success_rate...................: 100.00% ✓ 432767      ✗ 0     
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

     checks.........................: 100.00% ✓ 1297497     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 520 MB  4.3 MB/s
     http_req_blocked...............: avg=2.78µs  min=812ns   med=2.21µs  max=3.97ms   p(90)=3.53µs  p(95)=4.28µs   p(99.9)=31.28µs
     http_req_connecting............: avg=215ns   min=0s      med=0s      max=3.93ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.66ms min=8.04ms  med=13.21ms max=245.67ms p(90)=16.92ms p(95)=18.25ms  p(99.9)=26.1ms 
       { expected_response:true }...: avg=13.66ms min=8.04ms  med=13.21ms max=245.67ms p(90)=16.92ms p(95)=18.25ms  p(99.9)=26.1ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 432599
     http_req_receiving.............: avg=74.17µs min=24.46µs med=46.35µs max=108.04ms p(90)=98.74µs p(95)=188.85µs p(99.9)=1.99ms 
     http_req_sending...............: avg=33.21µs min=4.22µs  med=8.41µs  max=119.02ms p(90)=17.57µs p(95)=102.06µs p(99.9)=1.93ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.55ms min=7.98ms  med=13.1ms  max=245.33ms p(90)=16.8ms  p(95)=18.12ms  p(99.9)=25.84ms
     http_reqs......................: 432599  3576.742969/s
     iteration_duration.............: avg=13.86ms min=8.19ms  med=13.4ms  max=297.33ms p(90)=17.11ms p(95)=18.45ms  p(99.9)=26.32ms
     iterations.....................: 432499  3575.916166/s
     success_rate...................: 100.00% ✓ 432499      ✗ 0     
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

     checks.........................: 100.00% ✓ 1295595     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 519 MB  4.3 MB/s
     http_req_blocked...............: avg=3.27µs  min=871ns   med=2.33µs  max=8.58ms   p(90)=3.7µs   p(95)=4.48µs   p(99.9)=31.12µs
     http_req_connecting............: avg=537ns   min=0s      med=0s      max=8.45ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.68ms min=8.14ms  med=13.25ms max=279.59ms p(90)=16.9ms  p(95)=18.21ms  p(99.9)=25.9ms 
       { expected_response:true }...: avg=13.68ms min=8.14ms  med=13.25ms max=279.59ms p(90)=16.9ms  p(95)=18.21ms  p(99.9)=25.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 431965
     http_req_receiving.............: avg=74.42µs min=24.01µs med=45.85µs max=231.96ms p(90)=97.56µs p(95)=188.55µs p(99.9)=2.01ms 
     http_req_sending...............: avg=33.92µs min=4.36µs  med=8.58µs  max=231.84ms p(90)=17.37µs p(95)=100.25µs p(99.9)=1.93ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.57ms min=8.08ms  med=13.15ms max=263.97ms p(90)=16.78ms p(95)=18.08ms  p(99.9)=25.68ms
     http_reqs......................: 431965  3571.455806/s
     iteration_duration.............: avg=13.88ms min=8.29ms  med=13.45ms max=295.6ms  p(90)=17.09ms p(95)=18.41ms  p(99.9)=26.13ms
     iterations.....................: 431865  3570.629013/s
     success_rate...................: 100.00% ✓ 431865      ✗ 0     
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

     checks.........................: 100.00% ✓ 1290441     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.94µs  min=872ns   med=2.36µs  max=3.5ms    p(90)=3.8µs    p(95)=4.65µs   p(99.9)=33.77µs
     http_req_connecting............: avg=202ns   min=0s      med=0s      max=3.46ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.73ms min=7.51ms  med=13.26ms max=292.69ms p(90)=16.97ms  p(95)=18.33ms  p(99.9)=26.33ms
       { expected_response:true }...: avg=13.73ms min=7.51ms  med=13.26ms max=292.69ms p(90)=16.97ms  p(95)=18.33ms  p(99.9)=26.33ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 430247
     http_req_receiving.............: avg=76.26µs min=24.53µs med=47.96µs max=115.89ms p(90)=102.57µs p(95)=192.53µs p(99.9)=1.99ms 
     http_req_sending...............: avg=35.04µs min=4.28µs  med=8.77µs  max=168.46ms p(90)=18.42µs  p(95)=104.61µs p(99.9)=1.98ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.62ms min=7.45ms  med=13.16ms max=292.17ms p(90)=16.85ms  p(95)=18.18ms  p(99.9)=26.11ms
     http_reqs......................: 430247  3557.03588/s
     iteration_duration.............: avg=13.93ms min=7.63ms  med=13.46ms max=316.12ms p(90)=17.17ms  p(95)=18.52ms  p(99.9)=26.56ms
     iterations.....................: 430147  3556.209137/s
     success_rate...................: 100.00% ✓ 430147      ✗ 0     
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

     checks.........................: 100.00% ✓ 1289559     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.43µs  min=831ns   med=1.88µs  max=3.81ms   p(90)=3.1µs   p(95)=3.81µs   p(99.9)=26.08µs
     http_req_connecting............: avg=201ns   min=0s      med=0s      max=3.51ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.75ms min=8.15ms  med=13.36ms max=285.01ms p(90)=16.89ms p(95)=18.13ms  p(99.9)=25.46ms
       { expected_response:true }...: avg=13.75ms min=8.15ms  med=13.36ms max=285.01ms p(90)=16.89ms p(95)=18.13ms  p(99.9)=25.46ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429953
     http_req_receiving.............: avg=67.26µs min=23.72µs med=42.73µs max=47.15ms  p(90)=90.79µs p(95)=169.62µs p(99.9)=1.71ms 
     http_req_sending...............: avg=31.13µs min=4.32µs  med=8.01µs  max=122.16ms p(90)=16.61µs p(95)=94.78µs  p(99.9)=1.71ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.65ms min=8.1ms   med=13.26ms max=284.59ms p(90)=16.78ms p(95)=18.01ms  p(99.9)=25.25ms
     http_reqs......................: 429953  3554.694095/s
     iteration_duration.............: avg=13.94ms min=8.33ms  med=13.55ms max=302.12ms p(90)=17.08ms p(95)=18.32ms  p(99.9)=25.66ms
     iterations.....................: 429853  3553.867332/s
     success_rate...................: 100.00% ✓ 429853      ✗ 0     
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

     checks.........................: 100.00% ✓ 1228425     ✗ 0     
     data_received..................: 36 GB   296 MB/s
     data_sent......................: 492 MB  4.1 MB/s
     http_req_blocked...............: avg=2.97µs  min=872ns   med=2.34µs  max=3.53ms   p(90)=3.94µs   p(95)=4.81µs   p(99.9)=32.64µs
     http_req_connecting............: avg=210ns   min=0s      med=0s      max=3.48ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.44ms min=8.25ms  med=14.05ms max=294.53ms p(90)=17.61ms  p(95)=18.9ms   p(99.9)=26.73ms
       { expected_response:true }...: avg=14.44ms min=8.25ms  med=14.05ms max=294.53ms p(90)=17.61ms  p(95)=18.9ms   p(99.9)=26.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 409575
     http_req_receiving.............: avg=76.89µs min=25.26µs med=48.16µs max=164.7ms  p(90)=105.56µs p(95)=198.62µs p(99.9)=1.9ms  
     http_req_sending...............: avg=34.54µs min=4.45µs  med=8.79µs  max=115.33ms p(90)=19.18µs  p(95)=106.51µs p(99.9)=1.92ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.33ms min=8.2ms   med=13.94ms max=263.83ms p(90)=17.49ms  p(95)=18.76ms  p(99.9)=26.43ms
     http_reqs......................: 409575  3385.593025/s
     iteration_duration.............: avg=14.64ms min=8.4ms   med=14.24ms max=303.9ms  p(90)=17.81ms  p(95)=19.1ms   p(99.9)=26.95ms
     iterations.....................: 409475  3384.766414/s
     success_rate...................: 100.00% ✓ 409475      ✗ 0     
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

     checks.........................: 100.00% ✓ 1218453     ✗ 0     
     data_received..................: 36 GB   294 MB/s
     data_sent......................: 488 MB  4.0 MB/s
     http_req_blocked...............: avg=2.88µs  min=811ns   med=1.89µs  max=8.64ms   p(90)=3.2µs   p(95)=4µs      p(99.9)=25.69µs
     http_req_connecting............: avg=623ns   min=0s      med=0s      max=8.6ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.57ms min=8.31ms  med=14.24ms max=280.47ms p(90)=17.61ms p(95)=18.83ms  p(99.9)=26.26ms
       { expected_response:true }...: avg=14.57ms min=8.31ms  med=14.24ms max=280.47ms p(90)=17.61ms p(95)=18.83ms  p(99.9)=26.26ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 406251
     http_req_receiving.............: avg=67.41µs min=23.04µs med=43.93µs max=149.51ms p(90)=92.79µs p(95)=165.42µs p(99.9)=1.39ms 
     http_req_sending...............: avg=30.86µs min=4.24µs  med=8.04µs  max=203.3ms  p(90)=16.66µs p(95)=92.79µs  p(99.9)=1.64ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.47ms min=8.25ms  med=14.14ms max=258.57ms p(90)=17.51ms p(95)=18.72ms  p(99.9)=26.05ms
     http_reqs......................: 406251  3358.303662/s
     iteration_duration.............: avg=14.76ms min=8.47ms  med=14.42ms max=293.31ms p(90)=17.79ms p(95)=19.02ms  p(99.9)=26.48ms
     iterations.....................: 406151  3357.477005/s
     success_rate...................: 100.00% ✓ 406151      ✗ 0     
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

     checks.........................: 100.00% ✓ 535416      ✗ 0     
     data_received..................: 16 GB   128 MB/s
     data_sent......................: 215 MB  1.8 MB/s
     http_req_blocked...............: avg=3µs     min=942ns   med=2.17µs  max=3.42ms   p(90)=3.67µs  p(95)=4.4µs    p(99.9)=28.69µs 
     http_req_connecting............: avg=512ns   min=0s      med=0s      max=3.4ms    p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.4ms  min=18ms    med=32.91ms max=303.65ms p(90)=39.06ms p(95)=41.21ms  p(99.9)=58.41ms 
       { expected_response:true }...: avg=33.4ms  min=18ms    med=32.91ms max=303.65ms p(90)=39.06ms p(95)=41.21ms  p(99.9)=58.41ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 178572
     http_req_receiving.............: avg=70.42µs min=26.25µs med=58.19µs max=116.41ms p(90)=94.52µs p(95)=111.73µs p(99.9)=813.3µs 
     http_req_sending...............: avg=20.4µs  min=4.69µs  med=10.11µs max=115.03ms p(90)=15.77µs p(95)=19.49µs  p(99.9)=727.42µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.31ms min=17.86ms med=32.82ms max=303.18ms p(90)=38.97ms p(95)=41.11ms  p(99.9)=57.94ms 
     http_reqs......................: 178572  1464.192024/s
     iteration_duration.............: avg=33.61ms min=19.95ms med=33.11ms max=311.72ms p(90)=39.26ms p(95)=41.41ms  p(99.9)=59.17ms 
     iterations.....................: 178472  1463.372079/s
     success_rate...................: 100.00% ✓ 178472      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 533484      ✗ 0     
     data_received..................: 16 GB   128 MB/s
     data_sent......................: 214 MB  1.8 MB/s
     http_req_blocked...............: avg=3.23µs  min=821ns   med=2.14µs  max=4.01ms   p(90)=4.55µs   p(95)=5.49µs   p(99.9)=33.17µs
     http_req_connecting............: avg=506ns   min=0s      med=0s      max=3.92ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.48ms min=16.56ms med=33.23ms max=295.8ms  p(90)=39.12ms  p(95)=40.78ms  p(99.9)=48.98ms
       { expected_response:true }...: avg=33.48ms min=16.56ms med=33.23ms max=295.8ms  p(90)=39.12ms  p(95)=40.78ms  p(99.9)=48.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 177928
     http_req_receiving.............: avg=78.07µs min=25.67µs med=53.55µs max=90.87ms  p(90)=116.95µs p(95)=155.94µs p(99.9)=1.43ms 
     http_req_sending...............: avg=29.36µs min=4.5µs   med=9.16µs  max=163.93ms p(90)=21.3µs   p(95)=31.71µs  p(99.9)=1.23ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.37ms min=16.49ms med=33.13ms max=295.5ms  p(90)=39.01ms  p(95)=40.68ms  p(99.9)=48.73ms
     http_reqs......................: 177928  1459.320429/s
     iteration_duration.............: avg=33.73ms min=19.94ms med=33.46ms max=313.04ms p(90)=39.34ms  p(95)=41ms     p(99.9)=49.32ms
     iterations.....................: 177828  1458.500254/s
     success_rate...................: 100.00% ✓ 177828      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 526296      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 211 MB  1.7 MB/s
     http_req_blocked...............: avg=3µs     min=871ns   med=2.13µs  max=4.09ms   p(90)=3.66µs  p(95)=4.36µs   p(99.9)=33.64µs 
     http_req_connecting............: avg=528ns   min=0s      med=0s      max=4.04ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.98ms min=17.98ms med=33.43ms max=301.06ms p(90)=40.46ms p(95)=42.74ms  p(99.9)=53.94ms 
       { expected_response:true }...: avg=33.98ms min=17.98ms med=33.43ms max=301.06ms p(90)=40.46ms p(95)=42.74ms  p(99.9)=53.94ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 175532
     http_req_receiving.............: avg=73.91µs min=24.89µs med=59.39µs max=174.08ms p(90)=98.87µs p(95)=116.27µs p(99.9)=687.73µs
     http_req_sending...............: avg=20.89µs min=4.41µs  med=10.11µs max=104.67ms p(90)=17.44µs p(95)=21.31µs  p(99.9)=751.63µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.88ms min=17.92ms med=33.34ms max=284.12ms p(90)=40.37ms p(95)=42.64ms  p(99.9)=53.79ms 
     http_reqs......................: 175532  1439.229871/s
     iteration_duration.............: avg=34.19ms min=20.53ms med=33.63ms max=320.21ms p(90)=40.66ms p(95)=42.94ms  p(99.9)=54.18ms 
     iterations.....................: 175432  1438.409946/s
     success_rate...................: 100.00% ✓ 175432      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 217743     ✗ 0    
     data_received..................: 6.4 GB  52 MB/s
     data_sent......................: 87 MB   714 kB/s
     http_req_blocked...............: avg=4.49µs  min=1.06µs  med=2.92µs  max=3.91ms   p(90)=4.45µs   p(95)=5.08µs   p(99.9)=42.03µs 
     http_req_connecting............: avg=1.29µs  min=0s      med=0s      max=3.87ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=82.34ms min=19.85ms med=79.42ms max=341.67ms p(90)=101.02ms p(95)=109.77ms p(99.9)=202.01ms
       { expected_response:true }...: avg=82.34ms min=19.85ms med=79.42ms max=341.67ms p(90)=101.02ms p(95)=109.77ms p(99.9)=202.01ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 72681
     http_req_receiving.............: avg=83.87µs min=28.09µs med=70.69µs max=154.68ms p(90)=103.7µs  p(95)=116.42µs p(99.9)=570.91µs
     http_req_sending...............: avg=20.9µs  min=4.82µs  med=14.23µs max=94.86ms  p(90)=19.84µs  p(95)=21.79µs  p(99.9)=545.79µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=82.24ms min=19.73ms med=79.32ms max=330.61ms p(90)=100.93ms p(95)=109.66ms p(99.9)=201.59ms
     http_reqs......................: 72681   594.803128/s
     iteration_duration.............: avg=82.67ms min=40.62ms med=79.66ms max=349.85ms p(90)=101.26ms p(95)=110.06ms p(99.9)=202.61ms
     iterations.....................: 72581   593.984753/s
     success_rate...................: 100.00% ✓ 72581      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 189357     ✗ 0    
     data_received..................: 5.5 GB  45 MB/s
     data_sent......................: 76 MB   621 kB/s
     http_req_blocked...............: avg=7.08µs  min=1.27µs  med=3.41µs  max=6.57ms   p(90)=5.02µs   p(95)=5.66µs   p(99.9)=48.36µs 
     http_req_connecting............: avg=3.36µs  min=0s      med=0s      max=6.54ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=94.68ms min=19.97ms med=93.29ms max=323.14ms p(90)=118.04ms p(95)=125.89ms p(99.9)=164.08ms
       { expected_response:true }...: avg=94.68ms min=19.97ms med=93.29ms max=323.14ms p(90)=118.04ms p(95)=125.89ms p(99.9)=164.08ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63219
     http_req_receiving.............: avg=84.44µs min=31.04µs med=74.91µs max=205.51ms p(90)=107.82µs p(95)=119.74µs p(99.9)=529.54µs
     http_req_sending...............: avg=25.94µs min=5.6µs   med=15.68µs max=79.93ms  p(90)=21.41µs  p(95)=23.63µs  p(99.9)=733.43µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.57ms min=19.84ms med=93.19ms max=301.84ms p(90)=117.92ms p(95)=125.78ms p(99.9)=163.51ms
     http_reqs......................: 63219   517.262355/s
     iteration_duration.............: avg=95.07ms min=31.42ms med=93.57ms max=336.92ms p(90)=118.3ms  p(95)=126.17ms p(99.9)=166.15ms
     iterations.....................: 63119   516.444147/s
     success_rate...................: 100.00% ✓ 63119      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 188628     ✗ 0    
     data_received..................: 5.5 GB  45 MB/s
     data_sent......................: 76 MB   619 kB/s
     http_req_blocked...............: avg=4.91µs  min=1.21µs  med=3.15µs  max=4.19ms   p(90)=4.64µs   p(95)=5.27µs   p(99.9)=49.89µs 
     http_req_connecting............: avg=1.48µs  min=0s      med=0s      max=4.15ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=95.06ms min=19.66ms med=93.27ms max=307.72ms p(90)=119.89ms p(95)=128.51ms p(99.9)=166.55ms
       { expected_response:true }...: avg=95.06ms min=19.66ms med=93.27ms max=307.72ms p(90)=119.89ms p(95)=128.51ms p(99.9)=166.55ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 62976
     http_req_receiving.............: avg=79.31µs min=30.72µs med=72.46µs max=73.97ms  p(90)=105.76µs p(95)=118.06µs p(99.9)=546µs   
     http_req_sending...............: avg=21.8µs  min=5.6µs   med=14.72µs max=82.88ms  p(90)=20.74µs  p(95)=22.94µs  p(99.9)=573.45µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.96ms min=19.59ms med=93.17ms max=307.36ms p(90)=119.8ms  p(95)=128.41ms p(99.9)=166.4ms 
     http_reqs......................: 62976   515.353199/s
     iteration_duration.............: avg=95.44ms min=26ms    med=93.54ms max=324.3ms  p(90)=120.15ms p(95)=128.76ms p(99.9)=168.09ms
     iterations.....................: 62876   514.534867/s
     success_rate...................: 100.00% ✓ 62876      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 154002     ✗ 0    
     data_received..................: 4.5 GB  37 MB/s
     data_sent......................: 62 MB   505 kB/s
     http_req_blocked...............: avg=4.62µs   min=1.05µs  med=2.77µs   max=3.46ms   p(90)=4.16µs   p(95)=4.72µs   p(99.9)=102.91µs
     http_req_connecting............: avg=1.66µs   min=0s      med=0s       max=3.42ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=116.48ms min=20.92ms med=114.95ms max=343.08ms p(90)=143.91ms p(95)=153.44ms p(99.9)=197.8ms 
       { expected_response:true }...: avg=116.48ms min=20.92ms med=114.95ms max=343.08ms p(90)=143.91ms p(95)=153.44ms p(99.9)=197.8ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 51434
     http_req_receiving.............: avg=81.25µs  min=27.55µs med=74.21µs  max=122.35ms p(90)=105.53µs p(95)=117.14µs p(99.9)=457.17µs
     http_req_sending...............: avg=18.09µs  min=4.67µs  med=14.74µs  max=44.25ms  p(90)=19.9µs   p(95)=21.76µs  p(99.9)=466.82µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=116.38ms min=20.79ms med=114.85ms max=342.62ms p(90)=143.81ms p(95)=153.36ms p(99.9)=197.39ms
     http_reqs......................: 51434   420.484134/s
     iteration_duration.............: avg=116.92ms min=36.46ms med=115.22ms max=353.04ms p(90)=144.17ms p(95)=153.75ms p(99.9)=200.05ms
     iterations.....................: 51334   419.666613/s
     success_rate...................: 100.00% ✓ 51334      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 105456     ✗ 0    
     data_received..................: 3.1 GB  25 MB/s
     data_sent......................: 42 MB   347 kB/s
     http_req_blocked...............: avg=5.93µs   min=1.07µs  med=3µs      max=4.28ms   p(90)=4.32µs   p(95)=4.86µs   p(99.9)=1.22ms  
     http_req_connecting............: avg=2.74µs   min=0s      med=0s       max=4.24ms   p(90)=0s       p(95)=0s       p(99.9)=1.17ms  
     http_req_duration..............: avg=170.05ms min=17.2ms  med=156.38ms max=781.95ms p(90)=192.91ms p(95)=209.7ms  p(99.9)=698.84ms
       { expected_response:true }...: avg=170.05ms min=17.2ms  med=156.38ms max=781.95ms p(90)=192.91ms p(95)=209.7ms  p(99.9)=698.84ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 35252
     http_req_receiving.............: avg=93.54µs  min=31.13µs med=83.73µs  max=96.25ms  p(90)=113.41µs p(95)=124.87µs p(99.9)=928.55µs
     http_req_sending...............: avg=24.11µs  min=5.46µs  med=16.31µs  max=119.88ms p(90)=20.65µs  p(95)=22.41µs  p(99.9)=512.43µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=169.94ms min=17.06ms med=156.27ms max=781.85ms p(90)=192.81ms p(95)=209.54ms p(99.9)=698.76ms
     http_reqs......................: 35252   288.62489/s
     iteration_duration.............: avg=170.75ms min=30.27ms med=156.69ms max=782.2ms  p(90)=193.23ms p(95)=210.15ms p(99.9)=699.12ms
     iterations.....................: 35152   287.806142/s
     success_rate...................: 100.00% ✓ 35152      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 97869      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   321 kB/s
     http_req_blocked...............: avg=5.89µs   min=1.15µs  med=3.04µs   max=3.38ms   p(90)=4.33µs   p(95)=4.84µs   p(99.9)=1.25ms  
     http_req_connecting............: avg=2.66µs   min=0s      med=0s       max=3.34ms   p(90)=0s       p(95)=0s       p(99.9)=1.22ms  
     http_req_duration..............: avg=183.23ms min=22.58ms med=186.99ms max=384.24ms p(90)=198.55ms p(95)=203.6ms  p(99.9)=269.43ms
       { expected_response:true }...: avg=183.23ms min=22.58ms med=186.99ms max=384.24ms p(90)=198.55ms p(95)=203.6ms  p(99.9)=269.43ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32723
     http_req_receiving.............: avg=91.68µs  min=30.47µs med=86.62µs  max=41.71ms  p(90)=115.64µs p(95)=126.36µs p(99.9)=475.6µs 
     http_req_sending...............: avg=21.5µs   min=4.87µs  med=16.13µs  max=54.79ms  p(90)=20.23µs  p(95)=21.99µs  p(99.9)=512.53µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.12ms min=22.45ms med=186.88ms max=383.73ms p(90)=198.45ms p(95)=203.49ms p(99.9)=269.23ms
     http_reqs......................: 32723   266.990344/s
     iteration_duration.............: avg=184.01ms min=49.12ms med=187.28ms max=403.36ms p(90)=198.83ms p(95)=203.88ms p(99.9)=273.21ms
     iterations.....................: 32623   266.174433/s
     success_rate...................: 100.00% ✓ 32623      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

