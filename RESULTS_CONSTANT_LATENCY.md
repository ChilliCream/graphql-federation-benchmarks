## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 3,420 | 3,439 | 3,411 | 0.3% | 378 MB | 113.3 KB |  |
| fusion-aot-11 | 16.7.3 | 3,411 | 3,415 | 3,386 | 0.3% | 131 MB | 39.2 KB |  |
| fusion-net-11 | 16.7.3 | 3,398 | 3,411 | 3,390 | 0.3% | 372 MB | 112.2 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 3,348 | 3,376 | 3,345 | 0.4% | 140 MB | 42.7 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,280 | 3,292 | 3,239 | 0.6% | 2,297 MB | 717.0 KB |  |
| fusion-fed-net-11 | 16.7.3 | 2,798 | 2,804 | 2,790 | 0.2% | 410 MB | 149.9 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 2,787 | 2,803 | 2,767 | 0.5% | 395 MB | 145.1 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 2,756 | 2,767 | 2,736 | 0.5% | 156 MB | 58.1 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 2,755 | 2,760 | 2,754 | 0.1% | 141 MB | 52.5 KB |  |
| hive-router | v0.3.10 | 2,052 | 2,056 | 2,039 | 0.3% | 88 MB | 43.7 KB |  |
| grafbase | 0.53.5 | 1,451 | 1,454 | 1,443 | 0.3% | 99 MB | 70.1 KB |  |
| cosmo | 0.365.2 | 1,365 | 1,366 | 1,361 | 0.1% | 149 MB | 111.7 KB |  |
| caliban | 3.2.0 | 1,337 | 1,338 | 1,335 | 0.1% | 4,648 MB | 3,559.7 KB |  |
| apollo-router | v2.19.0 | 528 | 529 | 523 | 0.4% | 182 MB | 353.3 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 526 | 529 | 523 | 0.4% | 2,761 MB | 5,374.5 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 418 | 418 | 418 | 0.0% | 205 MB | 501.9 KB |  |
| apollo-gateway | 2.14.4 | 263 | 264 | 262 | 0.3% | 2,146 MB | 8,354.6 KB |  |
| hive-gateway | 2.15.6 | 256 | 257 | 255 | 0.3% | 3,583 MB | 14,332.6 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1241052     ✗ 0     
     data_received..................: 36 GB   299 MB/s
     data_sent......................: 497 MB  4.1 MB/s
     http_req_blocked...............: avg=2.87µs  min=872ns   med=2.28µs  max=3.76ms   p(90)=3.62µs  p(95)=4.37µs   p(99.9)=28.34µs
     http_req_connecting............: avg=229ns   min=0s      med=0s      max=3.72ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.29ms min=8.25ms  med=13.85ms max=285.81ms p(90)=17.81ms p(95)=19.21ms  p(99.9)=27.5ms 
       { expected_response:true }...: avg=14.29ms min=8.25ms  med=13.85ms max=285.81ms p(90)=17.81ms p(95)=19.21ms  p(99.9)=27.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 413784
     http_req_receiving.............: avg=73.8µs  min=24.56µs med=45.34µs max=193.75ms p(90)=94.77µs p(95)=184.44µs p(99.9)=2.11ms 
     http_req_sending...............: avg=33.77µs min=4.33µs  med=8.4µs   max=166.66ms p(90)=16.98µs p(95)=98.53µs  p(99.9)=2ms    
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.18ms min=8.17ms  med=13.74ms max=285.26ms p(90)=17.69ms p(95)=19.09ms  p(99.9)=27.19ms
     http_reqs......................: 413784  3420.957975/s
     iteration_duration.............: avg=14.49ms min=8.43ms  med=14.04ms max=298.42ms p(90)=18ms    p(95)=19.41ms  p(99.9)=27.76ms
     iterations.....................: 413684  3420.131225/s
     success_rate...................: 100.00% ✓ 413684      ✗ 0     
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

     checks.........................: 100.00% ✓ 1237500     ✗ 0     
     data_received..................: 36 GB   299 MB/s
     data_sent......................: 496 MB  4.1 MB/s
     http_req_blocked...............: avg=3.35µs  min=912ns   med=2.29µs  max=8.95ms   p(90)=3.65µs  p(95)=4.37µs   p(99.9)=29.93µs
     http_req_connecting............: avg=693ns   min=0s      med=0s      max=8.92ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.33ms min=8.24ms  med=13.87ms max=270.34ms p(90)=17.76ms p(95)=19.18ms  p(99.9)=27.84ms
       { expected_response:true }...: avg=14.33ms min=8.24ms  med=13.87ms max=270.34ms p(90)=17.76ms p(95)=19.18ms  p(99.9)=27.84ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 412600
     http_req_receiving.............: avg=71.83µs min=24.18µs med=43.94µs max=143.52ms p(90)=93.32µs p(95)=191.55µs p(99.9)=2.02ms 
     http_req_sending...............: avg=33.09µs min=4.63µs  med=8.65µs  max=85.83ms  p(90)=17.23µs p(95)=104.15µs p(99.9)=1.92ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.23ms min=8.18ms  med=13.77ms max=269.17ms p(90)=17.65ms p(95)=19.05ms  p(99.9)=27.61ms
     http_reqs......................: 412600  3411.128289/s
     iteration_duration.............: avg=14.53ms min=8.37ms  med=14.07ms max=295ms    p(90)=17.96ms p(95)=19.38ms  p(99.9)=28.07ms
     iterations.....................: 412500  3410.30155/s
     success_rate...................: 100.00% ✓ 412500      ✗ 0     
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

     checks.........................: 100.00% ✓ 1232937     ✗ 0     
     data_received..................: 36 GB   297 MB/s
     data_sent......................: 494 MB  4.1 MB/s
     http_req_blocked...............: avg=2.45µs  min=781ns   med=1.84µs  max=4.05ms   p(90)=3.19µs  p(95)=4.05µs   p(99.9)=25.81µs
     http_req_connecting............: avg=218ns   min=0s      med=0s      max=4ms      p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.39ms min=8.33ms  med=13.98ms max=276.26ms p(90)=17.86ms p(95)=19.22ms  p(99.9)=26.9ms 
       { expected_response:true }...: avg=14.39ms min=8.33ms  med=13.98ms max=276.26ms p(90)=17.86ms p(95)=19.22ms  p(99.9)=26.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 411079
     http_req_receiving.............: avg=68.59µs min=23.53µs med=42.12µs max=189.38ms p(90)=93.34µs p(95)=170.62µs p(99.9)=1.91ms 
     http_req_sending...............: avg=31.08µs min=4.24µs  med=7.7µs   max=190.78ms p(90)=17.49µs p(95)=92.37µs  p(99.9)=1.97ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.29ms min=8.27ms  med=13.88ms max=275.9ms  p(90)=17.75ms p(95)=19.1ms   p(99.9)=26.66ms
     http_reqs......................: 411079  3398.545381/s
     iteration_duration.............: avg=14.59ms min=8.48ms  med=14.17ms max=290.76ms p(90)=18.05ms p(95)=19.41ms  p(99.9)=27.15ms
     iterations.....................: 410979  3397.718643/s
     success_rate...................: 100.00% ✓ 410979      ✗ 0     
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

     checks.........................: 100.00% ✓ 1214961     ✗ 0     
     data_received..................: 35 GB   293 MB/s
     data_sent......................: 487 MB  4.0 MB/s
     http_req_blocked...............: avg=2.4µs   min=792ns   med=1.82µs  max=3.58ms   p(90)=2.94µs  p(95)=3.6µs    p(99.9)=23.58µs
     http_req_connecting............: avg=241ns   min=0s      med=0s      max=3.54ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.61ms min=8.33ms  med=14.19ms max=290.68ms p(90)=18.05ms p(95)=19.41ms  p(99.9)=27.49ms
       { expected_response:true }...: avg=14.61ms min=8.33ms  med=14.19ms max=290.68ms p(90)=18.05ms p(95)=19.41ms  p(99.9)=27.49ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 405087
     http_req_receiving.............: avg=67.15µs min=23.06µs med=42.51µs max=165.31ms p(90)=87.4µs  p(95)=164.66µs p(99.9)=1.73ms 
     http_req_sending...............: avg=31.28µs min=4.16µs  med=7.8µs   max=160.08ms p(90)=15.87µs p(95)=89.76µs  p(99.9)=1.65ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.51ms min=8.24ms  med=14.1ms  max=273.57ms p(90)=17.96ms p(95)=19.3ms   p(99.9)=27.28ms
     http_reqs......................: 405087  3348.859147/s
     iteration_duration.............: avg=14.8ms  min=8.48ms  med=14.38ms max=300.82ms p(90)=18.24ms p(95)=19.6ms   p(99.9)=27.71ms
     iterations.....................: 404987  3348.032446/s
     success_rate...................: 100.00% ✓ 404987      ✗ 0     
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

     checks.........................: 100.00% ✓ 1190274     ✗ 0     
     data_received..................: 35 GB   287 MB/s
     data_sent......................: 477 MB  3.9 MB/s
     http_req_blocked...............: avg=2.92µs  min=911ns   med=2.37µs  max=4.54ms   p(90)=3.86µs  p(95)=4.67µs   p(99.9)=31.77µs
     http_req_connecting............: avg=160ns   min=0s      med=0s      max=3.1ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.91ms min=8.27ms  med=14.54ms max=286.66ms p(90)=18.08ms p(95)=19.35ms  p(99.9)=27.13ms
       { expected_response:true }...: avg=14.91ms min=8.27ms  med=14.54ms max=286.66ms p(90)=18.08ms p(95)=19.35ms  p(99.9)=27.13ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 396858
     http_req_receiving.............: avg=71.49µs min=23.73µs med=46.63µs max=15.31ms  p(90)=95.42µs p(95)=178.72µs p(99.9)=1.68ms 
     http_req_sending...............: avg=34.28µs min=4.26µs  med=8.84µs  max=239.08ms p(90)=17.98µs p(95)=100.41µs p(99.9)=1.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.8ms  min=8.22ms  med=14.44ms max=277.28ms p(90)=17.97ms p(95)=19.23ms  p(99.9)=26.89ms
     http_reqs......................: 396858  3280.892529/s
     iteration_duration.............: avg=15.11ms min=8.45ms  med=14.74ms max=308.35ms p(90)=18.28ms p(95)=19.54ms  p(99.9)=27.5ms 
     iterations.....................: 396758  3280.065812/s
     success_rate...................: 100.00% ✓ 396758      ✗ 0     
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

     checks.........................: 100.00% ✓ 1019001     ✗ 0     
     data_received..................: 30 GB   245 MB/s
     data_sent......................: 408 MB  3.4 MB/s
     http_req_blocked...............: avg=2.53µs  min=812ns   med=1.86µs  max=9.01ms   p(90)=3.16µs  p(95)=3.95µs   p(99.9)=24.83µs
     http_req_connecting............: avg=279ns   min=0s      med=0s      max=3.67ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.45ms min=11.64ms med=17.03ms max=289.81ms p(90)=20.44ms p(95)=21.69ms  p(99.9)=28.33ms
       { expected_response:true }...: avg=17.45ms min=11.64ms med=17.03ms max=289.81ms p(90)=20.44ms p(95)=21.69ms  p(99.9)=28.33ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 339767
     http_req_receiving.............: avg=67.35µs min=25.2µs  med=45.38µs max=114.56ms p(90)=92.57µs p(95)=144.96µs p(99.9)=1.38ms 
     http_req_sending...............: avg=28.56µs min=4.29µs  med=7.92µs  max=170.69ms p(90)=16.49µs p(95)=81.85µs  p(99.9)=1.48ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.35ms min=11.58ms med=16.94ms max=289.16ms p(90)=20.34ms p(95)=21.57ms  p(99.9)=28.07ms
     http_reqs......................: 339767  2798.605273/s
     iteration_duration.............: avg=17.65ms min=11.77ms med=17.23ms max=301ms    p(90)=20.64ms p(95)=21.88ms  p(99.9)=28.54ms
     iterations.....................: 339667  2797.78159/s
     success_rate...................: 100.00% ✓ 339667      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 1014894     ✗ 0     
     data_received..................: 30 GB   244 MB/s
     data_sent......................: 407 MB  3.3 MB/s
     http_req_blocked...............: avg=2.42µs  min=781ns   med=1.79µs  max=3.5ms    p(90)=3.07µs  p(95)=3.84µs   p(99.9)=23.7µs 
     http_req_connecting............: avg=259ns   min=0s      med=0s      max=3.47ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.52ms min=11.73ms med=17.09ms max=281.96ms p(90)=20.6ms  p(95)=21.84ms  p(99.9)=28.67ms
       { expected_response:true }...: avg=17.52ms min=11.73ms med=17.09ms max=281.96ms p(90)=20.6ms  p(95)=21.84ms  p(99.9)=28.67ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 338398
     http_req_receiving.............: avg=66.62µs min=23.88µs med=44.68µs max=149.17ms p(90)=90.35µs p(95)=141.65µs p(99.9)=1.42ms 
     http_req_sending...............: avg=26.92µs min=4.04µs  med=7.67µs  max=130.32ms p(90)=15.4µs  p(95)=79.19µs  p(99.9)=1.39ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.43ms min=11.65ms med=17ms    max=281.45ms p(90)=20.5ms  p(95)=21.73ms  p(99.9)=28.45ms
     http_reqs......................: 338398  2787.344182/s
     iteration_duration.............: avg=17.72ms min=11.91ms med=17.29ms max=291.86ms p(90)=20.79ms p(95)=22.04ms  p(99.9)=28.92ms
     iterations.....................: 338298  2786.520494/s
     success_rate...................: 100.00% ✓ 338298      ✗ 0     
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

     checks.........................: 100.00% ✓ 1003737     ✗ 0     
     data_received..................: 29 GB   241 MB/s
     data_sent......................: 402 MB  3.3 MB/s
     http_req_blocked...............: avg=2.53µs  min=811ns   med=1.88µs  max=3.55ms   p(90)=3.22µs  p(95)=4.02µs  p(99.9)=24.69µs
     http_req_connecting............: avg=287ns   min=0s      med=0s      max=3.5ms    p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=17.72ms min=11.57ms med=17.32ms max=282.38ms p(90)=20.6ms  p(95)=21.82ms p(99.9)=28.59ms
       { expected_response:true }...: avg=17.72ms min=11.57ms med=17.32ms max=282.38ms p(90)=20.6ms  p(95)=21.82ms p(99.9)=28.59ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 334679
     http_req_receiving.............: avg=64.81µs min=24.35µs med=44.19µs max=27.75ms  p(90)=90.17µs p(95)=137.8µs p(99.9)=1.26ms 
     http_req_sending...............: avg=28.29µs min=4.25µs  med=8.03µs  max=213.2ms  p(90)=16.38µs p(95)=79.47µs p(99.9)=1.38ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.62ms min=11.53ms med=17.24ms max=282.03ms p(90)=20.51ms p(95)=21.7ms  p(99.9)=28.41ms
     http_reqs......................: 334679  2756.320758/s
     iteration_duration.............: avg=17.92ms min=11.74ms med=17.52ms max=292.99ms p(90)=20.8ms  p(95)=22.01ms p(99.9)=28.8ms 
     iterations.....................: 334579  2755.497187/s
     success_rate...................: 100.00% ✓ 334579      ✗ 0     
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

     checks.........................: 100.00% ✓ 1003395     ✗ 0     
     data_received..................: 29 GB   241 MB/s
     data_sent......................: 402 MB  3.3 MB/s
     http_req_blocked...............: avg=3.35µs  min=881ns   med=2.24µs  max=8.59ms   p(90)=3.6µs   p(95)=4.34µs   p(99.9)=31.33µs
     http_req_connecting............: avg=741ns   min=0s      med=0s      max=8.55ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.72ms min=11.81ms med=17.29ms max=286.13ms p(90)=20.75ms p(95)=22.02ms  p(99.9)=29.56ms
       { expected_response:true }...: avg=17.72ms min=11.81ms med=17.29ms max=286.13ms p(90)=20.75ms p(95)=22.02ms  p(99.9)=29.56ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 334565
     http_req_receiving.............: avg=68.54µs min=24.77µs med=45.97µs max=19.97ms  p(90)=93.11µs p(95)=154.26µs p(99.9)=1.36ms 
     http_req_sending...............: avg=29.07µs min=4.29µs  med=8.47µs  max=248.54ms p(90)=16.88µs p(95)=87.53µs  p(99.9)=1.45ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.62ms min=11.75ms med=17.2ms  max=282.59ms p(90)=20.64ms p(95)=21.91ms  p(99.9)=29.37ms
     http_reqs......................: 334565  2755.858043/s
     iteration_duration.............: avg=17.93ms min=12ms    med=17.49ms max=308.07ms p(90)=20.95ms p(95)=22.22ms  p(99.9)=29.9ms 
     iterations.....................: 334465  2755.034329/s
     success_rate...................: 100.00% ✓ 334465      ✗ 0     
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

     checks.........................: 100.00% ✓ 750144      ✗ 0     
     data_received..................: 22 GB   180 MB/s
     data_sent......................: 301 MB  2.5 MB/s
     http_req_blocked...............: avg=3.19µs  min=952ns   med=2.66µs  max=2.4ms    p(90)=4.26µs  p(95)=5.01µs   p(99.9)=35.59µs 
     http_req_connecting............: avg=195ns   min=0s      med=0s      max=2.37ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.76ms min=17.09ms med=23.41ms max=296.63ms p(90)=26.82ms p(95)=27.95ms  p(99.9)=33.57ms 
       { expected_response:true }...: avg=23.76ms min=17.09ms med=23.41ms max=296.63ms p(90)=26.82ms p(95)=27.95ms  p(99.9)=33.57ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 250148
     http_req_receiving.............: avg=69.26µs min=25.19µs med=51.5µs  max=254.34ms p(90)=91.81µs p(95)=115.86µs p(99.9)=929.9µs 
     http_req_sending...............: avg=27.46µs min=4.71µs  med=10.31µs max=144.98ms p(90)=17.48µs p(95)=24.69µs  p(99.9)=984.48µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.67ms min=17.02ms med=23.32ms max=288.74ms p(90)=26.73ms p(95)=27.85ms  p(99.9)=33.4ms  
     http_reqs......................: 250148  2052.697535/s
     iteration_duration.............: avg=23.98ms min=17.29ms med=23.62ms max=314.29ms p(90)=27.03ms p(95)=28.16ms  p(99.9)=33.84ms 
     iterations.....................: 250048  2051.876941/s
     success_rate...................: 100.00% ✓ 250048      ✗ 0     
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

     checks.........................: 100.00% ✓ 530619      ✗ 0     
     data_received..................: 16 GB   127 MB/s
     data_sent......................: 213 MB  1.7 MB/s
     http_req_blocked...............: avg=3.03µs  min=851ns   med=2.23µs  max=3.02ms   p(90)=4.57µs   p(95)=5.54µs   p(99.9)=36.28µs
     http_req_connecting............: avg=248ns   min=0s      med=0s      max=2.63ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.66ms min=17.57ms med=33.31ms max=315.2ms  p(90)=39.19ms  p(95)=40.91ms  p(99.9)=49.22ms
       { expected_response:true }...: avg=33.66ms min=17.57ms med=33.31ms max=315.2ms  p(90)=39.19ms  p(95)=40.91ms  p(99.9)=49.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 176973
     http_req_receiving.............: avg=80.36µs min=26.4µs  med=55.71µs max=171.38ms p(90)=116.67µs p(95)=155.34µs p(99.9)=1.32ms 
     http_req_sending...............: avg=27.75µs min=4.57µs  med=9.51µs  max=170.87ms p(90)=21.56µs  p(95)=31.2µs   p(99.9)=1.19ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.55ms min=17.51ms med=33.21ms max=314.73ms p(90)=39.08ms  p(95)=40.8ms   p(99.9)=49.01ms
     http_reqs......................: 176973  1451.390217/s
     iteration_duration.............: avg=33.91ms min=21.1ms  med=33.54ms max=324.89ms p(90)=39.41ms  p(95)=41.14ms  p(99.9)=49.43ms
     iterations.....................: 176873  1450.570098/s
     success_rate...................: 100.00% ✓ 176873      ✗ 0     
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

     checks.........................: 100.00% ✓ 499449      ✗ 0     
     data_received..................: 15 GB   120 MB/s
     data_sent......................: 200 MB  1.6 MB/s
     http_req_blocked...............: avg=3.47µs  min=911ns   med=2.1µs   max=7.48ms   p(90)=3.51µs  p(95)=4.2µs    p(99.9)=31.09µs 
     http_req_connecting............: avg=1.01µs  min=0s      med=0s      max=7.41ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.82ms min=18.23ms med=35.27ms max=298.61ms p(90)=42.87ms p(95)=45.34ms  p(99.9)=57.66ms 
       { expected_response:true }...: avg=35.82ms min=18.23ms med=35.27ms max=298.61ms p(90)=42.87ms p(95)=45.34ms  p(99.9)=57.66ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 166583
     http_req_receiving.............: avg=70.38µs min=24.47µs med=57.58µs max=97.88ms  p(90)=95.29µs p(95)=113.02µs p(99.9)=668.24µs
     http_req_sending...............: avg=21.62µs min=4.65µs  med=9.69µs  max=196.11ms p(90)=15.46µs p(95)=19.12µs  p(99.9)=751.97µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=35.73ms min=18.12ms med=35.19ms max=298.35ms p(90)=42.79ms p(95)=45.25ms  p(99.9)=57.36ms 
     http_reqs......................: 166583  1365.906846/s
     iteration_duration.............: avg=36.03ms min=21.04ms med=35.46ms max=311.43ms p(90)=43.06ms p(95)=45.54ms  p(99.9)=57.97ms 
     iterations.....................: 166483  1365.08689/s
     success_rate...................: 100.00% ✓ 166483      ✗ 0     
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

     checks.........................: 100.00% ✓ 489051      ✗ 0     
     data_received..................: 14 GB   117 MB/s
     data_sent......................: 196 MB  1.6 MB/s
     http_req_blocked...............: avg=2.95µs  min=942ns   med=2.1µs   max=3.92ms   p(90)=3.33µs  p(95)=3.93µs  p(99.9)=33.29µs 
     http_req_connecting............: avg=576ns   min=0s      med=0s      max=3.88ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=36.59ms min=18.07ms med=36.03ms max=306.16ms p(90)=43.57ms p(95)=46.02ms p(99.9)=59.22ms 
       { expected_response:true }...: avg=36.59ms min=18.07ms med=36.03ms max=306.16ms p(90)=43.57ms p(95)=46.02ms p(99.9)=59.22ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 163117
     http_req_receiving.............: avg=68.96µs min=27.07µs med=56.06µs max=169.31ms p(90)=88.14µs p(95)=102.1µs p(99.9)=739.56µs
     http_req_sending...............: avg=20.23µs min=4.69µs  med=10.12µs max=188.95ms p(90)=15.12µs p(95)=18.14µs p(99.9)=675.96µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=36.5ms  min=17.96ms med=35.95ms max=287.67ms p(90)=43.49ms p(95)=45.93ms p(99.9)=59.06ms 
     http_reqs......................: 163117  1337.199051/s
     iteration_duration.............: avg=36.8ms  min=21.51ms med=36.22ms max=312.55ms p(90)=43.76ms p(95)=46.21ms p(99.9)=59.61ms 
     iterations.....................: 163017  1336.379272/s
     success_rate...................: 100.00% ✓ 163017      ✗ 0     
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

     checks.........................: 100.00% ✓ 193434     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 78 MB   635 kB/s
     http_req_blocked...............: avg=4.45µs  min=1.06µs  med=2.77µs  max=3.82ms   p(90)=4.27µs   p(95)=4.86µs   p(99.9)=48.49µs 
     http_req_connecting............: avg=1.46µs  min=0s      med=0s      max=3.75ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.71ms min=19.89ms med=90.97ms max=309.95ms p(90)=116.94ms p(95)=124.9ms  p(99.9)=161.61ms
       { expected_response:true }...: avg=92.71ms min=19.89ms med=90.97ms max=309.95ms p(90)=116.94ms p(95)=124.9ms  p(99.9)=161.61ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64578
     http_req_receiving.............: avg=75.96µs min=26.53µs med=70.55µs max=42.94ms  p(90)=103.25µs p(95)=115.05µs p(99.9)=498.85µs
     http_req_sending...............: avg=26.4µs  min=4.88µs  med=13.84µs max=154.17ms p(90)=19.51µs  p(95)=21.64µs  p(99.9)=513.44µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.61ms min=19.8ms  med=90.88ms max=309.42ms p(90)=116.84ms p(95)=124.79ms p(99.9)=160.82ms
     http_reqs......................: 64578   528.419645/s
     iteration_duration.............: avg=93.07ms min=34.2ms  med=91.24ms max=317.95ms p(90)=117.19ms p(95)=125.17ms p(99.9)=162.64ms
     iterations.....................: 64478   527.60138/s
     success_rate...................: 100.00% ✓ 64478      ✗ 0    
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

     checks.........................: 100.00% ✓ 192903     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   633 kB/s
     http_req_blocked...............: avg=4.98µs  min=1.08µs  med=3.02µs  max=4.8ms    p(90)=4.56µs   p(95)=5.19µs   p(99.9)=42.59µs 
     http_req_connecting............: avg=1.73µs  min=0s      med=0s      max=4.76ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.97ms min=21.08ms med=89.39ms max=342.14ms p(90)=119.8ms  p(95)=129.06ms p(99.9)=230.09ms
       { expected_response:true }...: avg=92.97ms min=21.08ms med=89.39ms max=342.14ms p(90)=119.8ms  p(95)=129.06ms p(99.9)=230.09ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64401
     http_req_receiving.............: avg=83.3µs  min=29.25µs med=74.31µs max=89.76ms  p(90)=109.4µs  p(95)=122.47µs p(99.9)=615.02µs
     http_req_sending...............: avg=19.81µs min=4.97µs  med=14.22µs max=65.78ms  p(90)=20.13µs  p(95)=22.28µs  p(99.9)=573.22µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.87ms min=20.97ms med=89.3ms  max=341.4ms  p(90)=119.7ms  p(95)=128.96ms p(99.9)=230ms   
     http_reqs......................: 64401   526.726542/s
     iteration_duration.............: avg=93.33ms min=35ms    med=89.65ms max=357.84ms p(90)=120.05ms p(95)=129.31ms p(99.9)=230.95ms
     iterations.....................: 64301   525.908656/s
     success_rate...................: 100.00% ✓ 64301      ✗ 0    
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

     checks.........................: 100.00% ✓ 153243     ✗ 0    
     data_received..................: 4.5 GB  37 MB/s
     data_sent......................: 62 MB   503 kB/s
     http_req_blocked...............: avg=6.78µs   min=1.11µs  med=2.97µs   max=8.12ms   p(90)=4.37µs   p(95)=4.93µs   p(99.9)=107.16µs
     http_req_connecting............: avg=3.55µs   min=0s      med=0s       max=7.99ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=117.03ms min=20.97ms med=115.48ms max=295.28ms p(90)=144.77ms p(95)=154.33ms p(99.9)=199ms   
       { expected_response:true }...: avg=117.03ms min=20.97ms med=115.48ms max=295.28ms p(90)=144.77ms p(95)=154.33ms p(99.9)=199ms   
     http_req_failed................: 0.00%   ✓ 0          ✗ 51181
     http_req_receiving.............: avg=82.68µs  min=27.43µs med=74.55µs  max=110.08ms p(90)=105.54µs p(95)=117.32µs p(99.9)=458.08µs
     http_req_sending...............: avg=20.57µs  min=4.84µs  med=14.9µs   max=34.92ms  p(90)=20.36µs  p(95)=22.29µs  p(99.9)=662.38µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=116.93ms min=20.84ms med=115.39ms max=293.27ms p(90)=144.68ms p(95)=154.23ms p(99.9)=197.84ms
     http_reqs......................: 51181   418.479406/s
     iteration_duration.............: avg=117.47ms min=42.5ms  med=115.75ms max=336.42ms p(90)=145.02ms p(95)=154.6ms  p(99.9)=199.72ms
     iterations.....................: 51081   417.66176/s
     success_rate...................: 100.00% ✓ 51081      ✗ 0    
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

     checks.........................: 100.00% ✓ 96699      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   317 kB/s
     http_req_blocked...............: avg=12.25µs  min=1.36µs  med=3.47µs   max=8.91ms   p(90)=4.89µs   p(95)=5.5µs    p(99.9)=4.99ms  
     http_req_connecting............: avg=7.97µs   min=0s      med=0s       max=8.17ms   p(90)=0s       p(95)=0s       p(99.9)=4.6ms   
     http_req_duration..............: avg=185.43ms min=23.04ms med=185.53ms max=387.24ms p(90)=195.89ms p(95)=200.18ms p(99.9)=264.03ms
       { expected_response:true }...: avg=185.43ms min=23.04ms med=185.53ms max=387.24ms p(90)=195.89ms p(95)=200.18ms p(99.9)=264.03ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32333
     http_req_receiving.............: avg=90.72µs  min=37.72µs med=85.82µs  max=35.26ms  p(90)=115.44µs p(95)=126.16µs p(99.9)=401.81µs
     http_req_sending...............: avg=24.45µs  min=6.39µs  med=17.13µs  max=26.8ms   p(90)=21.92µs  p(95)=23.76µs  p(99.9)=1.09ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=185.32ms min=22.91ms med=185.43ms max=386.06ms p(90)=195.78ms p(95)=200.05ms p(99.9)=263.9ms 
     http_reqs......................: 32333   263.763473/s
     iteration_duration.............: avg=186.23ms min=60.45ms med=185.84ms max=403.02ms p(90)=196.18ms p(95)=200.48ms p(99.9)=265.55ms
     iterations.....................: 32233   262.947702/s
     success_rate...................: 100.00% ✓ 32233      ✗ 0    
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

     checks.........................: 100.00% ✓ 93534      ✗ 0    
     data_received..................: 2.7 GB  22 MB/s
     data_sent......................: 38 MB   308 kB/s
     http_req_blocked...............: avg=7.06µs   min=1.41µs  med=3.6µs    max=4.22ms   p(90)=5.02µs   p(95)=5.61µs   p(99.9)=1.47ms  
     http_req_connecting............: avg=3.22µs   min=0s      med=0s       max=4.17ms   p(90)=0s       p(95)=0s       p(99.9)=1.45ms  
     http_req_duration..............: avg=191.73ms min=17.69ms med=177.2ms  max=755.91ms p(90)=228.68ms p(95)=256.57ms p(99.9)=712.34ms
       { expected_response:true }...: avg=191.73ms min=17.69ms med=177.2ms  max=755.91ms p(90)=228.68ms p(95)=256.57ms p(99.9)=712.34ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31278
     http_req_receiving.............: avg=93.49µs  min=36.55µs med=87.46µs  max=28.92ms  p(90)=118.3µs  p(95)=131.05µs p(99.9)=673.76µs
     http_req_sending...............: avg=24.99µs  min=6.54µs  med=17.27µs  max=50.8ms   p(90)=21.92µs  p(95)=23.71µs  p(99.9)=491.51µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=191.61ms min=17.57ms med=177.09ms max=755.83ms p(90)=228.53ms p(95)=256.43ms p(99.9)=712.23ms
     http_reqs......................: 31278   256.080928/s
     iteration_duration.............: avg=192.55ms min=83.63ms med=177.63ms max=756.11ms p(90)=229.05ms p(95)=257.14ms p(99.9)=712.6ms 
     iterations.....................: 31178   255.262202/s
     success_rate...................: 100.00% ✓ 31178      ✗ 0    
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

