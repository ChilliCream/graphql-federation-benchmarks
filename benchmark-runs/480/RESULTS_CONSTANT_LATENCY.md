## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.15 | 3,569 | 3,583 | 3,553 | 0.3% | 388 MB | 111.2 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.15 | 3,567 | 3,581 | 3,556 | 0.3% | 123 MB | 35.3 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.15 | 3,550 | 3,555 | 3,541 | 0.2% | 405 MB | 116.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.15 | 3,547 | 3,555 | 3,535 | 0.2% | 147 MB | 42.5 KB |  |
| feddi-gateway | 2026-11-03-0517 | 3,493 | 3,494 | 3,475 | 0.2% | 2,281 MB | 668.8 KB |  |
| fusion-aot-11 | 16.7.5 | 3,427 | 3,437 | 3,404 | 0.4% | 140 MB | 41.8 KB |  |
| fusion-net-11 | 16.7.5 | 3,396 | 3,411 | 3,385 | 0.3% | 385 MB | 116.2 KB |  |
| fusion-fed-net-11 | 16.7.5 | 2,783 | 2,793 | 2,772 | 0.3% | 389 MB | 143.0 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 2,756 | 2,776 | 2,749 | 0.4% | 144 MB | 53.3 KB |  |
| hive-router | v0.3.13 | 2,062 | 2,069 | 2,058 | 0.2% | 94 MB | 46.5 KB |  |
| grafbase | 0.53.5 | 1,453 | 1,464 | 1,445 | 0.5% | 99 MB | 70.1 KB |  |
| caliban | 3.2.1 | 1,442 | 1,443 | 1,442 | 0.0% | 5,783 MB | 4,106.9 KB |  |
| cosmo | 0.372.0 | 1,415 | 1,417 | 1,413 | 0.1% | 151 MB | 109.5 KB |  |
| hive-gateway-router-runtime | 2.15.8 | 593 | 594 | 592 | 0.1% | 2,619 MB | 4,522.8 KB |  |
| apollo-router | v2.19.1 | 505 | 514 | 502 | 1.1% | 182 MB | 368.8 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 388 | 392 | 387 | 0.6% | 203 MB | 534.7 KB |  |
| hive-gateway | 2.15.8 | 285 | 286 | 284 | 0.3% | 3,244 MB | 11,653.9 KB |  |
| apollo-gateway | 2.14.4 | 264 | 265 | 262 | 0.4% | 2,143 MB | 8,313.2 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1294845     ✗ 0     
     data_received..................: 38 GB   312 MB/s
     data_sent......................: 519 MB  4.3 MB/s
     http_req_blocked...............: avg=2.75µs  min=811ns   med=1.86µs  max=7.79ms   p(90)=3.03µs  p(95)=3.74µs   p(99.9)=24.99µs
     http_req_connecting............: avg=514ns   min=0s      med=0s      max=7.76ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.69ms min=8.01ms  med=13.29ms max=284.3ms  p(90)=16.84ms p(95)=18.11ms  p(99.9)=25.43ms
       { expected_response:true }...: avg=13.69ms min=8.01ms  med=13.29ms max=284.3ms  p(90)=16.84ms p(95)=18.11ms  p(99.9)=25.43ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 431715
     http_req_receiving.............: avg=69.75µs min=24.39µs med=44.54µs max=133.47ms p(90)=92.23µs p(95)=173.89µs p(99.9)=1.76ms 
     http_req_sending...............: avg=32.09µs min=4.24µs  med=7.84µs  max=127.89ms p(90)=15.92µs p(95)=94.33µs  p(99.9)=1.78ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.59ms min=7.93ms  med=13.19ms max=283.32ms p(90)=16.73ms p(95)=17.99ms  p(99.9)=25.22ms
     http_reqs......................: 431715  3569.351413/s
     iteration_duration.............: avg=13.89ms min=8.14ms  med=13.48ms max=298.3ms  p(90)=17.03ms p(95)=18.3ms   p(99.9)=25.65ms
     iterations.....................: 431615  3568.524629/s
     success_rate...................: 100.00% ✓ 431615      ✗ 0     
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

     checks.........................: 100.00% ✓ 1294314     ✗ 0     
     data_received..................: 38 GB   312 MB/s
     data_sent......................: 519 MB  4.3 MB/s
     http_req_blocked...............: avg=2.45µs  min=852ns   med=1.93µs  max=3.99ms   p(90)=3.05µs  p(95)=3.68µs   p(99.9)=25.13µs
     http_req_connecting............: avg=204ns   min=0s      med=0s      max=3.95ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.7ms  min=8.15ms  med=13.29ms max=285.12ms p(90)=16.8ms  p(95)=18.06ms  p(99.9)=25.8ms 
       { expected_response:true }...: avg=13.7ms  min=8.15ms  med=13.29ms max=285.12ms p(90)=16.8ms  p(95)=18.06ms  p(99.9)=25.8ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 431538
     http_req_receiving.............: avg=68.53µs min=23.87µs med=44.05µs max=76.1ms   p(90)=90.07µs p(95)=174.33µs p(99.9)=1.74ms 
     http_req_sending...............: avg=31.89µs min=4.44µs  med=8.15µs  max=248.69ms p(90)=15.16µs p(95)=95.25µs  p(99.9)=1.6ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.6ms  min=8.09ms  med=13.19ms max=284.58ms p(90)=16.69ms p(95)=17.94ms  p(99.9)=25.61ms
     http_reqs......................: 431538  3567.868186/s
     iteration_duration.............: avg=13.89ms min=8.35ms  med=13.48ms max=298.11ms p(90)=16.99ms p(95)=18.25ms  p(99.9)=26.03ms
     iterations.....................: 431438  3567.041407/s
     success_rate...................: 100.00% ✓ 431438      ✗ 0     
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

     checks.........................: 100.00% ✓ 1288116     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 516 MB  4.3 MB/s
     http_req_blocked...............: avg=2.89µs  min=801ns   med=1.9µs   max=8.29ms   p(90)=3.29µs  p(95)=4.22µs   p(99.9)=27.04µs
     http_req_connecting............: avg=572ns   min=0s      med=0s      max=8.15ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.76ms min=8.14ms  med=13.34ms max=274.7ms  p(90)=16.93ms p(95)=18.21ms  p(99.9)=26.04ms
       { expected_response:true }...: avg=13.76ms min=8.14ms  med=13.34ms max=274.7ms  p(90)=16.93ms p(95)=18.21ms  p(99.9)=26.04ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429472
     http_req_receiving.............: avg=69.91µs min=23.68µs med=43.74µs max=11.04ms  p(90)=94.47µs p(95)=174.55µs p(99.9)=2.05ms 
     http_req_sending...............: avg=33.94µs min=4.29µs  med=8.08µs  max=250.58ms p(90)=17.57µs p(95)=95.73µs  p(99.9)=2.11ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.66ms min=8.1ms   med=13.24ms max=273.38ms p(90)=16.82ms p(95)=18.08ms  p(99.9)=25.75ms
     http_reqs......................: 429472  3550.889737/s
     iteration_duration.............: avg=13.96ms min=8.32ms  med=13.54ms max=293.61ms p(90)=17.12ms p(95)=18.4ms   p(99.9)=26.29ms
     iterations.....................: 429372  3550.062933/s
     success_rate...................: 100.00% ✓ 429372      ✗ 0     
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

     checks.........................: 100.00% ✓ 1287132     ✗ 0     
     data_received..................: 38 GB   310 MB/s
     data_sent......................: 516 MB  4.3 MB/s
     http_req_blocked...............: avg=2.7µs   min=772ns   med=2.13µs  max=3.72ms   p(90)=3.53µs  p(95)=4.28µs   p(99.9)=29.8µs 
     http_req_connecting............: avg=221ns   min=0s      med=0s      max=3.67ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.78ms min=8.3ms   med=13.36ms max=283.36ms p(90)=16.88ms p(95)=18.15ms  p(99.9)=26.25ms
       { expected_response:true }...: avg=13.78ms min=8.3ms   med=13.36ms max=283.36ms p(90)=16.88ms p(95)=18.15ms  p(99.9)=26.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429144
     http_req_receiving.............: avg=72µs    min=24.46µs med=45.97µs max=91ms     p(90)=96.32µs p(95)=179.97µs p(99.9)=1.87ms 
     http_req_sending...............: avg=32.84µs min=4.18µs  med=8.56µs  max=140.4ms  p(90)=17.64µs p(95)=98.95µs  p(99.9)=1.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.67ms min=8.24ms  med=13.26ms max=283.17ms p(90)=16.76ms p(95)=18.02ms  p(99.9)=25.96ms
     http_reqs......................: 429144  3547.759058/s
     iteration_duration.............: avg=13.97ms min=8.43ms  med=13.55ms max=302.37ms p(90)=17.07ms p(95)=18.34ms  p(99.9)=26.46ms
     iterations.....................: 429044  3546.932352/s
     success_rate...................: 100.00% ✓ 429044      ✗ 0     
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

     checks.........................: 100.00% ✓ 1267140     ✗ 0     
     data_received..................: 37 GB   305 MB/s
     data_sent......................: 508 MB  4.2 MB/s
     http_req_blocked...............: avg=2.89µs  min=952ns   med=2.32µs  max=5.24ms   p(90)=3.67µs  p(95)=4.37µs   p(99.9)=32.26µs
     http_req_connecting............: avg=191ns   min=0s      med=0s      max=5.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.99ms min=8.08ms  med=13.6ms  max=280.97ms p(90)=17.06ms p(95)=18.32ms  p(99.9)=26.25ms
       { expected_response:true }...: avg=13.99ms min=8.08ms  med=13.6ms  max=280.97ms p(90)=17.06ms p(95)=18.32ms  p(99.9)=26.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 422480
     http_req_receiving.............: avg=71.62µs min=23.75µs med=44.88µs max=233.51ms p(90)=90.22µs p(95)=176.91µs p(99.9)=1.95ms 
     http_req_sending...............: avg=34.38µs min=4.42µs  med=8.79µs  max=114.98ms p(90)=16.99µs p(95)=100.95µs p(99.9)=2.09ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.89ms min=8.03ms  med=13.5ms  max=279.58ms p(90)=16.94ms p(95)=18.2ms   p(99.9)=26.02ms
     http_reqs......................: 422480  3493.162459/s
     iteration_duration.............: avg=14.19ms min=8.22ms  med=13.79ms max=292.12ms p(90)=17.25ms p(95)=18.52ms  p(99.9)=26.47ms
     iterations.....................: 422380  3492.335636/s
     success_rate...................: 100.00% ✓ 422380      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1243392     ✗ 0     
     data_received..................: 36 GB   300 MB/s
     data_sent......................: 498 MB  4.1 MB/s
     http_req_blocked...............: avg=2.53µs  min=802ns   med=1.88µs  max=5.71ms   p(90)=3.14µs  p(95)=3.94µs   p(99.9)=24.92µs
     http_req_connecting............: avg=277ns   min=0s      med=0s      max=5.58ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.27ms min=8.31ms  med=13.84ms max=274.39ms p(90)=17.62ms p(95)=18.96ms  p(99.9)=26.67ms
       { expected_response:true }...: avg=14.27ms min=8.31ms  med=13.84ms max=274.39ms p(90)=17.62ms p(95)=18.96ms  p(99.9)=26.67ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 414564
     http_req_receiving.............: avg=68.73µs min=23.81µs med=42.4µs  max=122.66ms p(90)=90.9µs  p(95)=179.78µs p(99.9)=1.92ms 
     http_req_sending...............: avg=32.42µs min=4.34µs  med=8.02µs  max=131.15ms p(90)=17µs    p(95)=98.28µs  p(99.9)=1.78ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.17ms min=8.25ms  med=13.74ms max=273.71ms p(90)=17.5ms  p(95)=18.84ms  p(99.9)=26.35ms
     http_reqs......................: 414564  3427.229563/s
     iteration_duration.............: avg=14.46ms min=8.51ms  med=14.03ms max=284.61ms p(90)=17.81ms p(95)=19.15ms  p(99.9)=26.88ms
     iterations.....................: 414464  3426.402856/s
     success_rate...................: 100.00% ✓ 414464      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1232160     ✗ 0     
     data_received..................: 36 GB   297 MB/s
     data_sent......................: 494 MB  4.1 MB/s
     http_req_blocked...............: avg=2.82µs  min=861ns   med=2.23µs  max=3.89ms   p(90)=3.56µs  p(95)=4.28µs   p(99.9)=28.53µs
     http_req_connecting............: avg=223ns   min=0s      med=0s      max=3.69ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.39ms min=8.24ms  med=13.94ms max=306.39ms p(90)=17.98ms p(95)=19.41ms  p(99.9)=27.64ms
       { expected_response:true }...: avg=14.39ms min=8.24ms  med=13.94ms max=306.39ms p(90)=17.98ms p(95)=19.41ms  p(99.9)=27.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 410820
     http_req_receiving.............: avg=75.47µs min=24.28µs med=45.71µs max=245.22ms p(90)=95.92µs p(95)=186.64µs p(99.9)=2.28ms 
     http_req_sending...............: avg=33.29µs min=4.14µs  med=8.28µs  max=226.35ms p(90)=16.22µs p(95)=98.89µs  p(99.9)=2.07ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.28ms min=8.19ms  med=13.84ms max=263.58ms p(90)=17.86ms p(95)=19.28ms  p(99.9)=27.36ms
     http_reqs......................: 410820  3396.461172/s
     iteration_duration.............: avg=14.6ms  min=8.42ms  med=14.14ms max=315.13ms p(90)=18.17ms p(95)=19.6ms   p(99.9)=27.89ms
     iterations.....................: 410720  3395.63442/s
     success_rate...................: 100.00% ✓ 410720      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1013295     ✗ 0     
     data_received..................: 30 GB   244 MB/s
     data_sent......................: 406 MB  3.3 MB/s
     http_req_blocked...............: avg=2.51µs  min=852ns   med=1.87µs  max=4.13ms   p(90)=3.16µs  p(95)=3.94µs   p(99.9)=24.47µs
     http_req_connecting............: avg=267ns   min=0s      med=0s      max=4.08ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.55ms min=11.79ms med=17.11ms max=277.41ms p(90)=20.63ms p(95)=21.87ms  p(99.9)=28.82ms
       { expected_response:true }...: avg=17.55ms min=11.79ms med=17.11ms max=277.41ms p(90)=20.63ms p(95)=21.87ms  p(99.9)=28.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 337865
     http_req_receiving.............: avg=68.08µs min=24.77µs med=45.33µs max=175.56ms p(90)=92.53µs p(95)=146.53µs p(99.9)=1.59ms 
     http_req_sending...............: avg=28.36µs min=4.41µs  med=8.04µs  max=100.88ms p(90)=16.99µs p(95)=81.62µs  p(99.9)=1.59ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.45ms min=11.72ms med=17.02ms max=276.74ms p(90)=20.53ms p(95)=21.76ms  p(99.9)=28.5ms 
     http_reqs......................: 337865  2783.018695/s
     iteration_duration.............: avg=17.75ms min=11.97ms med=17.31ms max=301.34ms p(90)=20.83ms p(95)=22.07ms  p(99.9)=29.05ms
     iterations.....................: 337765  2782.194988/s
     success_rate...................: 100.00% ✓ 337765      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1003695     ✗ 0     
     data_received..................: 29 GB   241 MB/s
     data_sent......................: 402 MB  3.3 MB/s
     http_req_blocked...............: avg=2.92µs  min=922ns   med=2.25µs  max=4.2ms    p(90)=3.64µs  p(95)=4.37µs   p(99.9)=31.6µs 
     http_req_connecting............: avg=301ns   min=0s      med=0s      max=4.16ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.71ms min=11.94ms med=17.28ms max=277.42ms p(90)=20.76ms p(95)=22.03ms  p(99.9)=28.83ms
       { expected_response:true }...: avg=17.71ms min=11.94ms med=17.28ms max=277.42ms p(90)=20.76ms p(95)=22.03ms  p(99.9)=28.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 334665
     http_req_receiving.............: avg=69.4µs  min=24.04µs med=46.36µs max=113.63ms p(90)=92.64µs p(95)=147.99µs p(99.9)=1.37ms 
     http_req_sending...............: avg=28.82µs min=4.31µs  med=8.46µs  max=166.81ms p(90)=16.18µs p(95)=86.25µs  p(99.9)=1.39ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.61ms min=11.89ms med=17.18ms max=277.06ms p(90)=20.66ms p(95)=21.91ms  p(99.9)=28.62ms
     http_reqs......................: 334665  2756.480389/s
     iteration_duration.............: avg=17.92ms min=12.14ms med=17.48ms max=294.48ms p(90)=20.96ms p(95)=22.23ms  p(99.9)=29.07ms
     iterations.....................: 334565  2755.656735/s
     success_rate...................: 100.00% ✓ 334565      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 753744      ✗ 0     
     data_received..................: 22 GB   180 MB/s
     data_sent......................: 302 MB  2.5 MB/s
     http_req_blocked...............: avg=3.44µs  min=972ns   med=2.48µs  max=10.33ms  p(90)=3.93µs  p(95)=4.62µs   p(99.9)=32.08µs 
     http_req_connecting............: avg=639ns   min=0s      med=0s      max=10.3ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.65ms min=17.02ms med=23.28ms max=310.68ms p(90)=26.81ms p(95)=27.95ms  p(99.9)=34.14ms 
       { expected_response:true }...: avg=23.65ms min=17.02ms med=23.28ms max=310.68ms p(90)=26.81ms p(95)=27.95ms  p(99.9)=34.14ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 251348
     http_req_receiving.............: avg=67.16µs min=24.59µs med=51.5µs  max=57.87ms  p(90)=90.77µs p(95)=116.52µs p(99.9)=965.59µs
     http_req_sending...............: avg=26.84µs min=4.22µs  med=9.69µs  max=209.49ms p(90)=16.57µs p(95)=24.49µs  p(99.9)=1.02ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.56ms min=16.91ms med=23.19ms max=307.63ms p(90)=26.72ms p(95)=27.85ms  p(99.9)=33.91ms 
     http_reqs......................: 251348  2062.523109/s
     iteration_duration.............: avg=23.87ms min=17.44ms med=23.49ms max=320.87ms p(90)=27.02ms p(95)=28.15ms  p(99.9)=34.34ms 
     iterations.....................: 251248  2061.702524/s
     success_rate...................: 100.00% ✓ 251248      ✗ 0     
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

     checks.........................: 100.00% ✓ 531423      ✗ 0     
     data_received..................: 16 GB   127 MB/s
     data_sent......................: 213 MB  1.7 MB/s
     http_req_blocked...............: avg=3.2µs   min=861ns   med=2.15µs  max=3.98ms   p(90)=4.48µs   p(95)=5.43µs   p(99.9)=39.86µs
     http_req_connecting............: avg=505ns   min=0s      med=0s      max=3.96ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.62ms min=17.31ms med=33.3ms  max=300ms    p(90)=39.12ms  p(95)=40.79ms  p(99.9)=49.54ms
       { expected_response:true }...: avg=33.62ms min=17.31ms med=33.3ms  max=300ms    p(90)=39.12ms  p(95)=40.79ms  p(99.9)=49.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 177241
     http_req_receiving.............: avg=83.44µs min=26.16µs med=54.75µs max=232.2ms  p(90)=116.56µs p(95)=155.05µs p(99.9)=1.22ms 
     http_req_sending...............: avg=25.79µs min=4.43µs  med=9.17µs  max=42.73ms  p(90)=21.77µs  p(95)=31.35µs  p(99.9)=1.06ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.51ms min=17.2ms  med=33.2ms  max=299.4ms  p(90)=39.01ms  p(95)=40.69ms  p(99.9)=49.24ms
     http_reqs......................: 177241  1453.56311/s
     iteration_duration.............: avg=33.86ms min=21.15ms med=33.53ms max=308.46ms p(90)=39.33ms  p(95)=41.01ms  p(99.9)=49.78ms
     iterations.....................: 177141  1452.743004/s
     success_rate...................: 100.00% ✓ 177141      ✗ 0     
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

     checks.........................: 100.00% ✓ 527481      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 211 MB  1.7 MB/s
     http_req_blocked...............: avg=3µs     min=922ns   med=2.15µs  max=3.48ms   p(90)=3.64µs  p(95)=4.36µs  p(99.9)=29.77µs 
     http_req_connecting............: avg=533ns   min=0s      med=0s      max=3.45ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=33.89ms min=18.36ms med=33.41ms max=295.56ms p(90)=39.75ms p(95)=41.95ms p(99.9)=53.74ms 
       { expected_response:true }...: avg=33.89ms min=18.36ms med=33.41ms max=295.56ms p(90)=39.75ms p(95)=41.95ms p(99.9)=53.74ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 175927
     http_req_receiving.............: avg=68.15µs min=26.57µs med=56.24µs max=211.08ms p(90)=91.69µs p(95)=107.2µs p(99.9)=774.68µs
     http_req_sending...............: avg=20.95µs min=4.79µs  med=10.59µs max=191.1ms  p(90)=16.71µs p(95)=20.45µs p(99.9)=723.9µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=33.8ms  min=18.31ms med=33.32ms max=294.88ms p(90)=39.67ms p(95)=41.86ms p(99.9)=53.6ms  
     http_reqs......................: 175927  1442.259196/s
     iteration_duration.............: avg=34.11ms min=20.83ms med=33.61ms max=311.14ms p(90)=39.96ms p(95)=42.16ms p(99.9)=54.09ms 
     iterations.....................: 175827  1441.439391/s
     success_rate...................: 100.00% ✓ 175827      ✗ 0     
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

     checks.........................: 100.00% ✓ 517683      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 208 MB  1.7 MB/s
     http_req_blocked...............: avg=2.91µs  min=972ns   med=2.1µs   max=4ms      p(90)=3.56µs  p(95)=4.25µs   p(99.9)=30.84µs 
     http_req_connecting............: avg=495ns   min=0s      med=0s      max=3.95ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.55ms min=18ms    med=34ms    max=313.01ms p(90)=41.17ms p(95)=43.51ms  p(99.9)=56.01ms 
       { expected_response:true }...: avg=34.55ms min=18ms    med=34ms    max=313.01ms p(90)=41.17ms p(95)=43.51ms  p(99.9)=56.01ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 172661
     http_req_receiving.............: avg=71.92µs min=25.59µs med=59.65µs max=97.93ms  p(90)=97.71µs p(95)=114.78µs p(99.9)=715.83µs
     http_req_sending...............: avg=20.6µs  min=4.75µs  med=10.14µs max=116.2ms  p(90)=16.81µs p(95)=20.68µs  p(99.9)=725.83µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.46ms min=17.88ms med=33.91ms max=309.9ms  p(90)=41.08ms p(95)=43.41ms  p(99.9)=55.88ms 
     http_reqs......................: 172661  1415.789044/s
     iteration_duration.............: avg=34.76ms min=20.66ms med=34.2ms  max=321.51ms p(90)=41.36ms p(95)=43.7ms   p(99.9)=56.31ms 
     iterations.....................: 172561  1414.969062/s
     success_rate...................: 100.00% ✓ 172561      ✗ 0     
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

     checks.........................: 100.00% ✓ 217431     ✗ 0    
     data_received..................: 6.4 GB  52 MB/s
     data_sent......................: 87 MB   713 kB/s
     http_req_blocked...............: avg=5.18µs  min=1.1µs   med=2.69µs  max=6.61ms   p(90)=4.19µs   p(95)=4.81µs   p(99.9)=46.08µs 
     http_req_connecting............: avg=2.22µs  min=0s      med=0s      max=6.59ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=82.46ms min=20.66ms med=82ms    max=314.68ms p(90)=112.9ms  p(95)=122.63ms p(99.9)=220.15ms
       { expected_response:true }...: avg=82.46ms min=20.66ms med=82ms    max=314.68ms p(90)=112.9ms  p(95)=122.63ms p(99.9)=220.15ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 72577
     http_req_receiving.............: avg=81.32µs min=29.7µs  med=71.42µs max=122.25ms p(90)=106.17µs p(95)=118.97µs p(99.9)=494.86µs
     http_req_sending...............: avg=20.97µs min=4.92µs  med=13.81µs max=150.95ms p(90)=19.79µs  p(95)=21.84µs  p(99.9)=645.47µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=82.36ms min=20.56ms med=81.91ms max=287.88ms p(90)=112.81ms p(95)=122.52ms p(99.9)=219.65ms
     http_reqs......................: 72577   593.885155/s
     iteration_duration.............: avg=82.79ms min=25.29ms med=82.26ms max=323.81ms p(90)=113.15ms p(95)=122.91ms p(99.9)=222.13ms
     iterations.....................: 72477   593.066872/s
     success_rate...................: 100.00% ✓ 72477      ✗ 0    
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

     checks.........................: 100.00% ✓ 185019     ✗ 0    
     data_received..................: 5.4 GB  44 MB/s
     data_sent......................: 74 MB   607 kB/s
     http_req_blocked...............: avg=5.21µs  min=1.34µs  med=3.34µs  max=3.83ms   p(90)=4.81µs   p(95)=5.45µs   p(99.9)=53.74µs 
     http_req_connecting............: avg=1.59µs  min=0s      med=0s      max=3.78ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=96.93ms min=19.98ms med=94.96ms max=312.71ms p(90)=122.92ms p(95)=131.73ms p(99.9)=174.34ms
       { expected_response:true }...: avg=96.93ms min=19.98ms med=94.96ms max=312.71ms p(90)=122.92ms p(95)=131.73ms p(99.9)=174.34ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 61773
     http_req_receiving.............: avg=83.65µs min=31.74µs med=74.59µs max=191.57ms p(90)=106.78µs p(95)=118.59µs p(99.9)=499.15µs
     http_req_sending...............: avg=28.8µs  min=5.52µs  med=15.17µs max=180.92ms p(90)=20.69µs  p(95)=22.79µs  p(99.9)=536.12µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=96.82ms min=19.89ms med=94.86ms max=306.05ms p(90)=122.81ms p(95)=131.62ms p(99.9)=172.98ms
     http_reqs......................: 61773   505.450965/s
     iteration_duration.............: avg=97.31ms min=26.93ms med=95.23ms max=340.1ms  p(90)=123.19ms p(95)=131.99ms p(99.9)=174.99ms
     iterations.....................: 61673   504.632726/s
     success_rate...................: 100.00% ✓ 61673      ✗ 0    
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

     checks.........................: 100.00% ✓ 142140     ✗ 0    
     data_received..................: 4.2 GB  34 MB/s
     data_sent......................: 57 MB   466 kB/s
     http_req_blocked...............: avg=4.7µs    min=1.08µs  med=2.67µs   max=3.79ms   p(90)=4.01µs   p(95)=4.54µs   p(99.9)=393.71µs
     http_req_connecting............: avg=1.83µs   min=0s      med=0s       max=3.75ms   p(90)=0s       p(95)=0s       p(99.9)=373.39µs
     http_req_duration..............: avg=126.22ms min=20.8ms  med=124.34ms max=359.12ms p(90)=156.68ms p(95)=167.2ms  p(99.9)=214.09ms
       { expected_response:true }...: avg=126.22ms min=20.8ms  med=124.34ms max=359.12ms p(90)=156.68ms p(95)=167.2ms  p(99.9)=214.09ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 47480
     http_req_receiving.............: avg=83.07µs  min=28.55µs med=71.29µs  max=188.18ms p(90)=102.78µs p(95)=114.92µs p(99.9)=474.19µs
     http_req_sending...............: avg=20.46µs  min=5.17µs  med=13.68µs  max=55.59ms  p(90)=19.16µs  p(95)=20.92µs  p(99.9)=490.89µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=126.12ms min=20.73ms med=124.24ms max=358.63ms p(90)=156.57ms p(95)=167.09ms p(99.9)=213.17ms
     http_reqs......................: 47480   388.080438/s
     iteration_duration.............: avg=126.68ms min=50.52ms med=124.62ms max=364.98ms p(90)=156.95ms p(95)=167.51ms p(99.9)=218ms   
     iterations.....................: 47380   387.263083/s
     success_rate...................: 100.00% ✓ 47380      ✗ 0    
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

     checks.........................: 100.00% ✓ 104355     ✗ 0    
     data_received..................: 3.1 GB  25 MB/s
     data_sent......................: 42 MB   343 kB/s
     http_req_blocked...............: avg=6.08µs   min=1.09µs  med=3.13µs   max=3.73ms   p(90)=4.51µs   p(95)=5.08µs   p(99.9)=1.5ms   
     http_req_connecting............: avg=2.75µs   min=0s      med=0s       max=3.69ms   p(90)=0s       p(95)=0s       p(99.9)=1.47ms  
     http_req_duration..............: avg=171.85ms min=16.91ms med=157.91ms max=780.97ms p(90)=194.63ms p(95)=211.23ms p(99.9)=710.19ms
       { expected_response:true }...: avg=171.85ms min=16.91ms med=157.91ms max=780.97ms p(90)=194.63ms p(95)=211.23ms p(99.9)=710.19ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 34885
     http_req_receiving.............: avg=94.34µs  min=31.81µs med=85.1µs   max=144.38ms p(90)=114.3µs  p(95)=125.28µs p(99.9)=602.35µs
     http_req_sending...............: avg=23.32µs  min=5.48µs  med=16.28µs  max=109.56ms p(90)=20.74µs  p(95)=22.49µs  p(99.9)=392.68µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=171.74ms min=16.83ms med=157.78ms max=780.9ms  p(90)=194.51ms p(95)=211.07ms p(99.9)=710.09ms
     http_reqs......................: 34885   285.708098/s
     iteration_duration.............: avg=172.57ms min=45.94ms med=158.25ms max=781.14ms p(90)=194.92ms p(95)=211.7ms  p(99.9)=710.49ms
     iterations.....................: 34785   284.889098/s
     success_rate...................: 100.00% ✓ 34785      ✗ 0    
     vus............................: 48      min=0        max=50 
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

     checks.........................: 100.00% ✓ 97083      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   318 kB/s
     http_req_blocked...............: avg=5.89µs   min=1.16µs  med=3µs      max=3.97ms   p(90)=4.32µs   p(95)=4.86µs   p(99.9)=1.07ms  
     http_req_connecting............: avg=2.71µs   min=0s      med=0s       max=3.93ms   p(90)=0s       p(95)=0s       p(99.9)=1.04ms  
     http_req_duration..............: avg=184.72ms min=22.98ms med=191.37ms max=376.05ms p(90)=243.07ms p(95)=246.97ms p(99.9)=318.8ms 
       { expected_response:true }...: avg=184.72ms min=22.98ms med=191.37ms max=376.05ms p(90)=243.07ms p(95)=246.97ms p(99.9)=318.8ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 32461
     http_req_receiving.............: avg=84.86µs  min=31.02µs med=81.84µs  max=8.32ms   p(90)=111.72µs p(95)=123.03µs p(99.9)=470.52µs
     http_req_sending...............: avg=22.3µs   min=5.36µs  med=15.36µs  max=41.9ms   p(90)=19.86µs  p(95)=21.68µs  p(99.9)=550.11µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.62ms min=22.9ms  med=191.22ms max=375.5ms  p(90)=242.96ms p(95)=246.87ms p(99.9)=318.69ms
     http_reqs......................: 32461   264.785739/s
     iteration_duration.............: avg=185.49ms min=43.15ms med=193.54ms max=396.33ms p(90)=243.33ms p(95)=247.24ms p(99.9)=320.2ms 
     iterations.....................: 32361   263.970035/s
     success_rate...................: 100.00% ✓ 32361      ✗ 0    
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

