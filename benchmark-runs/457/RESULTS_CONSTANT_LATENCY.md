## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.2 | 3,408 | 3,423 | 3,395 | 0.3% | 372 MB | 111.9 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.7 | 3,407 | 3,414 | 3,374 | 0.5% | 379 MB | 113.9 KB |  |
| fusion-aot-11 | 16.7.2 | 3,358 | 3,361 | 3,354 | 0.1% | 130 MB | 39.7 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.7 | 3,349 | 3,363 | 3,337 | 0.4% | 133 MB | 40.5 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,283 | 3,296 | 3,227 | 0.9% | 2,309 MB | 720.3 KB |  |
| fusion-fed-net-11 | 16.7.2 | 2,806 | 2,811 | 2,792 | 0.3% | 400 MB | 146.0 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.7 | 2,803 | 2,815 | 2,793 | 0.3% | 408 MB | 148.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.7 | 2,752 | 2,756 | 2,751 | 0.1% | 158 MB | 58.8 KB |  |
| fusion-fed-aot-11 | 16.7.2 | 2,736 | 2,742 | 2,728 | 0.2% | 134 MB | 50.3 KB |  |
| hive-router | v0.3.6 | 2,039 | 2,047 | 2,037 | 0.2% | 90 MB | 45.3 KB |  |
| grafbase | 0.53.5 | 1,445 | 1,458 | 1,442 | 0.5% | 101 MB | 71.7 KB |  |
| cosmo | 0.363.0 | 1,421 | 1,422 | 1,420 | 0.1% | 146 MB | 105.1 KB |  |
| caliban | 3.2.0 | 1,359 | 1,359 | 1,357 | 0.1% | 4,626 MB | 3,485.8 KB |  |
| apollo-router | v2.19.0 | 527 | 528 | 527 | 0.1% | 183 MB | 355.1 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 520 | 523 | 519 | 0.3% | 2,755 MB | 5,424.6 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 420 | 420 | 419 | 0.1% | 208 MB | 508.3 KB |  |
| hive-gateway | 2.15.3 | 264 | 265 | 263 | 0.4% | 3,544 MB | 13,744.5 KB |  |
| apollo-gateway | 2.14.4 | 263 | 264 | 261 | 0.4% | 2,155 MB | 8,390.3 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1236561     ✗ 0     
     data_received..................: 36 GB   298 MB/s
     data_sent......................: 495 MB  4.1 MB/s
     http_req_blocked...............: avg=2.42µs  min=781ns   med=1.8µs   max=4.55ms   p(90)=3.16µs  p(95)=4.03µs   p(99.9)=25.78µs
     http_req_connecting............: avg=212ns   min=0s      med=0s      max=3.51ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.35ms min=7.91ms  med=13.94ms max=285.15ms p(90)=17.79ms p(95)=19.12ms  p(99.9)=26.71ms
       { expected_response:true }...: avg=14.35ms min=7.91ms  med=13.94ms max=285.15ms p(90)=17.79ms p(95)=19.12ms  p(99.9)=26.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 412287
     http_req_receiving.............: avg=68.33µs min=23.67µs med=42.18µs max=83.55ms  p(90)=92.37µs p(95)=169.22µs p(99.9)=2.08ms 
     http_req_sending...............: avg=31.78µs min=4.06µs  med=7.67µs  max=208.22ms p(90)=16.87µs p(95)=90.16µs  p(99.9)=1.79ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.25ms min=7.85ms  med=13.85ms max=284.6ms  p(90)=17.69ms p(95)=19ms     p(99.9)=26.44ms
     http_reqs......................: 412287  3408.700423/s
     iteration_duration.............: avg=14.54ms min=8.03ms  med=14.14ms max=296.27ms p(90)=17.99ms p(95)=19.31ms  p(99.9)=26.95ms
     iterations.....................: 412187  3407.873645/s
     success_rate...................: 100.00% ✓ 412187      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1236078     ✗ 0     
     data_received..................: 36 GB   298 MB/s
     data_sent......................: 495 MB  4.1 MB/s
     http_req_blocked...............: avg=2.79µs  min=832ns   med=2.19µs  max=4.01ms   p(90)=3.62µs  p(95)=4.43µs   p(99.9)=30.49µs
     http_req_connecting............: avg=223ns   min=0s      med=0s      max=3.97ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.35ms min=8.23ms  med=13.9ms  max=283.75ms p(90)=17.9ms  p(95)=19.3ms   p(99.9)=27.46ms
       { expected_response:true }...: avg=14.35ms min=8.23ms  med=13.9ms  max=283.75ms p(90)=17.9ms  p(95)=19.3ms   p(99.9)=27.46ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 412126
     http_req_receiving.............: avg=74.54µs min=24.59µs med=45.58µs max=123.88ms p(90)=97.2µs  p(95)=184.92µs p(99.9)=2.27ms 
     http_req_sending...............: avg=32.94µs min=4.5µs   med=8.51µs  max=115.58ms p(90)=17.96µs p(95)=98.31µs  p(99.9)=2.03ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.24ms min=8.15ms  med=13.8ms  max=266.87ms p(90)=17.78ms p(95)=19.17ms  p(99.9)=27.24ms
     http_reqs......................: 412126  3407.192826/s
     iteration_duration.............: avg=14.55ms min=8.47ms  med=14.1ms  max=294.02ms p(90)=18.1ms  p(95)=19.49ms  p(99.9)=27.69ms
     iterations.....................: 412026  3406.36609/s
     success_rate...................: 100.00% ✓ 412026      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1218417     ✗ 0     
     data_received..................: 36 GB   294 MB/s
     data_sent......................: 488 MB  4.0 MB/s
     http_req_blocked...............: avg=2.39µs  min=782ns   med=1.83µs  max=3.39ms   p(90)=3.02µs  p(95)=3.75µs   p(99.9)=23.82µs
     http_req_connecting............: avg=206ns   min=0s      med=0s      max=3.36ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.57ms min=8.48ms  med=14.14ms max=280.06ms p(90)=17.99ms p(95)=19.36ms  p(99.9)=27.73ms
       { expected_response:true }...: avg=14.57ms min=8.48ms  med=14.14ms max=280.06ms p(90)=17.99ms p(95)=19.36ms  p(99.9)=27.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 406239
     http_req_receiving.............: avg=66.42µs min=23.45µs med=41.91µs max=165.32ms p(90)=88.45µs p(95)=162.87µs p(99.9)=1.75ms 
     http_req_sending...............: avg=29.71µs min=4.12µs  med=7.71µs  max=180.72ms p(90)=15.45µs p(95)=89.24µs  p(99.9)=1.79ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.47ms min=8.35ms  med=14.04ms max=279.51ms p(90)=17.88ms p(95)=19.24ms  p(99.9)=27.47ms
     http_reqs......................: 406239  3358.321026/s
     iteration_duration.............: avg=14.76ms min=8.63ms  med=14.33ms max=296.55ms p(90)=18.17ms p(95)=19.55ms  p(99.9)=27.95ms
     iterations.....................: 406139  3357.49434/s
     success_rate...................: 100.00% ✓ 406139      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1215108     ✗ 0     
     data_received..................: 35 GB   293 MB/s
     data_sent......................: 487 MB  4.0 MB/s
     http_req_blocked...............: avg=2.72µs  min=762ns   med=1.82µs  max=7.41ms   p(90)=3µs     p(95)=3.73µs   p(99.9)=22.1µs 
     http_req_connecting............: avg=534ns   min=0s      med=0s      max=7.39ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.61ms min=8.14ms  med=14.19ms max=279.31ms p(90)=18.09ms p(95)=19.46ms  p(99.9)=27.89ms
       { expected_response:true }...: avg=14.61ms min=8.14ms  med=14.19ms max=279.31ms p(90)=18.09ms p(95)=19.46ms  p(99.9)=27.89ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 405136
     http_req_receiving.............: avg=67.43µs min=23.85µs med=42.94µs max=195.57ms p(90)=88.23µs p(95)=161.12µs p(99.9)=1.71ms 
     http_req_sending...............: avg=29.63µs min=4.14µs  med=7.69µs  max=113.45ms p(90)=15.69µs p(95)=88.42µs  p(99.9)=1.8ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.51ms min=8.08ms  med=14.1ms  max=278.13ms p(90)=17.99ms p(95)=19.35ms  p(99.9)=27.58ms
     http_reqs......................: 405136  3349.254653/s
     iteration_duration.............: avg=14.8ms  min=8.32ms  med=14.38ms max=289.8ms  p(90)=18.28ms p(95)=19.65ms  p(99.9)=28.12ms
     iterations.....................: 405036  3348.427954/s
     success_rate...................: 100.00% ✓ 405036      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-10-25-0247)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1191300     ✗ 0     
     data_received..................: 35 GB   287 MB/s
     data_sent......................: 477 MB  3.9 MB/s
     http_req_blocked...............: avg=2.51µs  min=781ns   med=1.92µs  max=4.03ms   p(90)=3.32µs  p(95)=4.13µs   p(99.9)=25.27µs
     http_req_connecting............: avg=222ns   min=0s      med=0s      max=3.98ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.9ms  min=8.46ms  med=14.58ms max=293.81ms p(90)=17.97ms p(95)=19.17ms  p(99.9)=26.9ms 
       { expected_response:true }...: avg=14.9ms  min=8.46ms  med=14.58ms max=293.81ms p(90)=17.97ms p(95)=19.17ms  p(99.9)=26.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 397200
     http_req_receiving.............: avg=81.25µs min=22.92µs med=42.56µs max=257.13ms p(90)=90.1µs  p(95)=164.84µs p(99.9)=1.59ms 
     http_req_sending...............: avg=29.69µs min=4.26µs  med=8.14µs  max=26.5ms   p(90)=16.85µs p(95)=92.71µs  p(99.9)=1.68ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.79ms min=8.4ms   med=14.48ms max=117.82ms p(90)=17.87ms p(95)=19.06ms  p(99.9)=26.71ms
     http_reqs......................: 397200  3283.705273/s
     iteration_duration.............: avg=15.1ms  min=8.58ms  med=14.77ms max=304.22ms p(90)=18.16ms p(95)=19.36ms  p(99.9)=27.36ms
     iterations.....................: 397100  3282.87856/s
     success_rate...................: 100.00% ✓ 397100      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1021674     ✗ 0     
     data_received..................: 30 GB   246 MB/s
     data_sent......................: 409 MB  3.4 MB/s
     http_req_blocked...............: avg=2.49µs  min=792ns   med=1.78µs  max=6.29ms   p(90)=3.11µs  p(95)=3.92µs   p(99.9)=24.31µs
     http_req_connecting............: avg=323ns   min=0s      med=0s      max=6.12ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.4ms  min=11.75ms med=16.99ms max=279.8ms  p(90)=20.37ms p(95)=21.61ms  p(99.9)=28.66ms
       { expected_response:true }...: avg=17.4ms  min=11.75ms med=16.99ms max=279.8ms  p(90)=20.37ms p(95)=21.61ms  p(99.9)=28.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 340658
     http_req_receiving.............: avg=67.24µs min=24.7µs  med=44.75µs max=148.2ms  p(90)=90.34µs p(95)=143.63µs p(99.9)=1.47ms 
     http_req_sending...............: avg=27.48µs min=3.94µs  med=7.57µs  max=177.61ms p(90)=15.68µs p(95)=79.84µs  p(99.9)=1.42ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.31ms min=11.62ms med=16.9ms  max=271.91ms p(90)=20.27ms p(95)=21.5ms   p(99.9)=28.32ms
     http_reqs......................: 340658  2806.278928/s
     iteration_duration.............: avg=17.6ms  min=11.95ms med=17.18ms max=291.54ms p(90)=20.57ms p(95)=21.8ms   p(99.9)=28.87ms
     iterations.....................: 340558  2805.455146/s
     success_rate...................: 100.00% ✓ 340558      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1020882     ✗ 0     
     data_received..................: 30 GB   245 MB/s
     data_sent......................: 409 MB  3.4 MB/s
     http_req_blocked...............: avg=2.44µs  min=772ns   med=1.86µs  max=3.52ms   p(90)=3.06µs  p(95)=3.81µs   p(99.9)=24.44µs
     http_req_connecting............: avg=251ns   min=0s      med=0s      max=3.49ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.42ms min=11.76ms med=16.99ms max=291.41ms p(90)=20.43ms p(95)=21.67ms  p(99.9)=28.67ms
       { expected_response:true }...: avg=17.42ms min=11.76ms med=16.99ms max=291.41ms p(90)=20.43ms p(95)=21.67ms  p(99.9)=28.67ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 340394
     http_req_receiving.............: avg=66.86µs min=24.41µs med=45.33µs max=145.94ms p(90)=89.93µs p(95)=145.65µs p(99.9)=1.49ms 
     http_req_sending...............: avg=29.22µs min=4.4µs   med=7.93µs  max=155.09ms p(90)=15.54µs p(95)=82.83µs  p(99.9)=1.49ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.32ms min=11.67ms med=16.9ms  max=291ms    p(90)=20.34ms p(95)=21.56ms  p(99.9)=28.48ms
     http_reqs......................: 340394  2803.954778/s
     iteration_duration.............: avg=17.62ms min=11.93ms med=17.19ms max=298.91ms p(90)=20.63ms p(95)=21.86ms  p(99.9)=28.9ms 
     iterations.....................: 340294  2803.13104/s
     success_rate...................: 100.00% ✓ 340294      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1002234     ✗ 0     
     data_received..................: 29 GB   241 MB/s
     data_sent......................: 402 MB  3.3 MB/s
     http_req_blocked...............: avg=2.85µs  min=861ns   med=2.21µs  max=4.05ms   p(90)=3.59µs  p(95)=4.35µs   p(99.9)=30.13µs
     http_req_connecting............: avg=290ns   min=0s      med=0s      max=4ms      p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.74ms min=11.6ms  med=17.32ms max=284.74ms p(90)=20.77ms p(95)=22.05ms  p(99.9)=29.2ms 
       { expected_response:true }...: avg=17.74ms min=11.6ms  med=17.32ms max=284.74ms p(90)=20.77ms p(95)=22.05ms  p(99.9)=29.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 334178
     http_req_receiving.............: avg=68.09µs min=24.25µs med=46µs    max=28.51ms  p(90)=92.31µs p(95)=152.08µs p(99.9)=1.36ms 
     http_req_sending...............: avg=28.86µs min=4.14µs  med=8.46µs  max=109.02ms p(90)=16.8µs  p(95)=86.86µs  p(99.9)=1.42ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.64ms min=11.53ms med=17.22ms max=275.04ms p(90)=20.67ms p(95)=21.93ms  p(99.9)=28.92ms
     http_reqs......................: 334178  2752.564976/s
     iteration_duration.............: avg=17.95ms min=11.78ms med=17.52ms max=294.71ms p(90)=20.97ms p(95)=22.25ms  p(99.9)=29.46ms
     iterations.....................: 334078  2751.741294/s
     success_rate...................: 100.00% ✓ 334078      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 996333      ✗ 0     
     data_received..................: 29 GB   239 MB/s
     data_sent......................: 399 MB  3.3 MB/s
     http_req_blocked...............: avg=3µs     min=812ns   med=1.84µs  max=9.63ms   p(90)=3.23µs  p(95)=4.04µs   p(99.9)=26.77µs
     http_req_connecting............: avg=752ns   min=0s      med=0s      max=9.58ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.85ms min=11.69ms med=17.43ms max=286.77ms p(90)=20.98ms p(95)=22.28ms  p(99.9)=29.74ms
       { expected_response:true }...: avg=17.85ms min=11.69ms med=17.43ms max=286.77ms p(90)=20.98ms p(95)=22.28ms  p(99.9)=29.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 332211
     http_req_receiving.............: avg=65.5µs  min=23.97µs med=43.59µs max=117.54ms p(90)=89.98µs p(95)=145.82µs p(99.9)=1.4ms  
     http_req_sending...............: avg=27.66µs min=4.27µs  med=7.93µs  max=60.3ms   p(90)=16.65µs p(95)=81.27µs  p(99.9)=1.59ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.76ms min=11.65ms med=17.34ms max=284.32ms p(90)=20.88ms p(95)=22.16ms  p(99.9)=29.57ms
     http_reqs......................: 332211  2736.299688/s
     iteration_duration.............: avg=18.05ms min=11.86ms med=17.62ms max=303.81ms p(90)=21.18ms p(95)=22.47ms  p(99.9)=30.03ms
     iterations.....................: 332111  2735.476025/s
     success_rate...................: 100.00% ✓ 332111      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 745512      ✗ 0     
     data_received..................: 22 GB   178 MB/s
     data_sent......................: 299 MB  2.5 MB/s
     http_req_blocked...............: avg=2.74µs  min=852ns   med=2.07µs  max=3.56ms   p(90)=3.53µs  p(95)=4.22µs   p(99.9)=28.83µs 
     http_req_connecting............: avg=347ns   min=0s      med=0s      max=3.51ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.92ms min=16.97ms med=23.57ms max=273.12ms p(90)=27.04ms p(95)=28.15ms  p(99.9)=33.73ms 
       { expected_response:true }...: avg=23.92ms min=16.97ms med=23.57ms max=273.12ms p(90)=27.04ms p(95)=28.15ms  p(99.9)=33.73ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 248604
     http_req_receiving.............: avg=65.42µs min=24.22µs med=49.04µs max=131.79ms p(90)=91.09µs p(95)=116.35µs p(99.9)=918.24µs
     http_req_sending...............: avg=25.77µs min=4.35µs  med=9.05µs  max=180.07ms p(90)=16.93µs p(95)=24.18µs  p(99.9)=910.21µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.82ms min=16.92ms med=23.49ms max=272.67ms p(90)=26.95ms p(95)=28.05ms  p(99.9)=33.54ms 
     http_reqs......................: 248604  2039.778202/s
     iteration_duration.............: avg=24.13ms min=17.16ms med=23.78ms max=299.99ms p(90)=27.24ms p(95)=28.35ms  p(99.9)=33.93ms 
     iterations.....................: 248504  2038.957709/s
     success_rate...................: 100.00% ✓ 248504      ✗ 0     
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

     checks.........................: 100.00% ✓ 528333      ✗ 0     
     data_received..................: 15 GB   127 MB/s
     data_sent......................: 212 MB  1.7 MB/s
     http_req_blocked...............: avg=3.22µs  min=821ns   med=2.15µs  max=3.78ms   p(90)=4.46µs   p(95)=5.37µs   p(99.9)=38.34µs
     http_req_connecting............: avg=518ns   min=0s      med=0s      max=3.75ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.81ms min=17.63ms med=33.55ms max=310.16ms p(90)=39.52ms  p(95)=41.2ms   p(99.9)=49.62ms
       { expected_response:true }...: avg=33.81ms min=17.63ms med=33.55ms max=310.16ms p(90)=39.52ms  p(95)=41.2ms   p(99.9)=49.62ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 176211
     http_req_receiving.............: avg=82.15µs min=26.9µs  med=54.48µs max=179.08ms p(90)=117.33µs p(95)=156.87µs p(99.9)=1.43ms 
     http_req_sending...............: avg=27.63µs min=4.43µs  med=9.27µs  max=93.2ms   p(90)=21.9µs   p(95)=32.98µs  p(99.9)=1.23ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.7ms  min=17.56ms med=33.44ms max=309.89ms p(90)=39.42ms  p(95)=41.1ms   p(99.9)=49.26ms
     http_reqs......................: 176211  1445.130355/s
     iteration_duration.............: avg=34.06ms min=20.5ms  med=33.78ms max=320.13ms p(90)=39.74ms  p(95)=41.42ms  p(99.9)=49.87ms
     iterations.....................: 176111  1444.310242/s
     success_rate...................: 100.00% ✓ 176111      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.363.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 519750      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 208 MB  1.7 MB/s
     http_req_blocked...............: avg=3.48µs  min=1.08µs  med=2.62µs  max=4.08ms   p(90)=4.2µs    p(95)=4.93µs   p(99.9)=34.87µs 
     http_req_connecting............: avg=546ns   min=0s      med=0s      max=4.05ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.4ms  min=17.92ms med=33.84ms max=291.94ms p(90)=41.05ms  p(95)=43.41ms  p(99.9)=55.91ms 
       { expected_response:true }...: avg=34.4ms  min=17.92ms med=33.84ms max=291.94ms p(90)=41.05ms  p(95)=43.41ms  p(99.9)=55.91ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 173350
     http_req_receiving.............: avg=73.8µs  min=26.44µs med=60.96µs max=138.55ms p(90)=100.11µs p(95)=117.61µs p(99.9)=758.35µs
     http_req_sending...............: avg=23.96µs min=5.05µs  med=11.33µs max=186.02ms p(90)=18.22µs  p(95)=22.33µs  p(99.9)=797.73µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.3ms  min=17.84ms med=33.75ms max=291.41ms p(90)=40.95ms  p(95)=43.31ms  p(99.9)=55.73ms 
     http_reqs......................: 173350  1421.384426/s
     iteration_duration.............: avg=34.62ms min=20.81ms med=34.04ms max=309.52ms p(90)=41.25ms  p(95)=43.61ms  p(99.9)=56.26ms 
     iterations.....................: 173250  1420.564476/s
     success_rate...................: 100.00% ✓ 173250      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: caliban (HotChocolate subgraphs) (3.2.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 497256      ✗ 0     
     data_received..................: 15 GB   119 MB/s
     data_sent......................: 199 MB  1.6 MB/s
     http_req_blocked...............: avg=2.97µs  min=902ns   med=2.08µs  max=4.05ms   p(90)=3.37µs  p(95)=3.99µs   p(99.9)=31.82µs 
     http_req_connecting............: avg=627ns   min=0s      med=0s      max=4ms      p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.98ms min=18.15ms med=35.43ms max=298.15ms p(90)=42.75ms p(95)=45.1ms   p(99.9)=58.26ms 
       { expected_response:true }...: avg=35.98ms min=18.15ms med=35.43ms max=298.15ms p(90)=42.75ms p(95)=45.1ms   p(99.9)=58.26ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 165852
     http_req_receiving.............: avg=67.85µs min=26.54µs med=56.93µs max=120.32ms p(90)=89.84µs p(95)=104.46µs p(99.9)=754.35µs
     http_req_sending...............: avg=21.26µs min=4.54µs  med=10.27µs max=189.72ms p(90)=15.72µs p(95)=19.03µs  p(99.9)=700.41µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=35.89ms min=18.03ms med=35.35ms max=296.04ms p(90)=42.66ms p(95)=45.01ms  p(99.9)=58.06ms 
     http_reqs......................: 165852  1359.610858/s
     iteration_duration.............: avg=36.19ms min=21.37ms med=35.63ms max=307.75ms p(90)=42.94ms p(95)=45.29ms  p(99.9)=58.59ms 
     iterations.....................: 165752  1358.791084/s
     success_rate...................: 100.00% ✓ 165752      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.19.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 193098     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   634 kB/s
     http_req_blocked...............: avg=4.37µs  min=1.08µs  med=2.78µs  max=3.6ms    p(90)=4.24µs   p(95)=4.81µs   p(99.9)=44.66µs 
     http_req_connecting............: avg=1.39µs  min=0s      med=0s      max=3.56ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.87ms min=18.75ms med=91.16ms max=331.3ms  p(90)=117.03ms p(95)=125.38ms p(99.9)=163.57ms
       { expected_response:true }...: avg=92.87ms min=18.75ms med=91.16ms max=331.3ms  p(90)=117.03ms p(95)=125.38ms p(99.9)=163.57ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64466
     http_req_receiving.............: avg=79.1µs  min=28.92µs med=71.84µs max=109.89ms p(90)=104.48µs p(95)=116.97µs p(99.9)=505.05µs
     http_req_sending...............: avg=21.33µs min=4.64µs  med=13.74µs max=111.46ms p(90)=19.26µs  p(95)=21.25µs  p(99.9)=463.05µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.76ms min=18.62ms med=91.07ms max=330.82ms p(90)=116.93ms p(95)=125.29ms p(99.9)=162.41ms
     http_reqs......................: 64466   527.557671/s
     iteration_duration.............: avg=93.22ms min=30ms    med=91.41ms max=339.62ms p(90)=117.29ms p(95)=125.67ms p(99.9)=166.01ms
     iterations.....................: 64366   526.739321/s
     success_rate...................: 100.00% ✓ 64366      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 190752     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   626 kB/s
     http_req_blocked...............: avg=4.4µs   min=1.05µs  med=2.66µs  max=3.53ms   p(90)=4.13µs   p(95)=4.72µs   p(99.9)=45.88µs 
     http_req_connecting............: avg=1.5µs   min=0s      med=0s      max=3.49ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=94.03ms min=20.67ms med=90.94ms max=326.58ms p(90)=122.65ms p(95)=131.78ms p(99.9)=230.03ms
       { expected_response:true }...: avg=94.03ms min=20.67ms med=90.94ms max=326.58ms p(90)=122.65ms p(95)=131.78ms p(99.9)=230.03ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63684
     http_req_receiving.............: avg=78.7µs  min=28.49µs med=69.86µs max=123.14ms p(90)=104.78µs p(95)=117.32µs p(99.9)=511.93µs
     http_req_sending...............: avg=24.13µs min=4.81µs  med=13.6µs  max=143.54ms p(90)=19.62µs  p(95)=21.61µs  p(99.9)=534.32µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.93ms min=20.58ms med=90.85ms max=326.37ms p(90)=122.55ms p(95)=131.68ms p(99.9)=229.74ms
     http_reqs......................: 63684   520.85343/s
     iteration_duration.............: avg=94.38ms min=34.57ms med=91.2ms  max=340.31ms p(90)=122.9ms  p(95)=132.04ms p(99.9)=231.49ms
     iterations.....................: 63584   520.035558/s
     success_rate...................: 100.00% ✓ 63584      ✗ 0    
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

     checks.........................: 100.00% ✓ 153888     ✗ 0    
     data_received..................: 4.5 GB  37 MB/s
     data_sent......................: 62 MB   505 kB/s
     http_req_blocked...............: avg=4.88µs   min=1.02µs  med=2.91µs   max=4.1ms    p(90)=4.28µs   p(95)=4.82µs   p(99.9)=158.97µs
     http_req_connecting............: avg=1.76µs   min=0s      med=0s       max=4.07ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=116.54ms min=20.12ms med=114.88ms max=332.17ms p(90)=144.02ms p(95)=153.78ms p(99.9)=195.37ms
       { expected_response:true }...: avg=116.54ms min=20.12ms med=114.88ms max=332.17ms p(90)=144.02ms p(95)=153.78ms p(99.9)=195.37ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51396
     http_req_receiving.............: avg=79.28µs  min=28.26µs med=75.52µs  max=15.69ms  p(90)=106.84µs p(95)=118.89µs p(99.9)=459.35µs
     http_req_sending...............: avg=22.28µs  min=5.2µs   med=14.56µs  max=71.5ms   p(90)=19.96µs  p(95)=21.95µs  p(99.9)=542.64µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=116.44ms min=20.05ms med=114.78ms max=331.51ms p(90)=143.93ms p(95)=153.68ms p(99.9)=195.24ms
     http_reqs......................: 51396   420.184954/s
     iteration_duration.............: avg=116.98ms min=36.31ms med=115.16ms max=341.2ms  p(90)=144.3ms  p(95)=154.05ms p(99.9)=197.64ms
     iterations.....................: 51296   419.36741/s
     success_rate...................: 100.00% ✓ 51296      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 96594      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   317 kB/s
     http_req_blocked...............: avg=6.32µs   min=1.18µs  med=3.2µs    max=3.89ms   p(90)=4.6µs    p(95)=5.2µs    p(99.9)=1.39ms  
     http_req_connecting............: avg=2.92µs   min=0s      med=0s       max=3.86ms   p(90)=0s       p(95)=0s       p(99.9)=1.34ms  
     http_req_duration..............: avg=185.74ms min=17.86ms med=172.48ms max=765.55ms p(90)=217.34ms p(95)=244.72ms p(99.9)=670.12ms
       { expected_response:true }...: avg=185.74ms min=17.86ms med=172.48ms max=765.55ms p(90)=217.34ms p(95)=244.72ms p(99.9)=670.12ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32298
     http_req_receiving.............: avg=99.25µs  min=30.29µs med=89.52µs  max=80.03ms  p(90)=121.02µs p(95)=134.64µs p(99.9)=653.3µs 
     http_req_sending...............: avg=29.04µs  min=5.47µs  med=16.62µs  max=76.26ms  p(90)=20.89µs  p(95)=22.7µs   p(99.9)=401.47µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=185.61ms min=17.75ms med=172.37ms max=765.46ms p(90)=217.21ms p(95)=244.6ms  p(99.9)=670.01ms
     http_reqs......................: 32298   264.384691/s
     iteration_duration.............: avg=186.53ms min=34.49ms med=172.88ms max=765.79ms p(90)=217.66ms p(95)=245.5ms  p(99.9)=670.42ms
     iterations.....................: 32198   263.566112/s
     success_rate...................: 100.00% ✓ 32198      ✗ 0    
     vus............................: 19      min=0        max=50 
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

     checks.........................: 100.00% ✓ 96426      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   316 kB/s
     http_req_blocked...............: avg=11.09µs  min=1.1µs   med=3µs      max=8.96ms   p(90)=4.29µs   p(95)=4.82µs   p(99.9)=4ms     
     http_req_connecting............: avg=7.55µs   min=0s      med=0s       max=8.8ms    p(90)=0s       p(95)=0s       p(99.9)=3.62ms  
     http_req_duration..............: avg=185.98ms min=22.33ms med=186.1ms  max=367.22ms p(90)=197.04ms p(95)=201.31ms p(99.9)=269.65ms
       { expected_response:true }...: avg=185.98ms min=22.33ms med=186.1ms  max=367.22ms p(90)=197.04ms p(95)=201.31ms p(99.9)=269.65ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32242
     http_req_receiving.............: avg=86.93µs  min=30.08µs med=82.13µs  max=71.85ms  p(90)=111.03µs p(95)=121.39µs p(99.9)=425.29µs
     http_req_sending...............: avg=27.63µs  min=4.94µs  med=15.46µs  max=112.8ms  p(90)=19.59µs  p(95)=21.29µs  p(99.9)=701.96µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=185.86ms min=22.2ms  med=186ms    max=366.22ms p(90)=196.94ms p(95)=201.21ms p(99.9)=269.55ms
     http_reqs......................: 32242   263.007716/s
     iteration_duration.............: avg=186.77ms min=37.07ms med=186.42ms max=388.47ms p(90)=197.3ms  p(95)=201.57ms p(99.9)=270.91ms
     iterations.....................: 32142   262.191986/s
     success_rate...................: 100.00% ✓ 32142      ✗ 0    
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

