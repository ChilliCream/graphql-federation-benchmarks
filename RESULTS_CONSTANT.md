## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 5,081 | 5,097 | 5,075 | 0.2% | 379 MB | 76.4 KB |  |
| fusion-net-11 | 16.7.3 | 5,068 | 5,076 | 5,046 | 0.2% | 369 MB | 74.5 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,856 | 4,895 | 4,830 | 0.5% | 371 MB | 78.2 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,812 | 4,824 | 4,793 | 0.3% | 123 MB | 26.1 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,770 | 4,790 | 4,744 | 0.4% | 385 MB | 82.6 KB |  |
| fusion-aot-11 | 16.7.3 | 4,685 | 4,691 | 4,664 | 0.2% | 120 MB | 26.3 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,564 | 4,597 | 4,546 | 0.4% | 128 MB | 28.7 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,515 | 4,550 | 4,491 | 0.5% | 135 MB | 30.6 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,318 | 4,347 | 4,191 | 1.6% | 2,311 MB | 548.1 KB |  |
| hive-router | v0.3.10 | 2,960 | 2,981 | 2,950 | 0.4% | 91 MB | 31.6 KB |  |
| grafbase | 0.53.5 | 1,765 | 1,773 | 1,763 | 0.2% | 101 MB | 58.6 KB |  |
| caliban | 3.2.0 | 1,523 | 1,524 | 1,519 | 0.1% | 4,976 MB | 3,345.6 KB |  |
| cosmo | 0.365.2 | 1,471 | 1,473 | 1,469 | 0.1% | 166 MB | 115.4 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 541 | 542 | 540 | 0.2% | 2,762 MB | 5,227.4 KB |  |
| apollo-router | v2.19.0 | 528 | 529 | 527 | 0.2% | 174 MB | 338.0 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 433 | 433 | 432 | 0.1% | 201 MB | 474.9 KB |  |
| hive-gateway | 2.15.6 | 273 | 275 | 272 | 0.6% | 3,569 MB | 13,385.2 KB |  |
| apollo-gateway | 2.14.4 | 269 | 271 | 266 | 0.8% | 2,177 MB | 8,287.5 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1830747     ✗ 0     
     data_received..................: 53 GB   445 MB/s
     data_sent......................: 734 MB  6.1 MB/s
     http_req_blocked...............: avg=2.42µs   min=771ns    med=1.85µs  max=10.29ms  p(90)=3.01µs  p(95)=3.65µs   p(99.9)=27.32µs
     http_req_connecting............: avg=138ns    min=0s       med=0s      max=3.45ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.62ms   min=814.54µs med=8.81ms  max=298.65ms p(90)=14.8ms  p(95)=17.53ms  p(99.9)=29.42ms
       { expected_response:true }...: avg=9.62ms   min=814.54µs med=8.81ms  max=298.65ms p(90)=14.8ms  p(95)=17.53ms  p(99.9)=29.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 610349
     http_req_receiving.............: avg=102.25µs min=23.58µs  med=44.81µs max=273.98ms p(90)=88.69µs p(95)=190.25µs p(99.9)=6.47ms 
     http_req_sending...............: avg=41.49µs  min=4.1µs    med=7.86µs  max=110.96ms p(90)=14.2µs  p(95)=100.14µs p(99.9)=4.61ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.48ms   min=751.92µs med=8.71ms  max=117.72ms p(90)=14.59ms p(95)=17.27ms  p(99.9)=28.84ms
     http_reqs......................: 610349  5081.609853/s
     iteration_duration.............: avg=9.82ms   min=1.1ms    med=9ms     max=321.49ms p(90)=15ms    p(95)=17.74ms  p(99.9)=29.64ms
     iterations.....................: 610249  5080.777279/s
     success_rate...................: 100.00% ✓ 610249      ✗ 0     
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

     checks.........................: 100.00% ✓ 1825965     ✗ 0     
     data_received..................: 53 GB   444 MB/s
     data_sent......................: 732 MB  6.1 MB/s
     http_req_blocked...............: avg=2.99µs  min=951ns    med=2.41µs  max=6.92ms   p(90)=3.67µs  p(95)=4.35µs   p(99.9)=32.09µs
     http_req_connecting............: avg=151ns   min=0s       med=0s      max=4.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.64ms  min=830.33µs med=8.71ms  max=266.17ms p(90)=15.14ms p(95)=18.24ms  p(99.9)=31.05ms
       { expected_response:true }...: avg=9.64ms  min=830.33µs med=8.71ms  max=266.17ms p(90)=15.14ms p(95)=18.24ms  p(99.9)=31.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 608755
     http_req_receiving.............: avg=95.47µs min=22.98µs  med=46.23µs max=150.02ms p(90)=90.81µs p(95)=197.77µs p(99.9)=6.13ms 
     http_req_sending...............: avg=44.16µs min=4.4µs    med=8.74µs  max=112.34ms p(90)=15.42µs p(95)=105.43µs p(99.9)=5.13ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.5ms   min=759.78µs med=8.6ms   max=265.5ms  p(90)=14.9ms  p(95)=17.96ms  p(99.9)=30.61ms
     http_reqs......................: 608755  5068.295102/s
     iteration_duration.............: avg=9.84ms  min=1.13ms   med=8.9ms   max=278.83ms p(90)=15.35ms p(95)=18.46ms  p(99.9)=31.31ms
     iterations.....................: 608655  5067.462535/s
     success_rate...................: 100.00% ✓ 608655      ✗ 0     
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

     checks.........................: 100.00% ✓ 1749801     ✗ 0     
     data_received..................: 51 GB   425 MB/s
     data_sent......................: 701 MB  5.8 MB/s
     http_req_blocked...............: avg=3.1µs    min=821ns    med=2.36µs  max=11.39ms  p(90)=3.79µs   p(95)=4.64µs   p(99.9)=34.04µs
     http_req_connecting............: avg=168ns    min=0s       med=0s      max=4.08ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.06ms  min=991.96µs med=9.18ms  max=247.61ms p(90)=15.6ms   p(95)=18.55ms  p(99.9)=31.26ms
       { expected_response:true }...: avg=10.06ms  min=991.96µs med=9.18ms  max=247.61ms p(90)=15.6ms   p(95)=18.55ms  p(99.9)=31.26ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 583367
     http_req_receiving.............: avg=111.33µs min=26.14µs  med=49.23µs max=186.14ms p(90)=100.12µs p(95)=204.67µs p(99.9)=7.53ms 
     http_req_sending...............: avg=46.03µs  min=4.38µs   med=8.67µs  max=68.69ms  p(90)=16.84µs  p(95)=105.7µs  p(99.9)=5.4ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.9ms    min=911.65µs med=9.06ms  max=61.55ms  p(90)=15.36ms  p(95)=18.26ms  p(99.9)=30.74ms
     http_reqs......................: 583367  4856.364876/s
     iteration_duration.............: avg=10.27ms  min=1.26ms   med=9.39ms  max=351.54ms p(90)=15.81ms  p(95)=18.77ms  p(99.9)=31.65ms
     iterations.....................: 583267  4855.532405/s
     success_rate...................: 100.00% ✓ 583267      ✗ 0     
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

     checks.........................: 100.00% ✓ 1733775     ✗ 0     
     data_received..................: 51 GB   421 MB/s
     data_sent......................: 695 MB  5.8 MB/s
     http_req_blocked...............: avg=2.41µs  min=811ns    med=1.88µs  max=5.28ms   p(90)=2.94µs  p(95)=3.48µs   p(99.9)=26.4µs 
     http_req_connecting............: avg=169ns   min=0s       med=0s      max=4.14ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.18ms min=910.59µs med=9.54ms  max=265.49ms p(90)=14.98ms p(95)=17.37ms  p(99.9)=28.4ms 
       { expected_response:true }...: avg=10.18ms min=910.59µs med=9.54ms  max=265.49ms p(90)=14.98ms p(95)=17.37ms  p(99.9)=28.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 578025
     http_req_receiving.............: avg=87.17µs min=23.93µs  med=43.86µs max=20.28ms  p(90)=89.13µs p(95)=198.61µs p(99.9)=5.3ms  
     http_req_sending...............: avg=38.32µs min=4.26µs   med=7.89µs  max=200.53ms p(90)=14.01µs p(95)=100.93µs p(99.9)=3.6ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.06ms min=829.76µs med=9.44ms  max=255.93ms p(90)=14.79ms p(95)=17.14ms  p(99.9)=28.01ms
     http_reqs......................: 578025  4812.109489/s
     iteration_duration.............: avg=10.37ms min=1.06ms   med=9.72ms  max=284.24ms p(90)=15.17ms p(95)=17.57ms  p(99.9)=28.67ms
     iterations.....................: 577925  4811.27698/s
     success_rate...................: 100.00% ✓ 577925      ✗ 0     
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

     checks.........................: 100.00% ✓ 1718838     ✗ 0     
     data_received..................: 50 GB   417 MB/s
     data_sent......................: 689 MB  5.7 MB/s
     http_req_blocked...............: avg=2.87µs  min=792ns    med=1.9µs   max=62.05ms  p(90)=3.07µs  p(95)=3.75µs  p(99.9)=27.17µs
     http_req_connecting............: avg=509ns   min=0s       med=0s      max=62ms     p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=10.26ms min=979.8µs  med=9.54ms  max=265.62ms p(90)=15.42ms p(95)=18.03ms p(99.9)=30.76ms
       { expected_response:true }...: avg=10.26ms min=979.8µs  med=9.54ms  max=265.62ms p(90)=15.42ms p(95)=18.03ms p(99.9)=30.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 573046
     http_req_receiving.............: avg=97.27µs min=25.06µs  med=47.61µs max=49.11ms  p(90)=95.69µs p(95)=199.4µs p(99.9)=6.08ms 
     http_req_sending...............: avg=42.36µs min=4.1µs    med=8.03µs  max=58.89ms  p(90)=14.97µs p(95)=99.8µs  p(99.9)=4.53ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=10.12ms min=928.54µs med=9.42ms  max=253.01ms p(90)=15.22ms p(95)=17.78ms p(99.9)=30.27ms
     http_reqs......................: 573046  4770.149303/s
     iteration_duration.............: avg=10.46ms min=1.41ms   med=9.73ms  max=295.07ms p(90)=15.63ms p(95)=18.24ms p(99.9)=31.03ms
     iterations.....................: 572946  4769.316883/s
     success_rate...................: 100.00% ✓ 572946      ✗ 0     
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

     checks.........................: 100.00% ✓ 1688025     ✗ 0     
     data_received..................: 49 GB   410 MB/s
     data_sent......................: 676 MB  5.6 MB/s
     http_req_blocked...............: avg=3.24µs  min=941ns    med=2.26µs  max=18.94ms  p(90)=3.51µs  p(95)=4.13µs   p(99.9)=30.48µs
     http_req_connecting............: avg=548ns   min=0s       med=0s      max=18.83ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.45ms min=940.42µs med=9.74ms  max=271.4ms  p(90)=15.63ms p(95)=18.34ms  p(99.9)=29.95ms
       { expected_response:true }...: avg=10.45ms min=940.42µs med=9.74ms  max=271.4ms  p(90)=15.63ms p(95)=18.34ms  p(99.9)=29.95ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 562775
     http_req_receiving.............: avg=95.38µs min=24.79µs  med=47.21µs max=66.13ms  p(90)=95.71µs p(95)=216.32µs p(99.9)=5.7ms  
     http_req_sending...............: avg=41.47µs min=4.29µs   med=8.47µs  max=183.09ms p(90)=15.08µs p(95)=108.03µs p(99.9)=4.16ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.32ms min=873.06µs med=9.63ms  max=259.55ms p(90)=15.42ms p(95)=18.08ms  p(99.9)=29.56ms
     http_reqs......................: 562775  4685.093819/s
     iteration_duration.............: avg=10.65ms min=1.33ms   med=9.92ms  max=316.16ms p(90)=15.83ms p(95)=18.56ms  p(99.9)=30.32ms
     iterations.....................: 562675  4684.261321/s
     success_rate...................: 100.00% ✓ 562675      ✗ 0     
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

     checks.........................: 100.00% ✓ 1644867     ✗ 0     
     data_received..................: 48 GB   399 MB/s
     data_sent......................: 659 MB  5.5 MB/s
     http_req_blocked...............: avg=2.51µs  min=791ns    med=1.92µs  max=4.38ms   p(90)=3.14µs  p(95)=3.84µs  p(99.9)=28.89µs
     http_req_connecting............: avg=162ns   min=0s       med=0s      max=3.66ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=10.73ms min=1.02ms   med=10.12ms max=253.72ms p(90)=15.67ms p(95)=18.08ms p(99.9)=29.86ms
       { expected_response:true }...: avg=10.73ms min=1.02ms   med=10.12ms max=253.72ms p(90)=15.67ms p(95)=18.08ms p(99.9)=29.86ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 548389
     http_req_receiving.............: avg=94.23µs min=25.38µs  med=47.01µs max=69.97ms  p(90)=96.75µs p(95)=204.1µs p(99.9)=5.55ms 
     http_req_sending...............: avg=40.34µs min=4.33µs   med=8.08µs  max=112.91ms p(90)=15.9µs  p(95)=102.4µs p(99.9)=4.08ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=10.59ms min=968.71µs med=10ms    max=253.25ms p(90)=15.47ms p(95)=17.84ms p(99.9)=29.42ms
     http_reqs......................: 548389  4564.488662/s
     iteration_duration.............: avg=10.93ms min=1.32ms   med=10.31ms max=286.36ms p(90)=15.87ms p(95)=18.29ms p(99.9)=30.11ms
     iterations.....................: 548289  4563.656317/s
     success_rate...................: 100.00% ✓ 548289      ✗ 0     
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

     checks.........................: 100.00% ✓ 1627212     ✗ 0     
     data_received..................: 48 GB   395 MB/s
     data_sent......................: 652 MB  5.4 MB/s
     http_req_blocked...............: avg=2.58µs  min=761ns   med=1.99µs  max=6.45ms   p(90)=3.19µs  p(95)=3.84µs   p(99.9)=27.02µs
     http_req_connecting............: avg=160ns   min=0s      med=0s      max=3.29ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.85ms min=1.05ms  med=10.27ms max=285.16ms p(90)=15.7ms  p(95)=18.09ms  p(99.9)=30.53ms
       { expected_response:true }...: avg=10.85ms min=1.05ms  med=10.27ms max=285.16ms p(90)=15.7ms  p(95)=18.09ms  p(99.9)=30.53ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 542504
     http_req_receiving.............: avg=92.67µs min=24.25µs med=46.23µs max=71.49ms  p(90)=94.15µs p(95)=202.07µs p(99.9)=5.53ms 
     http_req_sending...............: avg=40.48µs min=4.54µs  med=8.31µs  max=105.71ms p(90)=15.33µs p(95)=102.35µs p(99.9)=4.05ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.71ms min=1ms     med=10.15ms max=284.58ms p(90)=15.51ms p(95)=17.86ms  p(99.9)=30.14ms
     http_reqs......................: 542504  4515.355374/s
     iteration_duration.............: avg=11.05ms min=1.64ms  med=10.46ms max=305.84ms p(90)=15.91ms p(95)=18.31ms  p(99.9)=30.8ms 
     iterations.....................: 542404  4514.523057/s
     success_rate...................: 100.00% ✓ 542404      ✗ 0     
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

     checks.........................: 100.00% ✓ 1555932     ✗ 0     
     data_received..................: 45 GB   378 MB/s
     data_sent......................: 623 MB  5.2 MB/s
     http_req_blocked...............: avg=2.59µs  min=802ns    med=2.02µs  max=4.82ms   p(90)=3.19µs  p(95)=3.8µs    p(99.9)=29.35µs
     http_req_connecting............: avg=177ns   min=0s       med=0s      max=3.98ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.36ms min=769.07µs med=11.04ms max=279.86ms p(90)=16.44ms p(95)=18.49ms  p(99.9)=29.13ms
       { expected_response:true }...: avg=11.36ms min=769.07µs med=11.04ms max=279.86ms p(90)=16.44ms p(95)=18.49ms  p(99.9)=29.13ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 518744
     http_req_receiving.............: avg=84.39µs min=25.27µs  med=47.66µs max=101.3ms  p(90)=90.91µs p(95)=204.86µs p(99.9)=4.19ms 
     http_req_sending...............: avg=38.81µs min=4.41µs   med=8.56µs  max=184.68ms p(90)=14.74µs p(95)=107.75µs p(99.9)=3.16ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.24ms min=708.26µs med=10.93ms max=279.29ms p(90)=16.28ms p(95)=18.29ms  p(99.9)=28.81ms
     http_reqs......................: 518744  4318.887816/s
     iteration_duration.............: avg=11.55ms min=1.26ms   med=11.22ms max=296.7ms  p(90)=16.63ms p(95)=18.69ms  p(99.9)=29.39ms
     iterations.....................: 518644  4318.05525/s
     success_rate...................: 100.00% ✓ 518644      ✗ 0     
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

     checks.........................: 100.00% ✓ 1067100     ✗ 0     
     data_received..................: 31 GB   259 MB/s
     data_sent......................: 428 MB  3.6 MB/s
     http_req_blocked...............: avg=3.34µs  min=962ns   med=2.76µs  max=3.89ms   p(90)=4.24µs  p(95)=4.97µs   p(99.9)=40.12µs
     http_req_connecting............: avg=251ns   min=0s      med=0s      max=3.85ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.65ms min=1.42ms  med=16.67ms max=271.57ms p(90)=22.45ms p(95)=24.05ms  p(99.9)=31.73ms
       { expected_response:true }...: avg=16.65ms min=1.42ms  med=16.67ms max=271.57ms p(90)=22.45ms p(95)=24.05ms  p(99.9)=31.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 355800
     http_req_receiving.............: avg=78.66µs min=25.41µs med=54.49µs max=105.81ms p(90)=97.92µs p(95)=191.97µs p(99.9)=1.42ms 
     http_req_sending...............: avg=35.86µs min=4.57µs  med=10.45µs max=113.4ms  p(90)=17.73µs p(95)=114.73µs p(99.9)=1.39ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.54ms min=1.33ms  med=16.56ms max=257.46ms p(90)=22.33ms p(95)=23.92ms  p(99.9)=31.54ms
     http_reqs......................: 355800  2960.370075/s
     iteration_duration.............: avg=16.85ms min=3.07ms  med=16.86ms max=291.35ms p(90)=22.64ms p(95)=24.24ms  p(99.9)=31.95ms
     iterations.....................: 355700  2959.538043/s
     success_rate...................: 100.00% ✓ 355700      ✗ 0     
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

     checks.........................: 100.00% ✓ 636801      ✗ 0     
     data_received..................: 19 GB   155 MB/s
     data_sent......................: 255 MB  2.1 MB/s
     http_req_blocked...............: avg=4.33µs  min=1.01µs  med=3.08µs  max=6.48ms   p(90)=5.19µs   p(95)=6.24µs   p(99.9)=44.18µs
     http_req_connecting............: avg=737ns   min=0s      med=0s      max=6.44ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=28ms    min=1.86ms  med=27.31ms max=283.74ms p(90)=36.27ms  p(95)=39.19ms  p(99.9)=53.57ms
       { expected_response:true }...: avg=28ms    min=1.86ms  med=27.31ms max=283.74ms p(90)=36.27ms  p(95)=39.19ms  p(99.9)=53.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 212367
     http_req_receiving.............: avg=89.68µs min=27.88µs med=65.88µs max=180.32ms p(90)=122.33µs p(95)=174.72µs p(99.9)=1.3ms  
     http_req_sending...............: avg=34.55µs min=5.17µs  med=12.24µs max=141.02ms p(90)=22.71µs  p(95)=86.69µs  p(99.9)=1.38ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=27.88ms min=1.76ms  med=27.19ms max=283.37ms p(90)=36.14ms  p(95)=39.06ms  p(99.9)=53.36ms
     http_reqs......................: 212367  1765.963968/s
     iteration_duration.............: avg=28.25ms min=6.99ms  med=27.54ms max=306.87ms p(90)=36.5ms   p(95)=39.42ms  p(99.9)=53.88ms
     iterations.....................: 212267  1765.132406/s
     success_rate...................: 100.00% ✓ 212267      ✗ 0     
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

     checks.........................: 100.00% ✓ 549504      ✗ 0     
     data_received..................: 16 GB   133 MB/s
     data_sent......................: 220 MB  1.8 MB/s
     http_req_blocked...............: avg=4.22µs  min=952ns   med=2.5µs   max=9.1ms    p(90)=4.28µs  p(95)=5.05µs   p(99.9)=36.77µs 
     http_req_connecting............: avg=1.34µs  min=0s      med=0s      max=8.78ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.51ms min=2.14ms  med=31.6ms  max=281.33ms p(90)=45.84ms p(95)=50.5ms   p(99.9)=75.57ms 
       { expected_response:true }...: avg=32.51ms min=2.14ms  med=31.6ms  max=281.33ms p(90)=45.84ms p(95)=50.5ms   p(99.9)=75.57ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 183268
     http_req_receiving.............: avg=74.12µs min=24.15µs med=59.87µs max=160.32ms p(90)=99.29µs p(95)=116.13µs p(99.9)=843.68µs
     http_req_sending...............: avg=23.21µs min=4.77µs  med=11.78µs max=216.14ms p(90)=19.52µs p(95)=23.29µs  p(99.9)=772.46µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.41ms min=2.04ms  med=31.5ms  max=281.03ms p(90)=45.76ms p(95)=50.41ms  p(99.9)=75.21ms 
     http_reqs......................: 183268  1523.719677/s
     iteration_duration.............: avg=32.74ms min=5.87ms  med=31.81ms max=303.36ms p(90)=46.06ms p(95)=50.71ms  p(99.9)=75.9ms  
     iterations.....................: 183168  1522.888261/s
     success_rate...................: 100.00% ✓ 183168      ✗ 0     
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

     checks.........................: 100.00% ✓ 530640      ✗ 0     
     data_received..................: 16 GB   129 MB/s
     data_sent......................: 213 MB  1.8 MB/s
     http_req_blocked...............: avg=3.01µs  min=922ns   med=2.22µs  max=3.63ms   p(90)=3.68µs  p(95)=4.35µs   p(99.9)=25µs    
     http_req_connecting............: avg=492ns   min=0s      med=0s      max=3.58ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.69ms min=2.07ms  med=32.82ms max=280.58ms p(90)=48.55ms p(95)=53.52ms  p(99.9)=75.98ms 
       { expected_response:true }...: avg=33.69ms min=2.07ms  med=32.82ms max=280.58ms p(90)=48.55ms p(95)=53.52ms  p(99.9)=75.98ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 176980
     http_req_receiving.............: avg=70.07µs min=24.85µs med=58.91µs max=145.17ms p(90)=95.7µs  p(95)=111.32µs p(99.9)=677.91µs
     http_req_sending...............: avg=19.98µs min=4.55µs  med=10.25µs max=107.58ms p(90)=16.47µs p(95)=20.02µs  p(99.9)=743.1µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.6ms  min=1.99ms  med=32.73ms max=280.04ms p(90)=48.46ms p(95)=53.42ms  p(99.9)=75.72ms 
     http_reqs......................: 176980  1471.453143/s
     iteration_duration.............: avg=33.91ms min=4.4ms   med=33.01ms max=311.01ms p(90)=48.75ms p(95)=53.71ms  p(99.9)=76.49ms 
     iterations.....................: 176880  1470.621719/s
     success_rate...................: 100.00% ✓ 176880      ✗ 0     
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

     checks.........................: 100.00% ✓ 195639     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   651 kB/s
     http_req_blocked...............: avg=6.35µs  min=1.03µs  med=2.38µs  max=9.04ms   p(90)=3.81µs   p(95)=4.39µs   p(99.9)=45.51µs 
     http_req_connecting............: avg=3.49µs  min=0s      med=0s      max=8.87ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=91.65ms min=3.83ms  med=89.04ms max=314.5ms  p(90)=110.27ms p(95)=120.43ms p(99.9)=221.06ms
       { expected_response:true }...: avg=91.65ms min=3.83ms  med=89.04ms max=314.5ms  p(90)=110.27ms p(95)=120.43ms p(99.9)=221.06ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 65313
     http_req_receiving.............: avg=72.72µs min=27.58µs med=65.45µs max=32.4ms   p(90)=98.49µs  p(95)=110.71µs p(99.9)=508.37µs
     http_req_sending...............: avg=18.58µs min=4.96µs  med=12.23µs max=65.42ms  p(90)=18.17µs  p(95)=19.95µs  p(99.9)=605.24µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.56ms min=3.76ms  med=88.96ms max=308.9ms  p(90)=110.18ms p(95)=120.33ms p(99.9)=220.89ms
     http_reqs......................: 65313   541.818415/s
     iteration_duration.............: avg=92.02ms min=33.16ms med=89.27ms max=329.85ms p(90)=110.5ms  p(95)=120.69ms p(99.9)=223.5ms 
     iterations.....................: 65213   540.988843/s
     success_rate...................: 100.00% ✓ 65213      ✗ 0    
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

     checks.........................: 100.00% ✓ 190902     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   635 kB/s
     http_req_blocked...............: avg=4.65µs  min=1.07µs  med=3.1µs   max=3.52ms   p(90)=4.57µs   p(95)=5.12µs   p(99.9)=46.05µs 
     http_req_connecting............: avg=1.36µs  min=0s      med=0s      max=3.48ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.91ms min=4.46ms  med=92.08ms max=329.74ms p(90)=126.61ms p(95)=136.38ms p(99.9)=176.6ms 
       { expected_response:true }...: avg=93.91ms min=4.46ms  med=92.08ms max=329.74ms p(90)=126.61ms p(95)=136.38ms p(99.9)=176.6ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 63734
     http_req_receiving.............: avg=75.47µs min=27.55µs med=71.84µs max=4.47ms   p(90)=102.54µs p(95)=114.91µs p(99.9)=436.61µs
     http_req_sending...............: avg=17.9µs  min=5.08µs  med=14.82µs max=18.55ms  p(90)=19.96µs  p(95)=21.84µs  p(99.9)=454.04µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.82ms min=4.35ms  med=91.99ms max=329.21ms p(90)=126.53ms p(95)=136.3ms  p(99.9)=176.51ms
     http_reqs......................: 63734   528.560595/s
     iteration_duration.............: avg=94.3ms  min=23.97ms med=92.36ms max=341.63ms p(90)=126.88ms p(95)=136.71ms p(99.9)=177.98ms
     iterations.....................: 63634   527.731272/s
     success_rate...................: 100.00% ✓ 63634      ✗ 0    
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

     checks.........................: 100.00% ✓ 156621     ✗ 0    
     data_received..................: 4.6 GB  38 MB/s
     data_sent......................: 63 MB   521 kB/s
     http_req_blocked...............: avg=5.44µs   min=1.39µs  med=3.54µs   max=3.57ms   p(90)=4.98µs   p(95)=5.56µs   p(99.9)=105.67µs
     http_req_connecting............: avg=1.66µs   min=0s      med=0s       max=3.53ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=114.46ms min=5.29ms  med=112.24ms max=334.14ms p(90)=149.28ms p(95)=160.96ms p(99.9)=211.71ms
       { expected_response:true }...: avg=114.46ms min=5.29ms  med=112.24ms max=334.14ms p(90)=149.28ms p(95)=160.96ms p(99.9)=211.71ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 52307
     http_req_receiving.............: avg=83.4µs   min=30.76µs med=78.71µs  max=79.99ms  p(90)=108.03µs p(95)=119.43µs p(99.9)=510.16µs
     http_req_sending...............: avg=23.74µs  min=5.41µs  med=16.08µs  max=68.53ms  p(90)=20.68µs  p(95)=22.53µs  p(99.9)=533.92µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=114.35ms min=5.19ms  med=112.14ms max=324.56ms p(90)=149.19ms p(95)=160.86ms p(99.9)=211.56ms
     http_reqs......................: 52307   433.491265/s
     iteration_duration.............: avg=114.94ms min=32.05ms med=112.55ms max=360.03ms p(90)=149.57ms p(95)=161.26ms p(99.9)=213.14ms
     iterations.....................: 52207   432.66252/s
     success_rate...................: 100.00% ✓ 52207      ✗ 0    
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

     checks.........................: 100.00% ✓ 98913      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   328 kB/s
     http_req_blocked...............: avg=6.26µs   min=1.08µs  med=3.19µs   max=3.52ms   p(90)=4.51µs   p(95)=5.05µs   p(99.9)=1.48ms  
     http_req_connecting............: avg=2.85µs   min=0s      med=0s       max=3.48ms   p(90)=0s       p(95)=0s       p(99.9)=1.43ms  
     http_req_duration..............: avg=181.32ms min=5.7ms   med=163.78ms max=762.16ms p(90)=209.67ms p(95)=238.4ms  p(99.9)=681.37ms
       { expected_response:true }...: avg=181.32ms min=5.7ms   med=163.78ms max=762.16ms p(90)=209.67ms p(95)=238.4ms  p(99.9)=681.37ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33071
     http_req_receiving.............: avg=90.36µs  min=30.5µs  med=85.45µs  max=41.92ms  p(90)=115.13µs p(95)=126.17µs p(99.9)=804.6µs 
     http_req_sending...............: avg=22.39µs  min=5.04µs  med=16.56µs  max=56.74ms  p(90)=20.65µs  p(95)=22.44µs  p(99.9)=482.94µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=181.21ms min=5.62ms  med=163.67ms max=762.04ms p(90)=209.56ms p(95)=238.28ms p(99.9)=681.24ms
     http_reqs......................: 33071   273.542681/s
     iteration_duration.............: avg=182.11ms min=48.13ms med=164.13ms max=762.82ms p(90)=210.04ms p(95)=239.1ms  p(99.9)=681.66ms
     iterations.....................: 32971   272.715543/s
     success_rate...................: 100.00% ✓ 32971      ✗ 0    
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

     checks.........................: 100.00% ✓ 97359      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   323 kB/s
     http_req_blocked...............: avg=5.62µs   min=1.05µs  med=2.82µs   max=3.52ms   p(90)=4.02µs   p(95)=4.52µs   p(99.9)=1.26ms  
     http_req_connecting............: avg=2.61µs   min=0s      med=0s       max=3.48ms   p(90)=0s       p(95)=0s       p(99.9)=1.24ms  
     http_req_duration..............: avg=184.16ms min=7.57ms  med=189.01ms max=387.31ms p(90)=197.52ms p(95)=201.79ms p(99.9)=274.05ms
       { expected_response:true }...: avg=184.16ms min=7.57ms  med=189.01ms max=387.31ms p(90)=197.52ms p(95)=201.79ms p(99.9)=274.05ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32553
     http_req_receiving.............: avg=87.57µs  min=29.92µs med=81.57µs  max=78.55ms  p(90)=110.68µs p(95)=121.06µs p(99.9)=537.24µs
     http_req_sending...............: avg=28.11µs  min=4.97µs  med=15.42µs  max=86.01ms  p(90)=19.32µs  p(95)=20.95µs  p(99.9)=505.21µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.04ms min=7.43ms  med=188.91ms max=371.21ms p(90)=197.42ms p(95)=201.69ms p(99.9)=273.6ms 
     http_reqs......................: 32553   269.120818/s
     iteration_duration.............: avg=184.97ms min=38.31ms med=189.27ms max=400.64ms p(90)=197.79ms p(95)=202.09ms p(99.9)=281.87ms
     iterations.....................: 32453   268.294102/s
     success_rate...................: 100.00% ✓ 32453      ✗ 0    
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

