## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 4,986 | 5,040 | 4,984 | 0.5% | 392 MB | 80.6 KB |  |
| fusion-net-11 | 16.7.3 | 4,968 | 4,977 | 4,933 | 0.4% | 384 MB | 79.1 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,905 | 4,907 | 4,880 | 0.2% | 374 MB | 78.1 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,889 | 4,917 | 4,873 | 0.4% | 375 MB | 78.6 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,742 | 4,763 | 4,705 | 0.5% | 118 MB | 25.5 KB |  |
| fusion-aot-11 | 16.7.3 | 4,711 | 4,728 | 4,706 | 0.2% | 141 MB | 30.7 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,583 | 4,605 | 4,561 | 0.3% | 138 MB | 30.8 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,575 | 4,594 | 4,558 | 0.3% | 138 MB | 31.0 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,169 | 4,280 | 3,895 | 3.5% | 2,293 MB | 563.2 KB |  |
| hive-router | v0.3.10 | 3,069 | 3,085 | 3,050 | 0.5% | 90 MB | 30.1 KB |  |
| grafbase | 0.53.5 | 1,841 | 1,848 | 1,838 | 0.2% | 104 MB | 57.7 KB |  |
| caliban | 3.2.0 | 1,551 | 1,552 | 1,548 | 0.1% | 5,767 MB | 3,807.6 KB |  |
| cosmo | 0.365.2 | 1,431 | 1,432 | 1,430 | 0.1% | 166 MB | 118.9 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 546 | 546 | 546 | 0.0% | 2,751 MB | 5,159.9 KB |  |
| apollo-router | v2.19.0 | 485 | 489 | 484 | 0.4% | 170 MB | 359.8 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 402 | 406 | 401 | 0.6% | 202 MB | 515.6 KB |  |
| apollo-gateway | 2.14.4 | 269 | 270 | 269 | 0.2% | 2,145 MB | 8,166.3 KB |  |
| hive-gateway | 2.15.6 | 268 | 270 | 267 | 0.4% | 3,423 MB | 13,077.6 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1796439     ✗ 0     
     data_received..................: 52 GB   436 MB/s
     data_sent......................: 720 MB  6.0 MB/s
     http_req_blocked...............: avg=2.7µs   min=822ns    med=2.15µs  max=5.84ms   p(90)=3.37µs  p(95)=4µs      p(99.9)=31.11µs
     http_req_connecting............: avg=159ns   min=0s       med=0s      max=4.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.81ms  min=822.6µs  med=8.99ms  max=300.49ms p(90)=15.07ms p(95)=17.86ms  p(99.9)=30.11ms
       { expected_response:true }...: avg=9.81ms  min=822.6µs  med=8.99ms  max=300.49ms p(90)=15.07ms p(95)=17.86ms  p(99.9)=30.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 598913
     http_req_receiving.............: avg=99.41µs min=25.88µs  med=46.99µs max=240.09ms p(90)=91.37µs p(95)=196.58µs p(99.9)=5.68ms 
     http_req_sending...............: avg=42.41µs min=4.28µs   med=8.25µs  max=211.05ms p(90)=14.85µs p(95)=103.04µs p(99.9)=4.68ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.67ms  min=764.25µs med=8.88ms  max=153.94ms p(90)=14.87ms p(95)=17.61ms  p(99.9)=29.7ms 
     http_reqs......................: 598913  4986.350465/s
     iteration_duration.............: avg=10.01ms min=1.13ms   med=9.18ms  max=317.43ms p(90)=15.28ms p(95)=18.08ms  p(99.9)=30.41ms
     iterations.....................: 598813  4985.517898/s
     success_rate...................: 100.00% ✓ 598813      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1790094     ✗ 0     
     data_received..................: 52 GB   435 MB/s
     data_sent......................: 717 MB  6.0 MB/s
     http_req_blocked...............: avg=2.4µs   min=771ns    med=1.86µs  max=9.3ms    p(90)=2.96µs  p(95)=3.55µs   p(99.9)=26.34µs
     http_req_connecting............: avg=150ns   min=0s       med=0s      max=3.4ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.85ms  min=854.4µs  med=9.08ms  max=271.96ms p(90)=14.97ms p(95)=17.59ms  p(99.9)=29.69ms
       { expected_response:true }...: avg=9.85ms  min=854.4µs  med=9.08ms  max=271.96ms p(90)=14.97ms p(95)=17.59ms  p(99.9)=29.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 596798
     http_req_receiving.............: avg=90.44µs min=25.61µs  med=46.13µs max=228.69ms p(90)=88.83µs p(95)=190.91µs p(99.9)=5.6ms  
     http_req_sending...............: avg=40.94µs min=4.31µs   med=7.93µs  max=219.45ms p(90)=14.16µs p(95)=99.47µs  p(99.9)=4.48ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.72ms  min=793.11µs med=8.97ms  max=271.38ms p(90)=14.77ms p(95)=17.35ms  p(99.9)=29.3ms 
     http_reqs......................: 596798  4968.464276/s
     iteration_duration.............: avg=10.04ms min=1.12ms   med=9.27ms  max=293.22ms p(90)=15.17ms p(95)=17.8ms   p(99.9)=29.95ms
     iterations.....................: 596698  4967.631755/s
     success_rate...................: 100.00% ✓ 596698      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1767648     ✗ 0     
     data_received..................: 52 GB   429 MB/s
     data_sent......................: 708 MB  5.9 MB/s
     http_req_blocked...............: avg=3.19µs   min=842ns    med=2.47µs  max=9.39ms   p(90)=3.85µs  p(95)=4.61µs   p(99.9)=37.19µs
     http_req_connecting............: avg=169ns    min=0s       med=0s      max=3.82ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.96ms   min=972.99µs med=9.04ms  max=270.9ms  p(90)=15.53ms p(95)=18.51ms  p(99.9)=31.51ms
       { expected_response:true }...: avg=9.96ms   min=972.99µs med=9.04ms  max=270.9ms  p(90)=15.53ms p(95)=18.51ms  p(99.9)=31.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 589316
     http_req_receiving.............: avg=106.01µs min=25.25µs  med=48.46µs max=115.01ms p(90)=98.52µs p(95)=203.65µs p(99.9)=7.71ms 
     http_req_sending...............: avg=46.01µs  min=4.34µs   med=8.83µs  max=57.33ms  p(90)=16.54µs p(95)=105.83µs p(99.9)=5.29ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.81ms   min=856.7µs  med=8.92ms  max=270.15ms p(90)=15.29ms p(95)=18.22ms  p(99.9)=30.78ms
     http_reqs......................: 589316  4905.740437/s
     iteration_duration.............: avg=10.17ms  min=1.35ms   med=9.24ms  max=297.48ms p(90)=15.74ms p(95)=18.74ms  p(99.9)=31.82ms
     iterations.....................: 589216  4904.907991/s
     success_rate...................: 100.00% ✓ 589216      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1761816     ✗ 0     
     data_received..................: 51 GB   428 MB/s
     data_sent......................: 706 MB  5.9 MB/s
     http_req_blocked...............: avg=2.54µs   min=771ns    med=1.96µs  max=7.98ms   p(90)=3.2µs   p(95)=3.97µs   p(99.9)=27.75µs
     http_req_connecting............: avg=150ns    min=0s       med=0s      max=3.45ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10ms     min=970.42µs med=9.21ms  max=275.34ms p(90)=15.28ms p(95)=17.97ms  p(99.9)=30.17ms
       { expected_response:true }...: avg=10ms     min=970.42µs med=9.21ms  max=275.34ms p(90)=15.28ms p(95)=17.97ms  p(99.9)=30.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 587372
     http_req_receiving.............: avg=102.48µs min=24.81µs  med=47.16µs max=246.69ms p(90)=95.24µs p(95)=195.12µs p(99.9)=6.53ms 
     http_req_sending...............: avg=42.75µs  min=4.23µs   med=8.19µs  max=96.98ms  p(90)=15.8µs  p(95)=100.91µs p(99.9)=4.86ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.85ms   min=893.86µs med=9.09ms  max=223.38ms p(90)=15.06ms p(95)=17.7ms   p(99.9)=29.6ms 
     http_reqs......................: 587372  4889.463417/s
     iteration_duration.............: avg=10.2ms   min=1.41ms   med=9.4ms   max=286.22ms p(90)=15.49ms p(95)=18.19ms  p(99.9)=30.4ms 
     iterations.....................: 587272  4888.630987/s
     success_rate...................: 100.00% ✓ 587272      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1708869     ✗ 0     
     data_received..................: 50 GB   415 MB/s
     data_sent......................: 685 MB  5.7 MB/s
     http_req_blocked...............: avg=2.75µs  min=792ns    med=1.94µs  max=7.79ms   p(90)=3.1µs   p(95)=3.7µs    p(99.9)=27.87µs
     http_req_connecting............: avg=418ns   min=0s       med=0s      max=7.75ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.33ms min=910.02µs med=9.68ms  max=270.52ms p(90)=15.19ms p(95)=17.67ms  p(99.9)=28.98ms
       { expected_response:true }...: avg=10.33ms min=910.02µs med=9.68ms  max=270.52ms p(90)=15.19ms p(95)=17.67ms  p(99.9)=28.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 569723
     http_req_receiving.............: avg=92.63µs min=24.76µs  med=46.07µs max=60.43ms  p(90)=91.17µs p(95)=201.13µs p(99.9)=5.81ms 
     http_req_sending...............: avg=39.64µs min=4.51µs   med=8.22µs  max=243.65ms p(90)=14.47µs p(95)=101.84µs p(99.9)=3.88ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.2ms  min=838.34µs med=9.57ms  max=269.81ms p(90)=15ms    p(95)=17.44ms  p(99.9)=28.52ms
     http_reqs......................: 569723  4742.959523/s
     iteration_duration.............: avg=10.52ms min=1.22ms   med=9.87ms  max=309.37ms p(90)=15.39ms p(95)=17.88ms  p(99.9)=29.32ms
     iterations.....................: 569623  4742.12702/s
     success_rate...................: 100.00% ✓ 569623      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1697631     ✗ 0     
     data_received..................: 50 GB   412 MB/s
     data_sent......................: 680 MB  5.7 MB/s
     http_req_blocked...............: avg=2.94µs  min=951ns    med=2.35µs  max=5.36ms   p(90)=3.64µs  p(95)=4.29µs   p(99.9)=30.23µs
     http_req_connecting............: avg=173ns   min=0s       med=0s      max=4.14ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.39ms min=911.24µs med=9.65ms  max=253.98ms p(90)=15.61ms p(95)=18.41ms  p(99.9)=30.4ms 
       { expected_response:true }...: avg=10.39ms min=911.24µs med=9.65ms  max=253.98ms p(90)=15.61ms p(95)=18.41ms  p(99.9)=30.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 565977
     http_req_receiving.............: avg=97.28µs min=25.34µs  med=47.61µs max=67.2ms   p(90)=93.42µs p(95)=216.2µs  p(99.9)=5.98ms 
     http_req_sending...............: avg=42.24µs min=4.52µs   med=8.72µs  max=158.19ms p(90)=15.19µs p(95)=108.71µs p(99.9)=4.36ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.25ms min=860.38µs med=9.53ms  max=253.68ms p(90)=15.4ms  p(95)=18.15ms  p(99.9)=29.84ms
     http_reqs......................: 565977  4711.690933/s
     iteration_duration.............: avg=10.59ms min=1.14ms   med=9.84ms  max=288.17ms p(90)=15.82ms p(95)=18.64ms  p(99.9)=30.68ms
     iterations.....................: 565877  4710.858445/s
     success_rate...................: 100.00% ✓ 565877      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1651800     ✗ 0     
     data_received..................: 48 GB   401 MB/s
     data_sent......................: 662 MB  5.5 MB/s
     http_req_blocked...............: avg=7.03µs   min=821ns   med=2.02µs  max=159.21ms p(90)=3.35µs  p(95)=4.1µs    p(99.9)=28.18µs
     http_req_connecting............: avg=4.45µs   min=0s      med=0s      max=159.13ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.67ms  min=1.03ms  med=10.02ms max=266.2ms  p(90)=15.7ms  p(95)=18.33ms  p(99.9)=30.87ms
       { expected_response:true }...: avg=10.67ms  min=1.03ms  med=10.02ms max=266.2ms  p(90)=15.7ms  p(95)=18.33ms  p(99.9)=30.87ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 550700
     http_req_receiving.............: avg=100.07µs min=24.89µs med=46.88µs max=99.39ms  p(90)=97.13µs p(95)=206.83µs p(99.9)=6.27ms 
     http_req_sending...............: avg=42.54µs  min=4.26µs  med=8.41µs  max=149.13ms p(90)=16.81µs p(95)=106.82µs p(99.9)=4.37ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.53ms  min=946.6µs med=9.91ms  max=151.49ms p(90)=15.48ms p(95)=18.07ms  p(99.9)=30.34ms
     http_reqs......................: 550700  4583.678369/s
     iteration_duration.............: avg=10.88ms  min=1.47ms  med=10.22ms max=299.24ms p(90)=15.91ms p(95)=18.54ms  p(99.9)=31.13ms
     iterations.....................: 550600  4582.846033/s
     success_rate...................: 100.00% ✓ 550600      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1648641     ✗ 0     
     data_received..................: 48 GB   400 MB/s
     data_sent......................: 661 MB  5.5 MB/s
     http_req_blocked...............: avg=2.48µs  min=811ns  med=1.91µs  max=8.53ms   p(90)=3.14µs  p(95)=3.88µs   p(99.9)=28.14µs
     http_req_connecting............: avg=107ns   min=0s     med=0s      max=2.76ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.7ms  min=1.05ms med=10.09ms max=269.89ms p(90)=15.69ms p(95)=18.13ms  p(99.9)=30.04ms
       { expected_response:true }...: avg=10.7ms  min=1.05ms med=10.09ms max=269.89ms p(90)=15.69ms p(95)=18.13ms  p(99.9)=30.04ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 549647
     http_req_receiving.............: avg=96.36µs min=25.9µs med=46.61µs max=47ms     p(90)=97.39µs p(95)=204.28µs p(99.9)=6.02ms 
     http_req_sending...............: avg=42.02µs min=4.2µs  med=8.12µs  max=175.38ms p(90)=16.19µs p(95)=103.51µs p(99.9)=4.3ms  
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.57ms min=1ms    med=9.97ms  max=269.26ms p(90)=15.48ms p(95)=17.89ms  p(99.9)=29.56ms
     http_reqs......................: 549647  4575.173463/s
     iteration_duration.............: avg=10.9ms  min=1.62ms med=10.28ms max=280.21ms p(90)=15.89ms p(95)=18.34ms  p(99.9)=30.34ms
     iterations.....................: 549547  4574.341079/s
     success_rate...................: 100.00% ✓ 549547      ✗ 0     
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

     checks.........................: 100.00% ✓ 1502088     ✗ 0     
     data_received..................: 44 GB   364 MB/s
     data_sent......................: 602 MB  5.0 MB/s
     http_req_blocked...............: avg=3.39µs  min=842ns    med=2.53µs  max=9.2ms    p(90)=3.82µs  p(95)=4.44µs   p(99.9)=36.32µs
     http_req_connecting............: avg=483ns   min=0s       med=0s      max=9.14ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.78ms min=777.21µs med=11.71ms max=282.43ms p(90)=17.93ms p(95)=20.06ms  p(99.9)=30.89ms
       { expected_response:true }...: avg=11.78ms min=777.21µs med=11.71ms max=282.43ms p(90)=17.93ms p(95)=20.06ms  p(99.9)=30.89ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 500796
     http_req_receiving.............: avg=86.63µs min=24.32µs  med=48.79µs max=142.67ms p(90)=95.22µs p(95)=216.97µs p(99.9)=3.95ms 
     http_req_sending...............: avg=40.36µs min=4.68µs   med=9.47µs  max=161.01ms p(90)=16.31µs p(95)=116.55µs p(99.9)=2.97ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.65ms min=717.59µs med=11.59ms max=264.37ms p(90)=17.77ms p(95)=19.87ms  p(99.9)=30.57ms
     http_reqs......................: 500796  4169.293883/s
     iteration_duration.............: avg=11.97ms min=1.28ms   med=11.89ms max=295.53ms p(90)=18.12ms p(95)=20.26ms  p(99.9)=31.13ms
     iterations.....................: 500696  4168.461349/s
     success_rate...................: 100.00% ✓ 500696      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1106319     ✗ 0     
     data_received..................: 32 GB   268 MB/s
     data_sent......................: 443 MB  3.7 MB/s
     http_req_blocked...............: avg=2.92µs  min=872ns   med=2.34µs  max=3.44ms   p(90)=3.8µs   p(95)=4.54µs   p(99.9)=36.76µs
     http_req_connecting............: avg=230ns   min=0s      med=0s      max=3.4ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.05ms min=1.37ms  med=16.04ms max=298.73ms p(90)=21.46ms p(95)=22.93ms  p(99.9)=30.24ms
       { expected_response:true }...: avg=16.05ms min=1.37ms  med=16.04ms max=298.73ms p(90)=21.46ms p(95)=22.93ms  p(99.9)=30.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 368873
     http_req_receiving.............: avg=75.47µs min=25.24µs med=51.32µs max=144.79ms p(90)=97.56µs p(95)=186.34µs p(99.9)=1.4ms  
     http_req_sending...............: avg=34.69µs min=4.56µs  med=9.97µs  max=121.13ms p(90)=18.95µs p(95)=109.99µs p(99.9)=1.36ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=15.94ms min=1.33ms  med=15.93ms max=298.22ms p(90)=21.34ms p(95)=22.81ms  p(99.9)=30.09ms
     http_reqs......................: 368873  3069.267109/s
     iteration_duration.............: avg=16.26ms min=3.68ms  med=16.23ms max=308.85ms p(90)=21.65ms p(95)=23.13ms  p(99.9)=30.48ms
     iterations.....................: 368773  3068.435043/s
     success_rate...................: 100.00% ✓ 368773      ✗ 0     
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

     checks.........................: 100.00% ✓ 664101      ✗ 0     
     data_received..................: 19 GB   161 MB/s
     data_sent......................: 266 MB  2.2 MB/s
     http_req_blocked...............: avg=4.78µs  min=972ns   med=2.98µs  max=8.87ms   p(90)=5.06µs   p(95)=6.07µs   p(99.9)=42.45µs
     http_req_connecting............: avg=1.27µs  min=0s      med=0s      max=8.82ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.85ms min=1.87ms  med=26.21ms max=301.72ms p(90)=34.73ms  p(95)=37.59ms  p(99.9)=51.95ms
       { expected_response:true }...: avg=26.85ms min=1.87ms  med=26.21ms max=301.72ms p(90)=34.73ms  p(95)=37.59ms  p(99.9)=51.95ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 221467
     http_req_receiving.............: avg=88.74µs min=26.43µs med=62.8µs  max=124.28ms p(90)=120.77µs p(95)=182.71µs p(99.9)=1.46ms 
     http_req_sending...............: avg=35.73µs min=4.83µs  med=11.51µs max=160.51ms p(90)=22.39µs  p(95)=103.36µs p(99.9)=1.41ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.72ms min=1.82ms  med=26.1ms  max=299.8ms  p(90)=34.6ms   p(95)=37.45ms  p(99.9)=51.65ms
     http_reqs......................: 221467  1841.57954/s
     iteration_duration.............: avg=27.09ms min=7.8ms   med=26.43ms max=321.08ms p(90)=34.95ms  p(95)=37.82ms  p(99.9)=52.3ms 
     iterations.....................: 221367  1840.748003/s
     success_rate...................: 100.00% ✓ 221367      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 559455      ✗ 0     
     data_received..................: 16 GB   136 MB/s
     data_sent......................: 224 MB  1.9 MB/s
     http_req_blocked...............: avg=3.33µs  min=911ns   med=2.49µs  max=4.04ms   p(90)=4.26µs   p(95)=5.02µs   p(99.9)=35.66µs 
     http_req_connecting............: avg=497ns   min=0s      med=0s      max=4ms      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=31.92ms min=2.05ms  med=31.07ms max=275.37ms p(90)=44.97ms  p(95)=49.56ms  p(99.9)=73.92ms 
       { expected_response:true }...: avg=31.92ms min=2.05ms  med=31.07ms max=275.37ms p(90)=44.97ms  p(95)=49.56ms  p(99.9)=73.92ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 186585
     http_req_receiving.............: avg=77.73µs min=27.86µs med=62.69µs max=165.66ms p(90)=102.55µs p(95)=120.28µs p(99.9)=965.22µs
     http_req_sending...............: avg=22.83µs min=4.82µs  med=12µs    max=122.53ms p(90)=19.9µs   p(95)=23.69µs  p(99.9)=812.59µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=31.82ms min=1.98ms  med=30.97ms max=271.86ms p(90)=44.88ms  p(95)=49.46ms  p(99.9)=73.82ms 
     http_reqs......................: 186585  1551.07121/s
     iteration_duration.............: avg=32.16ms min=5.62ms  med=31.29ms max=313.04ms p(90)=45.19ms  p(95)=49.79ms  p(99.9)=74.42ms 
     iterations.....................: 186485  1550.239915/s
     success_rate...................: 100.00% ✓ 186485      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.365.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 516204      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=3.42µs  min=932ns   med=2.58µs  max=3.95ms   p(90)=4.12µs  p(95)=4.81µs   p(99.9)=36.22µs 
     http_req_connecting............: avg=533ns   min=0s      med=0s      max=3.91ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.63ms min=2.05ms  med=33.65ms max=291.06ms p(90)=50.25ms p(95)=55.48ms  p(99.9)=80.77ms 
       { expected_response:true }...: avg=34.63ms min=2.05ms  med=33.65ms max=291.06ms p(90)=50.25ms p(95)=55.48ms  p(99.9)=80.77ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 172168
     http_req_receiving.............: avg=75.34µs min=27.07µs med=61.77µs max=159.44ms p(90)=99.04µs p(95)=115.92µs p(99.9)=710.54µs
     http_req_sending...............: avg=22.66µs min=4.7µs   med=11.04µs max=114.68ms p(90)=17.03µs p(95)=20.78µs  p(99.9)=772.61µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.53ms min=2ms     med=33.56ms max=290.85ms p(90)=50.16ms p(95)=55.39ms  p(99.9)=80.48ms 
     http_reqs......................: 172168  1431.481757/s
     iteration_duration.............: avg=34.86ms min=4.31ms  med=33.86ms max=301.74ms p(90)=50.45ms p(95)=55.69ms  p(99.9)=81.3ms  
     iterations.....................: 172068  1430.650313/s
     success_rate...................: 100.00% ✓ 172068      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 197373     ✗ 0    
     data_received..................: 5.8 GB  48 MB/s
     data_sent......................: 79 MB   657 kB/s
     http_req_blocked...............: avg=4.6µs   min=1.17µs  med=3.06µs  max=4.28ms   p(90)=4.54µs   p(95)=5.18µs   p(99.9)=44.8µs  
     http_req_connecting............: avg=1.26µs  min=0s      med=0s      max=4.18ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=90.84ms min=3.73ms  med=88.98ms max=310.72ms p(90)=111.56ms p(95)=122.7ms  p(99.9)=220.41ms
       { expected_response:true }...: avg=90.84ms min=3.73ms  med=88.98ms max=310.72ms p(90)=111.56ms p(95)=122.7ms  p(99.9)=220.41ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 65891
     http_req_receiving.............: avg=81.4µs  min=29.15µs med=72.59µs max=70.43ms  p(90)=107.34µs p(95)=119.72µs p(99.9)=575.54µs
     http_req_sending...............: avg=23.87µs min=5.32µs  med=14.22µs max=73.01ms  p(90)=19.84µs  p(95)=21.93µs  p(99.9)=635.98µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=90.73ms min=3.67ms  med=88.88ms max=309.79ms p(90)=111.45ms p(95)=122.57ms p(99.9)=220.24ms
     http_reqs......................: 65891   546.633298/s
     iteration_duration.............: avg=91.21ms min=15.86ms med=89.23ms max=321.98ms p(90)=111.82ms p(95)=122.98ms p(99.9)=220.99ms
     iterations.....................: 65791   545.803696/s
     success_rate...................: 100.00% ✓ 65791      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 175350     ✗ 0    
     data_received..................: 5.1 GB  43 MB/s
     data_sent......................: 70 MB   583 kB/s
     http_req_blocked...............: avg=4.29µs   min=1.06µs  med=2.59µs   max=3.53ms   p(90)=4µs      p(95)=4.54µs   p(99.9)=53.03µs 
     http_req_connecting............: avg=1.47µs   min=0s      med=0s       max=3.48ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=102.27ms min=4.36ms  med=100.35ms max=307.21ms p(90)=138.27ms p(95)=149.06ms p(99.9)=196.68ms
       { expected_response:true }...: avg=102.27ms min=4.36ms  med=100.35ms max=307.21ms p(90)=138.27ms p(95)=149.06ms p(99.9)=196.68ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 58550
     http_req_receiving.............: avg=77.12µs  min=28.84µs med=66.91µs  max=146.53ms p(90)=98.31µs  p(95)=110.92µs p(99.9)=487µs   
     http_req_sending...............: avg=18.23µs  min=5.14µs  med=13.15µs  max=82.64ms  p(90)=18.84µs  p(95)=20.69µs  p(99.9)=439.29µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=102.18ms min=4.26ms  med=100.25ms max=306.71ms p(90)=138.18ms p(95)=148.96ms p(99.9)=196.15ms
     http_reqs......................: 58550   485.533272/s
     iteration_duration.............: avg=102.67ms min=13.85ms med=100.61ms max=317.37ms p(90)=138.54ms p(95)=149.31ms p(99.9)=198.64ms
     iterations.....................: 58450   484.704009/s
     success_rate...................: 100.00% ✓ 58450      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 145485     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   484 kB/s
     http_req_blocked...............: avg=5.11µs   min=982ns   med=2.94µs   max=4.05ms   p(90)=4.3µs    p(95)=4.79µs   p(99.9)=675.61µs
     http_req_connecting............: avg=1.98µs   min=0s      med=0s       max=4.01ms   p(90)=0s       p(95)=0s       p(99.9)=596.46µs
     http_req_duration..............: avg=123.27ms min=5.34ms  med=121.04ms max=317.86ms p(90)=161.36ms p(95)=173.73ms p(99.9)=222.93ms
       { expected_response:true }...: avg=123.27ms min=5.34ms  med=121.04ms max=317.86ms p(90)=161.36ms p(95)=173.73ms p(99.9)=222.93ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48595
     http_req_receiving.............: avg=77.41µs  min=28.3µs  med=72.58µs  max=46.98ms  p(90)=101.15µs p(95)=113.14µs p(99.9)=473.14µs
     http_req_sending...............: avg=20.58µs  min=5µs     med=14.25µs  max=75.31ms  p(90)=19.02µs  p(95)=20.65µs  p(99.9)=426.6µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=123.17ms min=5.26ms  med=120.94ms max=302.59ms p(90)=161.27ms p(95)=173.66ms p(99.9)=222.85ms
     http_reqs......................: 48595   402.646748/s
     iteration_duration.............: avg=123.76ms min=29.42ms med=121.34ms max=333.47ms p(90)=161.65ms p(95)=174.03ms p(99.9)=224.8ms 
     iterations.....................: 48495   401.818172/s
     success_rate...................: 100.00% ✓ 48495      ✗ 0    
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

     checks.........................: 100.00% ✓ 97569      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   324 kB/s
     http_req_blocked...............: avg=10.47µs  min=1.09µs  med=3.03µs   max=9.06ms   p(90)=4.32µs   p(95)=4.82µs   p(99.9)=3.33ms  
     http_req_connecting............: avg=7.11µs   min=0s      med=0s       max=8.91ms   p(90)=0s       p(95)=0s       p(99.9)=3.22ms  
     http_req_duration..............: avg=183.77ms min=7.74ms  med=183.77ms max=388.56ms p(90)=194.51ms p(95)=198.63ms p(99.9)=267.26ms
       { expected_response:true }...: avg=183.77ms min=7.74ms  med=183.77ms max=388.56ms p(90)=194.51ms p(95)=198.63ms p(99.9)=267.26ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32623
     http_req_receiving.............: avg=87.22µs  min=29.83µs med=81.08µs  max=65.95ms  p(90)=109.99µs p(95)=120.29µs p(99.9)=406.56µs
     http_req_sending...............: avg=30.14µs  min=4.98µs  med=14.97µs  max=107.94ms p(90)=18.9µs   p(95)=20.5µs   p(99.9)=1.01ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.65ms min=7.66ms  med=183.67ms max=387.48ms p(90)=194.41ms p(95)=198.52ms p(99.9)=266.5ms 
     http_reqs......................: 32623   269.663337/s
     iteration_duration.............: avg=184.58ms min=55.02ms med=184.1ms  max=412.5ms  p(90)=194.77ms p(95)=198.9ms  p(99.9)=269.01ms
     iterations.....................: 32523   268.836732/s
     success_rate...................: 100.00% ✓ 32523      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 97047      ✗ 0    
     data_received..................: 2.8 GB  24 MB/s
     data_sent......................: 39 MB   322 kB/s
     http_req_blocked...............: avg=6.15µs   min=1.12µs  med=3.12µs   max=4.13ms   p(90)=4.42µs   p(95)=4.95µs   p(99.9)=1.33ms  
     http_req_connecting............: avg=2.84µs   min=0s      med=0s       max=4.09ms   p(90)=0s       p(95)=0s       p(99.9)=1.24ms  
     http_req_duration..............: avg=184.83ms min=5.66ms  med=167.91ms max=763.99ms p(90)=213.15ms p(95)=247.61ms p(99.9)=675.73ms
       { expected_response:true }...: avg=184.83ms min=5.66ms  med=167.91ms max=763.99ms p(90)=213.15ms p(95)=247.61ms p(99.9)=675.73ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32449
     http_req_receiving.............: avg=92.5µs   min=32.16µs med=85.16µs  max=87.42ms  p(90)=113.41µs p(95)=124.34µs p(99.9)=612.29µs
     http_req_sending...............: avg=22.44µs  min=5.39µs  med=16.58µs  max=26.02ms  p(90)=20.58µs  p(95)=22.22µs  p(99.9)=561.92µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.72ms min=5.56ms  med=167.8ms  max=763.89ms p(90)=213.04ms p(95)=247.17ms p(99.9)=675.63ms
     http_reqs......................: 32449   268.265652/s
     iteration_duration.............: avg=185.64ms min=51.38ms med=168.24ms max=764.23ms p(90)=213.48ms p(95)=248.5ms  p(99.9)=676.13ms
     iterations.....................: 32349   267.438922/s
     success_rate...................: 100.00% ✓ 32349      ✗ 0    
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

