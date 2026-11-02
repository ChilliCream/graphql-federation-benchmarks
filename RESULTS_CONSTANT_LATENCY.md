## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 3,452 | 3,468 | 3,427 | 0.5% | 384 MB | 113.9 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 3,428 | 3,441 | 3,414 | 0.4% | 381 MB | 113.9 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 3,384 | 3,402 | 3,344 | 0.6% | 134 MB | 40.6 KB |  |
| fusion-aot-11 | 16.7.3 | 3,343 | 3,365 | 3,332 | 0.4% | 137 MB | 41.9 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,295 | 3,304 | 3,278 | 0.4% | 2,311 MB | 718.1 KB |  |
| fusion-fed-net-11 | 16.7.3 | 2,782 | 2,792 | 2,780 | 0.2% | 387 MB | 142.5 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 2,781 | 2,793 | 2,778 | 0.2% | 392 MB | 144.2 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 2,761 | 2,773 | 2,754 | 0.3% | 140 MB | 52.0 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 2,746 | 2,770 | 2,728 | 0.7% | 128 MB | 47.6 KB |  |
| hive-router | v0.3.6 | 2,039 | 2,055 | 2,032 | 0.5% | 92 MB | 46.0 KB |  |
| caliban | 3.2.0 | 1,473 | 1,474 | 1,470 | 0.1% | 4,931 MB | 3,428.1 KB |  |
| grafbase | 0.53.5 | 1,452 | 1,459 | 1,443 | 0.4% | 100 MB | 70.3 KB |  |
| cosmo | 0.363.0 | 1,411 | 1,414 | 1,395 | 0.6% | 150 MB | 108.5 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 521 | 522 | 519 | 0.3% | 2,746 MB | 5,397.7 KB |  |
| apollo-router | v2.19.0 | 481 | 482 | 481 | 0.1% | 177 MB | 376.9 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 417 | 418 | 417 | 0.1% | 205 MB | 502.2 KB |  |
| apollo-gateway | 2.14.4 | 271 | 271 | 270 | 0.2% | 2,140 MB | 8,087.2 KB |  |
| hive-gateway | 2.15.3 | 252 | 253 | 252 | 0.2% | 3,403 MB | 13,829.8 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1252587     ✗ 0     
     data_received..................: 37 GB   302 MB/s
     data_sent......................: 502 MB  4.1 MB/s
     http_req_blocked...............: avg=2.78µs  min=811ns   med=1.81µs  max=14.33ms  p(90)=3.01µs  p(95)=3.76µs   p(99.9)=23.72µs
     http_req_connecting............: avg=542ns   min=0s      med=0s      max=8.62ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.16ms min=8.3ms   med=13.73ms max=275.25ms p(90)=17.59ms p(95)=18.93ms  p(99.9)=26.7ms 
       { expected_response:true }...: avg=14.16ms min=8.3ms   med=13.73ms max=275.25ms p(90)=17.59ms p(95)=18.93ms  p(99.9)=26.7ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 417629
     http_req_receiving.............: avg=68.97µs min=23.25µs med=42.21µs max=177.13ms p(90)=90.39µs p(95)=171.16µs p(99.9)=2.03ms 
     http_req_sending...............: avg=31.2µs  min=4.34µs  med=7.82µs  max=115.53ms p(90)=16.64µs p(95)=91.65µs  p(99.9)=2.1ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.06ms min=8.23ms  med=13.64ms max=273.21ms p(90)=17.48ms p(95)=18.82ms  p(99.9)=26.47ms
     http_reqs......................: 417629  3452.780817/s
     iteration_duration.............: avg=14.36ms min=8.44ms  med=13.93ms max=289.32ms p(90)=17.77ms p(95)=19.12ms  p(99.9)=26.93ms
     iterations.....................: 417529  3451.954059/s
     success_rate...................: 100.00% ✓ 417529      ✗ 0     
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

     checks.........................: 100.00% ✓ 1243881     ✗ 0     
     data_received..................: 36 GB   300 MB/s
     data_sent......................: 498 MB  4.1 MB/s
     http_req_blocked...............: avg=3.08µs  min=832ns   med=2.16µs  max=126.65ms p(90)=3.58µs  p(95)=4.39µs   p(99.9)=28.56µs
     http_req_connecting............: avg=231ns   min=0s      med=0s      max=4.07ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.26ms min=8.16ms  med=13.8ms  max=291.93ms p(90)=17.79ms p(95)=19.22ms  p(99.9)=27.28ms
       { expected_response:true }...: avg=14.26ms min=8.16ms  med=13.8ms  max=291.93ms p(90)=17.79ms p(95)=19.22ms  p(99.9)=27.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 414727
     http_req_receiving.............: avg=73.99µs min=25.28µs med=45.51µs max=155.69ms p(90)=96.93µs p(95)=184.23µs p(99.9)=2.27ms 
     http_req_sending...............: avg=32.98µs min=3.94µs  med=8.2µs   max=114.25ms p(90)=17.48µs p(95)=98µs     p(99.9)=2.09ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.15ms min=8.1ms   med=13.7ms  max=291.39ms p(90)=17.67ms p(95)=19.09ms  p(99.9)=26.96ms
     http_reqs......................: 414727  3428.721546/s
     iteration_duration.............: avg=14.46ms min=8.28ms  med=14ms    max=313.74ms p(90)=17.98ms p(95)=19.41ms  p(99.9)=27.52ms
     iterations.....................: 414627  3427.894804/s
     success_rate...................: 100.00% ✓ 414627      ✗ 0     
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

     checks.........................: 100.00% ✓ 1227942     ✗ 0     
     data_received..................: 36 GB   296 MB/s
     data_sent......................: 492 MB  4.1 MB/s
     http_req_blocked...............: avg=2.77µs  min=842ns   med=2.17µs  max=4.19ms   p(90)=3.51µs  p(95)=4.24µs  p(99.9)=29.23µs
     http_req_connecting............: avg=238ns   min=0s      med=0s      max=4.15ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=14.45ms min=8.14ms  med=13.99ms max=278.9ms  p(90)=17.85ms p(95)=19.26ms p(99.9)=27.74ms
       { expected_response:true }...: avg=14.45ms min=8.14ms  med=13.99ms max=278.9ms  p(90)=17.85ms p(95)=19.26ms p(99.9)=27.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 409414
     http_req_receiving.............: avg=71.04µs min=24.49µs med=44.83µs max=58.18ms  p(90)=93.87µs p(95)=177.8µs p(99.9)=1.85ms 
     http_req_sending...............: avg=32.48µs min=4.15µs  med=8.31µs  max=217.23ms p(90)=16.97µs p(95)=97.01µs p(99.9)=1.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=14.34ms min=8.09ms  med=13.89ms max=278.72ms p(90)=17.75ms p(95)=19.13ms p(99.9)=27.5ms 
     http_reqs......................: 409414  3384.604127/s
     iteration_duration.............: avg=14.65ms min=8.33ms  med=14.19ms max=296.11ms p(90)=18.05ms p(95)=19.45ms p(99.9)=28.04ms
     iterations.....................: 409314  3383.777433/s
     success_rate...................: 100.00% ✓ 409314      ✗ 0     
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

     checks.........................: 100.00% ✓ 1213095     ✗ 0     
     data_received..................: 35 GB   293 MB/s
     data_sent......................: 486 MB  4.0 MB/s
     http_req_blocked...............: avg=2.86µs  min=932ns   med=2.28µs  max=4.05ms   p(90)=3.62µs  p(95)=4.34µs   p(99.9)=28.63µs
     http_req_connecting............: avg=237ns   min=0s      med=0s      max=4.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.62ms min=8.4ms   med=14.18ms max=273.99ms p(90)=18.13ms p(95)=19.54ms  p(99.9)=28.16ms
       { expected_response:true }...: avg=14.62ms min=8.4ms   med=14.18ms max=273.99ms p(90)=18.13ms p(95)=19.54ms  p(99.9)=28.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 404465
     http_req_receiving.............: avg=72.79µs min=24.48µs med=45.39µs max=114.9ms  p(90)=94.26µs p(95)=182.22µs p(99.9)=1.94ms 
     http_req_sending...............: avg=32.7µs  min=4.53µs  med=8.59µs  max=190.08ms p(90)=16.94µs p(95)=99.29µs  p(99.9)=1.85ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.52ms min=8.36ms  med=14.07ms max=273.41ms p(90)=18.02ms p(95)=19.42ms  p(99.9)=27.94ms
     http_reqs......................: 404465  3343.558122/s
     iteration_duration.............: avg=14.82ms min=8.57ms  med=14.38ms max=287.12ms p(90)=18.32ms p(95)=19.74ms  p(99.9)=28.38ms
     iterations.....................: 404365  3342.73146/s
     success_rate...................: 100.00% ✓ 404365      ✗ 0     
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

     checks.........................: 100.00% ✓ 1195605     ✗ 0     
     data_received..................: 35 GB   288 MB/s
     data_sent......................: 479 MB  4.0 MB/s
     http_req_blocked...............: avg=2.55µs  min=791ns  med=1.93µs  max=3.71ms   p(90)=3.32µs  p(95)=4.12µs   p(99.9)=25.3µs 
     http_req_connecting............: avg=251ns   min=0s     med=0s      max=3.67ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.85ms min=8.21ms med=14.52ms max=272.12ms p(90)=17.9ms  p(95)=19.09ms  p(99.9)=26.46ms
       { expected_response:true }...: avg=14.85ms min=8.21ms med=14.52ms max=272.12ms p(90)=17.9ms  p(95)=19.09ms  p(99.9)=26.46ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 398635
     http_req_receiving.............: avg=67.9µs  min=23.3µs med=44.51µs max=167.54ms p(90)=91.04µs p(95)=159.49µs p(99.9)=1.59ms 
     http_req_sending...............: avg=30.87µs min=4.12µs med=8.18µs  max=108.9ms  p(90)=16.53µs p(95)=91.21µs  p(99.9)=1.62ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.75ms min=8.12ms med=14.42ms max=271.66ms p(90)=17.8ms  p(95)=18.98ms  p(99.9)=26.24ms
     http_reqs......................: 398635  3295.802491/s
     iteration_duration.............: avg=15.04ms min=8.73ms med=14.71ms max=293.55ms p(90)=18.09ms p(95)=19.28ms  p(99.9)=26.68ms
     iterations.....................: 398535  3294.975719/s
     success_rate...................: 100.00% ✓ 398535      ✗ 0     
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

     checks.........................: 100.00% ✓ 1012905     ✗ 0     
     data_received..................: 30 GB   243 MB/s
     data_sent......................: 406 MB  3.3 MB/s
     http_req_blocked...............: avg=2.97µs  min=842ns   med=2.28µs  max=4.48ms   p(90)=3.76µs  p(95)=4.57µs   p(99.9)=28.23µs
     http_req_connecting............: avg=323ns   min=0s      med=0s      max=4.44ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.55ms min=11.31ms med=17.1ms  max=282.49ms p(90)=20.68ms p(95)=21.94ms  p(99.9)=29.03ms
       { expected_response:true }...: avg=17.55ms min=11.31ms med=17.1ms  max=282.49ms p(90)=20.68ms p(95)=21.94ms  p(99.9)=29.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 337735
     http_req_receiving.............: avg=72.19µs min=23.93µs med=47.79µs max=192.12ms p(90)=97.14µs p(95)=160.79µs p(99.9)=1.57ms 
     http_req_sending...............: avg=29.88µs min=4.56µs  med=8.81µs  max=72.3ms   p(90)=17.97µs p(95)=90.48µs  p(99.9)=1.6ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.44ms min=11.2ms  med=17ms    max=272.37ms p(90)=20.57ms p(95)=21.83ms  p(99.9)=28.78ms
     http_reqs......................: 337735  2782.232159/s
     iteration_duration.............: avg=17.76ms min=11.66ms med=17.3ms  max=301.43ms p(90)=20.88ms p(95)=22.15ms  p(99.9)=29.25ms
     iterations.....................: 337635  2781.408368/s
     success_rate...................: 100.00% ✓ 337635      ✗ 0     
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

     checks.........................: 100.00% ✓ 1012770     ✗ 0     
     data_received..................: 30 GB   243 MB/s
     data_sent......................: 406 MB  3.3 MB/s
     http_req_blocked...............: avg=2.34µs  min=821ns   med=1.85µs  max=3.47ms   p(90)=3.08µs  p(95)=3.8µs    p(99.9)=24.58µs
     http_req_connecting............: avg=147ns   min=0s      med=0s      max=2.42ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.56ms min=11.83ms med=17.14ms max=286.85ms p(90)=20.64ms p(95)=21.87ms  p(99.9)=28.22ms
       { expected_response:true }...: avg=17.56ms min=11.83ms med=17.14ms max=286.85ms p(90)=20.64ms p(95)=21.87ms  p(99.9)=28.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 337690
     http_req_receiving.............: avg=65.61µs min=24.08µs med=43.93µs max=103.68ms p(90)=89.15µs p(95)=144.68µs p(99.9)=1.41ms 
     http_req_sending...............: avg=27.92µs min=4.28µs  med=7.93µs  max=150.56ms p(90)=16.06µs p(95)=80.7µs   p(99.9)=1.4ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.46ms min=11.77ms med=17.05ms max=286.57ms p(90)=20.54ms p(95)=21.76ms  p(99.9)=27.93ms
     http_reqs......................: 337690  2781.603875/s
     iteration_duration.............: avg=17.76ms min=12ms    med=17.34ms max=295.99ms p(90)=20.83ms p(95)=22.06ms  p(99.9)=28.45ms
     iterations.....................: 337590  2780.78016/s
     success_rate...................: 100.00% ✓ 337590      ✗ 0     
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

     checks.........................: 100.00% ✓ 1005549     ✗ 0     
     data_received..................: 29 GB   242 MB/s
     data_sent......................: 403 MB  3.3 MB/s
     http_req_blocked...............: avg=3.01µs  min=801ns   med=1.84µs  max=8.95ms   p(90)=3.25µs  p(95)=4.04µs   p(99.9)=26.35µs
     http_req_connecting............: avg=758ns   min=0s      med=0s      max=8.91ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.68ms min=11.92ms med=17.27ms max=301.47ms p(90)=20.65ms p(95)=21.89ms  p(99.9)=28.52ms
       { expected_response:true }...: avg=17.68ms min=11.92ms med=17.27ms max=301.47ms p(90)=20.65ms p(95)=21.89ms  p(99.9)=28.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 335283
     http_req_receiving.............: avg=66.44µs min=25.2µs  med=44.71µs max=130.17ms p(90)=91.62µs p(95)=141.63µs p(99.9)=1.39ms 
     http_req_sending...............: avg=28.2µs  min=4.06µs  med=7.92µs  max=213.18ms p(90)=16.81µs p(95)=82.19µs  p(99.9)=1.39ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.59ms min=11.86ms med=17.18ms max=299.81ms p(90)=20.55ms p(95)=21.78ms  p(99.9)=28.26ms
     http_reqs......................: 335283  2761.635046/s
     iteration_duration.............: avg=17.89ms min=12.09ms med=17.47ms max=312.09ms p(90)=20.85ms p(95)=22.08ms  p(99.9)=28.72ms
     iterations.....................: 335183  2760.811374/s
     success_rate...................: 100.00% ✓ 335183      ✗ 0     
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

     checks.........................: 100.00% ✓ 1000017     ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 401 MB  3.3 MB/s
     http_req_blocked...............: avg=2.46µs  min=792ns   med=1.82µs  max=3.98ms   p(90)=3.1µs   p(95)=3.9µs    p(99.9)=24.07µs
     http_req_connecting............: avg=281ns   min=0s      med=0s      max=3.94ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.79ms min=11.84ms med=17.36ms max=289.13ms p(90)=20.84ms p(95)=22.1ms   p(99.9)=28.94ms
       { expected_response:true }...: avg=17.79ms min=11.84ms med=17.36ms max=289.13ms p(90)=20.84ms p(95)=22.1ms   p(99.9)=28.94ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 333439
     http_req_receiving.............: avg=65.65µs min=25.5µs  med=45.72µs max=50.41ms  p(90)=90.38µs p(95)=140.08µs p(99.9)=1.21ms 
     http_req_sending...............: avg=26.98µs min=4.42µs  med=7.94µs  max=188.63ms p(90)=16.04µs p(95)=78.32µs  p(99.9)=1.27ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.69ms min=11.79ms med=17.27ms max=289ms    p(90)=20.74ms p(95)=21.99ms  p(99.9)=28.72ms
     http_reqs......................: 333439  2746.339066/s
     iteration_duration.............: avg=17.99ms min=12.01ms med=17.55ms max=302.43ms p(90)=21.04ms p(95)=22.29ms  p(99.9)=29.14ms
     iterations.....................: 333339  2745.515425/s
     success_rate...................: 100.00% ✓ 333339      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 745515      ✗ 0     
     data_received..................: 22 GB   178 MB/s
     data_sent......................: 299 MB  2.5 MB/s
     http_req_blocked...............: avg=2.91µs  min=802ns   med=2.14µs  max=3.88ms   p(90)=3.73µs  p(95)=4.45µs   p(99.9)=29.83µs 
     http_req_connecting............: avg=411ns   min=0s      med=0s      max=3.83ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.92ms min=16.96ms med=23.58ms max=301.55ms p(90)=26.91ms p(95)=27.98ms  p(99.9)=33.67ms 
       { expected_response:true }...: avg=23.92ms min=16.96ms med=23.58ms max=301.55ms p(90)=26.91ms p(95)=27.98ms  p(99.9)=33.67ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 248605
     http_req_receiving.............: avg=65.08µs min=24.52µs med=49.31µs max=201.87ms p(90)=88.98µs p(95)=109.97µs p(99.9)=866.86µs
     http_req_sending...............: avg=23.23µs min=4.54µs  med=9.19µs  max=106.66ms p(90)=16.5µs  p(95)=22.01µs  p(99.9)=893.1µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.83ms min=16.9ms  med=23.5ms  max=301.12ms p(90)=26.82ms p(95)=27.89ms  p(99.9)=33.49ms 
     http_reqs......................: 248605  2039.77069/s
     iteration_duration.............: avg=24.13ms min=17.1ms  med=23.78ms max=322.86ms p(90)=27.12ms p(95)=28.19ms  p(99.9)=33.91ms 
     iterations.....................: 248505  2038.950203/s
     success_rate...................: 100.00% ✓ 248505      ✗ 0     
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

     checks.........................: 100.00% ✓ 538668      ✗ 0     
     data_received..................: 16 GB   129 MB/s
     data_sent......................: 216 MB  1.8 MB/s
     http_req_blocked...............: avg=4.04µs  min=941ns   med=2.63µs  max=7.47ms   p(90)=4.58µs   p(95)=5.4µs    p(99.9)=34.49µs 
     http_req_connecting............: avg=961ns   min=0s      med=0s      max=6.99ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.17ms min=17.82ms med=32.72ms max=292.46ms p(90)=38.64ms  p(95)=40.68ms  p(99.9)=53.68ms 
       { expected_response:true }...: avg=33.17ms min=17.82ms med=32.72ms max=292.46ms p(90)=38.64ms  p(95)=40.68ms  p(99.9)=53.68ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 179656
     http_req_receiving.............: avg=76.06µs min=26.75µs med=62.69µs max=104.83ms p(90)=104.15µs p(95)=123.04µs p(99.9)=876.6µs 
     http_req_sending...............: avg=24.65µs min=4.7µs   med=12.09µs max=134.67ms p(90)=20.56µs  p(95)=24.55µs  p(99.9)=798.33µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.07ms min=17.74ms med=32.62ms max=291.17ms p(90)=38.54ms  p(95)=40.58ms  p(99.9)=53.59ms 
     http_reqs......................: 179656  1473.153263/s
     iteration_duration.............: avg=33.4ms  min=20.43ms med=32.94ms max=302.68ms p(90)=38.85ms  p(95)=40.9ms   p(99.9)=53.96ms 
     iterations.....................: 179556  1472.333278/s
     success_rate...................: 100.00% ✓ 179556      ✗ 0     
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

     checks.........................: 100.00% ✓ 531246      ✗ 0     
     data_received..................: 16 GB   127 MB/s
     data_sent......................: 213 MB  1.7 MB/s
     http_req_blocked...............: avg=3.66µs  min=1.03µs  med=2.96µs  max=1.79ms   p(90)=5.21µs   p(95)=6.18µs   p(99.9)=41.15µs
     http_req_connecting............: avg=234ns   min=0s      med=0s      max=1.77ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.6ms  min=18.2ms  med=33.26ms max=311.22ms p(90)=39.23ms  p(95)=40.98ms  p(99.9)=49.33ms
       { expected_response:true }...: avg=33.6ms  min=18.2ms  med=33.26ms max=311.22ms p(90)=39.23ms  p(95)=40.98ms  p(99.9)=49.33ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 177182
     http_req_receiving.............: avg=88.06µs min=27.66µs med=61.96µs max=128.76ms p(90)=124.88µs p(95)=167.38µs p(99.9)=1.48ms 
     http_req_sending...............: avg=30.63µs min=4.74µs  med=11.4µs  max=85.52ms  p(90)=23.47µs  p(95)=43.33µs  p(99.9)=1.33ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.48ms min=18.1ms  med=33.15ms max=311.07ms p(90)=39.11ms  p(95)=40.86ms  p(99.9)=49.04ms
     http_reqs......................: 177182  1452.995765/s
     iteration_duration.............: avg=33.87ms min=19.82ms med=33.52ms max=319.45ms p(90)=39.46ms  p(95)=41.21ms  p(99.9)=49.64ms
     iterations.....................: 177082  1452.175707/s
     success_rate...................: 100.00% ✓ 177082      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 516024      ✗ 0     
     data_received..................: 15 GB   123 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=4.17µs  min=972ns   med=2.39µs  max=9.65ms   p(90)=3.9µs   p(95)=4.59µs   p(99.9)=29.35µs 
     http_req_connecting............: avg=1.38µs  min=0s      med=0s      max=9.07ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.66ms min=18.17ms med=34.11ms max=296.05ms p(90)=41.39ms p(95)=43.72ms  p(99.9)=55.79ms 
       { expected_response:true }...: avg=34.66ms min=18.17ms med=34.11ms max=296.05ms p(90)=41.39ms p(95)=43.72ms  p(99.9)=55.79ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 172108
     http_req_receiving.............: avg=74.37µs min=26.26µs med=61.66µs max=86.79ms  p(90)=99.7µs  p(95)=117.46µs p(99.9)=743.54µs
     http_req_sending...............: avg=22.72µs min=4.57µs  med=10.54µs max=114.23ms p(90)=17.07µs p(95)=21.11µs  p(99.9)=790.19µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.56ms min=18.13ms med=34.02ms max=287.28ms p(90)=41.3ms  p(95)=43.62ms  p(99.9)=55.4ms  
     http_reqs......................: 172108  1411.128046/s
     iteration_duration.............: avg=34.87ms min=18.36ms med=34.31ms max=315.42ms p(90)=41.59ms p(95)=43.91ms  p(99.9)=56ms    
     iterations.....................: 172008  1410.308137/s
     success_rate...................: 100.00% ✓ 172008      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 190866     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   626 kB/s
     http_req_blocked...............: avg=4.59µs  min=1.05µs  med=2.82µs  max=3.85ms   p(90)=4.34µs   p(95)=4.93µs   p(99.9)=45.54µs 
     http_req_connecting............: avg=1.55µs  min=0s      med=0s      max=3.81ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.97ms min=20.35ms med=91.3ms  max=355.82ms p(90)=115.27ms p(95)=124.32ms p(99.9)=222.78ms
       { expected_response:true }...: avg=93.97ms min=20.35ms med=91.3ms  max=355.82ms p(90)=115.27ms p(95)=124.32ms p(99.9)=222.78ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63722
     http_req_receiving.............: avg=81.36µs min=27.18µs med=71.11µs max=121.01ms p(90)=105.12µs p(95)=117.31µs p(99.9)=533.13µs
     http_req_sending...............: avg=23.05µs min=4.68µs  med=13.72µs max=116.94ms p(90)=19.17µs  p(95)=21.1µs   p(99.9)=557.07µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.86ms min=20.26ms med=91.21ms max=355.61ms p(90)=115.17ms p(95)=124.2ms  p(99.9)=222.07ms
     http_reqs......................: 63722   521.161902/s
     iteration_duration.............: avg=94.32ms min=42.22ms med=91.54ms max=363.34ms p(90)=115.51ms p(95)=124.6ms  p(99.9)=223.72ms
     iterations.....................: 63622   520.344034/s
     success_rate...................: 100.00% ✓ 63622      ✗ 0    
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

     checks.........................: 100.00% ✓ 176355     ✗ 0    
     data_received..................: 5.1 GB  42 MB/s
     data_sent......................: 71 MB   579 kB/s
     http_req_blocked...............: avg=4.35µs   min=982ns   med=2.64µs  max=4.28ms   p(90)=4.02µs   p(95)=4.57µs   p(99.9)=88.13µs 
     http_req_connecting............: avg=1.39µs   min=0s      med=0s      max=4.1ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=101.71ms min=19.65ms med=99.7ms  max=297.5ms  p(90)=129.05ms p(95)=138.4ms  p(99.9)=180.35ms
       { expected_response:true }...: avg=101.71ms min=19.65ms med=99.7ms  max=297.5ms  p(90)=129.05ms p(95)=138.4ms  p(99.9)=180.35ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 58885
     http_req_receiving.............: avg=75.26µs  min=28.01µs med=66.79µs max=74.66ms  p(90)=99.98µs  p(95)=112.49µs p(99.9)=489.82µs
     http_req_sending...............: avg=16.95µs  min=4.81µs  med=12.54µs max=41.59ms  p(90)=18.25µs  p(95)=20.14µs  p(99.9)=503.67µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=101.62ms min=19.54ms med=99.62ms max=283.24ms p(90)=128.94ms p(95)=138.31ms p(99.9)=180.02ms
     http_reqs......................: 58885   481.769479/s
     iteration_duration.............: avg=102.09ms min=24.66ms med=99.96ms max=325.03ms p(90)=129.3ms  p(95)=138.68ms p(99.9)=182.59ms
     iterations.....................: 58785   480.951326/s
     success_rate...................: 100.00% ✓ 58785      ✗ 0    
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

     checks.........................: 100.00% ✓ 152940     ✗ 0    
     data_received..................: 4.5 GB  37 MB/s
     data_sent......................: 61 MB   501 kB/s
     http_req_blocked...............: avg=5.57µs   min=1.26µs  med=3.43µs   max=3.45ms   p(90)=4.94µs   p(95)=5.55µs   p(99.9)=308.4µs 
     http_req_connecting............: avg=1.89µs   min=0s      med=0s       max=3.41ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=117.26ms min=20.78ms med=115.72ms max=320.28ms p(90)=144.92ms p(95)=153.96ms p(99.9)=198.53ms
       { expected_response:true }...: avg=117.26ms min=20.78ms med=115.72ms max=320.28ms p(90)=144.92ms p(95)=153.96ms p(99.9)=198.53ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51080
     http_req_receiving.............: avg=84.74µs  min=29.16µs med=77.8µs   max=108.44ms p(90)=110.34µs p(95)=122.02µs p(99.9)=511.09µs
     http_req_sending...............: avg=23.4µs   min=5.56µs  med=15.95µs  max=85.58ms  p(90)=21.59µs  p(95)=23.68µs  p(99.9)=502.72µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=117.15ms min=20.64ms med=115.61ms max=314.51ms p(90)=144.82ms p(95)=153.83ms p(99.9)=197.97ms
     http_reqs......................: 51080   417.611616/s
     iteration_duration.............: avg=117.71ms min=42.83ms med=116.01ms max=356.71ms p(90)=145.2ms  p(95)=154.23ms p(99.9)=200.57ms
     iterations.....................: 50980   416.794052/s
     success_rate...................: 100.00% ✓ 50980      ✗ 0    
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

     checks.........................: 100.00% ✓ 99696      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   327 kB/s
     http_req_blocked...............: avg=6.94µs   min=1.38µs  med=3.58µs   max=3.83ms   p(90)=5.06µs   p(95)=5.67µs   p(99.9)=1.7ms   
     http_req_connecting............: avg=3.08µs   min=0s      med=0s       max=3.79ms   p(90)=0s       p(95)=0s       p(99.9)=1.68ms  
     http_req_duration..............: avg=179.88ms min=21.91ms med=180.8ms  max=402.46ms p(90)=191.95ms p(95)=196.72ms p(99.9)=266.4ms 
       { expected_response:true }...: avg=179.88ms min=21.91ms med=180.8ms  max=402.46ms p(90)=191.95ms p(95)=196.72ms p(99.9)=266.4ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 33332
     http_req_receiving.............: avg=93.93µs  min=35.77µs med=88.17µs  max=62.37ms  p(90)=118.08µs p(95)=129.38µs p(99.9)=483.9µs 
     http_req_sending...............: avg=30.05µs  min=6.23µs  med=17.3µs   max=117.21ms p(90)=21.97µs  p(95)=23.85µs  p(99.9)=459.38µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=179.76ms min=21.78ms med=180.68ms max=401.99ms p(90)=191.84ms p(95)=196.61ms p(99.9)=265.42ms
     http_reqs......................: 33332   271.906894/s
     iteration_duration.............: avg=180.66ms min=58.98ms med=181.19ms max=412.52ms p(90)=192.25ms p(95)=197.02ms p(99.9)=269.4ms 
     iterations.....................: 33232   271.091141/s
     success_rate...................: 100.00% ✓ 33232      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 92184      ✗ 0    
     data_received..................: 2.7 GB  22 MB/s
     data_sent......................: 37 MB   303 kB/s
     http_req_blocked...............: avg=5.68µs   min=1.49µs  med=3.56µs   max=3.23ms   p(90)=4.99µs   p(95)=5.6µs    p(99.9)=590.54µs
     http_req_connecting............: avg=1.86µs   min=0s      med=0s       max=3.21ms   p(90)=0s       p(95)=0s       p(99.9)=569.56µs
     http_req_duration..............: avg=194.54ms min=17.22ms med=182.18ms max=645.04ms p(90)=230.42ms p(95)=259.96ms p(99.9)=594.08ms
       { expected_response:true }...: avg=194.54ms min=17.22ms med=182.18ms max=645.04ms p(90)=230.42ms p(95)=259.96ms p(99.9)=594.08ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 30828
     http_req_receiving.............: avg=133.01µs min=35.95µs med=85.87µs  max=186.81ms p(90)=115.75µs p(95)=127.27µs p(99.9)=1.09ms  
     http_req_sending...............: avg=29.11µs  min=6.13µs  med=17.34µs  max=132.58ms p(90)=21.9µs   p(95)=23.64µs  p(99.9)=556.71µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=194.37ms min=17.15ms med=182.05ms max=644.95ms p(90)=230.24ms p(95)=259.33ms p(99.9)=593.98ms
     http_reqs......................: 30828   252.447233/s
     iteration_duration.............: avg=195.41ms min=52.16ms med=182.6ms  max=645.34ms p(90)=230.78ms p(95)=261.65ms p(99.9)=594.3ms 
     iterations.....................: 30728   251.628344/s
     success_rate...................: 100.00% ✓ 30728      ✗ 0    
     vus............................: 29      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

