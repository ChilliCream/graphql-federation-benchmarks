## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.2 | 4,742 | 4,747 | 4,731 | 0.1% | 431 MB | 93.0 KB |  |
| fusion-fed-net-11 | 16.7.2 | 4,591 | 4,614 | 4,577 | 0.3% | 402 MB | 89.6 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.7 | 4,565 | 4,580 | 4,536 | 0.4% | 438 MB | 98.2 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.7 | 4,549 | 4,555 | 4,532 | 0.2% | 157 MB | 35.3 KB |  |
| fusion-fed-aot-11 | 16.7.2 | 4,430 | 4,437 | 4,370 | 0.6% | 164 MB | 37.9 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.7 | 4,422 | 4,530 | 4,403 | 1.2% | 413 MB | 95.5 KB |  |
| fusion-aot-11 | 16.7.2 | 4,419 | 4,424 | 4,407 | 0.2% | 182 MB | 42.1 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.7 | 4,338 | 4,353 | 4,325 | 0.3% | 182 MB | 42.9 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,191 | 4,243 | 4,113 | 1.3% | 2,288 MB | 559.0 KB |  |
| hive-router | v0.3.6 | 2,645 | 2,681 | 2,634 | 0.7% | 166 MB | 64.2 KB |  |
| caliban | 3.2.0 | 1,451 | 1,455 | 1,435 | 0.6% | 11,072 MB | 7,813.9 KB |  |
| cosmo | 0.363.0 | 1,355 | 1,358 | 1,355 | 0.1% | 551 MB | 416.4 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 484 | 486 | 480 | 0.5% | 3,170 MB | 6,707.1 KB |  |
| hive-gateway | 2.15.3 | 246 | 247 | 244 | 0.4% | 3,815 MB | 15,879.6 KB |  |
| apollo-gateway | 2.14.4 | 241 | 242 | 241 | 0.2% | 2,473 MB | 10,508.3 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (8392 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (4040 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (176043 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 863991      ✗ 0     
     data_received..................: 25 GB   415 MB/s
     data_sent......................: 347 MB  5.7 MB/s
     http_req_blocked...............: avg=61.2µs   min=782ns    med=2.05µs  max=129.92ms p(90)=3.65µs   p(95)=4.78µs   p(99.9)=21.97ms 
     http_req_connecting............: avg=57.73µs  min=0s       med=0s      max=123.44ms p(90)=0s       p(95)=0s       p(99.9)=21.26ms 
     http_req_duration..............: avg=47.57ms  min=758.07µs med=40.49ms max=298.68ms p(90)=99.29ms  p(95)=123.05ms p(99.9)=177.9ms 
       { expected_response:true }...: avg=47.57ms  min=758.07µs med=40.49ms max=298.68ms p(90)=99.29ms  p(95)=123.05ms p(99.9)=177.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 288997
     http_req_receiving.............: avg=354.71µs min=25.73µs  med=51.18µs max=122.6ms  p(90)=209.96µs p(95)=362.59µs p(99.9)=48.2ms  
     http_req_sending...............: avg=142.76µs min=4µs      med=8.52µs  max=81.28ms  p(90)=16.51µs  p(95)=114.11µs p(99.9)=26.24ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.07ms  min=719.67µs med=40.18ms max=298.08ms p(90)=98.14ms  p(95)=121.79ms p(99.9)=172.91ms
     http_reqs......................: 288997  4742.157553/s
     iteration_duration.............: avg=49.46ms  min=1.3ms    med=41.27ms max=333.6ms  p(90)=104.12ms p(95)=129.03ms p(99.9)=199.65ms
     iterations.....................: 287997  4725.748533/s
     success_rate...................: 100.00% ✓ 287997      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 838767      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 337 MB  5.5 MB/s
     http_req_blocked...............: avg=62.24µs  min=822ns    med=2.1µs   max=157.08ms p(90)=3.77µs   p(95)=4.92µs   p(99.9)=22.96ms 
     http_req_connecting............: avg=58.83µs  min=0s       med=0s      max=133.39ms p(90)=0s       p(95)=0s       p(99.9)=22.3ms  
     http_req_duration..............: avg=49.56ms  min=889.66µs med=41.86ms max=316.66ms p(90)=104.17ms p(95)=129.34ms p(99.9)=183.97ms
       { expected_response:true }...: avg=49.56ms  min=889.66µs med=41.86ms max=316.66ms p(90)=104.17ms p(95)=129.34ms p(99.9)=183.97ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280589
     http_req_receiving.............: avg=361.32µs min=22.67µs  med=53.27µs max=117.43ms p(90)=212.08µs p(95)=372.76µs p(99.9)=51.53ms 
     http_req_sending...............: avg=152.64µs min=4.23µs   med=8.9µs   max=254.55ms p(90)=18.08µs  p(95)=119.79µs p(99.9)=27.58ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.04ms  min=856.15µs med=41.56ms max=316.49ms p(90)=102.92ms p(95)=127.92ms p(99.9)=176.21ms
     http_reqs......................: 280589  4591.325636/s
     iteration_duration.............: avg=50.95ms  min=1.41ms   med=42.58ms max=341.87ms p(90)=107.02ms p(95)=133.6ms  p(99.9)=200.98ms
     iterations.....................: 279589  4574.962466/s
     success_rate...................: 100.00% ✓ 279589      ✗ 0     
     vus............................: 62      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 831765      ✗ 0     
     data_received..................: 24 GB   400 MB/s
     data_sent......................: 334 MB  5.5 MB/s
     http_req_blocked...............: avg=69.76µs  min=912ns    med=2.53µs  max=152.48ms p(90)=4.09µs   p(95)=5.26µs   p(99.9)=25.61ms 
     http_req_connecting............: avg=65.71µs  min=0s       med=0s      max=152.4ms  p(90)=0s       p(95)=0s       p(99.9)=25.07ms 
     http_req_duration..............: avg=49.61ms  min=757.4µs  med=41.55ms max=275.21ms p(90)=105.06ms p(95)=130.25ms p(99.9)=186.74ms
       { expected_response:true }...: avg=49.61ms  min=757.4µs  med=41.55ms max=275.21ms p(90)=105.06ms p(95)=130.25ms p(99.9)=186.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 278255
     http_req_receiving.............: avg=343.76µs min=25.26µs  med=53.88µs max=142.04ms p(90)=222.12µs p(95)=384.66µs p(99.9)=47.56ms 
     http_req_sending...............: avg=159.04µs min=4.06µs   med=9.06µs  max=172.93ms p(90)=17.61µs  p(95)=124.55µs p(99.9)=29.75ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.1ms   min=711.11µs med=41.2ms  max=270.12ms p(90)=103.83ms p(95)=128.99ms p(99.9)=182.17ms
     http_reqs......................: 278255  4565.755741/s
     iteration_duration.............: avg=51.38ms  min=1.27ms   med=42.41ms max=318.92ms p(90)=109.11ms p(95)=136.89ms p(99.9)=211.8ms 
     iterations.....................: 277255  4549.347211/s
     success_rate...................: 100.00% ✓ 277255      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 829926      ✗ 0     
     data_received..................: 24 GB   398 MB/s
     data_sent......................: 334 MB  5.5 MB/s
     http_req_blocked...............: avg=53.86µs  min=832ns    med=2.07µs  max=109.53ms p(90)=3.73µs   p(95)=4.92µs   p(99.9)=20.29ms 
     http_req_connecting............: avg=49.98µs  min=0s       med=0s      max=109.45ms p(90)=0s       p(95)=0s       p(99.9)=19.5ms  
     http_req_duration..............: avg=49.97ms  min=833.53µs med=41.83ms max=268.54ms p(90)=107.02ms p(95)=131.98ms p(99.9)=182.24ms
       { expected_response:true }...: avg=49.97ms  min=833.53µs med=41.83ms max=268.54ms p(90)=107.02ms p(95)=131.98ms p(99.9)=182.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 277642
     http_req_receiving.............: avg=283.44µs min=25.34µs  med=49.92µs max=87.36ms  p(90)=216.51µs p(95)=381.09µs p(99.9)=37.44ms 
     http_req_sending...............: avg=133.55µs min=4.08µs   med=8.54µs  max=225.09ms p(90)=17.54µs  p(95)=124.3µs  p(99.9)=24.22ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.55ms  min=788.72µs med=41.55ms max=268.17ms p(90)=106.1ms  p(95)=130.92ms p(99.9)=177.97ms
     http_reqs......................: 277642  4549.971189/s
     iteration_duration.............: avg=51.49ms  min=1.36ms   med=42.71ms max=374.15ms p(90)=109.83ms p(95)=135.82ms p(99.9)=205.25ms
     iterations.....................: 276642  4533.583282/s
     success_rate...................: 100.00% ✓ 276642      ✗ 0     
     vus............................: 58      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 810744      ✗ 0     
     data_received..................: 24 GB   388 MB/s
     data_sent......................: 326 MB  5.3 MB/s
     http_req_blocked...............: avg=49.6µs   min=801ns    med=2.08µs  max=106.18ms p(90)=3.85µs   p(95)=5.12µs   p(99.9)=15.62ms 
     http_req_connecting............: avg=46.26µs  min=0s       med=0s      max=105.97ms p(90)=0s       p(95)=0s       p(99.9)=14.97ms 
     http_req_duration..............: avg=51.57ms  min=988.95µs med=43.7ms  max=266.6ms  p(90)=110.1ms  p(95)=135.8ms  p(99.9)=187.87ms
       { expected_response:true }...: avg=51.57ms  min=988.95µs med=43.7ms  max=266.6ms  p(90)=110.1ms  p(95)=135.8ms  p(99.9)=187.87ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 271248
     http_req_receiving.............: avg=270.93µs min=26.03µs  med=49.67µs max=94.95ms  p(90)=217.58µs p(95)=381.22µs p(99.9)=36.89ms 
     http_req_sending...............: avg=121.11µs min=4.39µs   med=8.6µs   max=145.34ms p(90)=19.41µs  p(95)=125.84µs p(99.9)=20.73ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.18ms  min=948.01µs med=43.46ms max=266.24ms p(90)=109.21ms p(95)=134.7ms  p(99.9)=183.8ms 
     http_reqs......................: 271248  4430.550751/s
     iteration_duration.............: avg=52.71ms  min=1.48ms   med=44.34ms max=307.82ms p(90)=112.58ms p(95)=138.55ms p(99.9)=204.8ms 
     iterations.....................: 270248  4414.216803/s
     success_rate...................: 100.00% ✓ 270248      ✗ 0     
     vus............................: 66      min=0         max=496 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 807534      ✗ 0     
     data_received..................: 24 GB   387 MB/s
     data_sent......................: 325 MB  5.3 MB/s
     http_req_blocked...............: avg=68.79µs  min=851ns    med=2.67µs  max=136.56ms p(90)=4.31µs   p(95)=5.49µs   p(99.9)=25.78ms 
     http_req_connecting............: avg=64.66µs  min=0s       med=0s      max=136.51ms p(90)=0s       p(95)=0s       p(99.9)=25.33ms 
     http_req_duration..............: avg=51.27ms  min=912.71µs med=43.24ms max=346.9ms  p(90)=108.36ms p(95)=135.67ms p(99.9)=189.41ms
       { expected_response:true }...: avg=51.27ms  min=912.71µs med=43.24ms max=346.9ms  p(90)=108.36ms p(95)=135.67ms p(99.9)=189.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 270178
     http_req_receiving.............: avg=323.39µs min=22.53µs  med=54.84µs max=108.12ms p(90)=225.49µs p(95)=396.93µs p(99.9)=42.42ms 
     http_req_sending...............: avg=149.34µs min=4.06µs   med=9.29µs  max=102.62ms p(90)=18.44µs  p(95)=127.62µs p(99.9)=25.69ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.8ms   min=847.89µs med=42.9ms  max=338.88ms p(90)=107.25ms p(95)=134.59ms p(99.9)=185.39ms
     http_reqs......................: 270178  4422.057045/s
     iteration_duration.............: avg=52.92ms  min=1.46ms   med=43.88ms max=358.16ms p(90)=112.53ms p(95)=140.96ms p(99.9)=216.88ms
     iterations.....................: 269178  4405.689846/s
     success_rate...................: 100.00% ✓ 269178      ✗ 0     
     vus............................: 62      min=0         max=497 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 806151      ✗ 0     
     data_received..................: 24 GB   387 MB/s
     data_sent......................: 324 MB  5.3 MB/s
     http_req_blocked...............: avg=54.95µs  min=941ns    med=2.57µs  max=171.28ms p(90)=4.18µs   p(95)=5.34µs   p(99.9)=18.97ms 
     http_req_connecting............: avg=50.65µs  min=0s       med=0s      max=106.74ms p(90)=0s       p(95)=0s       p(99.9)=18.57ms 
     http_req_duration..............: avg=51.45ms  min=845.15µs med=42.4ms  max=313.41ms p(90)=111.48ms p(95)=138.3ms  p(99.9)=194.69ms
       { expected_response:true }...: avg=51.45ms  min=845.15µs med=42.4ms  max=313.41ms p(90)=111.48ms p(95)=138.3ms  p(99.9)=194.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 269717
     http_req_receiving.............: avg=336.44µs min=22.8µs   med=51.38µs max=89.24ms  p(90)=231.58µs p(95)=403.07µs p(99.9)=54.08ms 
     http_req_sending...............: avg=132.36µs min=4.07µs   med=9.08µs  max=212.79ms p(90)=17.92µs  p(95)=129.22µs p(99.9)=24.19ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.99ms  min=787.84µs med=42.09ms max=312.88ms p(90)=110.39ms p(95)=137.17ms p(99.9)=191.56ms
     http_reqs......................: 269717  4419.01406/s
     iteration_duration.............: avg=53.01ms  min=1.41ms   med=43.36ms max=331.64ms p(90)=114.65ms p(95)=142.5ms  p(99.9)=222.08ms
     iterations.....................: 268717  4402.630168/s
     success_rate...................: 100.00% ✓ 268717      ✗ 0     
     vus............................: 58      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 793554      ✗ 0     
     data_received..................: 23 GB   380 MB/s
     data_sent......................: 319 MB  5.2 MB/s
     http_req_blocked...............: avg=56.18µs  min=831ns    med=2.52µs  max=117.72ms p(90)=4.29µs   p(95)=5.56µs   p(99.9)=19.88ms 
     http_req_connecting............: avg=52.45µs  min=0s       med=0s      max=117.44ms p(90)=0s       p(95)=0s       p(99.9)=19.42ms 
     http_req_duration..............: avg=52.43ms  min=984.95µs med=43.62ms max=300.37ms p(90)=113.25ms p(95)=140.81ms p(99.9)=195.19ms
       { expected_response:true }...: avg=52.43ms  min=984.95µs med=43.62ms max=300.37ms p(90)=113.25ms p(95)=140.81ms p(99.9)=195.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 265518
     http_req_receiving.............: avg=362.77µs min=26.01µs  med=51.66µs max=160.65ms p(90)=236.61µs p(95)=414.2µs  p(99.9)=52.47ms 
     http_req_sending...............: avg=134.6µs  min=4.32µs   med=8.98µs  max=177.38ms p(90)=19.53µs  p(95)=134.47µs p(99.9)=23.77ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.93ms  min=936.97µs med=43.31ms max=300.21ms p(90)=112.1ms  p(95)=139.74ms p(99.9)=187.47ms
     http_reqs......................: 265518  4338.899222/s
     iteration_duration.............: avg=53.85ms  min=1.61ms   med=44.35ms max=357.99ms p(90)=116.06ms p(95)=144.49ms p(99.9)=224.69ms
     iterations.....................: 264518  4322.55796/s
     success_rate...................: 100.00% ✓ 264518      ✗ 0     
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

     checks.........................: 100.00% ✓ 763251      ✗ 0     
     data_received..................: 22 GB   366 MB/s
     data_sent......................: 307 MB  5.0 MB/s
     http_req_blocked...............: avg=51.83µs  min=792ns    med=2.51µs  max=120.96ms p(90)=4.4µs    p(95)=5.66µs   p(99.9)=14.08ms 
     http_req_connecting............: avg=48.6µs   min=0s       med=0s      max=120.67ms p(90)=0s       p(95)=0s       p(99.9)=13.96ms 
     http_req_duration..............: avg=54.7ms   min=686.69µs med=45.96ms max=297.12ms p(90)=117.62ms p(95)=148.48ms p(99.9)=216.77ms
       { expected_response:true }...: avg=54.7ms   min=686.69µs med=45.96ms max=297.12ms p(90)=117.62ms p(95)=148.48ms p(99.9)=216.77ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 255417
     http_req_receiving.............: avg=279.2µs  min=20.89µs  med=52.47µs max=89.32ms  p(90)=221.36µs p(95)=394.35µs p(99.9)=40.04ms 
     http_req_sending...............: avg=130.05µs min=4.18µs   med=9.52µs  max=85.61ms  p(90)=20.3µs   p(95)=134.63µs p(99.9)=23.19ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=54.29ms  min=648.69µs med=45.7ms  max=285.65ms p(90)=116.67ms p(95)=147.38ms p(99.9)=214.17ms
     http_reqs......................: 255417  4191.258409/s
     iteration_duration.............: avg=56ms     min=1.28ms   med=46.67ms max=306.13ms p(90)=120.32ms p(95)=152.12ms p(99.9)=231.83ms
     iterations.....................: 254417  4174.848936/s
     success_rate...................: 100.00% ✓ 254417      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 485937      ✗ 0     
     data_received..................: 14 GB   231 MB/s
     data_sent......................: 196 MB  3.2 MB/s
     http_req_blocked...............: avg=14.23µs  min=852ns   med=2.45µs  max=47.22ms  p(90)=4.19µs   p(95)=5.39µs   p(99.9)=877.29µs
     http_req_connecting............: avg=11.06µs  min=0s      med=0s      max=46.99ms  p(90)=0s       p(95)=0s       p(99.9)=757.09µs
     http_req_duration..............: avg=87.22ms  min=1.33ms  med=83.79ms max=327.63ms p(90)=168.2ms  p(95)=183.62ms p(99.9)=233.57ms
       { expected_response:true }...: avg=87.22ms  min=1.33ms  med=83.79ms max=327.63ms p(90)=168.2ms  p(95)=183.62ms p(99.9)=233.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 162979
     http_req_receiving.............: avg=126.23µs min=26.06µs med=55.31µs max=212.49ms p(90)=174.74µs p(95)=357.32µs p(99.9)=10.21ms 
     http_req_sending...............: avg=64.82µs  min=4.58µs  med=10.26µs max=39.03ms  p(90)=20.45µs  p(95)=125.61µs p(99.9)=8.3ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=87.03ms  min=1.28ms  med=83.61ms max=314.69ms p(90)=167.95ms p(95)=183.33ms p(99.9)=233.06ms
     http_reqs......................: 162979  2645.490828/s
     iteration_duration.............: avg=88.01ms  min=2.95ms  med=84.75ms max=346.79ms p(90)=168.67ms p(95)=184.09ms p(99.9)=234.85ms
     iterations.....................: 161979  2629.258732/s
     success_rate...................: 100.00% ✓ 161979      ✗ 0     
     vus............................: 84      min=0         max=495 
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

     checks.........................: 100.00% ✓ 268917      ✗ 0    
     data_received..................: 7.9 GB  127 MB/s
     data_sent......................: 109 MB  1.7 MB/s
     http_req_blocked...............: avg=7.38µs   min=1.16µs  med=3.48µs   max=26.81ms  p(90)=5.55µs   p(95)=6.7µs    p(99.9)=386.56µs
     http_req_connecting............: avg=3.16µs   min=0s      med=0s       max=26.76ms  p(90)=0s       p(95)=0s       p(99.9)=277.26µs
     http_req_duration..............: avg=157.32ms min=2.06ms  med=130.77ms max=1.02s    p(90)=324.24ms p(95)=390.52ms p(99.9)=716.53ms
       { expected_response:true }...: avg=157.32ms min=2.06ms  med=130.77ms max=1.02s    p(90)=324.24ms p(95)=390.52ms p(99.9)=716.53ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 90639
     http_req_receiving.............: avg=90.72µs  min=28.35µs med=66.53µs  max=133.88ms p(90)=110.04µs p(95)=135.75µs p(99.9)=2.35ms  
     http_req_sending...............: avg=46.57µs  min=5.17µs  med=14.36µs  max=231.75ms p(90)=22.35µs  p(95)=27.65µs  p(99.9)=5.51ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=157.18ms min=2.01ms  med=130.63ms max=1.02s    p(90)=324.12ms p(95)=390.39ms p(99.9)=716.44ms
     http_reqs......................: 90639   1451.11776/s
     iteration_duration.............: avg=159.34ms min=8.49ms  med=132.92ms max=1.02s    p(90)=325.46ms p(95)=391.78ms p(99.9)=717.46ms
     iterations.....................: 89639   1435.107899/s
     success_rate...................: 100.00% ✓ 89639       ✗ 0    
     vus............................: 79      min=0         max=493
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 250788      ✗ 0    
     data_received..................: 7.4 GB  119 MB/s
     data_sent......................: 102 MB  1.6 MB/s
     http_req_blocked...............: avg=5.34µs   min=891ns  med=2.29µs   max=11.5ms   p(90)=3.96µs   p(95)=4.88µs   p(99.9)=435.43µs
     http_req_connecting............: avg=2.38µs   min=0s     med=0s       max=11.32ms  p(90)=0s       p(95)=0s       p(99.9)=351.87µs
     http_req_duration..............: avg=168.62ms min=1.98ms med=165.83ms max=465.68ms p(90)=320.95ms p(95)=345.09ms p(99.9)=414.84ms
       { expected_response:true }...: avg=168.62ms min=1.98ms med=165.83ms max=465.68ms p(90)=320.95ms p(95)=345.09ms p(99.9)=414.84ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 84596
     http_req_receiving.............: avg=74.41µs  min=26.7µs med=59.56µs  max=41.71ms  p(90)=96.57µs  p(95)=111.99µs p(99.9)=1.45ms  
     http_req_sending...............: avg=29.73µs  min=4.68µs med=10.36µs  max=135.39ms p(90)=17.24µs  p(95)=20.76µs  p(99.9)=3.17ms  
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=168.51ms min=1.92ms med=165.73ms max=465.61ms p(90)=320.88ms p(95)=345.02ms p(99.9)=414.78ms
     http_reqs......................: 84596   1355.404938/s
     iteration_duration.............: avg=170.86ms min=4.39ms med=168.38ms max=465.98ms p(90)=321.72ms p(95)=345.65ms p(99.9)=415.46ms
     iterations.....................: 83596   1339.382846/s
     success_rate...................: 100.00% ✓ 83596       ✗ 0    
     vus............................: 77      min=0         max=493
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 91164      ✗ 0    
     data_received..................: 2.7 GB  42 MB/s
     data_sent......................: 38 MB   582 kB/s
     http_req_blocked...............: avg=8.82µs   min=1.07µs  med=2.64µs   max=15.59ms  p(90)=4.25µs   p(95)=5.31µs   p(99.9)=1.41ms
     http_req_connecting............: avg=5.22µs   min=0s      med=0s       max=15.53ms  p(90)=0s       p(95)=0s       p(99.9)=1.38ms
     http_req_duration..............: avg=457.66ms min=3.87ms  med=421.66ms max=1.88s    p(90)=904.66ms p(95)=979.59ms p(99.9)=1.45s 
       { expected_response:true }...: avg=457.66ms min=3.87ms  med=421.66ms max=1.88s    p(90)=904.66ms p(95)=979.59ms p(99.9)=1.45s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 31388
     http_req_receiving.............: avg=85.63µs  min=28.91µs med=71.37µs  max=109.02ms p(90)=108.04µs p(95)=122.06µs p(99.9)=1.07ms
     http_req_sending...............: avg=27.79µs  min=4.95µs  med=13.19µs  max=77.51ms  p(90)=19.51µs  p(95)=21.91µs  p(99.9)=2.24ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=457.55ms min=3.81ms  med=421.57ms max=1.88s    p(90)=904.54ms p(95)=979.51ms p(99.9)=1.45s 
     http_reqs......................: 31388   484.534769/s
     iteration_duration.............: avg=472.94ms min=20.34ms med=441.15ms max=1.88s    p(90)=908.68ms p(95)=983.14ms p(99.9)=1.46s 
     iterations.....................: 30388   469.097826/s
     success_rate...................: 100.00% ✓ 30388      ✗ 0    
     vus............................: 94      min=0        max=500
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 47076      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 20 MB   296 kB/s
     http_req_blocked...............: avg=13.99µs  min=1.17µs  med=3.27µs   max=12.11ms p(90)=4.94µs   p(95)=6.44µs   p(99.9)=2.17ms  
     http_req_connecting............: avg=9.19µs   min=0s      med=0s       max=12.05ms p(90)=0s       p(95)=0s       p(99.9)=2.15ms  
     http_req_duration..............: avg=871.23ms min=5.9ms   med=783.37ms max=5.33s   p(90)=1.72s    p(95)=2.01s    p(99.9)=3.91s   
       { expected_response:true }...: avg=871.23ms min=5.9ms   med=783.37ms max=5.33s   p(90)=1.72s    p(95)=2.01s    p(99.9)=3.91s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16692
     http_req_receiving.............: avg=95.24µs  min=35.03µs med=89.4µs   max=9.36ms  p(90)=123.99µs p(95)=139.29µs p(99.9)=957.76µs
     http_req_sending...............: avg=27.12µs  min=5.4µs   med=16.57µs  max=26.58ms p(90)=21.46µs  p(95)=25.06µs  p(99.9)=2.37ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=871.1ms  min=5.81ms  med=783.27ms max=5.33s   p(90)=1.72s    p(95)=2.01s    p(99.9)=3.91s   
     http_reqs......................: 16692   246.625863/s
     iteration_duration.............: avg=926.73ms min=43.04ms med=856.19ms max=5.34s   p(90)=1.74s    p(95)=2.04s    p(99.9)=3.95s   
     iterations.....................: 15692   231.850769/s
     success_rate...................: 100.00% ✓ 15692      ✗ 0    
     vus............................: 90      min=0        max=500
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

     checks.........................: 100.00% ✓ 46638      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   290 kB/s
     http_req_blocked...............: avg=14.72µs  min=1.13µs  med=3.16µs   max=9.16ms  p(90)=4.87µs   p(95)=6.35µs  p(99.9)=2.16ms
     http_req_connecting............: avg=9.93µs   min=0s      med=0s       max=8.95ms  p(90)=0s       p(95)=0s      p(99.9)=2.1ms 
     http_req_duration..............: avg=877.67ms min=7.54ms  med=807.36ms max=2.94s   p(90)=1.79s    p(95)=1.89s   p(99.9)=2.63s 
       { expected_response:true }...: avg=877.67ms min=7.54ms  med=807.36ms max=2.94s   p(90)=1.79s    p(95)=1.89s   p(99.9)=2.63s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16546
     http_req_receiving.............: avg=92.02µs  min=29.6µs  med=86.17µs  max=4.92ms  p(90)=124.06µs p(95)=139.6µs p(99.9)=1.1ms 
     http_req_sending...............: avg=35.89µs  min=5.36µs  med=16.53µs  max=98.94ms p(90)=21.57µs  p(95)=25.26µs p(99.9)=2.25ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s      p(99.9)=0s    
     http_req_waiting...............: avg=877.54ms min=7.46ms  med=807.25ms max=2.94s   p(90)=1.79s    p(95)=1.89s   p(99.9)=2.63s 
     http_reqs......................: 16546   241.801738/s
     iteration_duration.............: avg=934.08ms min=26.85ms med=862.09ms max=2.95s   p(90)=1.8s     p(95)=1.91s   p(99.9)=2.65s 
     iterations.....................: 15546   227.187829/s
     success_rate...................: 100.00% ✓ 15546      ✗ 0    
     vus............................: 80      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

