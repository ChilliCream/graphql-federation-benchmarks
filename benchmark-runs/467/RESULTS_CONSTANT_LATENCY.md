## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 3,418 | 3,430 | 3,408 | 0.2% | 383 MB | 114.8 KB |  |
| fusion-net-11 | 16.7.3 | 3,415 | 3,439 | 3,392 | 0.6% | 378 MB | 113.4 KB |  |
| fusion-aot-11 | 16.7.3 | 3,357 | 3,379 | 3,329 | 0.5% | 129 MB | 39.3 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 3,351 | 3,376 | 3,337 | 0.5% | 131 MB | 40.2 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,302 | 3,321 | 3,261 | 0.7% | 2,314 MB | 717.7 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 2,794 | 2,800 | 2,770 | 0.5% | 373 MB | 136.7 KB |  |
| fusion-fed-net-11 | 16.7.3 | 2,769 | 2,789 | 2,755 | 0.4% | 396 MB | 146.6 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 2,761 | 2,771 | 2,754 | 0.2% | 158 MB | 58.6 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 2,749 | 2,756 | 2,730 | 0.4% | 138 MB | 51.3 KB |  |
| hive-router | v0.3.10 | 2,048 | 2,056 | 2,041 | 0.3% | 88 MB | 44.2 KB |  |
| caliban | 3.2.0 | 1,490 | 1,491 | 1,487 | 0.1% | 5,263 MB | 3,617.0 KB |  |
| grafbase | 0.53.5 | 1,433 | 1,445 | 1,430 | 0.4% | 100 MB | 71.3 KB |  |
| cosmo | 0.365.2 | 1,418 | 1,422 | 1,415 | 0.2% | 146 MB | 105.6 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 537 | 537 | 536 | 0.1% | 2,741 MB | 5,226.0 KB |  |
| apollo-router | v2.19.0 | 531 | 531 | 530 | 0.1% | 180 MB | 347.1 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 418 | 418 | 418 | 0.0% | 205 MB | 502.7 KB |  |
| apollo-gateway | 2.14.4 | 265 | 266 | 265 | 0.2% | 2,151 MB | 8,310.4 KB |  |
| hive-gateway | 2.15.6 | 262 | 263 | 260 | 0.5% | 3,483 MB | 13,612.5 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1240125     ✗ 0     
     data_received..................: 36 GB   299 MB/s
     data_sent......................: 497 MB  4.1 MB/s
     http_req_blocked...............: avg=2.42µs  min=802ns   med=1.84µs  max=4.13ms   p(90)=3.13µs  p(95)=3.97µs  p(99.9)=24.43µs
     http_req_connecting............: avg=207ns   min=0s      med=0s      max=3.45ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=14.3ms  min=8.17ms  med=13.89ms max=288.3ms  p(90)=17.75ms p(95)=19.09ms p(99.9)=26.82ms
       { expected_response:true }...: avg=14.3ms  min=8.17ms  med=13.89ms max=288.3ms  p(90)=17.75ms p(95)=19.09ms p(99.9)=26.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 413475
     http_req_receiving.............: avg=70µs    min=25.05µs med=44.11µs max=94ms     p(90)=93.93µs p(95)=172.2µs p(99.9)=1.96ms 
     http_req_sending...............: avg=32.13µs min=4.48µs  med=7.89µs  max=161.44ms p(90)=16.75µs p(95)=91.88µs p(99.9)=1.96ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=14.2ms  min=8.12ms  med=13.79ms max=287.79ms p(90)=17.64ms p(95)=18.97ms p(99.9)=26.63ms
     http_reqs......................: 413475  3418.476405/s
     iteration_duration.............: avg=14.5ms  min=8.32ms  med=14.09ms max=298.03ms p(90)=17.94ms p(95)=19.28ms p(99.9)=27.02ms
     iterations.....................: 413375  3417.649637/s
     success_rate...................: 100.00% ✓ 413375      ✗ 0     
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

     checks.........................: 100.00% ✓ 1239087     ✗ 0     
     data_received..................: 36 GB   299 MB/s
     data_sent......................: 497 MB  4.1 MB/s
     http_req_blocked...............: avg=2.41µs  min=772ns   med=1.84µs  max=3.79ms   p(90)=3µs     p(95)=3.73µs   p(99.9)=23.15µs
     http_req_connecting............: avg=215ns   min=0s      med=0s      max=3.74ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.32ms min=8.17ms  med=13.9ms  max=278.05ms p(90)=17.8ms  p(95)=19.16ms  p(99.9)=27.17ms
       { expected_response:true }...: avg=14.32ms min=8.17ms  med=13.9ms  max=278.05ms p(90)=17.8ms  p(95)=19.16ms  p(99.9)=27.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 413129
     http_req_receiving.............: avg=68.95µs min=24.32µs med=44.05µs max=151.82ms p(90)=89.04µs p(95)=164.52µs p(99.9)=1.88ms 
     http_req_sending...............: avg=30.81µs min=4.41µs  med=7.81µs  max=172.15ms p(90)=15.26µs p(95)=89.01µs  p(99.9)=1.95ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.22ms min=8.12ms  med=13.8ms  max=277.56ms p(90)=17.69ms p(95)=19.05ms  p(99.9)=26.97ms
     http_reqs......................: 413129  3415.542385/s
     iteration_duration.............: avg=14.51ms min=8.32ms  med=14.09ms max=286.8ms  p(90)=17.99ms p(95)=19.35ms  p(99.9)=27.39ms
     iterations.....................: 413029  3414.715635/s
     success_rate...................: 100.00% ✓ 413029      ✗ 0     
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

     checks.........................: 100.00% ✓ 1218057     ✗ 0     
     data_received..................: 36 GB   294 MB/s
     data_sent......................: 488 MB  4.0 MB/s
     http_req_blocked...............: avg=2.57µs  min=791ns   med=2.01µs  max=3.45ms   p(90)=3.35µs  p(95)=4.09µs  p(99.9)=27.04µs
     http_req_connecting............: avg=191ns   min=0s      med=0s      max=3.4ms    p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=14.57ms min=8.14ms  med=14.13ms max=269.07ms p(90)=18.03ms p(95)=19.42ms p(99.9)=27.8ms 
       { expected_response:true }...: avg=14.57ms min=8.14ms  med=14.13ms max=269.07ms p(90)=18.03ms p(95)=19.42ms p(99.9)=27.8ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 406119
     http_req_receiving.............: avg=68.47µs min=23.54µs med=42.6µs  max=88.53ms  p(90)=91.73µs p(95)=176.2µs p(99.9)=1.77ms 
     http_req_sending...............: avg=31.7µs  min=4.2µs   med=7.92µs  max=178.87ms p(90)=16.26µs p(95)=95.3µs  p(99.9)=1.84ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=14.47ms min=8.08ms  med=14.04ms max=268.86ms p(90)=17.93ms p(95)=19.31ms p(99.9)=27.56ms
     http_reqs......................: 406119  3357.377238/s
     iteration_duration.............: avg=14.76ms min=8.31ms  med=14.33ms max=299.91ms p(90)=18.23ms p(95)=19.61ms p(99.9)=28.01ms
     iterations.....................: 406019  3356.55054/s
     success_rate...................: 100.00% ✓ 406019      ✗ 0     
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

     checks.........................: 100.00% ✓ 1216104     ✗ 0     
     data_received..................: 36 GB   293 MB/s
     data_sent......................: 487 MB  4.0 MB/s
     http_req_blocked...............: avg=2.35µs  min=792ns   med=1.79µs  max=3.95ms   p(90)=2.93µs  p(95)=3.59µs   p(99.9)=23.66µs
     http_req_connecting............: avg=208ns   min=0s      med=0s      max=3.41ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.6ms  min=8.32ms  med=14.17ms max=276.33ms p(90)=18.02ms p(95)=19.39ms  p(99.9)=27.25ms
       { expected_response:true }...: avg=14.6ms  min=8.32ms  med=14.17ms max=276.33ms p(90)=18.02ms p(95)=19.39ms  p(99.9)=27.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 405468
     http_req_receiving.............: avg=67.18µs min=23.77µs med=42.55µs max=191.49ms p(90)=88.53µs p(95)=167.59µs p(99.9)=1.65ms 
     http_req_sending...............: avg=30.06µs min=4.15µs  med=7.67µs  max=177.32ms p(90)=15.73µs p(95)=91.43µs  p(99.9)=1.56ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.5ms  min=8.27ms  med=14.08ms max=275.89ms p(90)=17.92ms p(95)=19.29ms  p(99.9)=27.01ms
     http_reqs......................: 405468  3351.916538/s
     iteration_duration.............: avg=14.79ms min=8.43ms  med=14.36ms max=284.43ms p(90)=18.21ms p(95)=19.58ms  p(99.9)=27.47ms
     iterations.....................: 405368  3351.08986/s
     success_rate...................: 100.00% ✓ 405368      ✗ 0     
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

     checks.........................: 100.00% ✓ 1197876     ✗ 0     
     data_received..................: 35 GB   289 MB/s
     data_sent......................: 480 MB  4.0 MB/s
     http_req_blocked...............: avg=2.53µs  min=812ns   med=1.94µs  max=5.6ms    p(90)=3.13µs  p(95)=3.78µs   p(99.9)=24.96µs
     http_req_connecting............: avg=256ns   min=0s      med=0s      max=5.29ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.82ms min=8.16ms  med=14.48ms max=286.09ms p(90)=17.87ms p(95)=19.06ms  p(99.9)=26.29ms
       { expected_response:true }...: avg=14.82ms min=8.16ms  med=14.48ms max=286.09ms p(90)=17.87ms p(95)=19.06ms  p(99.9)=26.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 399392
     http_req_receiving.............: avg=66.53µs min=24.04µs med=44.02µs max=56.28ms  p(90)=87.93µs p(95)=163.35µs p(99.9)=1.48ms 
     http_req_sending...............: avg=29.41µs min=4.48µs  med=8.18µs  max=76.04ms  p(90)=15.51µs p(95)=91.21µs  p(99.9)=1.53ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.72ms min=8.04ms  med=14.39ms max=285.29ms p(90)=17.77ms p(95)=18.95ms  p(99.9)=26.15ms
     http_reqs......................: 399392  3302.002779/s
     iteration_duration.............: avg=15.01ms min=8.83ms  med=14.68ms max=302ms    p(90)=18.06ms p(95)=19.24ms  p(99.9)=26.53ms
     iterations.....................: 399292  3301.176022/s
     success_rate...................: 100.00% ✓ 399292      ✗ 0     
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

     checks.........................: 100.00% ✓ 1017519     ✗ 0     
     data_received..................: 30 GB   245 MB/s
     data_sent......................: 408 MB  3.4 MB/s
     http_req_blocked...............: avg=2.92µs  min=852ns   med=2.2µs   max=4.71ms   p(90)=3.69µs  p(95)=4.49µs   p(99.9)=31.28µs
     http_req_connecting............: avg=315ns   min=0s      med=0s      max=4.65ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.47ms min=11.73ms med=17.03ms max=287.78ms p(90)=20.54ms p(95)=21.8ms   p(99.9)=28.6ms 
       { expected_response:true }...: avg=17.47ms min=11.73ms med=17.03ms max=287.78ms p(90)=20.54ms p(95)=21.8ms   p(99.9)=28.6ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 339273
     http_req_receiving.............: avg=71.05µs min=24.42µs med=46.15µs max=155.86ms p(90)=95.42µs p(95)=158.45µs p(99.9)=1.62ms 
     http_req_sending...............: avg=29.97µs min=4.27µs  med=8.3µs   max=197.17ms p(90)=17.19µs p(95)=87.98µs  p(99.9)=1.45ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.37ms min=11.69ms med=16.94ms max=287.58ms p(90)=20.44ms p(95)=21.68ms  p(99.9)=28.33ms
     http_reqs......................: 339273  2794.796185/s
     iteration_duration.............: avg=17.68ms min=11.9ms  med=17.23ms max=313.87ms p(90)=20.74ms p(95)=22ms     p(99.9)=28.83ms
     iterations.....................: 339173  2793.972425/s
     success_rate...................: 100.00% ✓ 339173      ✗ 0     
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

     checks.........................: 100.00% ✓ 1008504     ✗ 0     
     data_received..................: 29 GB   242 MB/s
     data_sent......................: 404 MB  3.3 MB/s
     http_req_blocked...............: avg=2.5µs   min=802ns   med=1.82µs  max=5.34ms   p(90)=3.26µs  p(95)=4.16µs   p(99.9)=25.89µs
     http_req_connecting............: avg=269ns   min=0s      med=0s      max=3.56ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.63ms min=11.66ms med=17.2ms  max=284.36ms p(90)=20.73ms p(95)=21.95ms  p(99.9)=28.63ms
       { expected_response:true }...: avg=17.63ms min=11.66ms med=17.2ms  max=284.36ms p(90)=20.73ms p(95)=21.95ms  p(99.9)=28.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 336268
     http_req_receiving.............: avg=66.11µs min=23.21µs med=43.41µs max=93.68ms  p(90)=92.43µs p(95)=147.55µs p(99.9)=1.42ms 
     http_req_sending...............: avg=27.76µs min=4.1µs   med=7.84µs  max=157.2ms  p(90)=17.57µs p(95)=81.92µs  p(99.9)=1.44ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.54ms min=11.6ms  med=17.12ms max=284.07ms p(90)=20.63ms p(95)=21.84ms  p(99.9)=28.36ms
     http_reqs......................: 336268  2769.931041/s
     iteration_duration.............: avg=17.84ms min=11.9ms  med=17.4ms  max=307.56ms p(90)=20.92ms p(95)=22.14ms  p(99.9)=28.85ms
     iterations.....................: 336168  2769.107314/s
     success_rate...................: 100.00% ✓ 336168      ✗ 0     
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

     checks.........................: 100.00% ✓ 1005321     ✗ 0     
     data_received..................: 29 GB   242 MB/s
     data_sent......................: 403 MB  3.3 MB/s
     http_req_blocked...............: avg=2.74µs  min=911ns   med=2.27µs  max=4.38ms   p(90)=3.66µs  p(95)=4.41µs   p(99.9)=31.68µs
     http_req_connecting............: avg=104ns   min=0s      med=0s      max=1.51ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.69ms min=11.65ms med=17.28ms max=286.69ms p(90)=20.62ms p(95)=21.89ms  p(99.9)=28.77ms
       { expected_response:true }...: avg=17.69ms min=11.65ms med=17.28ms max=286.69ms p(90)=20.62ms p(95)=21.89ms  p(99.9)=28.77ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 335207
     http_req_receiving.............: avg=69.55µs min=23.79µs med=47.33µs max=122.26ms p(90)=92.37µs p(95)=151.88µs p(99.9)=1.37ms 
     http_req_sending...............: avg=29.2µs  min=4.39µs  med=8.54µs  max=133.31ms p(90)=16.1µs  p(95)=87.03µs  p(99.9)=1.46ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.59ms min=11.59ms med=17.19ms max=286.05ms p(90)=20.52ms p(95)=21.77ms  p(99.9)=28.55ms
     http_reqs......................: 335207  2761.030324/s
     iteration_duration.............: avg=17.89ms min=11.81ms med=17.48ms max=296.5ms  p(90)=20.82ms p(95)=22.09ms  p(99.9)=29ms   
     iterations.....................: 335107  2760.206645/s
     success_rate...................: 100.00% ✓ 335107      ✗ 0     
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

     checks.........................: 100.00% ✓ 1001337     ✗ 0     
     data_received..................: 29 GB   241 MB/s
     data_sent......................: 401 MB  3.3 MB/s
     http_req_blocked...............: avg=2.5µs   min=802ns   med=1.88µs  max=4.14ms   p(90)=3.15µs  p(95)=3.84µs   p(99.9)=25.02µs
     http_req_connecting............: avg=275ns   min=0s      med=0s      max=4.11ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.76ms min=11.86ms med=17.34ms max=283.69ms p(90)=20.81ms p(95)=22.03ms  p(99.9)=28.86ms
       { expected_response:true }...: avg=17.76ms min=11.86ms med=17.34ms max=283.69ms p(90)=20.81ms p(95)=22.03ms  p(99.9)=28.86ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 333879
     http_req_receiving.............: avg=65.54µs min=24.11µs med=44.49µs max=32.69ms  p(90)=89.77µs p(95)=142.33µs p(99.9)=1.32ms 
     http_req_sending...............: avg=27.67µs min=4.39µs  med=7.95µs  max=123.59ms p(90)=16.29µs p(95)=81.49µs  p(99.9)=1.32ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.67ms min=11.82ms med=17.26ms max=270.36ms p(90)=20.71ms p(95)=21.92ms  p(99.9)=28.61ms
     http_reqs......................: 333879  2749.818057/s
     iteration_duration.............: avg=17.96ms min=11.99ms med=17.54ms max=291.8ms  p(90)=21.01ms p(95)=22.23ms  p(99.9)=29.11ms
     iterations.....................: 333779  2748.994459/s
     success_rate...................: 100.00% ✓ 333779      ✗ 0     
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

     checks.........................: 100.00% ✓ 748773      ✗ 0     
     data_received..................: 22 GB   179 MB/s
     data_sent......................: 300 MB  2.5 MB/s
     http_req_blocked...............: avg=3.12µs  min=812ns   med=2.08µs  max=8.41ms   p(90)=3.6µs   p(95)=4.29µs   p(99.9)=30.86µs 
     http_req_connecting............: avg=686ns   min=0s      med=0s      max=8.39ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.82ms min=16.89ms med=23.48ms max=287.89ms p(90)=26.8ms  p(95)=27.87ms  p(99.9)=33.19ms 
       { expected_response:true }...: avg=23.82ms min=16.89ms med=23.48ms max=287.89ms p(90)=26.8ms  p(95)=27.87ms  p(99.9)=33.19ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 249691
     http_req_receiving.............: avg=62.01µs min=24.92µs med=48.26µs max=144.33ms p(90)=85.96µs p(95)=106.12µs p(99.9)=804.27µs
     http_req_sending...............: avg=25.97µs min=4.56µs  med=9.12µs  max=241.49ms p(90)=16.57µs p(95)=21.98µs  p(99.9)=882.44µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.73ms min=16.82ms med=23.39ms max=286.19ms p(90)=26.71ms p(95)=27.78ms  p(99.9)=33.07ms 
     http_reqs......................: 249691  2048.768025/s
     iteration_duration.............: avg=24.03ms min=17.05ms med=23.68ms max=301.27ms p(90)=27ms    p(95)=28.07ms  p(99.9)=33.43ms 
     iterations.....................: 249591  2047.947503/s
     success_rate...................: 100.00% ✓ 249591      ✗ 0     
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

     checks.........................: 100.00% ✓ 545097      ✗ 0     
     data_received..................: 16 GB   130 MB/s
     data_sent......................: 218 MB  1.8 MB/s
     http_req_blocked...............: avg=3.21µs  min=862ns   med=2.45µs  max=2.86ms   p(90)=4.44µs  p(95)=5.28µs   p(99.9)=36.22µs 
     http_req_connecting............: avg=367ns   min=0s      med=0s      max=2.79ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.77ms min=17.56ms med=32.3ms  max=271.64ms p(90)=38.11ms p(95)=40.13ms  p(99.9)=52.91ms 
       { expected_response:true }...: avg=32.77ms min=17.56ms med=32.3ms  max=271.64ms p(90)=38.11ms p(95)=40.13ms  p(99.9)=52.91ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 181799
     http_req_receiving.............: avg=72.59µs min=24.92µs med=59.73µs max=17.04ms  p(90)=101.3µs p(95)=120.15µs p(99.9)=886.6µs 
     http_req_sending...............: avg=23.51µs min=4.74µs  med=11.79µs max=207.34ms p(90)=20.4µs  p(95)=24.45µs  p(99.9)=784.31µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.68ms min=17.43ms med=32.21ms max=270.81ms p(90)=38.01ms p(95)=40.03ms  p(99.9)=52.79ms 
     http_reqs......................: 181799  1490.688437/s
     iteration_duration.............: avg=33.01ms min=20.87ms med=32.52ms max=309.74ms p(90)=38.33ms p(95)=40.35ms  p(99.9)=53.35ms 
     iterations.....................: 181699  1489.868472/s
     success_rate...................: 100.00% ✓ 181699      ✗ 0     
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

     checks.........................: 100.00% ✓ 524199      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 210 MB  1.7 MB/s
     http_req_blocked...............: avg=4.07µs  min=1.06µs  med=2.99µs  max=4.12ms   p(90)=5.22µs   p(95)=6.22µs   p(99.9)=46.15µs
     http_req_connecting............: avg=598ns   min=0s      med=0s      max=4.08ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.06ms min=17.36ms med=33.73ms max=324.32ms p(90)=39.83ms  p(95)=41.56ms  p(99.9)=50.09ms
       { expected_response:true }...: avg=34.06ms min=17.36ms med=33.73ms max=324.32ms p(90)=39.83ms  p(95)=41.56ms  p(99.9)=50.09ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 174833
     http_req_receiving.............: avg=85.19µs min=25.23µs med=61.62µs max=94.25ms  p(90)=122.12µs p(95)=165.72µs p(99.9)=1.38ms 
     http_req_sending...............: avg=33.9µs  min=4.67µs  med=11.26µs max=204.1ms  p(90)=23.56µs  p(95)=50.95µs  p(99.9)=1.46ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.95ms min=17.22ms med=33.62ms max=323.98ms p(90)=39.71ms  p(95)=41.44ms  p(99.9)=49.82ms
     http_reqs......................: 174833  1433.739925/s
     iteration_duration.............: avg=34.32ms min=20.1ms  med=33.98ms max=336.94ms p(90)=40.06ms  p(95)=41.79ms  p(99.9)=50.39ms
     iterations.....................: 174733  1432.919862/s
     success_rate...................: 100.00% ✓ 174733      ✗ 0     
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

     checks.........................: 100.00% ✓ 518673      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 208 MB  1.7 MB/s
     http_req_blocked...............: avg=3.6µs   min=1.02µs  med=2.59µs  max=10.23ms  p(90)=4.2µs    p(95)=4.93µs   p(99.9)=31.82µs 
     http_req_connecting............: avg=629ns   min=0s      med=0s      max=4.87ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.47ms min=18.03ms med=33.91ms max=305.82ms p(90)=41.14ms  p(95)=43.46ms  p(99.9)=55.49ms 
       { expected_response:true }...: avg=34.47ms min=18.03ms med=33.91ms max=305.82ms p(90)=41.14ms  p(95)=43.46ms  p(99.9)=55.49ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 172991
     http_req_receiving.............: avg=78.22µs min=26.14µs med=63.39µs max=191.88ms p(90)=102.86µs p(95)=121.54µs p(99.9)=765.68µs
     http_req_sending...............: avg=22.84µs min=4.84µs  med=11.01µs max=73.88ms  p(90)=17.62µs  p(95)=21.91µs  p(99.9)=806.23µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.37ms min=17.96ms med=33.82ms max=295.11ms p(90)=41.04ms  p(95)=43.37ms  p(99.9)=55.32ms 
     http_reqs......................: 172991  1418.4139/s
     iteration_duration.............: avg=34.69ms min=20.4ms  med=34.12ms max=318.75ms p(90)=41.34ms  p(95)=43.66ms  p(99.9)=55.77ms 
     iterations.....................: 172891  1417.593965/s
     success_rate...................: 100.00% ✓ 172891      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 196800     ✗ 0    
     data_received..................: 5.8 GB  47 MB/s
     data_sent......................: 79 MB   646 kB/s
     http_req_blocked...............: avg=4.36µs  min=1.06µs  med=2.77µs  max=4ms      p(90)=4.23µs   p(95)=4.85µs   p(99.9)=52.27µs 
     http_req_connecting............: avg=1.35µs  min=0s      med=0s      max=3.97ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=91.13ms min=20.12ms med=89.69ms max=359.6ms  p(90)=106.83ms p(95)=115.49ms p(99.9)=206.6ms 
       { expected_response:true }...: avg=91.13ms min=20.12ms med=89.69ms max=359.6ms  p(90)=106.83ms p(95)=115.49ms p(99.9)=206.6ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 65700
     http_req_receiving.............: avg=79.17µs min=29.17µs med=70.88µs max=78.8ms   p(90)=105.08µs p(95)=117.41µs p(99.9)=567.23µs
     http_req_sending...............: avg=21.42µs min=5.18µs  med=13.66µs max=144.08ms p(90)=19.53µs  p(95)=21.54µs  p(99.9)=546.39µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.03ms min=20.01ms med=89.59ms max=359.07ms p(90)=106.74ms p(95)=115.39ms p(99.9)=206.4ms 
     http_reqs......................: 65700   537.455338/s
     iteration_duration.............: avg=91.48ms min=27.94ms med=89.94ms max=368.72ms p(90)=107.08ms p(95)=115.77ms p(99.9)=207.42ms
     iterations.....................: 65600   536.637293/s
     success_rate...................: 100.00% ✓ 65600      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 194478     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   638 kB/s
     http_req_blocked...............: avg=4.53µs  min=1.09µs  med=2.77µs  max=4.12ms   p(90)=4.27µs   p(95)=4.85µs   p(99.9)=44.53µs 
     http_req_connecting............: avg=1.52µs  min=0s      med=0s      max=4.08ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.2ms  min=19.51ms med=90.55ms max=298.57ms p(90)=116.09ms p(95)=124.14ms p(99.9)=161.43ms
       { expected_response:true }...: avg=92.2ms  min=19.51ms med=90.55ms max=298.57ms p(90)=116.09ms p(95)=124.14ms p(99.9)=161.43ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64926
     http_req_receiving.............: avg=79.46µs min=29.75µs med=71.08µs max=169.51ms p(90)=104.4µs  p(95)=117.04µs p(99.9)=520.36µs
     http_req_sending...............: avg=19.18µs min=4.99µs  med=14.26µs max=53.51ms  p(90)=20.04µs  p(95)=22.07µs  p(99.9)=521.39µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.1ms  min=19.38ms med=90.45ms max=298.37ms p(90)=115.99ms p(95)=124.05ms p(99.9)=160.65ms
     http_reqs......................: 64926   531.342754/s
     iteration_duration.............: avg=92.57ms min=25.29ms med=90.82ms max=315.07ms p(90)=116.36ms p(95)=124.41ms p(99.9)=163.44ms
     iterations.....................: 64826   530.524372/s
     success_rate...................: 100.00% ✓ 64826      ✗ 0    
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

     checks.........................: 100.00% ✓ 153258     ✗ 0    
     data_received..................: 4.5 GB  37 MB/s
     data_sent......................: 62 MB   502 kB/s
     http_req_blocked...............: avg=5.36µs   min=1.28µs  med=3.26µs   max=3.88ms   p(90)=4.69µs   p(95)=5.27µs   p(99.9)=172.62µs
     http_req_connecting............: avg=1.86µs   min=0s      med=0s       max=3.84ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=117.03ms min=21.2ms  med=115.26ms max=345.98ms p(90)=144.67ms p(95)=154.33ms p(99.9)=199.94ms
       { expected_response:true }...: avg=117.03ms min=21.2ms  med=115.26ms max=345.98ms p(90)=144.67ms p(95)=154.33ms p(99.9)=199.94ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51186
     http_req_receiving.............: avg=82.91µs  min=29.46µs med=79.37µs  max=3ms      p(90)=109.99µs p(95)=121.23µs p(99.9)=630.03µs
     http_req_sending...............: avg=22.11µs  min=5.58µs  med=16.17µs  max=64.11ms  p(90)=21.33µs  p(95)=23.27µs  p(99.9)=548.76µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=116.92ms min=21.06ms med=115.16ms max=345.43ms p(90)=144.56ms p(95)=154.24ms p(99.9)=199.63ms
     http_reqs......................: 51186   418.42714/s
     iteration_duration.............: avg=117.48ms min=31ms    med=115.54ms max=354.16ms p(90)=144.95ms p(95)=154.64ms p(99.9)=201.83ms
     iterations.....................: 51086   417.609676/s
     success_rate...................: 100.00% ✓ 51086      ✗ 0    
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

     checks.........................: 100.00% ✓ 97407      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   319 kB/s
     http_req_blocked...............: avg=6.03µs   min=1.15µs  med=3.14µs   max=3.59ms   p(90)=4.4µs    p(95)=4.92µs   p(99.9)=1.29ms  
     http_req_connecting............: avg=2.7µs    min=0s      med=0s       max=3.55ms   p(90)=0s       p(95)=0s       p(99.9)=1.26ms  
     http_req_duration..............: avg=184.12ms min=22.67ms med=184.16ms max=359.51ms p(90)=197.5ms  p(95)=202.73ms p(99.9)=273.32ms
       { expected_response:true }...: avg=184.12ms min=22.67ms med=184.16ms max=359.51ms p(90)=197.5ms  p(95)=202.73ms p(99.9)=273.32ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32569
     http_req_receiving.............: avg=94.42µs  min=30.17µs med=84.18µs  max=157.02ms p(90)=113.15µs p(95)=123.79µs p(99.9)=403.27µs
     http_req_sending...............: avg=21.36µs  min=5.17µs  med=15.8µs   max=54.86ms  p(90)=19.99µs  p(95)=21.7µs   p(99.9)=468.93µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.01ms min=22.53ms med=184.07ms max=348.74ms p(90)=197.39ms p(95)=202.63ms p(99.9)=272.95ms
     http_reqs......................: 32569   265.718932/s
     iteration_duration.............: avg=184.9ms  min=56.05ms med=184.62ms max=365.78ms p(90)=197.77ms p(95)=203.01ms p(99.9)=275.36ms
     iterations.....................: 32469   264.903068/s
     success_rate...................: 100.00% ✓ 32469      ✗ 0    
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

     checks.........................: 100.00% ✓ 95940      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   315 kB/s
     http_req_blocked...............: avg=7.06µs   min=1.3µs   med=3.73µs   max=4.13ms   p(90)=5.24µs   p(95)=5.88µs   p(99.9)=1.48ms  
     http_req_connecting............: avg=3.08µs   min=0s      med=0s       max=4.09ms   p(90)=0s       p(95)=0s       p(99.9)=1.46ms  
     http_req_duration..............: avg=186.95ms min=17.58ms med=170.72ms max=725.16ms p(90)=253.12ms p(95)=290.25ms p(99.9)=664.18ms
       { expected_response:true }...: avg=186.95ms min=17.58ms med=170.72ms max=725.16ms p(90)=253.12ms p(95)=290.25ms p(99.9)=664.18ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32080
     http_req_receiving.............: avg=97.65µs  min=37.38µs med=89.6µs   max=47.81ms  p(90)=120.86µs p(95)=132.62µs p(99.9)=1.05ms  
     http_req_sending...............: avg=25.68µs  min=6.57µs  med=18.71µs  max=48.32ms  p(90)=23.57µs  p(95)=25.49µs  p(99.9)=503.96µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=186.83ms min=17.49ms med=170.6ms  max=725.05ms p(90)=253ms    p(95)=290.08ms p(99.9)=664.07ms
     http_reqs......................: 32080   262.595018/s
     iteration_duration.............: avg=187.76ms min=53.68ms med=171.16ms max=725.42ms p(90)=253.53ms p(95)=290.85ms p(99.9)=664.54ms
     iterations.....................: 31980   261.776455/s
     success_rate...................: 100.00% ✓ 31980      ✗ 0    
     vus............................: 22      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

