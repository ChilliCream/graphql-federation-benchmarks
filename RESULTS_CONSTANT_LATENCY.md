## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-aot-11 | 16.7.7 | 3,613 | 3,631 | 3,607 | 0.3% | 114 MB | 32.3 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.20 | 3,609 | 3,627 | 3,590 | 0.5% | 367 MB | 104.0 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.20 | 3,604 | 3,608 | 3,586 | 0.3% | 119 MB | 33.8 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.20 | 3,596 | 3,619 | 3,586 | 0.4% | 112 MB | 31.9 KB |  |
| fusion-net-11 | 16.7.7 | 3,589 | 3,601 | 3,587 | 0.2% | 359 MB | 102.4 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 3,558 | 3,569 | 3,548 | 0.2% | 108 MB | 31.1 KB |  |
| fusion-fed-net-11 | 16.7.7 | 3,555 | 3,577 | 3,548 | 0.3% | 365 MB | 105.1 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.20 | 3,550 | 3,557 | 3,539 | 0.2% | 363 MB | 104.7 KB |  |
| feddi-gateway | 2026-11-03-0517 | 3,478 | 3,518 | 3,457 | 0.7% | 2,288 MB | 673.6 KB |  |
| hive-router-nightly | v0.3.19-nightly.e7e70652 | 3,357 | 3,368 | 3,351 | 0.2% | 89 MB | 27.0 KB |  |
| hive-router | v0.3.17 | 3,334 | 3,349 | 3,333 | 0.2% | 90 MB | 27.6 KB |  |
| grafbase | 0.53.5 | 1,455 | 1,459 | 1,453 | 0.2% | 102 MB | 71.6 KB |  |
| caliban | 3.2.1 | 1,428 | 1,432 | 1,424 | 0.2% | 5,800 MB | 4,159.0 KB |  |
| cosmo | 0.373.0 | 1,423 | 1,424 | 1,422 | 0.1% | 147 MB | 106.0 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 594 | 594 | 593 | 0.1% | 2,612 MB | 4,503.1 KB |  |
| apollo-router | v2.19.1 | 527 | 531 | 516 | 1.3% | 175 MB | 340.6 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.fbceee06 | 520 | 520 | 519 | 0.1% | 199 MB | 391.1 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 388 | 389 | 387 | 0.2% | 201 MB | 531.2 KB |  |
| hive-gateway | 2.15.10 | 293 | 293 | 292 | 0.2% | 3,307 MB | 11,557.8 KB |  |
| apollo-gateway | 2.14.4 | 264 | 265 | 264 | 0.2% | 2,150 MB | 8,338.5 KB |  |


### Details

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1310907     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 525 MB  4.3 MB/s
     http_req_blocked...............: avg=2.78µs  min=801ns   med=1.94µs  max=7.95ms   p(90)=3.12µs  p(95)=3.81µs   p(99.9)=25.72µs
     http_req_connecting............: avg=500ns   min=0s      med=0s      max=7.91ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.53ms min=8.03ms  med=13.1ms  max=268.1ms  p(90)=16.57ms p(95)=17.84ms  p(99.9)=25.5ms 
       { expected_response:true }...: avg=13.53ms min=8.03ms  med=13.1ms  max=268.1ms  p(90)=16.57ms p(95)=17.84ms  p(99.9)=25.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 437069
     http_req_receiving.............: avg=69.55µs min=23.56µs med=44.44µs max=160.34ms p(90)=91.16µs p(95)=174.37µs p(99.9)=1.67ms 
     http_req_sending...............: avg=31.75µs min=4.21µs  med=8.21µs  max=154.73ms p(90)=15.74µs p(95)=93.99µs  p(99.9)=1.81ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.42ms min=7.98ms  med=13ms    max=266.02ms p(90)=16.46ms p(95)=17.7ms   p(99.9)=25.31ms
     http_reqs......................: 437069  3613.558536/s
     iteration_duration.............: avg=13.72ms min=8.15ms  med=13.29ms max=297.51ms p(90)=16.76ms p(95)=18.03ms  p(99.9)=25.73ms
     iterations.....................: 436969  3612.731765/s
     success_rate...................: 100.00% ✓ 436969      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.20)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1309284     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 525 MB  4.3 MB/s
     http_req_blocked...............: avg=3.22µs  min=861ns   med=2.18µs  max=9.65ms   p(90)=3.47µs  p(95)=4.21µs   p(99.9)=31.6µs 
     http_req_connecting............: avg=671ns   min=0s      med=0s      max=9.61ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.54ms min=8.12ms  med=13.1ms  max=285.12ms p(90)=16.72ms p(95)=18.02ms  p(99.9)=25.67ms
       { expected_response:true }...: avg=13.54ms min=8.12ms  med=13.1ms  max=285.12ms p(90)=16.72ms p(95)=18.02ms  p(99.9)=25.67ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 436528
     http_req_receiving.............: avg=71.67µs min=24.08µs med=45.36µs max=117.29ms p(90)=93.78µs p(95)=180.09µs p(99.9)=1.9ms  
     http_req_sending...............: avg=33.69µs min=4.16µs  med=8.22µs  max=226.99ms p(90)=16.6µs  p(95)=98.2µs   p(99.9)=1.97ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.43ms min=8.04ms  med=13ms    max=283.42ms p(90)=16.6ms  p(95)=17.89ms  p(99.9)=25.44ms
     http_reqs......................: 436528  3609.193411/s
     iteration_duration.............: avg=13.73ms min=8.27ms  med=13.3ms  max=298.29ms p(90)=16.91ms p(95)=18.21ms  p(99.9)=25.89ms
     iterations.....................: 436428  3608.366616/s
     success_rate...................: 100.00% ✓ 436428      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.20)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1307808     ✗ 0     
     data_received..................: 38 GB   315 MB/s
     data_sent......................: 524 MB  4.3 MB/s
     http_req_blocked...............: avg=2.85µs  min=831ns   med=2.29µs  max=4.05ms   p(90)=3.58µs  p(95)=4.27µs   p(99.9)=31.77µs
     http_req_connecting............: avg=221ns   min=0s      med=0s      max=4.01ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.55ms min=8.08ms  med=13.1ms  max=280.43ms p(90)=16.68ms p(95)=17.99ms  p(99.9)=25.65ms
       { expected_response:true }...: avg=13.55ms min=8.08ms  med=13.1ms  max=280.43ms p(90)=16.68ms p(95)=17.99ms  p(99.9)=25.65ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 436036
     http_req_receiving.............: avg=73.37µs min=24.25µs med=45.69µs max=81.44ms  p(90)=95.67µs p(95)=190.36µs p(99.9)=1.96ms 
     http_req_sending...............: avg=33.97µs min=4.15µs  med=8.72µs  max=205.19ms p(90)=17.2µs  p(95)=101.26µs p(99.9)=1.95ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.44ms min=8.03ms  med=13ms    max=280.22ms p(90)=16.55ms p(95)=17.85ms  p(99.9)=25.41ms
     http_reqs......................: 436036  3604.929537/s
     iteration_duration.............: avg=13.75ms min=8.23ms  med=13.3ms  max=291.48ms p(90)=16.88ms p(95)=18.19ms  p(99.9)=25.87ms
     iterations.....................: 435936  3604.102787/s
     success_rate...................: 100.00% ✓ 435936      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.20)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1304793     ✗ 0     
     data_received..................: 38 GB   315 MB/s
     data_sent......................: 523 MB  4.3 MB/s
     http_req_blocked...............: avg=2.54µs  min=801ns   med=2.04µs  max=3.2ms    p(90)=3.29µs  p(95)=3.95µs   p(99.9)=25.96µs
     http_req_connecting............: avg=162ns   min=0s      med=0s      max=3.15ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.59ms min=8.09ms  med=13.18ms max=280.93ms p(90)=16.68ms p(95)=17.93ms  p(99.9)=25.25ms
       { expected_response:true }...: avg=13.59ms min=8.09ms  med=13.18ms max=280.93ms p(90)=16.68ms p(95)=17.93ms  p(99.9)=25.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 435031
     http_req_receiving.............: avg=67.27µs min=23.27µs med=42.64µs max=130.11ms p(90)=89.2µs  p(95)=172.46µs p(99.9)=1.59ms 
     http_req_sending...............: avg=31.8µs  min=4.32µs  med=8.26µs  max=203.77ms p(90)=16µs    p(95)=96.29µs  p(99.9)=1.68ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.49ms min=8.02ms  med=13.08ms max=280.3ms  p(90)=16.57ms p(95)=17.8ms   p(99.9)=25.05ms
     http_reqs......................: 435031  3596.65556/s
     iteration_duration.............: avg=13.78ms min=8.26ms  med=13.36ms max=290.19ms p(90)=16.87ms p(95)=18.12ms  p(99.9)=25.47ms
     iterations.....................: 434931  3595.828802/s
     success_rate...................: 100.00% ✓ 434931      ✗ 0     
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

     checks.........................: 100.00% ✓ 1302324     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 522 MB  4.3 MB/s
     http_req_blocked...............: avg=2.34µs  min=771ns   med=1.81µs  max=4.01ms   p(90)=2.91µs  p(95)=3.55µs   p(99.9)=25.12µs
     http_req_connecting............: avg=213ns   min=0s      med=0s      max=3.97ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.62ms min=8.11ms  med=13.22ms max=267.64ms p(90)=16.71ms p(95)=17.96ms  p(99.9)=25.19ms
       { expected_response:true }...: avg=13.62ms min=8.11ms  med=13.22ms max=267.64ms p(90)=16.71ms p(95)=17.96ms  p(99.9)=25.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 434208
     http_req_receiving.............: avg=67.83µs min=24.33µs med=44.34µs max=70.44ms  p(90)=89.7µs  p(95)=169.27µs p(99.9)=1.61ms 
     http_req_sending...............: avg=30.84µs min=4.04µs  med=7.74µs  max=126.52ms p(90)=15.05µs p(95)=91.45µs  p(99.9)=1.73ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.52ms min=8ms     med=13.12ms max=258.88ms p(90)=16.61ms p(95)=17.84ms  p(99.9)=25.02ms
     http_reqs......................: 434208  3589.860897/s
     iteration_duration.............: avg=13.81ms min=8.3ms   med=13.41ms max=284.03ms p(90)=16.9ms  p(95)=18.15ms  p(99.9)=25.39ms
     iterations.....................: 434108  3589.034136/s
     success_rate...................: 100.00% ✓ 434108      ✗ 0     
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

     checks.........................: 100.00% ✓ 1290924     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=3.18µs  min=882ns   med=2.31µs  max=8.42ms   p(90)=3.65µs  p(95)=4.38µs   p(99.9)=30.89µs
     http_req_connecting............: avg=512ns   min=0s      med=0s      max=8.38ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.73ms min=8.22ms  med=13.27ms max=266.94ms p(90)=16.96ms p(95)=18.32ms  p(99.9)=26.11ms
       { expected_response:true }...: avg=13.73ms min=8.22ms  med=13.27ms max=266.94ms p(90)=16.96ms p(95)=18.32ms  p(99.9)=26.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 430408
     http_req_receiving.............: avg=73.99µs min=23.88µs med=46.54µs max=62.7ms   p(90)=97.95µs p(95)=189.21µs p(99.9)=1.97ms 
     http_req_sending...............: avg=34.77µs min=4.33µs  med=8.73µs  max=130.48ms p(90)=17.51µs p(95)=102.75µs p(99.9)=1.89ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.62ms min=8.17ms  med=13.17ms max=266.76ms p(90)=16.84ms p(95)=18.19ms  p(99.9)=25.91ms
     http_reqs......................: 430408  3558.40245/s
     iteration_duration.............: avg=13.93ms min=8.34ms  med=13.47ms max=283.97ms p(90)=17.16ms p(95)=18.52ms  p(99.9)=26.32ms
     iterations.....................: 430308  3557.575699/s
     success_rate...................: 100.00% ✓ 430308      ✗ 0     
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

     checks.........................: 100.00% ✓ 1289709     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.46µs  min=752ns   med=1.84µs  max=3.61ms   p(90)=3.24µs  p(95)=4.14µs  p(99.9)=23.65µs
     http_req_connecting............: avg=238ns   min=0s      med=0s      max=3.59ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.75ms min=8.17ms  med=13.35ms max=282.86ms p(90)=16.88ms p(95)=18.13ms p(99.9)=25.52ms
       { expected_response:true }...: avg=13.75ms min=8.17ms  med=13.35ms max=282.86ms p(90)=16.88ms p(95)=18.13ms p(99.9)=25.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 430003
     http_req_receiving.............: avg=69.78µs min=23.44µs med=42.94µs max=158.31ms p(90)=94.63µs p(95)=173.8µs p(99.9)=1.9ms  
     http_req_sending...............: avg=30.88µs min=4.11µs  med=7.89µs  max=99.45ms  p(90)=18.01µs p(95)=93.54µs p(99.9)=1.78ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.65ms min=8.11ms  med=13.25ms max=272.59ms p(90)=16.77ms p(95)=18.01ms p(99.9)=25.26ms
     http_reqs......................: 430003  3555.214723/s
     iteration_duration.............: avg=13.94ms min=8.35ms  med=13.54ms max=297.21ms p(90)=17.07ms p(95)=18.32ms p(99.9)=25.75ms
     iterations.....................: 429903  3554.387935/s
     success_rate...................: 100.00% ✓ 429903      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.20)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1287993     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 516 MB  4.3 MB/s
     http_req_blocked...............: avg=2.8µs   min=922ns   med=2.24µs  max=4.19ms   p(90)=3.56µs  p(95)=4.29µs   p(99.9)=30.8µs 
     http_req_connecting............: avg=218ns   min=0s      med=0s      max=4.13ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.76ms min=8.22ms  med=13.33ms max=281.89ms p(90)=17.01ms p(95)=18.32ms  p(99.9)=26.24ms
       { expected_response:true }...: avg=13.76ms min=8.22ms  med=13.33ms max=281.89ms p(90)=17.01ms p(95)=18.32ms  p(99.9)=26.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429431
     http_req_receiving.............: avg=72.87µs min=24.68µs med=45.96µs max=110.49ms p(90)=95.31µs p(95)=185.14µs p(99.9)=1.99ms 
     http_req_sending...............: avg=33.83µs min=4.37µs  med=8.46µs  max=230.49ms p(90)=16.59µs p(95)=97.99µs  p(99.9)=1.93ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.66ms min=8.15ms  med=13.23ms max=281.26ms p(90)=16.89ms p(95)=18.18ms  p(99.9)=26.01ms
     http_reqs......................: 429431  3550.279197/s
     iteration_duration.............: avg=13.96ms min=8.39ms  med=13.53ms max=290.65ms p(90)=17.21ms p(95)=18.52ms  p(99.9)=26.46ms
     iterations.....................: 429331  3549.452456/s
     success_rate...................: 100.00% ✓ 429331      ✗ 0     
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

     checks.........................: 100.00% ✓ 1261884     ✗ 0     
     data_received..................: 37 GB   304 MB/s
     data_sent......................: 506 MB  4.2 MB/s
     http_req_blocked...............: avg=2.47µs  min=812ns   med=1.89µs  max=3.55ms   p(90)=3.17µs  p(95)=3.93µs   p(99.9)=26.89µs
     http_req_connecting............: avg=213ns   min=0s      med=0s      max=3.51ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.06ms min=8.42ms  med=13.72ms max=278.96ms p(90)=16.99ms p(95)=18.17ms  p(99.9)=25.5ms 
       { expected_response:true }...: avg=14.06ms min=8.42ms  med=13.72ms max=278.96ms p(90)=16.99ms p(95)=18.17ms  p(99.9)=25.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 420728
     http_req_receiving.............: avg=65.6µs  min=23.44µs med=41.58µs max=134ms    p(90)=87.12µs p(95)=164.17µs p(99.9)=1.65ms 
     http_req_sending...............: avg=31.04µs min=4.31µs  med=8.12µs  max=183.15ms p(90)=16.61µs p(95)=92.93µs  p(99.9)=1.71ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.96ms min=8.37ms  med=13.63ms max=278.13ms p(90)=16.88ms p(95)=18.05ms  p(99.9)=25.33ms
     http_reqs......................: 420728  3478.596165/s
     iteration_duration.............: avg=14.25ms min=8.55ms  med=13.91ms max=299.24ms p(90)=17.17ms p(95)=18.36ms  p(99.9)=25.72ms
     iterations.....................: 420628  3477.769361/s
     success_rate...................: 100.00% ✓ 420628      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.19-nightly.e7e70652)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1218141     ✗ 0     
     data_received..................: 36 GB   294 MB/s
     data_sent......................: 488 MB  4.0 MB/s
     http_req_blocked...............: avg=2.53µs  min=821ns   med=1.92µs  max=3.91ms   p(90)=3.32µs  p(95)=4.22µs  p(99.9)=25.3µs 
     http_req_connecting............: avg=242ns   min=0s      med=0s      max=3.87ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=14.57ms min=8.36ms  med=14.23ms max=287.66ms p(90)=17.69ms p(95)=18.92ms p(99.9)=26.92ms
       { expected_response:true }...: avg=14.57ms min=8.36ms  med=14.23ms max=287.66ms p(90)=17.69ms p(95)=18.92ms p(99.9)=26.92ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 406147
     http_req_receiving.............: avg=70.49µs min=23.88µs med=45.08µs max=93.9ms   p(90)=99.12µs p(95)=175.7µs p(99.9)=1.68ms 
     http_req_sending...............: avg=32.61µs min=4.35µs  med=8.15µs  max=261.27ms p(90)=18.41µs p(95)=95.12µs p(99.9)=1.72ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=14.46ms min=8.3ms   med=14.13ms max=287.44ms p(90)=17.58ms p(95)=18.8ms  p(99.9)=26.68ms
     http_reqs......................: 406147  3357.452768/s
     iteration_duration.............: avg=14.76ms min=8.56ms  med=14.42ms max=313.78ms p(90)=17.88ms p(95)=19.11ms p(99.9)=27.2ms 
     iterations.....................: 406047  3356.626108/s
     success_rate...................: 100.00% ✓ 406047      ✗ 0     
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

     checks.........................: 100.00% ✓ 1209861     ✗ 0     
     data_received..................: 35 GB   292 MB/s
     data_sent......................: 485 MB  4.0 MB/s
     http_req_blocked...............: avg=3µs     min=912ns   med=2.39µs  max=4ms      p(90)=3.97µs   p(95)=4.82µs   p(99.9)=32.69µs
     http_req_connecting............: avg=224ns   min=0s      med=0s      max=3.97ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.66ms min=8.58ms  med=14.28ms max=284.37ms p(90)=17.91ms  p(95)=19.21ms  p(99.9)=27.11ms
       { expected_response:true }...: avg=14.66ms min=8.58ms  med=14.28ms max=284.37ms p(90)=17.91ms  p(95)=19.21ms  p(99.9)=27.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 403387
     http_req_receiving.............: avg=74.61µs min=22.94µs med=46.39µs max=97.1ms   p(90)=103.93µs p(95)=193.04µs p(99.9)=1.8ms  
     http_req_sending...............: avg=34.12µs min=4.3µs   med=9.03µs  max=76.17ms  p(90)=19.07µs  p(95)=104.75µs p(99.9)=1.93ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.55ms min=8.51ms  med=14.18ms max=283.73ms p(90)=17.79ms  p(95)=19.08ms  p(99.9)=26.87ms
     http_reqs......................: 403387  3334.569563/s
     iteration_duration.............: avg=14.86ms min=8.74ms  med=14.48ms max=293.55ms p(90)=18.1ms   p(95)=19.41ms  p(99.9)=27.32ms
     iterations.....................: 403287  3333.74292/s
     success_rate...................: 100.00% ✓ 403287      ✗ 0     
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

     checks.........................: 100.00% ✓ 532284      ✗ 0     
     data_received..................: 16 GB   128 MB/s
     data_sent......................: 213 MB  1.7 MB/s
     http_req_blocked...............: avg=3.51µs  min=802ns   med=2.34µs  max=4.94ms   p(90)=4.62µs   p(95)=5.53µs   p(99.9)=37.02µs
     http_req_connecting............: avg=618ns   min=0s      med=0s      max=4.79ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.56ms min=17.81ms med=33.28ms max=300.5ms  p(90)=39.27ms  p(95)=40.95ms  p(99.9)=48.6ms 
       { expected_response:true }...: avg=33.56ms min=17.81ms med=33.28ms max=300.5ms  p(90)=39.27ms  p(95)=40.95ms  p(99.9)=48.6ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 177528
     http_req_receiving.............: avg=79.3µs  min=25.62µs med=55.06µs max=68.69ms  p(90)=118.31µs p(95)=158.94µs p(99.9)=1.26ms 
     http_req_sending...............: avg=30.48µs min=4.35µs  med=9.55µs  max=178.06ms p(90)=21.97µs  p(95)=37.14µs  p(99.9)=1.44ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.45ms min=17.67ms med=33.17ms max=300.37ms p(90)=39.17ms  p(95)=40.84ms  p(99.9)=48.31ms
     http_reqs......................: 177528  1455.931891/s
     iteration_duration.............: avg=33.81ms min=20.71ms med=33.51ms max=313.74ms p(90)=39.49ms  p(95)=41.16ms  p(99.9)=48.82ms
     iterations.....................: 177428  1455.111777/s
     success_rate...................: 100.00% ✓ 177428      ✗ 0     
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

     checks.........................: 100.00% ✓ 522432      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 209 MB  1.7 MB/s
     http_req_blocked...............: avg=3.81µs  min=1.13µs  med=3.02µs  max=3.46ms   p(90)=4.84µs  p(95)=5.65µs   p(99.9)=36.51µs 
     http_req_connecting............: avg=457ns   min=0s      med=0s      max=3.43ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.21ms min=17.8ms  med=33.71ms max=310.23ms p(90)=40.27ms p(95)=42.51ms  p(99.9)=55.39ms 
       { expected_response:true }...: avg=34.21ms min=17.8ms  med=33.71ms max=310.23ms p(90)=40.27ms p(95)=42.51ms  p(99.9)=55.39ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 174244
     http_req_receiving.............: avg=72.62µs min=26.18µs med=59.26µs max=108.5ms  p(90)=97.31µs p(95)=114.31µs p(99.9)=816.77µs
     http_req_sending...............: avg=25.67µs min=5.1µs   med=12.69µs max=114.94ms p(90)=19.47µs p(95)=23.52µs  p(99.9)=809.9µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.11ms min=17.69ms med=33.61ms max=293.88ms p(90)=40.17ms p(95)=42.4ms   p(99.9)=55.24ms 
     http_reqs......................: 174244  1428.772104/s
     iteration_duration.............: avg=34.44ms min=20.72ms med=33.93ms max=323.12ms p(90)=40.49ms p(95)=42.73ms  p(99.9)=55.65ms 
     iterations.....................: 174144  1427.952121/s
     success_rate...................: 100.00% ✓ 174144      ✗ 0     
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

     checks.........................: 100.00% ✓ 520485      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 209 MB  1.7 MB/s
     http_req_blocked...............: avg=3.47µs  min=1.02µs  med=2.57µs  max=4.47ms   p(90)=4.11µs   p(95)=4.84µs   p(99.9)=30.93µs 
     http_req_connecting............: avg=573ns   min=0s      med=0s      max=4.43ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.35ms min=18.02ms med=33.79ms max=296.01ms p(90)=41ms     p(95)=43.3ms   p(99.9)=54.57ms 
       { expected_response:true }...: avg=34.35ms min=18.02ms med=33.79ms max=296.01ms p(90)=41ms     p(95)=43.3ms   p(99.9)=54.57ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 173595
     http_req_receiving.............: avg=74.98µs min=25.93µs med=63.31µs max=28.82ms  p(90)=102.19µs p(95)=120.31µs p(99.9)=754.53µs
     http_req_sending...............: avg=22.6µs  min=4.79µs  med=11.1µs  max=79.36ms  p(90)=17.91µs  p(95)=22.15µs  p(99.9)=798.51µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.26ms min=17.83ms med=33.7ms  max=286.82ms p(90)=40.91ms  p(95)=43.2ms   p(99.9)=54.43ms 
     http_reqs......................: 173595  1423.383767/s
     iteration_duration.............: avg=34.57ms min=20.26ms med=34ms    max=310.85ms p(90)=41.2ms   p(95)=43.51ms  p(99.9)=54.87ms 
     iterations.....................: 173495  1422.563821/s
     success_rate...................: 100.00% ✓ 173495      ✗ 0     
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

     checks.........................: 100.00% ✓ 217719     ✗ 0    
     data_received..................: 6.4 GB  52 MB/s
     data_sent......................: 87 MB   714 kB/s
     http_req_blocked...............: avg=4.28µs  min=1.26µs  med=3.19µs  max=3.2ms    p(90)=4.73µs   p(95)=5.41µs   p(99.9)=44.43µs 
     http_req_connecting............: avg=856ns   min=0s      med=0s      max=3.14ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=82.35ms min=19.92ms med=80.17ms max=308.41ms p(90)=97.9ms   p(95)=106.78ms p(99.9)=206.57ms
       { expected_response:true }...: avg=82.35ms min=19.92ms med=80.17ms max=308.41ms p(90)=97.9ms   p(95)=106.78ms p(99.9)=206.57ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 72673
     http_req_receiving.............: avg=84.33µs min=29.38µs med=72.43µs max=146.77ms p(90)=106.25µs p(95)=118.87µs p(99.9)=554.06µs
     http_req_sending...............: avg=23.65µs min=5.06µs  med=14.84µs max=125.22ms p(90)=20.82µs  p(95)=22.98µs  p(99.9)=583.82µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=82.24ms min=19.77ms med=80.06ms max=307.88ms p(90)=97.78ms  p(95)=106.65ms p(99.9)=206.33ms
     http_reqs......................: 72673   594.811687/s
     iteration_duration.............: avg=82.68ms min=23.52ms med=80.42ms max=320.11ms p(90)=98.14ms  p(95)=107.05ms p(99.9)=207.49ms
     iterations.....................: 72573   593.993211/s
     success_rate...................: 100.00% ✓ 72573      ✗ 0    
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

     checks.........................: 100.00% ✓ 193161     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   634 kB/s
     http_req_blocked...............: avg=4.4µs   min=1.03µs  med=2.8µs   max=3.54ms   p(90)=4.34µs   p(95)=4.94µs   p(99.9)=45.25µs 
     http_req_connecting............: avg=1.39µs  min=0s      med=0s      max=3.5ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.85ms min=20.14ms med=91.06ms max=307.84ms p(90)=116.95ms p(95)=125.57ms p(99.9)=164.29ms
       { expected_response:true }...: avg=92.85ms min=20.14ms med=91.06ms max=307.84ms p(90)=116.95ms p(95)=125.57ms p(99.9)=164.29ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64487
     http_req_receiving.............: avg=74.15µs min=27.47µs med=68.86µs max=8.18ms   p(90)=101.87µs p(95)=114.44µs p(99.9)=474.3µs 
     http_req_sending...............: avg=20.24µs min=5.02µs  med=13.76µs max=69.88ms  p(90)=19.56µs  p(95)=21.63µs  p(99.9)=528.61µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.75ms min=19.99ms med=90.96ms max=307.34ms p(90)=116.85ms p(95)=125.48ms p(99.9)=164.05ms
     http_reqs......................: 64487   527.680061/s
     iteration_duration.............: avg=93.2ms  min=30.1ms  med=91.32ms max=323.21ms p(90)=117.23ms p(95)=125.79ms p(99.9)=165.49ms
     iterations.....................: 64387   526.861787/s
     success_rate...................: 100.00% ✓ 64387      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-nightly (HotChocolate subgraphs) (v3.0.0-preview.0-nightly.fbceee06)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 190551     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 76 MB   625 kB/s
     http_req_blocked...............: avg=5.08µs  min=1.16µs  med=3.38µs  max=3.68ms   p(90)=4.94µs   p(95)=5.55µs   p(99.9)=52.89µs 
     http_req_connecting............: avg=1.47µs  min=0s      med=0s      max=3.64ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=94.1ms  min=19.91ms med=92.69ms max=337.4ms  p(90)=117.1ms  p(95)=125ms    p(99.9)=162.45ms
       { expected_response:true }...: avg=94.1ms  min=19.91ms med=92.69ms max=337.4ms  p(90)=117.1ms  p(95)=125ms    p(99.9)=162.45ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63617
     http_req_receiving.............: avg=81.63µs min=31.68µs med=74.13µs max=150.3ms  p(90)=107.69µs p(95)=119.65µs p(99.9)=500.79µs
     http_req_sending...............: avg=28.49µs min=5.19µs  med=14.86µs max=187.85ms p(90)=21.12µs  p(95)=23.35µs  p(99.9)=541.61µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.99ms min=19.84ms med=92.6ms  max=336.9ms  p(90)=117ms    p(95)=124.89ms p(99.9)=162.03ms
     http_reqs......................: 63617   520.491774/s
     iteration_duration.............: avg=94.48ms min=25.81ms med=92.98ms max=345.84ms p(90)=117.37ms p(95)=125.26ms p(99.9)=163.58ms
     iterations.....................: 63517   519.673609/s
     success_rate...................: 100.00% ✓ 63517      ✗ 0    
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

     checks.........................: 100.00% ✓ 142212     ✗ 0    
     data_received..................: 4.2 GB  34 MB/s
     data_sent......................: 57 MB   466 kB/s
     http_req_blocked...............: avg=5.04µs   min=1.09µs  med=2.8µs    max=4.02ms   p(90)=4.17µs   p(95)=4.72µs   p(99.9)=794.9µs 
     http_req_connecting............: avg=2.04µs   min=0s      med=0s       max=3.98ms   p(90)=0s       p(95)=0s       p(99.9)=685.01µs
     http_req_duration..............: avg=126.12ms min=21.25ms med=124.41ms max=346.63ms p(90)=156.42ms p(95)=166.95ms p(99.9)=218.59ms
       { expected_response:true }...: avg=126.12ms min=21.25ms med=124.41ms max=346.63ms p(90)=156.42ms p(95)=166.95ms p(99.9)=218.59ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 47504
     http_req_receiving.............: avg=85.43µs  min=27.99µs med=73.75µs  max=105.49ms p(90)=104.45µs p(95)=116.05µs p(99.9)=463.76µs
     http_req_sending...............: avg=33.71µs  min=5.06µs  med=14.63µs  max=189.12ms p(90)=20.01µs  p(95)=21.84µs  p(99.9)=532.13µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=126ms    min=21.13ms med=124.31ms max=322.12ms p(90)=156.31ms p(95)=166.85ms p(99.9)=216.7ms 
     http_reqs......................: 47504   388.292451/s
     iteration_duration.............: avg=126.6ms  min=38.54ms med=124.69ms max=363.66ms p(90)=156.68ms p(95)=167.23ms p(99.9)=223.7ms 
     iterations.....................: 47404   387.475062/s
     success_rate...................: 100.00% ✓ 47404      ✗ 0    
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

     checks.........................: 100.00% ✓ 107199     ✗ 0    
     data_received..................: 3.1 GB  26 MB/s
     data_sent......................: 43 MB   352 kB/s
     http_req_blocked...............: avg=8.33µs   min=1.5µs   med=3.65µs   max=6.44ms   p(90)=5.24µs   p(95)=5.91µs   p(99.9)=1.19ms  
     http_req_connecting............: avg=4.19µs   min=0s      med=0s       max=6.41ms   p(90)=0s       p(95)=0s       p(99.9)=882.79µs
     http_req_duration..............: avg=167.28ms min=17.58ms med=142.51ms max=823.73ms p(90)=244.42ms p(95)=271.67ms p(99.9)=730.44ms
       { expected_response:true }...: avg=167.28ms min=17.58ms med=142.51ms max=823.73ms p(90)=244.42ms p(95)=271.67ms p(99.9)=730.44ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 35833
     http_req_receiving.............: avg=99.48µs  min=37.37µs med=90.08µs  max=59.22ms  p(90)=121.51µs p(95)=134.49µs p(99.9)=879.36µs
     http_req_sending...............: avg=24.73µs  min=6.59µs  med=18.07µs  max=42.78ms  p(90)=22.95µs  p(95)=24.9µs   p(99.9)=1.36ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=167.16ms min=17.45ms med=142.39ms max=823.61ms p(90)=244.28ms p(95)=271.56ms p(99.9)=730.31ms
     http_reqs......................: 35833   293.545386/s
     iteration_duration.............: avg=167.97ms min=57.67ms med=142.9ms  max=824.05ms p(90)=244.86ms p(95)=272.03ms p(99.9)=730.7ms 
     iterations.....................: 35733   292.726182/s
     success_rate...................: 100.00% ✓ 35733      ✗ 0    
     vus............................: 30      min=0        max=50 
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

     checks.........................: 100.00% ✓ 97146      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   318 kB/s
     http_req_blocked...............: avg=6.74µs   min=1.37µs  med=3.51µs   max=4.33ms   p(90)=4.88µs   p(95)=5.46µs   p(99.9)=1.33ms  
     http_req_connecting............: avg=2.95µs   min=0s      med=0s       max=4.29ms   p(90)=0s       p(95)=0s       p(99.9)=1.29ms  
     http_req_duration..............: avg=184.57ms min=22.08ms med=185.28ms max=398.8ms  p(90)=196.87ms p(95)=201.63ms p(99.9)=264.9ms 
       { expected_response:true }...: avg=184.57ms min=22.08ms med=185.28ms max=398.8ms  p(90)=196.87ms p(95)=201.63ms p(99.9)=264.9ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 32482
     http_req_receiving.............: avg=95.19µs  min=37.46µs med=85.2µs   max=181.1ms  p(90)=114.51µs p(95)=125.26µs p(99.9)=451.02µs
     http_req_sending...............: avg=27.29µs  min=5.97µs  med=16.83µs  max=94.41ms  p(90)=21.26µs  p(95)=23.08µs  p(99.9)=553.09µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.45ms min=21.86ms med=185.16ms max=398.13ms p(90)=196.76ms p(95)=201.5ms  p(99.9)=264.53ms
     http_reqs......................: 32482   264.975979/s
     iteration_duration.............: avg=185.39ms min=52.51ms med=185.64ms max=412.9ms  p(90)=197.17ms p(95)=201.94ms p(99.9)=270.91ms
     iterations.....................: 32382   264.160217/s
     success_rate...................: 100.00% ✓ 32382      ✗ 0    
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

