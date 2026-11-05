## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 3,418 | 3,429 | 3,401 | 0.4% | 375 MB | 112.3 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 3,410 | 3,418 | 3,404 | 0.1% | 368 MB | 110.4 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 3,379 | 3,386 | 3,371 | 0.2% | 134 MB | 40.5 KB |  |
| fusion-aot-11 | 16.7.3 | 3,352 | 3,368 | 3,333 | 0.4% | 133 MB | 40.7 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,248 | 3,286 | 3,222 | 0.8% | 2,301 MB | 725.3 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 2,804 | 2,807 | 2,796 | 0.2% | 406 MB | 148.3 KB |  |
| fusion-fed-net-11 | 16.7.3 | 2,791 | 2,794 | 2,768 | 0.4% | 382 MB | 140.3 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 2,742 | 2,747 | 2,713 | 0.5% | 136 MB | 50.9 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 2,735 | 2,751 | 2,725 | 0.4% | 143 MB | 53.6 KB |  |
| hive-router | v0.3.10 | 2,049 | 2,059 | 2,031 | 0.6% | 90 MB | 44.8 KB |  |
| caliban | 3.2.0 | 1,478 | 1,480 | 1,473 | 0.2% | 4,944 MB | 3,425.4 KB |  |
| grafbase | 0.53.5 | 1,451 | 1,464 | 1,445 | 0.5% | 101 MB | 71.2 KB |  |
| cosmo | 0.365.2 | 1,373 | 1,375 | 1,370 | 0.2% | 153 MB | 114.4 KB |  |
| apollo-router | v2.19.0 | 532 | 532 | 531 | 0.1% | 178 MB | 342.8 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 524 | 525 | 523 | 0.1% | 2,766 MB | 5,405.5 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 390 | 390 | 389 | 0.1% | 205 MB | 538.5 KB |  |
| apollo-gateway | 2.14.4 | 269 | 270 | 268 | 0.4% | 2,154 MB | 8,199.6 KB |  |
| hive-gateway | 2.15.6 | 269 | 269 | 268 | 0.2% | 3,689 MB | 14,041.4 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1239960     ✗ 0     
     data_received..................: 36 GB   299 MB/s
     data_sent......................: 497 MB  4.1 MB/s
     http_req_blocked...............: avg=2.9µs   min=922ns  med=2.3µs   max=4.07ms   p(90)=3.62µs  p(95)=4.33µs   p(99.9)=31.83µs
     http_req_connecting............: avg=241ns   min=0s     med=0s      max=4.03ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.3ms  min=8.14ms med=13.85ms max=317.03ms p(90)=17.85ms p(95)=19.27ms  p(99.9)=27.53ms
       { expected_response:true }...: avg=14.3ms  min=8.14ms med=13.85ms max=317.03ms p(90)=17.85ms p(95)=19.27ms  p(99.9)=27.53ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 413420
     http_req_receiving.............: avg=77.84µs min=23µs   med=44.47µs max=178.63ms p(90)=93.29µs p(95)=182.09µs p(99.9)=2.24ms 
     http_req_sending...............: avg=33.41µs min=4.49µs med=8.53µs  max=220.55ms p(90)=16.89µs p(95)=98.34µs  p(99.9)=2.08ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.19ms min=8.07ms med=13.75ms max=138.52ms p(90)=17.74ms p(95)=19.15ms  p(99.9)=27.26ms
     http_reqs......................: 413420  3418.015454/s
     iteration_duration.............: avg=14.5ms  min=8.32ms med=14.05ms max=339.43ms p(90)=18.05ms p(95)=19.47ms  p(99.9)=27.75ms
     iterations.....................: 413320  3417.188688/s
     success_rate...................: 100.00% ✓ 413320      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1237347     ✗ 0     
     data_received..................: 36 GB   298 MB/s
     data_sent......................: 496 MB  4.1 MB/s
     http_req_blocked...............: avg=2.36µs  min=781ns   med=1.77µs  max=3.98ms   p(90)=3.04µs  p(95)=3.83µs  p(99.9)=23.77µs
     http_req_connecting............: avg=208ns   min=0s      med=0s      max=3.36ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=14.34ms min=8.18ms  med=13.93ms max=280.14ms p(90)=17.81ms p(95)=19.14ms p(99.9)=26.77ms
       { expected_response:true }...: avg=14.34ms min=8.18ms  med=13.93ms max=280.14ms p(90)=17.81ms p(95)=19.14ms p(99.9)=26.77ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 412549
     http_req_receiving.............: avg=68.44µs min=24.84µs med=43.1µs  max=126.42ms p(90)=90.33µs p(95)=164.4µs p(99.9)=1.86ms 
     http_req_sending...............: avg=30.99µs min=4.16µs  med=7.55µs  max=191.52ms p(90)=16.12µs p(95)=89.4µs  p(99.9)=1.97ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=14.24ms min=8.13ms  med=13.83ms max=279.61ms p(90)=17.71ms p(95)=19.03ms p(99.9)=26.51ms
     http_reqs......................: 412549  3410.810605/s
     iteration_duration.............: avg=14.53ms min=8.31ms  med=14.12ms max=289.19ms p(90)=18ms    p(95)=19.33ms p(99.9)=26.97ms
     iterations.....................: 412449  3409.98384/s
     success_rate...................: 100.00% ✓ 412449      ✗ 0     
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

     checks.........................: 100.00% ✓ 1226028     ✗ 0     
     data_received..................: 36 GB   296 MB/s
     data_sent......................: 491 MB  4.1 MB/s
     http_req_blocked...............: avg=2.35µs  min=812ns   med=1.77µs  max=3.33ms   p(90)=3µs     p(95)=3.75µs   p(99.9)=26.85µs
     http_req_connecting............: avg=203ns   min=0s      med=0s      max=3.29ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.48ms min=8.49ms  med=14.06ms max=289.57ms p(90)=17.84ms p(95)=19.2ms   p(99.9)=27.44ms
       { expected_response:true }...: avg=14.48ms min=8.49ms  med=14.06ms max=289.57ms p(90)=17.84ms p(95)=19.2ms   p(99.9)=27.44ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 408776
     http_req_receiving.............: avg=66.58µs min=23.63µs med=41.66µs max=56.63ms  p(90)=90.41µs p(95)=165.13µs p(99.9)=1.83ms 
     http_req_sending...............: avg=30.02µs min=4.16µs  med=7.63µs  max=142.51ms p(90)=16.36µs p(95)=89.97µs  p(99.9)=1.69ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.38ms min=8.3ms   med=13.97ms max=286.46ms p(90)=17.74ms p(95)=19.09ms  p(99.9)=27.16ms
     http_reqs......................: 408776  3379.435383/s
     iteration_duration.............: avg=14.67ms min=8.67ms  med=14.25ms max=297.5ms  p(90)=18.03ms p(95)=19.4ms   p(99.9)=27.63ms
     iterations.....................: 408676  3378.608662/s
     success_rate...................: 100.00% ✓ 408676      ✗ 0     
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

     checks.........................: 100.00% ✓ 1216476     ✗ 0     
     data_received..................: 36 GB   293 MB/s
     data_sent......................: 487 MB  4.0 MB/s
     http_req_blocked...............: avg=3.07µs  min=862ns   med=2.22µs  max=6.55ms   p(90)=3.61µs  p(95)=4.37µs   p(99.9)=30.43µs
     http_req_connecting............: avg=435ns   min=0s      med=0s      max=6.49ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.59ms min=8.42ms  med=14.14ms max=295.37ms p(90)=18.08ms p(95)=19.51ms  p(99.9)=28.39ms
       { expected_response:true }...: avg=14.59ms min=8.42ms  med=14.14ms max=295.37ms p(90)=18.08ms p(95)=19.51ms  p(99.9)=28.39ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 405592
     http_req_receiving.............: avg=81.66µs min=23.98µs med=44.94µs max=183.84ms p(90)=95.12µs p(95)=187.67µs p(99.9)=2.26ms 
     http_req_sending...............: avg=32.45µs min=4.31µs  med=8.38µs  max=173.88ms p(90)=17.36µs p(95)=99.51µs  p(99.9)=1.92ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.47ms min=8.34ms  med=14.04ms max=111.45ms p(90)=17.97ms p(95)=19.38ms  p(99.9)=28.18ms
     http_reqs......................: 405592  3352.845676/s
     iteration_duration.............: avg=14.78ms min=8.6ms   med=14.34ms max=304.94ms p(90)=18.27ms p(95)=19.7ms   p(99.9)=28.61ms
     iterations.....................: 405492  3352.019021/s
     success_rate...................: 100.00% ✓ 405492      ✗ 0     
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

     checks.........................: 100.00% ✓ 1178454     ✗ 0     
     data_received..................: 34 GB   284 MB/s
     data_sent......................: 472 MB  3.9 MB/s
     http_req_blocked...............: avg=3.09µs  min=962ns  med=2.45µs  max=3.95ms   p(90)=4µs     p(95)=4.81µs   p(99.9)=34.58µs
     http_req_connecting............: avg=260ns   min=0s     med=0s      max=3.91ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=15.05ms min=8.68ms med=14.68ms max=305.97ms p(90)=18.28ms p(95)=19.59ms  p(99.9)=27.47ms
       { expected_response:true }...: avg=15.05ms min=8.68ms med=14.68ms max=305.97ms p(90)=18.28ms p(95)=19.59ms  p(99.9)=27.47ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 392918
     http_req_receiving.............: avg=74.85µs min=23.9µs med=47.44µs max=146.71ms p(90)=98.25µs p(95)=190.14µs p(99.9)=1.8ms  
     http_req_sending...............: avg=33.87µs min=4.61µs med=9.15µs  max=77.53ms  p(90)=18.17µs p(95)=104.46µs p(99.9)=1.89ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.94ms min=8.47ms med=14.58ms max=293.49ms p(90)=18.17ms p(95)=19.45ms  p(99.9)=27.24ms
     http_reqs......................: 392918  3248.231293/s
     iteration_duration.............: avg=15.26ms min=8.89ms med=14.89ms max=324.4ms  p(90)=18.48ms p(95)=19.78ms  p(99.9)=27.67ms
     iterations.....................: 392818  3247.404599/s
     success_rate...................: 100.00% ✓ 392818      ✗ 0     
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

     checks.........................: 100.00% ✓ 1021035     ✗ 0     
     data_received..................: 30 GB   245 MB/s
     data_sent......................: 409 MB  3.4 MB/s
     http_req_blocked...............: avg=2.94µs  min=832ns   med=1.87µs  max=8.73ms   p(90)=3.24µs  p(95)=4.02µs   p(99.9)=24.4µs 
     http_req_connecting............: avg=637ns   min=0s      med=0s      max=8.7ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.41ms min=11.65ms med=16.99ms max=253.28ms p(90)=20.39ms p(95)=21.63ms  p(99.9)=28.78ms
       { expected_response:true }...: avg=17.41ms min=11.65ms med=16.99ms max=253.28ms p(90)=20.39ms p(95)=21.63ms  p(99.9)=28.78ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 340445
     http_req_receiving.............: avg=67.73µs min=24.44µs med=44.95µs max=80.78ms  p(90)=94.14µs p(95)=149.67µs p(99.9)=1.49ms 
     http_req_sending...............: avg=29.74µs min=4.38µs  med=7.97µs  max=232.05ms p(90)=17µs    p(95)=82.87µs  p(99.9)=1.51ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.31ms min=11.6ms  med=16.9ms  max=249.95ms p(90)=20.28ms p(95)=21.51ms  p(99.9)=28.51ms
     http_reqs......................: 340445  2804.552451/s
     iteration_duration.............: avg=17.62ms min=11.82ms med=17.18ms max=301.21ms p(90)=20.59ms p(95)=21.82ms  p(99.9)=29.02ms
     iterations.....................: 340345  2803.728661/s
     success_rate...................: 100.00% ✓ 340345      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 1016352     ✗ 0     
     data_received..................: 30 GB   244 MB/s
     data_sent......................: 407 MB  3.4 MB/s
     http_req_blocked...............: avg=2.59µs  min=801ns   med=1.84µs  max=6.63ms   p(90)=3.12µs  p(95)=3.84µs   p(99.9)=25.32µs
     http_req_connecting............: avg=388ns   min=0s      med=0s      max=6.6ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.49ms min=11.6ms  med=17.07ms max=282.59ms p(90)=20.51ms p(95)=21.76ms  p(99.9)=28.24ms
       { expected_response:true }...: avg=17.49ms min=11.6ms  med=17.07ms max=282.59ms p(90)=20.51ms p(95)=21.76ms  p(99.9)=28.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 338884
     http_req_receiving.............: avg=65.97µs min=24.01µs med=43.9µs  max=227.66ms p(90)=91.37µs p(95)=142.78µs p(99.9)=1.31ms 
     http_req_sending...............: avg=27.37µs min=4.03µs  med=7.9µs   max=129.79ms p(90)=16.18µs p(95)=78.72µs  p(99.9)=1.32ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.4ms  min=11.55ms med=16.98ms max=282.47ms p(90)=20.41ms p(95)=21.65ms  p(99.9)=27.99ms
     http_reqs......................: 338884  2791.695681/s
     iteration_duration.............: avg=17.7ms  min=11.76ms med=17.26ms max=290.28ms p(90)=20.7ms  p(95)=21.95ms  p(99.9)=28.46ms
     iterations.....................: 338784  2790.87189/s
     success_rate...................: 100.00% ✓ 338784      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 998565      ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 400 MB  3.3 MB/s
     http_req_blocked...............: avg=2.48µs  min=801ns   med=1.83µs  max=6.94ms   p(90)=3.14µs  p(95)=3.92µs   p(99.9)=27.33µs
     http_req_connecting............: avg=269ns   min=0s      med=0s      max=3.85ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.81ms min=12.03ms med=17.42ms max=291.13ms p(90)=20.74ms p(95)=21.94ms  p(99.9)=28.87ms
       { expected_response:true }...: avg=17.81ms min=12.03ms med=17.42ms max=291.13ms p(90)=20.74ms p(95)=21.94ms  p(99.9)=28.87ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 332955
     http_req_receiving.............: avg=64.55µs min=24.23µs med=43.76µs max=101.35ms p(90)=89.82µs p(95)=139.58µs p(99.9)=1.23ms 
     http_req_sending...............: avg=28.29µs min=4.2µs   med=7.78µs  max=163.05ms p(90)=15.74µs p(95)=79.23µs  p(99.9)=1.35ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.72ms min=11.98ms med=17.34ms max=290.97ms p(90)=20.63ms p(95)=21.84ms  p(99.9)=28.64ms
     http_reqs......................: 332955  2742.370559/s
     iteration_duration.............: avg=18.01ms min=12.23ms med=17.62ms max=302.27ms p(90)=20.93ms p(95)=22.14ms  p(99.9)=29.1ms 
     iterations.....................: 332855  2741.546913/s
     success_rate...................: 100.00% ✓ 332855      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 995991      ✗ 0     
     data_received..................: 29 GB   239 MB/s
     data_sent......................: 399 MB  3.3 MB/s
     http_req_blocked...............: avg=2.48µs  min=811ns   med=1.9µs   max=3.46ms   p(90)=3.27µs  p(95)=4.04µs   p(99.9)=25.72µs
     http_req_connecting............: avg=203ns   min=0s      med=0s      max=3.22ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.85ms min=11.84ms med=17.44ms max=278.12ms p(90)=20.91ms p(95)=22.15ms  p(99.9)=29.01ms
       { expected_response:true }...: avg=17.85ms min=11.84ms med=17.44ms max=278.12ms p(90)=20.91ms p(95)=22.15ms  p(99.9)=29.01ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 332097
     http_req_receiving.............: avg=66.49µs min=24.61µs med=45.43µs max=19.19ms  p(90)=92.39µs p(95)=141.83µs p(99.9)=1.32ms 
     http_req_sending...............: avg=26.99µs min=4.41µs  med=8.07µs  max=98.75ms  p(90)=16.64µs p(95)=78.25µs  p(99.9)=1.37ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.76ms min=11.78ms med=17.35ms max=266.98ms p(90)=20.81ms p(95)=22.03ms  p(99.9)=28.75ms
     http_reqs......................: 332097  2735.274907/s
     iteration_duration.............: avg=18.06ms min=12ms    med=17.64ms max=288.47ms p(90)=21.11ms p(95)=22.35ms  p(99.9)=29.24ms
     iterations.....................: 331997  2734.45127/s
     success_rate...................: 100.00% ✓ 331997      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 748878      ✗ 0     
     data_received..................: 22 GB   179 MB/s
     data_sent......................: 300 MB  2.5 MB/s
     http_req_blocked...............: avg=2.76µs  min=812ns   med=2.02µs  max=3.92ms   p(90)=3.52µs  p(95)=4.23µs   p(99.9)=30.1µs  
     http_req_connecting............: avg=397ns   min=0s      med=0s      max=3.87ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.82ms min=17.11ms med=23.46ms max=301.22ms p(90)=26.95ms p(95)=28.05ms  p(99.9)=33.47ms 
       { expected_response:true }...: avg=23.82ms min=17.11ms med=23.46ms max=301.22ms p(90)=26.95ms p(95)=28.05ms  p(99.9)=33.47ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 249726
     http_req_receiving.............: avg=64.09µs min=24.17µs med=48.74µs max=128.14ms p(90)=89.57µs p(95)=112.97µs p(99.9)=862.69µs
     http_req_sending...............: avg=25.35µs min=4.33µs  med=8.76µs  max=117.93ms p(90)=16.59µs p(95)=23.08µs  p(99.9)=903.23µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.73ms min=17.07ms med=23.37ms max=300.95ms p(90)=26.86ms p(95)=27.96ms  p(99.9)=33.28ms 
     http_reqs......................: 249726  2049.137065/s
     iteration_duration.............: avg=24.02ms min=17.23ms med=23.66ms max=310.26ms p(90)=27.15ms p(95)=28.25ms  p(99.9)=33.64ms 
     iterations.....................: 249626  2048.31651/s
     success_rate...................: 100.00% ✓ 249626      ✗ 0     
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

     checks.........................: 100.00% ✓ 540624      ✗ 0     
     data_received..................: 16 GB   129 MB/s
     data_sent......................: 217 MB  1.8 MB/s
     http_req_blocked...............: avg=4.04µs  min=1.14µs  med=3.18µs  max=4.1ms    p(90)=5.01µs   p(95)=5.84µs   p(99.9)=38.12µs 
     http_req_connecting............: avg=528ns   min=0s      med=0s      max=4.06ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.04ms min=17.9ms  med=32.54ms max=293.54ms p(90)=38.48ms  p(95)=40.54ms  p(99.9)=56.9ms  
       { expected_response:true }...: avg=33.04ms min=17.9ms  med=32.54ms max=293.54ms p(90)=38.48ms  p(95)=40.54ms  p(99.9)=56.9ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 180308
     http_req_receiving.............: avg=79.95µs min=27.48µs med=65.54µs max=136.16ms p(90)=108.13µs p(95)=129.22µs p(99.9)=970.53µs
     http_req_sending...............: avg=27.43µs min=5.07µs  med=13.34µs max=231.97ms p(90)=21.2µs   p(95)=25.75µs  p(99.9)=859.47µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.93ms min=17.75ms med=32.44ms max=284.77ms p(90)=38.38ms  p(95)=40.43ms  p(99.9)=56.54ms 
     http_reqs......................: 180308  1478.501259/s
     iteration_duration.............: avg=33.28ms min=21.53ms med=32.77ms max=312.47ms p(90)=38.71ms  p(95)=40.77ms  p(99.9)=57.2ms  
     iterations.....................: 180208  1477.681272/s
     success_rate...................: 100.00% ✓ 180208      ✗ 0     
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

     checks.........................: 100.00% ✓ 530493      ✗ 0     
     data_received..................: 16 GB   127 MB/s
     data_sent......................: 213 MB  1.7 MB/s
     http_req_blocked...............: avg=3.27µs  min=841ns   med=2.24µs  max=3.62ms   p(90)=4.55µs   p(95)=5.46µs   p(99.9)=41.57µs
     http_req_connecting............: avg=498ns   min=0s      med=0s      max=3.59ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.67ms min=17.48ms med=33.37ms max=303.74ms p(90)=39.25ms  p(95)=40.99ms  p(99.9)=49.3ms 
       { expected_response:true }...: avg=33.67ms min=17.48ms med=33.37ms max=303.74ms p(90)=39.25ms  p(95)=40.99ms  p(99.9)=49.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 176931
     http_req_receiving.............: avg=79.44µs min=25.9µs  med=54.91µs max=179.03ms p(90)=116.97µs p(95)=156.68µs p(99.9)=1.41ms 
     http_req_sending...............: avg=27.46µs min=4.38µs  med=9.27µs  max=74.94ms  p(90)=22µs     p(95)=33.62µs  p(99.9)=1.31ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.56ms min=17.39ms med=33.27ms max=303.21ms p(90)=39.15ms  p(95)=40.87ms  p(99.9)=49.19ms
     http_reqs......................: 176931  1451.118881/s
     iteration_duration.............: avg=33.92ms min=20.13ms med=33.6ms  max=318.31ms p(90)=39.47ms  p(95)=41.21ms  p(99.9)=49.57ms
     iterations.....................: 176831  1450.29872/s
     success_rate...................: 100.00% ✓ 176831      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 502287      ✗ 0     
     data_received..................: 15 GB   120 MB/s
     data_sent......................: 201 MB  1.7 MB/s
     http_req_blocked...............: avg=4.68µs  min=1.09µs  med=2.65µs  max=9.1ms    p(90)=4.2µs    p(95)=4.9µs    p(99.9)=34.57µs 
     http_req_connecting............: avg=1.68µs  min=0s      med=0s      max=9.05ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.6ms  min=18.42ms med=35.04ms max=281.31ms p(90)=42.6ms   p(95)=44.99ms  p(99.9)=57.26ms 
       { expected_response:true }...: avg=35.6ms  min=18.42ms med=35.04ms max=281.31ms p(90)=42.6ms   p(95)=44.99ms  p(99.9)=57.26ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 167529
     http_req_receiving.............: avg=76.49µs min=26.08µs med=62.7µs  max=143.57ms p(90)=101.76µs p(95)=120.56µs p(99.9)=736.74µs
     http_req_sending...............: avg=23.03µs min=5.13µs  med=11.07µs max=217.69ms p(90)=17.1µs   p(95)=21µs     p(99.9)=804.66µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=35.5ms  min=18.31ms med=34.94ms max=279.87ms p(90)=42.51ms  p(95)=44.9ms   p(99.9)=56.94ms 
     http_reqs......................: 167529  1373.711646/s
     iteration_duration.............: avg=35.82ms min=20.12ms med=35.24ms max=316.59ms p(90)=42.8ms   p(95)=45.2ms   p(99.9)=57.86ms 
     iterations.....................: 167429  1372.891662/s
     success_rate...................: 100.00% ✓ 167429      ✗ 0     
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

     checks.........................: 100.00% ✓ 194988     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   640 kB/s
     http_req_blocked...............: avg=5.19µs  min=1.29µs  med=3.44µs  max=3.69ms   p(90)=4.98µs   p(95)=5.61µs   p(99.9)=51.94µs 
     http_req_connecting............: avg=1.5µs   min=0s      med=0s      max=3.63ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=91.95ms min=19.89ms med=90.21ms max=315.58ms p(90)=115.77ms p(95)=123.97ms p(99.9)=163.88ms
       { expected_response:true }...: avg=91.95ms min=19.89ms med=90.21ms max=315.58ms p(90)=115.77ms p(95)=123.97ms p(99.9)=163.88ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 65096
     http_req_receiving.............: avg=83.25µs min=29.65µs med=75.91µs max=102.32ms p(90)=107.33µs p(95)=119.25µs p(99.9)=576.59µs
     http_req_sending...............: avg=27.9µs  min=4.93µs  med=15.41µs max=156.52ms p(90)=20.94µs  p(95)=23.08µs  p(99.9)=558.83µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.84ms min=19.78ms med=90.1ms  max=308.52ms p(90)=115.66ms p(95)=123.88ms p(99.9)=162.99ms
     http_reqs......................: 65096   532.719076/s
     iteration_duration.............: avg=92.33ms min=26.87ms med=90.48ms max=336.9ms  p(90)=116.05ms p(95)=124.25ms p(99.9)=164.88ms
     iterations.....................: 64996   531.900717/s
     success_rate...................: 100.00% ✓ 64996      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 191973     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   630 kB/s
     http_req_blocked...............: avg=4.11µs  min=1µs     med=2.44µs  max=4.08ms   p(90)=3.87µs   p(95)=4.44µs   p(99.9)=43.92µs 
     http_req_connecting............: avg=1.4µs   min=0s      med=0s      max=4.04ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.43ms min=20.33ms med=91.48ms max=336.53ms p(90)=111.95ms p(95)=120.6ms  p(99.9)=216.12ms
       { expected_response:true }...: avg=93.43ms min=20.33ms med=91.48ms max=336.53ms p(90)=111.95ms p(95)=120.6ms  p(99.9)=216.12ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64091
     http_req_receiving.............: avg=77.87µs min=29.25µs med=67.71µs max=97.05ms  p(90)=101.36µs p(95)=113.27µs p(99.9)=573.96µs
     http_req_sending...............: avg=21.41µs min=5.06µs  med=12.38µs max=225.42ms p(90)=18.23µs  p(95)=20.13µs  p(99.9)=512.46µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.33ms min=20.2ms  med=91.39ms max=335.98ms p(90)=111.87ms p(95)=120.5ms  p(99.9)=215.84ms
     http_reqs......................: 64091   524.305147/s
     iteration_duration.............: avg=93.78ms min=31.71ms med=91.73ms max=344.28ms p(90)=112.18ms p(95)=120.89ms p(99.9)=217.8ms 
     iterations.....................: 63991   523.487084/s
     success_rate...................: 100.00% ✓ 63991      ✗ 0    
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

     checks.........................: 100.00% ✓ 142980     ✗ 0    
     data_received..................: 4.2 GB  34 MB/s
     data_sent......................: 57 MB   469 kB/s
     http_req_blocked...............: avg=5.74µs   min=1.1µs   med=3.36µs   max=4.39ms   p(90)=4.78µs   p(95)=5.37µs   p(99.9)=603.52µs
     http_req_connecting............: avg=2.17µs   min=0s      med=0s       max=4.35ms   p(90)=0s       p(95)=0s       p(99.9)=570.68µs
     http_req_duration..............: avg=125.43ms min=21.03ms med=123.69ms max=326.7ms  p(90)=155.75ms p(95)=166.15ms p(99.9)=210.27ms
       { expected_response:true }...: avg=125.43ms min=21.03ms med=123.69ms max=326.7ms  p(90)=155.75ms p(95)=166.15ms p(99.9)=210.27ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 47760
     http_req_receiving.............: avg=85.64µs  min=31.78µs med=76.62µs  max=175.65ms p(90)=108.42µs p(95)=120.59µs p(99.9)=496.24µs
     http_req_sending...............: avg=25.8µs   min=5.3µs   med=15.91µs  max=175.35ms p(90)=21.16µs  p(95)=23.07µs  p(99.9)=574.99µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=125.32ms min=20.95ms med=123.58ms max=325.88ms p(90)=155.63ms p(95)=166.01ms p(99.9)=209.49ms
     http_reqs......................: 47760   390.427787/s
     iteration_duration.............: avg=125.92ms min=44.11ms med=123.98ms max=355.37ms p(90)=156.01ms p(95)=166.44ms p(99.9)=212.66ms
     iterations.....................: 47660   389.610308/s
     success_rate...................: 100.00% ✓ 47660      ✗ 0    
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

     checks.........................: 100.00% ✓ 98850      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   324 kB/s
     http_req_blocked...............: avg=6.43µs   min=1.22µs  med=3.27µs   max=4.18ms   p(90)=4.72µs   p(95)=5.35µs   p(99.9)=1.23ms  
     http_req_connecting............: avg=2.92µs   min=0s      med=0s       max=4.14ms   p(90)=0s       p(95)=0s       p(99.9)=1.21ms  
     http_req_duration..............: avg=181.41ms min=23.02ms med=186.54ms max=385.51ms p(90)=196.06ms p(95)=200.29ms p(99.9)=262.56ms
       { expected_response:true }...: avg=181.41ms min=23.02ms med=186.54ms max=385.51ms p(90)=196.06ms p(95)=200.29ms p(99.9)=262.56ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33050
     http_req_receiving.............: avg=91.95µs  min=33.05µs med=86.99µs  max=75.99ms  p(90)=116.6µs  p(95)=127.89µs p(99.9)=492.51µs
     http_req_sending...............: avg=34.85µs  min=5.55µs  med=16.76µs  max=129.94ms p(90)=21.49µs  p(95)=23.4µs   p(99.9)=500.24µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=181.28ms min=22.94ms med=186.43ms max=385.34ms p(90)=195.95ms p(95)=200.16ms p(99.9)=261.69ms
     http_reqs......................: 33050   269.557573/s
     iteration_duration.............: avg=182.19ms min=58.5ms  med=186.81ms max=397.29ms p(90)=196.34ms p(95)=200.6ms  p(99.9)=265.44ms
     iterations.....................: 32950   268.741968/s
     success_rate...................: 100.00% ✓ 32950      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 98583      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   324 kB/s
     http_req_blocked...............: avg=6.87µs   min=1.28µs  med=3.65µs   max=4.29ms   p(90)=5.21µs   p(95)=5.86µs   p(99.9)=1.34ms  
     http_req_connecting............: avg=2.94µs   min=0s      med=0s       max=4.25ms   p(90)=0s       p(95)=0s       p(99.9)=1.31ms  
     http_req_duration..............: avg=181.94ms min=17.79ms med=168.53ms max=767.95ms p(90)=208.8ms  p(95)=226.86ms p(99.9)=698.28ms
       { expected_response:true }...: avg=181.94ms min=17.79ms med=168.53ms max=767.95ms p(90)=208.8ms  p(95)=226.86ms p(99.9)=698.28ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32961
     http_req_receiving.............: avg=94.3µs   min=36.79µs med=88.3µs   max=47.15ms  p(90)=118.79µs p(95)=131.1µs  p(99.9)=894.4µs 
     http_req_sending...............: avg=40.54µs  min=6.55µs  med=18.26µs  max=177.35ms p(90)=23.17µs  p(95)=25.2µs   p(99.9)=531.58µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=181.81ms min=17.71ms med=168.39ms max=767.82ms p(90)=208.68ms p(95)=226.7ms  p(99.9)=698.19ms
     http_reqs......................: 32961   269.421281/s
     iteration_duration.............: avg=182.74ms min=39.17ms med=168.91ms max=768.19ms p(90)=209.15ms p(95)=227.25ms p(99.9)=698.52ms
     iterations.....................: 32861   268.603887/s
     success_rate...................: 100.00% ✓ 32861      ✗ 0    
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

