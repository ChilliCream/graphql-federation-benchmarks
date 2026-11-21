## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-fed-net-11 | 16.8.0-p.17 | 5,395 | 5,415 | 5,383 | 0.2% | 369 MB | 70.1 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.17 | 5,357 | 5,421 | 5,344 | 0.6% | 362 MB | 69.2 KB |  |
| fusion-fed-net-11 | 16.7.6 | 5,351 | 5,388 | 5,293 | 0.7% | 369 MB | 70.7 KB |  |
| fusion-aot-11 | 16.7.6 | 5,273 | 5,324 | 5,255 | 0.6% | 125 MB | 24.2 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.17 | 5,254 | 5,273 | 5,249 | 0.2% | 120 MB | 23.4 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.17 | 5,202 | 5,231 | 5,167 | 0.4% | 116 MB | 22.9 KB |  |
| fusion-fed-aot-11 | 16.7.6 | 5,163 | 5,207 | 5,147 | 0.5% | 117 MB | 23.1 KB |  |
| feddi-gateway | 2026-11-03-0517 | 4,991 | 5,004 | 4,955 | 0.4% | 2,299 MB | 471.7 KB |  |
| hive-router | v0.3.17 | 4,675 | 4,695 | 4,626 | 0.6% | 109 MB | 23.9 KB |  |
| hive-router-nightly | v0.3.19-nightly.9815b25d | 4,484 | 4,494 | 4,443 | 0.5% | 94 MB | 21.4 KB |  |
| grafbase | 0.53.5 | 1,865 | 1,869 | 1,863 | 0.1% | 111 MB | 61.0 KB |  |
| cosmo | 0.373.0 | 1,459 | 1,463 | 1,451 | 0.3% | 170 MB | 119.4 KB |  |
| caliban | 3.2.1 | 1,413 | 1,414 | 1,412 | 0.1% | 5,689 MB | 4,122.9 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 600 | 603 | 599 | 0.3% | 2,614 MB | 4,461.5 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.b787dc86 | 476 | 477 | 476 | 0.1% | 193 MB | 415.3 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 401 | 401 | 400 | 0.1% | 199 MB | 509.2 KB |  |
| hive-gateway | 2.15.10 | 285 | 286 | 282 | 0.5% | 3,407 MB | 12,239.5 KB |  |
| apollo-gateway | 2.14.4 | 274 | 275 | 274 | 0.2% | 2,173 MB | 8,122.2 KB |  |
| apollo-router | — | — | — | — | — | — | — | benchmark run failed |
| fusion-net-11 | — | — | — | — | — | — | — | benchmark run failed |


### Details

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1943739     ✗ 0     
     data_received..................: 57 GB   472 MB/s
     data_sent......................: 779 MB  6.5 MB/s
     http_req_blocked...............: avg=5.5µs   min=831ns    med=2µs     max=103.96ms p(90)=3.17µs  p(95)=3.82µs   p(99.9)=28.54µs
     http_req_connecting............: avg=3.08µs  min=0s       med=0s      max=103.85ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.05ms  min=807.5µs  med=8.1ms   max=236.22ms p(90)=14.52ms p(95)=17.75ms  p(99.9)=30.28ms
       { expected_response:true }...: avg=9.05ms  min=807.5µs  med=8.1ms   max=236.22ms p(90)=14.52ms p(95)=17.75ms  p(99.9)=30.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 648013
     http_req_receiving.............: avg=95.45µs min=25.05µs  med=46.23µs max=108.4ms  p(90)=88.85µs p(95)=192.72µs p(99.9)=6.5ms  
     http_req_sending...............: avg=43.42µs min=4.07µs   med=8.28µs  max=75.32ms  p(90)=14.18µs p(95)=101.42µs p(99.9)=4.91ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.91ms  min=730.42µs med=7.99ms  max=193.68ms p(90)=14.28ms p(95)=17.46ms  p(99.9)=29.72ms
     http_reqs......................: 648013  5395.537316/s
     iteration_duration.............: avg=9.25ms  min=1.07ms   med=8.29ms  max=269.54ms p(90)=14.72ms p(95)=17.97ms  p(99.9)=30.62ms
     iterations.....................: 647913  5394.704688/s
     success_rate...................: 100.00% ✓ 647913      ✗ 0     
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

     checks.........................: 100.00% ✓ 1930278     ✗ 0     
     data_received..................: 56 GB   469 MB/s
     data_sent......................: 774 MB  6.4 MB/s
     http_req_blocked...............: avg=2.91µs   min=932ns    med=2.31µs  max=6.34ms   p(90)=3.49µs  p(95)=4.1µs    p(99.9)=31.99µs
     http_req_connecting............: avg=154ns    min=0s       med=0s      max=3.61ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.11ms   min=823.42µs med=8.13ms  max=236.67ms p(90)=14.79ms p(95)=18.15ms  p(99.9)=31.91ms
       { expected_response:true }...: avg=9.11ms   min=823.42µs med=8.13ms  max=236.67ms p(90)=14.79ms p(95)=18.15ms  p(99.9)=31.91ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 643526
     http_req_receiving.............: avg=100.03µs min=25.57µs  med=47.59µs max=134.17ms p(90)=89.62µs p(95)=198.65µs p(99.9)=6.66ms 
     http_req_sending...............: avg=44.19µs  min=4.37µs   med=8.49µs  max=135.42ms p(90)=14.23µs p(95)=103.7µs  p(99.9)=5.21ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.97ms   min=759.51µs med=8.02ms  max=148.95ms p(90)=14.54ms p(95)=17.86ms  p(99.9)=31.43ms
     http_reqs......................: 643526  5357.856946/s
     iteration_duration.............: avg=9.31ms   min=998.3µs  med=8.32ms  max=332.41ms p(90)=15ms    p(95)=18.37ms  p(99.9)=32.21ms
     iterations.....................: 643426  5357.024368/s
     success_rate...................: 100.00% ✓ 643426      ✗ 0     
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

     checks.........................: 100.00% ✓ 1927965     ✗ 0     
     data_received..................: 56 GB   468 MB/s
     data_sent......................: 773 MB  6.4 MB/s
     http_req_blocked...............: avg=2.47µs  min=791ns    med=1.94µs  max=5.63ms   p(90)=3.05µs  p(95)=3.63µs   p(99.9)=28.8µs 
     http_req_connecting............: avg=139ns   min=0s       med=0s      max=4.01ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.13ms  min=818.17µs med=8.23ms  max=275.14ms p(90)=14.56ms p(95)=17.6ms   p(99.9)=29.89ms
       { expected_response:true }...: avg=9.13ms  min=818.17µs med=8.23ms  max=275.14ms p(90)=14.56ms p(95)=17.6ms   p(99.9)=29.89ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 642755
     http_req_receiving.............: avg=92.5µs  min=25.4µs   med=46.99µs max=27.22ms  p(90)=87.36µs p(95)=191.57µs p(99.9)=5.91ms 
     http_req_sending...............: avg=40.62µs min=4.36µs   med=8.15µs  max=90.12ms  p(90)=13.61µs p(95)=98.96µs  p(99.9)=4.49ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.99ms  min=744.61µs med=8.12ms  max=255.57ms p(90)=14.35ms p(95)=17.33ms  p(99.9)=29.44ms
     http_reqs......................: 642755  5351.503506/s
     iteration_duration.............: avg=9.32ms  min=1.04ms   med=8.42ms  max=284.26ms p(90)=14.77ms p(95)=17.82ms  p(99.9)=30.16ms
     iterations.....................: 642655  5350.670917/s
     success_rate...................: 100.00% ✓ 642655      ✗ 0     
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

     checks.........................: 100.00% ✓ 1899870     ✗ 0     
     data_received..................: 55 GB   461 MB/s
     data_sent......................: 761 MB  6.3 MB/s
     http_req_blocked...............: avg=2.93µs  min=782ns    med=2.36µs  max=6.24ms   p(90)=3.6µs   p(95)=4.22µs   p(99.9)=32.34µs
     http_req_connecting............: avg=134ns   min=0s       med=0s      max=3.48ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.26ms  min=842.79µs med=8.28ms  max=268.04ms p(90)=15ms    p(95)=18.49ms  p(99.9)=31.5ms 
       { expected_response:true }...: avg=9.26ms  min=842.79µs med=8.28ms  max=268.04ms p(90)=15ms    p(95)=18.49ms  p(99.9)=31.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 633390
     http_req_receiving.............: avg=96.63µs min=25.02µs  med=46.45µs max=20.81ms  p(90)=89.77µs p(95)=201.5µs  p(99.9)=6.34ms 
     http_req_sending...............: avg=43.93µs min=4.62µs   med=8.77µs  max=174.57ms p(90)=14.85µs p(95)=105.78µs p(99.9)=4.84ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.12ms  min=784.99µs med=8.17ms  max=267.46ms p(90)=14.75ms p(95)=18.2ms   p(99.9)=31ms   
     http_reqs......................: 633390  5273.117004/s
     iteration_duration.............: avg=9.46ms  min=1.09ms   med=8.46ms  max=293.18ms p(90)=15.21ms p(95)=18.72ms  p(99.9)=31.76ms
     iterations.....................: 633290  5272.284481/s
     success_rate...................: 100.00% ✓ 633290      ✗ 0     
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

     checks.........................: 100.00% ✓ 1893210     ✗ 0     
     data_received..................: 55 GB   460 MB/s
     data_sent......................: 759 MB  6.3 MB/s
     http_req_blocked...............: avg=2.48µs  min=801ns    med=1.92µs  max=6.83ms   p(90)=3.01µs  p(95)=3.6µs    p(99.9)=27.08µs
     http_req_connecting............: avg=124ns   min=0s       med=0s      max=3.41ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.3ms   min=834.33µs med=8.41ms  max=266.06ms p(90)=14.92ms p(95)=17.93ms  p(99.9)=30.46ms
       { expected_response:true }...: avg=9.3ms   min=834.33µs med=8.41ms  max=266.06ms p(90)=14.92ms p(95)=17.93ms  p(99.9)=30.46ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 631170
     http_req_receiving.............: avg=93.12µs min=25.63µs  med=46.58µs max=85.48ms  p(90)=88.55µs p(95)=196.51µs p(99.9)=5.86ms 
     http_req_sending...............: avg=41.25µs min=4.13µs   med=8.17µs  max=180.71ms p(90)=13.78µs p(95)=100.74µs p(99.9)=4.45ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.17ms  min=791.38µs med=8.3ms   max=265.41ms p(90)=14.71ms p(95)=17.67ms  p(99.9)=30.09ms
     http_reqs......................: 631170  5254.808085/s
     iteration_duration.............: avg=9.49ms  min=1.33ms   med=8.59ms  max=287.52ms p(90)=15.12ms p(95)=18.15ms  p(99.9)=30.74ms
     iterations.....................: 631070  5253.975535/s
     success_rate...................: 100.00% ✓ 631070      ✗ 0     
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

     checks.........................: 100.00% ✓ 1874433     ✗ 0     
     data_received..................: 55 GB   455 MB/s
     data_sent......................: 751 MB  6.3 MB/s
     http_req_blocked...............: avg=4.09µs min=802ns    med=2.03µs  max=111.96ms p(90)=3.23µs  p(95)=3.84µs   p(99.9)=28.61µs
     http_req_connecting............: avg=1.61µs min=0s       med=0s      max=111.84ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.4ms  min=862.7µs  med=8.51ms  max=240.07ms p(90)=14.97ms p(95)=18.05ms  p(99.9)=30.63ms
       { expected_response:true }...: avg=9.4ms  min=862.7µs  med=8.51ms  max=240.07ms p(90)=14.97ms p(95)=18.05ms  p(99.9)=30.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 624911
     http_req_receiving.............: avg=92.9µs min=25.96µs  med=46.89µs max=72.09ms  p(90)=87.63µs p(95)=196.15µs p(99.9)=5.87ms 
     http_req_sending...............: avg=43.4µs min=3.98µs   med=8.32µs  max=213.81ms p(90)=14.22µs p(95)=101.37µs p(99.9)=4.45ms 
     http_req_tls_handshaking.......: avg=0s     min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.26ms min=790.77µs med=8.4ms   max=231.95ms p(90)=14.75ms p(95)=17.79ms  p(99.9)=30.2ms 
     http_reqs......................: 624911  5202.855523/s
     iteration_duration.............: avg=9.59ms min=1.28ms   med=8.69ms  max=331.44ms p(90)=15.17ms p(95)=18.26ms  p(99.9)=30.93ms
     iterations.....................: 624811  5202.022948/s
     success_rate...................: 100.00% ✓ 624811      ✗ 0     
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

     checks.........................: 100.00% ✓ 1860147     ✗ 0     
     data_received..................: 54 GB   452 MB/s
     data_sent......................: 745 MB  6.2 MB/s
     http_req_blocked...............: avg=4.98µs  min=861ns    med=2.36µs  max=57.08ms  p(90)=3.66µs  p(95)=4.3µs    p(99.9)=33.6µs 
     http_req_connecting............: avg=2.14µs  min=0s       med=0s      max=50.67ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.46ms  min=855.4µs  med=8.49ms  max=222.73ms p(90)=15.23ms p(95)=18.62ms  p(99.9)=31.53ms
       { expected_response:true }...: avg=9.46ms  min=855.4µs  med=8.49ms  max=222.73ms p(90)=15.23ms p(95)=18.62ms  p(99.9)=31.53ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 620149
     http_req_receiving.............: avg=99.31µs min=25.98µs  med=47.91µs max=56.33ms  p(90)=91.54µs p(95)=209.12µs p(99.9)=6.39ms 
     http_req_sending...............: avg=45.72µs min=4.37µs   med=8.67µs  max=69.21ms  p(90)=14.89µs p(95)=108.81µs p(99.9)=5.09ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.32ms  min=794.87µs med=8.38ms  max=183.34ms p(90)=14.99ms p(95)=18.35ms  p(99.9)=31.13ms
     http_reqs......................: 620149  5163.112228/s
     iteration_duration.............: avg=9.66ms  min=1.22ms   med=8.68ms  max=273.58ms p(90)=15.45ms p(95)=18.86ms  p(99.9)=31.82ms
     iterations.....................: 620049  5162.279668/s
     success_rate...................: 100.00% ✓ 620049      ✗ 0     
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

     checks.........................: 100.00% ✓ 1798203     ✗ 0     
     data_received..................: 52 GB   436 MB/s
     data_sent......................: 721 MB  6.0 MB/s
     http_req_blocked...............: avg=3.34µs  min=861ns    med=2.42µs  max=9.07ms   p(90)=3.82µs  p(95)=4.51µs   p(99.9)=33.57µs
     http_req_connecting............: avg=395ns   min=0s       med=0s      max=8.47ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.79ms  min=698.06µs med=8.89ms  max=275.02ms p(90)=15.19ms p(95)=18.64ms  p(99.9)=30.77ms
       { expected_response:true }...: avg=9.79ms  min=698.06µs med=8.89ms  max=275.02ms p(90)=15.19ms p(95)=18.64ms  p(99.9)=30.77ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 599501
     http_req_receiving.............: avg=97.01µs min=23.49µs  med=46.85µs max=109.02ms p(90)=93.07µs p(95)=205.27µs p(99.9)=6.37ms 
     http_req_sending...............: avg=45.24µs min=4.53µs   med=8.92µs  max=139.26ms p(90)=15.94µs p(95)=111.63µs p(99.9)=5.04ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.65ms  min=638.03µs med=8.79ms  max=271.88ms p(90)=14.9ms  p(95)=18.38ms  p(99.9)=30.15ms
     http_reqs......................: 599501  4991.561171/s
     iteration_duration.............: avg=9.99ms  min=1.07ms   med=9.07ms  max=297.09ms p(90)=15.41ms p(95)=18.86ms  p(99.9)=31.01ms
     iterations.....................: 599401  4990.728551/s
     success_rate...................: 100.00% ✓ 599401      ✗ 0     
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

     checks.........................: 100.00% ✓ 1684710     ✗ 0     
     data_received..................: 49 GB   409 MB/s
     data_sent......................: 675 MB  5.6 MB/s
     http_req_blocked...............: avg=2.74µs  min=812ns    med=2.13µs max=6.1ms    p(90)=3.53µs   p(95)=4.27µs   p(99.9)=35.11µs
     http_req_connecting............: avg=141ns   min=0s       med=0s     max=3.4ms    p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.47ms min=950.71µs med=9.72ms max=253.67ms p(90)=15.11ms  p(95)=18.48ms  p(99.9)=30.14ms
       { expected_response:true }...: avg=10.47ms min=950.71µs med=9.72ms max=253.67ms p(90)=15.11ms  p(95)=18.48ms  p(99.9)=30.14ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 561670
     http_req_receiving.............: avg=96.66µs min=23.95µs  med=49.9µs max=130.88ms p(90)=100.47µs p(95)=214.5µs  p(99.9)=5.78ms 
     http_req_sending...............: avg=44.19µs min=4.46µs   med=8.72µs max=142.98ms p(90)=15.84µs  p(95)=114.09µs p(99.9)=4.59ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.33ms min=899.41µs med=9.62ms max=253.2ms  p(90)=14.85ms  p(95)=18.19ms  p(99.9)=29.66ms
     http_reqs......................: 561670  4675.659518/s
     iteration_duration.............: avg=10.67ms min=1.58ms   med=9.9ms  max=313.37ms p(90)=15.33ms  p(95)=18.7ms   p(99.9)=30.46ms
     iterations.....................: 561570  4674.827061/s
     success_rate...................: 100.00% ✓ 561570      ✗ 0     
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

     checks.........................: 100.00% ✓ 1615674     ✗ 0     
     data_received..................: 47 GB   392 MB/s
     data_sent......................: 647 MB  5.4 MB/s
     http_req_blocked...............: avg=4.27µs  min=822ns    med=2.05µs  max=176.4ms  p(90)=3.32µs  p(95)=3.97µs   p(99.9)=29.23µs
     http_req_connecting............: avg=1.79µs  min=0s       med=0s      max=176.25ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.93ms min=955.33µs med=10.46ms max=252.75ms p(90)=14.89ms p(95)=17.94ms  p(99.9)=28.48ms
       { expected_response:true }...: avg=10.93ms min=955.33µs med=10.46ms max=252.75ms p(90)=14.89ms p(95)=17.94ms  p(99.9)=28.48ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 538658
     http_req_receiving.............: avg=92.38µs min=26.01µs  med=49.73µs max=20.06ms  p(90)=95.07µs p(95)=206.28µs p(99.9)=5.47ms 
     http_req_sending...............: avg=43.01µs min=4.43µs   med=8.8µs   max=220.67ms p(90)=15.32µs p(95)=107.72µs p(99.9)=4.2ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.79ms min=871.34µs med=10.37ms max=248.84ms p(90)=14.63ms p(95)=17.67ms  p(99.9)=28.09ms
     http_reqs......................: 538658  4484.230686/s
     iteration_duration.............: avg=11.13ms min=1.6ms    med=10.64ms max=326.8ms  p(90)=15.1ms  p(95)=18.17ms  p(99.9)=28.78ms
     iterations.....................: 538558  4483.398204/s
     success_rate...................: 100.00% ✓ 538558      ✗ 0     
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

     checks.........................: 100.00% ✓ 672873      ✗ 0     
     data_received..................: 20 GB   164 MB/s
     data_sent......................: 270 MB  2.2 MB/s
     http_req_blocked...............: avg=3.65µs  min=851ns   med=2.73µs  max=10.19ms  p(90)=4.96µs   p(95)=5.99µs   p(99.9)=42.19µs
     http_req_connecting............: avg=356ns   min=0s      med=0s      max=10.15ms  p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.5ms  min=1.9ms   med=25.94ms max=285.52ms p(90)=34.38ms  p(95)=37.15ms  p(99.9)=51.39ms
       { expected_response:true }...: avg=26.5ms  min=1.9ms   med=25.94ms max=285.52ms p(90)=34.38ms  p(95)=37.15ms  p(99.9)=51.39ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 224391
     http_req_receiving.............: avg=88.45µs min=27.16µs med=59.06µs max=59.44ms  p(90)=123.36µs p(95)=201.43µs p(99.9)=1.73ms 
     http_req_sending...............: avg=36.56µs min=4.82µs  med=10.91µs max=240.92ms p(90)=23.83µs  p(95)=111.79µs p(99.9)=1.7ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.37ms min=1.78ms  med=25.83ms max=276.14ms p(90)=34.25ms  p(95)=37.01ms  p(99.9)=51.11ms
     http_reqs......................: 224391  1865.910711/s
     iteration_duration.............: avg=26.74ms min=7.52ms  med=26.17ms max=312.11ms p(90)=34.61ms  p(95)=37.38ms  p(99.9)=51.73ms
     iterations.....................: 224291  1865.079167/s
     success_rate...................: 100.00% ✓ 224291      ✗ 0     
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

     checks.........................: 100.00% ✓ 526245      ✗ 0     
     data_received..................: 15 GB   128 MB/s
     data_sent......................: 211 MB  1.8 MB/s
     http_req_blocked...............: avg=4.47µs  min=972ns   med=2.55µs  max=9.04ms   p(90)=4.01µs  p(95)=4.68µs   p(99.9)=32.77µs 
     http_req_connecting............: avg=1.63µs  min=0s      med=0s      max=8.98ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.97ms min=2.05ms  med=33.06ms max=301.31ms p(90)=49.09ms p(95)=53.98ms  p(99.9)=78.19ms 
       { expected_response:true }...: avg=33.97ms min=2.05ms  med=33.06ms max=301.31ms p(90)=49.09ms p(95)=53.98ms  p(99.9)=78.19ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 175515
     http_req_receiving.............: avg=73.69µs min=26.75µs med=61.4µs  max=194.58ms p(90)=97.36µs p(95)=113.28µs p(99.9)=725.52µs
     http_req_sending...............: avg=20.99µs min=4.8µs   med=10.83µs max=80.06ms  p(90)=16.71µs p(95)=20.55µs  p(99.9)=779.91µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.87ms min=1.99ms  med=32.97ms max=293.74ms p(90)=48.99ms p(95)=53.89ms  p(99.9)=77.86ms 
     http_reqs......................: 175515  1459.237226/s
     iteration_duration.............: avg=34.19ms min=4.55ms  med=33.26ms max=312.6ms  p(90)=49.29ms p(95)=54.18ms  p(99.9)=78.63ms 
     iterations.....................: 175415  1458.405823/s
     success_rate...................: 100.00% ✓ 175415      ✗ 0     
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

     checks.........................: 100.00% ✓ 509910      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 204 MB  1.7 MB/s
     http_req_blocked...............: avg=3.05µs  min=951ns   med=2.24µs  max=3.52ms   p(90)=3.7µs   p(95)=4.36µs  p(99.9)=33.94µs 
     http_req_connecting............: avg=524ns   min=0s      med=0s      max=3.48ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=35.07ms min=2.18ms  med=34.04ms max=286.88ms p(90)=50.27ms p(95)=55.59ms p(99.9)=83.46ms 
       { expected_response:true }...: avg=35.07ms min=2.18ms  med=34.04ms max=286.88ms p(90)=50.27ms p(95)=55.59ms p(99.9)=83.46ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 170070
     http_req_receiving.............: avg=67.67µs min=25.47µs med=55.52µs max=183.3ms  p(90)=88.25µs p(95)=102.2µs p(99.9)=722.62µs
     http_req_sending...............: avg=20.03µs min=4.63µs  med=10.35µs max=189.46ms p(90)=15.78µs p(95)=18.95µs p(99.9)=687.98µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=34.98ms min=2.13ms  med=33.95ms max=286.36ms p(90)=50.19ms p(95)=55.5ms  p(99.9)=83.11ms 
     http_reqs......................: 170070  1413.838767/s
     iteration_duration.............: avg=35.29ms min=4.7ms   med=34.24ms max=302.03ms p(90)=50.47ms p(95)=55.8ms  p(99.9)=83.84ms 
     iterations.....................: 169970  1413.007439/s
     success_rate...................: 100.00% ✓ 169970      ✗ 0     
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

     checks.........................: 100.00% ✓ 216630     ✗ 0    
     data_received..................: 6.3 GB  53 MB/s
     data_sent......................: 87 MB   721 kB/s
     http_req_blocked...............: avg=4.73µs  min=1.08µs  med=2.73µs  max=6.69ms   p(90)=4.19µs   p(95)=4.81µs   p(99.9)=43.19µs 
     http_req_connecting............: avg=1.52µs  min=0s      med=0s      max=6.63ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=82.76ms min=3.44ms  med=80.29ms max=307.15ms p(90)=101.24ms p(95)=111.35ms p(99.9)=204.51ms
       { expected_response:true }...: avg=82.76ms min=3.44ms  med=80.29ms max=307.15ms p(90)=101.24ms p(95)=111.35ms p(99.9)=204.51ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 72310
     http_req_receiving.............: avg=78.11µs min=30.33µs med=67.77µs max=110.78ms p(90)=100.23µs p(95)=112.32µs p(99.9)=582.57µs
     http_req_sending...............: avg=22.5µs  min=5.06µs  med=12.82µs max=77.4ms   p(90)=18.3µs   p(95)=20.37µs  p(99.9)=600.01µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=82.66ms min=3.38ms  med=80.2ms  max=307.06ms p(90)=101.16ms p(95)=111.22ms p(99.9)=204.33ms
     http_reqs......................: 72310   600.12001/s
     iteration_duration.............: avg=83.1ms  min=26.52ms med=80.51ms max=321.18ms p(90)=101.48ms p(95)=111.61ms p(99.9)=206.48ms
     iterations.....................: 72210   599.290083/s
     success_rate...................: 100.00% ✓ 72210      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-nightly (HotChocolate subgraphs) (v3.0.0-preview.0-nightly.b787dc86)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 172020     ✗ 0    
     data_received..................: 5.0 GB  42 MB/s
     data_sent......................: 69 MB   572 kB/s
     http_req_blocked...............: avg=4.3µs    min=1.08µs  med=2.54µs   max=4.07ms   p(90)=3.85µs   p(95)=4.39µs   p(99.9)=51.53µs 
     http_req_connecting............: avg=1.56µs   min=0s      med=0s       max=4.03ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=104.24ms min=4.69ms  med=102.04ms max=317.22ms p(90)=138.79ms p(95)=149.98ms p(99.9)=197.67ms
       { expected_response:true }...: avg=104.24ms min=4.69ms  med=102.04ms max=317.22ms p(90)=138.79ms p(95)=149.98ms p(99.9)=197.67ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 57440
     http_req_receiving.............: avg=81.24µs  min=29.28µs med=70.28µs  max=209.1ms  p(90)=101.75µs p(95)=114.12µs p(99.9)=495.79µs
     http_req_sending...............: avg=24.18µs  min=4.96µs  med=13.76µs  max=173.47ms p(90)=19.31µs  p(95)=21.12µs  p(99.9)=497.62µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=104.13ms min=4.56ms  med=101.93ms max=313.25ms p(90)=138.68ms p(95)=149.85ms p(99.9)=197.1ms 
     http_reqs......................: 57440   476.201312/s
     iteration_duration.............: avg=104.66ms min=17.96ms med=102.31ms max=330.19ms p(90)=139.04ms p(95)=150.28ms p(99.9)=200.4ms 
     iterations.....................: 57340   475.37227/s
     success_rate...................: 100.00% ✓ 57340      ✗ 0    
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

     checks.........................: 100.00% ✓ 145023     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   482 kB/s
     http_req_blocked...............: avg=5.33µs   min=1.09µs  med=3.21µs   max=3.94ms   p(90)=4.54µs   p(95)=5.1µs    p(99.9)=716.34µs
     http_req_connecting............: avg=1.95µs   min=0s      med=0s       max=3.91ms   p(90)=0s       p(95)=0s       p(99.9)=695.14µs
     http_req_duration..............: avg=123.65ms min=5.38ms  med=121.3ms  max=344.25ms p(90)=161.86ms p(95)=174.24ms p(99.9)=224ms   
       { expected_response:true }...: avg=123.65ms min=5.38ms  med=121.3ms  max=344.25ms p(90)=161.86ms p(95)=174.24ms p(99.9)=224ms   
     http_req_failed................: 0.00%   ✓ 0          ✗ 48441
     http_req_receiving.............: avg=81.07µs  min=29.93µs med=73.85µs  max=75.59ms  p(90)=102.95µs p(95)=114.91µs p(99.9)=533.25µs
     http_req_sending...............: avg=20.68µs  min=5.32µs  med=14.99µs  max=60.57ms  p(90)=19.84µs  p(95)=21.6µs   p(99.9)=469.92µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=123.55ms min=5.29ms  med=121.19ms max=343.86ms p(90)=161.77ms p(95)=174.11ms p(99.9)=223.93ms
     http_reqs......................: 48441   401.338627/s
     iteration_duration.............: avg=124.16ms min=32.51ms med=121.61ms max=363.73ms p(90)=162.17ms p(95)=174.56ms p(99.9)=228.37ms
     iterations.....................: 48341   400.510117/s
     success_rate...................: 100.00% ✓ 48341      ✗ 0    
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

     checks.........................: 100.00% ✓ 103425     ✗ 0    
     data_received..................: 3.0 GB  25 MB/s
     data_sent......................: 42 MB   343 kB/s
     http_req_blocked...............: avg=5.65µs   min=1.1µs   med=2.77µs   max=4.05ms   p(90)=4.06µs   p(95)=4.61µs   p(99.9)=1.2ms   
     http_req_connecting............: avg=2.7µs    min=0s      med=0s       max=4.01ms   p(90)=0s       p(95)=0s       p(99.9)=1.17ms  
     http_req_duration..............: avg=173.49ms min=5.29ms  med=154.87ms max=754.54ms p(90)=196.36ms p(95)=223.74ms p(99.9)=691.69ms
       { expected_response:true }...: avg=173.49ms min=5.29ms  med=154.87ms max=754.54ms p(90)=196.36ms p(95)=223.74ms p(99.9)=691.69ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 34575
     http_req_receiving.............: avg=85.61µs  min=30.94µs med=79.98µs  max=77.14ms  p(90)=108.84µs p(95)=119.83µs p(99.9)=544.64µs
     http_req_sending...............: avg=19.76µs  min=5.26µs  med=15µs     max=40.57ms  p(90)=19.18µs  p(95)=20.73µs  p(99.9)=479.04µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=173.39ms min=5.19ms  med=154.78ms max=754.46ms p(90)=196.25ms p(95)=223.65ms p(99.9)=691.59ms
     http_reqs......................: 34575   285.402722/s
     iteration_duration.............: avg=174.23ms min=46.32ms med=155.17ms max=754.74ms p(90)=196.68ms p(95)=224.27ms p(99.9)=691.99ms
     iterations.....................: 34475   284.577262/s
     success_rate...................: 100.00% ✓ 34475      ✗ 0    
     vus............................: 17      min=17       max=50 
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

     checks.........................: 100.00% ✓ 99171      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   329 kB/s
     http_req_blocked...............: avg=6.2µs    min=1.37µs  med=3.29µs   max=3.72ms   p(90)=4.65µs   p(95)=5.26µs   p(99.9)=1.25ms  
     http_req_connecting............: avg=2.68µs   min=0s      med=0s       max=3.68ms   p(90)=0s       p(95)=0s       p(99.9)=1.23ms  
     http_req_duration..............: avg=180.77ms min=7.52ms  med=173.92ms max=406.86ms p(90)=207.63ms p(95)=212.91ms p(99.9)=284.68ms
       { expected_response:true }...: avg=180.77ms min=7.52ms  med=173.92ms max=406.86ms p(90)=207.63ms p(95)=212.91ms p(99.9)=284.68ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33157
     http_req_receiving.............: avg=90.48µs  min=33.5µs  med=84.15µs  max=49.93ms  p(90)=113.18µs p(95)=123.25µs p(99.9)=631.82µs
     http_req_sending...............: avg=29.01µs  min=5.71µs  med=16.62µs  max=75.6ms   p(90)=20.91µs  p(95)=22.66µs  p(99.9)=560.18µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=180.65ms min=7.44ms  med=173.81ms max=406.33ms p(90)=207.53ms p(95)=212.8ms  p(99.9)=284.59ms
     http_reqs......................: 33157   274.112947/s
     iteration_duration.............: avg=181.59ms min=31.49ms med=174.19ms max=414.54ms p(90)=207.91ms p(95)=213.2ms  p(99.9)=292.13ms
     iterations.....................: 33057   273.286235/s
     success_rate...................: 100.00% ✓ 33057      ✗ 0    
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

