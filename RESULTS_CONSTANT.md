## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.7 | 5,485 | 5,511 | 5,423 | 0.6% | 365 MB | 68.2 KB |  |
| fusion-fed-net-11 | 16.7.7 | 5,433 | 5,453 | 5,385 | 0.5% | 373 MB | 70.2 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.17 | 5,396 | 5,403 | 5,279 | 1.0% | 354 MB | 67.1 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.17 | 5,355 | 5,360 | 5,331 | 0.2% | 120 MB | 23.0 KB |  |
| fusion-aot-11 | 16.7.7 | 5,341 | 5,350 | 5,337 | 0.1% | 119 MB | 22.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.17 | 5,329 | 5,356 | 5,316 | 0.3% | 363 MB | 69.8 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.17 | 5,284 | 5,298 | 5,247 | 0.4% | 116 MB | 22.4 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 5,276 | 5,300 | 5,263 | 0.3% | 117 MB | 22.8 KB |  |
| feddi-gateway | 2026-11-03-0517 | 5,037 | 5,054 | 5,024 | 0.3% | 2,280 MB | 463.6 KB |  |
| hive-router-nightly | v0.3.19-nightly.9815b25d | 4,646 | 4,657 | 4,617 | 0.4% | 98 MB | 21.6 KB |  |
| hive-router | v0.3.17 | 4,537 | 4,554 | 4,512 | 0.4% | 99 MB | 22.3 KB |  |
| grafbase | 0.53.5 | 1,835 | 1,836 | 1,832 | 0.1% | 106 MB | 59.2 KB |  |
| caliban | 3.2.1 | 1,600 | 1,602 | 1,598 | 0.1% | 6,326 MB | 4,048.9 KB |  |
| cosmo | 0.373.0 | 1,452 | 1,454 | 1,448 | 0.2% | 168 MB | 118.3 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 602 | 604 | 602 | 0.2% | 2,605 MB | 4,431.4 KB |  |
| apollo-router | v2.19.1 | 533 | 533 | 532 | 0.1% | 172 MB | 331.2 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.a909a280 | 475 | 475 | 474 | 0.1% | 198 MB | 426.6 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 402 | 415 | 400 | 1.6% | 200 MB | 510.2 KB |  |
| hive-gateway | 2.15.10 | 300 | 301 | 299 | 0.3% | 3,196 MB | 10,907.9 KB |  |
| apollo-gateway | 2.14.4 | 273 | 273 | 272 | 0.2% | 2,150 MB | 8,062.8 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1975983     ✗ 0     
     data_received..................: 58 GB   480 MB/s
     data_sent......................: 792 MB  6.6 MB/s
     http_req_blocked...............: avg=2.85µs  min=801ns    med=1.94µs  max=45.08ms  p(90)=2.95µs  p(95)=3.51µs   p(99.9)=26.46µs
     http_req_connecting............: avg=493ns   min=0s       med=0s      max=44.92ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.9ms   min=771.48µs med=8.01ms  max=286.78ms p(90)=14.29ms p(95)=17.35ms  p(99.9)=29.63ms
       { expected_response:true }...: avg=8.9ms   min=771.48µs med=8.01ms  max=286.78ms p(90)=14.29ms p(95)=17.35ms  p(99.9)=29.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 658761
     http_req_receiving.............: avg=90.41µs min=26.03µs  med=46.22µs max=125.75ms p(90)=84.25µs p(95)=186.07µs p(99.9)=5.71ms 
     http_req_sending...............: avg=42.79µs min=4.35µs   med=8.15µs  max=219.86ms p(90)=13.35µs p(95)=96.52µs  p(99.9)=4.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.77ms  min=710.74µs med=7.91ms  max=282.08ms p(90)=14.07ms p(95)=17.1ms   p(99.9)=29.21ms
     http_reqs......................: 658761  5485.002826/s
     iteration_duration.............: avg=9.1ms   min=996.45µs med=8.2ms   max=298.58ms p(90)=14.49ms p(95)=17.57ms  p(99.9)=29.88ms
     iterations.....................: 658661  5484.170202/s
     success_rate...................: 100.00% ✓ 658661      ✗ 0     
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

     checks.........................: 100.00% ✓ 1957572     ✗ 0     
     data_received..................: 57 GB   475 MB/s
     data_sent......................: 784 MB  6.5 MB/s
     http_req_blocked...............: avg=2.54µs  min=821ns    med=1.94µs max=8.13ms   p(90)=3.03µs  p(95)=3.64µs   p(99.9)=27.1µs 
     http_req_connecting............: avg=159ns   min=0s       med=0s     max=3.82ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.98ms  min=785.06µs med=8.05ms max=280.86ms p(90)=14.39ms p(95)=17.6ms   p(99.9)=30.38ms
       { expected_response:true }...: avg=8.98ms  min=785.06µs med=8.05ms max=280.86ms p(90)=14.39ms p(95)=17.6ms   p(99.9)=30.38ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 652624
     http_req_receiving.............: avg=94.16µs min=25.09µs  med=46.3µs max=60.45ms  p(90)=87.23µs p(95)=186.93µs p(99.9)=6.46ms 
     http_req_sending...............: avg=42.48µs min=4.45µs   med=8.25µs max=171.02ms p(90)=13.88µs p(95)=98.41µs  p(99.9)=4.87ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.85ms  min=732.54µs med=7.94ms max=267.57ms p(90)=14.16ms p(95)=17.32ms  p(99.9)=29.78ms
     http_reqs......................: 652624  5433.566174/s
     iteration_duration.............: avg=9.18ms  min=1.15ms   med=8.24ms max=289.58ms p(90)=14.6ms  p(95)=17.82ms  p(99.9)=30.65ms
     iterations.....................: 652524  5432.733601/s
     success_rate...................: 100.00% ✓ 652524      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1944231     ✗ 0     
     data_received..................: 57 GB   472 MB/s
     data_sent......................: 779 MB  6.5 MB/s
     http_req_blocked...............: avg=2.85µs  min=931ns    med=2.34µs  max=6.13ms   p(90)=3.53µs  p(95)=4.15µs   p(99.9)=33.74µs
     http_req_connecting............: avg=135ns   min=0s       med=0s      max=3.73ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.05ms  min=788.39µs med=8.07ms  max=328.06ms p(90)=14.68ms p(95)=18.02ms  p(99.9)=31.19ms
       { expected_response:true }...: avg=9.05ms  min=788.39µs med=8.07ms  max=328.06ms p(90)=14.68ms p(95)=18.02ms  p(99.9)=31.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 648177
     http_req_receiving.............: avg=95.6µs  min=25.98µs  med=47.35µs max=48.97ms  p(90)=88.28µs p(95)=196.63µs p(99.9)=6.15ms 
     http_req_sending...............: avg=43.54µs min=4.38µs   med=8.53µs  max=100.77ms p(90)=14.31µs p(95)=103.27µs p(99.9)=4.97ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.91ms  min=738.61µs med=7.96ms  max=327.84ms p(90)=14.43ms p(95)=17.74ms  p(99.9)=30.73ms
     http_reqs......................: 648177  5396.456593/s
     iteration_duration.............: avg=9.24ms  min=968.5µs  med=8.26ms  max=337.73ms p(90)=14.89ms p(95)=18.24ms  p(99.9)=31.45ms
     iterations.....................: 648077  5395.624034/s
     success_rate...................: 100.00% ✓ 648077      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1929543     ✗ 0     
     data_received..................: 56 GB   469 MB/s
     data_sent......................: 773 MB  6.4 MB/s
     http_req_blocked...............: avg=4.7µs   min=782ns    med=1.85µs  max=136.76ms p(90)=2.9µs   p(95)=3.46µs   p(99.9)=26.47µs
     http_req_connecting............: avg=2.29µs  min=0s       med=0s      max=136.15ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.13ms  min=844.58µs med=8.25ms  max=251.33ms p(90)=14.57ms p(95)=17.59ms  p(99.9)=29.71ms
       { expected_response:true }...: avg=9.13ms  min=844.58µs med=8.25ms  max=251.33ms p(90)=14.57ms p(95)=17.59ms  p(99.9)=29.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 643281
     http_req_receiving.............: avg=88.05µs min=23.89µs  med=44.11µs max=47.2ms   p(90)=84.49µs p(95)=189.25µs p(99.9)=5.59ms 
     http_req_sending...............: avg=42.11µs min=4.23µs   med=7.94µs  max=129.44ms p(90)=13.41µs p(95)=98.4µs   p(99.9)=4.58ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9ms     min=785.46µs med=8.15ms  max=189.19ms p(90)=14.36ms p(95)=17.34ms  p(99.9)=29.36ms
     http_reqs......................: 643281  5355.747373/s
     iteration_duration.............: avg=9.31ms  min=1.3ms    med=8.43ms  max=282.39ms p(90)=14.76ms p(95)=17.8ms   p(99.9)=29.99ms
     iterations.....................: 643181  5354.914805/s
     success_rate...................: 100.00% ✓ 643181      ✗ 0     
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

     checks.........................: 100.00% ✓ 1924569     ✗ 0     
     data_received..................: 56 GB   467 MB/s
     data_sent......................: 771 MB  6.4 MB/s
     http_req_blocked...............: avg=2.64µs  min=821ns    med=1.99µs  max=7.23ms   p(90)=3.11µs  p(95)=3.69µs  p(99.9)=26.81µs
     http_req_connecting............: avg=174ns   min=0s       med=0s      max=4.67ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=9.14ms  min=833.71µs med=8.21ms  max=268.42ms p(90)=14.73ms p(95)=17.93ms p(99.9)=30.14ms
       { expected_response:true }...: avg=9.14ms  min=833.71µs med=8.21ms  max=268.42ms p(90)=14.73ms p(95)=17.93ms p(99.9)=30.14ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 641623
     http_req_receiving.............: avg=93.02µs min=23.89µs  med=45.08µs max=160.69ms p(90)=85.35µs p(95)=192.8µs p(99.9)=6.04ms 
     http_req_sending...............: avg=42.15µs min=4.36µs   med=8.41µs  max=190.45ms p(90)=14.04µs p(95)=101.2µs p(99.9)=4.63ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=9.01ms  min=776.87µs med=8.1ms   max=267.71ms p(90)=14.5ms  p(95)=17.67ms p(99.9)=29.63ms
     http_reqs......................: 641623  5341.920712/s
     iteration_duration.............: avg=9.34ms  min=1.21ms   med=8.4ms   max=277.42ms p(90)=14.93ms p(95)=18.15ms p(99.9)=30.38ms
     iterations.....................: 641523  5341.088148/s
     success_rate...................: 100.00% ✓ 641523      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1919913     ✗ 0     
     data_received..................: 56 GB   466 MB/s
     data_sent......................: 769 MB  6.4 MB/s
     http_req_blocked...............: avg=2.92µs  min=922ns    med=2.39µs  max=9.95ms   p(90)=3.58µs  p(95)=4.23µs   p(99.9)=31.86µs
     http_req_connecting............: avg=146ns   min=0s       med=0s      max=4.11ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.16ms  min=810.16µs med=8.17ms  max=280.51ms p(90)=14.84ms p(95)=18.24ms  p(99.9)=31.31ms
       { expected_response:true }...: avg=9.16ms  min=810.16µs med=8.17ms  max=280.51ms p(90)=14.84ms p(95)=18.24ms  p(99.9)=31.31ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 640071
     http_req_receiving.............: avg=98.35µs min=25.85µs  med=48.67µs max=35.6ms   p(90)=88.84µs p(95)=195.85µs p(99.9)=6.48ms 
     http_req_sending...............: avg=44.62µs min=4.59µs   med=8.62µs  max=193.54ms p(90)=14.21µs p(95)=102.21µs p(99.9)=5.08ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.02ms  min=752.57µs med=8.06ms  max=279.81ms p(90)=14.6ms  p(95)=17.95ms  p(99.9)=30.77ms
     http_reqs......................: 640071  5329.039466/s
     iteration_duration.............: avg=9.36ms  min=975.33µs med=8.36ms  max=289.99ms p(90)=15.06ms p(95)=18.46ms  p(99.9)=31.59ms
     iterations.....................: 639971  5328.206896/s
     success_rate...................: 100.00% ✓ 639971      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1904070     ✗ 0     
     data_received..................: 56 GB   462 MB/s
     data_sent......................: 763 MB  6.4 MB/s
     http_req_blocked...............: avg=3.02µs  min=761ns    med=1.96µs max=129.62ms p(90)=3.12µs  p(95)=3.75µs   p(99.9)=28.08µs
     http_req_connecting............: avg=646ns   min=0s       med=0s     max=129.48ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.25ms  min=856.92µs med=8.34ms max=261.09ms p(90)=14.76ms p(95)=17.92ms  p(99.9)=30.39ms
       { expected_response:true }...: avg=9.25ms  min=856.92µs med=8.34ms max=261.09ms p(90)=14.76ms p(95)=17.92ms  p(99.9)=30.39ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 634790
     http_req_receiving.............: avg=93.35µs min=24.99µs  med=46.4µs max=107.44ms p(90)=88.99µs p(95)=195.38µs p(99.9)=5.87ms 
     http_req_sending...............: avg=43.09µs min=4.33µs   med=8.25µs max=229.05ms p(90)=14.16µs p(95)=101.39µs p(99.9)=4.84ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.11ms  min=786.16µs med=8.23ms max=239.2ms  p(90)=14.55ms p(95)=17.65ms  p(99.9)=29.94ms
     http_reqs......................: 634790  5284.994308/s
     iteration_duration.............: avg=9.44ms  min=1.27ms   med=8.52ms max=288.62ms p(90)=14.97ms p(95)=18.13ms  p(99.9)=30.7ms 
     iterations.....................: 634690  5284.16175/s
     success_rate...................: 100.00% ✓ 634690      ✗ 0     
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

     checks.........................: 100.00% ✓ 1901109     ✗ 0     
     data_received..................: 56 GB   462 MB/s
     data_sent......................: 762 MB  6.3 MB/s
     http_req_blocked...............: avg=2.51µs  min=811ns    med=1.96µs  max=6.07ms   p(90)=3.09µs  p(95)=3.71µs   p(99.9)=28.26µs
     http_req_connecting............: avg=154ns   min=0s       med=0s      max=4.27ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.26ms  min=820.72µs med=8.35ms  max=271.39ms p(90)=14.79ms p(95)=17.9ms   p(99.9)=30.29ms
       { expected_response:true }...: avg=9.26ms  min=820.72µs med=8.35ms  max=271.39ms p(90)=14.79ms p(95)=17.9ms   p(99.9)=30.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 633803
     http_req_receiving.............: avg=91.39µs min=24.87µs  med=46.01µs max=112.93ms p(90)=86.95µs p(95)=191.77µs p(99.9)=5.84ms 
     http_req_sending...............: avg=42.65µs min=4.53µs   med=8.29µs  max=134.89ms p(90)=14.06µs p(95)=101.91µs p(99.9)=4.88ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.12ms  min=782.73µs med=8.24ms  max=270.95ms p(90)=14.57ms p(95)=17.63ms  p(99.9)=29.91ms
     http_reqs......................: 633803  5276.816511/s
     iteration_duration.............: avg=9.45ms  min=1.08ms   med=8.53ms  max=281.37ms p(90)=14.99ms p(95)=18.11ms  p(99.9)=30.53ms
     iterations.....................: 633703  5275.983946/s
     success_rate...................: 100.00% ✓ 633703      ✗ 0     
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

     checks.........................: 100.00% ✓ 1814703     ✗ 0     
     data_received..................: 53 GB   440 MB/s
     data_sent......................: 727 MB  6.1 MB/s
     http_req_blocked...............: avg=4.28µs  min=811ns    med=1.95µs max=226.53ms p(90)=3.08µs  p(95)=3.65µs   p(99.9)=28.4µs 
     http_req_connecting............: avg=1.87µs  min=0s       med=0s     max=226.49ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.71ms  min=691.75µs med=8.69ms max=257.43ms p(90)=14.74ms p(95)=17.98ms  p(99.9)=29.93ms
       { expected_response:true }...: avg=9.71ms  min=691.75µs med=8.69ms max=257.43ms p(90)=14.74ms p(95)=17.98ms  p(99.9)=29.93ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 605001
     http_req_receiving.............: avg=89.77µs min=23.41µs  med=45.8µs max=137.78ms p(90)=86.14µs p(95)=192.84µs p(99.9)=5.85ms 
     http_req_sending...............: avg=42.99µs min=4.44µs   med=8.39µs max=109.61ms p(90)=14.26µs p(95)=103.69µs p(99.9)=4.39ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.58ms  min=654.34µs med=8.59ms max=219.37ms p(90)=14.52ms p(95)=17.72ms  p(99.9)=29.51ms
     http_reqs......................: 605001  5037.362301/s
     iteration_duration.............: avg=9.9ms   min=1.23ms   med=8.87ms max=286.54ms p(90)=14.96ms p(95)=18.19ms  p(99.9)=30.21ms
     iterations.....................: 604901  5036.52968/s
     success_rate...................: 100.00% ✓ 604901      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.19-nightly.9815b25d)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1674231     ✗ 0     
     data_received..................: 49 GB   406 MB/s
     data_sent......................: 671 MB  5.6 MB/s
     http_req_blocked...............: avg=3.16µs  min=812ns    med=2.27µs  max=9.02ms   p(90)=3.7µs   p(95)=4.46µs   p(99.9)=32.76µs
     http_req_connecting............: avg=419ns   min=0s       med=0s      max=8.42ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.54ms min=968.02µs med=9.89ms  max=272.13ms p(90)=14.89ms p(95)=18.31ms  p(99.9)=29.68ms
       { expected_response:true }...: avg=10.54ms min=968.02µs med=9.89ms  max=272.13ms p(90)=14.89ms p(95)=18.31ms  p(99.9)=29.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 558177
     http_req_receiving.............: avg=95.92µs min=23.82µs  med=50.13µs max=133.44ms p(90)=98.72µs p(95)=208.29µs p(99.9)=5.79ms 
     http_req_sending...............: avg=44.48µs min=4.48µs   med=9.11µs  max=150.4ms  p(90)=16.51µs p(95)=112.42µs p(99.9)=4.45ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.4ms  min=890.43µs med=9.79ms  max=270.17ms p(90)=14.63ms p(95)=18.03ms  p(99.9)=29.17ms
     http_reqs......................: 558177  4646.668843/s
     iteration_duration.............: avg=10.74ms min=1.52ms   med=10.08ms max=293.73ms p(90)=15.11ms p(95)=18.53ms  p(99.9)=29.94ms
     iterations.....................: 558077  4645.836371/s
     success_rate...................: 100.00% ✓ 558077      ✗ 0     
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

     checks.........................: 100.00% ✓ 1634796     ✗ 0     
     data_received..................: 48 GB   397 MB/s
     data_sent......................: 655 MB  5.5 MB/s
     http_req_blocked...............: avg=3.24µs   min=972ns    med=2.59µs  max=7.59ms   p(90)=3.99µs   p(95)=4.7µs    p(99.9)=38.11µs
     http_req_connecting............: avg=160ns    min=0s       med=0s      max=3.48ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.79ms  min=948.73µs med=10.13ms max=284.62ms p(90)=15.44ms  p(95)=18.94ms  p(99.9)=30.37ms
       { expected_response:true }...: avg=10.79ms  min=948.73µs med=10.13ms max=284.62ms p(90)=15.44ms  p(95)=18.94ms  p(99.9)=30.37ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 545032
     http_req_receiving.............: avg=103.18µs min=26.02µs  med=52.6µs  max=230.71ms p(90)=102.41µs p(95)=222.84µs p(99.9)=6.4ms  
     http_req_sending...............: avg=46.46µs  min=4.69µs   med=9.53µs  max=101.04ms p(90)=16.46µs  p(95)=116.18µs p(99.9)=4.8ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.64ms  min=874.14µs med=10.03ms max=269.63ms p(90)=15.15ms  p(95)=18.64ms  p(99.9)=29.93ms
     http_reqs......................: 545032  4537.165806/s
     iteration_duration.............: avg=11ms     min=1.42ms   med=10.32ms max=295.41ms p(90)=15.66ms  p(95)=19.18ms  p(99.9)=30.68ms
     iterations.....................: 544932  4536.333347/s
     success_rate...................: 100.00% ✓ 544932      ✗ 0     
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

     checks.........................: 100.00% ✓ 661884      ✗ 0     
     data_received..................: 19 GB   161 MB/s
     data_sent......................: 265 MB  2.2 MB/s
     http_req_blocked...............: avg=3.23µs  min=882ns   med=2.31µs  max=4.03ms   p(90)=4.36µs   p(95)=5.37µs   p(99.9)=31.51µs
     http_req_connecting............: avg=433ns   min=0s      med=0s      max=3.99ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.95ms min=1.88ms  med=26.36ms max=297.41ms p(90)=34.91ms  p(95)=37.73ms  p(99.9)=52.75ms
       { expected_response:true }...: avg=26.95ms min=1.88ms  med=26.36ms max=297.41ms p(90)=34.91ms  p(95)=37.73ms  p(99.9)=52.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 220728
     http_req_receiving.............: avg=83.75µs min=27.03µs med=56.67µs max=223.3ms  p(90)=115.28µs p(95)=170.44µs p(99.9)=1.3ms  
     http_req_sending...............: avg=32.11µs min=4.59µs  med=9.74µs  max=183.16ms p(90)=21.44µs  p(95)=91.83µs  p(99.9)=1.27ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.83ms min=1.8ms   med=26.25ms max=263.14ms p(90)=34.79ms  p(95)=37.6ms   p(99.9)=52.54ms
     http_reqs......................: 220728  1835.335513/s
     iteration_duration.............: avg=27.18ms min=3.24ms  med=26.57ms max=324.72ms p(90)=35.13ms  p(95)=37.95ms  p(99.9)=52.97ms
     iterations.....................: 220628  1834.504021/s
     success_rate...................: 100.00% ✓ 220628      ✗ 0     
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

     checks.........................: 100.00% ✓ 577314      ✗ 0     
     data_received..................: 17 GB   140 MB/s
     data_sent......................: 231 MB  1.9 MB/s
     http_req_blocked...............: avg=4.27µs  min=1.04µs  med=3.39µs  max=4.05ms   p(90)=5.27µs   p(95)=6.08µs   p(99.9)=43.65µs 
     http_req_connecting............: avg=536ns   min=0s      med=0s      max=4ms      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=30.92ms min=2.02ms  med=30.07ms max=295.14ms p(90)=43.52ms  p(95)=47.9ms   p(99.9)=72.37ms 
       { expected_response:true }...: avg=30.92ms min=2.02ms  med=30.07ms max=295.14ms p(90)=43.52ms  p(95)=47.9ms   p(99.9)=72.37ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 192538
     http_req_receiving.............: avg=77.42µs min=27.32µs med=63.99µs max=97.29ms  p(90)=104.23µs p(95)=123.13µs p(99.9)=899.99µs
     http_req_sending...............: avg=27.44µs min=5.21µs  med=13.86µs max=207.52ms p(90)=21.19µs  p(95)=25.67µs  p(99.9)=886.52µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=30.81ms min=1.92ms  med=29.97ms max=294.77ms p(90)=43.41ms  p(95)=47.8ms   p(99.9)=72.15ms 
     http_reqs......................: 192538  1600.952606/s
     iteration_duration.............: avg=31.16ms min=4.8ms   med=30.3ms  max=304.72ms p(90)=43.75ms  p(95)=48.13ms  p(99.9)=72.75ms 
     iterations.....................: 192438  1600.121106/s
     success_rate...................: 100.00% ✓ 192438      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 523830      ✗ 0     
     data_received..................: 15 GB   127 MB/s
     data_sent......................: 210 MB  1.7 MB/s
     http_req_blocked...............: avg=3.38µs  min=1.07µs  med=2.57µs  max=3.67ms   p(90)=4.03µs  p(95)=4.69µs   p(99.9)=31.69µs 
     http_req_connecting............: avg=527ns   min=0s      med=0s      max=3.63ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.12ms min=2.02ms  med=33.14ms max=288.09ms p(90)=49.38ms p(95)=54.43ms  p(99.9)=78.07ms 
       { expected_response:true }...: avg=34.12ms min=2.02ms  med=33.14ms max=288.09ms p(90)=49.38ms p(95)=54.43ms  p(99.9)=78.07ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 174710
     http_req_receiving.............: avg=73.75µs min=27.18µs med=60.94µs max=145.06ms p(90)=97.76µs p(95)=114.48µs p(99.9)=745.64µs
     http_req_sending...............: avg=24.78µs min=5.04µs  med=11.17µs max=161.73ms p(90)=16.91µs p(95)=20.64µs  p(99.9)=774.1µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.02ms min=1.94ms  med=33.05ms max=287.54ms p(90)=49.3ms  p(95)=54.33ms  p(99.9)=77.77ms 
     http_reqs......................: 174710  1452.67364/s
     iteration_duration.............: avg=34.35ms min=4.06ms  med=33.35ms max=304.5ms  p(90)=49.59ms p(95)=54.63ms  p(99.9)=78.67ms 
     iterations.....................: 174610  1451.842163/s
     success_rate...................: 100.00% ✓ 174610      ✗ 0     
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

     checks.........................: 100.00% ✓ 217323     ✗ 0    
     data_received..................: 6.4 GB  53 MB/s
     data_sent......................: 87 MB   723 kB/s
     http_req_blocked...............: avg=3.19µs  min=982ns   med=2.28µs  max=3.15ms   p(90)=3.75µs   p(95)=4.31µs   p(99.9)=40.01µs 
     http_req_connecting............: avg=570ns   min=0s      med=0s      max=1.99ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=82.51ms min=3.5ms   med=79.63ms max=308.35ms p(90)=99.83ms  p(95)=110.42ms p(99.9)=204.99ms
       { expected_response:true }...: avg=82.51ms min=3.5ms   med=79.63ms max=308.35ms p(90)=99.83ms  p(95)=110.42ms p(99.9)=204.99ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 72541
     http_req_receiving.............: avg=73.27µs min=29.11µs med=65.66µs max=14.21ms  p(90)=98.64µs  p(95)=110.68µs p(99.9)=625.85µs
     http_req_sending...............: avg=17.84µs min=4.62µs  med=11.47µs max=61.95ms  p(90)=17.52µs  p(95)=19.25µs  p(99.9)=530.23µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=82.42ms min=3.42ms  med=79.55ms max=297.76ms p(90)=99.74ms  p(95)=110.29ms p(99.9)=204.89ms
     http_reqs......................: 72541   602.163412/s
     iteration_duration.............: avg=82.83ms min=16.04ms med=79.85ms max=314.9ms  p(90)=100.05ms p(95)=110.69ms p(99.9)=205.97ms
     iterations.....................: 72441   601.333312/s
     success_rate...................: 100.00% ✓ 72441      ✗ 0    
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

     checks.........................: 100.00% ✓ 192630     ✗ 0    
     data_received..................: 5.6 GB  47 MB/s
     data_sent......................: 77 MB   641 kB/s
     http_req_blocked...............: avg=4.91µs  min=1.22µs  med=3.19µs  max=4.04ms   p(90)=4.65µs   p(95)=5.25µs   p(99.9)=45.41µs 
     http_req_connecting............: avg=1.49µs  min=0s      med=0s      max=4ms      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.06ms min=4.45ms  med=91.09ms max=326.62ms p(90)=125.34ms p(95)=135.65ms p(99.9)=176.54ms
       { expected_response:true }...: avg=93.06ms min=4.45ms  med=91.09ms max=326.62ms p(90)=125.34ms p(95)=135.65ms p(99.9)=176.54ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64310
     http_req_receiving.............: avg=83.1µs  min=29.03µs med=74.25µs max=159.22ms p(90)=105.67µs p(95)=118.09µs p(99.9)=478.58µs
     http_req_sending...............: avg=21.82µs min=5.31µs  med=14.92µs max=45.69ms  p(90)=20.27µs  p(95)=22.28µs  p(99.9)=549.89µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.96ms min=4.34ms  med=90.98ms max=325.96ms p(90)=125.23ms p(95)=135.56ms p(99.9)=176.1ms 
     http_reqs......................: 64310   533.344221/s
     iteration_duration.............: avg=93.45ms min=23.31ms med=91.38ms max=335.94ms p(90)=125.61ms p(95)=135.93ms p(99.9)=177.36ms
     iterations.....................: 64210   532.514888/s
     success_rate...................: 100.00% ✓ 64210      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-nightly (HotChocolate subgraphs) (v3.0.0-preview.0-nightly.a909a280)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 171675     ✗ 0    
     data_received..................: 5.0 GB  42 MB/s
     data_sent......................: 69 MB   571 kB/s
     http_req_blocked...............: avg=4.32µs   min=1.04µs  med=2.44µs   max=4.22ms   p(90)=3.88µs   p(95)=4.44µs   p(99.9)=70.56µs 
     http_req_connecting............: avg=1.61µs   min=0s      med=0s       max=4.16ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=104.47ms min=4.53ms  med=102.16ms max=332.02ms p(90)=139.19ms p(95)=150.95ms p(99.9)=199.03ms
       { expected_response:true }...: avg=104.47ms min=4.53ms  med=102.16ms max=332.02ms p(90)=139.19ms p(95)=150.95ms p(99.9)=199.03ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 57325
     http_req_receiving.............: avg=73.03µs  min=27.32µs med=65.82µs  max=62.47ms  p(90)=97.05µs  p(95)=109.78µs p(99.9)=460.24µs
     http_req_sending...............: avg=21.59µs  min=4.84µs  med=12.88µs  max=98.52ms  p(90)=18.53µs  p(95)=20.26µs  p(99.9)=506.48µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=104.37ms min=4.44ms  med=102.07ms max=331.63ms p(90)=139.1ms  p(95)=150.86ms p(99.9)=198.94ms
     http_reqs......................: 57325   475.281207/s
     iteration_duration.............: avg=104.87ms min=26.22ms med=102.41ms max=341.7ms  p(90)=139.45ms p(95)=151.19ms p(99.9)=201.66ms
     iterations.....................: 57225   474.452107/s
     success_rate...................: 100.00% ✓ 57225      ✗ 0    
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

     checks.........................: 100.00% ✓ 145608     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 58 MB   484 kB/s
     http_req_blocked...............: avg=4.89µs   min=1.1µs   med=2.84µs   max=3.89ms   p(90)=4.14µs   p(95)=4.66µs   p(99.9)=366.69µs
     http_req_connecting............: avg=1.88µs   min=0s      med=0s       max=3.86ms   p(90)=0s       p(95)=0s       p(99.9)=345.65µs
     http_req_duration..............: avg=123.17ms min=5.28ms  med=120.71ms max=330.29ms p(90)=161.05ms p(95)=173.45ms p(99.9)=225.05ms
       { expected_response:true }...: avg=123.17ms min=5.28ms  med=120.71ms max=330.29ms p(90)=161.05ms p(95)=173.45ms p(99.9)=225.05ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48636
     http_req_receiving.............: avg=77.84µs  min=28.95µs med=74.81µs  max=9.3ms    p(90)=104.43µs p(95)=116.05µs p(99.9)=470.56µs
     http_req_sending...............: avg=22.59µs  min=5.14µs  med=15.04µs  max=80.81ms  p(90)=19.68µs  p(95)=21.33µs  p(99.9)=474.69µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=123.07ms min=5.2ms   med=120.62ms max=330.04ms p(90)=160.96ms p(95)=173.35ms p(99.9)=224.97ms
     http_reqs......................: 48636   402.984756/s
     iteration_duration.............: avg=123.66ms min=40.65ms med=121.02ms max=339.78ms p(90)=161.32ms p(95)=173.74ms p(99.9)=228.91ms
     iterations.....................: 48536   402.156183/s
     success_rate...................: 100.00% ✓ 48536      ✗ 0    
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

     checks.........................: 100.00% ✓ 108555     ✗ 0    
     data_received..................: 3.2 GB  26 MB/s
     data_sent......................: 44 MB   360 kB/s
     http_req_blocked...............: avg=5.65µs   min=1.04µs  med=3.03µs   max=3.68ms   p(90)=4.35µs   p(95)=4.87µs   p(99.9)=1.01ms  
     http_req_connecting............: avg=2.46µs   min=0s      med=0s       max=3.64ms   p(90)=0s       p(95)=0s       p(99.9)=994.29µs
     http_req_duration..............: avg=165.21ms min=5.12ms  med=149.77ms max=798.54ms p(90)=202.7ms  p(95)=228ms    p(99.9)=703.22ms
       { expected_response:true }...: avg=165.21ms min=5.12ms  med=149.77ms max=798.54ms p(90)=202.7ms  p(95)=228ms    p(99.9)=703.22ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 36285
     http_req_receiving.............: avg=86.35µs  min=30.97µs med=82.16µs  max=39.13ms  p(90)=111.03µs p(95)=123.09µs p(99.9)=643.36µs
     http_req_sending...............: avg=25.37µs  min=5.35µs  med=16.08µs  max=51.08ms  p(90)=20.2µs   p(95)=21.87µs  p(99.9)=495.22µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=165.1ms  min=5.04ms  med=149.66ms max=798.42ms p(90)=202.6ms  p(95)=227.81ms p(99.9)=703.14ms
     http_reqs......................: 36285   300.184212/s
     iteration_duration.............: avg=165.9ms  min=52.09ms med=150.15ms max=798.81ms p(90)=203.07ms p(95)=228.36ms p(99.9)=703.44ms
     iterations.....................: 36185   299.356916/s
     success_rate...................: 100.00% ✓ 36185      ✗ 0    
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

     checks.........................: 100.00% ✓ 98925      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   328 kB/s
     http_req_blocked...............: avg=6.43µs   min=1.19µs  med=3.37µs   max=4.11ms   p(90)=4.72µs   p(95)=5.27µs   p(99.9)=1.21ms  
     http_req_connecting............: avg=2.85µs   min=0s      med=0s       max=4.07ms   p(90)=0s       p(95)=0s       p(99.9)=1.19ms  
     http_req_duration..............: avg=181.23ms min=7.64ms  med=180.39ms max=397.61ms p(90)=195.19ms p(95)=200.29ms p(99.9)=264.78ms
       { expected_response:true }...: avg=181.23ms min=7.64ms  med=180.39ms max=397.61ms p(90)=195.19ms p(95)=200.29ms p(99.9)=264.78ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33075
     http_req_receiving.............: avg=91.52µs  min=35.1µs  med=84.94µs  max=61.39ms  p(90)=114.41µs p(95)=125.31µs p(99.9)=437.86µs
     http_req_sending...............: avg=30.74µs  min=5.47µs  med=16.56µs  max=91.21ms  p(90)=21.08µs  p(95)=22.86µs  p(99.9)=478.41µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=181.11ms min=7.52ms  med=180.28ms max=397.14ms p(90)=195.08ms p(95)=200.16ms p(99.9)=264.69ms
     http_reqs......................: 33075   273.410316/s
     iteration_duration.............: avg=182.05ms min=26.01ms med=180.72ms max=409.97ms p(90)=195.47ms p(95)=200.6ms  p(99.9)=266.15ms
     iterations.....................: 32975   272.583678/s
     success_rate...................: 100.00% ✓ 32975      ✗ 0    
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

