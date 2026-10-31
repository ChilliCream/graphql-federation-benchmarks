## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 3,433 | 3,449 | 3,429 | 0.3% | 398 MB | 118.6 KB |  |
| fusion-net-11 | 16.7.3 | 3,411 | 3,422 | 3,406 | 0.2% | 402 MB | 120.8 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 3,391 | 3,439 | 3,379 | 0.7% | 130 MB | 39.2 KB |  |
| fusion-aot-11 | 16.7.3 | 3,362 | 3,368 | 3,346 | 0.3% | 144 MB | 43.9 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,279 | 3,314 | 3,242 | 0.9% | 2,296 MB | 717.1 KB |  |
| fusion-fed-net-11 | 16.7.3 | 2,793 | 2,805 | 2,792 | 0.2% | 384 MB | 140.9 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 2,781 | 2,794 | 2,771 | 0.3% | 391 MB | 143.9 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 2,754 | 2,769 | 2,747 | 0.3% | 142 MB | 52.7 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 2,743 | 2,756 | 2,737 | 0.3% | 136 MB | 50.9 KB |  |
| hive-router | v0.3.6 | 2,058 | 2,062 | 2,050 | 0.2% | 90 MB | 44.7 KB |  |
| caliban | 3.2.0 | 1,479 | 1,482 | 1,477 | 0.1% | 5,175 MB | 3,583.0 KB |  |
| grafbase | 0.53.5 | 1,435 | 1,443 | 1,429 | 0.4% | 101 MB | 72.2 KB |  |
| cosmo | 0.363.0 | 1,433 | 1,434 | 1,429 | 0.2% | 148 MB | 105.6 KB |  |
| apollo-router | v2.19.0 | 527 | 528 | 527 | 0.1% | 180 MB | 349.9 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 524 | 525 | 522 | 0.3% | 2,743 MB | 5,360.2 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 410 | 420 | 391 | 2.8% | 207 MB | 517.8 KB |  |
| hive-gateway | 2.15.3 | 268 | 269 | 267 | 0.3% | 3,558 MB | 13,595.8 KB |  |
| apollo-gateway | 2.14.4 | 267 | 268 | 266 | 0.3% | 2,172 MB | 8,328.8 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1245750     ✗ 0     
     data_received..................: 36 GB   301 MB/s
     data_sent......................: 499 MB  4.1 MB/s
     http_req_blocked...............: avg=2.78µs  min=792ns   med=1.82µs  max=7.98ms   p(90)=3.07µs  p(95)=3.8µs    p(99.9)=24.45µs
     http_req_connecting............: avg=560ns   min=0s      med=0s      max=7.96ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.24ms min=8.13ms  med=13.81ms max=288.88ms p(90)=17.71ms p(95)=19.07ms  p(99.9)=26.76ms
       { expected_response:true }...: avg=14.24ms min=8.13ms  med=13.81ms max=288.88ms p(90)=17.71ms p(95)=19.07ms  p(99.9)=26.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 415350
     http_req_receiving.............: avg=68.53µs min=23.98µs med=41.99µs max=128.31ms p(90)=91.02µs p(95)=172.68µs p(99.9)=2.02ms 
     http_req_sending...............: avg=30.6µs  min=4.23µs  med=7.7µs   max=149.1ms  p(90)=15.88µs p(95)=91.48µs  p(99.9)=1.85ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.14ms min=8.08ms  med=13.72ms max=280.21ms p(90)=17.61ms p(95)=18.94ms  p(99.9)=26.46ms
     http_reqs......................: 415350  3433.949757/s
     iteration_duration.............: avg=14.44ms min=8.27ms  med=14.01ms max=302.8ms  p(90)=17.9ms  p(95)=19.25ms  p(99.9)=26.97ms
     iterations.....................: 415250  3433.122997/s
     success_rate...................: 100.00% ✓ 415250      ✗ 0     
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

     checks.........................: 100.00% ✓ 1237731     ✗ 0     
     data_received..................: 36 GB   299 MB/s
     data_sent......................: 496 MB  4.1 MB/s
     http_req_blocked...............: avg=2.43µs  min=802ns   med=1.84µs  max=4.3ms    p(90)=3.04µs  p(95)=3.8µs    p(99.9)=23.21µs
     http_req_connecting............: avg=253ns   min=0s      med=0s      max=4.26ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.33ms min=7.97ms  med=13.91ms max=287.9ms  p(90)=17.83ms p(95)=19.18ms  p(99.9)=27.25ms
       { expected_response:true }...: avg=14.33ms min=7.97ms  med=13.91ms max=287.9ms  p(90)=17.83ms p(95)=19.18ms  p(99.9)=27.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 412677
     http_req_receiving.............: avg=77.45µs min=24.38µs med=42.7µs  max=188.24ms p(90)=91.31µs p(95)=170.29µs p(99.9)=2.17ms 
     http_req_sending...............: avg=31.93µs min=4.4µs   med=7.88µs  max=221.89ms p(90)=16.75µs p(95)=91.2µs   p(99.9)=1.91ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.22ms min=7.92ms  med=13.81ms max=100.3ms  p(90)=17.72ms p(95)=19.07ms  p(99.9)=26.95ms
     http_reqs......................: 412677  3411.749212/s
     iteration_duration.............: avg=14.53ms min=8.12ms  med=14.1ms  max=317.16ms p(90)=18.02ms p(95)=19.38ms  p(99.9)=27.59ms
     iterations.....................: 412577  3410.922476/s
     success_rate...................: 100.00% ✓ 412577      ✗ 0     
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

     checks.........................: 100.00% ✓ 1230612     ✗ 0     
     data_received..................: 36 GB   297 MB/s
     data_sent......................: 493 MB  4.1 MB/s
     http_req_blocked...............: avg=2.44µs  min=791ns   med=1.84µs  max=3.9ms    p(90)=3µs     p(95)=3.74µs   p(99.9)=24.33µs
     http_req_connecting............: avg=244ns   min=0s      med=0s      max=3.86ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.42ms min=8.29ms  med=13.98ms max=273.45ms p(90)=17.84ms p(95)=19.21ms  p(99.9)=27.4ms 
       { expected_response:true }...: avg=14.42ms min=8.29ms  med=13.98ms max=273.45ms p(90)=17.84ms p(95)=19.21ms  p(99.9)=27.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 410304
     http_req_receiving.............: avg=68.27µs min=24.71µs med=43.77µs max=24.74ms  p(90)=90.21µs p(95)=169.04µs p(99.9)=1.9ms  
     http_req_sending...............: avg=30.92µs min=4.52µs  med=7.9µs   max=140.44ms p(90)=15.88µs p(95)=91.38µs  p(99.9)=1.72ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.32ms min=8.24ms  med=13.88ms max=259.06ms p(90)=17.74ms p(95)=19.1ms   p(99.9)=27.14ms
     http_reqs......................: 410304  3391.955265/s
     iteration_duration.............: avg=14.61ms min=8.45ms  med=14.17ms max=283.57ms p(90)=18.03ms p(95)=19.41ms  p(99.9)=27.6ms 
     iterations.....................: 410204  3391.128572/s
     success_rate...................: 100.00% ✓ 410204      ✗ 0     
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

     checks.........................: 100.00% ✓ 1219968     ✗ 0     
     data_received..................: 36 GB   294 MB/s
     data_sent......................: 489 MB  4.0 MB/s
     http_req_blocked...............: avg=2.71µs  min=861ns   med=2.14µs  max=3.36ms   p(90)=3.4µs   p(95)=4.07µs   p(99.9)=28.83µs
     http_req_connecting............: avg=239ns   min=0s      med=0s      max=3.32ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.54ms min=8.13ms  med=14.09ms max=286.47ms p(90)=18.05ms p(95)=19.47ms  p(99.9)=27.81ms
       { expected_response:true }...: avg=14.54ms min=8.13ms  med=14.09ms max=286.47ms p(90)=18.05ms p(95)=19.47ms  p(99.9)=27.81ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 406756
     http_req_receiving.............: avg=71.62µs min=24.61µs med=45.57µs max=82.81ms  p(90)=91.94µs p(95)=179.45µs p(99.9)=1.99ms 
     http_req_sending...............: avg=32.32µs min=4.52µs  med=8.31µs  max=191.54ms p(90)=15.85µs p(95)=96.68µs  p(99.9)=1.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.44ms min=8.04ms  med=13.99ms max=273.93ms p(90)=17.94ms p(95)=19.35ms  p(99.9)=27.54ms
     http_reqs......................: 406756  3362.576282/s
     iteration_duration.............: avg=14.74ms min=8.31ms  med=14.28ms max=294.85ms p(90)=18.24ms p(95)=19.67ms  p(99.9)=28.06ms
     iterations.....................: 406656  3361.749601/s
     success_rate...................: 100.00% ✓ 406656      ✗ 0     
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

     checks.........................: 100.00% ✓ 1189887     ✗ 0     
     data_received..................: 35 GB   287 MB/s
     data_sent......................: 477 MB  3.9 MB/s
     http_req_blocked...............: avg=3µs     min=932ns   med=2.42µs  max=3.57ms   p(90)=3.84µs  p(95)=4.59µs   p(99.9)=31.81µs
     http_req_connecting............: avg=216ns   min=0s      med=0s      max=3.53ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.91ms min=8.56ms  med=14.54ms max=285.59ms p(90)=18.1ms  p(95)=19.38ms  p(99.9)=27.35ms
       { expected_response:true }...: avg=14.91ms min=8.56ms  med=14.54ms max=285.59ms p(90)=18.1ms  p(95)=19.38ms  p(99.9)=27.35ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 396729
     http_req_receiving.............: avg=73.39µs min=24.06µs med=47.57µs max=66.2ms   p(90)=96.03µs p(95)=183.58µs p(99.9)=1.78ms 
     http_req_sending...............: avg=34.24µs min=4.59µs  med=9.13µs  max=157.44ms p(90)=17.77µs p(95)=102.43µs p(99.9)=1.81ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.8ms  min=8.49ms  med=14.44ms max=285.09ms p(90)=17.99ms p(95)=19.25ms  p(99.9)=27.09ms
     http_reqs......................: 396729  3279.656532/s
     iteration_duration.............: avg=15.11ms min=8.75ms  med=14.74ms max=301.24ms p(90)=18.3ms  p(95)=19.58ms  p(99.9)=27.57ms
     iterations.....................: 396629  3278.829858/s
     success_rate...................: 100.00% ✓ 396629      ✗ 0     
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

     checks.........................: 100.00% ✓ 1017063     ✗ 0     
     data_received..................: 30 GB   244 MB/s
     data_sent......................: 408 MB  3.4 MB/s
     http_req_blocked...............: avg=2.46µs  min=761ns   med=1.81µs  max=3.34ms   p(90)=3.27µs  p(95)=4.12µs   p(99.9)=24.95µs
     http_req_connecting............: avg=248ns   min=0s      med=0s      max=3.3ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.48ms min=11.61ms med=17.05ms max=281.61ms p(90)=20.51ms p(95)=21.74ms  p(99.9)=28.76ms
       { expected_response:true }...: avg=17.48ms min=11.61ms med=17.05ms max=281.61ms p(90)=20.51ms p(95)=21.74ms  p(99.9)=28.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 339121
     http_req_receiving.............: avg=67.57µs min=24.48µs med=44.43µs max=81.57ms  p(90)=94.29µs p(95)=147.63µs p(99.9)=1.59ms 
     http_req_sending...............: avg=27.95µs min=4.18µs  med=7.72µs  max=208.24ms p(90)=16.75µs p(95)=82.44µs  p(99.9)=1.52ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.39ms min=11.55ms med=16.96ms max=273.31ms p(90)=20.41ms p(95)=21.62ms  p(99.9)=28.45ms
     http_reqs......................: 339121  2793.672713/s
     iteration_duration.............: avg=17.68ms min=11.8ms  med=17.25ms max=297.52ms p(90)=20.71ms p(95)=21.93ms  p(99.9)=29.04ms
     iterations.....................: 339021  2792.848914/s
     success_rate...................: 100.00% ✓ 339021      ✗ 0     
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

     checks.........................: 100.00% ✓ 1012896     ✗ 0     
     data_received..................: 30 GB   243 MB/s
     data_sent......................: 406 MB  3.3 MB/s
     http_req_blocked...............: avg=2.47µs  min=771ns   med=1.8µs   max=3.66ms   p(90)=3.26µs  p(95)=4.11µs   p(99.9)=24.5µs 
     http_req_connecting............: avg=279ns   min=0s      med=0s      max=3.63ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.55ms min=11.67ms med=17.12ms max=287.08ms p(90)=20.65ms p(95)=21.91ms  p(99.9)=28.91ms
       { expected_response:true }...: avg=17.55ms min=11.67ms med=17.12ms max=287.08ms p(90)=20.65ms p(95)=21.91ms  p(99.9)=28.91ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 337732
     http_req_receiving.............: avg=66.91µs min=23.65µs med=42.83µs max=128.03ms p(90)=90.48µs p(95)=142.13µs p(99.9)=1.75ms 
     http_req_sending...............: avg=26.88µs min=4.12µs  med=7.77µs  max=82.02ms  p(90)=16.58µs p(95)=79.5µs   p(99.9)=1.39ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.46ms min=11.6ms  med=17.04ms max=286.72ms p(90)=20.55ms p(95)=21.79ms  p(99.9)=28.51ms
     http_reqs......................: 337732  2781.852748/s
     iteration_duration.............: avg=17.76ms min=11.89ms med=17.32ms max=305.84ms p(90)=20.84ms p(95)=22.1ms   p(99.9)=29.15ms
     iterations.....................: 337632  2781.029061/s
     success_rate...................: 100.00% ✓ 337632      ✗ 0     
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

     checks.........................: 100.00% ✓ 1003008     ✗ 0     
     data_received..................: 29 GB   241 MB/s
     data_sent......................: 402 MB  3.3 MB/s
     http_req_blocked...............: avg=2.52µs  min=811ns   med=1.85µs  max=3.4ms    p(90)=3.28µs  p(95)=4.07µs   p(99.9)=24.83µs
     http_req_connecting............: avg=280ns   min=0s      med=0s      max=3.36ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.73ms min=11.89ms med=17.31ms max=303.21ms p(90)=20.77ms p(95)=22.02ms  p(99.9)=29.31ms
       { expected_response:true }...: avg=17.73ms min=11.89ms med=17.31ms max=303.21ms p(90)=20.77ms p(95)=22.02ms  p(99.9)=29.31ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 334436
     http_req_receiving.............: avg=65.93µs min=25.13µs med=44.54µs max=17.25ms  p(90)=92.25µs p(95)=143.78µs p(99.9)=1.34ms 
     http_req_sending...............: avg=26.53µs min=4.37µs  med=7.89µs  max=87.63ms  p(90)=16.36µs p(95)=80.53µs  p(99.9)=1.3ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.64ms min=11.81ms med=17.22ms max=302.77ms p(90)=20.67ms p(95)=21.91ms  p(99.9)=29.01ms
     http_reqs......................: 334436  2754.903104/s
     iteration_duration.............: avg=17.93ms min=12.14ms med=17.51ms max=312.43ms p(90)=20.96ms p(95)=22.22ms  p(99.9)=29.52ms
     iterations.....................: 334336  2754.079358/s
     success_rate...................: 100.00% ✓ 334336      ✗ 0     
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

     checks.........................: 100.00% ✓ 999072      ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 400 MB  3.3 MB/s
     http_req_blocked...............: avg=2.51µs  min=821ns   med=1.88µs  max=3.93ms   p(90)=3.13µs  p(95)=3.86µs   p(99.9)=23.11µs
     http_req_connecting............: avg=292ns   min=0s      med=0s      max=3.9ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.8ms  min=11.79ms med=17.39ms max=288.47ms p(90)=20.81ms p(95)=22.03ms  p(99.9)=28.48ms
       { expected_response:true }...: avg=17.8ms  min=11.79ms med=17.39ms max=288.47ms p(90)=20.81ms p(95)=22.03ms  p(99.9)=28.48ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 333124
     http_req_receiving.............: avg=64.77µs min=23.88µs med=44.27µs max=41.43ms  p(90)=88.22µs p(95)=140.68µs p(99.9)=1.31ms 
     http_req_sending...............: avg=27.93µs min=4.36µs  med=7.9µs   max=210.08ms p(90)=15.54µs p(95)=79.66µs  p(99.9)=1.25ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.71ms min=11.64ms med=17.31ms max=288.03ms p(90)=20.71ms p(95)=21.92ms  p(99.9)=28.23ms
     http_reqs......................: 333124  2743.957925/s
     iteration_duration.............: avg=18ms    min=11.99ms med=17.59ms max=298.33ms p(90)=21ms    p(95)=22.23ms  p(99.9)=28.71ms
     iterations.....................: 333024  2743.13422/s
     success_rate...................: 100.00% ✓ 333024      ✗ 0     
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

     checks.........................: 100.00% ✓ 752496      ✗ 0     
     data_received..................: 22 GB   180 MB/s
     data_sent......................: 302 MB  2.5 MB/s
     http_req_blocked...............: avg=2.87µs  min=811ns   med=2.13µs  max=4.05ms   p(90)=3.79µs  p(95)=4.5µs    p(99.9)=30.12µs 
     http_req_connecting............: avg=375ns   min=0s      med=0s      max=4ms      p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.7ms  min=17.34ms med=23.37ms max=285.9ms  p(90)=26.65ms p(95)=27.71ms  p(99.9)=33.04ms 
       { expected_response:true }...: avg=23.7ms  min=17.34ms med=23.37ms max=285.9ms  p(90)=26.65ms p(95)=27.71ms  p(99.9)=33.04ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 250932
     http_req_receiving.............: avg=63.29µs min=24.26µs med=48.29µs max=9.76ms   p(90)=89.74µs p(95)=112.25µs p(99.9)=900.82µs
     http_req_sending...............: avg=25.32µs min=4.41µs  med=9.3µs   max=165.17ms p(90)=17.5µs  p(95)=23.37µs  p(99.9)=915.9µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.61ms min=17.22ms med=23.28ms max=285.11ms p(90)=26.56ms p(95)=27.61ms  p(99.9)=32.86ms 
     http_reqs......................: 250932  2058.864068/s
     iteration_duration.............: avg=23.91ms min=17.58ms med=23.57ms max=306.71ms p(90)=26.85ms p(95)=27.91ms  p(99.9)=33.26ms 
     iterations.....................: 250832  2058.043581/s
     success_rate...................: 100.00% ✓ 250832      ✗ 0     
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

     checks.........................: 100.00% ✓ 541164      ✗ 0     
     data_received..................: 16 GB   129 MB/s
     data_sent......................: 217 MB  1.8 MB/s
     http_req_blocked...............: avg=3.33µs  min=962ns   med=2.43µs  max=3.94ms   p(90)=4.31µs   p(95)=5.11µs  p(99.9)=32.81µs 
     http_req_connecting............: avg=523ns   min=0s      med=0s      max=3.9ms    p(90)=0s       p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=33.02ms min=18.23ms med=32.55ms max=297.55ms p(90)=38.46ms  p(95)=40.49ms p(99.9)=51.88ms 
       { expected_response:true }...: avg=33.02ms min=18.23ms med=32.55ms max=297.55ms p(90)=38.46ms  p(95)=40.49ms p(99.9)=51.88ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 180488
     http_req_receiving.............: avg=76.47µs min=27.81µs med=62.24µs max=121.48ms p(90)=104.16µs p(95)=123.2µs p(99.9)=946.61µs
     http_req_sending...............: avg=23.66µs min=4.84µs  med=11.71µs max=110.34ms p(90)=19.82µs  p(95)=23.78µs p(99.9)=777.39µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=32.92ms min=18.13ms med=32.45ms max=291.25ms p(90)=38.35ms  p(95)=40.39ms p(99.9)=51.72ms 
     http_reqs......................: 180488  1479.78602/s
     iteration_duration.............: avg=33.25ms min=19.84ms med=32.76ms max=308.04ms p(90)=38.67ms  p(95)=40.72ms p(99.9)=52.23ms 
     iterations.....................: 180388  1478.966139/s
     success_rate...................: 100.00% ✓ 180388      ✗ 0     
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

     checks.........................: 100.00% ✓ 524646      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 210 MB  1.7 MB/s
     http_req_blocked...............: avg=3.14µs  min=792ns   med=2.1µs   max=3.49ms   p(90)=4.41µs   p(95)=5.35µs   p(99.9)=36.67µs
     http_req_connecting............: avg=502ns   min=0s      med=0s      max=3.45ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.05ms min=17.23ms med=33.83ms max=300.3ms  p(90)=39.72ms  p(95)=41.37ms  p(99.9)=49.63ms
       { expected_response:true }...: avg=34.05ms min=17.23ms med=33.83ms max=300.3ms  p(90)=39.72ms  p(95)=41.37ms  p(99.9)=49.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 174982
     http_req_receiving.............: avg=76.86µs min=25.45µs med=51.81µs max=159.75ms p(90)=113.21µs p(95)=155.98µs p(99.9)=1.39ms 
     http_req_sending...............: avg=30.07µs min=4.42µs  med=8.96µs  max=187.2ms  p(90)=21.53µs  p(95)=41.93µs  p(99.9)=1.45ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.94ms min=17.15ms med=33.73ms max=299.78ms p(90)=39.62ms  p(95)=41.26ms  p(99.9)=49.21ms
     http_reqs......................: 174982  1435.13666/s
     iteration_duration.............: avg=34.3ms  min=20.21ms med=34.06ms max=310.29ms p(90)=39.93ms  p(95)=41.58ms  p(99.9)=50.02ms
     iterations.....................: 174882  1434.316498/s
     success_rate...................: 100.00% ✓ 174882      ✗ 0     
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

     checks.........................: 100.00% ✓ 524097      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 210 MB  1.7 MB/s
     http_req_blocked...............: avg=3.59µs  min=982ns   med=2.75µs  max=3.73ms   p(90)=4.4µs    p(95)=5.15µs   p(99.9)=33.48µs 
     http_req_connecting............: avg=513ns   min=0s      med=0s      max=3.69ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.11ms min=17.97ms med=33.54ms max=299.91ms p(90)=40.62ms  p(95)=42.9ms   p(99.9)=55.31ms 
       { expected_response:true }...: avg=34.11ms min=17.97ms med=33.54ms max=299.91ms p(90)=40.62ms  p(95)=42.9ms   p(99.9)=55.31ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 174799
     http_req_receiving.............: avg=75.99µs min=24.51µs med=62.44µs max=73.12ms  p(90)=103.25µs p(95)=123.17µs p(99.9)=792.23µs
     http_req_sending...............: avg=24.01µs min=4.97µs  med=11.78µs max=90.56ms  p(90)=18.73µs  p(95)=23.24µs  p(99.9)=845.17µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.01ms min=17.89ms med=33.44ms max=299.37ms p(90)=40.52ms  p(95)=42.8ms   p(99.9)=55.06ms 
     http_reqs......................: 174799  1433.193441/s
     iteration_duration.............: avg=34.33ms min=18.95ms med=33.75ms max=316.8ms  p(90)=40.83ms  p(95)=43.11ms  p(99.9)=55.59ms 
     iterations.....................: 174699  1432.373532/s
     success_rate...................: 100.00% ✓ 174699      ✗ 0     
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

     checks.........................: 100.00% ✓ 193104     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   634 kB/s
     http_req_blocked...............: avg=4.43µs  min=1.04µs  med=2.75µs  max=4.14ms   p(90)=4.24µs   p(95)=4.78µs   p(99.9)=44.68µs 
     http_req_connecting............: avg=1.46µs  min=0s      med=0s      max=4.1ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.86ms min=19.53ms med=91.13ms max=325.8ms  p(90)=116.92ms p(95)=125.22ms p(99.9)=161.18ms
       { expected_response:true }...: avg=92.86ms min=19.53ms med=91.13ms max=325.8ms  p(90)=116.92ms p(95)=125.22ms p(99.9)=161.18ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64468
     http_req_receiving.............: avg=75.42µs min=26.39µs med=70.71µs max=2.17ms   p(90)=103.32µs p(95)=115.34µs p(99.9)=490.88µs
     http_req_sending...............: avg=20.28µs min=4.92µs  med=13.64µs max=77.61ms  p(90)=19.45µs  p(95)=21.57µs  p(99.9)=499.62µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.77ms min=19.42ms med=91.03ms max=325.5ms  p(90)=116.81ms p(95)=125.12ms p(99.9)=160.84ms
     http_reqs......................: 64468   527.572166/s
     iteration_duration.............: avg=93.22ms min=27.98ms med=91.38ms max=347.22ms p(90)=117.19ms p(95)=125.48ms p(99.9)=162.71ms
     iterations.....................: 64368   526.753819/s
     success_rate...................: 100.00% ✓ 64368      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 192099     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   630 kB/s
     http_req_blocked...............: avg=5.52µs  min=1.21µs  med=3.23µs  max=6.79ms   p(90)=4.76µs   p(95)=5.44µs   p(99.9)=46.54µs 
     http_req_connecting............: avg=1.96µs  min=0s      med=0s      max=6.67ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.36ms min=20.41ms med=88.45ms max=321.51ms p(90)=125.18ms p(95)=136.88ms p(99.9)=235.29ms
       { expected_response:true }...: avg=93.36ms min=20.41ms med=88.45ms max=321.51ms p(90)=125.18ms p(95)=136.88ms p(99.9)=235.29ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64133
     http_req_receiving.............: avg=87.96µs min=31.92µs med=76.11µs max=138.32ms p(90)=109.29µs p(95)=121.93µs p(99.9)=600.3µs 
     http_req_sending...............: avg=21.52µs min=5.62µs  med=15.11µs max=96.69ms  p(90)=20.87µs  p(95)=22.95µs  p(99.9)=622.52µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.25ms min=20.28ms med=88.35ms max=320.99ms p(90)=125.06ms p(95)=136.78ms p(99.9)=234.5ms 
     http_reqs......................: 64133   524.463048/s
     iteration_duration.............: avg=93.72ms min=29.17ms med=88.71ms max=341.39ms p(90)=125.45ms p(95)=137.18ms p(99.9)=237.08ms
     iterations.....................: 64033   523.645274/s
     success_rate...................: 100.00% ✓ 64033      ✗ 0    
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

     checks.........................: 100.00% ✓ 150189     ✗ 0    
     data_received..................: 4.4 GB  36 MB/s
     data_sent......................: 60 MB   492 kB/s
     http_req_blocked...............: avg=5.48µs   min=1.26µs  med=3.51µs   max=3.46ms   p(90)=5.01µs   p(95)=5.65µs   p(99.9)=164.89µs
     http_req_connecting............: avg=1.72µs   min=0s      med=0s       max=3.43ms   p(90)=0s       p(95)=0s       p(99.9)=63.58µs 
     http_req_duration..............: avg=119.42ms min=21.23ms med=117.66ms max=339.57ms p(90)=147.87ms p(95)=157.53ms p(99.9)=203.15ms
       { expected_response:true }...: avg=119.42ms min=21.23ms med=117.66ms max=339.57ms p(90)=147.87ms p(95)=157.53ms p(99.9)=203.15ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 50163
     http_req_receiving.............: avg=89.31µs  min=30.08µs med=77.36µs  max=179.5ms  p(90)=109.21µs p(95)=121.31µs p(99.9)=558.45µs
     http_req_sending...............: avg=24.4µs   min=5.78µs  med=16.39µs  max=120.85ms p(90)=21.77µs  p(95)=23.77µs  p(99.9)=511.56µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=119.31ms min=21.11ms med=117.57ms max=329.52ms p(90)=147.75ms p(95)=157.42ms p(99.9)=201.68ms
     http_reqs......................: 50163   410.019299/s
     iteration_duration.............: avg=119.88ms min=32.21ms med=117.95ms max=349.04ms p(90)=148.14ms p(95)=157.82ms p(99.9)=205.07ms
     iterations.....................: 50063   409.201925/s
     success_rate...................: 100.00% ✓ 50063      ✗ 0    
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

     checks.........................: 100.00% ✓ 98259      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   323 kB/s
     http_req_blocked...............: avg=5.38µs   min=1.35µs  med=3.75µs   max=2.11ms   p(90)=5.33µs   p(95)=5.98µs   p(99.9)=626.62µs
     http_req_connecting............: avg=1.31µs   min=0s      med=0s       max=2.05ms   p(90)=0s       p(95)=0s       p(99.9)=601.82µs
     http_req_duration..............: avg=182.5ms  min=17.57ms med=169.96ms max=810.51ms p(90)=209.88ms p(95)=230.08ms p(99.9)=690.14ms
       { expected_response:true }...: avg=182.5ms  min=17.57ms med=169.96ms max=810.51ms p(90)=209.88ms p(95)=230.08ms p(99.9)=690.14ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32853
     http_req_receiving.............: avg=95.81µs  min=37.21µs med=89.79µs  max=63.91ms  p(90)=120.79µs p(95)=133.39µs p(99.9)=607.89µs
     http_req_sending...............: avg=28.04µs  min=5.82µs  med=18.44µs  max=47.36ms  p(90)=23.29µs  p(95)=25.36µs  p(99.9)=515.87µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=182.38ms min=17.44ms med=169.84ms max=810.42ms p(90)=209.79ms p(95)=229.95ms p(99.9)=690.04ms
     http_reqs......................: 32853   268.984971/s
     iteration_duration.............: avg=183.28ms min=66.82ms med=170.37ms max=810.77ms p(90)=210.22ms p(95)=230.67ms p(99.9)=690.42ms
     iterations.....................: 32753   268.166218/s
     success_rate...................: 100.00% ✓ 32753      ✗ 0    
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

     checks.........................: 100.00% ✓ 98127      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   321 kB/s
     http_req_blocked...............: avg=5.97µs   min=1.11µs  med=3.16µs   max=3.53ms   p(90)=4.5µs    p(95)=5.02µs   p(99.9)=1.26ms  
     http_req_connecting............: avg=2.62µs   min=0s      med=0s       max=3.49ms   p(90)=0s       p(95)=0s       p(99.9)=1.24ms  
     http_req_duration..............: avg=182.8ms  min=22.94ms med=181.3ms  max=410.56ms p(90)=195.84ms p(95)=200.37ms p(99.9)=266.13ms
       { expected_response:true }...: avg=182.8ms  min=22.94ms med=181.3ms  max=410.56ms p(90)=195.84ms p(95)=200.37ms p(99.9)=266.13ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32809
     http_req_receiving.............: avg=86.22µs  min=30.36µs med=84.29µs  max=3.04ms   p(90)=113.45µs p(95)=123.32µs p(99.9)=484.8µs 
     http_req_sending...............: avg=25.42µs  min=5.3µs   med=15.94µs  max=85.34ms  p(90)=20.19µs  p(95)=21.95µs  p(99.9)=469.85µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=182.69ms min=22.82ms med=181.19ms max=410.07ms p(90)=195.73ms p(95)=200.25ms p(99.9)=265.81ms
     http_reqs......................: 32809   267.517982/s
     iteration_duration.............: avg=183.59ms min=61.98ms med=181.6ms  max=427.17ms p(90)=196.1ms  p(95)=200.66ms p(99.9)=268.27ms
     iterations.....................: 32709   266.702602/s
     success_rate...................: 100.00% ✓ 32709      ✗ 0    
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

