## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 4,790 | 4,805 | 4,781 | 0.2% | 416 MB | 88.9 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 4,744 | 4,746 | 4,739 | 0.1% | 420 MB | 90.7 KB |  |
| fusion-aot-11 | 16.7.3 | 4,498 | 4,554 | 4,481 | 0.7% | 156 MB | 35.6 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,433 | 4,531 | 4,411 | 1.1% | 169 MB | 39.1 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,429 | 4,515 | 4,386 | 1.2% | 422 MB | 97.5 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,385 | 4,505 | 4,356 | 1.5% | 419 MB | 97.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,322 | 4,332 | 4,305 | 0.2% | 178 MB | 42.3 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,245 | 4,264 | 4,241 | 0.2% | 163 MB | 39.3 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,156 | 4,175 | 4,122 | 0.6% | 2,295 MB | 565.4 KB |  |
| hive-router | v0.3.6 | 2,738 | 2,742 | 2,725 | 0.3% | 169 MB | 63.3 KB |  |
| caliban | 3.2.0 | 1,465 | 1,467 | 1,464 | 0.1% | 10,736 MB | 7,504.6 KB |  |
| cosmo | 0.363.0 | 1,311 | 1,317 | 1,308 | 0.3% | 539 MB | 421.1 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 489 | 492 | 486 | 0.4% | 3,148 MB | 6,591.8 KB |  |
| hive-gateway | 2.15.3 | 252 | 254 | 248 | 0.9% | 3,843 MB | 15,615.7 KB |  |
| apollo-gateway | 2.14.4 | 240 | 241 | 239 | 0.3% | 2,452 MB | 10,460.9 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (13332 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (5985 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (159961 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 872856      ✗ 0     
     data_received..................: 26 GB   419 MB/s
     data_sent......................: 351 MB  5.8 MB/s
     http_req_blocked...............: avg=62.71µs  min=801ns    med=2.05µs  max=130.78ms p(90)=3.64µs   p(95)=4.76µs   p(99.9)=21.62ms 
     http_req_connecting............: avg=58.9µs   min=0s       med=0s      max=130.7ms  p(90)=0s       p(95)=0s       p(99.9)=20.62ms 
     http_req_duration..............: avg=46.99ms  min=740.85µs med=39.33ms max=310.94ms p(90)=98.47ms  p(95)=122.89ms p(99.9)=177.69ms
       { expected_response:true }...: avg=46.99ms  min=740.85µs med=39.33ms max=310.94ms p(90)=98.47ms  p(95)=122.89ms p(99.9)=177.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 291952
     http_req_receiving.............: avg=363.5µs  min=22.39µs  med=51.44µs max=130.15ms p(90)=203.22µs p(95)=354.76µs p(99.9)=53.8ms  
     http_req_sending...............: avg=142.46µs min=3.81µs   med=8.48µs  max=155.04ms p(90)=16.57µs  p(95)=113.45µs p(99.9)=25.58ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.49ms  min=703.04µs med=39.03ms max=310.78ms p(90)=97.25ms  p(95)=121.54ms p(99.9)=167.14ms
     http_reqs......................: 291952  4790.846637/s
     iteration_duration.............: avg=48.95ms  min=1.16ms   med=40.38ms max=320.59ms p(90)=103.07ms p(95)=128.47ms p(99.9)=198.91ms
     iterations.....................: 290952  4774.436931/s
     success_rate...................: 100.00% ✓ 290952      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 864426      ✗ 0     
     data_received..................: 25 GB   415 MB/s
     data_sent......................: 347 MB  5.7 MB/s
     http_req_blocked...............: avg=59.67µs  min=781ns    med=2µs     max=119.34ms p(90)=3.61µs   p(95)=4.7µs    p(99.9)=21.28ms 
     http_req_connecting............: avg=56.34µs  min=0s       med=0s      max=116.98ms p(90)=0s       p(95)=0s       p(99.9)=20.38ms 
     http_req_duration..............: avg=47.89ms  min=754.52µs med=40.43ms max=303.14ms p(90)=101.04ms p(95)=125.48ms p(99.9)=174.33ms
       { expected_response:true }...: avg=47.89ms  min=754.52µs med=40.43ms max=303.14ms p(90)=101.04ms p(95)=125.48ms p(99.9)=174.33ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 289142
     http_req_receiving.............: avg=318.11µs min=23.65µs  med=50.63µs max=189.66ms p(90)=209.79µs p(95)=364.38µs p(99.9)=40.96ms 
     http_req_sending...............: avg=141.99µs min=4.12µs   med=8.38µs  max=264.29ms p(90)=16.38µs  p(95)=116.13µs p(99.9)=25.85ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.43ms  min=718.82µs med=40.16ms max=289.21ms p(90)=99.86ms  p(95)=124.3ms  p(99.9)=171.23ms
     http_reqs......................: 289142  4744.432526/s
     iteration_duration.............: avg=49.43ms  min=1.18ms   med=41.15ms max=362.31ms p(90)=104.41ms p(95)=130.12ms p(99.9)=208.48ms
     iterations.....................: 288142  4728.023867/s
     success_rate...................: 100.00% ✓ 288142      ✗ 0     
     vus............................: 55      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 820626      ✗ 0     
     data_received..................: 24 GB   394 MB/s
     data_sent......................: 330 MB  5.4 MB/s
     http_req_blocked...............: avg=54.04µs  min=781ns    med=2.24µs  max=115.49ms p(90)=3.89µs   p(95)=5.02µs   p(99.9)=17.64ms 
     http_req_connecting............: avg=49.77µs  min=0s       med=0s      max=115.43ms p(90)=0s       p(95)=0s       p(99.9)=16.43ms 
     http_req_duration..............: avg=50.37ms  min=840.95µs med=41.88ms max=248.73ms p(90)=109.13ms p(95)=135.41ms p(99.9)=187.51ms
       { expected_response:true }...: avg=50.37ms  min=840.95µs med=41.88ms max=248.73ms p(90)=109.13ms p(95)=135.41ms p(99.9)=187.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 274542
     http_req_receiving.............: avg=278.16µs min=24.78µs  med=49.76µs max=135.49ms p(90)=213.08µs p(95)=381.62µs p(99.9)=37.87ms 
     http_req_sending...............: avg=130.91µs min=4.04µs   med=8.55µs  max=172.34ms p(90)=17.77µs  p(95)=126.7µs  p(99.9)=23.83ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.96ms  min=796.16µs med=41.6ms  max=248.68ms p(90)=108.25ms p(95)=134.38ms p(99.9)=183.96ms
     http_reqs......................: 274542  4498.60544/s
     iteration_duration.............: avg=52.07ms  min=1.41ms   med=42.62ms max=383.2ms  p(90)=112.85ms p(95)=139.54ms p(99.9)=219.04ms
     iterations.....................: 273542  4482.219585/s
     success_rate...................: 100.00% ✓ 273542      ✗ 0     
     vus............................: 59      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 808923      ✗ 0     
     data_received..................: 24 GB   388 MB/s
     data_sent......................: 325 MB  5.3 MB/s
     http_req_blocked...............: avg=58.97µs  min=952ns    med=2.52µs  max=126.04ms p(90)=4.21µs   p(95)=5.4µs    p(99.9)=19.56ms 
     http_req_connecting............: avg=55.3µs   min=0s       med=0s      max=125.95ms p(90)=0s       p(95)=0s       p(99.9)=19.19ms 
     http_req_duration..............: avg=51ms     min=839.28µs med=41.88ms max=305.64ms p(90)=109.96ms p(95)=137.89ms p(99.9)=193.4ms 
       { expected_response:true }...: avg=51ms     min=839.28µs med=41.88ms max=305.64ms p(90)=109.96ms p(95)=137.89ms p(99.9)=193.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 270641
     http_req_receiving.............: avg=310.31µs min=22.9µs   med=51µs    max=92.95ms  p(90)=227.79µs p(95)=400.63µs p(99.9)=46.04ms 
     http_req_sending...............: avg=141.42µs min=4.04µs   med=9.01µs  max=131.37ms p(90)=19.03µs  p(95)=132.03µs p(99.9)=24.77ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.55ms  min=795.72µs med=41.57ms max=305.34ms p(90)=109.01ms p(95)=136.8ms  p(99.9)=185.55ms
     http_reqs......................: 270641  4433.894111/s
     iteration_duration.............: avg=52.83ms  min=1.52ms   med=43.25ms max=370.04ms p(90)=113.88ms p(95)=142.75ms p(99.9)=214.87ms
     iterations.....................: 269641  4417.511175/s
     success_rate...................: 100.00% ✓ 269641      ✗ 0     
     vus............................: 58      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 809463      ✗ 0     
     data_received..................: 24 GB   388 MB/s
     data_sent......................: 325 MB  5.3 MB/s
     http_req_blocked...............: avg=64.46µs  min=811ns    med=2.57µs  max=167.23ms p(90)=4.28µs   p(95)=5.44µs   p(99.9)=23.32ms 
     http_req_connecting............: avg=59.62µs  min=0s       med=0s      max=142.95ms p(90)=0s       p(95)=0s       p(99.9)=22.23ms 
     http_req_duration..............: avg=51.21ms  min=908.72µs med=43.02ms max=279.25ms p(90)=110.42ms p(95)=135.62ms p(99.9)=187.36ms
       { expected_response:true }...: avg=51.21ms  min=908.72µs med=43.02ms max=279.25ms p(90)=110.42ms p(95)=135.62ms p(99.9)=187.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 270821
     http_req_receiving.............: avg=311.17µs min=25.37µs  med=53.51µs max=130.83ms p(90)=220.61µs p(95)=393.78µs p(99.9)=41.88ms 
     http_req_sending...............: avg=146.62µs min=4.11µs   med=9.3µs   max=201.03ms p(90)=18.37µs  p(95)=127.44µs p(99.9)=25.81ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.75ms  min=860.57µs med=42.73ms max=278.62ms p(90)=109.31ms p(95)=134.55ms p(99.9)=182.81ms
     http_reqs......................: 270821  4429.82284/s
     iteration_duration.............: avg=52.79ms  min=1.41ms   med=43.76ms max=309.64ms p(90)=113.85ms p(95)=140.6ms  p(99.9)=219.3ms 
     iterations.....................: 269821  4413.465826/s
     success_rate...................: 100.00% ✓ 269821      ✗ 0     
     vus............................: 63      min=0         max=496 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 801318      ✗ 0     
     data_received..................: 24 GB   384 MB/s
     data_sent......................: 322 MB  5.3 MB/s
     http_req_blocked...............: avg=65.8µs   min=802ns    med=2.67µs  max=153.22ms p(90)=4.36µs   p(95)=5.56µs   p(99.9)=23.76ms 
     http_req_connecting............: avg=62.12µs  min=0s       med=0s      max=121.65ms p(90)=0s       p(95)=0s       p(99.9)=23.07ms 
     http_req_duration..............: avg=51.18ms  min=908.11µs med=42.57ms max=268.23ms p(90)=109.39ms p(95)=136.35ms p(99.9)=191.02ms
       { expected_response:true }...: avg=51.18ms  min=908.11µs med=42.57ms max=268.23ms p(90)=109.39ms p(95)=136.35ms p(99.9)=191.02ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 268106
     http_req_receiving.............: avg=336.05µs min=26.55µs  med=54.45µs max=125.3ms  p(90)=227.11µs p(95)=399.39µs p(99.9)=42.94ms 
     http_req_sending...............: avg=156.98µs min=4.28µs   med=9.42µs  max=148.55ms p(90)=19.1µs   p(95)=127.99µs p(99.9)=26.97ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.69ms  min=868.97µs med=42.23ms max=265.07ms p(90)=108.22ms p(95)=135.23ms p(99.9)=186.93ms
     http_reqs......................: 268106  4385.19119/s
     iteration_duration.............: avg=53.33ms  min=1.39ms   med=43.74ms max=346.09ms p(90)=114.17ms p(95)=142.16ms p(99.9)=228.01ms
     iterations.....................: 267106  4368.835005/s
     success_rate...................: 100.00% ✓ 267106      ✗ 0     
     vus............................: 63      min=0         max=496 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 790503      ✗ 0     
     data_received..................: 23 GB   378 MB/s
     data_sent......................: 318 MB  5.2 MB/s
     http_req_blocked...............: avg=38.67µs  min=801ns    med=2µs     max=89.12ms  p(90)=3.57µs   p(95)=4.73µs   p(99.9)=10.18ms 
     http_req_connecting............: avg=35.37µs  min=0s       med=0s      max=88.94ms  p(90)=0s       p(95)=0s       p(99.9)=9.82ms  
     http_req_duration..............: avg=53.13ms  min=968.91µs med=44.95ms max=314.5ms  p(90)=111.38ms p(95)=137.53ms p(99.9)=191.65ms
       { expected_response:true }...: avg=53.13ms  min=968.91µs med=44.95ms max=314.5ms  p(90)=111.38ms p(95)=137.53ms p(99.9)=191.65ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 264501
     http_req_receiving.............: avg=271.83µs min=24.53µs  med=49.43µs max=80.86ms  p(90)=223.67µs p(95)=375.76µs p(99.9)=35.93ms 
     http_req_sending...............: avg=109.99µs min=4.21µs   med=8.44µs  max=264.57ms p(90)=17.87µs  p(95)=122.65µs p(99.9)=18.79ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=52.75ms  min=924.59µs med=44.68ms max=314.22ms p(90)=110.55ms p(95)=136.45ms p(99.9)=189.03ms
     http_reqs......................: 264501  4322.203597/s
     iteration_duration.............: avg=54.06ms  min=1.68ms   med=45.67ms max=335.31ms p(90)=113.22ms p(95)=139.37ms p(99.9)=202.53ms
     iterations.....................: 263501  4305.862624/s
     success_rate...................: 100.00% ✓ 263501      ✗ 0     
     vus............................: 66      min=0         max=496 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 776826      ✗ 0     
     data_received..................: 23 GB   372 MB/s
     data_sent......................: 312 MB  5.1 MB/s
     http_req_blocked...............: avg=53.15µs  min=911ns    med=2.65µs  max=138.7ms  p(90)=4.38µs   p(95)=5.56µs   p(99.9)=15.51ms 
     http_req_connecting............: avg=49.13µs  min=0s       med=0s      max=138.49ms p(90)=0s       p(95)=0s       p(99.9)=14.98ms 
     http_req_duration..............: avg=53.62ms  min=982.2µs  med=44.67ms max=255.73ms p(90)=116.16ms p(95)=143.57ms p(99.9)=196.4ms 
       { expected_response:true }...: avg=53.62ms  min=982.2µs  med=44.67ms max=255.73ms p(90)=116.16ms p(95)=143.57ms p(99.9)=196.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 259942
     http_req_receiving.............: avg=289.87µs min=26.11µs  med=52.6µs  max=80.66ms  p(90)=236.04µs p(95)=410.61µs p(99.9)=38.39ms 
     http_req_sending...............: avg=138.18µs min=4.4µs    med=9.4µs   max=236.25ms p(90)=19.44µs  p(95)=136.56µs p(99.9)=25.8ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.19ms  min=936.28µs med=44.37ms max=255.18ms p(90)=115.26ms p(95)=142.57ms p(99.9)=192.74ms
     http_reqs......................: 259942  4245.28008/s
     iteration_duration.............: avg=55.02ms  min=1.65ms   med=45.46ms max=322.89ms p(90)=118.86ms p(95)=146.8ms  p(99.9)=222.22ms
     iterations.....................: 258942  4228.948436/s
     success_rate...................: 100.00% ✓ 258942      ✗ 0     
     vus............................: 67      min=0         max=496 
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

     checks.........................: 100.00% ✓ 757188      ✗ 0     
     data_received..................: 22 GB   363 MB/s
     data_sent......................: 304 MB  5.0 MB/s
     http_req_blocked...............: avg=45.11µs  min=761ns    med=2.17µs  max=112.49ms p(90)=3.78µs   p(95)=4.87µs   p(99.9)=11.3ms  
     http_req_connecting............: avg=41.19µs  min=0s       med=0s      max=93.23ms  p(90)=0s       p(95)=0s       p(99.9)=9.34ms  
     http_req_duration..............: avg=55.24ms  min=729.29µs med=46.58ms max=299.52ms p(90)=116.14ms p(95)=144.84ms p(99.9)=218.66ms
       { expected_response:true }...: avg=55.24ms  min=729.29µs med=46.58ms max=299.52ms p(90)=116.14ms p(95)=144.84ms p(99.9)=218.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 253396
     http_req_receiving.............: avg=251.33µs min=25.4µs   med=50.88µs max=98.65ms  p(90)=210.53µs p(95)=372.19µs p(99.9)=35.88ms 
     http_req_sending...............: avg=119.13µs min=4.2µs    med=9.06µs  max=129.59ms p(90)=18.15µs  p(95)=125.64µs p(99.9)=21.55ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=54.87ms  min=673.74µs med=46.34ms max=299.13ms p(90)=115.32ms p(95)=143.92ms p(99.9)=215.95ms
     http_reqs......................: 253396  4156.248032/s
     iteration_duration.............: avg=56.45ms  min=1.44ms   med=47.36ms max=361.54ms p(90)=118.52ms p(95)=148.13ms p(99.9)=231.39ms
     iterations.....................: 252396  4139.845847/s
     success_rate...................: 100.00% ✓ 252396      ✗ 0     
     vus............................: 56      min=0         max=499 
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

     checks.........................: 100.00% ✓ 503595      ✗ 0     
     data_received..................: 15 GB   240 MB/s
     data_sent......................: 203 MB  3.3 MB/s
     http_req_blocked...............: avg=25.49µs  min=942ns   med=2.99µs  max=73.92ms  p(90)=4.93µs   p(95)=6.26µs   p(99.9)=1.88ms  
     http_req_connecting............: avg=21.43µs  min=0s      med=0s      max=73.72ms  p(90)=0s       p(95)=0s       p(99.9)=1.75ms  
     http_req_duration..............: avg=84.16ms  min=1.35ms  med=77.84ms max=299.36ms p(90)=165.64ms p(95)=182.47ms p(99.9)=242.95ms
       { expected_response:true }...: avg=84.16ms  min=1.35ms  med=77.84ms max=299.36ms p(90)=165.64ms p(95)=182.47ms p(99.9)=242.95ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 168865
     http_req_receiving.............: avg=189.81µs min=26.18µs med=58.13µs max=51.45ms  p(90)=214.62µs p(95)=408.85µs p(99.9)=22.24ms 
     http_req_sending...............: avg=87.31µs  min=4.46µs  med=11.5µs  max=186.34ms p(90)=22.66µs  p(95)=142.62µs p(99.9)=13.03ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=83.88ms  min=1.27ms  med=77.62ms max=299.21ms p(90)=165.24ms p(95)=181.77ms p(99.9)=241.45ms
     http_reqs......................: 168865  2738.236886/s
     iteration_duration.............: avg=84.93ms  min=2.55ms  med=78.77ms max=330.78ms p(90)=166.15ms p(95)=182.97ms p(99.9)=243.92ms
     iterations.....................: 167865  2722.021347/s
     success_rate...................: 100.00% ✓ 167865      ✗ 0     
     vus............................: 87      min=0         max=495 
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

     checks.........................: 100.00% ✓ 270993      ✗ 0    
     data_received..................: 8.0 GB  128 MB/s
     data_sent......................: 110 MB  1.8 MB/s
     http_req_blocked...............: avg=5.96µs   min=971ns   med=2.58µs   max=23.27ms  p(90)=4.69µs   p(95)=5.79µs   p(99.9)=509.97µs
     http_req_connecting............: avg=2.61µs   min=0s      med=0s       max=23.14ms  p(90)=0s       p(95)=0s       p(99.9)=451µs   
     http_req_duration..............: avg=156.15ms min=1.93ms  med=130.07ms max=850.61ms p(90)=323.17ms p(95)=382.98ms p(99.9)=646.17ms
       { expected_response:true }...: avg=156.15ms min=1.93ms  med=130.07ms max=850.61ms p(90)=323.17ms p(95)=382.98ms p(99.9)=646.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 91331
     http_req_receiving.............: avg=83.13µs  min=28.71µs med=62.85µs  max=182.24ms p(90)=104.86µs p(95)=125.22µs p(99.9)=2.28ms  
     http_req_sending...............: avg=34.96µs  min=4.74µs  med=12µs     max=182.15ms p(90)=20.12µs  p(95)=24.48µs  p(99.9)=3.84ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=156.03ms min=1.87ms  med=129.95ms max=850.55ms p(90)=323.05ms p(95)=382.81ms p(99.9)=646.1ms 
     http_reqs......................: 91331   1465.436044/s
     iteration_duration.............: avg=158.13ms min=6.56ms  med=132.28ms max=850.79ms p(90)=324.63ms p(95)=384.01ms p(99.9)=647.23ms
     iterations.....................: 90331   1449.390714/s
     success_rate...................: 100.00% ✓ 90331       ✗ 0    
     vus............................: 72      min=0         max=494
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

     checks.........................: 100.00% ✓ 242646      ✗ 0    
     data_received..................: 7.2 GB  115 MB/s
     data_sent......................: 98 MB   1.6 MB/s
     http_req_blocked...............: avg=5.23µs   min=912ns  med=2.29µs   max=14.33ms  p(90)=3.92µs   p(95)=4.83µs   p(99.9)=367.47µs
     http_req_connecting............: avg=2.3µs    min=0s     med=0s       max=14.28ms  p(90)=0s       p(95)=0s       p(99.9)=255.05µs
     http_req_duration..............: avg=174.22ms min=2ms    med=171.87ms max=469.75ms p(90)=330.29ms p(95)=354.73ms p(99.9)=420.51ms
       { expected_response:true }...: avg=174.22ms min=2ms    med=171.87ms max=469.75ms p(90)=330.29ms p(95)=354.73ms p(99.9)=420.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 81882
     http_req_receiving.............: avg=70.35µs  min=25.8µs med=58.67µs  max=22.7ms   p(90)=95.45µs  p(95)=110.82µs p(99.9)=892.32µs
     http_req_sending...............: avg=30.43µs  min=4.69µs med=10.25µs  max=111.05ms p(90)=16.62µs  p(95)=20.01µs  p(99.9)=3.38ms  
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=174.12ms min=1.94ms med=171.78ms max=469.68ms p(90)=330.2ms  p(95)=354.63ms p(99.9)=420.45ms
     http_reqs......................: 81882   1311.675955/s
     iteration_duration.............: avg=176.59ms min=5.27ms med=174.45ms max=469.99ms p(90)=331.08ms p(95)=355.4ms  p(99.9)=420.81ms
     iterations.....................: 80882   1295.656855/s
     success_rate...................: 100.00% ✓ 80882       ✗ 0    
     vus............................: 76      min=0         max=493
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

     checks.........................: 100.00% ✓ 92049      ✗ 0    
     data_received..................: 2.8 GB  43 MB/s
     data_sent......................: 38 MB   588 kB/s
     http_req_blocked...............: avg=8.97µs   min=1.03µs  med=2.58µs   max=10.73ms  p(90)=4.24µs   p(95)=5.2µs    p(99.9)=1.88ms
     http_req_connecting............: avg=5.4µs    min=0s      med=0s       max=10.68ms  p(90)=0s       p(95)=0s       p(99.9)=1.86ms
     http_req_duration..............: avg=453.56ms min=3.83ms  med=423.57ms max=1.79s    p(90)=887.84ms p(95)=975.5ms  p(99.9)=1.47s 
       { expected_response:true }...: avg=453.56ms min=3.83ms  med=423.57ms max=1.79s    p(90)=887.84ms p(95)=975.5ms  p(99.9)=1.47s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 31683
     http_req_receiving.............: avg=84.03µs  min=29.84µs med=70.33µs  max=45.85ms  p(90)=108.44µs p(95)=123.38µs p(99.9)=1.24ms
     http_req_sending...............: avg=28.79µs  min=4.95µs  med=13.3µs   max=104.92ms p(90)=19.81µs  p(95)=22.22µs  p(99.9)=2.08ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=453.45ms min=3.76ms  med=423.5ms  max=1.79s    p(90)=887.67ms p(95)=975.41ms p(99.9)=1.47s 
     http_reqs......................: 31683   489.492569/s
     iteration_duration.............: avg=468.55ms min=17.61ms med=440.79ms max=1.79s    p(90)=893.03ms p(95)=980.26ms p(99.9)=1.48s 
     iterations.....................: 30683   474.042878/s
     success_rate...................: 100.00% ✓ 30683      ✗ 0    
     vus............................: 92      min=0        max=500
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

     checks.........................: 100.00% ✓ 48054      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 20 MB   303 kB/s
     http_req_blocked...............: avg=18.25µs  min=1.4µs   med=3.85µs   max=10.1ms  p(90)=5.77µs   p(95)=7.35µs   p(99.9)=4.72ms
     http_req_connecting............: avg=12.39µs  min=0s      med=0s       max=10.03ms p(90)=0s       p(95)=0s       p(99.9)=4.67ms
     http_req_duration..............: avg=854.2ms  min=5.59ms  med=770.94ms max=4.65s   p(90)=1.71s    p(95)=1.93s    p(99.9)=3.78s 
       { expected_response:true }...: avg=854.2ms  min=5.59ms  med=770.94ms max=4.65s   p(90)=1.71s    p(95)=1.93s    p(99.9)=3.78s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 17018
     http_req_receiving.............: avg=100.69µs min=36.75µs med=92.69µs  max=15.96ms p(90)=130.53µs p(95)=147.04µs p(99.9)=1.41ms
     http_req_sending...............: avg=29.02µs  min=6.15µs  med=18.53µs  max=20.59ms p(90)=24.22µs  p(95)=27.77µs  p(99.9)=2.54ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=854.07ms min=5.51ms  med=770.8ms  max=4.65s   p(90)=1.71s    p(95)=1.93s    p(99.9)=3.78s 
     http_reqs......................: 17018   252.721069/s
     iteration_duration.............: avg=907.58ms min=31.08ms med=845.68ms max=4.66s   p(90)=1.73s    p(95)=1.94s    p(99.9)=3.79s 
     iterations.....................: 16018   237.870848/s
     success_rate...................: 100.00% ✓ 16018      ✗ 0    
     vus............................: 73      min=0        max=500
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

     checks.........................: 100.00% ✓ 46467      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   289 kB/s
     http_req_blocked...............: avg=14.08µs  min=1.22µs  med=3.31µs   max=12.78ms  p(90)=5.04µs   p(95)=6.59µs   p(99.9)=2.08ms  
     http_req_connecting............: avg=8.99µs   min=0s      med=0s       max=12.72ms  p(90)=0s       p(95)=0s       p(99.9)=1.96ms  
     http_req_duration..............: avg=880.34ms min=7.47ms  med=801.97ms max=2.93s    p(90)=1.78s    p(95)=1.92s    p(99.9)=2.63s   
       { expected_response:true }...: avg=880.34ms min=7.47ms  med=801.97ms max=2.93s    p(90)=1.78s    p(95)=1.92s    p(99.9)=2.63s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16489
     http_req_receiving.............: avg=95.26µs  min=33.78µs med=86.72µs  max=32.89ms  p(90)=125.66µs p(95)=141.19µs p(99.9)=986.53µs
     http_req_sending...............: avg=42.15µs  min=5.1µs   med=16.53µs  max=153.52ms p(90)=21.87µs  p(95)=25.37µs  p(99.9)=2.8ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=880.2ms  min=7.38ms  med=801.84ms max=2.93s    p(90)=1.78s    p(95)=1.92s    p(99.9)=2.63s   
     http_reqs......................: 16489   240.934329/s
     iteration_duration.............: avg=937.21ms min=46.05ms med=869.04ms max=2.94s    p(90)=1.8s     p(95)=1.93s    p(99.9)=2.64s   
     iterations.....................: 15489   226.322507/s
     success_rate...................: 100.00% ✓ 15489      ✗ 0    
     vus............................: 78      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

