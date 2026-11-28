## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| nitro-router | 16.8.0-p.25 | 3,613 | 3,636 | 3,593 | 0.5% | 148 MB | 42.0 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.25 | 3,607 | 3,617 | 3,595 | 0.2% | 97 MB | 27.5 KB |  |
| fusion-aot-11 | 16.7.7 | 3,593 | 3,603 | 3,565 | 0.4% | 111 MB | 31.8 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.25 | 3,593 | 3,611 | 3,574 | 0.4% | 349 MB | 99.6 KB |  |
| nitro-router-fed | 16.8.0-p.25 | 3,578 | 3,581 | 3,555 | 0.3% | 149 MB | 42.5 KB |  |
| fusion-fed-net-11 | 16.7.7 | 3,559 | 3,571 | 3,551 | 0.2% | 370 MB | 106.5 KB |  |
| fusion-net-11 | 16.7.7 | 3,558 | 3,576 | 3,553 | 0.3% | 358 MB | 102.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.25 | 3,555 | 3,582 | 3,539 | 0.5% | 96 MB | 27.7 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 3,550 | 3,553 | 3,545 | 0.1% | 110 MB | 31.7 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.25 | 3,542 | 3,554 | 3,531 | 0.2% | 356 MB | 102.8 KB |  |
| feddi-gateway | 2026-11-22-1912 | 3,534 | 3,551 | 3,519 | 0.4% | 2,309 MB | 669.1 KB |  |
| hive-router-nightly | v0.3.21-nightly.f689b548 | 3,344 | 3,354 | 3,331 | 0.3% | 89 MB | 27.2 KB |  |
| hive-router | v0.3.21 | 3,332 | 3,354 | 3,320 | 0.4% | 88 MB | 27.2 KB |  |
| caliban | 3.2.1 | 1,531 | 1,534 | 1,526 | 0.2% | 5,727 MB | 3,830.2 KB |  |
| grafbase | 0.53.5 | 1,430 | 1,441 | 1,420 | 0.6% | 100 MB | 71.8 KB |  |
| cosmo | 0.378.1 | 1,410 | 1,414 | 1,409 | 0.2% | 152 MB | 110.7 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 603 | 604 | 603 | 0.1% | 2,611 MB | 4,434.1 KB |  |
| apollo-router | v2.19.1 | 486 | 487 | 486 | 0.1% | 175 MB | 368.7 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.95b76d0a | 481 | 481 | 480 | 0.1% | 194 MB | 412.7 KB |  |
| hive-gateway | 2.15.10 | 290 | 293 | 287 | 0.8% | 3,202 MB | 11,305.4 KB |  |
| apollo-gateway | 2.14.4 | 269 | 270 | 269 | 0.2% | 2,168 MB | 8,254.8 KB |  |


### Details

<details>
  <summary>Summary for: nitro-router (HotChocolate subgraphs) (16.8.0-p.25)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1310967     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 525 MB  4.3 MB/s
     http_req_blocked...............: avg=2.49µs  min=801ns   med=1.91µs  max=4.3ms    p(90)=3.16µs  p(95)=3.93µs   p(99.9)=25.39µs
     http_req_connecting............: avg=213ns   min=0s      med=0s      max=4.01ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.52ms min=8.07ms  med=13.1ms  max=284.16ms p(90)=16.65ms p(95)=17.93ms  p(99.9)=25.29ms
       { expected_response:true }...: avg=13.52ms min=8.07ms  med=13.1ms  max=284.16ms p(90)=16.65ms p(95)=17.93ms  p(99.9)=25.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 437089
     http_req_receiving.............: avg=68.36µs min=23.01µs med=42.42µs max=188.78ms p(90)=91.33µs p(95)=171.56µs p(99.9)=1.8ms  
     http_req_sending...............: avg=32.54µs min=4.44µs  med=8.02µs  max=188.6ms  p(90)=16.29µs p(95)=92.78µs  p(99.9)=1.94ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.42ms min=8.01ms  med=13ms    max=283.63ms p(90)=16.54ms p(95)=17.8ms   p(99.9)=25.07ms
     http_reqs......................: 437089  3613.744468/s
     iteration_duration.............: avg=13.72ms min=8.2ms   med=13.29ms max=293.05ms p(90)=16.85ms p(95)=18.12ms  p(99.9)=25.51ms
     iterations.....................: 436989  3612.917693/s
     success_rate...................: 100.00% ✓ 436989      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.25)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1308822     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 524 MB  4.3 MB/s
     http_req_blocked...............: avg=2.7µs   min=842ns   med=2.13µs  max=4.04ms   p(90)=3.45µs  p(95)=4.15µs  p(99.9)=29.73µs
     http_req_connecting............: avg=231ns   min=0s      med=0s      max=3.98ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.54ms min=8.05ms  med=13.1ms  max=290.05ms p(90)=16.72ms p(95)=18.04ms p(99.9)=25.91ms
       { expected_response:true }...: avg=13.54ms min=8.05ms  med=13.1ms  max=290.05ms p(90)=16.72ms p(95)=18.04ms p(99.9)=25.91ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 436374
     http_req_receiving.............: avg=71.63µs min=23.91µs med=43.9µs  max=170.26ms p(90)=93.18µs p(95)=184.3µs p(99.9)=1.99ms 
     http_req_sending...............: avg=33.7µs  min=4.28µs  med=8.38µs  max=189.09ms p(90)=16.65µs p(95)=99.79µs p(99.9)=1.97ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.43ms min=8ms     med=13ms    max=289.95ms p(90)=16.6ms  p(95)=17.9ms  p(99.9)=25.64ms
     http_reqs......................: 436374  3607.918018/s
     iteration_duration.............: avg=13.74ms min=8.23ms  med=13.29ms max=301.08ms p(90)=16.92ms p(95)=18.24ms p(99.9)=26.16ms
     iterations.....................: 436274  3607.091223/s
     success_rate...................: 100.00% ✓ 436274      ✗ 0     
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

     checks.........................: 100.00% ✓ 1303674     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 522 MB  4.3 MB/s
     http_req_blocked...............: avg=2.4µs   min=792ns   med=1.9µs   max=3.03ms   p(90)=3.12µs  p(95)=3.84µs   p(99.9)=23.25µs
     http_req_connecting............: avg=172ns   min=0s      med=0s      max=3.01ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.6ms  min=8.1ms   med=13.19ms max=290.29ms p(90)=16.62ms p(95)=17.85ms  p(99.9)=25.29ms
       { expected_response:true }...: avg=13.6ms  min=8.1ms   med=13.19ms max=290.29ms p(90)=16.62ms p(95)=17.85ms  p(99.9)=25.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 434658
     http_req_receiving.............: avg=68.87µs min=23.76µs med=43.89µs max=147.25ms p(90)=93.27µs p(95)=172.06µs p(99.9)=1.7ms  
     http_req_sending...............: avg=30.5µs  min=4.28µs  med=7.92µs  max=178.66ms p(90)=16.41µs p(95)=93.7µs   p(99.9)=1.56ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.5ms  min=8.05ms  med=13.1ms  max=279.76ms p(90)=16.51ms p(95)=17.73ms  p(99.9)=25.04ms
     http_reqs......................: 434658  3593.412295/s
     iteration_duration.............: avg=13.79ms min=8.23ms  med=13.38ms max=301.31ms p(90)=16.8ms  p(95)=18.04ms  p(99.9)=25.51ms
     iterations.....................: 434558  3592.585574/s
     success_rate...................: 100.00% ✓ 434558      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.25)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1303644     ✗ 0     
     data_received..................: 38 GB   315 MB/s
     data_sent......................: 522 MB  4.3 MB/s
     http_req_blocked...............: avg=2.41µs  min=821ns  med=1.86µs  max=3.96ms   p(90)=2.99µs  p(95)=3.68µs  p(99.9)=24.66µs
     http_req_connecting............: avg=206ns   min=0s     med=0s      max=3.91ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.6ms  min=8.12ms med=13.19ms max=273.32ms p(90)=16.75ms p(95)=18.01ms p(99.9)=25.51ms
       { expected_response:true }...: avg=13.6ms  min=8.12ms med=13.19ms max=273.32ms p(90)=16.75ms p(95)=18.01ms p(99.9)=25.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 434648
     http_req_receiving.............: avg=71.15µs min=25.1µs med=45.01µs max=119.83ms p(90)=92.57µs p(95)=171.6µs p(99.9)=1.88ms 
     http_req_sending...............: avg=30.79µs min=4.43µs med=7.95µs  max=82.7ms   p(90)=15.91µs p(95)=92.73µs p(99.9)=1.79ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.5ms  min=8.06ms med=13.09ms max=254.93ms p(90)=16.64ms p(95)=17.89ms p(99.9)=25.25ms
     http_reqs......................: 434648  3593.736894/s
     iteration_duration.............: avg=13.79ms min=8.26ms med=13.39ms max=291.33ms p(90)=16.94ms p(95)=18.2ms  p(99.9)=25.73ms
     iterations.....................: 434548  3592.910078/s
     success_rate...................: 100.00% ✓ 434548      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: nitro-router-fed (HotChocolate subgraphs) (16.8.0-p.25)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1298226     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 520 MB  4.3 MB/s
     http_req_blocked...............: avg=2.81µs  min=852ns   med=2.23µs  max=6.66ms   p(90)=3.62µs  p(95)=4.41µs   p(99.9)=30.1µs 
     http_req_connecting............: avg=196ns   min=0s      med=0s      max=3.61ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.65ms min=8.18ms  med=13.21ms max=262.9ms  p(90)=16.89ms p(95)=18.2ms   p(99.9)=26.1ms 
       { expected_response:true }...: avg=13.65ms min=8.18ms  med=13.21ms max=262.9ms  p(90)=16.89ms p(95)=18.2ms   p(99.9)=26.1ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 432842
     http_req_receiving.............: avg=84.3µs  min=24.92µs med=45.81µs max=224.47ms p(90)=98.16µs p(95)=185µs    p(99.9)=2.1ms  
     http_req_sending...............: avg=33.85µs min=4.37µs  med=8.41µs  max=194.13ms p(90)=17.63µs p(95)=100.97µs p(99.9)=1.89ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.54ms min=8.09ms  med=13.11ms max=194.81ms p(90)=16.77ms p(95)=18.07ms  p(99.9)=25.79ms
     http_reqs......................: 432842  3578.643667/s
     iteration_duration.............: avg=13.85ms min=8.37ms  med=13.41ms max=297.62ms p(90)=17.08ms p(95)=18.4ms   p(99.9)=26.32ms
     iterations.....................: 432742  3577.816889/s
     success_rate...................: 100.00% ✓ 432742      ✗ 0     
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

     checks.........................: 100.00% ✓ 1291311     ✗ 0     
     data_received..................: 38 GB   312 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.77µs  min=891ns   med=2.25µs  max=8.7ms    p(90)=3.64µs  p(95)=4.41µs   p(99.9)=31.73µs
     http_req_connecting............: avg=109ns   min=0s      med=0s      max=2.91ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.72ms min=8.17ms  med=13.28ms max=308.47ms p(90)=16.98ms p(95)=18.3ms   p(99.9)=26.06ms
       { expected_response:true }...: avg=13.72ms min=8.17ms  med=13.28ms max=308.47ms p(90)=16.98ms p(95)=18.3ms   p(99.9)=26.06ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 430537
     http_req_receiving.............: avg=74.43µs min=24.46µs med=45.11µs max=263.12ms p(90)=97.87µs p(95)=189.19µs p(99.9)=2.05ms 
     http_req_sending...............: avg=35.17µs min=4.41µs  med=8.58µs  max=279.64ms p(90)=18.12µs p(95)=102.16µs p(99.9)=2.11ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.61ms min=8.12ms  med=13.18ms max=301.81ms p(90)=16.85ms p(95)=18.16ms  p(99.9)=25.79ms
     http_reqs......................: 430537  3559.678409/s
     iteration_duration.............: avg=13.92ms min=8.34ms  med=13.48ms max=316.56ms p(90)=17.17ms p(95)=18.5ms   p(99.9)=26.28ms
     iterations.....................: 430437  3558.85161/s
     success_rate...................: 100.00% ✓ 430437      ✗ 0     
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

     checks.........................: 100.00% ✓ 1290876     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.81µs  min=882ns   med=2.22µs  max=4.82ms   p(90)=3.54µs  p(95)=4.27µs   p(99.9)=29.35µs
     http_req_connecting............: avg=224ns   min=0s      med=0s      max=3.62ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.73ms min=8.19ms  med=13.29ms max=277.39ms p(90)=16.99ms p(95)=18.33ms  p(99.9)=26.25ms
       { expected_response:true }...: avg=13.73ms min=8.19ms  med=13.29ms max=277.39ms p(90)=16.99ms p(95)=18.33ms  p(99.9)=26.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 430392
     http_req_receiving.............: avg=72.31µs min=24.08µs med=45µs    max=124.68ms p(90)=95.19µs p(95)=185.79µs p(99.9)=1.89ms 
     http_req_sending...............: avg=32.75µs min=4.27µs  med=8.42µs  max=71.6ms   p(90)=16.98µs p(95)=100.43µs p(99.9)=1.95ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.63ms min=8.13ms  med=13.19ms max=277.1ms  p(90)=16.87ms p(95)=18.19ms  p(99.9)=26ms   
     http_reqs......................: 430392  3558.42778/s
     iteration_duration.............: avg=13.93ms min=8.36ms  med=13.49ms max=286.23ms p(90)=17.18ms p(95)=18.52ms  p(99.9)=26.47ms
     iterations.....................: 430292  3557.600992/s
     success_rate...................: 100.00% ✓ 430292      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.25)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1289784     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.4µs   min=752ns   med=1.84µs  max=3.7ms    p(90)=2.95µs  p(95)=3.62µs   p(99.9)=24.25µs
     http_req_connecting............: avg=232ns   min=0s      med=0s      max=3.66ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.75ms min=8.22ms  med=13.37ms max=267.99ms p(90)=16.89ms p(95)=18.14ms  p(99.9)=25.31ms
       { expected_response:true }...: avg=13.75ms min=8.22ms  med=13.37ms max=267.99ms p(90)=16.89ms p(95)=18.14ms  p(99.9)=25.31ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 430028
     http_req_receiving.............: avg=67.4µs  min=23.73µs med=43.03µs max=90.82ms  p(90)=89.14µs p(95)=169.55µs p(99.9)=1.66ms 
     http_req_sending...............: avg=30.35µs min=4.24µs  med=7.8µs   max=100.35ms p(90)=15.28µs p(95)=90.92µs  p(99.9)=1.77ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.65ms min=7.61ms  med=13.27ms max=267.84ms p(90)=16.78ms p(95)=18.02ms  p(99.9)=25.09ms
     http_reqs......................: 430028  3555.219505/s
     iteration_duration.............: avg=13.94ms min=8.37ms  med=13.55ms max=288.46ms p(90)=17.07ms p(95)=18.32ms  p(99.9)=25.53ms
     iterations.....................: 429928  3554.392763/s
     success_rate...................: 100.00% ✓ 429928      ✗ 0     
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

     checks.........................: 100.00% ✓ 1288197     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 516 MB  4.3 MB/s
     http_req_blocked...............: avg=2.61µs  min=802ns   med=2.09µs  max=3.52ms   p(90)=3.36µs  p(95)=4.03µs   p(99.9)=25.92µs
     http_req_connecting............: avg=202ns   min=0s      med=0s      max=3.48ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.77ms min=8.18ms  med=13.33ms max=263.2ms  p(90)=16.95ms p(95)=18.25ms  p(99.9)=26.17ms
       { expected_response:true }...: avg=13.77ms min=8.18ms  med=13.33ms max=263.2ms  p(90)=16.95ms p(95)=18.25ms  p(99.9)=26.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429499
     http_req_receiving.............: avg=79.32µs min=23.85µs med=45.27µs max=230.4ms  p(90)=91.91µs p(95)=180.79µs p(99.9)=1.83ms 
     http_req_sending...............: avg=32.34µs min=4.36µs  med=8.5µs   max=85.72ms  p(90)=16.09µs p(95)=97.91µs  p(99.9)=1.71ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.65ms min=8.14ms  med=13.23ms max=223.76ms p(90)=16.83ms p(95)=18.12ms  p(99.9)=25.92ms
     http_reqs......................: 429499  3550.79251/s
     iteration_duration.............: avg=13.96ms min=8.36ms  med=13.52ms max=299.94ms p(90)=17.15ms p(95)=18.44ms  p(99.9)=26.37ms
     iterations.....................: 429399  3549.965781/s
     success_rate...................: 100.00% ✓ 429399      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.25)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1284966     ✗ 0     
     data_received..................: 38 GB   310 MB/s
     data_sent......................: 515 MB  4.3 MB/s
     http_req_blocked...............: avg=2.25µs  min=791ns  med=1.81µs  max=1.75ms   p(90)=3.01µs  p(95)=3.71µs  p(99.9)=22.95µs
     http_req_connecting............: avg=91ns    min=0s     med=0s      max=1.63ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.8ms  min=8.04ms med=13.41ms max=290.62ms p(90)=16.98ms p(95)=18.22ms p(99.9)=25.5ms 
       { expected_response:true }...: avg=13.8ms  min=8.04ms med=13.41ms max=290.62ms p(90)=16.98ms p(95)=18.22ms p(99.9)=25.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 428422
     http_req_receiving.............: avg=67.94µs min=23.3µs med=42.42µs max=28.87ms  p(90)=91.49µs p(95)=172.5µs p(99.9)=1.93ms 
     http_req_sending...............: avg=30.38µs min=4.14µs med=7.81µs  max=72.8ms   p(90)=16.34µs p(95)=91.53µs p(99.9)=1.8ms  
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.7ms  min=7.99ms med=13.32ms max=290.26ms p(90)=16.87ms p(95)=18.1ms  p(99.9)=25.16ms
     http_reqs......................: 428422  3542.12408/s
     iteration_duration.............: avg=14ms    min=8.16ms med=13.61ms max=300.8ms  p(90)=17.17ms p(95)=18.41ms p(99.9)=25.72ms
     iterations.....................: 428322  3541.297296/s
     success_rate...................: 100.00% ✓ 428322      ✗ 0     
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

     checks.........................: 100.00% ✓ 1282245     ✗ 0     
     data_received..................: 37 GB   309 MB/s
     data_sent......................: 514 MB  4.2 MB/s
     http_req_blocked...............: avg=3.01µs  min=901ns   med=2.38µs  max=4.13ms   p(90)=3.88µs   p(95)=4.73µs   p(99.9)=33.6µs 
     http_req_connecting............: avg=232ns   min=0s      med=0s      max=4.08ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.82ms min=8.25ms  med=13.37ms max=304.9ms  p(90)=17.05ms  p(95)=18.4ms   p(99.9)=26.75ms
       { expected_response:true }...: avg=13.82ms min=8.25ms  med=13.37ms max=304.9ms  p(90)=17.05ms  p(95)=18.4ms   p(99.9)=26.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 427515
     http_req_receiving.............: avg=76.25µs min=24.23µs med=47.21µs max=128.88ms p(90)=101.78µs p(95)=191.06µs p(99.9)=2.2ms  
     http_req_sending...............: avg=34.2µs  min=4.42µs  med=8.86µs  max=222.91ms p(90)=18.86µs  p(95)=102.34µs p(99.9)=1.93ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.71ms min=8.06ms  med=13.27ms max=282.58ms p(90)=16.92ms  p(95)=18.27ms  p(99.9)=26.44ms
     http_reqs......................: 427515  3534.472363/s
     iteration_duration.............: avg=14.02ms min=8.46ms  med=13.57ms max=314.32ms p(90)=17.25ms  p(95)=18.6ms   p(99.9)=26.98ms
     iterations.....................: 427415  3533.645614/s
     success_rate...................: 100.00% ✓ 427415      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.21-nightly.f689b548)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1213281     ✗ 0     
     data_received..................: 35 GB   293 MB/s
     data_sent......................: 486 MB  4.0 MB/s
     http_req_blocked...............: avg=2.45µs  min=781ns   med=1.85µs  max=4.07ms   p(90)=3.17µs  p(95)=3.96µs   p(99.9)=24.77µs
     http_req_connecting............: avg=244ns   min=0s      med=0s      max=4.01ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.63ms min=8.38ms  med=14.3ms  max=297.04ms p(90)=17.73ms p(95)=18.98ms  p(99.9)=26.48ms
       { expected_response:true }...: avg=14.63ms min=8.38ms  med=14.3ms  max=297.04ms p(90)=17.73ms p(95)=18.98ms  p(99.9)=26.48ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 404527
     http_req_receiving.............: avg=75.28µs min=23.21µs med=44.14µs max=219.47ms p(90)=95.78µs p(95)=173.86µs p(99.9)=1.77ms 
     http_req_sending...............: avg=31.43µs min=4.08µs  med=8.03µs  max=216.91ms p(90)=17.28µs p(95)=94.35µs  p(99.9)=1.64ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.52ms min=8.34ms  med=14.2ms  max=249.01ms p(90)=17.63ms p(95)=18.86ms  p(99.9)=26.22ms
     http_reqs......................: 404527  3344.078707/s
     iteration_duration.............: avg=14.82ms min=8.57ms  med=14.48ms max=308.6ms  p(90)=17.92ms p(95)=19.16ms  p(99.9)=26.7ms 
     iterations.....................: 404427  3343.252043/s
     success_rate...................: 100.00% ✓ 404427      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1209162     ✗ 0     
     data_received..................: 35 GB   292 MB/s
     data_sent......................: 485 MB  4.0 MB/s
     http_req_blocked...............: avg=2.77µs  min=851ns   med=2.24µs  max=5.53ms   p(90)=3.81µs  p(95)=4.67µs   p(99.9)=30.89µs
     http_req_connecting............: avg=125ns   min=0s      med=0s      max=2.33ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.67ms min=8.58ms  med=14.29ms max=271.07ms p(90)=17.88ms p(95)=19.19ms  p(99.9)=27.32ms
       { expected_response:true }...: avg=14.67ms min=8.58ms  med=14.29ms max=271.07ms p(90)=17.88ms p(95)=19.19ms  p(99.9)=27.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 403154
     http_req_receiving.............: avg=73.37µs min=23.37µs med=46.29µs max=126.14ms p(90)=99.73µs p(95)=184.68µs p(99.9)=1.85ms 
     http_req_sending...............: avg=34.06µs min=4.46µs  med=8.75µs  max=124.78ms p(90)=18.68µs p(95)=102.29µs p(99.9)=1.95ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.56ms min=8.49ms  med=14.19ms max=270.6ms  p(90)=17.76ms p(95)=19.05ms  p(99.9)=27.09ms
     http_reqs......................: 403154  3332.620063/s
     iteration_duration.............: avg=14.87ms min=8.74ms  med=14.49ms max=294.16ms p(90)=18.08ms p(95)=19.39ms  p(99.9)=27.55ms
     iterations.....................: 403054  3331.793426/s
     success_rate...................: 100.00% ✓ 403054      ✗ 0     
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

     checks.........................: 100.00% ✓ 559872      ✗ 0     
     data_received..................: 16 GB   134 MB/s
     data_sent......................: 224 MB  1.8 MB/s
     http_req_blocked...............: avg=3.43µs  min=872ns   med=2.52µs  max=3.67ms   p(90)=4.45µs   p(95)=5.26µs   p(99.9)=33.76µs 
     http_req_connecting............: avg=527ns   min=0s      med=0s      max=3.63ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=31.91ms min=17.84ms med=31.44ms max=286.58ms p(90)=36.95ms  p(95)=38.93ms  p(99.9)=53.16ms 
       { expected_response:true }...: avg=31.91ms min=17.84ms med=31.44ms max=286.58ms p(90)=36.95ms  p(95)=38.93ms  p(99.9)=53.16ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 186724
     http_req_receiving.............: avg=74.49µs min=24.38µs med=58.9µs  max=150.16ms p(90)=101.86µs p(95)=123.09µs p(99.9)=917.76µs
     http_req_sending...............: avg=23.26µs min=4.74µs  med=11.12µs max=175.32ms p(90)=19.35µs  p(95)=23.69µs  p(99.9)=797.96µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=31.81ms min=17.79ms med=31.34ms max=255.18ms p(90)=36.86ms  p(95)=38.83ms  p(99.9)=52.92ms 
     http_reqs......................: 186724  1531.051292/s
     iteration_duration.............: avg=32.14ms min=20.81ms med=31.65ms max=308.37ms p(90)=37.16ms  p(95)=39.14ms  p(99.9)=53.54ms 
     iterations.....................: 186624  1530.231338/s
     success_rate...................: 100.00% ✓ 186624      ✗ 0     
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

     checks.........................: 100.00% ✓ 523143      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 210 MB  1.7 MB/s
     http_req_blocked...............: avg=3.45µs  min=801ns   med=2.46µs  max=7.1ms    p(90)=4.62µs   p(95)=5.54µs   p(99.9)=37.56µs
     http_req_connecting............: avg=476ns   min=0s      med=0s      max=3.33ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.14ms min=17.4ms  med=33.86ms max=299.3ms  p(90)=40.04ms  p(95)=41.81ms  p(99.9)=50.54ms
       { expected_response:true }...: avg=34.14ms min=17.4ms  med=33.86ms max=299.3ms  p(90)=40.04ms  p(95)=41.81ms  p(99.9)=50.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 174481
     http_req_receiving.............: avg=80.48µs min=24.43µs med=54.29µs max=229.88ms p(90)=115.67µs p(95)=158.91µs p(99.9)=1.45ms 
     http_req_sending...............: avg=30.69µs min=4.45µs  med=9.97µs  max=162.88ms p(90)=22.26µs  p(95)=48.4µs   p(99.9)=1.43ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.03ms min=17.28ms med=33.76ms max=298.27ms p(90)=39.93ms  p(95)=41.7ms   p(99.9)=50.3ms 
     http_reqs......................: 174481  1430.917446/s
     iteration_duration.............: avg=34.39ms min=19.77ms med=34.1ms  max=326.52ms p(90)=40.26ms  p(95)=42.03ms  p(99.9)=50.81ms
     iterations.....................: 174381  1430.097347/s
     success_rate...................: 100.00% ✓ 174381      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.378.1)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 515796      ✗ 0     
     data_received..................: 15 GB   123 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=2.99µs  min=921ns   med=2.11µs  max=4.18ms   p(90)=3.64µs  p(95)=4.34µs   p(99.9)=26.42µs 
     http_req_connecting............: avg=551ns   min=0s      med=0s      max=4.14ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.67ms min=17.94ms med=34.11ms max=301.99ms p(90)=41.38ms p(95)=43.7ms   p(99.9)=55.35ms 
       { expected_response:true }...: avg=34.67ms min=17.94ms med=34.11ms max=301.99ms p(90)=41.38ms p(95)=43.7ms   p(99.9)=55.35ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 172032
     http_req_receiving.............: avg=69.87µs min=25.69µs med=58.93µs max=26.04ms  p(90)=97.73µs p(95)=115.19µs p(99.9)=688.95µs
     http_req_sending...............: avg=22.56µs min=4.67µs  med=10.29µs max=123.58ms p(90)=17.18µs p(95)=20.87µs  p(99.9)=745.06µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.58ms min=17.87ms med=34.02ms max=301.43ms p(90)=41.28ms p(95)=43.61ms  p(99.9)=55.26ms 
     http_reqs......................: 172032  1410.642547/s
     iteration_duration.............: avg=34.89ms min=21.06ms med=34.31ms max=308.93ms p(90)=41.57ms p(95)=43.9ms   p(99.9)=55.76ms 
     iterations.....................: 171932  1409.822559/s
     success_rate...................: 100.00% ✓ 171932      ✗ 0     
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

     checks.........................: 100.00% ✓ 221001     ✗ 0    
     data_received..................: 6.5 GB  53 MB/s
     data_sent......................: 89 MB   725 kB/s
     http_req_blocked...............: avg=4.81µs  min=1.24µs  med=3.26µs  max=4.17ms   p(90)=4.86µs   p(95)=5.6µs    p(99.9)=45.47µs 
     http_req_connecting............: avg=1.26µs  min=0s      med=0s      max=4.13ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=81.12ms min=19.76ms med=78.57ms max=325.14ms p(90)=98.1ms   p(95)=106.52ms p(99.9)=200.62ms
       { expected_response:true }...: avg=81.12ms min=19.76ms med=78.57ms max=325.14ms p(90)=98.1ms   p(95)=106.52ms p(99.9)=200.62ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 73767
     http_req_receiving.............: avg=82.14µs min=30.65µs med=74.77µs max=51.14ms  p(90)=108.15µs p(95)=120.29µs p(99.9)=657.39µs
     http_req_sending...............: avg=22.14µs min=5.74µs  med=14.5µs  max=102.93ms p(90)=20.69µs  p(95)=23.13µs  p(99.9)=599.83µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=81.01ms min=19.63ms med=78.47ms max=324.97ms p(90)=97.99ms  p(95)=106.41ms p(99.9)=200.03ms
     http_reqs......................: 73767   603.774982/s
     iteration_duration.............: avg=81.45ms min=29.22ms med=78.82ms max=333.94ms p(90)=98.34ms  p(95)=106.79ms p(99.9)=201.64ms
     iterations.....................: 73667   602.956493/s
     success_rate...................: 100.00% ✓ 73667      ✗ 0    
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

     checks.........................: 100.00% ✓ 178200     ✗ 0    
     data_received..................: 5.2 GB  43 MB/s
     data_sent......................: 72 MB   585 kB/s
     http_req_blocked...............: avg=4.99µs   min=1.14µs  med=3.19µs  max=4.13ms   p(90)=4.61µs   p(95)=5.22µs   p(99.9)=47.24µs 
     http_req_connecting............: avg=1.57µs   min=0s      med=0s      max=4.09ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=100.65ms min=18.78ms med=98.65ms max=318.51ms p(90)=127.72ms p(95)=137.05ms p(99.9)=176.2ms 
       { expected_response:true }...: avg=100.65ms min=18.78ms med=98.65ms max=318.51ms p(90)=127.72ms p(95)=137.05ms p(99.9)=176.2ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 59500
     http_req_receiving.............: avg=84.86µs  min=30.82µs med=72.93µs max=169.27ms p(90)=105.63µs p(95)=117.5µs  p(99.9)=502.61µs
     http_req_sending...............: avg=22.94µs  min=5.68µs  med=14.47µs max=84.69ms  p(90)=20.03µs  p(95)=22.11µs  p(99.9)=570.25µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=100.54ms min=18.67ms med=98.55ms max=304.54ms p(90)=127.62ms p(95)=136.94ms p(99.9)=175.74ms
     http_reqs......................: 59500   486.920871/s
     iteration_duration.............: avg=101.03ms min=32.63ms med=98.92ms max=330.93ms p(90)=127.97ms p(95)=137.36ms p(99.9)=177.53ms
     iterations.....................: 59400   486.102516/s
     success_rate...................: 100.00% ✓ 59400      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-nightly (HotChocolate subgraphs) (v3.0.0-preview.0-nightly.95b76d0a)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 176238     ✗ 0    
     data_received..................: 5.1 GB  42 MB/s
     data_sent......................: 71 MB   578 kB/s
     http_req_blocked...............: avg=4.21µs   min=1.24µs  med=3.26µs   max=2.19ms   p(90)=4.75µs   p(95)=5.38µs   p(99.9)=44.91µs 
     http_req_connecting............: avg=721ns    min=0s      med=0s       max=2.16ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=101.77ms min=18.62ms med=100.19ms max=333.64ms p(90)=127.47ms p(95)=136.31ms p(99.9)=176.82ms
       { expected_response:true }...: avg=101.77ms min=18.62ms med=100.19ms max=333.64ms p(90)=127.47ms p(95)=136.31ms p(99.9)=176.82ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 58846
     http_req_receiving.............: avg=83.89µs  min=31.07µs med=74.29µs  max=66.98ms  p(90)=107.75µs p(95)=120.26µs p(99.9)=581.69µs
     http_req_sending...............: avg=20.96µs  min=5.6µs   med=14.94µs  max=71.47ms  p(90)=20.58µs  p(95)=22.67µs  p(99.9)=554.86µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=101.66ms min=18.51ms med=100.09ms max=332.99ms p(90)=127.37ms p(95)=136.21ms p(99.9)=176.63ms
     http_reqs......................: 58846   481.455485/s
     iteration_duration.............: avg=102.16ms min=38.85ms med=100.44ms max=340.2ms  p(90)=127.72ms p(95)=136.58ms p(99.9)=178.41ms
     iterations.....................: 58746   480.637323/s
     success_rate...................: 100.00% ✓ 58746      ✗ 0    
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

     checks.........................: 100.00% ✓ 106182     ✗ 0    
     data_received..................: 3.1 GB  25 MB/s
     data_sent......................: 43 MB   349 kB/s
     http_req_blocked...............: avg=10.15µs  min=1.09µs  med=2.99µs   max=9ms      p(90)=4.3µs    p(95)=4.84µs   p(99.9)=3.02ms  
     http_req_connecting............: avg=6.83µs   min=0s      med=0s       max=8.98ms   p(90)=0s       p(95)=0s       p(99.9)=2.95ms  
     http_req_duration..............: avg=168.96ms min=16.84ms med=155.26ms max=720.56ms p(90)=190.54ms p(95)=206.66ms p(99.9)=684.23ms
       { expected_response:true }...: avg=168.96ms min=16.84ms med=155.26ms max=720.56ms p(90)=190.54ms p(95)=206.66ms p(99.9)=684.23ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 35494
     http_req_receiving.............: avg=85.13µs  min=31.43µs med=82.25µs  max=9.85ms   p(90)=111.87µs p(95)=123.17µs p(99.9)=508.6µs 
     http_req_sending...............: avg=23.41µs  min=5.39µs  med=15.72µs  max=73.34ms  p(90)=20.04µs  p(95)=21.69µs  p(99.9)=816.65µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=168.85ms min=16.76ms med=155.16ms max=720.46ms p(90)=190.44ms p(95)=206.54ms p(99.9)=684.12ms
     http_reqs......................: 35494   290.590471/s
     iteration_duration.............: avg=169.64ms min=55.52ms med=155.58ms max=720.76ms p(90)=190.84ms p(95)=207.1ms  p(99.9)=684.48ms
     iterations.....................: 35394   289.771768/s
     success_rate...................: 100.00% ✓ 35394      ✗ 0    
     vus............................: 7       min=0        max=50 
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

     checks.........................: 100.00% ✓ 98979      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   324 kB/s
     http_req_blocked...............: avg=6.83µs   min=1.34µs  med=3.46µs   max=4.19ms   p(90)=4.88µs   p(95)=5.51µs   p(99.9)=1.53ms  
     http_req_connecting............: avg=3.1µs    min=0s      med=0s       max=4.15ms   p(90)=0s       p(95)=0s       p(99.9)=1.5ms   
     http_req_duration..............: avg=181.19ms min=22.59ms med=189.11ms max=381.94ms p(90)=209.97ms p(95)=215.53ms p(99.9)=281.52ms
       { expected_response:true }...: avg=181.19ms min=22.59ms med=189.11ms max=381.94ms p(90)=209.97ms p(95)=215.53ms p(99.9)=281.52ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33093
     http_req_receiving.............: avg=94.94µs  min=32.33µs med=85.26µs  max=101.41ms p(90)=115.68µs p(95)=127.23µs p(99.9)=582.44µs
     http_req_sending...............: avg=28.38µs  min=5.93µs  med=17.76µs  max=64.24ms  p(90)=22.67µs  p(95)=24.63µs  p(99.9)=518.29µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=181.07ms min=22.47ms med=188.89ms max=381.82ms p(90)=209.86ms p(95)=215.42ms p(99.9)=281.33ms
     http_reqs......................: 33093   269.962238/s
     iteration_duration.............: avg=181.97ms min=61.68ms med=190.28ms max=399.86ms p(90)=210.27ms p(95)=215.88ms p(99.9)=282.92ms
     iterations.....................: 32993   269.14647/s
     success_rate...................: 100.00% ✓ 32993      ✗ 0    
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

