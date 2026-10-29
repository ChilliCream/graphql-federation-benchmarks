## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.7 | 5,137 | 5,161 | 5,115 | 0.3% | 369 MB | 73.6 KB |  |
| fusion-net-11 | 16.7.2 | 5,073 | 5,112 | 5,055 | 0.4% | 370 MB | 74.6 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.7 | 4,800 | 4,853 | 4,741 | 1.0% | 375 MB | 80.1 KB |  |
| fusion-fed-net-11 | 16.7.2 | 4,783 | 4,810 | 4,742 | 0.6% | 382 MB | 81.8 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.7 | 4,749 | 4,809 | 4,734 | 0.6% | 118 MB | 25.4 KB |  |
| fusion-aot-11 | 16.7.2 | 4,741 | 4,753 | 4,732 | 0.2% | 115 MB | 24.9 KB |  |
| fusion-fed-aot-11 | 16.7.2 | 4,573 | 4,599 | 4,530 | 0.7% | 126 MB | 28.1 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.7 | 4,514 | 4,529 | 4,507 | 0.2% | 132 MB | 30.0 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,164 | 4,323 | 4,100 | 2.5% | 2,300 MB | 565.7 KB |  |
| hive-router | v0.3.6 | 3,075 | 3,088 | 3,058 | 0.4% | 92 MB | 30.6 KB |  |
| grafbase | 0.53.5 | 1,892 | 1,894 | 1,882 | 0.3% | 114 MB | 61.6 KB |  |
| caliban | 3.2.0 | 1,538 | 1,539 | 1,534 | 0.1% | 4,383 MB | 2,918.5 KB |  |
| cosmo | 0.363.0 | 1,485 | 1,490 | 1,482 | 0.2% | 165 MB | 113.7 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 537 | 539 | 536 | 0.2% | 2,734 MB | 5,214.1 KB |  |
| apollo-router | v2.19.0 | 526 | 532 | 514 | 1.3% | 173 MB | 336.0 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 416 | 426 | 404 | 1.9% | 202 MB | 497.6 KB |  |
| apollo-gateway | 2.14.4 | 274 | 277 | 273 | 0.6% | 2,140 MB | 7,997.1 KB |  |
| hive-gateway | 2.15.3 | 269 | 271 | 269 | 0.3% | 3,515 MB | 13,382.4 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1850889     ✗ 0     
     data_received..................: 54 GB   450 MB/s
     data_sent......................: 742 MB  6.2 MB/s
     http_req_blocked...............: avg=2.95µs  min=762ns    med=1.87µs  max=98.51ms  p(90)=3.02µs  p(95)=3.66µs   p(99.9)=25.63µs
     http_req_connecting............: avg=470ns   min=0s       med=0s      max=34.47ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.52ms  min=786.43µs med=8.69ms  max=251.91ms p(90)=14.7ms  p(95)=17.46ms  p(99.9)=29.69ms
       { expected_response:true }...: avg=9.52ms  min=786.43µs med=8.69ms  max=251.91ms p(90)=14.7ms  p(95)=17.46ms  p(99.9)=29.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 617063
     http_req_receiving.............: avg=90.93µs min=22.43µs  med=44.02µs max=64.34ms  p(90)=86.7µs  p(95)=183.62µs p(99.9)=6.29ms 
     http_req_sending...............: avg=41.89µs min=3.96µs   med=7.83µs  max=153.95ms p(90)=13.95µs p(95)=96.59µs  p(99.9)=4.72ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.38ms  min=738.77µs med=8.58ms  max=241.18ms p(90)=14.48ms p(95)=17.21ms  p(99.9)=29.29ms
     http_reqs......................: 617063  5137.672715/s
     iteration_duration.............: avg=9.71ms  min=1.2ms    med=8.88ms  max=275.95ms p(90)=14.9ms  p(95)=17.68ms  p(99.9)=29.92ms
     iterations.....................: 616963  5136.840114/s
     success_rate...................: 100.00% ✓ 616963      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1827897     ✗ 0     
     data_received..................: 53 GB   444 MB/s
     data_sent......................: 732 MB  6.1 MB/s
     http_req_blocked...............: avg=6.71µs  min=802ns    med=1.93µs  max=191.46ms p(90)=3.09µs  p(95)=3.72µs   p(99.9)=26.18µs
     http_req_connecting............: avg=4.26µs  min=0s       med=0s      max=191.43ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.63ms  min=805.09µs med=8.81ms  max=223.69ms p(90)=14.87ms p(95)=17.74ms  p(99.9)=30.19ms
       { expected_response:true }...: avg=9.63ms  min=805.09µs med=8.81ms  max=223.69ms p(90)=14.87ms p(95)=17.74ms  p(99.9)=30.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 609399
     http_req_receiving.............: avg=92.43µs min=25.26µs  med=46.27µs max=35.07ms  p(90)=88.22µs p(95)=191.42µs p(99.9)=6.12ms 
     http_req_sending...............: avg=42.93µs min=4.31µs   med=8.19µs  max=171.61ms p(90)=14.52µs p(95)=100.21µs p(99.9)=4.78ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.5ms   min=759.65µs med=8.7ms   max=187.36ms p(90)=14.65ms p(95)=17.48ms  p(99.9)=29.68ms
     http_reqs......................: 609399  5073.823716/s
     iteration_duration.............: avg=9.83ms  min=974.01µs med=9ms     max=295.66ms p(90)=15.07ms p(95)=17.95ms  p(99.9)=30.47ms
     iterations.....................: 609299  5072.991122/s
     success_rate...................: 100.00% ✓ 609299      ✗ 0     
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

     checks.........................: 100.00% ✓ 1729629     ✗ 0     
     data_received..................: 51 GB   420 MB/s
     data_sent......................: 693 MB  5.8 MB/s
     http_req_blocked...............: avg=3.03µs   min=892ns    med=2.36µs  max=5.76ms   p(90)=3.69µs  p(95)=4.43µs   p(99.9)=33.89µs
     http_req_connecting............: avg=194ns    min=0s       med=0s      max=4.01ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.18ms  min=1ms      med=9.34ms  max=195.52ms p(90)=15.65ms p(95)=18.49ms  p(99.9)=31.41ms
       { expected_response:true }...: avg=10.18ms  min=1ms      med=9.34ms  max=195.52ms p(90)=15.65ms p(95)=18.49ms  p(99.9)=31.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 576643
     http_req_receiving.............: avg=101.68µs min=25.72µs  med=48.74µs max=66.55ms  p(90)=97.98µs p(95)=204.63µs p(99.9)=6.62ms 
     http_req_sending...............: avg=44.39µs  min=4.43µs   med=8.51µs  max=91.52ms  p(90)=16.08µs p(95)=105.38µs p(99.9)=4.96ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.03ms  min=926.07µs med=9.22ms  max=195.32ms p(90)=15.42ms p(95)=18.23ms  p(99.9)=30.93ms
     http_reqs......................: 576643  4800.328974/s
     iteration_duration.............: avg=10.39ms  min=1.25ms   med=9.53ms  max=352.78ms p(90)=15.86ms p(95)=18.72ms  p(99.9)=31.89ms
     iterations.....................: 576543  4799.496513/s
     success_rate...................: 100.00% ✓ 576543      ✗ 0     
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

     checks.........................: 100.00% ✓ 1723884     ✗ 0     
     data_received..................: 50 GB   419 MB/s
     data_sent......................: 691 MB  5.7 MB/s
     http_req_blocked...............: avg=3.11µs   min=842ns    med=2.44µs max=7.06ms   p(90)=3.75µs  p(95)=4.46µs   p(99.9)=33.36µs
     http_req_connecting............: avg=165ns    min=0s       med=0s     max=3.98ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.22ms  min=971.91µs med=9.39ms max=288.48ms p(90)=15.67ms p(95)=18.54ms  p(99.9)=31.69ms
       { expected_response:true }...: avg=10.22ms  min=971.91µs med=9.39ms max=288.48ms p(90)=15.67ms p(95)=18.54ms  p(99.9)=31.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 574728
     http_req_receiving.............: avg=103.27µs min=25.68µs  med=49µs   max=133.33ms p(90)=97.84µs p(95)=204.59µs p(99.9)=6.94ms 
     http_req_sending...............: avg=44.94µs  min=4.49µs   med=8.74µs max=132.41ms p(90)=16.02µs p(95)=105.45µs p(99.9)=4.92ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.07ms  min=917.09µs med=9.27ms max=288.38ms p(90)=15.45ms p(95)=18.25ms  p(99.9)=31.17ms
     http_reqs......................: 574728  4783.992123/s
     iteration_duration.............: avg=10.43ms  min=1.42ms   med=9.59ms max=305.62ms p(90)=15.88ms p(95)=18.76ms  p(99.9)=31.94ms
     iterations.....................: 574628  4783.159731/s
     success_rate...................: 100.00% ✓ 574628      ✗ 0     
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

     checks.........................: 100.00% ✓ 1711326     ✗ 0     
     data_received..................: 50 GB   416 MB/s
     data_sent......................: 686 MB  5.7 MB/s
     http_req_blocked...............: avg=2.55µs  min=821ns    med=1.93µs  max=9.11ms   p(90)=3.01µs  p(95)=3.58µs   p(99.9)=26.32µs
     http_req_connecting............: avg=176ns   min=0s       med=0s      max=4.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.31ms min=888.38µs med=9.7ms   max=223.81ms p(90)=15.14ms p(95)=17.5ms   p(99.9)=28.59ms
       { expected_response:true }...: avg=10.31ms min=888.38µs med=9.7ms   max=223.81ms p(90)=15.14ms p(95)=17.5ms   p(99.9)=28.59ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 570542
     http_req_receiving.............: avg=92.77µs min=24.17µs  med=46.26µs max=23.21ms  p(90)=89.92µs p(95)=203.93µs p(99.9)=5.8ms  
     http_req_sending...............: avg=37.59µs min=4.14µs   med=8.08µs  max=211.15ms p(90)=14.03µs p(95)=100.3µs  p(99.9)=3.54ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.18ms min=838µs    med=9.59ms  max=223.4ms  p(90)=14.95ms p(95)=17.27ms  p(99.9)=28.09ms
     http_reqs......................: 570542  4749.625414/s
     iteration_duration.............: avg=10.5ms  min=1.42ms   med=9.88ms  max=325.52ms p(90)=15.34ms p(95)=17.71ms  p(99.9)=28.95ms
     iterations.....................: 570442  4748.792938/s
     success_rate...................: 100.00% ✓ 570442      ✗ 0     
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

     checks.........................: 100.00% ✓ 1708449     ✗ 0     
     data_received..................: 50 GB   415 MB/s
     data_sent......................: 685 MB  5.7 MB/s
     http_req_blocked...............: avg=2.43µs  min=791ns    med=1.88µs  max=5.85ms   p(90)=2.98µs  p(95)=3.53µs   p(99.9)=24.6µs 
     http_req_connecting............: avg=159ns   min=0s       med=0s      max=3.91ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.33ms min=899.36µs med=9.7ms   max=264.66ms p(90)=15.18ms p(95)=17.57ms  p(99.9)=28.98ms
       { expected_response:true }...: avg=10.33ms min=899.36µs med=9.7ms   max=264.66ms p(90)=15.18ms p(95)=17.57ms  p(99.9)=28.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 569583
     http_req_receiving.............: avg=87.11µs min=24.11µs  med=44.77µs max=80.52ms  p(90)=89.26µs p(95)=201µs    p(99.9)=5.07ms 
     http_req_sending...............: avg=39.2µs  min=4.31µs   med=7.95µs  max=199.45ms p(90)=14.07µs p(95)=102.03µs p(99.9)=3.82ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.21ms min=847.07µs med=9.59ms  max=264.39ms p(90)=14.99ms p(95)=17.34ms  p(99.9)=28.69ms
     http_reqs......................: 569583  4741.891696/s
     iteration_duration.............: avg=10.52ms min=1.43ms   med=9.88ms  max=324.07ms p(90)=15.38ms p(95)=17.78ms  p(99.9)=29.32ms
     iterations.....................: 569483  4741.059176/s
     success_rate...................: 100.00% ✓ 569483      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1648089     ✗ 0     
     data_received..................: 48 GB   400 MB/s
     data_sent......................: 660 MB  5.5 MB/s
     http_req_blocked...............: avg=2.7µs   min=832ns    med=2.15µs  max=5.18ms   p(90)=3.47µs  p(95)=4.18µs   p(99.9)=29.49µs
     http_req_connecting............: avg=164ns   min=0s       med=0s      max=4.07ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.7ms  min=1.03ms   med=10.05ms max=299.16ms p(90)=15.75ms p(95)=18.29ms  p(99.9)=30.28ms
       { expected_response:true }...: avg=10.7ms  min=1.03ms   med=10.05ms max=299.16ms p(90)=15.75ms p(95)=18.29ms  p(99.9)=30.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 549463
     http_req_receiving.............: avg=97.9µs  min=26.24µs  med=47.73µs max=20.98ms  p(90)=98.05µs p(95)=207.16µs p(99.9)=5.97ms 
     http_req_sending...............: avg=42.87µs min=4.58µs   med=8.49µs  max=272.87ms p(90)=16.32µs p(95)=105.98µs p(99.9)=4.31ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.56ms min=992.45µs med=9.93ms  max=296.33ms p(90)=15.54ms p(95)=18.04ms  p(99.9)=29.84ms
     http_reqs......................: 549463  4573.586103/s
     iteration_duration.............: avg=10.91ms min=1.73ms   med=10.24ms max=328.49ms p(90)=15.96ms p(95)=18.51ms  p(99.9)=30.53ms
     iterations.....................: 549363  4572.753729/s
     success_rate...................: 100.00% ✓ 549363      ✗ 0     
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

     checks.........................: 100.00% ✓ 1626792     ✗ 0     
     data_received..................: 48 GB   395 MB/s
     data_sent......................: 652 MB  5.4 MB/s
     http_req_blocked...............: avg=2.47µs  min=802ns    med=1.94µs  max=7.55ms   p(90)=3.06µs  p(95)=3.7µs    p(99.9)=25.32µs
     http_req_connecting............: avg=155ns   min=0s       med=0s      max=3.34ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.86ms min=1.02ms   med=10.31ms max=274.28ms p(90)=15.63ms p(95)=17.87ms  p(99.9)=28.92ms
       { expected_response:true }...: avg=10.86ms min=1.02ms   med=10.31ms max=274.28ms p(90)=15.63ms p(95)=17.87ms  p(99.9)=28.92ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 542364
     http_req_receiving.............: avg=93.69µs min=24.38µs  med=46.47µs max=173.71ms p(90)=93.26µs p(95)=203.25µs p(99.9)=5.31ms 
     http_req_sending...............: avg=38.13µs min=4.3µs    med=8.06µs  max=86.02ms  p(90)=14.97µs p(95)=101.05µs p(99.9)=3.69ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.72ms min=989.65µs med=10.2ms  max=246.82ms p(90)=15.44ms p(95)=17.66ms  p(99.9)=28.57ms
     http_reqs......................: 542364  4514.289015/s
     iteration_duration.............: avg=11.05ms min=1.67ms   med=10.5ms  max=292.33ms p(90)=15.83ms p(95)=18.08ms  p(99.9)=29.17ms
     iterations.....................: 542264  4513.456679/s
     success_rate...................: 100.00% ✓ 542264      ✗ 0     
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

     checks.........................: 100.00% ✓ 1500426     ✗ 0     
     data_received..................: 44 GB   364 MB/s
     data_sent......................: 601 MB  5.0 MB/s
     http_req_blocked...............: avg=3.08µs  min=1.02µs   med=2.5µs   max=7.13ms   p(90)=3.78µs  p(95)=4.39µs   p(99.9)=35.14µs
     http_req_connecting............: avg=185ns   min=0s       med=0s      max=4.16ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.79ms min=779.47µs med=11.69ms max=281.72ms p(90)=18.12ms p(95)=20.23ms  p(99.9)=31.43ms
       { expected_response:true }...: avg=11.79ms min=779.47µs med=11.69ms max=281.72ms p(90)=18.12ms p(95)=20.23ms  p(99.9)=31.43ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 500242
     http_req_receiving.............: avg=86.03µs min=25.01µs  med=48.66µs max=248.24ms p(90)=94.51µs p(95)=213.88µs p(99.9)=4.03ms 
     http_req_sending...............: avg=40.44µs min=4.68µs   med=9.36µs  max=248.83ms p(90)=15.99µs p(95)=115.09µs p(99.9)=3.11ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.66ms min=710.06µs med=11.58ms max=281.09ms p(90)=17.97ms p(95)=20.06ms  p(99.9)=31.09ms
     http_reqs......................: 500242  4164.413231/s
     iteration_duration.............: avg=11.98ms min=1.14ms   med=11.88ms max=312.54ms p(90)=18.31ms p(95)=20.43ms  p(99.9)=31.69ms
     iterations.....................: 500142  4163.580751/s
     success_rate...................: 100.00% ✓ 500142      ✗ 0     
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

     checks.........................: 100.00% ✓ 1108422     ✗ 0     
     data_received..................: 32 GB   269 MB/s
     data_sent......................: 444 MB  3.7 MB/s
     http_req_blocked...............: avg=2.73µs  min=811ns   med=2.2µs   max=3.32ms   p(90)=3.64µs  p(95)=4.37µs   p(99.9)=30.08µs
     http_req_connecting............: avg=178ns   min=0s      med=0s      max=3.28ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.03ms min=1.33ms  med=16ms    max=273.72ms p(90)=21.42ms p(95)=22.91ms  p(99.9)=30.46ms
       { expected_response:true }...: avg=16.03ms min=1.33ms  med=16ms    max=273.72ms p(90)=21.42ms p(95)=22.91ms  p(99.9)=30.46ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 369574
     http_req_receiving.............: avg=74.52µs min=24.41µs med=51.31µs max=20.37ms  p(90)=96.03µs p(95)=183.96µs p(99.9)=1.39ms 
     http_req_sending...............: avg=34.32µs min=4.55µs  med=9.61µs  max=116.94ms p(90)=18.21µs p(95)=109.21µs p(99.9)=1.47ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=15.92ms min=1.28ms  med=15.89ms max=273.29ms p(90)=21.31ms p(95)=22.79ms  p(99.9)=30.26ms
     http_reqs......................: 369574  3075.040997/s
     iteration_duration.............: avg=16.23ms min=2.57ms  med=16.19ms max=283.25ms p(90)=21.61ms p(95)=23.1ms   p(99.9)=30.68ms
     iterations.....................: 369474  3074.208947/s
     success_rate...................: 100.00% ✓ 369474      ✗ 0     
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

     checks.........................: 100.00% ✓ 682434      ✗ 0     
     data_received..................: 20 GB   166 MB/s
     data_sent......................: 274 MB  2.3 MB/s
     http_req_blocked...............: avg=3.42µs  min=861ns   med=2.38µs  max=4.28ms   p(90)=4.64µs   p(95)=5.71µs   p(99.9)=42.74µs
     http_req_connecting............: avg=467ns   min=0s      med=0s      max=4.24ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.12ms min=1.83ms  med=25.57ms max=271.34ms p(90)=34.01ms  p(95)=36.74ms  p(99.9)=50.41ms
       { expected_response:true }...: avg=26.12ms min=1.83ms  med=25.57ms max=271.34ms p(90)=34.01ms  p(95)=36.74ms  p(99.9)=50.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 227578
     http_req_receiving.............: avg=84.25µs min=25.95µs med=55.56µs max=138.29ms p(90)=118.87µs p(95)=192.1µs  p(99.9)=1.5ms  
     http_req_sending...............: avg=34.84µs min=4.6µs   med=10.09µs max=156.41ms p(90)=23.24µs  p(95)=106.01µs p(99.9)=1.67ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26ms    min=1.78ms  med=25.46ms max=268.04ms p(90)=33.87ms  p(95)=36.61ms  p(99.9)=50.24ms
     http_reqs......................: 227578  1892.519818/s
     iteration_duration.............: avg=26.36ms min=7.72ms  med=25.79ms max=304.67ms p(90)=34.22ms  p(95)=36.96ms  p(99.9)=50.73ms
     iterations.....................: 227478  1891.688226/s
     success_rate...................: 100.00% ✓ 227478      ✗ 0     
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

     checks.........................: 100.00% ✓ 554991      ✗ 0     
     data_received..................: 16 GB   135 MB/s
     data_sent......................: 222 MB  1.8 MB/s
     http_req_blocked...............: avg=3.39µs  min=962ns   med=2.5µs   max=4.26ms   p(90)=4.34µs  p(95)=5.14µs   p(99.9)=26.42µs 
     http_req_connecting............: avg=528ns   min=0s      med=0s      max=4.21ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.19ms min=2.08ms  med=31.31ms max=307.33ms p(90)=45.42ms p(95)=50.11ms  p(99.9)=74.62ms 
       { expected_response:true }...: avg=32.19ms min=2.08ms  med=31.31ms max=307.33ms p(90)=45.42ms p(95)=50.11ms  p(99.9)=74.62ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 185097
     http_req_receiving.............: avg=73.66µs min=26.46µs med=60.69µs max=209.08ms p(90)=99.07µs p(95)=115.96µs p(99.9)=912.83µs
     http_req_sending...............: avg=21.48µs min=4.72µs  med=11.3µs  max=89.34ms  p(90)=18.61µs p(95)=22.44µs  p(99.9)=763.38µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.09ms min=2.03ms  med=31.22ms max=307.2ms  p(90)=45.33ms p(95)=50.01ms  p(99.9)=74.38ms 
     http_reqs......................: 185097  1538.534892/s
     iteration_duration.............: avg=32.42ms min=5.39ms  med=31.52ms max=328.29ms p(90)=45.63ms p(95)=50.31ms  p(99.9)=75.09ms 
     iterations.....................: 184997  1537.703687/s
     success_rate...................: 100.00% ✓ 184997      ✗ 0     
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

     checks.........................: 100.00% ✓ 535671      ✗ 0     
     data_received..................: 16 GB   130 MB/s
     data_sent......................: 215 MB  1.8 MB/s
     http_req_blocked...............: avg=2.87µs  min=942ns   med=2.05µs  max=3.97ms   p(90)=3.48µs  p(95)=4.15µs   p(99.9)=28.33µs 
     http_req_connecting............: avg=500ns   min=0s      med=0s      max=3.93ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.38ms min=2.08ms  med=32.49ms max=290.67ms p(90)=48.16ms p(95)=53.12ms  p(99.9)=75.92ms 
       { expected_response:true }...: avg=33.38ms min=2.08ms  med=32.49ms max=290.67ms p(90)=48.16ms p(95)=53.12ms  p(99.9)=75.92ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 178657
     http_req_receiving.............: avg=67.84µs min=24.41µs med=56.93µs max=66.37ms  p(90)=92.53µs p(95)=107.55µs p(99.9)=680.84µs
     http_req_sending...............: avg=20.76µs min=4.55µs  med=9.73µs  max=154.46ms p(90)=15.73µs p(95)=19.61µs  p(99.9)=733.61µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.29ms min=1.99ms  med=32.4ms  max=256.25ms p(90)=48.07ms p(95)=53.03ms  p(99.9)=75.78ms 
     http_reqs......................: 178657  1485.461184/s
     iteration_duration.............: avg=33.59ms min=4.27ms  med=32.68ms max=297.42ms p(90)=48.35ms p(95)=53.31ms  p(99.9)=76.31ms 
     iterations.....................: 178557  1484.629724/s
     success_rate...................: 100.00% ✓ 178557      ✗ 0     
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

     checks.........................: 100.00% ✓ 193983    ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   645 kB/s
     http_req_blocked...............: avg=4.29µs  min=1µs     med=2.43µs  max=3.91ms   p(90)=3.91µs   p(95)=4.49µs   p(99.9)=42.37µs 
     http_req_connecting............: avg=1.58µs  min=0s      med=0s      max=3.87ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.44ms min=3.98ms  med=89.71ms max=316.44ms p(90)=113.65ms p(95)=125.57ms p(99.9)=222.17ms
       { expected_response:true }...: avg=92.44ms min=3.98ms  med=89.71ms max=316.44ms p(90)=113.65ms p(95)=125.57ms p(99.9)=222.17ms
     http_req_failed................: 0.00%   ✓ 0         ✗ 64761
     http_req_receiving.............: avg=74.29µs min=28.02µs med=64.91µs max=101.12ms p(90)=98.3µs   p(95)=110.87µs p(99.9)=533.15µs
     http_req_sending...............: avg=18.56µs min=4.74µs  med=11.96µs max=89.79ms  p(90)=18.05µs  p(95)=19.94µs  p(99.9)=526.17µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.35ms min=3.91ms  med=89.63ms max=316.03ms p(90)=113.56ms p(95)=125.5ms  p(99.9)=221.79ms
     http_reqs......................: 64761   537.15327/s
     iteration_duration.............: avg=92.81ms min=24.71ms med=89.95ms max=328.89ms p(90)=113.89ms p(95)=125.85ms p(99.9)=224.32ms
     iterations.....................: 64661   536.32383/s
     success_rate...................: 100.00% ✓ 64661     ✗ 0    
     vus............................: 50      min=50      max=50 
     vus_max........................: 50      min=50      max=50
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

     checks.........................: 100.00% ✓ 189990     ✗ 0    
     data_received..................: 5.5 GB  46 MB/s
     data_sent......................: 76 MB   632 kB/s
     http_req_blocked...............: avg=7.59µs  min=1.09µs  med=2.8µs   max=10ms     p(90)=4.21µs   p(95)=4.76µs   p(99.9)=45.42µs 
     http_req_connecting............: avg=4.53µs  min=0s      med=0s      max=9.95ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=94.36ms min=4.49ms  med=92.28ms max=299.02ms p(90)=127.4ms  p(95)=137.84ms p(99.9)=179.57ms
       { expected_response:true }...: avg=94.36ms min=4.49ms  med=92.28ms max=299.02ms p(90)=127.4ms  p(95)=137.84ms p(99.9)=179.57ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63430
     http_req_receiving.............: avg=78.03µs min=29.06µs med=71.65µs max=126.97ms p(90)=103.14µs p(95)=115.13µs p(99.9)=488.48µs
     http_req_sending...............: avg=22.21µs min=4.78µs  med=13.69µs max=100.27ms p(90)=19.09µs  p(95)=20.87µs  p(99.9)=571.32µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.26ms min=4.37ms  med=92.18ms max=298.55ms p(90)=127.29ms p(95)=137.72ms p(99.9)=178.84ms
     http_reqs......................: 63430   526.103052/s
     iteration_duration.............: avg=94.75ms min=23.19ms med=92.57ms max=323.13ms p(90)=127.65ms p(95)=138.14ms p(99.9)=181.9ms 
     iterations.....................: 63330   525.273629/s
     success_rate...................: 100.00% ✓ 63330      ✗ 0    
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

     checks.........................: 100.00% ✓ 150546     ✗ 0    
     data_received..................: 4.4 GB  36 MB/s
     data_sent......................: 60 MB   500 kB/s
     http_req_blocked...............: avg=5.03µs   min=922ns   med=2.96µs   max=3.79ms   p(90)=4.29µs   p(95)=4.8µs    p(99.9)=164.09µs
     http_req_connecting............: avg=1.91µs   min=0s      med=0s       max=3.75ms   p(90)=0s       p(95)=0s       p(99.9)=62.47µs 
     http_req_duration..............: avg=119.11ms min=5.47ms  med=116.69ms max=336.01ms p(90)=156.11ms p(95)=168.3ms  p(99.9)=214.64ms
       { expected_response:true }...: avg=119.11ms min=5.47ms  med=116.69ms max=336.01ms p(90)=156.11ms p(95)=168.3ms  p(99.9)=214.64ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 50282
     http_req_receiving.............: avg=80.97µs  min=28.62µs med=76.59µs  max=71.4ms   p(90)=105.22µs p(95)=116.64µs p(99.9)=463.92µs
     http_req_sending...............: avg=20.91µs  min=4.78µs  med=15µs     max=72.4ms   p(90)=19.69µs  p(95)=21.46µs  p(99.9)=459.18µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=119.01ms min=5.4ms   med=116.6ms  max=335.83ms p(90)=156.01ms p(95)=168.17ms p(99.9)=214.51ms
     http_reqs......................: 50282   416.606377/s
     iteration_duration.............: avg=119.59ms min=34.06ms med=116.99ms max=344.69ms p(90)=156.41ms p(95)=168.57ms p(99.9)=217.03ms
     iterations.....................: 50182   415.777837/s
     success_rate...................: 100.00% ✓ 50182      ✗ 0    
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

     checks.........................: 100.00% ✓ 99258      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   329 kB/s
     http_req_blocked...............: avg=9.88µs   min=1.34µs  med=3.4µs    max=8.32ms   p(90)=4.77µs   p(95)=5.36µs   p(99.9)=2.87ms  
     http_req_connecting............: avg=5.76µs   min=0s      med=0s       max=8.09ms   p(90)=0s       p(95)=0s       p(99.9)=2.57ms  
     http_req_duration..............: avg=180.64ms min=7.48ms  med=179.55ms max=357.61ms p(90)=195.79ms p(95)=202.36ms p(99.9)=270.06ms
       { expected_response:true }...: avg=180.64ms min=7.48ms  med=179.55ms max=357.61ms p(90)=195.79ms p(95)=202.36ms p(99.9)=270.06ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33186
     http_req_receiving.............: avg=96.08µs  min=34.28µs med=84.7µs   max=102.59ms p(90)=114.54µs p(95)=125.42µs p(99.9)=589.57µs
     http_req_sending...............: avg=30.48µs  min=6.07µs  med=16.47µs  max=92.75ms  p(90)=20.94µs  p(95)=22.77µs  p(99.9)=1.6ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=180.51ms min=7.39ms  med=179.44ms max=356.24ms p(90)=195.69ms p(95)=202.25ms p(99.9)=269.75ms
     http_reqs......................: 33186   274.334659/s
     iteration_duration.............: avg=181.44ms min=54.1ms  med=179.87ms max=364.25ms p(90)=196.08ms p(95)=202.68ms p(99.9)=271.7ms 
     iterations.....................: 33086   273.508001/s
     success_rate...................: 100.00% ✓ 33086      ✗ 0    
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

     checks.........................: 100.00% ✓ 97428      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   323 kB/s
     http_req_blocked...............: avg=6.12µs   min=962ns   med=3.1µs    max=4.32ms   p(90)=4.38µs   p(95)=4.93µs   p(99.9)=1.26ms  
     http_req_connecting............: avg=2.85µs   min=0s      med=0s       max=4.28ms   p(90)=0s       p(95)=0s       p(99.9)=1.23ms  
     http_req_duration..............: avg=184.11ms min=5.79ms  med=167.55ms max=775.76ms p(90)=213.24ms p(95)=246.06ms p(99.9)=684.41ms
       { expected_response:true }...: avg=184.11ms min=5.79ms  med=167.55ms max=775.76ms p(90)=213.24ms p(95)=246.06ms p(99.9)=684.41ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32576
     http_req_receiving.............: avg=94.36µs  min=32.62µs med=88.87µs  max=58.47ms  p(90)=119.17µs p(95)=131.34µs p(99.9)=946.79µs
     http_req_sending...............: avg=34.57µs  min=5.28µs  med=16.77µs  max=174.51ms p(90)=20.69µs  p(95)=22.43µs  p(99.9)=555.85µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.98ms min=5.66ms  med=167.41ms max=775.67ms p(90)=213.08ms p(95)=245.89ms p(99.9)=684.32ms
     http_reqs......................: 32576   269.010642/s
     iteration_duration.............: avg=184.94ms min=32.29ms med=167.89ms max=775.96ms p(90)=213.65ms p(95)=246.86ms p(99.9)=684.69ms
     iterations.....................: 32476   268.184848/s
     success_rate...................: 100.00% ✓ 32476      ✗ 0    
     vus............................: 13      min=13       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

