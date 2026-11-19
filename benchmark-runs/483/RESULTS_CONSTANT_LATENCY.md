## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-fed-aot-11 | 16.8.0-p.16 | 3,584 | 3,596 | 3,575 | 0.2% | 145 MB | 41.4 KB |  |
| fusion-aot-11 | 16.7.6 | 3,577 | 3,608 | 3,562 | 0.5% | 130 MB | 37.3 KB |  |
| fusion-net-11 | 16.7.6 | 3,565 | 3,576 | 3,544 | 0.4% | 391 MB | 112.3 KB |  |
| fusion-fed-net-11 | 16.7.6 | 3,564 | 3,570 | 3,557 | 0.2% | 392 MB | 112.6 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.16 | 3,562 | 3,566 | 3,552 | 0.2% | 374 MB | 107.4 KB |  |
| fusion-fed-aot-11 | 16.7.6 | 3,554 | 3,559 | 3,534 | 0.3% | 132 MB | 38.1 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.16 | 3,552 | 3,564 | 3,544 | 0.2% | 125 MB | 35.9 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.16 | 3,551 | 3,561 | 3,548 | 0.1% | 386 MB | 111.4 KB |  |
| feddi-gateway | 2026-11-03-0517 | 3,469 | 3,488 | 3,459 | 0.3% | 2,293 MB | 676.9 KB |  |
| caliban | 3.2.1 | 1,436 | 1,442 | 1,436 | 0.2% | 6,069 MB | 4,327.5 KB |  |
| cosmo | 0.372.0 | 1,422 | 1,423 | 1,419 | 0.1% | 150 MB | 107.8 KB |  |
| grafbase | 0.53.5 | 1,422 | 1,424 | 1,418 | 0.2% | 100 MB | 72.0 KB |  |
| hive-gateway-router-runtime | 2.15.8 | 582 | 583 | 582 | 0.1% | 2,616 MB | 4,603.4 KB |  |
| apollo-router | v2.19.1 | 485 | 486 | 485 | 0.1% | 179 MB | 378.7 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 416 | 417 | 416 | 0.1% | 208 MB | 512.3 KB |  |
| hive-gateway | 2.15.8 | 283 | 284 | 281 | 0.5% | 3,229 MB | 11,682.2 KB |  |
| apollo-gateway | 2.14.4 | 265 | 265 | 264 | 0.2% | 2,154 MB | 8,321.8 KB |  |
| hive-router | — | — | — | — | — | — | — | benchmark run failed |


### Details

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1300215     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 521 MB  4.3 MB/s
     http_req_blocked...............: avg=2.74µs  min=782ns   med=1.93µs  max=6.9ms    p(90)=3.16µs  p(95)=3.9µs    p(99.9)=28.61µs
     http_req_connecting............: avg=455ns   min=0s      med=0s      max=6.86ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.64ms min=8.26ms  med=13.22ms max=283.32ms p(90)=16.68ms p(95)=17.94ms  p(99.9)=25.68ms
       { expected_response:true }...: avg=13.64ms min=8.26ms  med=13.22ms max=283.32ms p(90)=16.68ms p(95)=17.94ms  p(99.9)=25.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 433505
     http_req_receiving.............: avg=68.6µs  min=23.65µs med=43.49µs max=103.65ms p(90)=92.1µs  p(95)=176.42µs p(99.9)=1.66ms 
     http_req_sending...............: avg=33.31µs min=4.44µs  med=8.11µs  max=131.42ms p(90)=16.65µs p(95)=96.69µs  p(99.9)=1.94ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.53ms min=8.2ms   med=13.12ms max=270.71ms p(90)=16.57ms p(95)=17.81ms  p(99.9)=25.39ms
     http_reqs......................: 433505  3584.072006/s
     iteration_duration.............: avg=13.83ms min=8.44ms  med=13.41ms max=293.47ms p(90)=16.88ms p(95)=18.13ms  p(99.9)=25.91ms
     iterations.....................: 433405  3583.24524/s
     success_rate...................: 100.00% ✓ 433405      ✗ 0     
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

     checks.........................: 100.00% ✓ 1297815     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 520 MB  4.3 MB/s
     http_req_blocked...............: avg=2.88µs  min=892ns   med=2.33µs  max=3.94ms   p(90)=3.66µs  p(95)=4.37µs   p(99.9)=29.58µs
     http_req_connecting............: avg=203ns   min=0s      med=0s      max=3.9ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.66ms min=8.27ms  med=13.2ms  max=291.65ms p(90)=16.81ms p(95)=18.14ms  p(99.9)=26.08ms
       { expected_response:true }...: avg=13.66ms min=8.27ms  med=13.2ms  max=291.65ms p(90)=16.81ms p(95)=18.14ms  p(99.9)=26.08ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 432705
     http_req_receiving.............: avg=86.19µs min=23.82µs med=45.96µs max=259.32ms p(90)=96.24µs p(95)=191.21µs p(99.9)=1.85ms 
     http_req_sending...............: avg=33.77µs min=4.49µs  med=8.81µs  max=109.69ms p(90)=17.71µs p(95)=103.76µs p(99.9)=1.88ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.54ms min=8.22ms  med=13.1ms  max=134.72ms p(90)=16.69ms p(95)=18ms     p(99.9)=25.76ms
     http_reqs......................: 432705  3577.255699/s
     iteration_duration.............: avg=13.86ms min=8.41ms  med=13.4ms  max=309.06ms p(90)=17.01ms p(95)=18.33ms  p(99.9)=26.32ms
     iterations.....................: 432605  3576.42898/s
     success_rate...................: 100.00% ✓ 432605      ✗ 0     
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

     checks.........................: 100.00% ✓ 1293681     ✗ 0     
     data_received..................: 38 GB   312 MB/s
     data_sent......................: 518 MB  4.3 MB/s
     http_req_blocked...............: avg=2.69µs  min=781ns   med=1.89µs  max=7.34ms   p(90)=3.06µs  p(95)=3.76µs   p(99.9)=24.73µs
     http_req_connecting............: avg=441ns   min=0s      med=0s      max=7.21ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.71ms min=8.11ms  med=13.29ms max=281.78ms p(90)=16.87ms p(95)=18.14ms  p(99.9)=25.51ms
       { expected_response:true }...: avg=13.71ms min=8.11ms  med=13.29ms max=281.78ms p(90)=16.87ms p(95)=18.14ms  p(99.9)=25.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 431327
     http_req_receiving.............: avg=68.62µs min=24.63µs med=43.98µs max=112.2ms  p(90)=90.91µs p(95)=170.05µs p(99.9)=1.72ms 
     http_req_sending...............: avg=31.22µs min=4.33µs  med=8µs     max=136.22ms p(90)=15.78µs p(95)=93.94µs  p(99.9)=1.72ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.61ms min=8.03ms  med=13.2ms  max=280.29ms p(90)=16.76ms p(95)=18.02ms  p(99.9)=25.32ms
     http_reqs......................: 431327  3565.506047/s
     iteration_duration.............: avg=13.9ms  min=8.28ms  med=13.48ms max=292.3ms  p(90)=17.06ms p(95)=18.33ms  p(99.9)=25.73ms
     iterations.....................: 431227  3564.67941/s
     success_rate...................: 100.00% ✓ 431227      ✗ 0     
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

     checks.........................: 100.00% ✓ 1293159     ✗ 0     
     data_received..................: 38 GB   312 MB/s
     data_sent......................: 518 MB  4.3 MB/s
     http_req_blocked...............: avg=3.02µs  min=871ns  med=2.31µs  max=6.37ms   p(90)=3.59µs  p(95)=4.25µs   p(99.9)=29.82µs
     http_req_connecting............: avg=338ns   min=0s     med=0s      max=6.18ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.71ms min=8.07ms med=13.25ms max=272.26ms p(90)=17ms    p(95)=18.36ms  p(99.9)=25.88ms
       { expected_response:true }...: avg=13.71ms min=8.07ms med=13.25ms max=272.26ms p(90)=17ms    p(95)=18.36ms  p(99.9)=25.88ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 431153
     http_req_receiving.............: avg=73.65µs min=24.7µs med=46.91µs max=126.42ms p(90)=94.38µs p(95)=188.36µs p(99.9)=1.95ms 
     http_req_sending...............: avg=35.1µs  min=4.57µs med=8.67µs  max=235.59ms p(90)=16.3µs  p(95)=100.86µs p(99.9)=1.93ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.6ms  min=8.02ms med=13.14ms max=271.72ms p(90)=16.88ms p(95)=18.23ms  p(99.9)=25.66ms
     http_reqs......................: 431153  3564.7771/s
     iteration_duration.............: avg=13.91ms min=8.18ms med=13.44ms max=282.34ms p(90)=17.2ms  p(95)=18.56ms  p(99.9)=26.11ms
     iterations.....................: 431053  3563.950299/s
     success_rate...................: 100.00% ✓ 431053      ✗ 0     
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

     checks.........................: 100.00% ✓ 1292256     ✗ 0     
     data_received..................: 38 GB   312 MB/s
     data_sent......................: 518 MB  4.3 MB/s
     http_req_blocked...............: avg=2.79µs  min=841ns   med=2.22µs  max=4.16ms   p(90)=3.56µs  p(95)=4.3µs    p(99.9)=28.14µs
     http_req_connecting............: avg=220ns   min=0s      med=0s      max=4.12ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.71ms min=8.19ms  med=13.27ms max=286.98ms p(90)=16.97ms p(95)=18.3ms   p(99.9)=25.8ms 
       { expected_response:true }...: avg=13.71ms min=8.19ms  med=13.27ms max=286.98ms p(90)=16.97ms p(95)=18.3ms   p(99.9)=25.8ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 430852
     http_req_receiving.............: avg=73.24µs min=24.24µs med=45.84µs max=178.8ms  p(90)=94.92µs p(95)=187.78µs p(99.9)=2.04ms 
     http_req_sending...............: avg=33.59µs min=4.55µs  med=8.5µs   max=175.53ms p(90)=16.86µs p(95)=101.19µs p(99.9)=1.9ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.61ms min=8.12ms  med=13.17ms max=286.32ms p(90)=16.85ms p(95)=18.17ms  p(99.9)=25.56ms
     http_reqs......................: 430852  3562.263817/s
     iteration_duration.............: avg=13.92ms min=8.33ms  med=13.47ms max=295.74ms p(90)=17.17ms p(95)=18.5ms   p(99.9)=26.02ms
     iterations.....................: 430752  3561.437022/s
     success_rate...................: 100.00% ✓ 430752      ✗ 0     
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

     checks.........................: 100.00% ✓ 1289457     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.5µs   min=811ns   med=1.9µs   max=3.72ms   p(90)=3.2µs   p(95)=3.95µs   p(99.9)=26.46µs
     http_req_connecting............: avg=222ns   min=0s      med=0s      max=3.68ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.75ms min=8.16ms  med=13.36ms max=273.23ms p(90)=16.8ms  p(95)=18.02ms  p(99.9)=25.03ms
       { expected_response:true }...: avg=13.75ms min=8.16ms  med=13.36ms max=273.23ms p(90)=16.8ms  p(95)=18.02ms  p(99.9)=25.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429919
     http_req_receiving.............: avg=67.54µs min=23.47µs med=43.11µs max=71.5ms   p(90)=90.86µs p(95)=172.31µs p(99.9)=1.6ms  
     http_req_sending...............: avg=32.84µs min=4.27µs  med=7.98µs  max=231.47ms p(90)=16.35µs p(95)=95.39µs  p(99.9)=1.71ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.65ms min=8.08ms  med=13.26ms max=262.56ms p(90)=16.69ms p(95)=17.91ms  p(99.9)=24.82ms
     http_reqs......................: 429919  3554.341184/s
     iteration_duration.............: avg=13.95ms min=8.3ms   med=13.55ms max=281.91ms p(90)=16.98ms p(95)=18.21ms  p(99.9)=25.24ms
     iterations.....................: 429819  3553.514438/s
     success_rate...................: 100.00% ✓ 429819      ✗ 0     
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

     checks.........................: 100.00% ✓ 1288617     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 516 MB  4.3 MB/s
     http_req_blocked...............: avg=2.37µs  min=811ns   med=1.85µs  max=3.54ms   p(90)=3µs     p(95)=3.63µs   p(99.9)=24.78µs
     http_req_connecting............: avg=201ns   min=0s      med=0s      max=3.51ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.77ms min=8.17ms  med=13.36ms max=276.35ms p(90)=16.84ms p(95)=18.08ms  p(99.9)=25.12ms
       { expected_response:true }...: avg=13.77ms min=8.17ms  med=13.36ms max=276.35ms p(90)=16.84ms p(95)=18.08ms  p(99.9)=25.12ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429639
     http_req_receiving.............: avg=67.75µs min=23.58µs med=43.63µs max=107.85ms p(90)=89.49µs p(95)=170.41µs p(99.9)=1.56ms 
     http_req_sending...............: avg=31.23µs min=3.98µs  med=7.9µs   max=160.74ms p(90)=15.3µs  p(95)=93.97µs  p(99.9)=1.6ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.67ms min=8.11ms  med=13.27ms max=275.76ms p(90)=16.73ms p(95)=17.96ms  p(99.9)=24.87ms
     http_reqs......................: 429639  3552.142003/s
     iteration_duration.............: avg=13.96ms min=8.32ms  med=13.55ms max=292.3ms  p(90)=17.03ms p(95)=18.27ms  p(99.9)=25.34ms
     iterations.....................: 429539  3551.315229/s
     success_rate...................: 100.00% ✓ 429539      ✗ 0     
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

     checks.........................: 100.00% ✓ 1288362     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 516 MB  4.3 MB/s
     http_req_blocked...............: avg=2.45µs  min=801ns   med=1.86µs  max=3.96ms   p(90)=3.04µs  p(95)=3.76µs   p(99.9)=24.4µs 
     http_req_connecting............: avg=230ns   min=0s      med=0s      max=3.92ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.76ms min=8.06ms  med=13.36ms max=276.31ms p(90)=16.93ms p(95)=18.2ms   p(99.9)=25.78ms
       { expected_response:true }...: avg=13.76ms min=8.06ms  med=13.36ms max=276.31ms p(90)=16.93ms p(95)=18.2ms   p(99.9)=25.78ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429554
     http_req_receiving.............: avg=70.4µs  min=24.81µs med=44.91µs max=157.37ms p(90)=91.57µs p(95)=173.56µs p(99.9)=1.8ms  
     http_req_sending...............: avg=32.28µs min=4.15µs  med=8.03µs  max=171.5ms  p(90)=16.14µs p(95)=93.84µs  p(99.9)=1.82ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.66ms min=7.99ms  med=13.26ms max=269.1ms  p(90)=16.82ms p(95)=18.07ms  p(99.9)=25.57ms
     http_reqs......................: 429554  3551.558197/s
     iteration_duration.............: avg=13.96ms min=8.23ms  med=13.55ms max=294.89ms p(90)=17.12ms p(95)=18.39ms  p(99.9)=25.99ms
     iterations.....................: 429454  3550.731396/s
     success_rate...................: 100.00% ✓ 429454      ✗ 0     
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

     checks.........................: 100.00% ✓ 1258704     ✗ 0     
     data_received..................: 37 GB   303 MB/s
     data_sent......................: 504 MB  4.2 MB/s
     http_req_blocked...............: avg=2.83µs  min=811ns   med=1.85µs  max=9.25ms   p(90)=2.92µs  p(95)=3.53µs   p(99.9)=25.27µs
     http_req_connecting............: avg=666ns   min=0s      med=0s      max=9.21ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.1ms  min=8.66ms  med=13.76ms max=290.86ms p(90)=17ms    p(95)=18.14ms  p(99.9)=25.36ms
       { expected_response:true }...: avg=14.1ms  min=8.66ms  med=13.76ms max=290.86ms p(90)=17ms    p(95)=18.14ms  p(99.9)=25.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 419668
     http_req_receiving.............: avg=64.19µs min=23.87µs med=43.45µs max=58.6ms   p(90)=83.08µs p(95)=151.46µs p(99.9)=1.35ms 
     http_req_sending...............: avg=29.68µs min=4.16µs  med=7.86µs  max=214.14ms p(90)=14.59µs p(95)=89.2µs   p(99.9)=1.47ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.01ms min=8.6ms   med=13.67ms max=290.19ms p(90)=16.9ms  p(95)=18.04ms  p(99.9)=25.18ms
     http_reqs......................: 419668  3469.885804/s
     iteration_duration.............: avg=14.29ms min=8.79ms  med=13.95ms max=305.85ms p(90)=17.18ms p(95)=18.32ms  p(99.9)=25.6ms 
     iterations.....................: 419568  3469.058987/s
     success_rate...................: 100.00% ✓ 419568      ✗ 0     
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

     checks.........................: 100.00% ✓ 525186      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 211 MB  1.7 MB/s
     http_req_blocked...............: avg=4.37µs  min=972ns   med=2.39µs  max=9.87ms   p(90)=4.14µs  p(95)=4.88µs   p(99.9)=26.41µs 
     http_req_connecting............: avg=1.6µs   min=0s      med=0s      max=9.81ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.04ms min=17.98ms med=33.55ms max=297.33ms p(90)=39.95ms p(95)=42.12ms  p(99.9)=54.02ms 
       { expected_response:true }...: avg=34.04ms min=17.98ms med=33.55ms max=297.33ms p(90)=39.95ms p(95)=42.12ms  p(99.9)=54.02ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 175162
     http_req_receiving.............: avg=70.96µs min=24.52µs med=57.76µs max=180.06ms p(90)=94.16µs p(95)=110.91µs p(99.9)=786.03µs
     http_req_sending...............: avg=21.13µs min=4.98µs  med=10.87µs max=95.75ms  p(90)=17.49µs p(95)=21.34µs  p(99.9)=748.18µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.95ms min=17.88ms med=33.46ms max=295.75ms p(90)=39.86ms p(95)=42.03ms  p(99.9)=53.86ms 
     http_reqs......................: 175162  1436.126224/s
     iteration_duration.............: avg=34.26ms min=20.91ms med=33.76ms max=310.16ms p(90)=40.16ms p(95)=42.32ms  p(99.9)=54.32ms 
     iterations.....................: 175062  1435.306339/s
     success_rate...................: 100.00% ✓ 175062      ✗ 0     
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

     checks.........................: 100.00% ✓ 520095      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 208 MB  1.7 MB/s
     http_req_blocked...............: avg=2.9µs   min=962ns   med=2.18µs  max=3.18ms   p(90)=3.75µs  p(95)=4.44µs   p(99.9)=31.21µs 
     http_req_connecting............: avg=373ns   min=0s      med=0s      max=3.15ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.39ms min=17.86ms med=33.82ms max=307.61ms p(90)=41.01ms p(95)=43.37ms  p(99.9)=55.74ms 
       { expected_response:true }...: avg=34.39ms min=17.86ms med=33.82ms max=307.61ms p(90)=41.01ms p(95)=43.37ms  p(99.9)=55.74ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 173465
     http_req_receiving.............: avg=70.21µs min=24.71µs med=57.12µs max=130.24ms p(90)=95.5µs  p(95)=113.57µs p(99.9)=762.06µs
     http_req_sending...............: avg=22.48µs min=4.51µs  med=9.9µs   max=114.19ms p(90)=16.52µs p(95)=20.55µs  p(99.9)=749.81µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.3ms  min=17.76ms med=33.73ms max=307.51ms p(90)=40.92ms p(95)=43.27ms  p(99.9)=55.33ms 
     http_reqs......................: 173465  1422.392207/s
     iteration_duration.............: avg=34.6ms  min=20.68ms med=34.01ms max=317.89ms p(90)=41.21ms p(95)=43.55ms  p(99.9)=56.19ms 
     iterations.....................: 173365  1421.572219/s
     success_rate...................: 100.00% ✓ 173365      ✗ 0     
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

     checks.........................: 100.00% ✓ 520002      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 208 MB  1.7 MB/s
     http_req_blocked...............: avg=3.83µs  min=932ns   med=2.85µs  max=3.54ms   p(90)=5.05µs   p(95)=6µs      p(99.9)=42.74µs
     http_req_connecting............: avg=513ns   min=0s      med=0s      max=3.5ms    p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.34ms min=17.61ms med=34.08ms max=304.81ms p(90)=40.22ms  p(95)=41.93ms  p(99.9)=50.34ms
       { expected_response:true }...: avg=34.34ms min=17.61ms med=34.08ms max=304.81ms p(90)=40.22ms  p(95)=41.93ms  p(99.9)=50.34ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 173434
     http_req_receiving.............: avg=83.4µs  min=26.47µs med=58.74µs max=121.86ms p(90)=121.01µs p(95)=166.82µs p(99.9)=1.4ms  
     http_req_sending...............: avg=33.55µs min=4.37µs  med=10.62µs max=182.64ms p(90)=23.02µs  p(95)=47.21µs  p(99.9)=1.41ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.22ms min=17.46ms med=33.97ms max=304.15ms p(90)=40.11ms  p(95)=41.82ms  p(99.9)=50.06ms
     http_reqs......................: 173434  1422.444376/s
     iteration_duration.............: avg=34.6ms  min=20.71ms med=34.33ms max=328.54ms p(90)=40.45ms  p(95)=42.16ms  p(99.9)=50.64ms
     iterations.....................: 173334  1421.624212/s
     success_rate...................: 100.00% ✓ 173334      ✗ 0     
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

     checks.........................: 100.00% ✓ 213183     ✗ 0    
     data_received..................: 6.2 GB  51 MB/s
     data_sent......................: 86 MB   700 kB/s
     http_req_blocked...............: avg=7.75µs  min=1.16µs  med=3.21µs  max=10.01ms  p(90)=4.75µs   p(95)=5.41µs   p(99.9)=45.81µs 
     http_req_connecting............: avg=4µs     min=0s      med=0s      max=9.96ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=84.11ms min=20.29ms med=82.2ms  max=350.02ms p(90)=97.55ms  p(95)=106.08ms p(99.9)=212.73ms
       { expected_response:true }...: avg=84.11ms min=20.29ms med=82.2ms  max=350.02ms p(90)=97.55ms  p(95)=106.08ms p(99.9)=212.73ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 71161
     http_req_receiving.............: avg=80µs    min=31.34µs med=73.14µs max=49.98ms  p(90)=106.44µs p(95)=118.51µs p(99.9)=568.03µs
     http_req_sending...............: avg=23.58µs min=4.92µs  med=14.42µs max=87.69ms  p(90)=20.3µs   p(95)=22.44µs  p(99.9)=640.71µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=84ms    min=20.15ms med=82.11ms max=348.27ms p(90)=97.46ms  p(95)=105.92ms p(99.9)=212.65ms
     http_reqs......................: 71161   582.376308/s
     iteration_duration.............: avg=84.44ms min=30.51ms med=82.45ms max=359.15ms p(90)=97.79ms  p(95)=106.38ms p(99.9)=214.85ms
     iterations.....................: 71061   581.557915/s
     success_rate...................: 100.00% ✓ 71061      ✗ 0    
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

     checks.........................: 100.00% ✓ 177756     ✗ 0    
     data_received..................: 5.2 GB  43 MB/s
     data_sent......................: 71 MB   583 kB/s
     http_req_blocked...............: avg=4.38µs   min=1.08µs  med=2.62µs  max=3.99ms   p(90)=4.09µs   p(95)=4.63µs   p(99.9)=58.5µs  
     http_req_connecting............: avg=1.51µs   min=0s      med=0s      max=3.95ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=100.9ms  min=19.91ms med=98.92ms max=329ms    p(90)=128.4ms  p(95)=137.59ms p(99.9)=177.5ms 
       { expected_response:true }...: avg=100.9ms  min=19.91ms med=98.92ms max=329ms    p(90)=128.4ms  p(95)=137.59ms p(99.9)=177.5ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 59352
     http_req_receiving.............: avg=75.57µs  min=28.01µs med=70.06µs max=35.91ms  p(90)=102.43µs p(95)=114.54µs p(99.9)=492.99µs
     http_req_sending...............: avg=20.61µs  min=5.07µs  med=13.4µs  max=76.09ms  p(90)=19.33µs  p(95)=21.25µs  p(99.9)=506.03µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=100.8ms  min=19.78ms med=98.83ms max=328.47ms p(90)=128.31ms p(95)=137.49ms p(99.9)=177.27ms
     http_reqs......................: 59352   485.628427/s
     iteration_duration.............: avg=101.28ms min=31.93ms med=99.18ms max=348.7ms  p(90)=128.66ms p(95)=137.84ms p(99.9)=179.49ms
     iterations.....................: 59252   484.810209/s
     success_rate...................: 100.00% ✓ 59252      ✗ 0    
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

     checks.........................: 100.00% ✓ 152559     ✗ 0    
     data_received..................: 4.5 GB  36 MB/s
     data_sent......................: 61 MB   500 kB/s
     http_req_blocked...............: avg=4.64µs   min=1.04µs  med=3.08µs   max=3.02ms   p(90)=4.5µs    p(95)=5.06µs   p(99.9)=98.75µs 
     http_req_connecting............: avg=1.38µs   min=0s      med=0s       max=2.99ms   p(90)=0s       p(95)=0s       p(99.9)=2.92µs  
     http_req_duration..............: avg=117.56ms min=20.97ms med=115.93ms max=329.82ms p(90)=145.28ms p(95)=154.8ms  p(99.9)=199.84ms
       { expected_response:true }...: avg=117.56ms min=20.97ms med=115.93ms max=329.82ms p(90)=145.28ms p(95)=154.8ms  p(99.9)=199.84ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 50953
     http_req_receiving.............: avg=86.68µs  min=27.64µs med=78.74µs  max=129.42ms p(90)=108.26µs p(95)=119.98µs p(99.9)=514.84µs
     http_req_sending...............: avg=21.11µs  min=4.81µs  med=15.28µs  max=75.63ms  p(90)=20.14µs  p(95)=22.04µs  p(99.9)=485.72µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=117.45ms min=20.84ms med=115.83ms max=329.3ms  p(90)=145.18ms p(95)=154.66ms p(99.9)=198.91ms
     http_reqs......................: 50953   416.544326/s
     iteration_duration.............: avg=118.01ms min=29.67ms med=116.21ms max=347.36ms p(90)=145.55ms p(95)=155.05ms p(99.9)=203.84ms
     iterations.....................: 50853   415.726819/s
     success_rate...................: 100.00% ✓ 50853      ✗ 0    
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

     checks.........................: 100.00% ✓ 103611     ✗ 0    
     data_received..................: 3.0 GB  25 MB/s
     data_sent......................: 42 MB   341 kB/s
     http_req_blocked...............: avg=10.77µs  min=1.14µs  med=3.08µs   max=9.54ms   p(90)=4.45µs   p(95)=5µs      p(99.9)=3.85ms  
     http_req_connecting............: avg=7.18µs   min=0s      med=0s       max=9.38ms   p(90)=0s       p(95)=0s       p(99.9)=3.58ms  
     http_req_duration..............: avg=173.08ms min=17.32ms med=159.45ms max=753.66ms p(90)=197.21ms p(95)=213.65ms p(99.9)=699.44ms
       { expected_response:true }...: avg=173.08ms min=17.32ms med=159.45ms max=753.66ms p(90)=197.21ms p(95)=213.65ms p(99.9)=699.44ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 34637
     http_req_receiving.............: avg=90.31µs  min=30.25µs med=84.63µs  max=88.43ms  p(90)=114.41µs p(95)=125.27µs p(99.9)=610.13µs
     http_req_sending...............: avg=38.2µs   min=5.16µs  med=16.07µs  max=142.77ms p(90)=20.39µs  p(95)=22.21µs  p(99.9)=722.62µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=172.95ms min=17.19ms med=159.33ms max=753.55ms p(90)=197.07ms p(95)=213.46ms p(99.9)=699.31ms
     http_reqs......................: 34637   283.966261/s
     iteration_duration.............: avg=173.8ms  min=48.22ms med=159.76ms max=753.91ms p(90)=197.54ms p(95)=214ms    p(99.9)=699.72ms
     iterations.....................: 34537   283.146426/s
     success_rate...................: 100.00% ✓ 34537      ✗ 0    
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

     checks.........................: 100.00% ✓ 97404      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   319 kB/s
     http_req_blocked...............: avg=11.11µs  min=1.13µs  med=3.01µs   max=8.41ms   p(90)=4.34µs   p(95)=4.86µs   p(99.9)=4.54ms  
     http_req_connecting............: avg=7.69µs   min=0s      med=0s       max=8.26ms   p(90)=0s       p(95)=0s       p(99.9)=4.41ms  
     http_req_duration..............: avg=184.12ms min=22.74ms med=186.77ms max=380.41ms p(90)=197.4ms  p(95)=201.87ms p(99.9)=267.74ms
       { expected_response:true }...: avg=184.12ms min=22.74ms med=186.77ms max=380.41ms p(90)=197.4ms  p(95)=201.87ms p(99.9)=267.74ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32568
     http_req_receiving.............: avg=92.92µs  min=32.82µs med=84.43µs  max=81.46ms  p(90)=112.98µs p(95)=123.33µs p(99.9)=488.13µs
     http_req_sending...............: avg=25.04µs  min=5.37µs  med=16.09µs  max=69.03ms  p(90)=20.42µs  p(95)=22.33µs  p(99.9)=647.1µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184ms    min=22.64ms med=186.66ms max=380.04ms p(90)=197.28ms p(95)=201.76ms p(99.9)=267.59ms
     http_reqs......................: 32568   265.664041/s
     iteration_duration.............: avg=184.9ms  min=41.44ms med=187.04ms max=394.33ms p(90)=197.66ms p(95)=202.18ms p(99.9)=268.99ms
     iterations.....................: 32468   264.84832/s
     success_rate...................: 100.00% ✓ 32468      ✗ 0    
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

