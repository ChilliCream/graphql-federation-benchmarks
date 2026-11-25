## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.21 | 5,523 | 5,572 | 5,478 | 0.7% | 342 MB | 63.5 KB |  |
| fusion-net-11 | 16.7.7 | 5,490 | 5,500 | 5,428 | 0.5% | 356 MB | 66.4 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.21 | 5,406 | 5,430 | 5,386 | 0.3% | 351 MB | 66.5 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.21 | 5,398 | 5,406 | 5,389 | 0.1% | 98 MB | 18.6 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.21 | 5,392 | 5,398 | 5,363 | 0.3% | 102 MB | 19.3 KB |  |
| fusion-aot-11 | 16.7.7 | 5,358 | 5,362 | 5,317 | 0.3% | 109 MB | 20.9 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 5,350 | 5,369 | 5,302 | 0.5% | 117 MB | 22.4 KB |  |
| fusion-fed-net-11 | 16.7.7 | 5,318 | 5,338 | 5,308 | 0.3% | 359 MB | 69.2 KB |  |
| feddi-gateway | 2026-11-22-1912 | 5,061 | 5,105 | 5,049 | 0.5% | 2,319 MB | 469.2 KB |  |
| hive-router-nightly | v0.3.19-nightly.be76f6cb | 4,684 | 4,737 | 4,674 | 0.6% | 91 MB | 20.0 KB |  |
| hive-router | v0.3.17 | 4,554 | 4,587 | 4,545 | 0.4% | 97 MB | 21.7 KB |  |
| grafbase | 0.53.5 | 1,830 | 1,832 | 1,827 | 0.1% | 104 MB | 58.2 KB |  |
| cosmo | 0.373.0 | 1,517 | 1,517 | 1,514 | 0.1% | 164 MB | 111.0 KB |  |
| caliban | 3.2.1 | 1,497 | 1,499 | 1,492 | 0.2% | 5,912 MB | 4,044.2 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 619 | 622 | 616 | 0.4% | 2,619 MB | 4,331.9 KB |  |
| apollo-router | v2.19.1 | 536 | 536 | 535 | 0.1% | 172 MB | 328.2 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.0e21b2b0 | 477 | 482 | 469 | 1.2% | 197 MB | 423.3 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 432 | 433 | 431 | 0.2% | 199 MB | 472.1 KB |  |
| hive-gateway | 2.15.10 | 296 | 297 | 294 | 0.4% | 3,174 MB | 10,980.6 KB |  |
| apollo-gateway | 2.14.4 | 277 | 279 | 276 | 0.4% | 2,156 MB | 7,968.9 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1989735     ✗ 0     
     data_received..................: 58 GB   483 MB/s
     data_sent......................: 797 MB  6.6 MB/s
     http_req_blocked...............: avg=2.51µs  min=762ns    med=1.96µs  max=8.42ms   p(90)=3.11µs  p(95)=3.75µs   p(99.9)=28.03µs
     http_req_connecting............: avg=142ns   min=0s       med=0s      max=3.97ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.84ms  min=782.47µs med=7.9ms   max=265.54ms p(90)=14.32ms p(95)=17.6ms   p(99.9)=30.33ms
       { expected_response:true }...: avg=8.84ms  min=782.47µs med=7.9ms   max=265.54ms p(90)=14.32ms p(95)=17.6ms   p(99.9)=30.33ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 663345
     http_req_receiving.............: avg=95.54µs min=26.28µs  med=46.89µs max=183.55ms p(90)=86.8µs  p(95)=188.38µs p(99.9)=6.47ms 
     http_req_sending...............: avg=41.92µs min=4.43µs   med=8.14µs  max=181.99ms p(90)=13.5µs  p(95)=98.18µs  p(99.9)=4.78ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.7ms   min=721.62µs med=7.79ms  max=262.7ms  p(90)=14.07ms p(95)=17.3ms   p(99.9)=29.82ms
     http_reqs......................: 663345  5523.090818/s
     iteration_duration.............: avg=9.03ms  min=892.77µs med=8.08ms  max=283.82ms p(90)=14.52ms p(95)=17.82ms  p(99.9)=30.59ms
     iterations.....................: 663245  5522.258206/s
     success_rate...................: 100.00% ✓ 663245      ✗ 0     
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

     checks.........................: 100.00% ✓ 1978044     ✗ 0     
     data_received..................: 58 GB   480 MB/s
     data_sent......................: 793 MB  6.6 MB/s
     http_req_blocked...............: avg=2.6µs   min=791ns    med=1.87µs  max=102.1ms  p(90)=2.98µs  p(95)=3.55µs   p(99.9)=26.24µs
     http_req_connecting............: avg=154ns   min=0s       med=0s      max=3.86ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.89ms  min=770.84µs med=7.98ms  max=284.68ms p(90)=14.34ms p(95)=17.47ms  p(99.9)=30.08ms
       { expected_response:true }...: avg=8.89ms  min=770.84µs med=7.98ms  max=284.68ms p(90)=14.34ms p(95)=17.47ms  p(99.9)=30.08ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 659448
     http_req_receiving.............: avg=94.08µs min=25.37µs  med=46.04µs max=88.55ms  p(90)=85.59µs p(95)=187.97µs p(99.9)=6.28ms 
     http_req_sending...............: avg=40.96µs min=4.33µs   med=7.89µs  max=141.35ms p(90)=13.4µs  p(95)=96.96µs  p(99.9)=4.66ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.76ms  min=717.04µs med=7.87ms  max=284.44ms p(90)=14.12ms p(95)=17.2ms   p(99.9)=29.53ms
     http_reqs......................: 659448  5490.319535/s
     iteration_duration.............: avg=9.08ms  min=1.08ms   med=8.16ms  max=317.2ms  p(90)=14.54ms p(95)=17.69ms  p(99.9)=30.37ms
     iterations.....................: 659348  5489.486972/s
     success_rate...................: 100.00% ✓ 659348      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1947654     ✗ 0     
     data_received..................: 57 GB   473 MB/s
     data_sent......................: 781 MB  6.5 MB/s
     http_req_blocked...............: avg=2.68µs  min=782ns    med=2.07µs  max=6.94ms   p(90)=3.31µs  p(95)=3.96µs   p(99.9)=29.8µs 
     http_req_connecting............: avg=138ns   min=0s       med=0s      max=3.85ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.03ms  min=791.48µs med=8.08ms  max=266.74ms p(90)=14.51ms p(95)=17.75ms  p(99.9)=30.67ms
       { expected_response:true }...: avg=9.03ms  min=791.48µs med=8.08ms  max=266.74ms p(90)=14.51ms p(95)=17.75ms  p(99.9)=30.67ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 649318
     http_req_receiving.............: avg=94.57µs min=23.97µs  med=47.16µs max=79.8ms   p(90)=89.24µs p(95)=193.66µs p(99.9)=6.1ms  
     http_req_sending...............: avg=42.52µs min=4.4µs    med=8.35µs  max=195.04ms p(90)=14.29µs p(95)=101.53µs p(99.9)=4.79ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.89ms  min=723.11µs med=7.97ms  max=266.59ms p(90)=14.28ms p(95)=17.48ms  p(99.9)=30.17ms
     http_reqs......................: 649318  5406.328852/s
     iteration_duration.............: avg=9.23ms  min=1.07ms   med=8.27ms  max=277.8ms  p(90)=14.73ms p(95)=17.97ms  p(99.9)=30.99ms
     iterations.....................: 649218  5405.496235/s
     success_rate...................: 100.00% ✓ 649218      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1944987     ✗ 0     
     data_received..................: 57 GB   472 MB/s
     data_sent......................: 779 MB  6.5 MB/s
     http_req_blocked...............: avg=2.49µs  min=802ns    med=1.96µs  max=7.32ms   p(90)=3.08µs  p(95)=3.68µs   p(99.9)=28.48µs
     http_req_connecting............: avg=132ns   min=0s       med=0s      max=3.13ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.05ms  min=816.9µs  med=8.13ms  max=275.23ms p(90)=14.55ms p(95)=17.67ms  p(99.9)=30.37ms
       { expected_response:true }...: avg=9.05ms  min=816.9µs  med=8.13ms  max=275.23ms p(90)=14.55ms p(95)=17.67ms  p(99.9)=30.37ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 648429
     http_req_receiving.............: avg=99.19µs min=25.34µs  med=45.96µs max=204.28ms p(90)=87.59µs p(95)=189.96µs p(99.9)=6.39ms 
     http_req_sending...............: avg=41.5µs  min=4.34µs   med=8.23µs  max=163.48ms p(90)=13.8µs  p(95)=98.86µs  p(99.9)=4.57ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.91ms  min=751.53µs med=8.02ms  max=274.43ms p(90)=14.32ms p(95)=17.4ms   p(99.9)=29.75ms
     http_reqs......................: 648429  5398.722737/s
     iteration_duration.............: avg=9.24ms  min=1.07ms   med=8.32ms  max=285ms    p(90)=14.75ms p(95)=17.89ms  p(99.9)=30.64ms
     iterations.....................: 648329  5397.890152/s
     success_rate...................: 100.00% ✓ 648329      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1942665     ✗ 0     
     data_received..................: 57 GB   472 MB/s
     data_sent......................: 779 MB  6.5 MB/s
     http_req_blocked...............: avg=2.45µs  min=792ns    med=1.88µs  max=5.61ms   p(90)=2.98µs  p(95)=3.58µs   p(99.9)=26.28µs
     http_req_connecting............: avg=137ns   min=0s       med=0s      max=3.46ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.06ms  min=826.61µs med=8.16ms  max=282.04ms p(90)=14.49ms p(95)=17.55ms  p(99.9)=29.72ms
       { expected_response:true }...: avg=9.06ms  min=826.61µs med=8.16ms  max=282.04ms p(90)=14.49ms p(95)=17.55ms  p(99.9)=29.72ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 647655
     http_req_receiving.............: avg=90.41µs min=25.85µs  med=46.11µs max=184.05ms p(90)=85.18µs p(95)=185.97µs p(99.9)=5.8ms  
     http_req_sending...............: avg=41.78µs min=4.44µs   med=8.12µs  max=181.43ms p(90)=13.61µs p(95)=98.62µs  p(99.9)=4.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.93ms  min=762.82µs med=8.05ms  max=265.7ms  p(90)=14.27ms p(95)=17.29ms  p(99.9)=29.35ms
     http_reqs......................: 647655  5392.221055/s
     iteration_duration.............: avg=9.25ms  min=998.52µs med=8.35ms  max=305.18ms p(90)=14.69ms p(95)=17.77ms  p(99.9)=29.99ms
     iterations.....................: 647555  5391.388479/s
     success_rate...................: 100.00% ✓ 647555      ✗ 0     
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

     checks.........................: 100.00% ✓ 1930437     ✗ 0     
     data_received..................: 56 GB   469 MB/s
     data_sent......................: 774 MB  6.4 MB/s
     http_req_blocked...............: avg=2.52µs  min=792ns    med=1.92µs max=7.51ms   p(90)=3.03µs  p(95)=3.62µs   p(99.9)=28.24µs
     http_req_connecting............: avg=132ns   min=0s       med=0s     max=3.46ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.12ms  min=847.34µs med=8.21ms max=269.08ms p(90)=14.62ms p(95)=17.77ms  p(99.9)=30.16ms
       { expected_response:true }...: avg=9.12ms  min=847.34µs med=8.21ms max=269.08ms p(90)=14.62ms p(95)=17.77ms  p(99.9)=30.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 643579
     http_req_receiving.............: avg=90.76µs min=23.49µs  med=44.5µs max=185.43ms p(90)=85.44µs p(95)=190.71µs p(99.9)=5.96ms 
     http_req_sending...............: avg=41.28µs min=4.37µs   med=8.18µs max=169.56ms p(90)=13.91µs p(95)=100µs    p(99.9)=4.57ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.99ms  min=793.57µs med=8.11ms max=268.57ms p(90)=14.4ms  p(95)=17.51ms  p(99.9)=29.76ms
     http_reqs......................: 643579  5358.14144/s
     iteration_duration.............: avg=9.31ms  min=1.22ms   med=8.39ms max=279.17ms p(90)=14.83ms p(95)=17.99ms  p(99.9)=30.45ms
     iterations.....................: 643479  5357.308886/s
     success_rate...................: 100.00% ✓ 643479      ✗ 0     
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

     checks.........................: 100.00% ✓ 1927686     ✗ 0     
     data_received..................: 56 GB   468 MB/s
     data_sent......................: 773 MB  6.4 MB/s
     http_req_blocked...............: avg=2.45µs  min=781ns    med=1.9µs   max=9.04ms   p(90)=3µs     p(95)=3.58µs   p(99.9)=26.78µs
     http_req_connecting............: avg=129ns   min=0s       med=0s      max=3.52ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.13ms  min=866.14µs med=8.25ms  max=244.69ms p(90)=14.54ms p(95)=17.6ms   p(99.9)=29.67ms
       { expected_response:true }...: avg=9.13ms  min=866.14µs med=8.25ms  max=244.69ms p(90)=14.54ms p(95)=17.6ms   p(99.9)=29.67ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 642662
     http_req_receiving.............: avg=96.92µs min=24.28µs  med=44.78µs max=219.93ms p(90)=84.68µs p(95)=191.05µs p(99.9)=5.71ms 
     http_req_sending...............: avg=40.8µs  min=4.14µs   med=8µs     max=224.1ms  p(90)=13.84µs p(95)=101.91µs p(99.9)=4.54ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.99ms  min=795.64µs med=8.15ms  max=70.99ms  p(90)=14.33ms p(95)=17.35ms  p(99.9)=29.11ms
     http_reqs......................: 642662  5350.305534/s
     iteration_duration.............: avg=9.32ms  min=1.18ms   med=8.43ms  max=336.44ms p(90)=14.74ms p(95)=17.81ms  p(99.9)=30.08ms
     iterations.....................: 642562  5349.473011/s
     success_rate...................: 100.00% ✓ 642562      ✗ 0     
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

     checks.........................: 100.00% ✓ 1916109     ✗ 0     
     data_received..................: 56 GB   465 MB/s
     data_sent......................: 768 MB  6.4 MB/s
     http_req_blocked...............: avg=3.09µs  min=992ns    med=2.48µs  max=6.52ms   p(90)=3.71µs  p(95)=4.37µs   p(99.9)=32.97µs
     http_req_connecting............: avg=143ns   min=0s       med=0s      max=3.97ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.18ms  min=802.98µs med=8.19ms  max=268.85ms p(90)=14.83ms p(95)=18.21ms  p(99.9)=31.45ms
       { expected_response:true }...: avg=9.18ms  min=802.98µs med=8.19ms  max=268.85ms p(90)=14.83ms p(95)=18.21ms  p(99.9)=31.45ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 638803
     http_req_receiving.............: avg=99.12µs min=25.69µs  med=48.08µs max=137.05ms p(90)=90.51µs p(95)=197.12µs p(99.9)=6.58ms 
     http_req_sending...............: avg=44.79µs min=4.63µs   med=8.91µs  max=143.31ms p(90)=14.7µs  p(95)=103.22µs p(99.9)=5.2ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.03ms  min=736.73µs med=8.08ms  max=267.11ms p(90)=14.59ms p(95)=17.91ms  p(99.9)=30.85ms
     http_reqs......................: 638803  5318.521139/s
     iteration_duration.............: avg=9.38ms  min=996.8µs  med=8.38ms  max=278.94ms p(90)=15.05ms p(95)=18.43ms  p(99.9)=31.74ms
     iterations.....................: 638703  5317.688563/s
     success_rate...................: 100.00% ✓ 638703      ✗ 0     
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

     checks.........................: 100.00% ✓ 1823769     ✗ 0     
     data_received..................: 53 GB   442 MB/s
     data_sent......................: 731 MB  6.1 MB/s
     http_req_blocked...............: avg=2.97µs   min=801ns    med=2.36µs  max=6.51ms   p(90)=3.74µs  p(95)=4.43µs   p(99.9)=33.69µs
     http_req_connecting............: avg=137ns    min=0s       med=0s      max=3.54ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.65ms   min=835.12µs med=8.73ms  max=294.05ms p(90)=15.57ms p(95)=19ms     p(99.9)=32.04ms
       { expected_response:true }...: avg=9.65ms   min=835.12µs med=8.73ms  max=294.05ms p(90)=15.57ms p(95)=19ms     p(99.9)=32.04ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 608023
     http_req_receiving.............: avg=105.17µs min=24.46µs  med=48.34µs max=127.39ms p(90)=95.51µs p(95)=213.83µs p(99.9)=6.56ms 
     http_req_sending...............: avg=42.75µs  min=4.4µs    med=8.79µs  max=91.52ms  p(90)=15.39µs p(95)=110.17µs p(99.9)=4.67ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.51ms   min=759.18µs med=8.6ms   max=293.13ms p(90)=15.32ms p(95)=18.71ms  p(99.9)=31.55ms
     http_reqs......................: 608023  5061.730034/s
     iteration_duration.............: avg=9.85ms   min=1.26ms   med=8.92ms  max=307.08ms p(90)=15.78ms p(95)=19.22ms  p(99.9)=32.35ms
     iterations.....................: 607923  5060.897544/s
     success_rate...................: 100.00% ✓ 607923      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.19-nightly.be76f6cb)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1687974     ✗ 0     
     data_received..................: 49 GB   410 MB/s
     data_sent......................: 676 MB  5.6 MB/s
     http_req_blocked...............: avg=3.19µs   min=932ns    med=2.54µs max=7.02ms   p(90)=4µs      p(95)=4.77µs   p(99.9)=37.14µs
     http_req_connecting............: avg=156ns    min=0s       med=0s     max=3.9ms    p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.44ms  min=937.94µs med=9.7ms  max=256.48ms p(90)=15.09ms  p(95)=18.78ms  p(99.9)=30.85ms
       { expected_response:true }...: avg=10.44ms  min=937.94µs med=9.7ms  max=256.48ms p(90)=15.09ms  p(95)=18.78ms  p(99.9)=30.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 562758
     http_req_receiving.............: avg=100.88µs min=25.83µs  med=51.2µs max=103.79ms p(90)=100.77µs p(95)=214.24µs p(99.9)=6.22ms 
     http_req_sending...............: avg=46.26µs  min=4.49µs   med=9.19µs max=107.52ms p(90)=16.43µs  p(95)=115.56µs p(99.9)=5.03ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s     max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.3ms   min=867.44µs med=9.6ms  max=254.91ms p(90)=14.8ms   p(95)=18.48ms  p(99.9)=30.42ms
     http_reqs......................: 562758  4684.744905/s
     iteration_duration.............: avg=10.65ms  min=1.49ms   med=9.89ms max=274.91ms p(90)=15.31ms  p(95)=19.01ms  p(99.9)=31.18ms
     iterations.....................: 562658  4683.912443/s
     success_rate...................: 100.00% ✓ 562658      ✗ 0     
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

     checks.........................: 100.00% ✓ 1640946     ✗ 0     
     data_received..................: 48 GB   398 MB/s
     data_sent......................: 658 MB  5.5 MB/s
     http_req_blocked...............: avg=2.61µs   min=852ns    med=2.06µs  max=5.48ms   p(90)=3.26µs  p(95)=3.88µs   p(99.9)=28.07µs
     http_req_connecting............: avg=175ns    min=0s       med=0s      max=4.21ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.76ms  min=937.26µs med=10.24ms max=290.43ms p(90)=14.83ms p(95)=17.95ms  p(99.9)=28.89ms
       { expected_response:true }...: avg=10.76ms  min=937.26µs med=10.24ms max=290.43ms p(90)=14.83ms p(95)=17.95ms  p(99.9)=28.89ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 547082
     http_req_receiving.............: avg=102.17µs min=22.96µs  med=48.56µs max=258.12ms p(90)=92.82µs p(95)=203.81µs p(99.9)=5.98ms 
     http_req_sending...............: avg=42.48µs  min=4.46µs   med=8.73µs  max=242.91ms p(90)=14.87µs p(95)=107.83µs p(99.9)=4.44ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.62ms  min=889.55µs med=10.15ms max=123.99ms p(90)=14.57ms p(95)=17.67ms  p(99.9)=28.49ms
     http_reqs......................: 547082  4554.153633/s
     iteration_duration.............: avg=10.95ms  min=1.59ms   med=10.42ms max=304.7ms  p(90)=15.04ms p(95)=18.17ms  p(99.9)=29.12ms
     iterations.....................: 546982  4553.321189/s
     success_rate...................: 100.00% ✓ 546982      ✗ 0     
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

     checks.........................: 100.00% ✓ 660048      ✗ 0     
     data_received..................: 19 GB   160 MB/s
     data_sent......................: 265 MB  2.2 MB/s
     http_req_blocked...............: avg=4.97µs  min=1.06µs  med=3.07µs  max=9.61ms   p(90)=5.11µs   p(95)=6.21µs   p(99.9)=43.59µs
     http_req_connecting............: avg=1.33µs  min=0s      med=0s      max=9.56ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=27.01ms min=1.85ms  med=26.49ms max=290.96ms p(90)=35.02ms  p(95)=37.78ms  p(99.9)=51.56ms
       { expected_response:true }...: avg=27.01ms min=1.85ms  med=26.49ms max=290.96ms p(90)=35.02ms  p(95)=37.78ms  p(99.9)=51.56ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 220116
     http_req_receiving.............: avg=91.27µs min=28.15µs med=62.13µs max=193.16ms p(90)=124.91µs p(95)=210.56µs p(99.9)=1.61ms 
     http_req_sending...............: avg=37.24µs min=5.13µs  med=11.54µs max=81.97ms  p(90)=23.98µs  p(95)=115.54µs p(99.9)=1.82ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.88ms min=1.8ms   med=26.37ms max=290.19ms p(90)=34.88ms  p(95)=37.64ms  p(99.9)=51.22ms
     http_reqs......................: 220116  1830.285406/s
     iteration_duration.............: avg=27.26ms min=7.72ms  med=26.72ms max=311.26ms p(90)=35.25ms  p(95)=38.01ms  p(99.9)=51.88ms
     iterations.....................: 220016  1829.453896/s
     success_rate...................: 100.00% ✓ 220016      ✗ 0     
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

     checks.........................: 100.00% ✓ 547179      ✗ 0     
     data_received..................: 16 GB   133 MB/s
     data_sent......................: 219 MB  1.8 MB/s
     http_req_blocked...............: avg=3µs     min=942ns   med=2.16µs  max=4.07ms   p(90)=3.57µs  p(95)=4.23µs   p(99.9)=27.94µs 
     http_req_connecting............: avg=538ns   min=0s      med=0s      max=4.03ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.67ms min=1.97ms  med=31.82ms max=290.23ms p(90)=47.08ms p(95)=51.87ms  p(99.9)=74.37ms 
       { expected_response:true }...: avg=32.67ms min=1.97ms  med=31.82ms max=290.23ms p(90)=47.08ms p(95)=51.87ms  p(99.9)=74.37ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 182493
     http_req_receiving.............: avg=67.93µs min=25.29µs med=57.72µs max=36.73ms  p(90)=93.79µs p(95)=108.94µs p(99.9)=672.78µs
     http_req_sending...............: avg=22.2µs  min=4.68µs  med=10.46µs max=160.78ms p(90)=16.97µs p(95)=20.66µs  p(99.9)=751.88µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.58ms min=1.92ms  med=31.74ms max=289.84ms p(90)=46.99ms p(95)=51.79ms  p(99.9)=74.22ms 
     http_reqs......................: 182493  1517.329379/s
     iteration_duration.............: avg=32.89ms min=3.67ms  med=32.02ms max=317.65ms p(90)=47.27ms p(95)=52.07ms  p(99.9)=74.78ms 
     iterations.....................: 182393  1516.497934/s
     success_rate...................: 100.00% ✓ 182393      ✗ 0     
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

     checks.........................: 100.00% ✓ 540063      ✗ 0     
     data_received..................: 16 GB   131 MB/s
     data_sent......................: 216 MB  1.8 MB/s
     http_req_blocked...............: avg=4.11µs  min=1.11µs  med=2.9µs   max=9.33ms   p(90)=4.49µs  p(95)=5.21µs   p(99.9)=39.11µs
     http_req_connecting............: avg=828ns   min=0s      med=0s      max=6.57ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.08ms min=2.03ms  med=32.14ms max=279.31ms p(90)=46.99ms p(95)=51.98ms  p(99.9)=79.5ms 
       { expected_response:true }...: avg=33.08ms min=2.03ms  med=32.14ms max=279.31ms p(90)=46.99ms p(95)=51.98ms  p(99.9)=79.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 180121
     http_req_receiving.............: avg=73.01µs min=27.26µs med=61.76µs max=6.76ms   p(90)=97.5µs  p(95)=113.38µs p(99.9)=870.2µs
     http_req_sending...............: avg=23.56µs min=5.14µs  med=12.31µs max=154.73ms p(90)=18.16µs p(95)=21.86µs  p(99.9)=802µs  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=32.98ms min=1.95ms  med=32.04ms max=277.28ms p(90)=46.89ms p(95)=51.87ms  p(99.9)=79.16ms
     http_reqs......................: 180121  1497.407307/s
     iteration_duration.............: avg=33.32ms min=5.14ms  med=32.35ms max=296.36ms p(90)=47.2ms  p(95)=52.19ms  p(99.9)=79.92ms
     iterations.....................: 180021  1496.575973/s
     success_rate...................: 100.00% ✓ 180021      ✗ 0     
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

     checks.........................: 100.00% ✓ 223560     ✗ 0    
     data_received..................: 6.5 GB  54 MB/s
     data_sent......................: 90 MB   744 kB/s
     http_req_blocked...............: avg=4.68µs  min=1.16µs  med=3.12µs  max=4.04ms   p(90)=4.63µs   p(95)=5.31µs   p(99.9)=44.71µs 
     http_req_connecting............: avg=1.31µs  min=0s      med=0s      max=4ms      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=80.18ms min=3.47ms  med=77.38ms max=326.62ms p(90)=96.7ms   p(95)=106.19ms p(99.9)=203.25ms
       { expected_response:true }...: avg=80.18ms min=3.47ms  med=77.38ms max=326.62ms p(90)=96.7ms   p(95)=106.19ms p(99.9)=203.25ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 74620
     http_req_receiving.............: avg=80.22µs min=29.09µs med=72.87µs max=44.94ms  p(90)=105.81µs p(95)=117.87µs p(99.9)=547.56µs
     http_req_sending...............: avg=23.59µs min=5.32µs  med=14.37µs max=152.05ms p(90)=20.25µs  p(95)=22.33µs  p(99.9)=568.61µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=80.08ms min=3.37ms  med=77.28ms max=326.07ms p(90)=96.6ms   p(95)=106.04ms p(99.9)=203.17ms
     http_reqs......................: 74620   619.31723/s
     iteration_duration.............: avg=80.52ms min=19.93ms med=77.63ms max=336.05ms p(90)=96.94ms  p(95)=106.46ms p(99.9)=204.23ms
     iterations.....................: 74520   618.487269/s
     success_rate...................: 100.00% ✓ 74520      ✗ 0    
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

     checks.........................: 100.00% ✓ 193611     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   644 kB/s
     http_req_blocked...............: avg=4.36µs  min=1.04µs  med=2.69µs  max=3.44ms   p(90)=4.06µs   p(95)=4.61µs   p(99.9)=45.21µs 
     http_req_connecting............: avg=1.46µs  min=0s      med=0s      max=3.4ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.6ms  min=4.4ms   med=90.56ms max=321.4ms  p(90)=125.04ms p(95)=134.95ms p(99.9)=175.43ms
       { expected_response:true }...: avg=92.6ms  min=4.4ms   med=90.56ms max=321.4ms  p(90)=125.04ms p(95)=134.95ms p(99.9)=175.43ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64637
     http_req_receiving.............: avg=76.8µs  min=27.28µs med=72.49µs max=30.41ms  p(90)=102.94µs p(95)=115.06µs p(99.9)=504.07µs
     http_req_sending...............: avg=20.23µs min=4.92µs  med=13.82µs max=109.62ms p(90)=19.51µs  p(95)=21.34µs  p(99.9)=486.63µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.5ms  min=4.27ms  med=90.46ms max=321.16ms p(90)=124.94ms p(95)=134.84ms p(99.9)=175.11ms
     http_reqs......................: 64637   536.092324/s
     iteration_duration.............: avg=92.98ms min=17.08ms med=90.83ms max=330.87ms p(90)=125.3ms  p(95)=135.21ms p(99.9)=176.65ms
     iterations.....................: 64537   535.262935/s
     success_rate...................: 100.00% ✓ 64537      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-nightly (HotChocolate subgraphs) (v3.0.0-preview.0-nightly.0e21b2b0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 172647     ✗ 0    
     data_received..................: 5.0 GB  42 MB/s
     data_sent......................: 69 MB   574 kB/s
     http_req_blocked...............: avg=4.47µs   min=972ns   med=2.72µs   max=3.43ms   p(90)=4.1µs    p(95)=4.61µs   p(99.9)=49.32µs 
     http_req_connecting............: avg=1.55µs   min=0s      med=0s       max=3.39ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=103.87ms min=4.7ms   med=101.52ms max=296.69ms p(90)=138.78ms p(95)=150.27ms p(99.9)=198.2ms 
       { expected_response:true }...: avg=103.87ms min=4.7ms   med=101.52ms max=296.69ms p(90)=138.78ms p(95)=150.27ms p(99.9)=198.2ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 57649
     http_req_receiving.............: avg=76.55µs  min=28.46µs med=68.75µs  max=108.02ms p(90)=99.95µs  p(95)=112.93µs p(99.9)=499.52µs
     http_req_sending...............: avg=19.49µs  min=4.8µs   med=13.08µs  max=87.04ms  p(90)=18.51µs  p(95)=20.24µs  p(99.9)=514.52µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=103.78ms min=4.58ms  med=101.43ms max=296.29ms p(90)=138.68ms p(95)=150.17ms p(99.9)=198ms   
     http_reqs......................: 57649   477.893414/s
     iteration_duration.............: avg=104.28ms min=17.41ms med=101.8ms  max=329.7ms  p(90)=139.03ms p(95)=150.54ms p(99.9)=199.43ms
     iterations.....................: 57549   477.064444/s
     success_rate...................: 100.00% ✓ 57549      ✗ 0    
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

     checks.........................: 100.00% ✓ 156411     ✗ 0    
     data_received..................: 4.6 GB  38 MB/s
     data_sent......................: 63 MB   520 kB/s
     http_req_blocked...............: avg=4.91µs   min=982ns   med=2.98µs   max=3.99ms   p(90)=4.37µs   p(95)=4.92µs   p(99.9)=140.66µs
     http_req_connecting............: avg=1.72µs   min=0s      med=0s       max=3.95ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=114.63ms min=5.25ms  med=112.38ms max=347.43ms p(90)=149.61ms p(95)=161.07ms p(99.9)=213.47ms
       { expected_response:true }...: avg=114.63ms min=5.25ms  med=112.38ms max=347.43ms p(90)=149.61ms p(95)=161.07ms p(99.9)=213.47ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 52237
     http_req_receiving.............: avg=80.05µs  min=29.76µs med=76.99µs  max=27.96ms  p(90)=105.94µs p(95)=117.42µs p(99.9)=488.95µs
     http_req_sending...............: avg=19.8µs   min=5.09µs  med=15.38µs  max=49.96ms  p(90)=20.15µs  p(95)=21.86µs  p(99.9)=509.48µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=114.53ms min=5.18ms  med=112.29ms max=346.67ms p(90)=149.52ms p(95)=160.98ms p(99.9)=213.39ms
     http_reqs......................: 52237   432.904586/s
     iteration_duration.............: avg=115.1ms  min=22.18ms med=112.68ms max=360.81ms p(90)=149.9ms  p(95)=161.38ms p(99.9)=216.95ms
     iterations.....................: 52137   432.075854/s
     success_rate...................: 100.00% ✓ 52137      ✗ 0    
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

     checks.........................: 100.00% ✓ 107109     ✗ 0    
     data_received..................: 3.1 GB  26 MB/s
     data_sent......................: 43 MB   356 kB/s
     http_req_blocked...............: avg=5.84µs   min=1.05µs  med=3.08µs   max=3.57ms   p(90)=4.43µs   p(95)=4.98µs   p(99.9)=1.27ms  
     http_req_connecting............: avg=2.56µs   min=0s      med=0s       max=3.53ms   p(90)=0s       p(95)=0s       p(99.9)=1.13ms  
     http_req_duration..............: avg=167.42ms min=5.16ms  med=149.87ms max=819.41ms p(90)=192.47ms p(95)=214.1ms  p(99.9)=710.8ms 
       { expected_response:true }...: avg=167.42ms min=5.16ms  med=149.87ms max=819.41ms p(90)=192.47ms p(95)=214.1ms  p(99.9)=710.8ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 35803
     http_req_receiving.............: avg=90.46µs  min=32.34µs med=82.91µs  max=110.33ms p(90)=112.55µs p(95)=123.88µs p(99.9)=614.13µs
     http_req_sending...............: avg=24.21µs  min=5.3µs   med=15.3µs   max=73.72ms  p(90)=19.62µs  p(95)=21.37µs  p(99.9)=529.84µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=167.3ms  min=5.05ms  med=149.75ms max=819.23ms p(90)=192.36ms p(95)=213.94ms p(99.9)=710.73ms
     http_reqs......................: 35803   296.076009/s
     iteration_duration.............: avg=168.14ms min=25.25ms med=150.19ms max=819.65ms p(90)=192.82ms p(95)=214.68ms p(99.9)=710.98ms
     iterations.....................: 35703   295.24905/s
     success_rate...................: 100.00% ✓ 35703      ✗ 0    
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

     checks.........................: 100.00% ✓ 100227     ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   333 kB/s
     http_req_blocked...............: avg=6.24µs   min=1.21µs  med=3.34µs   max=4.09ms   p(90)=4.73µs   p(95)=5.33µs   p(99.9)=1.02ms  
     http_req_connecting............: avg=2.65µs   min=0s      med=0s       max=4.04ms   p(90)=0s       p(95)=0s       p(99.9)=1ms     
     http_req_duration..............: avg=178.9ms  min=7.49ms  med=178.1ms  max=352ms    p(90)=219.85ms p(95)=224.72ms p(99.9)=296.86ms
       { expected_response:true }...: avg=178.9ms  min=7.49ms  med=178.1ms  max=352ms    p(90)=219.85ms p(95)=224.72ms p(99.9)=296.86ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33509
     http_req_receiving.............: avg=90.14µs  min=32.09µs med=85.04µs  max=69.28ms  p(90)=114.74µs p(95)=125.11µs p(99.9)=586.92µs
     http_req_sending...............: avg=25.09µs  min=5.72µs  med=16.31µs  max=53.74ms  p(90)=20.82µs  p(95)=22.63µs  p(99.9)=550.81µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=178.78ms min=7.4ms   med=177.97ms max=351.45ms p(90)=219.75ms p(95)=224.63ms p(99.9)=296.77ms
     http_reqs......................: 33509   277.062283/s
     iteration_duration.............: avg=179.69ms min=36.16ms med=178.79ms max=372.28ms p(90)=220.14ms p(95)=224.99ms p(99.9)=300.29ms
     iterations.....................: 33409   276.235453/s
     success_rate...................: 100.00% ✓ 33409      ✗ 0    
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

