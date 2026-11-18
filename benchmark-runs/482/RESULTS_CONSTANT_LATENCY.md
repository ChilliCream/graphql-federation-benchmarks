## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.6 | 3,616 | 3,631 | 3,604 | 0.3% | 383 MB | 108.6 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.15 | 3,613 | 3,614 | 3,586 | 0.3% | 126 MB | 35.7 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.15 | 3,592 | 3,595 | 3,581 | 0.2% | 376 MB | 107.2 KB |  |
| fusion-aot-11 | 16.7.6 | 3,590 | 3,611 | 3,579 | 0.4% | 131 MB | 37.4 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.15 | 3,581 | 3,588 | 3,575 | 0.2% | 407 MB | 116.2 KB |  |
| fusion-fed-aot-11 | 16.7.6 | 3,560 | 3,575 | 3,550 | 0.3% | 131 MB | 37.7 KB |  |
| fusion-fed-net-11 | 16.7.6 | 3,554 | 3,558 | 3,551 | 0.1% | 398 MB | 114.7 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.15 | 3,514 | 3,527 | 3,510 | 0.2% | 134 MB | 39.1 KB |  |
| feddi-gateway | 2026-11-03-0517 | 3,461 | 3,472 | 3,451 | 0.2% | 2,289 MB | 677.1 KB |  |
| hive-router | v0.3.13 | 2,051 | 2,056 | 2,044 | 0.3% | 97 MB | 48.2 KB |  |
| caliban | 3.2.1 | 1,475 | 1,476 | 1,471 | 0.1% | 5,832 MB | 4,048.6 KB |  |
| cosmo | 0.372.0 | 1,433 | 1,434 | 1,430 | 0.1% | 149 MB | 106.2 KB |  |
| grafbase | 0.53.5 | 1,425 | 1,434 | 1,418 | 0.5% | 99 MB | 71.5 KB |  |
| hive-gateway-router-runtime | 2.15.8 | 582 | 584 | 581 | 0.2% | 2,612 MB | 4,595.1 KB |  |
| apollo-router | v2.19.1 | 486 | 486 | 485 | 0.1% | 180 MB | 379.6 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 418 | 420 | 417 | 0.3% | 205 MB | 502.1 KB |  |
| hive-gateway | 2.15.8 | 279 | 280 | 279 | 0.2% | 3,281 MB | 12,043.9 KB |  |
| apollo-gateway | 2.14.4 | 270 | 271 | 268 | 0.6% | 2,167 MB | 8,219.4 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1311930     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 526 MB  4.3 MB/s
     http_req_blocked...............: avg=2.54µs  min=821ns   med=1.86µs  max=6.71ms   p(90)=3.01µs  p(95)=3.72µs   p(99.9)=25.26µs
     http_req_connecting............: avg=322ns   min=0s      med=0s      max=6.67ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.51ms min=8.12ms  med=13.09ms max=266.03ms p(90)=16.64ms p(95)=17.91ms  p(99.9)=25.67ms
       { expected_response:true }...: avg=13.51ms min=8.12ms  med=13.09ms max=266.03ms p(90)=16.64ms p(95)=17.91ms  p(99.9)=25.67ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 437410
     http_req_receiving.............: avg=68.98µs min=24.67µs med=44.53µs max=10.58ms  p(90)=92.18µs p(95)=173.97µs p(99.9)=1.82ms 
     http_req_sending...............: avg=33.27µs min=4.42µs  med=8.02µs  max=179.92ms p(90)=16.2µs  p(95)=93.69µs  p(99.9)=1.86ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.41ms min=8.07ms  med=12.99ms max=263.37ms p(90)=16.53ms p(95)=17.79ms  p(99.9)=25.37ms
     http_reqs......................: 437410  3616.485655/s
     iteration_duration.............: avg=13.71ms min=8.29ms  med=13.28ms max=279.19ms p(90)=16.83ms p(95)=18.11ms  p(99.9)=25.87ms
     iterations.....................: 437310  3615.65886/s
     success_rate...................: 100.00% ✓ 437310      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1310913     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 525 MB  4.3 MB/s
     http_req_blocked...............: avg=2.37µs  min=801ns   med=1.84µs  max=3.98ms   p(90)=3µs     p(95)=3.69µs  p(99.9)=24.22µs
     http_req_connecting............: avg=204ns   min=0s      med=0s      max=3.94ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.53ms min=8.29ms  med=13.12ms max=311.47ms p(90)=16.54ms p(95)=17.78ms p(99.9)=25.24ms
       { expected_response:true }...: avg=13.53ms min=8.29ms  med=13.12ms max=311.47ms p(90)=16.54ms p(95)=17.78ms p(99.9)=25.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 437071
     http_req_receiving.............: avg=79.65µs min=23.98µs med=42.38µs max=276.03ms p(90)=88.66µs p(95)=171.4µs p(99.9)=1.84ms 
     http_req_sending...............: avg=30.47µs min=4.25µs  med=8µs     max=34.88ms  p(90)=16.13µs p(95)=94.05µs p(99.9)=1.61ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.42ms min=8.02ms  med=13.03ms max=113.54ms p(90)=16.43ms p(95)=17.65ms p(99.9)=25.06ms
     http_reqs......................: 437071  3613.591003/s
     iteration_duration.............: avg=13.72ms min=8.46ms  med=13.31ms max=319.88ms p(90)=16.73ms p(95)=17.96ms p(99.9)=25.47ms
     iterations.....................: 436971  3612.764228/s
     success_rate...................: 100.00% ✓ 436971      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1303449     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 522 MB  4.3 MB/s
     http_req_blocked...............: avg=2.4µs   min=801ns   med=1.83µs  max=4.26ms   p(90)=2.95µs  p(95)=3.61µs   p(99.9)=23.12µs
     http_req_connecting............: avg=230ns   min=0s      med=0s      max=4.22ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.6ms  min=7.98ms  med=13.19ms max=288.47ms p(90)=16.7ms  p(95)=17.97ms  p(99.9)=25.64ms
       { expected_response:true }...: avg=13.6ms  min=7.98ms  med=13.19ms max=288.47ms p(90)=16.7ms  p(95)=17.97ms  p(99.9)=25.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 434583
     http_req_receiving.............: avg=67.43µs min=23.91µs med=42.41µs max=125.34ms p(90)=89.56µs p(95)=173.01µs p(99.9)=1.8ms  
     http_req_sending...............: avg=30.51µs min=4.02µs  med=7.84µs  max=182.03ms p(90)=15.79µs p(95)=93.36µs  p(99.9)=1.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.5ms  min=7.93ms  med=13.1ms  max=287.64ms p(90)=16.59ms p(95)=17.85ms  p(99.9)=25.49ms
     http_reqs......................: 434583  3592.925685/s
     iteration_duration.............: avg=13.8ms  min=8.19ms  med=13.38ms max=298.31ms p(90)=16.89ms p(95)=18.16ms  p(99.9)=25.86ms
     iterations.....................: 434483  3592.098933/s
     success_rate...................: 100.00% ✓ 434483      ✗ 0     
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

     checks.........................: 100.00% ✓ 1302531     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 522 MB  4.3 MB/s
     http_req_blocked...............: avg=2.53µs  min=861ns   med=1.98µs  max=4ms      p(90)=3.25µs  p(95)=4µs      p(99.9)=25.37µs
     http_req_connecting............: avg=213ns   min=0s      med=0s      max=3.95ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.61ms min=8.18ms  med=13.19ms max=283.5ms  p(90)=16.69ms p(95)=17.95ms  p(99.9)=25.3ms 
       { expected_response:true }...: avg=13.61ms min=8.18ms  med=13.19ms max=283.5ms  p(90)=16.69ms p(95)=17.95ms  p(99.9)=25.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 434277
     http_req_receiving.............: avg=71.17µs min=24.67µs med=45.46µs max=167.11ms p(90)=94.05µs p(95)=176.88µs p(99.9)=1.77ms 
     http_req_sending...............: avg=32.42µs min=4.39µs  med=8.23µs  max=112ms    p(90)=16.96µs p(95)=96.56µs  p(99.9)=1.8ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.51ms min=8.12ms  med=13.09ms max=283.37ms p(90)=16.57ms p(95)=17.83ms  p(99.9)=25.06ms
     http_reqs......................: 434277  3590.357821/s
     iteration_duration.............: avg=13.81ms min=8.38ms  med=13.38ms max=295.22ms p(90)=16.88ms p(95)=18.14ms  p(99.9)=25.5ms 
     iterations.....................: 434177  3589.531077/s
     success_rate...................: 100.00% ✓ 434177      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1299120     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 521 MB  4.3 MB/s
     http_req_blocked...............: avg=2.49µs  min=831ns   med=1.93µs  max=4.17ms   p(90)=3.15µs  p(95)=3.88µs   p(99.9)=24.54µs
     http_req_connecting............: avg=210ns   min=0s      med=0s      max=4.13ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.65ms min=8.17ms  med=13.23ms max=289.93ms p(90)=16.79ms p(95)=18.06ms  p(99.9)=25.54ms
       { expected_response:true }...: avg=13.65ms min=8.17ms  med=13.23ms max=289.93ms p(90)=16.79ms p(95)=18.06ms  p(99.9)=25.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 433140
     http_req_receiving.............: avg=69.62µs min=24.24µs med=44.45µs max=62.38ms  p(90)=93.24µs p(95)=171.96µs p(99.9)=1.82ms 
     http_req_sending...............: avg=31.82µs min=4.37µs  med=8.08µs  max=113.8ms  p(90)=16.5µs  p(95)=93.23µs  p(99.9)=1.71ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.54ms min=8.12ms  med=13.14ms max=289.32ms p(90)=16.68ms p(95)=17.93ms  p(99.9)=25.31ms
     http_reqs......................: 433140  3581.175315/s
     iteration_duration.............: avg=13.84ms min=8.32ms  med=13.43ms max=299.1ms  p(90)=16.98ms p(95)=18.25ms  p(99.9)=25.79ms
     iterations.....................: 433040  3580.348521/s
     success_rate...................: 100.00% ✓ 433040      ✗ 0     
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

     checks.........................: 100.00% ✓ 1291668     ✗ 0     
     data_received..................: 38 GB   312 MB/s
     data_sent......................: 518 MB  4.3 MB/s
     http_req_blocked...............: avg=2.32µs  min=811ns   med=1.88µs  max=2.44ms   p(90)=3.04µs  p(95)=3.7µs    p(99.9)=23.5µs 
     http_req_connecting............: avg=118ns   min=0s      med=0s      max=2.42ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.73ms min=8.21ms  med=13.33ms max=284.99ms p(90)=16.78ms p(95)=18.02ms  p(99.9)=25.53ms
       { expected_response:true }...: avg=13.73ms min=8.21ms  med=13.33ms max=284.99ms p(90)=16.78ms p(95)=18.02ms  p(99.9)=25.53ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 430656
     http_req_receiving.............: avg=67.72µs min=23.53µs med=44.13µs max=83.19ms  p(90)=90.89µs p(95)=169.55µs p(99.9)=1.56ms 
     http_req_sending...............: avg=31.38µs min=4.3µs   med=8.02µs  max=164.72ms p(90)=15.4µs  p(95)=93.91µs  p(99.9)=1.7ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.63ms min=8.16ms  med=13.23ms max=284.72ms p(90)=16.68ms p(95)=17.9ms   p(99.9)=25.32ms
     http_reqs......................: 430656  3560.429698/s
     iteration_duration.............: avg=13.92ms min=8.4ms   med=13.52ms max=293.22ms p(90)=16.97ms p(95)=18.21ms  p(99.9)=25.73ms
     iterations.....................: 430556  3559.602952/s
     success_rate...................: 100.00% ✓ 430556      ✗ 0     
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

     checks.........................: 100.00% ✓ 1289442     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.48µs  min=792ns   med=1.9µs   max=3.32ms   p(90)=3.18µs  p(95)=4µs      p(99.9)=27.85µs
     http_req_connecting............: avg=204ns   min=0s      med=0s      max=3.29ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.74ms min=8.2ms   med=13.35ms max=285.69ms p(90)=16.89ms p(95)=18.16ms  p(99.9)=25.59ms
       { expected_response:true }...: avg=13.74ms min=8.2ms   med=13.35ms max=285.69ms p(90)=16.89ms p(95)=18.16ms  p(99.9)=25.59ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429914
     http_req_receiving.............: avg=70.59µs min=25.23µs med=45.05µs max=210.72ms p(90)=95.5µs  p(95)=172.79µs p(99.9)=1.71ms 
     http_req_sending...............: avg=32.27µs min=4.4µs   med=8.16µs  max=141.02ms p(90)=17.48µs p(95)=95.8µs   p(99.9)=1.81ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.64ms min=8.14ms  med=13.25ms max=285.29ms p(90)=16.78ms p(95)=18.03ms  p(99.9)=25.43ms
     http_reqs......................: 429914  3554.392315/s
     iteration_duration.............: avg=13.95ms min=8.35ms  med=13.54ms max=298.86ms p(90)=17.08ms p(95)=18.35ms  p(99.9)=25.8ms 
     iterations.....................: 429814  3553.565547/s
     success_rate...................: 100.00% ✓ 429814      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1274832     ✗ 0     
     data_received..................: 37 GB   308 MB/s
     data_sent......................: 511 MB  4.2 MB/s
     http_req_blocked...............: avg=2.88µs  min=882ns   med=2.28µs  max=5.65ms   p(90)=3.69µs  p(95)=4.47µs   p(99.9)=35.2µs 
     http_req_connecting............: avg=203ns   min=0s      med=0s      max=3.43ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.9ms  min=8.31ms  med=13.48ms max=273.32ms p(90)=17.12ms p(95)=18.41ms  p(99.9)=26.39ms
       { expected_response:true }...: avg=13.9ms  min=8.31ms  med=13.48ms max=273.32ms p(90)=17.12ms p(95)=18.41ms  p(99.9)=26.39ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 425044
     http_req_receiving.............: avg=73.38µs min=24.06µs med=45.1µs  max=200.4ms  p(90)=96.86µs p(95)=191.21µs p(99.9)=1.95ms 
     http_req_sending...............: avg=33.49µs min=4.39µs  med=8.61µs  max=118.63ms p(90)=17.71µs p(95)=103.62µs p(99.9)=1.8ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.8ms  min=8.26ms  med=13.38ms max=262.42ms p(90)=16.99ms p(95)=18.28ms  p(99.9)=26.11ms
     http_reqs......................: 425044  3514.051587/s
     iteration_duration.............: avg=14.1ms  min=8.45ms  med=13.67ms max=285.54ms p(90)=17.31ms p(95)=18.6ms   p(99.9)=26.63ms
     iterations.....................: 424944  3513.224837/s
     success_rate...................: 100.00% ✓ 424944      ✗ 0     
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

     checks.........................: 100.00% ✓ 1255485     ✗ 0     
     data_received..................: 37 GB   303 MB/s
     data_sent......................: 503 MB  4.2 MB/s
     http_req_blocked...............: avg=2.37µs  min=781ns   med=1.84µs  max=4.02ms   p(90)=2.95µs  p(95)=3.59µs   p(99.9)=24.16µs
     http_req_connecting............: avg=227ns   min=0s      med=0s      max=3.97ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.14ms min=8.35ms  med=13.8ms  max=287.67ms p(90)=17.06ms p(95)=18.22ms  p(99.9)=25.12ms
       { expected_response:true }...: avg=14.14ms min=8.35ms  med=13.8ms  max=287.67ms p(90)=17.06ms p(95)=18.22ms  p(99.9)=25.12ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 418595
     http_req_receiving.............: avg=66.98µs min=24.02µs med=43.71µs max=120.84ms p(90)=87.29µs p(95)=161.37µs p(99.9)=1.6ms  
     http_req_sending...............: avg=30.66µs min=3.93µs  med=7.86µs  max=190.57ms p(90)=14.78µs p(95)=90.1µs   p(99.9)=1.69ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.04ms min=8.3ms   med=13.71ms max=273.37ms p(90)=16.97ms p(95)=18.11ms  p(99.9)=24.94ms
     http_reqs......................: 418595  3461.001095/s
     iteration_duration.............: avg=14.32ms min=8.53ms  med=13.98ms max=298.83ms p(90)=17.25ms p(95)=18.41ms  p(99.9)=25.33ms
     iterations.....................: 418495  3460.174281/s
     success_rate...................: 100.00% ✓ 418495      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.13)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 749877      ✗ 0     
     data_received..................: 22 GB   180 MB/s
     data_sent......................: 301 MB  2.5 MB/s
     http_req_blocked...............: avg=2.88µs  min=851ns   med=2.13µs  max=4.21ms   p(90)=3.68µs  p(95)=4.39µs   p(99.9)=29.46µs 
     http_req_connecting............: avg=387ns   min=0s      med=0s      max=4.16ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.78ms min=17.06ms med=23.43ms max=300.32ms p(90)=26.83ms p(95)=27.91ms  p(99.9)=33.4ms  
       { expected_response:true }...: avg=23.78ms min=17.06ms med=23.43ms max=300.32ms p(90)=26.83ms p(95)=27.91ms  p(99.9)=33.4ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 250059
     http_req_receiving.............: avg=63.66µs min=25.15µs med=48.78µs max=40.44ms  p(90)=89.31µs p(95)=112.79µs p(99.9)=862.55µs
     http_req_sending...............: avg=24.69µs min=4.43µs  med=9.1µs   max=138.06ms p(90)=16.75µs p(95)=23.22µs  p(99.9)=894.73µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.69ms min=16.88ms med=23.35ms max=299.67ms p(90)=26.74ms p(95)=27.82ms  p(99.9)=33.18ms 
     http_reqs......................: 250059  2051.846467/s
     iteration_duration.............: avg=23.99ms min=17.25ms med=23.63ms max=309.71ms p(90)=27.03ms p(95)=28.11ms  p(99.9)=33.61ms 
     iterations.....................: 249959  2051.025922/s
     success_rate...................: 100.00% ✓ 249959      ✗ 0     
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

     checks.........................: 100.00% ✓ 539655      ✗ 0     
     data_received..................: 16 GB   129 MB/s
     data_sent......................: 216 MB  1.8 MB/s
     http_req_blocked...............: avg=3.19µs  min=952ns   med=2.33µs  max=3.54ms   p(90)=4.03µs  p(95)=4.83µs   p(99.9)=27.67µs 
     http_req_connecting............: avg=515ns   min=0s      med=0s      max=3.5ms    p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.12ms min=18.53ms med=32.58ms max=289.25ms p(90)=38.75ms p(95)=40.95ms  p(99.9)=57.31ms 
       { expected_response:true }...: avg=33.12ms min=18.53ms med=32.58ms max=289.25ms p(90)=38.75ms p(95)=40.95ms  p(99.9)=57.31ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 179985
     http_req_receiving.............: avg=72.43µs min=27.02µs med=59.32µs max=159.52ms p(90)=97.7µs  p(95)=116.32µs p(99.9)=862.66µs
     http_req_sending...............: avg=21.74µs min=4.76µs  med=10.85µs max=119.17ms p(90)=17.51µs p(95)=21.67µs  p(99.9)=751.65µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.02ms min=18.34ms med=32.49ms max=288.57ms p(90)=38.66ms p(95)=40.86ms  p(99.9)=57.07ms 
     http_reqs......................: 179985  1475.589268/s
     iteration_duration.............: avg=33.34ms min=20.29ms med=32.79ms max=303.75ms p(90)=38.96ms p(95)=41.15ms  p(99.9)=57.64ms 
     iterations.....................: 179885  1474.769428/s
     success_rate...................: 100.00% ✓ 179885      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.372.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 524094      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 210 MB  1.7 MB/s
     http_req_blocked...............: avg=3.63µs  min=1.08µs  med=2.77µs  max=4.15ms   p(90)=4.4µs    p(95)=5.14µs   p(99.9)=35.95µs 
     http_req_connecting............: avg=524ns   min=0s      med=0s      max=4.1ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.11ms min=18.04ms med=33.54ms max=313.23ms p(90)=40.64ms  p(95)=42.94ms  p(99.9)=55.8ms  
       { expected_response:true }...: avg=34.11ms min=18.04ms med=33.54ms max=313.23ms p(90)=40.64ms  p(95)=42.94ms  p(99.9)=55.8ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 174798
     http_req_receiving.............: avg=75.03µs min=26.73µs med=61.96µs max=60.78ms  p(90)=101.69µs p(95)=120.39µs p(99.9)=801.84µs
     http_req_sending...............: avg=25.46µs min=4.71µs  med=11.93µs max=145.32ms p(90)=19.08µs  p(95)=23.62µs  p(99.9)=835.42µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.01ms min=17.92ms med=33.44ms max=312.8ms  p(90)=40.53ms  p(95)=42.84ms  p(99.9)=55.42ms 
     http_reqs......................: 174798  1433.250383/s
     iteration_duration.............: avg=34.33ms min=20.56ms med=33.75ms max=322.5ms  p(90)=40.85ms  p(95)=43.14ms  p(99.9)=56.07ms 
     iterations.....................: 174698  1432.430437/s
     success_rate...................: 100.00% ✓ 174698      ✗ 0     
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

     checks.........................: 100.00% ✓ 521100      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 209 MB  1.7 MB/s
     http_req_blocked...............: avg=3.98µs  min=961ns   med=2.89µs  max=4.66ms   p(90)=5.03µs   p(95)=6µs      p(99.9)=45.08µs
     http_req_connecting............: avg=590ns   min=0s      med=0s      max=4.61ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.27ms min=18.1ms  med=33.99ms max=313.84ms p(90)=40.04ms  p(95)=41.85ms  p(99.9)=51.17ms
       { expected_response:true }...: avg=34.27ms min=18.1ms  med=33.99ms max=313.84ms p(90)=40.04ms  p(95)=41.85ms  p(99.9)=51.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 173800
     http_req_receiving.............: avg=85.19µs min=27.31µs med=60.8µs  max=67.79ms  p(90)=122.62µs p(95)=168.39µs p(99.9)=1.48ms 
     http_req_sending...............: avg=31.63µs min=4.77µs  med=11.17µs max=210.13ms p(90)=22.93µs  p(95)=52.92µs  p(99.9)=1.18ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.15ms min=17.83ms med=33.88ms max=313.24ms p(90)=39.92ms  p(95)=41.73ms  p(99.9)=50.79ms
     http_reqs......................: 173800  1425.286802/s
     iteration_duration.............: avg=34.53ms min=21.08ms med=34.24ms max=323.18ms p(90)=40.27ms  p(95)=42.08ms  p(99.9)=51.47ms
     iterations.....................: 173700  1424.466729/s
     success_rate...................: 100.00% ✓ 173700      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 213261     ✗ 0    
     data_received..................: 6.2 GB  51 MB/s
     data_sent......................: 86 MB   700 kB/s
     http_req_blocked...............: avg=4.21µs  min=1.1µs   med=2.71µs  max=4.05ms   p(90)=4.23µs   p(95)=4.84µs   p(99.9)=43.7µs  
     http_req_connecting............: avg=1.25µs  min=0s      med=0s      max=4ms      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=84.09ms min=20ms    med=81.39ms max=322.28ms p(90)=102.51ms p(95)=112.76ms p(99.9)=212.43ms
       { expected_response:true }...: avg=84.09ms min=20ms    med=81.39ms max=322.28ms p(90)=102.51ms p(95)=112.76ms p(99.9)=212.43ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 71187
     http_req_receiving.............: avg=79.87µs min=29.31µs med=70µs    max=132.22ms p(90)=104.53µs p(95)=117.04µs p(99.9)=589.24µs
     http_req_sending...............: avg=21.5µs  min=5.05µs  med=13.25µs max=157.83ms p(90)=19.28µs  p(95)=21.33µs  p(99.9)=524.4µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=83.99ms min=19.85ms med=81.3ms  max=321.88ms p(90)=102.4ms  p(95)=112.66ms p(99.9)=211.91ms
     http_reqs......................: 71187   582.626603/s
     iteration_duration.............: avg=84.41ms min=33.78ms med=81.62ms max=331.96ms p(90)=102.75ms p(95)=113.01ms p(99.9)=214.29ms
     iterations.....................: 71087   581.808157/s
     success_rate...................: 100.00% ✓ 71087      ✗ 0    
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

     checks.........................: 100.00% ✓ 178089     ✗ 0    
     data_received..................: 5.2 GB  43 MB/s
     data_sent......................: 71 MB   584 kB/s
     http_req_blocked...............: avg=3.77µs   min=1.1µs   med=2.61µs  max=2.53ms   p(90)=4.06µs   p(95)=4.62µs   p(99.9)=53.05µs 
     http_req_connecting............: avg=891ns    min=0s      med=0s      max=2.5ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=100.71ms min=19.9ms  med=98.91ms max=329.82ms p(90)=127.76ms p(95)=136.64ms p(99.9)=178.41ms
       { expected_response:true }...: avg=100.71ms min=19.9ms  med=98.91ms max=329.82ms p(90)=127.76ms p(95)=136.64ms p(99.9)=178.41ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 59463
     http_req_receiving.............: avg=77.27µs  min=28µs    med=66.93µs max=95.83ms  p(90)=99.14µs  p(95)=111.34µs p(99.9)=521.35µs
     http_req_sending...............: avg=20.25µs  min=4.92µs  med=12.57µs max=107.54ms p(90)=18.57µs  p(95)=20.52µs  p(99.9)=502.4µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=100.61ms min=19.78ms med=98.81ms max=329.39ms p(90)=127.68ms p(95)=136.54ms p(99.9)=178.32ms
     http_reqs......................: 59463   486.599924/s
     iteration_duration.............: avg=101.09ms min=38.8ms  med=99.18ms max=338.13ms p(90)=128.01ms p(95)=136.91ms p(99.9)=179.74ms
     iterations.....................: 59363   485.7816/s
     success_rate...................: 100.00% ✓ 59363      ✗ 0    
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

     checks.........................: 100.00% ✓ 153405     ✗ 0    
     data_received..................: 4.5 GB  37 MB/s
     data_sent......................: 62 MB   503 kB/s
     http_req_blocked...............: avg=5.59µs   min=1.16µs  med=3.38µs   max=4.28ms   p(90)=4.91µs   p(95)=5.52µs   p(99.9)=139.04µs
     http_req_connecting............: avg=1.93µs   min=0s      med=0s       max=4.22ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=116.91ms min=21.01ms med=115.37ms max=352.64ms p(90)=144.29ms p(95)=153.87ms p(99.9)=198.11ms
       { expected_response:true }...: avg=116.91ms min=21.01ms med=115.37ms max=352.64ms p(90)=144.29ms p(95)=153.87ms p(99.9)=198.11ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51235
     http_req_receiving.............: avg=83.23µs  min=29.13µs med=76.8µs   max=91.93ms  p(90)=108.17µs p(95)=119.58µs p(99.9)=515.02µs
     http_req_sending...............: avg=22.3µs   min=5.44µs  med=15.74µs  max=80.16ms  p(90)=21.46µs  p(95)=23.57µs  p(99.9)=541.18µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=116.8ms  min=20.88ms med=115.27ms max=352.44ms p(90)=144.2ms  p(95)=153.77ms p(99.9)=197.64ms
     http_reqs......................: 51235   418.881699/s
     iteration_duration.............: avg=117.36ms min=34.07ms med=115.67ms max=366.21ms p(90)=144.57ms p(95)=154.16ms p(99.9)=201.52ms
     iterations.....................: 51135   418.06413/s
     success_rate...................: 100.00% ✓ 51135      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 102156     ✗ 0    
     data_received..................: 3.0 GB  25 MB/s
     data_sent......................: 41 MB   336 kB/s
     http_req_blocked...............: avg=6.49µs   min=1.39µs  med=3.56µs   max=3.97ms   p(90)=4.93µs   p(95)=5.53µs   p(99.9)=986.69µs
     http_req_connecting............: avg=2.68µs   min=0s      med=0s       max=3.93ms   p(90)=0s       p(95)=0s       p(99.9)=952.74µs
     http_req_duration..............: avg=175.56ms min=17.69ms med=153.86ms max=781.82ms p(90)=223.83ms p(95)=245.5ms  p(99.9)=716.49ms
       { expected_response:true }...: avg=175.56ms min=17.69ms med=153.86ms max=781.82ms p(90)=223.83ms p(95)=245.5ms  p(99.9)=716.49ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 34152
     http_req_receiving.............: avg=89.79µs  min=34.01µs med=85.03µs  max=15.23ms  p(90)=114.29µs p(95)=125.14µs p(99.9)=494.13µs
     http_req_sending...............: avg=24.79µs  min=6.1µs   med=17.04µs  max=76.18ms  p(90)=21.67µs  p(95)=23.47µs  p(99.9)=562.4µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=175.44ms min=17.57ms med=153.76ms max=781.72ms p(90)=223.72ms p(95)=245.4ms  p(99.9)=716.37ms
     http_reqs......................: 34152   279.902199/s
     iteration_duration.............: avg=176.28ms min=32.35ms med=154.32ms max=782.06ms p(90)=224.18ms p(95)=245.87ms p(99.9)=716.82ms
     iterations.....................: 34052   279.082621/s
     success_rate...................: 100.00% ✓ 34052      ✗ 0    
     vus............................: 11      min=0        max=50 
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

     checks.........................: 100.00% ✓ 99267      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   325 kB/s
     http_req_blocked...............: avg=6.79µs   min=1.42µs  med=3.59µs   max=4.26ms   p(90)=5.07µs   p(95)=5.67µs   p(99.9)=1.28ms  
     http_req_connecting............: avg=2.92µs   min=0s      med=0s       max=4.22ms   p(90)=0s       p(95)=0s       p(99.9)=1.22ms  
     http_req_duration..............: avg=180.63ms min=22.19ms med=181.11ms max=409.57ms p(90)=192.12ms p(95)=196.38ms p(99.9)=267.9ms 
       { expected_response:true }...: avg=180.63ms min=22.19ms med=181.11ms max=409.57ms p(90)=192.12ms p(95)=196.38ms p(99.9)=267.9ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 33189
     http_req_receiving.............: avg=92.59µs  min=32.03µs med=86.68µs  max=41.58ms  p(90)=116.21µs p(95)=127.01µs p(99.9)=636.72µs
     http_req_sending...............: avg=27.38µs  min=6.11µs  med=17.55µs  max=118.51ms p(90)=22.23µs  p(95)=24.09µs  p(99.9)=502.08µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=180.51ms min=22.12ms med=181.01ms max=409.4ms  p(90)=192ms    p(95)=196.27ms p(99.9)=267.09ms
     http_reqs......................: 33189   270.766115/s
     iteration_duration.............: avg=181.4ms  min=57.68ms med=181.48ms max=418.88ms p(90)=192.42ms p(95)=196.67ms p(99.9)=279.33ms
     iterations.....................: 33089   269.950284/s
     success_rate...................: 100.00% ✓ 33089      ✗ 0    
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

