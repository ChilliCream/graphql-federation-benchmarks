## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-fed-aot-11 | 16.8.0-p.18 | 3,603 | 3,608 | 3,581 | 0.3% | 118 MB | 33.5 KB |  |
| fusion-aot-11 | 16.7.7 | 3,602 | 3,641 | 3,581 | 0.7% | 111 MB | 31.4 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.18 | 3,595 | 3,603 | 3,585 | 0.2% | 367 MB | 104.4 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.18 | 3,571 | 3,595 | 3,562 | 0.3% | 110 MB | 31.6 KB |  |
| fusion-net-11 | 16.7.7 | 3,567 | 3,586 | 3,547 | 0.4% | 365 MB | 104.6 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 3,558 | 3,571 | 3,557 | 0.2% | 110 MB | 31.6 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.18 | 3,537 | 3,548 | 3,519 | 0.3% | 369 MB | 107.0 KB |  |
| fusion-fed-net-11 | 16.7.7 | 3,516 | 3,517 | 3,501 | 0.2% | 371 MB | 108.2 KB |  |
| feddi-gateway | 2026-11-03-0517 | 3,484 | 3,518 | 3,451 | 0.7% | 2,308 MB | 678.3 KB |  |
| hive-router | v0.3.17 | 3,368 | 3,377 | 3,352 | 0.3% | 90 MB | 27.3 KB |  |
| hive-router-nightly | v0.3.19-nightly.9fc3d405 | 3,363 | 3,374 | 3,332 | 0.5% | 94 MB | 28.5 KB |  |
| caliban | 3.2.1 | 1,482 | 1,483 | 1,479 | 0.1% | 6,632 MB | 4,582.3 KB |  |
| grafbase | 0.53.5 | 1,434 | 1,440 | 1,419 | 0.6% | 100 MB | 71.3 KB |  |
| cosmo | 0.373.0 | 1,416 | 1,417 | 1,415 | 0.1% | 151 MB | 109.4 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 592 | 595 | 591 | 0.3% | 2,602 MB | 4,500.8 KB |  |
| apollo-router | v2.19.1 | 491 | 492 | 491 | 0.1% | 181 MB | 376.7 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.e028e66f | 468 | 469 | 468 | 0.1% | 199 MB | 435.0 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 419 | 419 | 418 | 0.1% | 203 MB | 495.6 KB |  |
| hive-gateway | 2.15.10 | 287 | 288 | 286 | 0.3% | 3,425 MB | 12,221.1 KB |  |
| apollo-gateway | 2.14.4 | 263 | 263 | 262 | 0.2% | 2,148 MB | 8,363.3 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.18)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1307169     ✗ 0     
     data_received..................: 38 GB   315 MB/s
     data_sent......................: 524 MB  4.3 MB/s
     http_req_blocked...............: avg=2.37µs  min=802ns   med=1.87µs  max=3.52ms   p(90)=2.99µs  p(95)=3.65µs   p(99.9)=23.95µs
     http_req_connecting............: avg=196ns   min=0s      med=0s      max=3.48ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.56ms min=8.24ms  med=13.16ms max=284.78ms p(90)=16.58ms p(95)=17.82ms  p(99.9)=24.97ms
       { expected_response:true }...: avg=13.56ms min=8.24ms  med=13.16ms max=284.78ms p(90)=16.58ms p(95)=17.82ms  p(99.9)=24.97ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 435823
     http_req_receiving.............: avg=68.79µs min=23.99µs med=44.04µs max=122.73ms p(90)=90.63µs p(95)=170.29µs p(99.9)=1.76ms 
     http_req_sending...............: avg=31.32µs min=4.13µs  med=8.1µs   max=84.78ms  p(90)=16.06µs p(95)=93.78µs  p(99.9)=1.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.46ms min=8.17ms  med=13.06ms max=284.24ms p(90)=16.47ms p(95)=17.69ms  p(99.9)=24.74ms
     http_reqs......................: 435823  3603.200339/s
     iteration_duration.............: avg=13.76ms min=8.37ms  med=13.35ms max=294.05ms p(90)=16.78ms p(95)=18.01ms  p(99.9)=25.2ms 
     iterations.....................: 435723  3602.373581/s
     success_rate...................: 100.00% ✓ 435723      ✗ 0     
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

     checks.........................: 100.00% ✓ 1307088     ✗ 0     
     data_received..................: 38 GB   315 MB/s
     data_sent......................: 524 MB  4.3 MB/s
     http_req_blocked...............: avg=2.86µs  min=912ns   med=2.28µs  max=3.98ms   p(90)=3.63µs  p(95)=4.38µs   p(99.9)=31.4µs 
     http_req_connecting............: avg=218ns   min=0s      med=0s      max=3.94ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.56ms min=8.12ms  med=13.1ms  max=279.48ms p(90)=16.7ms  p(95)=18.02ms  p(99.9)=25.5ms 
       { expected_response:true }...: avg=13.56ms min=8.12ms  med=13.1ms  max=279.48ms p(90)=16.7ms  p(95)=18.02ms  p(99.9)=25.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 435796
     http_req_receiving.............: avg=73.81µs min=24.32µs med=45.64µs max=128.38ms p(90)=96.23µs p(95)=190.3µs  p(99.9)=2.03ms 
     http_req_sending...............: avg=34.03µs min=4.57µs  med=8.67µs  max=126.58ms p(90)=17.33µs p(95)=102.79µs p(99.9)=1.88ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.45ms min=8.05ms  med=13ms    max=279.09ms p(90)=16.57ms p(95)=17.87ms  p(99.9)=25.27ms
     http_reqs......................: 435796  3602.878857/s
     iteration_duration.............: avg=13.76ms min=8.26ms  med=13.3ms  max=297.1ms  p(90)=16.9ms  p(95)=18.22ms  p(99.9)=25.73ms
     iterations.....................: 435696  3602.052122/s
     success_rate...................: 100.00% ✓ 435696      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.18)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1304439     ✗ 0     
     data_received..................: 38 GB   315 MB/s
     data_sent......................: 523 MB  4.3 MB/s
     http_req_blocked...............: avg=3.1µs   min=882ns   med=2.32µs  max=7.08ms   p(90)=3.73µs   p(95)=4.55µs   p(99.9)=33.89µs
     http_req_connecting............: avg=391ns   min=0s      med=0s      max=7.04ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.58ms min=8.19ms  med=13.14ms max=289.33ms p(90)=16.79ms  p(95)=18.11ms  p(99.9)=26.27ms
       { expected_response:true }...: avg=13.58ms min=8.19ms  med=13.14ms max=289.33ms p(90)=16.79ms  p(95)=18.11ms  p(99.9)=26.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 434913
     http_req_receiving.............: avg=74.04µs min=23.48µs med=46.49µs max=18.83ms  p(90)=100.14µs p(95)=188.16µs p(99.9)=1.99ms 
     http_req_sending...............: avg=34.22µs min=4.34µs  med=8.67µs  max=221.1ms  p(90)=17.39µs  p(95)=101.41µs p(99.9)=2.01ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.48ms min=8.13ms  med=13.04ms max=288.78ms p(90)=16.66ms  p(95)=17.97ms  p(99.9)=25.99ms
     http_reqs......................: 434913  3595.970324/s
     iteration_duration.............: avg=13.78ms min=8.33ms  med=13.34ms max=301.69ms p(90)=16.98ms  p(95)=18.31ms  p(99.9)=26.68ms
     iterations.....................: 434813  3595.143499/s
     success_rate...................: 100.00% ✓ 434813      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.18)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1295631     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 519 MB  4.3 MB/s
     http_req_blocked...............: avg=2.86µs  min=861ns   med=2.31µs  max=3.85ms   p(90)=3.62µs  p(95)=4.32µs   p(99.9)=32.91µs
     http_req_connecting............: avg=200ns   min=0s      med=0s      max=3.48ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.68ms min=8.22ms  med=13.24ms max=286.25ms p(90)=16.84ms p(95)=18.15ms  p(99.9)=25.91ms
       { expected_response:true }...: avg=13.68ms min=8.22ms  med=13.24ms max=286.25ms p(90)=16.84ms p(95)=18.15ms  p(99.9)=25.91ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 431977
     http_req_receiving.............: avg=73.02µs min=24.47µs med=46.06µs max=75.34ms  p(90)=97.3µs  p(95)=190.04µs p(99.9)=1.81ms 
     http_req_sending...............: avg=34.21µs min=4.38µs  med=8.76µs  max=140.01ms p(90)=17.49µs p(95)=102.43µs p(99.9)=1.82ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.57ms min=8.16ms  med=13.13ms max=277.91ms p(90)=16.72ms p(95)=18.02ms  p(99.9)=25.64ms
     http_reqs......................: 431977  3571.438572/s
     iteration_duration.............: avg=13.88ms min=8.37ms  med=13.43ms max=298.64ms p(90)=17.04ms p(95)=18.35ms  p(99.9)=26.11ms
     iterations.....................: 431877  3570.611806/s
     success_rate...................: 100.00% ✓ 431877      ✗ 0     
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

     checks.........................: 100.00% ✓ 1294308     ✗ 0     
     data_received..................: 38 GB   312 MB/s
     data_sent......................: 519 MB  4.3 MB/s
     http_req_blocked...............: avg=2.7µs   min=782ns  med=1.84µs  max=8.01ms   p(90)=3.01µs  p(95)=3.69µs   p(99.9)=24.04µs
     http_req_connecting............: avg=505ns   min=0s     med=0s      max=7.77ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.7ms  min=8.22ms med=13.3ms  max=254.16ms p(90)=16.84ms p(95)=18.08ms  p(99.9)=25.6ms 
       { expected_response:true }...: avg=13.7ms  min=8.22ms med=13.3ms  max=254.16ms p(90)=16.84ms p(95)=18.08ms  p(99.9)=25.6ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 431536
     http_req_receiving.............: avg=68.03µs min=23.6µs med=42.31µs max=101.4ms  p(90)=90.36µs p(95)=173.88µs p(99.9)=1.81ms 
     http_req_sending...............: avg=31.48µs min=4.28µs med=7.93µs  max=162.51ms p(90)=16.38µs p(95)=93.11µs  p(99.9)=1.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.6ms  min=8.15ms med=13.21ms max=252.97ms p(90)=16.74ms p(95)=17.96ms  p(99.9)=25.35ms
     http_reqs......................: 431536  3567.873479/s
     iteration_duration.............: avg=13.89ms min=8.37ms med=13.49ms max=279.66ms p(90)=17.03ms p(95)=18.26ms  p(99.9)=25.8ms 
     iterations.....................: 431436  3567.046694/s
     success_rate...................: 100.00% ✓ 431436      ✗ 0     
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

     checks.........................: 100.00% ✓ 1291062     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.47µs  min=762ns  med=1.9µs   max=4.44ms   p(90)=3.08µs  p(95)=3.78µs   p(99.9)=25.92µs
     http_req_connecting............: avg=223ns   min=0s     med=0s      max=4.4ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.73ms min=8.15ms med=13.32ms max=278.47ms p(90)=16.86ms p(95)=18.13ms  p(99.9)=25.33ms
       { expected_response:true }...: avg=13.73ms min=8.15ms med=13.32ms max=278.47ms p(90)=16.86ms p(95)=18.13ms  p(99.9)=25.33ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 430454
     http_req_receiving.............: avg=69.95µs min=24.5µs med=44.56µs max=226.79ms p(90)=92.04µs p(95)=174.55µs p(99.9)=1.74ms 
     http_req_sending...............: avg=31.54µs min=4.35µs med=8.18µs  max=143.8ms  p(90)=16.64µs p(95)=94.46µs  p(99.9)=1.68ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.63ms min=8.08ms med=13.22ms max=262.58ms p(90)=16.74ms p(95)=18.01ms  p(99.9)=25.14ms
     http_reqs......................: 430454  3558.689824/s
     iteration_duration.............: avg=13.93ms min=8.36ms med=13.51ms max=286.79ms p(90)=17.05ms p(95)=18.32ms  p(99.9)=25.58ms
     iterations.....................: 430354  3557.863094/s
     success_rate...................: 100.00% ✓ 430354      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.18)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1283301     ✗ 0     
     data_received..................: 37 GB   310 MB/s
     data_sent......................: 514 MB  4.3 MB/s
     http_req_blocked...............: avg=2.92µs  min=952ns   med=2.33µs  max=4.1ms    p(90)=3.7µs   p(95)=4.46µs   p(99.9)=31.51µs
     http_req_connecting............: avg=226ns   min=0s      med=0s      max=4.06ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.81ms min=8.13ms  med=13.38ms max=281.53ms p(90)=17.08ms p(95)=18.4ms   p(99.9)=26.59ms
       { expected_response:true }...: avg=13.81ms min=8.13ms  med=13.38ms max=281.53ms p(90)=17.08ms p(95)=18.4ms   p(99.9)=26.59ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 427867
     http_req_receiving.............: avg=73.82µs min=23.79µs med=45µs    max=233.19ms p(90)=95.9µs  p(95)=186.84µs p(99.9)=2.15ms 
     http_req_sending...............: avg=34.88µs min=4.5µs   med=8.77µs  max=169.34ms p(90)=17.49µs p(95)=101.92µs p(99.9)=2ms    
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.7ms  min=8.08ms  med=13.27ms max=273.65ms p(90)=16.96ms p(95)=18.26ms  p(99.9)=26.31ms
     http_reqs......................: 427867  3537.578581/s
     iteration_duration.............: avg=14.01ms min=8.28ms  med=13.58ms max=308.74ms p(90)=17.28ms p(95)=18.6ms   p(99.9)=26.82ms
     iterations.....................: 427767  3536.751788/s
     success_rate...................: 100.00% ✓ 427767      ✗ 0     
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

     checks.........................: 100.00% ✓ 1275546     ✗ 0     
     data_received..................: 37 GB   308 MB/s
     data_sent......................: 511 MB  4.2 MB/s
     http_req_blocked...............: avg=2.81µs  min=771ns   med=1.84µs  max=8.55ms   p(90)=3.05µs  p(95)=3.8µs    p(99.9)=25.64µs
     http_req_connecting............: avg=604ns   min=0s      med=0s      max=8.51ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.9ms  min=8.21ms  med=13.5ms  max=261.03ms p(90)=17.09ms p(95)=18.35ms  p(99.9)=25.45ms
       { expected_response:true }...: avg=13.9ms  min=8.21ms  med=13.5ms  max=261.03ms p(90)=17.09ms p(95)=18.35ms  p(99.9)=25.45ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 425282
     http_req_receiving.............: avg=69.66µs min=24.55µs med=44.91µs max=51.98ms  p(90)=93.77µs p(95)=169.32µs p(99.9)=1.8ms  
     http_req_sending...............: avg=31.08µs min=3.86µs  med=7.88µs  max=244.55ms p(90)=15.84µs p(95)=91.18µs  p(99.9)=1.74ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.8ms  min=8.15ms  med=13.41ms max=260.92ms p(90)=16.99ms p(95)=18.23ms  p(99.9)=25.25ms
     http_reqs......................: 425282  3516.143602/s
     iteration_duration.............: avg=14.1ms  min=8.4ms   med=13.7ms  max=280.73ms p(90)=17.28ms p(95)=18.53ms  p(99.9)=25.68ms
     iterations.....................: 425182  3515.316823/s
     success_rate...................: 100.00% ✓ 425182      ✗ 0     
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

     checks.........................: 100.00% ✓ 1264053     ✗ 0     
     data_received..................: 37 GB   305 MB/s
     data_sent......................: 507 MB  4.2 MB/s
     http_req_blocked...............: avg=2.43µs  min=812ns   med=1.9µs   max=4.97ms   p(90)=3.09µs  p(95)=3.76µs   p(99.9)=25.43µs
     http_req_connecting............: avg=187ns   min=0s      med=0s      max=4.85ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.04ms min=8.26ms  med=13.72ms max=270.9ms  p(90)=16.96ms p(95)=18.11ms  p(99.9)=25.4ms 
       { expected_response:true }...: avg=14.04ms min=8.26ms  med=13.72ms max=270.9ms  p(90)=16.96ms p(95)=18.11ms  p(99.9)=25.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 421451
     http_req_receiving.............: avg=65.4µs  min=23.52µs med=42.74µs max=98.79ms  p(90)=86.11µs p(95)=160.31µs p(99.9)=1.57ms 
     http_req_sending...............: avg=30.9µs  min=4.48µs  med=8.13µs  max=144.75ms p(90)=15.84µs p(95)=91.76µs  p(99.9)=1.71ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.94ms min=8.18ms  med=13.63ms max=268.81ms p(90)=16.86ms p(95)=18ms     p(99.9)=25.18ms
     http_reqs......................: 421451  3484.629095/s
     iteration_duration.............: avg=14.23ms min=8.4ms   med=13.9ms  max=290.95ms p(90)=17.15ms p(95)=18.3ms   p(99.9)=25.65ms
     iterations.....................: 421351  3483.802278/s
     success_rate...................: 100.00% ✓ 421351      ✗ 0     
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

     checks.........................: 100.00% ✓ 1222041     ✗ 0     
     data_received..................: 36 GB   295 MB/s
     data_sent......................: 490 MB  4.0 MB/s
     http_req_blocked...............: avg=2.98µs  min=942ns   med=2.38µs  max=4.29ms   p(90)=3.89µs   p(95)=4.73µs   p(99.9)=32.83µs
     http_req_connecting............: avg=172ns   min=0s      med=0s      max=4.25ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.52ms min=8.65ms  med=14.12ms max=295.93ms p(90)=17.71ms  p(95)=19.05ms  p(99.9)=27.56ms
       { expected_response:true }...: avg=14.52ms min=8.65ms  med=14.12ms max=295.93ms p(90)=17.71ms  p(95)=19.05ms  p(99.9)=27.56ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 407447
     http_req_receiving.............: avg=73.9µs  min=23.82µs med=47.23µs max=21.48ms  p(90)=100.25µs p(95)=194.25µs p(99.9)=1.76ms 
     http_req_sending...............: avg=33.38µs min=4.55µs  med=8.86µs  max=60.01ms  p(90)=18.19µs  p(95)=103.88µs p(99.9)=1.86ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.41ms min=8.59ms  med=14.02ms max=295.83ms p(90)=17.6ms   p(95)=18.91ms  p(99.9)=27.32ms
     http_reqs......................: 407447  3368.115056/s
     iteration_duration.............: avg=14.71ms min=8.84ms  med=14.31ms max=308.66ms p(90)=17.91ms  p(95)=19.24ms  p(99.9)=27.78ms
     iterations.....................: 407347  3367.288417/s
     success_rate...................: 100.00% ✓ 407347      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.19-nightly.9fc3d405)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1220298     ✗ 0     
     data_received..................: 36 GB   294 MB/s
     data_sent......................: 489 MB  4.0 MB/s
     http_req_blocked...............: avg=3.19µs  min=922ns  med=2.41µs  max=9.17ms   p(90)=4.06µs  p(95)=5µs      p(99.9)=33.37µs
     http_req_connecting............: avg=344ns   min=0s     med=0s      max=9.15ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.53ms min=8.43ms med=14.14ms max=305.49ms p(90)=17.75ms p(95)=19.08ms  p(99.9)=27.35ms
       { expected_response:true }...: avg=14.53ms min=8.43ms med=14.14ms max=305.49ms p(90)=17.75ms p(95)=19.08ms  p(99.9)=27.35ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 406866
     http_req_receiving.............: avg=75.17µs min=23.8µs med=46.8µs  max=15.59ms  p(90)=105.4µs p(95)=197.43µs p(99.9)=1.98ms 
     http_req_sending...............: avg=34.77µs min=4.37µs med=9.12µs  max=51.88ms  p(90)=19.92µs p(95)=105.74µs p(99.9)=2.04ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.43ms min=8.39ms med=14.04ms max=304.36ms p(90)=17.63ms p(95)=18.94ms  p(99.9)=27.1ms 
     http_reqs......................: 406866  3363.231359/s
     iteration_duration.............: avg=14.74ms min=8.62ms med=14.34ms max=320.92ms p(90)=17.94ms p(95)=19.28ms  p(99.9)=27.59ms
     iterations.....................: 406766  3362.404741/s
     success_rate...................: 100.00% ✓ 406766      ✗ 0     
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

     checks.........................: 100.00% ✓ 541989      ✗ 0     
     data_received..................: 16 GB   130 MB/s
     data_sent......................: 217 MB  1.8 MB/s
     http_req_blocked...............: avg=3.94µs  min=961ns   med=2.38µs  max=7.48ms   p(90)=4.17µs  p(95)=4.97µs   p(99.9)=35.44µs 
     http_req_connecting............: avg=1.13µs  min=0s      med=0s      max=7.46ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.98ms min=17.84ms med=32.48ms max=296.33ms p(90)=38.54ms p(95)=40.63ms  p(99.9)=57.6ms  
       { expected_response:true }...: avg=32.98ms min=17.84ms med=32.48ms max=296.33ms p(90)=38.54ms p(95)=40.63ms  p(99.9)=57.6ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 180763
     http_req_receiving.............: avg=72.08µs min=26.19µs med=60.25µs max=7.13ms   p(90)=99.62µs p(95)=117.74µs p(99.9)=804.23µs
     http_req_sending...............: avg=21.8µs  min=4.7µs   med=11µs    max=96.79ms  p(90)=18.03µs p(95)=22.16µs  p(99.9)=786.91µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.88ms min=17.78ms med=32.38ms max=294.21ms p(90)=38.44ms p(95)=40.53ms  p(99.9)=57.26ms 
     http_reqs......................: 180763  1482.188149/s
     iteration_duration.............: avg=33.2ms  min=20.84ms med=32.68ms max=309.95ms p(90)=38.74ms p(95)=40.84ms  p(99.9)=58.41ms 
     iterations.....................: 180663  1481.368187/s
     success_rate...................: 100.00% ✓ 180663      ✗ 0     
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

     checks.........................: 100.00% ✓ 524496      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 210 MB  1.7 MB/s
     http_req_blocked...............: avg=3.63µs  min=842ns   med=2.57µs  max=9.31ms   p(90)=4.81µs   p(95)=5.76µs   p(99.9)=40.9µs 
     http_req_connecting............: avg=549ns   min=0s      med=0s      max=9.28ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.05ms min=17.57ms med=33.75ms max=313.28ms p(90)=39.76ms  p(95)=41.54ms  p(99.9)=50ms   
       { expected_response:true }...: avg=34.05ms min=17.57ms med=33.75ms max=313.28ms p(90)=39.76ms  p(95)=41.54ms  p(99.9)=50ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 174932
     http_req_receiving.............: avg=83.08µs min=26.57µs med=57.75µs max=177.89ms p(90)=119.16µs p(95)=162.77µs p(99.9)=1.41ms 
     http_req_sending...............: avg=32.59µs min=4.5µs   med=10.04µs max=255.12ms p(90)=21.78µs  p(95)=45.16µs  p(99.9)=1.36ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.93ms min=17.49ms med=33.64ms max=312.96ms p(90)=39.65ms  p(95)=41.42ms  p(99.9)=49.65ms
     http_reqs......................: 174932  1434.622476/s
     iteration_duration.............: avg=34.3ms  min=20.83ms med=33.99ms max=322.14ms p(90)=39.98ms  p(95)=41.76ms  p(99.9)=50.28ms
     iterations.....................: 174832  1433.802373/s
     success_rate...................: 100.00% ✓ 174832      ✗ 0     
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

     checks.........................: 100.00% ✓ 518046      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 208 MB  1.7 MB/s
     http_req_blocked...............: avg=3.61µs  min=1.05µs  med=2.7µs   max=3.67ms   p(90)=4.35µs   p(95)=5.1µs    p(99.9)=35.03µs 
     http_req_connecting............: avg=589ns   min=0s      med=0s      max=3.63ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.51ms min=18.07ms med=33.95ms max=294.48ms p(90)=41.16ms  p(95)=43.48ms  p(99.9)=56.23ms 
       { expected_response:true }...: avg=34.51ms min=18.07ms med=33.95ms max=294.48ms p(90)=41.16ms  p(95)=43.48ms  p(99.9)=56.23ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 172782
     http_req_receiving.............: avg=74.78µs min=26.01µs med=62.02µs max=52.8ms   p(90)=101.23µs p(95)=120.31µs p(99.9)=785.59µs
     http_req_sending...............: avg=23.73µs min=4.85µs  med=11.29µs max=183.1ms  p(90)=18.14µs  p(95)=22.53µs  p(99.9)=806.24µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.42ms min=17.9ms  med=33.86ms max=294.17ms p(90)=41.07ms  p(95)=43.39ms  p(99.9)=56.04ms 
     http_reqs......................: 172782  1416.605127/s
     iteration_duration.............: avg=34.73ms min=20.84ms med=34.16ms max=316.03ms p(90)=41.37ms  p(95)=43.69ms  p(99.9)=56.47ms 
     iterations.....................: 172682  1415.785247/s
     success_rate...................: 100.00% ✓ 172682      ✗ 0     
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

     checks.........................: 100.00% ✓ 217071     ✗ 0    
     data_received..................: 6.3 GB  52 MB/s
     data_sent......................: 87 MB   712 kB/s
     http_req_blocked...............: avg=6.73µs  min=1.11µs  med=3.07µs  max=8.9ms    p(90)=4.6µs    p(95)=5.29µs   p(99.9)=49.01µs 
     http_req_connecting............: avg=3.29µs  min=0s      med=0s      max=8.71ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=82.59ms min=20.14ms med=80.88ms max=330.49ms p(90)=95.66ms  p(95)=104.21ms p(99.9)=197.88ms
       { expected_response:true }...: avg=82.59ms min=20.14ms med=80.88ms max=330.49ms p(90)=95.66ms  p(95)=104.21ms p(99.9)=197.88ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 72457
     http_req_receiving.............: avg=83.73µs min=29.88µs med=74.87µs max=148.83ms p(90)=108.51µs p(95)=120.94µs p(99.9)=572.71µs
     http_req_sending...............: avg=23.13µs min=5.1µs   med=14.87µs max=102.43ms p(90)=20.51µs  p(95)=22.63µs  p(99.9)=571.26µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=82.49ms min=19.96ms med=80.78ms max=329.96ms p(90)=95.56ms  p(95)=104.08ms p(99.9)=197.6ms 
     http_reqs......................: 72457   592.94064/s
     iteration_duration.............: avg=82.93ms min=28.46ms med=81.12ms max=350.83ms p(90)=95.91ms  p(95)=104.54ms p(99.9)=199.26ms
     iterations.....................: 72357   592.122305/s
     success_rate...................: 100.00% ✓ 72357      ✗ 0    
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

     checks.........................: 100.00% ✓ 179727     ✗ 0    
     data_received..................: 5.2 GB  43 MB/s
     data_sent......................: 72 MB   590 kB/s
     http_req_blocked...............: avg=3.72µs   min=1.09µs  med=2.73µs  max=1.97ms   p(90)=4.15µs   p(95)=4.72µs   p(99.9)=51.9µs  
     http_req_connecting............: avg=784ns    min=0s      med=0s      max=1.95ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=99.79ms  min=19.85ms med=97.91ms max=312.18ms p(90)=126.48ms p(95)=135.48ms p(99.9)=172.37ms
       { expected_response:true }...: avg=99.79ms  min=19.85ms med=97.91ms max=312.18ms p(90)=126.48ms p(95)=135.48ms p(99.9)=172.37ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 60009
     http_req_receiving.............: avg=76.4µs   min=28.89µs med=70.22µs max=58.4ms   p(90)=101.82µs p(95)=113.44µs p(99.9)=523.87µs
     http_req_sending...............: avg=22.58µs  min=5.14µs  med=13.34µs max=112.59ms p(90)=18.92µs  p(95)=20.82µs  p(99.9)=427.45µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=99.69ms  min=19.73ms med=97.82ms max=311.91ms p(90)=126.39ms p(95)=135.37ms p(99.9)=171.82ms
     http_reqs......................: 60009   491.036212/s
     iteration_duration.............: avg=100.16ms min=28.43ms med=98.18ms max=320.87ms p(90)=126.75ms p(95)=135.72ms p(99.9)=173.7ms 
     iterations.....................: 59909   490.217941/s
     success_rate...................: 100.00% ✓ 59909      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-nightly (HotChocolate subgraphs) (v3.0.0-preview.0-nightly.e028e66f)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 171393     ✗ 0    
     data_received..................: 5.0 GB  41 MB/s
     data_sent......................: 69 MB   562 kB/s
     http_req_blocked...............: avg=4.4µs    min=1.06µs  med=2.46µs   max=4.3ms    p(90)=3.89µs   p(95)=4.45µs   p(99.9)=46.73µs 
     http_req_connecting............: avg=1.67µs   min=0s      med=0s       max=4.25ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=104.67ms min=19.76ms med=103.21ms max=329.64ms p(90)=131.17ms p(95)=140.26ms p(99.9)=181.67ms
       { expected_response:true }...: avg=104.67ms min=19.76ms med=103.21ms max=329.64ms p(90)=131.17ms p(95)=140.26ms p(99.9)=181.67ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 57231
     http_req_receiving.............: avg=73.59µs  min=28.96µs med=66.42µs  max=62.52ms  p(90)=99.78µs  p(95)=112.22µs p(99.9)=501.94µs
     http_req_sending...............: avg=18.62µs  min=4.92µs  med=12.9µs   max=59.66ms  p(90)=19.02µs  p(95)=20.96µs  p(99.9)=506.35µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=104.58ms min=19.68ms med=103.11ms max=329.52ms p(90)=131.09ms p(95)=140.18ms p(99.9)=181.18ms
     http_reqs......................: 57231   468.236229/s
     iteration_duration.............: avg=105.05ms min=33.95ms med=103.46ms max=338.37ms p(90)=131.42ms p(95)=140.52ms p(99.9)=182.92ms
     iterations.....................: 57131   467.418077/s
     success_rate...................: 100.00% ✓ 57131      ✗ 0    
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

     checks.........................: 100.00% ✓ 153525     ✗ 0    
     data_received..................: 4.5 GB  37 MB/s
     data_sent......................: 62 MB   503 kB/s
     http_req_blocked...............: avg=5.24µs   min=1.11µs  med=3.27µs   max=3.6ms    p(90)=4.73µs   p(95)=5.34µs   p(99.9)=106.6µs 
     http_req_connecting............: avg=1.74µs   min=0s      med=0s       max=3.57ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=116.81ms min=20.85ms med=115.18ms max=342.53ms p(90)=143.98ms p(95)=153.63ms p(99.9)=201.46ms
       { expected_response:true }...: avg=116.81ms min=20.85ms med=115.18ms max=342.53ms p(90)=143.98ms p(95)=153.63ms p(99.9)=201.46ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51275
     http_req_receiving.............: avg=83.27µs  min=27.21µs med=76.74µs  max=75.91ms  p(90)=108.77µs p(95)=121.01µs p(99.9)=534.1µs 
     http_req_sending...............: avg=26.95µs  min=5.47µs  med=15.89µs  max=123.22ms p(90)=21.57µs  p(95)=23.63µs  p(99.9)=534.75µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=116.7ms  min=20.72ms med=115.08ms max=328.89ms p(90)=143.86ms p(95)=153.51ms p(99.9)=200.61ms
     http_reqs......................: 51275   419.20261/s
     iteration_duration.............: avg=117.27ms min=38.46ms med=115.46ms max=348.18ms p(90)=144.26ms p(95)=153.95ms p(99.9)=204.69ms
     iterations.....................: 51175   418.385053/s
     success_rate...................: 100.00% ✓ 51175      ✗ 0    
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

     checks.........................: 100.00% ✓ 104919     ✗ 0    
     data_received..................: 3.1 GB  25 MB/s
     data_sent......................: 42 MB   345 kB/s
     http_req_blocked...............: avg=6.27µs   min=1.15µs  med=3.1µs    max=7.68ms   p(90)=4.48µs   p(95)=5.1µs    p(99.9)=705.2µs 
     http_req_connecting............: avg=2.43µs   min=0s      med=0s       max=5.34ms   p(90)=0s       p(95)=0s       p(99.9)=498.06µs
     http_req_duration..............: avg=170.93ms min=17.3ms  med=156.04ms max=746.11ms p(90)=193.55ms p(95)=210.9ms  p(99.9)=693.63ms
       { expected_response:true }...: avg=170.93ms min=17.3ms  med=156.04ms max=746.11ms p(90)=193.55ms p(95)=210.9ms  p(99.9)=693.63ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 35073
     http_req_receiving.............: avg=93.67µs  min=31.61µs med=88.9µs   max=29.75ms  p(90)=118.67µs p(95)=130.27µs p(99.9)=835.87µs
     http_req_sending...............: avg=34.21µs  min=5.56µs  med=17.15µs  max=93.58ms  p(90)=21.59µs  p(95)=23.34µs  p(99.9)=894.64µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=170.8ms  min=17.19ms med=155.93ms max=746.04ms p(90)=193.44ms p(95)=210.79ms p(99.9)=693.54ms
     http_reqs......................: 35073   287.240014/s
     iteration_duration.............: avg=171.64ms min=41.03ms med=156.38ms max=746.28ms p(90)=193.89ms p(95)=211.37ms p(99.9)=693.94ms
     iterations.....................: 34973   286.421036/s
     success_rate...................: 100.00% ✓ 34973      ✗ 0    
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

     checks.........................: 100.00% ✓ 96741      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   317 kB/s
     http_req_blocked...............: avg=8.94µs   min=1.07µs  med=2.96µs   max=83.74ms  p(90)=4.23µs   p(95)=4.72µs   p(99.9)=1.62ms  
     http_req_connecting............: avg=3.19µs   min=0s      med=0s       max=4.26ms   p(90)=0s       p(95)=0s       p(99.9)=1.53ms  
     http_req_duration..............: avg=185.36ms min=22.8ms  med=178.65ms max=385.56ms p(90)=209.35ms p(95)=215.55ms p(99.9)=277.38ms
       { expected_response:true }...: avg=185.36ms min=22.8ms  med=178.65ms max=385.56ms p(90)=209.35ms p(95)=215.55ms p(99.9)=277.38ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32347
     http_req_receiving.............: avg=85.45µs  min=32.68µs med=82.8µs   max=15.49ms  p(90)=111.49µs p(95)=122.1µs  p(99.9)=446.32µs
     http_req_sending...............: avg=30.99µs  min=4.86µs  med=15.47µs  max=149.86ms p(90)=19.52µs  p(95)=21.19µs  p(99.9)=546.45µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=185.25ms min=22.71ms med=178.56ms max=384.9ms  p(90)=209.24ms p(95)=215.42ms p(99.9)=277.29ms
     http_reqs......................: 32347   263.876523/s
     iteration_duration.............: avg=186.15ms min=42.46ms med=178.93ms max=393.19ms p(90)=209.63ms p(95)=215.88ms p(99.9)=279.62ms
     iterations.....................: 32247   263.060755/s
     success_rate...................: 100.00% ✓ 32247      ✗ 0    
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

