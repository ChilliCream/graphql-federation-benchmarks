## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.7 | 5,032 | 5,072 | 5,017 | 0.4% | 363 MB | 73.8 KB |  |
| fusion-net-11 | 16.7.3 | 5,017 | 5,072 | 4,999 | 0.6% | 390 MB | 79.7 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.7 | 4,874 | 4,877 | 4,833 | 0.4% | 398 MB | 83.6 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,857 | 4,867 | 4,845 | 0.2% | 385 MB | 81.1 KB |  |
| fusion-aot-11 | 16.7.3 | 4,782 | 4,789 | 4,761 | 0.3% | 123 MB | 26.4 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.7 | 4,754 | 4,758 | 4,738 | 0.2% | 135 MB | 29.2 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.7 | 4,598 | 4,601 | 4,583 | 0.2% | 129 MB | 28.8 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,510 | 4,525 | 4,500 | 0.2% | 128 MB | 29.1 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,137 | 4,490 | 3,974 | 4.7% | 2,306 MB | 570.8 KB |  |
| hive-router | v0.3.6 | 3,081 | 3,087 | 3,065 | 0.3% | 90 MB | 30.0 KB |  |
| grafbase | 0.53.5 | 1,856 | 1,866 | 1,850 | 0.4% | 108 MB | 59.7 KB |  |
| cosmo | 0.363.0 | 1,494 | 1,495 | 1,493 | 0.1% | 163 MB | 111.5 KB |  |
| caliban | 3.2.0 | 1,476 | 1,483 | 1,427 | 1.5% | 4,672 MB | 3,241.4 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 536 | 539 | 534 | 0.3% | 2,758 MB | 5,269.5 KB |  |
| apollo-router | v2.19.0 | 526 | 526 | 526 | 0.0% | 176 MB | 341.7 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 429 | 430 | 429 | 0.1% | 194 MB | 463.3 KB |  |
| hive-gateway | 2.15.3 | 273 | 274 | 272 | 0.3% | 3,616 MB | 13,563.6 KB |  |
| apollo-gateway | 2.14.4 | 270 | 271 | 270 | 0.2% | 2,150 MB | 8,153.1 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1813065     ✗ 0     
     data_received..................: 53 GB   440 MB/s
     data_sent......................: 727 MB  6.0 MB/s
     http_req_blocked...............: avg=5.07µs  min=952ns    med=2.39µs  max=266.44ms p(90)=3.7µs   p(95)=4.39µs   p(99.9)=34.78µs
     http_req_connecting............: avg=1.65µs  min=0s       med=0s      max=194.45ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.71ms  min=804.81µs med=8.78ms  max=264.72ms p(90)=15.23ms p(95)=18.35ms  p(99.9)=31.05ms
       { expected_response:true }...: avg=9.71ms  min=804.81µs med=8.78ms  max=264.72ms p(90)=15.23ms p(95)=18.35ms  p(99.9)=31.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 604455
     http_req_receiving.............: avg=99.2µs  min=24.95µs  med=47.16µs max=102.6ms  p(90)=92.79µs p(95)=200.63µs p(99.9)=6.63ms 
     http_req_sending...............: avg=45.79µs min=4.45µs   med=8.8µs   max=104.63ms p(90)=15.75µs p(95)=106.85µs p(99.9)=5.08ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.56ms  min=748.82µs med=8.67ms  max=240.29ms p(90)=15ms    p(95)=18.06ms  p(99.9)=30.55ms
     http_reqs......................: 604455  5032.735326/s
     iteration_duration.............: avg=9.91ms  min=1.14ms   med=8.98ms  max=286.93ms p(90)=15.45ms p(95)=18.58ms  p(99.9)=31.31ms
     iterations.....................: 604355  5031.902719/s
     success_rate...................: 100.00% ✓ 604355      ✗ 0     
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

     checks.........................: 100.00% ✓ 1807737     ✗ 0     
     data_received..................: 53 GB   439 MB/s
     data_sent......................: 724 MB  6.0 MB/s
     http_req_blocked...............: avg=3.37µs  min=771ns    med=1.85µs  max=133.4ms  p(90)=2.99µs  p(95)=3.62µs   p(99.9)=26.45µs
     http_req_connecting............: avg=1.05µs  min=0s       med=0s      max=133.27ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.75ms  min=832.14µs med=8.96ms  max=261.1ms  p(90)=14.95ms p(95)=17.61ms  p(99.9)=29.49ms
       { expected_response:true }...: avg=9.75ms  min=832.14µs med=8.96ms  max=261.1ms  p(90)=14.95ms p(95)=17.61ms  p(99.9)=29.49ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 602679
     http_req_receiving.............: avg=91.15µs min=23.88µs  med=45.27µs max=35.65ms  p(90)=89.69µs p(95)=191.57µs p(99.9)=6.1ms  
     http_req_sending...............: avg=44.21µs min=4.01µs   med=7.92µs  max=118.34ms p(90)=14.4µs  p(95)=99.58µs  p(99.9)=4.61ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.61ms  min=758.89µs med=8.85ms  max=186.8ms  p(90)=14.74ms p(95)=17.36ms  p(99.9)=28.94ms
     http_reqs......................: 602679  5017.842139/s
     iteration_duration.............: avg=9.94ms  min=1.09ms   med=9.15ms  max=278.52ms p(90)=15.15ms p(95)=17.82ms  p(99.9)=29.78ms
     iterations.....................: 602579  5017.009549/s
     success_rate...................: 100.00% ✓ 602579      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1756452     ✗ 0     
     data_received..................: 51 GB   427 MB/s
     data_sent......................: 704 MB  5.9 MB/s
     http_req_blocked...............: avg=2.73µs   min=792ns    med=2.1µs   max=6.22ms   p(90)=3.47µs  p(95)=4.29µs   p(99.9)=30.74µs
     http_req_connecting............: avg=154ns    min=0s       med=0s      max=3.88ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.03ms  min=1ms      med=9.2ms   max=284.68ms p(90)=15.36ms p(95)=18.16ms  p(99.9)=30.55ms
       { expected_response:true }...: avg=10.03ms  min=1ms      med=9.2ms   max=284.68ms p(90)=15.36ms p(95)=18.16ms  p(99.9)=30.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 585584
     http_req_receiving.............: avg=100.05µs min=25.99µs  med=48.09µs max=22.86ms  p(90)=97.79µs p(95)=196.84µs p(99.9)=6.6ms  
     http_req_sending...............: avg=43.9µs   min=4.33µs   med=8.41µs  max=75.58ms  p(90)=16.23µs p(95)=101.91µs p(99.9)=5.03ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.89ms   min=926.61µs med=9.09ms  max=284.2ms  p(90)=15.14ms p(95)=17.89ms  p(99.9)=30.1ms 
     http_reqs......................: 585584  4874.61873/s
     iteration_duration.............: avg=10.23ms  min=1.3ms    med=9.4ms   max=304.59ms p(90)=15.57ms p(95)=18.38ms  p(99.9)=30.8ms 
     iterations.....................: 585484  4873.786293/s
     success_rate...................: 100.00% ✓ 585484      ✗ 0     
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

     checks.........................: 100.00% ✓ 1750161     ✗ 0     
     data_received..................: 51 GB   425 MB/s
     data_sent......................: 701 MB  5.8 MB/s
     http_req_blocked...............: avg=3.03µs   min=841ns    med=2.39µs  max=6.45ms   p(90)=3.71µs  p(95)=4.47µs   p(99.9)=33.7µs 
     http_req_connecting............: avg=169ns    min=0s       med=0s      max=4.11ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.06ms  min=1ms      med=9.18ms  max=277.74ms p(90)=15.58ms p(95)=18.41ms  p(99.9)=31.3ms 
       { expected_response:true }...: avg=10.06ms  min=1ms      med=9.18ms  max=277.74ms p(90)=15.58ms p(95)=18.41ms  p(99.9)=31.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 583487
     http_req_receiving.............: avg=101.62µs min=25.79µs  med=48.56µs max=77.79ms  p(90)=96.62µs p(95)=198.82µs p(99.9)=6.8ms  
     http_req_sending...............: avg=45.72µs  min=4.51µs   med=8.87µs  max=191.59ms p(90)=16.09µs p(95)=103.55µs p(99.9)=5.17ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.91ms   min=929.94µs med=9.06ms  max=263.9ms  p(90)=15.36ms p(95)=18.14ms  p(99.9)=30.73ms
     http_reqs......................: 583487  4857.212686/s
     iteration_duration.............: avg=10.27ms  min=1.31ms   med=9.38ms  max=292.37ms p(90)=15.8ms  p(95)=18.63ms  p(99.9)=31.58ms
     iterations.....................: 583387  4856.38024/s
     success_rate...................: 100.00% ✓ 583387      ✗ 0     
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

     checks.........................: 100.00% ✓ 1723041     ✗ 0     
     data_received..................: 50 GB   419 MB/s
     data_sent......................: 690 MB  5.7 MB/s
     http_req_blocked...............: avg=2.46µs  min=802ns    med=1.88µs  max=13.49ms  p(90)=2.96µs  p(95)=3.52µs   p(99.9)=26.22µs
     http_req_connecting............: avg=186ns   min=0s       med=0s      max=3.83ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.24ms min=904.67µs med=9.58ms  max=287.17ms p(90)=15.11ms p(95)=17.57ms  p(99.9)=28.59ms
       { expected_response:true }...: avg=10.24ms min=904.67µs med=9.58ms  max=287.17ms p(90)=15.11ms p(95)=17.57ms  p(99.9)=28.59ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 574447
     http_req_receiving.............: avg=89.44µs min=24.61µs  med=44.98µs max=121.74ms p(90)=89.84µs p(95)=199.53µs p(99.9)=5.41ms 
     http_req_sending...............: avg=39.18µs min=4.46µs   med=8µs     max=141.75ms p(90)=13.85µs p(95)=101.7µs  p(99.9)=3.91ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.11ms min=852.27µs med=9.48ms  max=281.73ms p(90)=14.91ms p(95)=17.32ms  p(99.9)=28.16ms
     http_reqs......................: 574447  4782.410147/s
     iteration_duration.............: avg=10.43ms min=1.05ms   med=9.76ms  max=299.03ms p(90)=15.31ms p(95)=17.78ms  p(99.9)=28.83ms
     iterations.....................: 574347  4781.577623/s
     success_rate...................: 100.00% ✓ 574347      ✗ 0     
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

     checks.........................: 100.00% ✓ 1712961     ✗ 0     
     data_received..................: 50 GB   416 MB/s
     data_sent......................: 686 MB  5.7 MB/s
     http_req_blocked...............: avg=2.37µs  min=762ns    med=1.82µs  max=6.04ms   p(90)=2.91µs  p(95)=3.48µs   p(99.9)=25.9µs 
     http_req_connecting............: avg=155ns   min=0s       med=0s      max=3.83ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.31ms min=892.52µs med=9.69ms  max=266.85ms p(90)=15.14ms p(95)=17.5ms   p(99.9)=28.47ms
       { expected_response:true }...: avg=10.31ms min=892.52µs med=9.69ms  max=266.85ms p(90)=15.14ms p(95)=17.5ms   p(99.9)=28.47ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 571087
     http_req_receiving.............: avg=89.13µs min=23.96µs  med=44.84µs max=149ms    p(90)=89.98µs p(95)=201.27µs p(99.9)=5.35ms 
     http_req_sending...............: avg=38.53µs min=4.3µs    med=7.87µs  max=202.62ms p(90)=14.05µs p(95)=101.81µs p(99.9)=3.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.18ms min=836.64µs med=9.58ms  max=266.69ms p(90)=14.95ms p(95)=17.27ms  p(99.9)=28.09ms
     http_reqs......................: 571087  4754.285279/s
     iteration_duration.............: avg=10.49ms min=1.26ms   med=9.87ms  max=277.7ms  p(90)=15.33ms p(95)=17.71ms  p(99.9)=28.72ms
     iterations.....................: 570987  4753.452781/s
     success_rate...................: 100.00% ✓ 570987      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1657131     ✗ 0     
     data_received..................: 48 GB   402 MB/s
     data_sent......................: 664 MB  5.5 MB/s
     http_req_blocked...............: avg=2.53µs  min=801ns   med=1.95µs  max=5.6ms    p(90)=3.28µs  p(95)=4.04µs   p(99.9)=28.11µs
     http_req_connecting............: avg=156ns   min=0s      med=0s      max=3.83ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.65ms min=1.07ms  med=10.01ms max=279.29ms p(90)=15.6ms  p(95)=18.14ms  p(99.9)=30.39ms
       { expected_response:true }...: avg=10.65ms min=1.07ms  med=10.01ms max=279.29ms p(90)=15.6ms  p(95)=18.14ms  p(99.9)=30.39ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 552477
     http_req_receiving.............: avg=95.66µs min=24.84µs med=46.36µs max=49.69ms  p(90)=97.29µs p(95)=205.58µs p(99.9)=6.09ms 
     http_req_sending...............: avg=42.31µs min=4.22µs  med=8.24µs  max=158.58ms p(90)=16.79µs p(95)=105.2µs  p(99.9)=4.43ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.51ms min=1ms     med=9.89ms  max=278.73ms p(90)=15.4ms  p(95)=17.88ms  p(99.9)=29.97ms
     http_reqs......................: 552477  4598.175484/s
     iteration_duration.............: avg=10.85ms min=1.7ms   med=10.2ms  max=293.52ms p(90)=15.81ms p(95)=18.36ms  p(99.9)=30.67ms
     iterations.....................: 552377  4597.3432/s
     success_rate...................: 100.00% ✓ 552377      ✗ 0     
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

     checks.........................: 100.00% ✓ 1625361     ✗ 0     
     data_received..................: 47 GB   395 MB/s
     data_sent......................: 651 MB  5.4 MB/s
     http_req_blocked...............: avg=3.08µs   min=951ns   med=2.44µs  max=5.18ms   p(90)=3.85µs   p(95)=4.56µs   p(99.9)=32.41µs
     http_req_connecting............: avg=172ns    min=0s      med=0s      max=4.16ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.86ms  min=1.14ms  med=10.22ms max=295.44ms p(90)=15.95ms  p(95)=18.52ms  p(99.9)=30.76ms
       { expected_response:true }...: avg=10.86ms  min=1.14ms  med=10.22ms max=295.44ms p(90)=15.95ms  p(95)=18.52ms  p(99.9)=30.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 541887
     http_req_receiving.............: avg=101.82µs min=25.59µs med=48.33µs max=195.4ms  p(90)=100.27µs p(95)=215.4µs  p(99.9)=6.15ms 
     http_req_sending...............: avg=43.5µs   min=4.47µs  med=8.92µs  max=134.21ms p(90)=16.85µs  p(95)=109.97µs p(99.9)=4.58ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.71ms  min=1.05ms  med=10.1ms  max=294.63ms p(90)=15.74ms  p(95)=18.28ms  p(99.9)=30.34ms
     http_reqs......................: 541887  4510.363421/s
     iteration_duration.............: avg=11.06ms  min=1.3ms   med=10.42ms max=305.21ms p(90)=16.15ms  p(95)=18.74ms  p(99.9)=31.04ms
     iterations.....................: 541787  4509.531077/s
     success_rate...................: 100.00% ✓ 541787      ✗ 0     
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

     checks.........................: 100.00% ✓ 1490676     ✗ 0     
     data_received..................: 43 GB   362 MB/s
     data_sent......................: 597 MB  5.0 MB/s
     http_req_blocked...............: avg=2.96µs  min=811ns    med=2.12µs  max=12.34ms  p(90)=3.37µs  p(95)=3.99µs   p(99.9)=29.93µs
     http_req_connecting............: avg=457ns   min=0s       med=0s      max=9.36ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.87ms min=794.09µs med=11.92ms max=281.38ms p(90)=18.22ms p(95)=20.17ms  p(99.9)=30.09ms
       { expected_response:true }...: avg=11.87ms min=794.09µs med=11.92ms max=281.38ms p(90)=18.22ms p(95)=20.17ms  p(99.9)=30.09ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 496992
     http_req_receiving.............: avg=81.05µs min=24.44µs  med=47.09µs max=182.31ms p(90)=91.75µs p(95)=201.02µs p(99.9)=3.5ms  
     http_req_sending...............: avg=38.4µs  min=4.53µs   med=8.98µs  max=193.17ms p(90)=15.66µs p(95)=109.72µs p(99.9)=2.78ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.75ms min=725.9µs  med=11.82ms max=264.61ms p(90)=18.08ms p(95)=20.01ms  p(99.9)=29.82ms
     http_reqs......................: 496992  4137.651987/s
     iteration_duration.............: avg=12.06ms min=1.24ms   med=12.11ms max=297.98ms p(90)=18.42ms p(95)=20.36ms  p(99.9)=30.35ms
     iterations.....................: 496892  4136.819448/s
     success_rate...................: 100.00% ✓ 496892      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1110597     ✗ 0     
     data_received..................: 32 GB   270 MB/s
     data_sent......................: 445 MB  3.7 MB/s
     http_req_blocked...............: avg=3.16µs  min=852ns   med=2.21µs  max=9.85ms   p(90)=3.66µs  p(95)=4.39µs   p(99.9)=34.72µs
     http_req_connecting............: avg=557ns   min=0s      med=0s      max=8.43ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=15.99ms min=1.41ms  med=16.03ms max=275.36ms p(90)=21.32ms p(95)=22.78ms  p(99.9)=30.38ms
       { expected_response:true }...: avg=15.99ms min=1.41ms  med=16.03ms max=275.36ms p(90)=21.32ms p(95)=22.78ms  p(99.9)=30.38ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 370299
     http_req_receiving.............: avg=73.73µs min=24.88µs med=50.86µs max=55.06ms  p(90)=94.21µs p(95)=183.12µs p(99.9)=1.33ms 
     http_req_sending...............: avg=34.6µs  min=4.44µs  med=9.8µs   max=75.22ms  p(90)=17.89µs p(95)=110.16µs p(99.9)=1.49ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=15.89ms min=1.33ms  med=15.92ms max=274.53ms p(90)=21.21ms p(95)=22.66ms  p(99.9)=30.19ms
     http_reqs......................: 370299  3081.279331/s
     iteration_duration.............: avg=16.19ms min=3.08ms  med=16.22ms max=326.57ms p(90)=21.51ms p(95)=22.97ms  p(99.9)=30.61ms
     iterations.....................: 370199  3080.447225/s
     success_rate...................: 100.00% ✓ 370199      ✗ 0     
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

     checks.........................: 100.00% ✓ 669297      ✗ 0     
     data_received..................: 20 GB   163 MB/s
     data_sent......................: 268 MB  2.2 MB/s
     http_req_blocked...............: avg=3.84µs  min=852ns   med=2.31µs  max=8.98ms   p(90)=4.48µs   p(95)=5.52µs   p(99.9)=42.72µs
     http_req_connecting............: avg=888ns   min=0s      med=0s      max=8.94ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.65ms min=1.85ms  med=26.04ms max=300.34ms p(90)=34.51ms  p(95)=37.3ms   p(99.9)=51.02ms
       { expected_response:true }...: avg=26.65ms min=1.85ms  med=26.04ms max=300.34ms p(90)=34.51ms  p(95)=37.3ms   p(99.9)=51.02ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 223199
     http_req_receiving.............: avg=83.15µs min=27.03µs med=56.58µs max=131.61ms p(90)=116.61µs p(95)=175.91µs p(99.9)=1.37ms 
     http_req_sending...............: avg=32.11µs min=4.36µs  med=9.85µs  max=98.06ms  p(90)=22.26µs  p(95)=96.21µs  p(99.9)=1.38ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.53ms min=1.75ms  med=25.93ms max=287.46ms p(90)=34.39ms  p(95)=37.16ms  p(99.9)=50.77ms
     http_reqs......................: 223199  1856.029341/s
     iteration_duration.............: avg=26.88ms min=8.14ms  med=26.25ms max=310.66ms p(90)=34.72ms  p(95)=37.51ms  p(99.9)=51.29ms
     iterations.....................: 223099  1855.197783/s
     success_rate...................: 100.00% ✓ 223099      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 538806      ✗ 0     
     data_received..................: 16 GB   131 MB/s
     data_sent......................: 216 MB  1.8 MB/s
     http_req_blocked...............: avg=3.68µs  min=912ns   med=2.07µs  max=8.01ms   p(90)=3.48µs  p(95)=4.15µs   p(99.9)=28.96µs 
     http_req_connecting............: avg=1.28µs  min=0s      med=0s      max=7.98ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.18ms min=2.01ms  med=32.29ms max=282.86ms p(90)=47.92ms p(95)=52.95ms  p(99.9)=76.79ms 
       { expected_response:true }...: avg=33.18ms min=2.01ms  med=32.29ms max=282.86ms p(90)=47.92ms p(95)=52.95ms  p(99.9)=76.79ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 179702
     http_req_receiving.............: avg=67.38µs min=25.73µs med=56.5µs  max=61.93ms  p(90)=92.5µs  p(95)=107.76µs p(99.9)=690.76µs
     http_req_sending...............: avg=21.62µs min=4.75µs  med=10.23µs max=98.69ms  p(90)=16.69µs p(95)=20.32µs  p(99.9)=759.16µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.09ms min=1.95ms  med=32.2ms  max=280.61ms p(90)=47.83ms p(95)=52.86ms  p(99.9)=76.53ms 
     http_reqs......................: 179702  1494.160395/s
     iteration_duration.............: avg=33.4ms  min=4.43ms  med=32.49ms max=301.91ms p(90)=48.12ms p(95)=53.14ms  p(99.9)=77.08ms 
     iterations.....................: 179602  1493.328929/s
     success_rate...................: 100.00% ✓ 179602      ✗ 0     
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

     checks.........................: 100.00% ✓ 532560      ✗ 0     
     data_received..................: 16 GB   129 MB/s
     data_sent......................: 213 MB  1.8 MB/s
     http_req_blocked...............: avg=5.88µs  min=1.12µs  med=3.04µs  max=79.23ms  p(90)=4.71µs   p(95)=5.46µs   p(99.9)=39.7µs  
     http_req_connecting............: avg=2.42µs  min=0s      med=0s      max=66.42ms  p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.54ms min=2.12ms  med=32.64ms max=290.1ms  p(90)=47.49ms  p(95)=52.43ms  p(99.9)=77.81ms 
       { expected_response:true }...: avg=33.54ms min=2.12ms  med=32.64ms max=290.1ms  p(90)=47.49ms  p(95)=52.43ms  p(99.9)=77.81ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 177620
     http_req_receiving.............: avg=76.97µs min=28.65µs med=64.78µs max=29.74ms  p(90)=102.86µs p(95)=119.64µs p(99.9)=961.31µs
     http_req_sending...............: avg=28.26µs min=5.27µs  med=12.77µs max=102.31ms p(90)=19.51µs  p(95)=23.43µs  p(99.9)=836.29µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.43ms min=2.05ms  med=32.53ms max=256.86ms p(90)=47.39ms  p(95)=52.32ms  p(99.9)=77.62ms 
     http_reqs......................: 177620  1476.711604/s
     iteration_duration.............: avg=33.78ms min=6.1ms   med=32.86ms max=300.83ms p(90)=47.72ms  p(95)=52.66ms  p(99.9)=78.24ms 
     iterations.....................: 177520  1475.880216/s
     success_rate...................: 100.00% ✓ 177520      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 193779     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   644 kB/s
     http_req_blocked...............: avg=4.21µs  min=1.1µs   med=3.05µs  max=3.41ms   p(90)=4.53µs   p(95)=5.18µs   p(99.9)=46.97µs 
     http_req_connecting............: avg=910ns   min=0s      med=0s      max=3.39ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.53ms min=3.88ms  med=89.67ms max=321.71ms p(90)=112.21ms p(95)=123.93ms p(99.9)=215.12ms
       { expected_response:true }...: avg=92.53ms min=3.88ms  med=89.67ms max=321.71ms p(90)=112.21ms p(95)=123.93ms p(99.9)=215.12ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64693
     http_req_receiving.............: avg=81.65µs min=28.9µs  med=70.27µs max=67.77ms  p(90)=103.07µs p(95)=115.63µs p(99.9)=650.78µs
     http_req_sending...............: avg=21.6µs  min=5µs     med=13.71µs max=68.44ms  p(90)=19.35µs  p(95)=21.4µs   p(99.9)=604.06µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.43ms min=3.82ms  med=89.57ms max=297.77ms p(90)=112.12ms p(95)=123.82ms p(99.9)=214.58ms
     http_reqs......................: 64693   536.595067/s
     iteration_duration.............: avg=92.9ms  min=18.97ms med=89.91ms max=336.11ms p(90)=112.47ms p(95)=124.24ms p(99.9)=215.95ms
     iterations.....................: 64593   535.765618/s
     success_rate...................: 100.00% ✓ 64593      ✗ 0    
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

     checks.........................: 100.00% ✓ 190308     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 76 MB   633 kB/s
     http_req_blocked...............: avg=4.31µs   min=1.07µs  med=2.78µs  max=3.39ms   p(90)=4.21µs   p(95)=4.75µs   p(99.9)=49.94µs 
     http_req_connecting............: avg=1.33µs   min=0s      med=0s      max=3.36ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=94.22ms  min=4.44ms  med=92.31ms max=330.88ms p(90)=127.3ms  p(95)=137.5ms  p(99.9)=180.23ms
       { expected_response:true }...: avg=94.22ms  min=4.44ms  med=92.31ms max=330.88ms p(90)=127.3ms  p(95)=137.5ms  p(99.9)=180.23ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63536
     http_req_receiving.............: avg=122.33µs min=26.78µs med=69.84µs max=234.82ms p(90)=101.15µs p(95)=113.66µs p(99.9)=619.63µs
     http_req_sending...............: avg=18.36µs  min=5.08µs  med=14.04µs max=25.76ms  p(90)=19.68µs  p(95)=21.61µs  p(99.9)=485.41µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.08ms  min=4.32ms  med=92.21ms max=247.85ms p(90)=127.16ms p(95)=137.32ms p(99.9)=176.94ms
     http_reqs......................: 63536   526.886664/s
     iteration_duration.............: avg=94.6ms   min=24.16ms med=92.58ms max=340.97ms p(90)=127.55ms p(95)=137.77ms p(99.9)=181.38ms
     iterations.....................: 63436   526.057392/s
     success_rate...................: 100.00% ✓ 63436      ✗ 0    
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

     checks.........................: 100.00% ✓ 155232     ✗ 0    
     data_received..................: 4.5 GB  38 MB/s
     data_sent......................: 62 MB   516 kB/s
     http_req_blocked...............: avg=4.94µs   min=1.01µs  med=2.9µs    max=6.31ms   p(90)=4.29µs   p(95)=4.82µs   p(99.9)=98.86µs 
     http_req_connecting............: avg=1.78µs   min=0s      med=0s       max=6.27ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=115.51ms min=5.31ms  med=113.21ms max=311.69ms p(90)=151.24ms p(95)=162.92ms p(99.9)=212.45ms
       { expected_response:true }...: avg=115.51ms min=5.31ms  med=113.21ms max=311.69ms p(90)=151.24ms p(95)=162.92ms p(99.9)=212.45ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51844
     http_req_receiving.............: avg=83.71µs  min=28.38µs med=77.88µs  max=75.63ms  p(90)=106.9µs  p(95)=118.49µs p(99.9)=453.47µs
     http_req_sending...............: avg=25.61µs  min=5.11µs  med=15.46µs  max=169.51ms p(90)=20.19µs  p(95)=21.93µs  p(99.9)=522.86µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=115.4ms  min=5.19ms  med=113.12ms max=311.59ms p(90)=151.13ms p(95)=162.8ms  p(99.9)=212.05ms
     http_reqs......................: 51844   429.599115/s
     iteration_duration.............: avg=115.98ms min=15.82ms med=113.5ms  max=319.42ms p(90)=151.55ms p(95)=163.2ms  p(99.9)=213.86ms
     iterations.....................: 51744   428.770477/s
     success_rate...................: 100.00% ✓ 51744      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 98901      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   328 kB/s
     http_req_blocked...............: avg=5.17µs   min=1.09µs  med=3.11µs   max=4.23ms   p(90)=4.45µs   p(95)=4.99µs   p(99.9)=430.65µs
     http_req_connecting............: avg=1.77µs   min=0s      med=0s       max=3.61ms   p(90)=0s       p(95)=0s       p(99.9)=381.03µs
     http_req_duration..............: avg=181.39ms min=5.67ms  med=166.77ms max=827.08ms p(90)=212.47ms p(95)=241.04ms p(99.9)=680.61ms
       { expected_response:true }...: avg=181.39ms min=5.67ms  med=166.77ms max=827.08ms p(90)=212.47ms p(95)=241.04ms p(99.9)=680.61ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33067
     http_req_receiving.............: avg=93.7µs   min=30.9µs  med=86.94µs  max=112.44ms p(90)=115µs    p(95)=126.19µs p(99.9)=804.98µs
     http_req_sending...............: avg=24.92µs  min=5.18µs  med=16.44µs  max=60ms     p(90)=20.5µs   p(95)=22.22µs  p(99.9)=629.56µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=181.27ms min=5.59ms  med=166.66ms max=826.99ms p(90)=212.36ms p(95)=240.86ms p(99.9)=680.53ms
     http_reqs......................: 33067   273.381155/s
     iteration_duration.............: avg=182.19ms min=32.31ms med=167.12ms max=827.29ms p(90)=212.8ms  p(95)=241.71ms p(99.9)=680.88ms
     iterations.....................: 32967   272.554406/s
     success_rate...................: 100.00% ✓ 32967      ✗ 0    
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

     checks.........................: 100.00% ✓ 98031      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   325 kB/s
     http_req_blocked...............: avg=6.49µs   min=1.4µs   med=3.49µs   max=4.16ms   p(90)=4.83µs   p(95)=5.4µs    p(99.9)=1.24ms  
     http_req_connecting............: avg=2.79µs   min=0s      med=0s       max=4.12ms   p(90)=0s       p(95)=0s       p(99.9)=1.21ms  
     http_req_duration..............: avg=182.9ms  min=7.54ms  med=186.72ms max=375.55ms p(90)=237.61ms p(95)=243.33ms p(99.9)=324.64ms
       { expected_response:true }...: avg=182.9ms  min=7.54ms  med=186.72ms max=375.55ms p(90)=237.61ms p(95)=243.33ms p(99.9)=324.64ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32777
     http_req_receiving.............: avg=84.3µs   min=32.48µs med=80.53µs  max=6.76ms   p(90)=109.65µs p(95)=119.68µs p(99.9)=457.21µs
     http_req_sending...............: avg=38.45µs  min=5.91µs  med=16.09µs  max=177.38ms p(90)=20.55µs  p(95)=22.34µs  p(99.9)=578.33µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=182.78ms min=7.39ms  med=186.53ms max=375ms    p(90)=237.5ms  p(95)=243.22ms p(99.9)=324.54ms
     http_reqs......................: 32777   270.980079/s
     iteration_duration.............: avg=183.72ms min=40.37ms med=188.69ms max=390.8ms  p(90)=237.93ms p(95)=243.62ms p(99.9)=327.04ms
     iterations.....................: 32677   270.153341/s
     success_rate...................: 100.00% ✓ 32677      ✗ 0    
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

