## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.6 | 3,597 | 3,614 | 3,591 | 0.2% | 385 MB | 109.6 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.16 | 3,588 | 3,601 | 3,580 | 0.2% | 378 MB | 108.0 KB |  |
| fusion-aot-11 | 16.7.6 | 3,585 | 3,596 | 3,568 | 0.3% | 132 MB | 37.7 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.16 | 3,569 | 3,573 | 3,546 | 0.3% | 125 MB | 35.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.16 | 3,555 | 3,560 | 3,547 | 0.1% | 391 MB | 112.7 KB |  |
| fusion-fed-net-11 | 16.7.6 | 3,553 | 3,559 | 3,542 | 0.2% | 396 MB | 114.2 KB |  |
| fusion-fed-aot-11 | 16.7.6 | 3,543 | 3,545 | 3,535 | 0.1% | 145 MB | 42.0 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.16 | 3,543 | 3,546 | 3,530 | 0.2% | 128 MB | 37.1 KB |  |
| feddi-gateway | 2026-11-03-0517 | 3,457 | 3,481 | 3,441 | 0.4% | 2,310 MB | 684.2 KB |  |
| hive-router | v0.3.16 | 3,352 | 3,379 | 3,347 | 0.4% | 93 MB | 28.5 KB |  |
| grafbase | 0.53.5 | 1,448 | 1,459 | 1,441 | 0.5% | 99 MB | 70.3 KB |  |
| caliban | 3.2.1 | 1,442 | 1,445 | 1,442 | 0.1% | 6,459 MB | 4,586.7 KB |  |
| cosmo | 0.373.0 | 1,380 | 1,380 | 1,378 | 0.1% | 158 MB | 117.5 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 596 | 598 | 594 | 0.3% | 2,598 MB | 4,463.5 KB |  |
| apollo-router | v2.19.1 | 532 | 533 | 532 | 0.1% | 179 MB | 345.3 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 386 | 392 | 386 | 0.7% | 203 MB | 539.3 KB |  |
| hive-gateway | 2.15.10 | 279 | 280 | 277 | 0.4% | 3,252 MB | 11,936.4 KB |  |
| apollo-gateway | 2.14.4 | 269 | 269 | 265 | 0.7% | 2,154 MB | 8,198.8 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1304979     ✗ 0     
     data_received..................: 38 GB   315 MB/s
     data_sent......................: 523 MB  4.3 MB/s
     http_req_blocked...............: avg=2.74µs  min=811ns   med=2.17µs  max=4.89ms   p(90)=3.52µs  p(95)=4.28µs   p(99.9)=27.94µs
     http_req_connecting............: avg=215ns   min=0s      med=0s      max=3.43ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.58ms min=7.85ms  med=13.14ms max=282.9ms  p(90)=16.78ms p(95)=18.09ms  p(99.9)=25.8ms 
       { expected_response:true }...: avg=13.58ms min=7.85ms  med=13.14ms max=282.9ms  p(90)=16.78ms p(95)=18.09ms  p(99.9)=25.8ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 435093
     http_req_receiving.............: avg=72.88µs min=24.49µs med=45.53µs max=88.09ms  p(90)=95.91µs p(95)=181.68µs p(99.9)=2.05ms 
     http_req_sending...............: avg=33.97µs min=4.18µs  med=8.44µs  max=154.77ms p(90)=17.07µs p(95)=98.8µs   p(99.9)=1.96ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.48ms min=7.81ms  med=13.04ms max=282.49ms p(90)=16.66ms p(95)=17.96ms  p(99.9)=25.54ms
     http_reqs......................: 435093  3597.167601/s
     iteration_duration.............: avg=13.78ms min=8.04ms  med=13.34ms max=292.29ms p(90)=16.98ms p(95)=18.29ms  p(99.9)=26.04ms
     iterations.....................: 434993  3596.340842/s
     success_rate...................: 100.00% ✓ 434993      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1301961     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 522 MB  4.3 MB/s
     http_req_blocked...............: avg=2.46µs  min=841ns  med=1.88µs  max=3.71ms   p(90)=3.02µs  p(95)=3.71µs  p(99.9)=25.39µs
     http_req_connecting............: avg=220ns   min=0s     med=0s      max=3.67ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.62ms min=8ms    med=13.2ms  max=304.11ms p(90)=16.76ms p(95)=18.01ms p(99.9)=25.35ms
       { expected_response:true }...: avg=13.62ms min=8ms    med=13.2ms  max=304.11ms p(90)=16.76ms p(95)=18.01ms p(99.9)=25.35ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 434087
     http_req_receiving.............: avg=78.85µs min=24.7µs med=43.84µs max=227.32ms p(90)=89.69µs p(95)=167.6µs p(99.9)=1.79ms 
     http_req_sending...............: avg=30.69µs min=4.3µs  med=8.02µs  max=36.94ms  p(90)=16µs    p(95)=92.48µs p(99.9)=1.79ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.51ms min=7.95ms med=13.11ms max=84.47ms  p(90)=16.65ms p(95)=17.89ms p(99.9)=25.06ms
     http_reqs......................: 434087  3588.976149/s
     iteration_duration.............: avg=13.81ms min=8.12ms med=13.4ms  max=326.4ms  p(90)=16.95ms p(95)=18.2ms  p(99.9)=25.57ms
     iterations.....................: 433987  3588.149361/s
     success_rate...................: 100.00% ✓ 433987      ✗ 0     
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

     checks.........................: 100.00% ✓ 1300764     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 521 MB  4.3 MB/s
     http_req_blocked...............: avg=2.49µs  min=811ns   med=1.93µs  max=3.81ms   p(90)=3.17µs  p(95)=3.87µs   p(99.9)=25.35µs
     http_req_connecting............: avg=195ns   min=0s      med=0s      max=3.46ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.63ms min=8.17ms  med=13.21ms max=283.07ms p(90)=16.71ms p(95)=17.94ms  p(99.9)=25.25ms
       { expected_response:true }...: avg=13.63ms min=8.17ms  med=13.21ms max=283.07ms p(90)=16.71ms p(95)=17.94ms  p(99.9)=25.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 433688
     http_req_receiving.............: avg=70.46µs min=25.17µs med=44.85µs max=90.9ms   p(90)=93.49µs p(95)=177.95µs p(99.9)=1.83ms 
     http_req_sending...............: avg=33.39µs min=4.4µs   med=8.15µs  max=219.91ms p(90)=16.98µs p(95)=96.56µs  p(99.9)=1.84ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.53ms min=8.08ms  med=13.11ms max=282.61ms p(90)=16.6ms  p(95)=17.82ms  p(99.9)=25ms   
     http_reqs......................: 433688  3585.437008/s
     iteration_duration.............: avg=13.82ms min=8.36ms  med=13.4ms  max=292.78ms p(90)=16.9ms  p(95)=18.13ms  p(99.9)=25.47ms
     iterations.....................: 433588  3584.610276/s
     success_rate...................: 100.00% ✓ 433588      ✗ 0     
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

     checks.........................: 100.00% ✓ 1295139     ✗ 0     
     data_received..................: 38 GB   312 MB/s
     data_sent......................: 519 MB  4.3 MB/s
     http_req_blocked...............: avg=2.44µs  min=862ns   med=1.9µs   max=3.9ms    p(90)=3.01µs  p(95)=3.67µs   p(99.9)=24.21µs
     http_req_connecting............: avg=220ns   min=0s      med=0s      max=3.86ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.69ms min=8.19ms  med=13.29ms max=306.52ms p(90)=16.78ms p(95)=18.02ms  p(99.9)=25.73ms
       { expected_response:true }...: avg=13.69ms min=8.19ms  med=13.29ms max=306.52ms p(90)=16.78ms p(95)=18.02ms  p(99.9)=25.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 431813
     http_req_receiving.............: avg=67.4µs  min=24.32µs med=43.94µs max=84.64ms  p(90)=87.97µs p(95)=169.91µs p(99.9)=1.56ms 
     http_req_sending...............: avg=30.73µs min=4.45µs  med=8.07µs  max=195.06ms p(90)=15.37µs p(95)=93.87µs  p(99.9)=1.61ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.6ms  min=8.13ms  med=13.19ms max=292.93ms p(90)=16.67ms p(95)=17.91ms  p(99.9)=25.48ms
     http_reqs......................: 431813  3569.944605/s
     iteration_duration.............: avg=13.88ms min=8.37ms  med=13.48ms max=328.68ms p(90)=16.97ms p(95)=18.21ms  p(99.9)=25.97ms
     iterations.....................: 431713  3569.117871/s
     success_rate...................: 100.00% ✓ 431713      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1289985     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.44µs  min=822ns   med=1.9µs   max=3.93ms   p(90)=3.06µs  p(95)=3.74µs   p(99.9)=22.4µs 
     http_req_connecting............: avg=213ns   min=0s      med=0s      max=3.88ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.74ms min=8.17ms  med=13.32ms max=288.77ms p(90)=16.94ms p(95)=18.22ms  p(99.9)=25.94ms
       { expected_response:true }...: avg=13.74ms min=8.17ms  med=13.32ms max=288.77ms p(90)=16.94ms p(95)=18.22ms  p(99.9)=25.94ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 430095
     http_req_receiving.............: avg=70.43µs min=25.01µs med=45.18µs max=94.39ms  p(90)=92.72µs p(95)=177.49µs p(99.9)=1.77ms 
     http_req_sending...............: avg=30.91µs min=4.35µs  med=8.02µs  max=20ms     p(90)=16.02µs p(95)=94.55µs  p(99.9)=1.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.64ms min=8.13ms  med=13.23ms max=271.71ms p(90)=16.82ms p(95)=18.1ms   p(99.9)=25.74ms
     http_reqs......................: 430095  3555.826653/s
     iteration_duration.............: avg=13.94ms min=8.33ms  med=13.52ms max=297.9ms  p(90)=17.13ms p(95)=18.41ms  p(99.9)=26.17ms
     iterations.....................: 429995  3554.999899/s
     success_rate...................: 100.00% ✓ 429995      ✗ 0     
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

     checks.........................: 100.00% ✓ 1289103     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.44µs  min=792ns   med=1.89µs  max=3.93ms   p(90)=3.03µs  p(95)=3.69µs   p(99.9)=24.57µs
     http_req_connecting............: avg=215ns   min=0s      med=0s      max=3.89ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.75ms min=8.11ms  med=13.34ms max=273.28ms p(90)=16.93ms p(95)=18.19ms  p(99.9)=25.8ms 
       { expected_response:true }...: avg=13.75ms min=8.11ms  med=13.34ms max=273.28ms p(90)=16.93ms p(95)=18.19ms  p(99.9)=25.8ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 429801
     http_req_receiving.............: avg=71.06µs min=25.22µs med=44.92µs max=230.94ms p(90)=90.13µs p(95)=172.36µs p(99.9)=1.95ms 
     http_req_sending...............: avg=31.74µs min=4.35µs  med=7.98µs  max=225.8ms  p(90)=15.36µs p(95)=93.26µs  p(99.9)=1.89ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.65ms min=8.06ms  med=13.25ms max=272.04ms p(90)=16.82ms p(95)=18.07ms  p(99.9)=25.47ms
     http_reqs......................: 429801  3553.63551/s
     iteration_duration.............: avg=13.95ms min=8.24ms  med=13.54ms max=293.59ms p(90)=17.12ms p(95)=18.38ms  p(99.9)=26.01ms
     iterations.....................: 429701  3552.808701/s
     success_rate...................: 100.00% ✓ 429701      ✗ 0     
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

     checks.........................: 100.00% ✓ 1285452     ✗ 0     
     data_received..................: 38 GB   310 MB/s
     data_sent......................: 515 MB  4.3 MB/s
     http_req_blocked...............: avg=2.65µs  min=812ns   med=1.88µs  max=8.61ms   p(90)=3.26µs  p(95)=4.09µs   p(99.9)=24.61µs
     http_req_connecting............: avg=334ns   min=0s      med=0s      max=5.78ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.8ms  min=8.17ms  med=13.38ms max=264.13ms p(90)=16.95ms p(95)=18.21ms  p(99.9)=25.61ms
       { expected_response:true }...: avg=13.8ms  min=8.17ms  med=13.38ms max=264.13ms p(90)=16.95ms p(95)=18.21ms  p(99.9)=25.61ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 428584
     http_req_receiving.............: avg=69.44µs min=24.96µs med=44.58µs max=87.57ms  p(90)=94.23µs p(95)=170.27µs p(99.9)=1.7ms  
     http_req_sending...............: avg=31.91µs min=4.02µs  med=7.96µs  max=188.97ms p(90)=17.18µs p(95)=93.7µs   p(99.9)=1.79ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.69ms min=8.07ms  med=13.28ms max=262.37ms p(90)=16.84ms p(95)=18.1ms   p(99.9)=25.42ms
     http_reqs......................: 428584  3543.262911/s
     iteration_duration.............: avg=13.99ms min=8.36ms  med=13.57ms max=284.62ms p(90)=17.14ms p(95)=18.41ms  p(99.9)=25.82ms
     iterations.....................: 428484  3542.436174/s
     success_rate...................: 100.00% ✓ 428484      ✗ 0     
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

     checks.........................: 100.00% ✓ 1285596     ✗ 0     
     data_received..................: 38 GB   310 MB/s
     data_sent......................: 515 MB  4.3 MB/s
     http_req_blocked...............: avg=2.79µs  min=842ns   med=2.26µs  max=3.48ms   p(90)=3.5µs   p(95)=4.17µs   p(99.9)=30.76µs
     http_req_connecting............: avg=204ns   min=0s      med=0s      max=3.45ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.79ms min=8.17ms  med=13.37ms max=287.65ms p(90)=16.95ms p(95)=18.26ms  p(99.9)=25.84ms
       { expected_response:true }...: avg=13.79ms min=8.17ms  med=13.37ms max=287.65ms p(90)=16.95ms p(95)=18.26ms  p(99.9)=25.84ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 428632
     http_req_receiving.............: avg=84.92µs min=24.76µs med=46.87µs max=244.5ms  p(90)=95.11µs p(95)=191.2µs  p(99.9)=1.89ms 
     http_req_sending...............: avg=32.22µs min=4.19µs  med=8.53µs  max=27.74ms  p(90)=16.27µs p(95)=102.38µs p(99.9)=1.74ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.68ms min=8.1ms   med=13.27ms max=129.76ms p(90)=16.83ms p(95)=18.12ms  p(99.9)=25.59ms
     http_reqs......................: 428632  3543.716138/s
     iteration_duration.............: avg=13.99ms min=8.41ms  med=13.56ms max=298.89ms p(90)=17.14ms p(95)=18.45ms  p(99.9)=26.06ms
     iterations.....................: 428532  3542.889388/s
     success_rate...................: 100.00% ✓ 428532      ✗ 0     
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

     checks.........................: 100.00% ✓ 1254492     ✗ 0     
     data_received..................: 37 GB   302 MB/s
     data_sent......................: 503 MB  4.2 MB/s
     http_req_blocked...............: avg=2.93µs  min=912ns   med=2.35µs  max=4.02ms   p(90)=3.74µs  p(95)=4.49µs   p(99.9)=32.44µs
     http_req_connecting............: avg=215ns   min=0s      med=0s      max=3.97ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.14ms min=8.26ms  med=13.75ms max=288.29ms p(90)=17.19ms p(95)=18.46ms  p(99.9)=26.08ms
       { expected_response:true }...: avg=14.14ms min=8.26ms  med=13.75ms max=288.29ms p(90)=17.19ms p(95)=18.46ms  p(99.9)=26.08ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 418264
     http_req_receiving.............: avg=71.73µs min=23.35µs med=44.96µs max=184.23ms p(90)=92.49µs p(95)=177.54µs p(99.9)=1.85ms 
     http_req_sending...............: avg=33.5µs  min=4.35µs  med=8.92µs  max=112.08ms p(90)=17.56µs p(95)=101.52µs p(99.9)=1.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.03ms min=8.21ms  med=13.65ms max=285.53ms p(90)=17.08ms p(95)=18.33ms  p(99.9)=25.84ms
     http_reqs......................: 418264  3457.95003/s
     iteration_duration.............: avg=14.33ms min=8.41ms  med=13.94ms max=299.53ms p(90)=17.39ms p(95)=18.65ms  p(99.9)=26.29ms
     iterations.....................: 418164  3457.123292/s
     success_rate...................: 100.00% ✓ 418164      ✗ 0     
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

     checks.........................: 100.00% ✓ 1216398     ✗ 0     
     data_received..................: 36 GB   293 MB/s
     data_sent......................: 487 MB  4.0 MB/s
     http_req_blocked...............: avg=2.53µs  min=831ns   med=1.96µs  max=3.27ms   p(90)=3.34µs  p(95)=4.23µs   p(99.9)=29.26µs
     http_req_connecting............: avg=204ns   min=0s      med=0s      max=3.24ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.59ms min=8.32ms  med=14.24ms max=277.24ms p(90)=17.64ms p(95)=18.87ms  p(99.9)=26.28ms
       { expected_response:true }...: avg=14.59ms min=8.32ms  med=14.24ms max=277.24ms p(90)=17.64ms p(95)=18.87ms  p(99.9)=26.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 405566
     http_req_receiving.............: avg=70.58µs min=24.12µs med=45.16µs max=146.34ms p(90)=97.48µs p(95)=178.95µs p(99.9)=1.61ms 
     http_req_sending...............: avg=32.27µs min=4.49µs  med=8.34µs  max=175.95ms p(90)=17.55µs p(95)=97.38µs  p(99.9)=1.58ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.49ms min=8.23ms  med=14.15ms max=275.99ms p(90)=17.53ms p(95)=18.74ms  p(99.9)=26.09ms
     http_reqs......................: 405566  3352.514604/s
     iteration_duration.............: avg=14.78ms min=8.46ms  med=14.44ms max=299.61ms p(90)=17.83ms p(95)=19.06ms  p(99.9)=26.53ms
     iterations.....................: 405466  3351.687978/s
     success_rate...................: 100.00% ✓ 405466      ✗ 0     
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

     checks.........................: 100.00% ✓ 529677      ✗ 0     
     data_received..................: 16 GB   127 MB/s
     data_sent......................: 212 MB  1.7 MB/s
     http_req_blocked...............: avg=3.94µs  min=982ns   med=2.89µs  max=3.93ms   p(90)=5.11µs   p(95)=6.1µs    p(99.9)=43.57µs
     http_req_connecting............: avg=568ns   min=0s      med=0s      max=3.9ms    p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.71ms min=17.62ms med=33.43ms max=324.55ms p(90)=39.23ms  p(95)=40.98ms  p(99.9)=50.17ms
       { expected_response:true }...: avg=33.71ms min=17.62ms med=33.43ms max=324.55ms p(90)=39.23ms  p(95)=40.98ms  p(99.9)=50.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 176659
     http_req_receiving.............: avg=83.21µs min=27.13µs med=60.11µs max=38.07ms  p(90)=119.72µs p(95)=164.43µs p(99.9)=1.32ms 
     http_req_sending...............: avg=31.35µs min=4.3µs   med=10.79µs max=232ms    p(90)=22.41µs  p(95)=48.18µs  p(99.9)=1.33ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.6ms  min=17.47ms med=33.32ms max=324.05ms p(90)=39.12ms  p(95)=40.86ms  p(99.9)=49.81ms
     http_reqs......................: 176659  1448.845717/s
     iteration_duration.............: avg=33.97ms min=21.17ms med=33.68ms max=336.16ms p(90)=39.46ms  p(95)=41.2ms   p(99.9)=50.44ms
     iterations.....................: 176559  1448.025581/s
     success_rate...................: 100.00% ✓ 176559      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 527610      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 211 MB  1.7 MB/s
     http_req_blocked...............: avg=3.11µs  min=971ns   med=2.23µs  max=4.42ms   p(90)=3.62µs  p(95)=4.28µs   p(99.9)=29.91µs 
     http_req_connecting............: avg=597ns   min=0s      med=0s      max=4.37ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.89ms min=17.96ms med=33.36ms max=297.41ms p(90)=39.76ms p(95)=42.01ms  p(99.9)=57.61ms 
       { expected_response:true }...: avg=33.89ms min=17.96ms med=33.36ms max=297.41ms p(90)=39.76ms p(95)=42.01ms  p(99.9)=57.61ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 175970
     http_req_receiving.............: avg=70.28µs min=27.13µs med=58.5µs  max=126.12ms p(90)=94.54µs p(95)=111.32µs p(99.9)=811.61µs
     http_req_sending...............: avg=21.41µs min=4.68µs  med=10.37µs max=140.66ms p(90)=16.36µs p(95)=20.14µs  p(99.9)=723.2µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.8ms  min=17.89ms med=33.27ms max=289.64ms p(90)=39.67ms p(95)=41.92ms  p(99.9)=57.18ms 
     http_reqs......................: 175970  1442.927204/s
     iteration_duration.............: avg=34.1ms  min=19.67ms med=33.56ms max=308.77ms p(90)=39.96ms p(95)=42.22ms  p(99.9)=58.13ms 
     iterations.....................: 175870  1442.107219/s
     success_rate...................: 100.00% ✓ 175870      ✗ 0     
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

     checks.........................: 100.00% ✓ 504852      ✗ 0     
     data_received..................: 15 GB   121 MB/s
     data_sent......................: 202 MB  1.7 MB/s
     http_req_blocked...............: avg=2.9µs   min=902ns   med=2.03µs  max=4ms      p(90)=3.38µs  p(95)=4.02µs   p(99.9)=28.82µs 
     http_req_connecting............: avg=572ns   min=0s      med=0s      max=3.95ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.43ms min=18.08ms med=34.9ms  max=308.6ms  p(90)=42.31ms p(95)=44.7ms   p(99.9)=56.59ms 
       { expected_response:true }...: avg=35.43ms min=18.08ms med=34.9ms  max=308.6ms  p(90)=42.31ms p(95)=44.7ms   p(99.9)=56.59ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 168384
     http_req_receiving.............: avg=70.09µs min=25.71µs med=58.3µs  max=123.13ms p(90)=96.16µs p(95)=114.71µs p(99.9)=681.19µs
     http_req_sending...............: avg=19.83µs min=4.53µs  med=9.73µs  max=98.76ms  p(90)=15.88µs p(95)=19.49µs  p(99.9)=729.14µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=35.34ms min=17.97ms med=34.82ms max=307.91ms p(90)=42.23ms p(95)=44.61ms  p(99.9)=56.46ms 
     http_reqs......................: 168384  1380.611346/s
     iteration_duration.............: avg=35.64ms min=21.43ms med=35.09ms max=317.05ms p(90)=42.5ms  p(95)=44.89ms  p(99.9)=56.92ms 
     iterations.....................: 168284  1379.791427/s
     success_rate...................: 100.00% ✓ 168284      ✗ 0     
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

     checks.........................: 100.00% ✓ 218250     ✗ 0    
     data_received..................: 6.4 GB  52 MB/s
     data_sent......................: 88 MB   716 kB/s
     http_req_blocked...............: avg=4.5µs   min=1.01µs  med=2.71µs  max=4.23ms   p(90)=4.16µs   p(95)=4.76µs   p(99.9)=48.01µs 
     http_req_connecting............: avg=1.52µs  min=0s      med=0s      max=4.19ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=82.16ms min=19.87ms med=80.28ms max=313.45ms p(90)=95.55ms  p(95)=103.85ms p(99.9)=200.53ms
       { expected_response:true }...: avg=82.16ms min=19.87ms med=80.28ms max=313.45ms p(90)=95.55ms  p(95)=103.85ms p(99.9)=200.53ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 72850
     http_req_receiving.............: avg=80.28µs min=29.95µs med=70.83µs max=146.29ms p(90)=104.34µs p(95)=117.4µs  p(99.9)=537.6µs 
     http_req_sending...............: avg=20.37µs min=4.98µs  med=13.59µs max=58.13ms  p(90)=19.4µs   p(95)=21.53µs  p(99.9)=563.72µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=82.06ms min=19.66ms med=80.18ms max=313.06ms p(90)=95.45ms  p(95)=103.71ms p(99.9)=199.96ms
     http_reqs......................: 72850   596.143937/s
     iteration_duration.............: avg=82.48ms min=31.55ms med=80.52ms max=339ms    p(90)=95.78ms  p(95)=104.11ms p(99.9)=202.18ms
     iterations.....................: 72750   595.32562/s
     success_rate...................: 100.00% ✓ 72750      ✗ 0    
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

     checks.........................: 100.00% ✓ 195006     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   640 kB/s
     http_req_blocked...............: avg=5.02µs  min=1.21µs  med=3.38µs  max=3.61ms   p(90)=4.93µs   p(95)=5.59µs   p(99.9)=45.35µs 
     http_req_connecting............: avg=1.4µs   min=0s      med=0s      max=3.57ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=91.95ms min=20.47ms med=90.25ms max=307.28ms p(90)=115.93ms p(95)=123.87ms p(99.9)=160.01ms
       { expected_response:true }...: avg=91.95ms min=20.47ms med=90.25ms max=307.28ms p(90)=115.93ms p(95)=123.87ms p(99.9)=160.01ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 65102
     http_req_receiving.............: avg=82.33µs min=31.33µs med=76.57µs max=26.54ms  p(90)=109.78µs p(95)=122.06µs p(99.9)=531.81µs
     http_req_sending...............: avg=25.9µs  min=5.67µs  med=15.19µs max=153.45ms p(90)=20.8µs   p(95)=22.95µs  p(99.9)=605.69µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.84ms min=20.32ms med=90.15ms max=306.6ms  p(90)=115.83ms p(95)=123.78ms p(99.9)=159.07ms
     http_reqs......................: 65102   532.762027/s
     iteration_duration.............: avg=92.32ms min=32.4ms  med=90.52ms max=337.68ms p(90)=116.2ms  p(95)=124.14ms p(99.9)=160.69ms
     iterations.....................: 65002   531.943677/s
     success_rate...................: 100.00% ✓ 65002      ✗ 0    
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

     checks.........................: 100.00% ✓ 141723     ✗ 0    
     data_received..................: 4.1 GB  34 MB/s
     data_sent......................: 57 MB   465 kB/s
     http_req_blocked...............: avg=4.66µs   min=1.1µs   med=2.52µs   max=3.9ms    p(90)=3.9µs    p(95)=4.45µs   p(99.9)=432.98µs
     http_req_connecting............: avg=1.91µs   min=0s      med=0s       max=3.86ms   p(90)=0s       p(95)=0s       p(99.9)=414.16µs
     http_req_duration..............: avg=126.56ms min=21.15ms med=124.77ms max=338.39ms p(90)=156.79ms p(95)=167.57ms p(99.9)=216.35ms
       { expected_response:true }...: avg=126.56ms min=21.15ms med=124.77ms max=338.39ms p(90)=156.79ms p(95)=167.57ms p(99.9)=216.35ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 47341
     http_req_receiving.............: avg=76.39µs  min=29.35µs med=69.61µs  max=82.66ms  p(90)=101.23µs p(95)=113.14µs p(99.9)=481.1µs 
     http_req_sending...............: avg=28.24µs  min=5.07µs  med=13.83µs  max=148.16ms p(90)=19.53µs  p(95)=21.46µs  p(99.9)=502.85µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=126.46ms min=20.98ms med=124.68ms max=338.06ms p(90)=156.69ms p(95)=167.44ms p(99.9)=215.18ms
     http_reqs......................: 47341   386.982132/s
     iteration_duration.............: avg=127.04ms min=43.39ms med=125.05ms max=347.96ms p(90)=157.08ms p(95)=167.88ms p(99.9)=220.74ms
     iterations.....................: 47241   386.164696/s
     success_rate...................: 100.00% ✓ 47241      ✗ 0    
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

     checks.........................: 100.00% ✓ 101916     ✗ 0    
     data_received..................: 3.0 GB  25 MB/s
     data_sent......................: 41 MB   335 kB/s
     http_req_blocked...............: avg=6.55µs   min=1.45µs  med=3.41µs   max=3.88ms   p(90)=4.76µs   p(95)=5.37µs   p(99.9)=1.62ms  
     http_req_connecting............: avg=2.9µs    min=0s      med=0s       max=3.84ms   p(90)=0s       p(95)=0s       p(99.9)=1.6ms   
     http_req_duration..............: avg=175.93ms min=17.42ms med=162.44ms max=746.88ms p(90)=196.62ms p(95)=212.57ms p(99.9)=712.95ms
       { expected_response:true }...: avg=175.93ms min=17.42ms med=162.44ms max=746.88ms p(90)=196.62ms p(95)=212.57ms p(99.9)=712.95ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 34072
     http_req_receiving.............: avg=88.39µs  min=37.91µs med=83.29µs  max=12.87ms  p(90)=113.51µs p(95)=124.57µs p(99.9)=639.67µs
     http_req_sending...............: avg=27.1µs   min=5.83µs  med=16.45µs  max=84.95ms  p(90)=21.21µs  p(95)=22.95µs  p(99.9)=476.61µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=175.82ms min=17.28ms med=162.32ms max=746.75ms p(90)=196.52ms p(95)=212.48ms p(99.9)=712.85ms
     http_reqs......................: 34072   279.351968/s
     iteration_duration.............: avg=176.68ms min=37.2ms  med=162.77ms max=747.16ms p(90)=196.92ms p(95)=213.12ms p(99.9)=713.21ms
     iterations.....................: 33972   278.532081/s
     success_rate...................: 100.00% ✓ 33972      ✗ 0    
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

     checks.........................: 100.00% ✓ 98646      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   323 kB/s
     http_req_blocked...............: avg=4.58µs   min=1.16µs  med=3.15µs   max=1.83ms   p(90)=4.52µs   p(95)=5.07µs   p(99.9)=510.37µs
     http_req_connecting............: avg=1.21µs   min=0s      med=0s       max=1.8ms    p(90)=0s       p(95)=0s       p(99.9)=478.5µs 
     http_req_duration..............: avg=181.81ms min=22.78ms med=182.48ms max=337.65ms p(90)=192.15ms p(95)=196.26ms p(99.9)=262.95ms
       { expected_response:true }...: avg=181.81ms min=22.78ms med=182.48ms max=337.65ms p(90)=192.15ms p(95)=196.26ms p(99.9)=262.95ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32982
     http_req_receiving.............: avg=89.15µs  min=31.05µs med=84.79µs  max=56.53ms  p(90)=113.17µs p(95)=123.11µs p(99.9)=479.14µs
     http_req_sending...............: avg=19.72µs  min=5.14µs  med=16.64µs  max=18.79ms  p(90)=20.83µs  p(95)=22.59µs  p(99.9)=419.52µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=181.7ms  min=22.61ms med=182.38ms max=337.52ms p(90)=192.05ms p(95)=196.14ms p(99.9)=262.87ms
     http_reqs......................: 32982   269.021592/s
     iteration_duration.............: avg=182.57ms min=68.49ms med=182.78ms max=345.71ms p(90)=192.4ms  p(95)=196.53ms p(99.9)=265.65ms
     iterations.....................: 32882   268.20593/s
     success_rate...................: 100.00% ✓ 32882      ✗ 0    
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

