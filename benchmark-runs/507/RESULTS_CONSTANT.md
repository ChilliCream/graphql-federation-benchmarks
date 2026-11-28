## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-aot-11 | 16.8.0-p.25 | 5,566 | 5,572 | 5,548 | 0.2% | 93 MB | 17.0 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.25 | 5,563 | 5,576 | 5,531 | 0.3% | 353 MB | 65.0 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.25 | 5,512 | 5,516 | 5,495 | 0.1% | 88 MB | 16.3 KB |  |
| fusion-fed-net-11 | 16.7.7 | 5,496 | 5,504 | 5,407 | 0.8% | 359 MB | 66.8 KB |  |
| nitro-router | 16.8.0-p.25 | 5,474 | 5,487 | 5,468 | 0.2% | 139 MB | 25.9 KB |  |
| fusion-net-11 | 16.7.7 | 5,459 | 5,482 | 5,450 | 0.2% | 367 MB | 68.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.25 | 5,440 | 5,464 | 5,407 | 0.4% | 347 MB | 65.3 KB |  |
| nitro-router-fed | 16.8.0-p.25 | 5,407 | 5,436 | 5,398 | 0.3% | 135 MB | 25.6 KB |  |
| fusion-aot-11 | 16.7.7 | 5,301 | 5,324 | 5,290 | 0.3% | 121 MB | 23.4 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 5,248 | 5,269 | 5,217 | 0.4% | 113 MB | 22.1 KB |  |
| feddi-gateway | 2026-11-22-1912 | 5,101 | 5,118 | 5,095 | 0.2% | 2,308 MB | 463.3 KB |  |
| hive-router | v0.3.21 | 4,664 | 4,687 | 4,645 | 0.3% | 93 MB | 20.5 KB |  |
| hive-router-nightly | v0.3.21-nightly.f689b548 | 4,623 | 4,628 | 4,590 | 0.3% | 93 MB | 20.7 KB |  |
| grafbase | 0.53.5 | 1,856 | 1,862 | 1,852 | 0.2% | 110 MB | 60.6 KB |  |
| caliban | 3.2.1 | 1,491 | 1,496 | 1,457 | 1.4% | 5,938 MB | 4,077.8 KB |  |
| cosmo | 0.378.1 | 1,473 | 1,480 | 1,472 | 0.2% | 170 MB | 118.1 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 602 | 604 | 601 | 0.2% | 2,604 MB | 4,429.3 KB |  |
| apollo-router | v2.19.1 | 536 | 537 | 535 | 0.1% | 180 MB | 344.3 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.95b76d0a | 487 | 497 | 482 | 1.4% | 194 MB | 407.0 KB |  |
| hive-gateway | 2.15.10 | 285 | 286 | 284 | 0.3% | 3,422 MB | 12,295.5 KB |  |
| apollo-gateway | 2.14.4 | 269 | 270 | 268 | 0.3% | 2,134 MB | 8,122.7 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.25)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 2005326     ✗ 0     
     data_received..................: 59 GB   487 MB/s
     data_sent......................: 804 MB  6.7 MB/s
     http_req_blocked...............: avg=2.59µs  min=791ns    med=1.95µs  max=6.91ms   p(90)=3.11µs  p(95)=3.76µs   p(99.9)=27.96µs
     http_req_connecting............: avg=174ns   min=0s       med=0s      max=4.93ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.77ms  min=774.39µs med=7.82ms  max=289.51ms p(90)=14.15ms p(95)=17.39ms  p(99.9)=29.81ms
       { expected_response:true }...: avg=8.77ms  min=774.39µs med=7.82ms  max=289.51ms p(90)=14.15ms p(95)=17.39ms  p(99.9)=29.81ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 668542
     http_req_receiving.............: avg=92.76µs min=24.53µs  med=45.24µs max=105.67ms p(90)=86.19µs p(95)=185.91µs p(99.9)=6.15ms 
     http_req_sending...............: avg=41.29µs min=4.28µs   med=8.17µs  max=79.17ms  p(90)=13.77µs p(95)=97.2µs   p(99.9)=4.94ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.63ms  min=731.27µs med=7.72ms  max=285.18ms p(90)=13.92ms p(95)=17.1ms   p(99.9)=29.35ms
     http_reqs......................: 668542  5566.491497/s
     iteration_duration.............: avg=8.96ms  min=1.19ms   med=8.01ms  max=300.91ms p(90)=14.35ms p(95)=17.6ms   p(99.9)=30.06ms
     iterations.....................: 668442  5565.658865/s
     success_rate...................: 100.00% ✓ 668442      ✗ 0     
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

     checks.........................: 100.00% ✓ 2004441     ✗ 0     
     data_received..................: 59 GB   487 MB/s
     data_sent......................: 803 MB  6.7 MB/s
     http_req_blocked...............: avg=2.72µs  min=801ns    med=1.95µs  max=8.6ms    p(90)=2.96µs  p(95)=3.51µs  p(99.9)=25.94µs
     http_req_connecting............: avg=394ns   min=0s       med=0s      max=8.46ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=8.77ms  min=750.37µs med=7.85ms  max=291.15ms p(90)=14.11ms p(95)=17.31ms p(99.9)=29.86ms
       { expected_response:true }...: avg=8.77ms  min=750.37µs med=7.85ms  max=291.15ms p(90)=14.11ms p(95)=17.31ms p(99.9)=29.86ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 668247
     http_req_receiving.............: avg=96.05µs min=25.77µs  med=47.47µs max=47.34ms  p(90)=83.11µs p(95)=185.7µs p(99.9)=6.57ms 
     http_req_sending...............: avg=42.17µs min=4.23µs   med=8.27µs  max=269.44ms p(90)=13.38µs p(95)=95.14µs p(99.9)=4.85ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=8.63ms  min=700.76µs med=7.74ms  max=290.41ms p(90)=13.87ms p(95)=17.01ms p(99.9)=29.3ms 
     http_reqs......................: 668247  5563.947534/s
     iteration_duration.............: avg=8.97ms  min=1.15ms   med=8.03ms  max=318.81ms p(90)=14.32ms p(95)=17.53ms p(99.9)=30.13ms
     iterations.....................: 668147  5563.114915/s
     success_rate...................: 100.00% ✓ 668147      ✗ 0     
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

     checks.........................: 100.00% ✓ 1985940     ✗ 0     
     data_received..................: 58 GB   482 MB/s
     data_sent......................: 796 MB  6.6 MB/s
     http_req_blocked...............: avg=2.88µs  min=882ns    med=2.3µs   max=6.93ms   p(90)=3.51µs  p(95)=4.15µs   p(99.9)=32.95µs
     http_req_connecting............: avg=138ns   min=0s       med=0s      max=3.52ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.85ms  min=803.09µs med=7.87ms  max=271.38ms p(90)=14.33ms p(95)=17.71ms  p(99.9)=30.63ms
       { expected_response:true }...: avg=8.85ms  min=803.09µs med=7.87ms  max=271.38ms p(90)=14.33ms p(95)=17.71ms  p(99.9)=30.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 662080
     http_req_receiving.............: avg=96.56µs min=24.11µs  med=46.01µs max=132.96ms p(90)=87.91µs p(95)=190.51µs p(99.9)=6.64ms 
     http_req_sending...............: avg=44.92µs min=4.53µs   med=8.51µs  max=101.12ms p(90)=14.41µs p(95)=102.02µs p(99.9)=5.3ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.71ms  min=738.44µs med=7.76ms  max=261.67ms p(90)=14.08ms p(95)=17.42ms  p(99.9)=30.17ms
     http_reqs......................: 662080  5512.37605/s
     iteration_duration.............: avg=9.05ms  min=966.88µs med=8.06ms  max=282.41ms p(90)=14.54ms p(95)=17.93ms  p(99.9)=30.94ms
     iterations.....................: 661980  5511.543465/s
     success_rate...................: 100.00% ✓ 661980      ✗ 0     
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

     checks.........................: 100.00% ✓ 1980033     ✗ 0     
     data_received..................: 58 GB   481 MB/s
     data_sent......................: 793 MB  6.6 MB/s
     http_req_blocked...............: avg=2.39µs  min=782ns    med=1.86µs  max=6.61ms   p(90)=2.95µs  p(95)=3.54µs   p(99.9)=26.66µs
     http_req_connecting............: avg=148ns   min=0s       med=0s      max=3.57ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.89ms  min=801.29µs med=7.97ms  max=259.57ms p(90)=14.24ms p(95)=17.38ms  p(99.9)=29.91ms
       { expected_response:true }...: avg=8.89ms  min=801.29µs med=7.97ms  max=259.57ms p(90)=14.24ms p(95)=17.38ms  p(99.9)=29.91ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 660111
     http_req_receiving.............: avg=92.38µs min=25.6µs   med=45.83µs max=142.47ms p(90)=86.2µs  p(95)=184.49µs p(99.9)=6.06ms 
     http_req_sending...............: avg=41.01µs min=4.19µs   med=7.96µs  max=120.12ms p(90)=13.56µs p(95)=97.83µs  p(99.9)=4.65ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.75ms  min=728.64µs med=7.86ms  max=259.25ms p(90)=14.01ms p(95)=17.1ms   p(99.9)=29.54ms
     http_reqs......................: 660111  5496.042822/s
     iteration_duration.............: avg=9.08ms  min=999.31µs med=8.15ms  max=278.43ms p(90)=14.44ms p(95)=17.59ms  p(99.9)=30.21ms
     iterations.....................: 660011  5495.210229/s
     success_rate...................: 100.00% ✓ 660011      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: nitro-router (HotChocolate subgraphs) (16.8.0-p.25)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1972350     ✗ 0     
     data_received..................: 58 GB   479 MB/s
     data_sent......................: 790 MB  6.6 MB/s
     http_req_blocked...............: avg=2.88µs  min=871ns    med=2.33µs  max=9.75ms   p(90)=3.51µs  p(95)=4.13µs   p(99.9)=33.88µs
     http_req_connecting............: avg=140ns   min=0s       med=0s      max=4.05ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.91ms  min=799.45µs med=7.94ms  max=289.81ms p(90)=14.46ms p(95)=17.86ms  p(99.9)=30.82ms
       { expected_response:true }...: avg=8.91ms  min=799.45µs med=7.94ms  max=289.81ms p(90)=14.46ms p(95)=17.86ms  p(99.9)=30.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 657550
     http_req_receiving.............: avg=98.47µs min=25.25µs  med=47.09µs max=187.04ms p(90)=88.52µs p(95)=197µs    p(99.9)=6.36ms 
     http_req_sending...............: avg=43.51µs min=4.42µs   med=8.38µs  max=126.56ms p(90)=14.04µs p(95)=102.21µs p(99.9)=4.94ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.77ms  min=722.64µs med=7.83ms  max=289.5ms  p(90)=14.21ms p(95)=17.57ms  p(99.9)=30.38ms
     http_reqs......................: 657550  5474.581216/s
     iteration_duration.............: avg=9.11ms  min=1.06ms   med=8.13ms  max=300.21ms p(90)=14.68ms p(95)=18.09ms  p(99.9)=31.1ms 
     iterations.....................: 657450  5473.748644/s
     success_rate...................: 100.00% ✓ 657450      ✗ 0     
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

     checks.........................: 100.00% ✓ 1966788     ✗ 0     
     data_received..................: 57 GB   478 MB/s
     data_sent......................: 788 MB  6.6 MB/s
     http_req_blocked...............: avg=3µs     min=901ns    med=2.41µs  max=6.36ms   p(90)=3.67µs  p(95)=4.33µs   p(99.9)=34.17µs
     http_req_connecting............: avg=138ns   min=0s       med=0s      max=4.06ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.94ms  min=779.4µs  med=7.92ms  max=249.08ms p(90)=14.57ms p(95)=18.11ms  p(99.9)=31.36ms
       { expected_response:true }...: avg=8.94ms  min=779.4µs  med=7.92ms  max=249.08ms p(90)=14.57ms p(95)=18.11ms  p(99.9)=31.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 655696
     http_req_receiving.............: avg=98.91µs min=25.3µs   med=46.89µs max=71.18ms  p(90)=89.78µs p(95)=197.2µs  p(99.9)=6.67ms 
     http_req_sending...............: avg=44.46µs min=4.58µs   med=8.74µs  max=81.84ms  p(90)=14.79µs p(95)=103.81µs p(99.9)=5.17ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.79ms  min=714.49µs med=7.81ms  max=248.61ms p(90)=14.32ms p(95)=17.81ms  p(99.9)=30.86ms
     http_reqs......................: 655696  5459.548481/s
     iteration_duration.............: avg=9.14ms  min=1.12ms   med=8.11ms  max=318.38ms p(90)=14.79ms p(95)=18.34ms  p(99.9)=31.69ms
     iterations.....................: 655596  5458.715847/s
     success_rate...................: 100.00% ✓ 655596      ✗ 0     
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

     checks.........................: 100.00% ✓ 1960134     ✗ 0     
     data_received..................: 57 GB   476 MB/s
     data_sent......................: 786 MB  6.5 MB/s
     http_req_blocked...............: avg=2.95µs   min=932ns    med=2.38µs max=11.41ms  p(90)=3.64µs  p(95)=4.34µs   p(99.9)=32.88µs
     http_req_connecting............: avg=134ns    min=0s       med=0s     max=3.55ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.96ms   min=787.03µs med=7.94ms max=279.03ms p(90)=14.59ms p(95)=18.09ms  p(99.9)=31.33ms
       { expected_response:true }...: avg=8.96ms   min=787.03µs med=7.94ms max=279.03ms p(90)=14.59ms p(95)=18.09ms  p(99.9)=31.33ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 653478
     http_req_receiving.............: avg=104.71µs min=26.49µs  med=48.5µs max=174.68ms p(90)=92.69µs p(95)=197.23µs p(99.9)=7.39ms 
     http_req_sending...............: avg=45.96µs  min=4.46µs   med=8.83µs max=18.53ms  p(90)=14.92µs p(95)=103.93µs p(99.9)=5.57ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.81ms   min=710.72µs med=7.82ms max=256.73ms p(90)=14.32ms p(95)=17.76ms  p(99.9)=30.49ms
     http_reqs......................: 653478  5440.939572/s
     iteration_duration.............: avg=9.17ms   min=979.96µs med=8.13ms max=293.99ms p(90)=14.81ms p(95)=18.32ms  p(99.9)=31.65ms
     iterations.....................: 653378  5440.10696/s
     success_rate...................: 100.00% ✓ 653378      ✗ 0     
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

     checks.........................: 100.00% ✓ 1948245     ✗ 0     
     data_received..................: 57 GB   473 MB/s
     data_sent......................: 781 MB  6.5 MB/s
     http_req_blocked...............: avg=2.97µs   min=932ns    med=2.37µs  max=6.66ms   p(90)=3.59µs  p(95)=4.25µs   p(99.9)=34.61µs
     http_req_connecting............: avg=145ns    min=0s       med=0s      max=4.22ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.02ms   min=816.33µs med=8.03ms  max=267.94ms p(90)=14.63ms p(95)=18.13ms  p(99.9)=31.18ms
       { expected_response:true }...: avg=9.02ms   min=816.33µs med=8.03ms  max=267.94ms p(90)=14.63ms p(95)=18.13ms  p(99.9)=31.18ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 649515
     http_req_receiving.............: avg=100.11µs min=27.02µs  med=48.05µs max=184.33ms p(90)=91.91µs p(95)=197.3µs  p(99.9)=6.53ms 
     http_req_sending...............: avg=44.86µs  min=4.54µs   med=8.78µs  max=155.15ms p(90)=14.77µs p(95)=104.26µs p(99.9)=5.24ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.88ms   min=738.69µs med=7.92ms  max=267.71ms p(90)=14.38ms p(95)=17.82ms  p(99.9)=30.57ms
     http_reqs......................: 649515  5407.685719/s
     iteration_duration.............: avg=9.22ms   min=1.18ms   med=8.22ms  max=285.4ms  p(90)=14.85ms p(95)=18.36ms  p(99.9)=31.47ms
     iterations.....................: 649415  5406.853146/s
     success_rate...................: 100.00% ✓ 649415      ✗ 0     
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

     checks.........................: 100.00% ✓ 1910112     ✗ 0     
     data_received..................: 56 GB   464 MB/s
     data_sent......................: 765 MB  6.4 MB/s
     http_req_blocked...............: avg=2.99µs  min=932ns    med=2.38µs  max=6.21ms   p(90)=3.63µs  p(95)=4.28µs   p(99.9)=34.23µs
     http_req_connecting............: avg=157ns   min=0s       med=0s      max=3.73ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.21ms  min=832.15µs med=8.24ms  max=280.38ms p(90)=14.88ms p(95)=18.28ms  p(99.9)=31.31ms
       { expected_response:true }...: avg=9.21ms  min=832.15µs med=8.24ms  max=280.38ms p(90)=14.88ms p(95)=18.28ms  p(99.9)=31.31ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 636804
     http_req_receiving.............: avg=94.84µs min=25.4µs   med=46.73µs max=117.41ms p(90)=90.11µs p(95)=201.88µs p(99.9)=5.86ms 
     http_req_sending...............: avg=43.42µs min=4.48µs   med=8.71µs  max=119.64ms p(90)=14.72µs p(95)=105.68µs p(99.9)=4.81ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.07ms  min=758.95µs med=8.13ms  max=268.66ms p(90)=14.65ms p(95)=17.99ms  p(99.9)=30.88ms
     http_reqs......................: 636804  5301.683693/s
     iteration_duration.............: avg=9.41ms  min=1.29ms   med=8.43ms  max=290.7ms  p(90)=15.09ms p(95)=18.51ms  p(99.9)=31.62ms
     iterations.....................: 636704  5300.851147/s
     success_rate...................: 100.00% ✓ 636704      ✗ 0     
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

     checks.........................: 100.00% ✓ 1890918     ✗ 0     
     data_received..................: 55 GB   459 MB/s
     data_sent......................: 758 MB  6.3 MB/s
     http_req_blocked...............: avg=2.54µs  min=801ns    med=1.99µs  max=5.67ms   p(90)=3.14µs  p(95)=3.72µs   p(99.9)=27.01µs
     http_req_connecting............: avg=143ns   min=0s       med=0s      max=4.03ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.31ms  min=861.25µs med=8.41ms  max=274.45ms p(90)=14.88ms p(95)=17.99ms  p(99.9)=30.42ms
       { expected_response:true }...: avg=9.31ms  min=861.25µs med=8.41ms  max=274.45ms p(90)=14.88ms p(95)=17.99ms  p(99.9)=30.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 630406
     http_req_receiving.............: avg=89.86µs min=24.72µs  med=46.03µs max=62.16ms  p(90)=88.16µs p(95)=196.62µs p(99.9)=5.49ms 
     http_req_sending...............: avg=41.52µs min=4.34µs   med=7.99µs  max=115.27ms p(90)=13.72µs p(95)=103.91µs p(99.9)=4.63ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.18ms  min=783.12µs med=8.3ms   max=268.11ms p(90)=14.66ms p(95)=17.74ms  p(99.9)=30.09ms
     http_reqs......................: 630406  5248.338245/s
     iteration_duration.............: avg=9.51ms  min=1.29ms   med=8.59ms  max=283.14ms p(90)=15.08ms p(95)=18.21ms  p(99.9)=30.72ms
     iterations.....................: 630306  5247.505712/s
     success_rate...................: 100.00% ✓ 630306      ✗ 0     
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

     checks.........................: 100.00% ✓ 1838070     ✗ 0     
     data_received..................: 54 GB   446 MB/s
     data_sent......................: 737 MB  6.1 MB/s
     http_req_blocked...............: avg=2.74µs  min=781ns    med=1.92µs  max=8.15ms   p(90)=3.05µs  p(95)=3.64µs   p(99.9)=27.71µs
     http_req_connecting............: avg=370ns   min=0s       med=0s      max=8.12ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.59ms  min=809.55µs med=8.75ms  max=264.72ms p(90)=15.2ms  p(95)=18.24ms  p(99.9)=30.94ms
       { expected_response:true }...: avg=9.59ms  min=809.55µs med=8.75ms  max=264.72ms p(90)=15.2ms  p(95)=18.24ms  p(99.9)=30.94ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 612790
     http_req_receiving.............: avg=96.76µs min=24.6µs   med=46.21µs max=259.8ms  p(90)=88.22µs p(95)=198.33µs p(99.9)=6.23ms 
     http_req_sending...............: avg=42.21µs min=4.35µs   med=8.09µs  max=246ms    p(90)=13.81µs p(95)=102.75µs p(99.9)=4.63ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.45ms  min=736.24µs med=8.62ms  max=260.46ms p(90)=14.97ms p(95)=17.98ms  p(99.9)=30.54ms
     http_reqs......................: 612790  5101.953999/s
     iteration_duration.............: avg=9.78ms  min=1.35ms   med=8.93ms  max=282.94ms p(90)=15.4ms  p(95)=18.46ms  p(99.9)=31.18ms
     iterations.....................: 612690  5101.121421/s
     success_rate...................: 100.00% ✓ 612690      ✗ 0     
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

     checks.........................: 100.00% ✓ 1680636     ✗ 0     
     data_received..................: 49 GB   408 MB/s
     data_sent......................: 673 MB  5.6 MB/s
     http_req_blocked...............: avg=3.26µs   min=802ns    med=2.67µs  max=6.29ms   p(90)=4.1µs    p(95)=4.86µs   p(99.9)=38.48µs
     http_req_connecting............: avg=158ns    min=0s       med=0s      max=3.48ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.49ms  min=931.78µs med=9.7ms   max=266.9ms  p(90)=15.26ms  p(95)=19.07ms  p(99.9)=31.24ms
       { expected_response:true }...: avg=10.49ms  min=931.78µs med=9.7ms   max=266.9ms  p(90)=15.26ms  p(95)=19.07ms  p(99.9)=31.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 560312
     http_req_receiving.............: avg=104.09µs min=25.3µs   med=51.16µs max=142.97ms p(90)=101.81µs p(95)=218.81µs p(99.9)=6.66ms 
     http_req_sending...............: avg=47.94µs  min=4.52µs   med=10.05µs max=159.35ms p(90)=17.23µs  p(95)=116.1µs  p(99.9)=5.29ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.33ms  min=861.59µs med=9.6ms   max=266.42ms p(90)=14.96ms  p(95)=18.75ms  p(99.9)=30.63ms
     http_reqs......................: 560312  4664.29576/s
     iteration_duration.............: avg=10.69ms  min=1.51ms   med=9.9ms   max=283.56ms p(90)=15.49ms  p(95)=19.31ms  p(99.9)=31.5ms 
     iterations.....................: 560212  4663.463314/s
     success_rate...................: 100.00% ✓ 560212      ✗ 0     
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

     checks.........................: 100.00% ✓ 1665942     ✗ 0     
     data_received..................: 49 GB   404 MB/s
     data_sent......................: 668 MB  5.6 MB/s
     http_req_blocked...............: avg=2.49µs  min=762ns    med=1.97µs  max=7.69ms   p(90)=3.11µs  p(95)=3.7µs    p(99.9)=27.35µs
     http_req_connecting............: avg=155ns   min=0s       med=0s      max=3.48ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.6ms  min=973.63µs med=10.08ms max=280.68ms p(90)=14.6ms  p(95)=17.61ms  p(99.9)=28.25ms
       { expected_response:true }...: avg=10.6ms  min=973.63µs med=10.08ms max=280.68ms p(90)=14.6ms  p(95)=17.61ms  p(99.9)=28.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 555414
     http_req_receiving.............: avg=91.24µs min=24.38µs  med=49.38µs max=83.54ms  p(90)=93.24µs p(95)=201.77µs p(99.9)=5.54ms 
     http_req_sending...............: avg=39.91µs min=3.89µs   med=8.55µs  max=112.93ms p(90)=14.59µs p(95)=105.4µs  p(99.9)=4.1ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.47ms min=879.15µs med=9.99ms  max=280.21ms p(90)=14.37ms p(95)=17.35ms  p(99.9)=27.9ms 
     http_reqs......................: 555414  4623.394116/s
     iteration_duration.............: avg=10.79ms min=1.62ms   med=10.26ms max=290.02ms p(90)=14.81ms p(95)=17.83ms  p(99.9)=28.5ms 
     iterations.....................: 555314  4622.561693/s
     success_rate...................: 100.00% ✓ 555314      ✗ 0     
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

     checks.........................: 100.00% ✓ 669426      ✗ 0     
     data_received..................: 20 GB   163 MB/s
     data_sent......................: 268 MB  2.2 MB/s
     http_req_blocked...............: avg=3.24µs  min=822ns   med=2.28µs  max=6.21ms   p(90)=4.32µs   p(95)=5.34µs   p(99.9)=38.79µs
     http_req_connecting............: avg=423ns   min=0s      med=0s      max=4.1ms    p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.64ms min=1.82ms  med=26.13ms max=314.46ms p(90)=34.61ms  p(95)=37.4ms   p(99.9)=51.05ms
       { expected_response:true }...: avg=26.64ms min=1.82ms  med=26.13ms max=314.46ms p(90)=34.61ms  p(95)=37.4ms   p(99.9)=51.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 223242
     http_req_receiving.............: avg=84.91µs min=26.65µs med=56.34µs max=162.61ms p(90)=118.22µs p(95)=186.27µs p(99.9)=1.57ms 
     http_req_sending...............: avg=32.6µs  min=4.67µs  med=9.79µs  max=128.79ms p(90)=22.83µs  p(95)=98.98µs  p(99.9)=1.27ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.53ms min=1.77ms  med=26.02ms max=297.69ms p(90)=34.48ms  p(95)=37.27ms  p(99.9)=50.67ms
     http_reqs......................: 223242  1856.366527/s
     iteration_duration.............: avg=26.87ms min=6.39ms  med=26.34ms max=331.2ms  p(90)=34.82ms  p(95)=37.62ms  p(99.9)=51.43ms
     iterations.....................: 223142  1855.534978/s
     success_rate...................: 100.00% ✓ 223142      ✗ 0     
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

     checks.........................: 100.00% ✓ 537903      ✗ 0     
     data_received..................: 16 GB   130 MB/s
     data_sent......................: 216 MB  1.8 MB/s
     http_req_blocked...............: avg=3.83µs  min=1.09µs  med=3.1µs   max=3.85ms   p(90)=4.77µs  p(95)=5.53µs   p(99.9)=36.84µs 
     http_req_connecting............: avg=420ns   min=0s      med=0s      max=3.82ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.2ms  min=2.05ms  med=32.29ms max=284.71ms p(90)=47.07ms p(95)=51.88ms  p(99.9)=78.7ms  
       { expected_response:true }...: avg=33.2ms  min=2.05ms  med=32.29ms max=284.71ms p(90)=47.07ms p(95)=51.88ms  p(99.9)=78.7ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 179401
     http_req_receiving.............: avg=75.25µs min=28.01µs med=63.06µs max=82.67ms  p(90)=99.78µs p(95)=115.59µs p(99.9)=845.18µs
     http_req_sending...............: avg=24.29µs min=5.19µs  med=12.71µs max=142.63ms p(90)=18.69µs p(95)=22.4µs   p(99.9)=794.99µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.11ms min=1.95ms  med=32.2ms  max=284.49ms p(90)=46.97ms p(95)=51.78ms  p(99.9)=78.54ms 
     http_reqs......................: 179401  1491.586531/s
     iteration_duration.............: avg=33.45ms min=5.57ms  med=32.52ms max=296.68ms p(90)=47.29ms p(95)=52.11ms  p(99.9)=79.1ms  
     iterations.....................: 179301  1490.755105/s
     success_rate...................: 100.00% ✓ 179301      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 531264      ✗ 0     
     data_received..................: 16 GB   129 MB/s
     data_sent......................: 213 MB  1.8 MB/s
     http_req_blocked...............: avg=3µs     min=912ns   med=2.15µs  max=4.04ms   p(90)=3.63µs  p(95)=4.3µs    p(99.9)=26.54µs 
     http_req_connecting............: avg=547ns   min=0s      med=0s      max=4ms      p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.65ms min=2.02ms  med=32.77ms max=285.82ms p(90)=48.58ms p(95)=53.53ms  p(99.9)=76.73ms 
       { expected_response:true }...: avg=33.65ms min=2.02ms  med=32.77ms max=285.82ms p(90)=48.58ms p(95)=53.53ms  p(99.9)=76.73ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 177188
     http_req_receiving.............: avg=67.41µs min=24.83µs med=56.93µs max=124ms    p(90)=92.96µs p(95)=107.77µs p(99.9)=659.55µs
     http_req_sending...............: avg=22.47µs min=4.45µs  med=9.92µs  max=176.01ms p(90)=16.18µs p(95)=19.81µs  p(99.9)=733.97µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.56ms min=1.97ms  med=32.68ms max=285.37ms p(90)=48.49ms p(95)=53.45ms  p(99.9)=76.58ms 
     http_reqs......................: 177188  1473.250761/s
     iteration_duration.............: avg=33.87ms min=4.23ms  med=32.97ms max=302.37ms p(90)=48.77ms p(95)=53.72ms  p(99.9)=77.28ms 
     iterations.....................: 177088  1472.419299/s
     success_rate...................: 100.00% ✓ 177088      ✗ 0     
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

     checks.........................: 100.00% ✓ 217440     ✗ 0    
     data_received..................: 6.4 GB  53 MB/s
     data_sent......................: 87 MB   723 kB/s
     http_req_blocked...............: avg=4.29µs  min=1.21µs  med=2.98µs  max=3.9ms    p(90)=4.43µs   p(95)=5.04µs   p(99.9)=42.64µs 
     http_req_connecting............: avg=919ns   min=0s      med=0s      max=3.14ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=82.44ms min=3.45ms  med=79.76ms max=323.94ms p(90)=101.44ms p(95)=112.87ms p(99.9)=204.94ms
       { expected_response:true }...: avg=82.44ms min=3.45ms  med=79.76ms max=323.94ms p(90)=101.44ms p(95)=112.87ms p(99.9)=204.94ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 72580
     http_req_receiving.............: avg=84.03µs min=28.8µs  med=69.81µs max=148.49ms p(90)=102.72µs p(95)=114.85µs p(99.9)=589.18µs
     http_req_sending...............: avg=21.96µs min=5.15µs  med=13.42µs max=89.58ms  p(90)=19.35µs  p(95)=21.29µs  p(99.9)=642.35µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=82.34ms min=3.4ms   med=79.66ms max=323.62ms p(90)=101.33ms p(95)=112.77ms p(99.9)=203.99ms
     http_reqs......................: 72580   602.346859/s
     iteration_duration.............: avg=82.79ms min=23.45ms med=80ms    max=331.34ms p(90)=101.69ms p(95)=113.15ms p(99.9)=207.58ms
     iterations.....................: 72480   601.516951/s
     success_rate...................: 100.00% ✓ 72480      ✗ 0    
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

     checks.........................: 100.00% ✓ 193638     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   644 kB/s
     http_req_blocked...............: avg=4.38µs  min=1.03µs  med=2.86µs  max=3.42ms   p(90)=4.25µs   p(95)=4.8µs    p(99.9)=46.92µs 
     http_req_connecting............: avg=1.34µs  min=0s      med=0s      max=3.37ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.59ms min=4.38ms  med=90.73ms max=292.19ms p(90)=124.45ms p(95)=134.19ms p(99.9)=176.38ms
       { expected_response:true }...: avg=92.59ms min=4.38ms  med=90.73ms max=292.19ms p(90)=124.45ms p(95)=134.19ms p(99.9)=176.38ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64646
     http_req_receiving.............: avg=82.3µs  min=26.95µs med=70.64µs max=121.4ms  p(90)=101.46µs p(95)=114.03µs p(99.9)=547.01µs
     http_req_sending...............: avg=23.68µs min=5µs     med=14.28µs max=117.26ms p(90)=19.6µs   p(95)=21.48µs  p(99.9)=536.73µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.48ms min=4.25ms  med=90.63ms max=291.72ms p(90)=124.35ms p(95)=134.08ms p(99.9)=175.62ms
     http_reqs......................: 64646   536.168156/s
     iteration_duration.............: avg=92.97ms min=13.97ms med=91.01ms max=311.61ms p(90)=124.72ms p(95)=134.44ms p(99.9)=178.19ms
     iterations.....................: 64546   535.338765/s
     success_rate...................: 100.00% ✓ 64546      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 176067     ✗ 0    
     data_received..................: 5.1 GB  43 MB/s
     data_sent......................: 71 MB   585 kB/s
     http_req_blocked...............: avg=6.42µs   min=1.05µs  med=2.75µs   max=7.71ms   p(90)=4.21µs   p(95)=4.73µs   p(99.9)=46.29µs 
     http_req_connecting............: avg=3.44µs   min=0s      med=0s       max=7.68ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=101.85ms min=4.57ms  med=99.87ms  max=295.84ms p(90)=135.34ms p(95)=146.38ms p(99.9)=191.5ms 
       { expected_response:true }...: avg=101.85ms min=4.57ms  med=99.87ms  max=295.84ms p(90)=135.34ms p(95)=146.38ms p(99.9)=191.5ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 58789
     http_req_receiving.............: avg=77.42µs  min=28.45µs med=67.68µs  max=126.63ms p(90)=98.24µs  p(95)=111.27µs p(99.9)=510.14µs
     http_req_sending...............: avg=22.86µs  min=5.21µs  med=13.39µs  max=69.33ms  p(90)=19.24µs  p(95)=20.98µs  p(99.9)=776.52µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=101.75ms min=4.5ms   med=99.78ms  max=290.98ms p(90)=135.25ms p(95)=146.28ms p(99.9)=190.54ms
     http_reqs......................: 58789   487.405573/s
     iteration_duration.............: avg=102.26ms min=18.74ms med=100.15ms max=312.82ms p(90)=135.63ms p(95)=146.67ms p(99.9)=192.22ms
     iterations.....................: 58689   486.576497/s
     success_rate...................: 100.00% ✓ 58689      ✗ 0    
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

     checks.........................: 100.00% ✓ 103233     ✗ 0    
     data_received..................: 3.0 GB  25 MB/s
     data_sent......................: 41 MB   343 kB/s
     http_req_blocked...............: avg=6.49µs   min=1.3µs   med=3.4µs    max=3.59ms   p(90)=4.77µs   p(95)=5.34µs   p(99.9)=1.46ms  
     http_req_connecting............: avg=2.87µs   min=0s      med=0s       max=3.49ms   p(90)=0s       p(95)=0s       p(99.9)=1.44ms  
     http_req_duration..............: avg=173.71ms min=5.47ms  med=155.83ms max=806.73ms p(90)=197.9ms  p(95)=219.04ms p(99.9)=710.67ms
       { expected_response:true }...: avg=173.71ms min=5.47ms  med=155.83ms max=806.73ms p(90)=197.9ms  p(95)=219.04ms p(99.9)=710.67ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 34511
     http_req_receiving.............: avg=86.77µs  min=34.11µs med=82.13µs  max=9.05ms   p(90)=111.81µs p(95)=122.5µs  p(99.9)=586.12µs
     http_req_sending...............: avg=21.8µs   min=6.02µs  med=16.51µs  max=40.21ms  p(90)=21.21µs  p(95)=22.84µs  p(99.9)=471.87µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=173.6ms  min=5.39ms  med=155.72ms max=806.61ms p(90)=197.79ms p(95)=218.93ms p(99.9)=710.58ms
     http_reqs......................: 34511   285.686781/s
     iteration_duration.............: avg=174.46ms min=66.31ms med=156.14ms max=806.96ms p(90)=198.21ms p(95)=219.44ms p(99.9)=710.97ms
     iterations.....................: 34411   284.858967/s
     success_rate...................: 100.00% ✓ 34411      ✗ 0    
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

     checks.........................: 100.00% ✓ 97392      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   323 kB/s
     http_req_blocked...............: avg=6.62µs   min=1.22µs  med=3.37µs   max=4.39ms   p(90)=4.69µs   p(95)=5.25µs   p(99.9)=1.46ms  
     http_req_connecting............: avg=2.99µs   min=0s      med=0s       max=4.35ms   p(90)=0s       p(95)=0s       p(99.9)=1.36ms  
     http_req_duration..............: avg=184.08ms min=7.51ms  med=184.9ms  max=369.52ms p(90)=195.27ms p(95)=200.22ms p(99.9)=267.95ms
       { expected_response:true }...: avg=184.08ms min=7.51ms  med=184.9ms  max=369.52ms p(90)=195.27ms p(95)=200.22ms p(99.9)=267.95ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32564
     http_req_receiving.............: avg=92.63µs  min=34.36µs med=84.21µs  max=52.81ms  p(90)=112.79µs p(95)=123.04µs p(99.9)=496.16µs
     http_req_sending...............: avg=30.58µs  min=5.79µs  med=16.67µs  max=88.09ms  p(90)=20.98µs  p(95)=22.66µs  p(99.9)=620.95µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.96ms min=7.38ms  med=184.79ms max=368.82ms p(90)=195.15ms p(95)=200.07ms p(99.9)=267.85ms
     http_reqs......................: 32564   269.255658/s
     iteration_duration.............: avg=184.91ms min=38.28ms med=185.25ms max=378.74ms p(90)=195.54ms p(95)=200.49ms p(99.9)=270.69ms
     iterations.....................: 32464   268.428808/s
     success_rate...................: 100.00% ✓ 32464      ✗ 0    
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

