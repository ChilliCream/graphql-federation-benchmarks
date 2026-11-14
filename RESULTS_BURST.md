## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.5 | 4,726 | 4,742 | 4,705 | 0.3% | 420 MB | 91.0 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.12 | 4,653 | 4,745 | 4,599 | 1.4% | 414 MB | 91.2 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.12 | 4,650 | 4,770 | 4,637 | 1.2% | 413 MB | 90.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.12 | 4,542 | 4,652 | 4,499 | 1.3% | 153 MB | 34.6 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.12 | 4,500 | 4,514 | 4,442 | 0.6% | 150 MB | 34.1 KB |  |
| fusion-aot-11 | 16.7.5 | 4,461 | 4,486 | 4,448 | 0.4% | 155 MB | 35.6 KB |  |
| fusion-fed-net-11 | 16.7.5 | 4,412 | 4,418 | 4,406 | 0.1% | 408 MB | 94.8 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 4,401 | 4,411 | 4,399 | 0.1% | 166 MB | 38.6 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,216 | 4,235 | 4,199 | 0.4% | 2,311 MB | 561.4 KB |  |
| hive-router | v0.3.10 | 2,613 | 2,630 | 2,606 | 0.4% | 163 MB | 63.7 KB |  |
| caliban | 3.2.0 | 1,365 | 1,367 | 1,363 | 0.1% | 10,793 MB | 8,096.8 KB |  |
| cosmo | 0.365.2 | 1,295 | 1,296 | 1,292 | 0.1% | 685 MB | 541.6 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 491 | 491 | 488 | 0.3% | 3,164 MB | 6,598.0 KB |  |
| apollo-gateway | 2.14.4 | 242 | 242 | 242 | 0.0% | 2,449 MB | 10,361.8 KB |  |
| hive-gateway | 2.15.6 | 240 | 241 | 239 | 0.4% | 3,969 MB | 16,932.4 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (4318 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (3806 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (152684 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 861471      ✗ 0     
     data_received..................: 25 GB   414 MB/s
     data_sent......................: 346 MB  5.7 MB/s
     http_req_blocked...............: avg=66.7µs   min=802ns    med=2.08µs  max=137.53ms p(90)=3.65µs   p(95)=4.8µs    p(99.9)=25.51ms 
     http_req_connecting............: avg=63.34µs  min=0s       med=0s      max=137.13ms p(90)=0s       p(95)=0s       p(99.9)=25.24ms 
     http_req_duration..............: avg=47.9ms   min=773.73µs med=40.58ms max=264.42ms p(90)=100ms    p(95)=124.46ms p(99.9)=176.31ms
       { expected_response:true }...: avg=47.9ms   min=773.73µs med=40.58ms max=264.42ms p(90)=100ms    p(95)=124.46ms p(99.9)=176.31ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288157
     http_req_receiving.............: avg=375.1µs  min=25.31µs  med=52.39µs max=183.86ms p(90)=209.04µs p(95)=361.46µs p(99.9)=52ms    
     http_req_sending...............: avg=148.62µs min=4.27µs   med=8.71µs  max=196.3ms  p(90)=17.07µs  p(95)=114.57µs p(99.9)=26.77ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.38ms  min=732.32µs med=40.22ms max=252.29ms p(90)=98.89ms  p(95)=123.23ms p(99.9)=169.34ms
     http_reqs......................: 288157  4726.346595/s
     iteration_duration.............: avg=49.6ms   min=1.24ms   med=41.26ms max=317.37ms p(90)=104.13ms p(95)=129.73ms p(99.9)=200.21ms
     iterations.....................: 287157  4709.944611/s
     success_rate...................: 100.00% ✓ 287157      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.12)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 847662      ✗ 0     
     data_received..................: 25 GB   407 MB/s
     data_sent......................: 341 MB  5.6 MB/s
     http_req_blocked...............: avg=71.05µs  min=832ns    med=2.65µs  max=158.88ms p(90)=4.22µs   p(95)=5.38µs   p(99.9)=27.51ms 
     http_req_connecting............: avg=66.69µs  min=0s       med=0s      max=139.79ms p(90)=0s       p(95)=0s       p(99.9)=26.73ms 
     http_req_duration..............: avg=48.09ms  min=751.37µs med=40.42ms max=299.26ms p(90)=101.67ms p(95)=126.61ms p(99.9)=186.74ms
       { expected_response:true }...: avg=48.09ms  min=751.37µs med=40.42ms max=299.26ms p(90)=101.67ms p(95)=126.61ms p(99.9)=186.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 283554
     http_req_receiving.............: avg=347.36µs min=21.78µs  med=54.28µs max=213.03ms p(90)=219.38µs p(95)=375.44µs p(99.9)=47.76ms 
     http_req_sending...............: avg=159.42µs min=4.08µs   med=9.36µs  max=100.26ms p(90)=17.38µs  p(95)=120.47µs p(99.9)=28.89ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.59ms  min=702.95µs med=40.03ms max=298.95ms p(90)=100.52ms p(95)=125.43ms p(99.9)=179.14ms
     http_reqs......................: 283554  4653.962186/s
     iteration_duration.............: avg=50.42ms  min=1.25ms   med=41.55ms max=326.95ms p(90)=107.06ms p(95)=133.94ms p(99.9)=225.79ms
     iterations.....................: 282554  4637.54922/s
     success_rate...................: 100.00% ✓ 282554      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.12)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 847023      ✗ 0     
     data_received..................: 25 GB   407 MB/s
     data_sent......................: 340 MB  5.6 MB/s
     http_req_blocked...............: avg=68.41µs  min=882ns    med=2.64µs  max=133.93ms p(90)=4.19µs   p(95)=5.34µs   p(99.9)=25.42ms 
     http_req_connecting............: avg=64.39µs  min=0s       med=0s      max=133.85ms p(90)=0s       p(95)=0s       p(99.9)=24.73ms 
     http_req_duration..............: avg=48.46ms  min=746.51µs med=40.6ms  max=300.24ms p(90)=103.5ms  p(95)=129.08ms p(99.9)=186.74ms
       { expected_response:true }...: avg=48.46ms  min=746.51µs med=40.6ms  max=300.24ms p(90)=103.5ms  p(95)=129.08ms p(99.9)=186.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 283341
     http_req_receiving.............: avg=361.53µs min=25.62µs  med=53.28µs max=141.38ms p(90)=220.45µs p(95)=380.2µs  p(99.9)=51.12ms 
     http_req_sending...............: avg=155.02µs min=4.05µs   med=9.18µs  max=188.3ms  p(90)=17.27µs  p(95)=121.56µs p(99.9)=28.15ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.94ms  min=701.86µs med=40.26ms max=299.79ms p(90)=102.13ms p(95)=127.48ms p(99.9)=181.22ms
     http_reqs......................: 283341  4650.699673/s
     iteration_duration.............: avg=50.45ms  min=1.17ms   med=41.6ms  max=338.67ms p(90)=108.46ms p(95)=135.46ms p(99.9)=221.53ms
     iterations.....................: 282341  4634.285883/s
     success_rate...................: 100.00% ✓ 282341      ✗ 0     
     vus............................: 55      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.12)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 828585      ✗ 0     
     data_received..................: 24 GB   398 MB/s
     data_sent......................: 333 MB  5.5 MB/s
     http_req_blocked...............: avg=62.35µs  min=841ns    med=2.3µs   max=196.85ms p(90)=4µs      p(95)=5.19µs   p(99.9)=22.14ms 
     http_req_connecting............: avg=58.22µs  min=0s       med=0s      max=196.77ms p(90)=0s       p(95)=0s       p(99.9)=21.27ms 
     http_req_duration..............: avg=49.91ms  min=827.19µs med=41.11ms max=295.08ms p(90)=108.1ms  p(95)=135.89ms p(99.9)=194.12ms
       { expected_response:true }...: avg=49.91ms  min=827.19µs med=41.11ms max=295.08ms p(90)=108.1ms  p(95)=135.89ms p(99.9)=194.12ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 277195
     http_req_receiving.............: avg=330.89µs min=23.81µs  med=51.42µs max=152.29ms p(90)=217.02µs p(95)=389.33µs p(99.9)=48ms    
     http_req_sending...............: avg=142.29µs min=4.43µs   med=8.8µs   max=241.88ms p(90)=17.47µs  p(95)=125.92µs p(99.9)=26.53ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.43ms  min=769.38µs med=40.84ms max=294.79ms p(90)=106.97ms p(95)=134.73ms p(99.9)=186.17ms
     http_reqs......................: 277195  4542.89581/s
     iteration_duration.............: avg=51.58ms  min=1.33ms   med=41.95ms max=325.36ms p(90)=111.91ms p(95)=140.91ms p(99.9)=217.47ms
     iterations.....................: 276195  4526.507002/s
     success_rate...................: 100.00% ✓ 276195      ✗ 0     
     vus............................: 57      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.12)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 820662      ✗ 0     
     data_received..................: 24 GB   394 MB/s
     data_sent......................: 330 MB  5.4 MB/s
     http_req_blocked...............: avg=50.41µs  min=841ns    med=2.05µs  max=107.5ms  p(90)=3.61µs   p(95)=4.73µs   p(99.9)=17.46ms 
     http_req_connecting............: avg=47.39µs  min=0s       med=0s      max=107.23ms p(90)=0s       p(95)=0s       p(99.9)=16.99ms 
     http_req_duration..............: avg=50.79ms  min=813.51µs med=42.46ms max=299.22ms p(90)=108.41ms p(95)=134.17ms p(99.9)=189.79ms
       { expected_response:true }...: avg=50.79ms  min=813.51µs med=42.46ms max=299.22ms p(90)=108.41ms p(95)=134.17ms p(99.9)=189.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 274554
     http_req_receiving.............: avg=280.79µs min=26.2µs   med=50.8µs  max=125.88ms p(90)=213.53µs p(95)=376.98µs p(99.9)=36.73ms 
     http_req_sending...............: avg=124.83µs min=4.02µs   med=8.66µs  max=149.7ms  p(90)=16.87µs  p(95)=122.38µs p(99.9)=21.93ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.39ms  min=772.36µs med=42.2ms  max=256.86ms p(90)=107.58ms p(95)=133.18ms p(99.9)=184.8ms 
     http_reqs......................: 274554  4500.414426/s
     iteration_duration.............: avg=52.07ms  min=1.4ms    med=43.36ms max=327.82ms p(90)=110.96ms p(95)=137.25ms p(99.9)=208.03ms
     iterations.....................: 273554  4484.022698/s
     success_rate...................: 100.00% ✓ 273554      ✗ 0     
     vus............................: 58      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 814131      ✗ 0     
     data_received..................: 24 GB   390 MB/s
     data_sent......................: 327 MB  5.4 MB/s
     http_req_blocked...............: avg=58.86µs  min=831ns    med=2.39µs  max=120.84ms p(90)=4.04µs   p(95)=5.17µs   p(99.9)=19.86ms 
     http_req_connecting............: avg=55.29µs  min=0s       med=0s      max=120.66ms p(90)=0s       p(95)=0s       p(99.9)=19.56ms 
     http_req_duration..............: avg=51.11ms  min=845.75µs med=42.6ms  max=323.51ms p(90)=110.22ms p(95)=136.36ms p(99.9)=191.17ms
       { expected_response:true }...: avg=51.11ms  min=845.75µs med=42.6ms  max=323.51ms p(90)=110.22ms p(95)=136.36ms p(99.9)=191.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 272377
     http_req_receiving.............: avg=295.43µs min=26.23µs  med=51.07µs max=115.49ms p(90)=229.05µs p(95)=398.62µs p(99.9)=40.94ms 
     http_req_sending...............: avg=137.01µs min=4.13µs   med=8.69µs  max=134.63ms p(90)=17.5µs   p(95)=129.65µs p(99.9)=25.04ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.68ms  min=805.3µs  med=42.31ms max=304.23ms p(90)=109.26ms p(95)=135.33ms p(99.9)=186.26ms
     http_reqs......................: 272377  4461.264899/s
     iteration_duration.............: avg=52.49ms  min=1.3ms    med=43.39ms max=332.07ms p(90)=112.44ms p(95)=140.73ms p(99.9)=214.95ms
     iterations.....................: 271377  4444.885892/s
     success_rate...................: 100.00% ✓ 271377      ✗ 0     
     vus............................: 60      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 806511      ✗ 0     
     data_received..................: 24 GB   386 MB/s
     data_sent......................: 324 MB  5.3 MB/s
     http_req_blocked...............: avg=65.49µs  min=1.01µs   med=2.72µs  max=128.61ms p(90)=4.41µs   p(95)=5.65µs   p(99.9)=23.72ms 
     http_req_connecting............: avg=62µs     min=0s       med=0s      max=128.53ms p(90)=0s       p(95)=0s       p(99.9)=23.63ms 
     http_req_duration..............: avg=51ms     min=926.47µs med=42.96ms max=269.18ms p(90)=108.83ms p(95)=134.73ms p(99.9)=188.74ms
       { expected_response:true }...: avg=51ms     min=926.47µs med=42.96ms max=269.18ms p(90)=108.83ms p(95)=134.73ms p(99.9)=188.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 269837
     http_req_receiving.............: avg=331.12µs min=26.41µs  med=54.87µs max=127.81ms p(90)=222.58µs p(95)=396.74µs p(99.9)=43.21ms 
     http_req_sending...............: avg=150.95µs min=4.2µs    med=9.44µs  max=146.18ms p(90)=18.59µs  p(95)=127.54µs p(99.9)=27.3ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.52ms  min=869.05µs med=42.64ms max=268.93ms p(90)=107.69ms p(95)=133.41ms p(99.9)=184.91ms
     http_reqs......................: 269837  4412.527014/s
     iteration_duration.............: avg=52.98ms  min=1.52ms   med=43.89ms max=355.87ms p(90)=112.9ms  p(95)=141.1ms  p(99.9)=225.8ms 
     iterations.....................: 268837  4396.17445/s
     success_rate...................: 100.00% ✓ 268837      ✗ 0     
     vus............................: 64      min=0         max=496 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 804942      ✗ 0     
     data_received..................: 24 GB   385 MB/s
     data_sent......................: 324 MB  5.3 MB/s
     http_req_blocked...............: avg=46.89µs  min=842ns    med=2.07µs  max=104.81ms p(90)=3.71µs   p(95)=4.86µs   p(99.9)=16.2ms  
     http_req_connecting............: avg=44.01µs  min=0s       med=0s      max=104.72ms p(90)=0s       p(95)=0s       p(99.9)=15.79ms 
     http_req_duration..............: avg=51.94ms  min=971.95µs med=43.93ms max=342.4ms  p(90)=110.17ms p(95)=135.22ms p(99.9)=188.73ms
       { expected_response:true }...: avg=51.94ms  min=971.95µs med=43.93ms max=342.4ms  p(90)=110.17ms p(95)=135.22ms p(99.9)=188.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 269314
     http_req_receiving.............: avg=297.26µs min=26.35µs  med=50.46µs max=152.91ms p(90)=223.94µs p(95)=380.22µs p(99.9)=40.15ms 
     http_req_sending...............: avg=122.9µs  min=4.2µs    med=8.68µs  max=173.74ms p(90)=18.5µs   p(95)=124.84µs p(99.9)=21.92ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.52ms  min=931.95µs med=43.67ms max=326.43ms p(90)=109.32ms p(95)=134.2ms  p(99.9)=181.91ms
     http_reqs......................: 269314  4401.016636/s
     iteration_duration.............: avg=53.09ms  min=1.6ms    med=44.58ms max=355.55ms p(90)=112.51ms p(95)=137.9ms  p(99.9)=208.4ms 
     iterations.....................: 268314  4384.675054/s
     success_rate...................: 100.00% ✓ 268314      ✗ 0     
     vus............................: 66      min=0         max=496 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 767862     ✗ 0     
     data_received..................: 23 GB   369 MB/s
     data_sent......................: 309 MB  5.1 MB/s
     http_req_blocked...............: avg=47.74µs  min=792ns    med=2.21µs  max=111.16ms p(90)=3.94µs   p(95)=5.14µs   p(99.9)=12.93ms 
     http_req_connecting............: avg=44.19µs  min=0s       med=0s      max=110.95ms p(90)=0s       p(95)=0s       p(99.9)=12.55ms 
     http_req_duration..............: avg=54.25ms  min=710.16µs med=45.79ms max=326.13ms p(90)=114.37ms p(95)=141.25ms p(99.9)=206.9ms 
       { expected_response:true }...: avg=54.25ms  min=710.16µs med=45.79ms max=326.13ms p(90)=114.37ms p(95)=141.25ms p(99.9)=206.9ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 256954
     http_req_receiving.............: avg=257.49µs min=25.56µs  med=51.25µs max=165.71ms p(90)=212.63µs p(95)=377.26µs p(99.9)=36.11ms 
     http_req_sending...............: avg=124.31µs min=4.06µs   med=9.17µs  max=86ms     p(90)=19.52µs  p(95)=129.53µs p(99.9)=21.79ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.87ms  min=647.84µs med=45.5ms  max=299.75ms p(90)=113.6ms  p(95)=140.38ms p(99.9)=203.79ms
     http_reqs......................: 256954  4216.22964/s
     iteration_duration.............: avg=55.66ms  min=1.3ms    med=46.81ms max=336.39ms p(90)=117.36ms p(95)=144.97ms p(99.9)=221.84ms
     iterations.....................: 255954  4199.82114/s
     success_rate...................: 100.00% ✓ 255954     ✗ 0     
     vus............................: 55      min=0        max=499 
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 479025      ✗ 0     
     data_received..................: 14 GB   229 MB/s
     data_sent......................: 193 MB  3.1 MB/s
     http_req_blocked...............: avg=11.19µs  min=842ns   med=2.29µs  max=42.22ms  p(90)=3.88µs   p(95)=5.12µs   p(99.9)=650.45µs
     http_req_connecting............: avg=8.15µs   min=0s      med=0s      max=42.11ms  p(90)=0s       p(95)=0s       p(99.9)=592.8µs 
     http_req_duration..............: avg=88.49ms  min=1.2ms   med=83.62ms max=338.8ms  p(90)=173ms    p(95)=186.65ms p(99.9)=225.51ms
       { expected_response:true }...: avg=88.49ms  min=1.2ms   med=83.62ms max=338.8ms  p(90)=173ms    p(95)=186.65ms p(99.9)=225.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 160675
     http_req_receiving.............: avg=115.14µs min=28.32µs med=56.2µs  max=29.1ms   p(90)=150.32µs p(95)=344.47µs p(99.9)=8.17ms  
     http_req_sending...............: avg=62.25µs  min=4.48µs  med=10.13µs max=157.38ms p(90)=19.69µs  p(95)=121.93µs p(99.9)=7.6ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=88.31ms  min=1.16ms  med=83.46ms max=338.3ms  p(90)=172.78ms p(95)=186.44ms p(99.9)=225.13ms
     http_reqs......................: 160675  2613.795844/s
     iteration_duration.............: avg=89.28ms  min=3.04ms  med=84.6ms  max=349.59ms p(90)=173.45ms p(95)=187.03ms p(99.9)=226.12ms
     iterations.....................: 159675  2597.528249/s
     success_rate...................: 100.00% ✓ 159675      ✗ 0     
     vus............................: 79      min=0         max=493 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 252579      ✗ 0    
     data_received..................: 7.4 GB  119 MB/s
     data_sent......................: 102 MB  1.6 MB/s
     http_req_blocked...............: avg=12.28µs  min=1.15µs  med=3.03µs   max=29.37ms  p(90)=4.78µs   p(95)=5.73µs   p(99.9)=484.92µs
     http_req_connecting............: avg=8.54µs   min=0s      med=0s       max=29.34ms  p(90)=0s       p(95)=0s       p(99.9)=411.55µs
     http_req_duration..............: avg=167.43ms min=2ms     med=138.89ms max=715.89ms p(90)=350.07ms p(95)=401.68ms p(99.9)=589.37ms
       { expected_response:true }...: avg=167.43ms min=2ms     med=138.89ms max=715.89ms p(90)=350.07ms p(95)=401.68ms p(99.9)=589.37ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 85193
     http_req_receiving.............: avg=76.31µs  min=28.92µs med=60.56µs  max=22.09ms  p(90)=97.39µs  p(95)=113.04µs p(99.9)=1.78ms  
     http_req_sending...............: avg=68.74µs  min=4.79µs  med=12.39µs  max=156.63ms p(90)=18.6µs   p(95)=22.38µs  p(99.9)=5.06ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=167.29ms min=1.93ms  med=138.65ms max=715.83ms p(90)=349.96ms p(95)=401.54ms p(99.9)=589.29ms
     http_reqs......................: 85193   1365.7463/s
     iteration_duration.............: avg=169.67ms min=6.89ms  med=141.74ms max=716.11ms p(90)=351.33ms p(95)=402.66ms p(99.9)=589.71ms
     iterations.....................: 84193   1349.715097/s
     success_rate...................: 100.00% ✓ 84193       ✗ 0    
     vus............................: 75      min=0         max=494
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 239808      ✗ 0    
     data_received..................: 7.1 GB  113 MB/s
     data_sent......................: 97 MB   1.6 MB/s
     http_req_blocked...............: avg=5.75µs   min=1.08µs  med=2.72µs   max=16.03ms  p(90)=4.38µs   p(95)=5.35µs   p(99.9)=357.74µs
     http_req_connecting............: avg=2.42µs   min=0s      med=0s       max=15.97ms  p(90)=0s       p(95)=0s       p(99.9)=319.62µs
     http_req_duration..............: avg=176.25ms min=2.01ms  med=174.83ms max=497.31ms p(90)=334.24ms p(95)=357.69ms p(99.9)=433.57ms
       { expected_response:true }...: avg=176.25ms min=2.01ms  med=174.83ms max=497.31ms p(90)=334.24ms p(95)=357.69ms p(99.9)=433.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 80936
     http_req_receiving.............: avg=76.78µs  min=27.98µs med=62.86µs  max=32.95ms  p(90)=100.72µs p(95)=117.1µs  p(99.9)=1.08ms  
     http_req_sending...............: avg=28.69µs  min=5µs     med=11.54µs  max=182.93ms p(90)=17.86µs  p(95)=21.42µs  p(99.9)=3.07ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=176.14ms min=1.96ms  med=174.73ms max=497.22ms p(90)=334.15ms p(95)=357.6ms  p(99.9)=433.5ms 
     http_reqs......................: 80936   1295.548944/s
     iteration_duration.............: avg=178.69ms min=5.17ms  med=177.65ms max=497.53ms p(90)=334.99ms p(95)=358.26ms p(99.9)=433.79ms
     iterations.....................: 79936   1279.541865/s
     success_rate...................: 100.00% ✓ 79936       ✗ 0    
     vus............................: 78      min=0         max=493
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 92367      ✗ 0    
     data_received..................: 2.8 GB  43 MB/s
     data_sent......................: 38 MB   590 kB/s
     http_req_blocked...............: avg=8.58µs   min=1.01µs  med=2.72µs   max=12.02ms p(90)=4.35µs   p(95)=5.31µs   p(99.9)=1.3ms   
     http_req_connecting............: avg=4.86µs   min=0s      med=0s       max=11.97ms p(90)=0s       p(95)=0s       p(99.9)=1.28ms  
     http_req_duration..............: avg=451.93ms min=3.82ms  med=418.73ms max=1.85s   p(90)=894.71ms p(95)=980.45ms p(99.9)=1.52s   
       { expected_response:true }...: avg=451.93ms min=3.82ms  med=418.73ms max=1.85s   p(90)=894.71ms p(95)=980.45ms p(99.9)=1.52s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 31789
     http_req_receiving.............: avg=79.05µs  min=27.36µs med=69.95µs  max=7.54ms  p(90)=107.71µs p(95)=122.63µs p(99.9)=892.08µs
     http_req_sending...............: avg=28.67µs  min=5.11µs  med=13.49µs  max=62.02ms p(90)=19.99µs  p(95)=22.69µs  p(99.9)=2.53ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=451.83ms min=3.72ms  med=418.63ms max=1.85s   p(90)=894.64ms p(95)=980.37ms p(99.9)=1.52s   
     http_reqs......................: 31789   491.682066/s
     iteration_duration.............: avg=466.83ms min=22.52ms med=438.56ms max=1.86s   p(90)=899.08ms p(95)=984.24ms p(99.9)=1.52s   
     iterations.....................: 30789   476.215016/s
     success_rate...................: 100.00% ✓ 30789      ✗ 0    
     vus............................: 87      min=0        max=500
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 46851      ✗ 0    
     data_received..................: 1.5 GB  21 MB/s
     data_sent......................: 20 MB   291 kB/s
     http_req_blocked...............: avg=13.89µs  min=1.17µs  med=3.11µs   max=3.83ms  p(90)=4.92µs   p(95)=6.44µs   p(99.9)=2.22ms  
     http_req_connecting............: avg=9.14µs   min=0s      med=0s       max=3.79ms  p(90)=0s       p(95)=0s       p(99.9)=2.19ms  
     http_req_duration..............: avg=873.36ms min=7.64ms  med=801.47ms max=3.08s   p(90)=1.79s    p(95)=1.9s     p(99.9)=2.64s   
       { expected_response:true }...: avg=873.36ms min=7.64ms  med=801.47ms max=3.08s   p(90)=1.79s    p(95)=1.9s     p(99.9)=2.64s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16617
     http_req_receiving.............: avg=95.28µs  min=31.28µs med=88.38µs  max=18.22ms p(90)=126.02µs p(95)=141.48µs p(99.9)=865.07µs
     http_req_sending...............: avg=38.78µs  min=5.36µs  med=16.64µs  max=79.26ms p(90)=22.03µs  p(95)=25.68µs  p(99.9)=4.26ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=873.22ms min=7.53ms  med=801.33ms max=3.08s   p(90)=1.79s    p(95)=1.9s     p(99.9)=2.64s   
     http_reqs......................: 16617   242.467902/s
     iteration_duration.............: avg=929.23ms min=37.47ms med=856.46ms max=3.08s   p(90)=1.8s     p(95)=1.9s     p(99.9)=2.64s   
     iterations.....................: 15617   227.876345/s
     success_rate...................: 100.00% ✓ 15617      ✗ 0    
     vus............................: 84      min=0        max=500
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 45561      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 19 MB   289 kB/s
     http_req_blocked...............: avg=14.59µs  min=1.07µs  med=3.16µs   max=7.51ms p(90)=4.85µs   p(95)=6.35µs   p(99.9)=2.26ms
     http_req_connecting............: avg=9.6µs    min=0s      med=0s       max=7.15ms p(90)=0s       p(95)=0s       p(99.9)=2.16ms
     http_req_duration..............: avg=900.52ms min=5.57ms  med=831.58ms max=4.95s  p(90)=1.79s    p(95)=2.05s    p(99.9)=4.07s 
       { expected_response:true }...: avg=900.52ms min=5.57ms  med=831.58ms max=4.95s  p(90)=1.79s    p(95)=2.05s    p(99.9)=4.07s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16187
     http_req_receiving.............: avg=91.89µs  min=31.39µs med=85.97µs  max=8.99ms p(90)=123.61µs p(95)=139.22µs p(99.9)=1.04ms
     http_req_sending...............: avg=35.08µs  min=4.76µs  med=16.06µs  max=73.4ms p(90)=21.06µs  p(95)=24.26µs  p(99.9)=4.51ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s     p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=900.39ms min=5.48ms  med=831.46ms max=4.95s  p(90)=1.79s    p(95)=2.05s    p(99.9)=4.07s 
     http_reqs......................: 16187   240.481366/s
     iteration_duration.............: avg=959.84ms min=43.46ms med=890.92ms max=4.95s  p(90)=1.81s    p(95)=2.07s    p(99.9)=4.12s 
     iterations.....................: 15187   225.624915/s
     success_rate...................: 100.00% ✓ 15187      ✗ 0    
     vus............................: 71      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

