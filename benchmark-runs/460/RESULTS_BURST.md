## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 4,725 | 4,736 | 4,721 | 0.1% | 428 MB | 92.7 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.7 | 4,666 | 4,753 | 4,626 | 1.1% | 420 MB | 92.3 KB |  |
| fusion-aot-11 | 16.7.3 | 4,598 | 4,611 | 4,589 | 0.2% | 169 MB | 37.7 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.7 | 4,565 | 4,587 | 4,402 | 1.7% | 406 MB | 91.0 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,483 | 4,489 | 4,475 | 0.1% | 418 MB | 95.4 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.7 | 4,456 | 4,525 | 4,430 | 1.0% | 185 MB | 42.4 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,418 | 4,423 | 4,328 | 1.0% | 186 MB | 43.1 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.7 | 4,281 | 4,288 | 4,267 | 0.2% | 157 MB | 37.6 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,150 | 4,182 | 4,131 | 0.5% | 2,294 MB | 565.9 KB |  |
| hive-router | v0.3.6 | 2,716 | 2,731 | 2,713 | 0.3% | 179 MB | 67.6 KB |  |
| cosmo | 0.363.0 | 1,362 | 1,365 | 1,360 | 0.1% | 654 MB | 491.4 KB |  |
| caliban | 3.2.0 | 1,353 | 1,364 | 1,350 | 0.4% | 10,786 MB | 8,163.1 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 497 | 498 | 492 | 0.5% | 3,163 MB | 6,516.4 KB |  |
| hive-gateway | 2.15.3 | 252 | 253 | 249 | 0.7% | 3,962 MB | 16,098.4 KB |  |
| apollo-gateway | 2.14.4 | 235 | 237 | 234 | 0.5% | 2,452 MB | 10,683.8 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (5115 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (6332 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (158173 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 860853      ✗ 0     
     data_received..................: 25 GB   414 MB/s
     data_sent......................: 346 MB  5.7 MB/s
     http_req_blocked...............: avg=60.8µs   min=782ns    med=2.04µs  max=224.24ms p(90)=3.66µs   p(95)=4.79µs   p(99.9)=22.03ms 
     http_req_connecting............: avg=56.95µs  min=0s       med=0s      max=115.39ms p(90)=0s       p(95)=0s       p(99.9)=21.28ms 
     http_req_duration..............: avg=48.06ms  min=748.71µs med=40.57ms max=310.09ms p(90)=101.76ms p(95)=125.66ms p(99.9)=180.77ms
       { expected_response:true }...: avg=48.06ms  min=748.71µs med=40.57ms max=310.09ms p(90)=101.76ms p(95)=125.66ms p(99.9)=180.77ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 287951
     http_req_receiving.............: avg=339.85µs min=25.59µs  med=50.32µs max=200.45ms p(90)=207.44µs p(95)=363.62µs p(99.9)=51.77ms 
     http_req_sending...............: avg=142.41µs min=3.94µs   med=8.51µs  max=129.59ms p(90)=16.75µs  p(95)=117.04µs p(99.9)=25.99ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.58ms  min=709.39µs med=40.28ms max=263.74ms p(90)=100.6ms  p(95)=124.32ms p(99.9)=171.72ms
     http_reqs......................: 287951  4725.680527/s
     iteration_duration.............: avg=49.64ms  min=1.31ms   med=41.23ms max=336.52ms p(90)=105.53ms p(95)=131.15ms p(99.9)=203.11ms
     iterations.....................: 286951  4709.269122/s
     success_rate...................: 100.00% ✓ 286951      ✗ 0     
     vus............................: 54      min=0         max=499 
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

     checks.........................: 100.00% ✓ 850425      ✗ 0     
     data_received..................: 25 GB   408 MB/s
     data_sent......................: 342 MB  5.6 MB/s
     http_req_blocked...............: avg=69.65µs  min=811ns    med=2.41µs  max=148.49ms p(90)=4.05µs   p(95)=5.21µs   p(99.9)=25.61ms 
     http_req_connecting............: avg=66.16µs  min=0s       med=0s      max=148.45ms p(90)=0s       p(95)=0s       p(99.9)=24.87ms 
     http_req_duration..............: avg=48.23ms  min=772.25µs med=40.58ms max=285.92ms p(90)=101.29ms p(95)=124.87ms p(99.9)=180.25ms
       { expected_response:true }...: avg=48.23ms  min=772.25µs med=40.58ms max=285.92ms p(90)=101.29ms p(95)=124.87ms p(99.9)=180.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 284475
     http_req_receiving.............: avg=362.02µs min=24.05µs  med=52.69µs max=129.54ms p(90)=207.67µs p(95)=360.9µs  p(99.9)=50.87ms 
     http_req_sending...............: avg=161.25µs min=3.92µs   med=9.07µs  max=223.86ms p(90)=17.31µs  p(95)=117.35µs p(99.9)=28.63ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.7ms   min=723.64µs med=40.24ms max=253.49ms p(90)=100.03ms p(95)=123.58ms p(99.9)=174.18ms
     http_reqs......................: 284475  4666.084347/s
     iteration_duration.............: avg=50.25ms  min=1.2ms    med=41.53ms max=362.97ms p(90)=106.26ms p(95)=132.01ms p(99.9)=202.74ms
     iterations.....................: 283475  4649.681906/s
     success_rate...................: 100.00% ✓ 283475      ✗ 0     
     vus............................: 56      min=0         max=498 
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

     checks.........................: 100.00% ✓ 838860      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 337 MB  5.5 MB/s
     http_req_blocked...............: avg=52µs     min=852ns    med=2.04µs  max=151.4ms  p(90)=3.59µs   p(95)=4.72µs   p(99.9)=17.73ms 
     http_req_connecting............: avg=48.25µs  min=0s       med=0s      max=118.9ms  p(90)=0s       p(95)=0s       p(99.9)=17.51ms 
     http_req_duration..............: avg=49.45ms  min=848.81µs med=41.54ms max=299.92ms p(90)=105.91ms p(95)=130.65ms p(99.9)=182.05ms
       { expected_response:true }...: avg=49.45ms  min=848.81µs med=41.54ms max=299.92ms p(90)=105.91ms p(95)=130.65ms p(99.9)=182.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280620
     http_req_receiving.............: avg=272.49µs min=24.83µs  med=49.32µs max=94.32ms  p(90)=209.02µs p(95)=372.24µs p(99.9)=35.48ms 
     http_req_sending...............: avg=125.77µs min=4.16µs   med=8.55µs  max=85.73ms  p(90)=16.77µs  p(95)=120.29µs p(99.9)=23.25ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.05ms  min=789.36µs med=41.27ms max=298.78ms p(90)=104.98ms p(95)=129.72ms p(99.9)=178.83ms
     http_reqs......................: 280620  4598.360821/s
     iteration_duration.............: avg=50.94ms  min=1.4ms    med=42.31ms max=353.96ms p(90)=109.15ms p(95)=134.5ms  p(99.9)=203.69ms
     iterations.....................: 279620  4581.974388/s
     success_rate...................: 100.00% ✓ 279620      ✗ 0     
     vus............................: 58      min=0         max=498 
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

     checks.........................: 100.00% ✓ 834033      ✗ 0     
     data_received..................: 24 GB   400 MB/s
     data_sent......................: 335 MB  5.5 MB/s
     http_req_blocked...............: avg=62.78µs  min=811ns    med=2.13µs  max=125.93ms p(90)=3.89µs   p(95)=5.12µs   p(99.9)=21.43ms 
     http_req_connecting............: avg=59.45µs  min=0s       med=0s      max=120.61ms p(90)=0s       p(95)=0s       p(99.9)=20.57ms 
     http_req_duration..............: avg=49.75ms  min=899.47µs med=41.94ms max=322.83ms p(90)=105.83ms p(95)=130.53ms p(99.9)=182.22ms
       { expected_response:true }...: avg=49.75ms  min=899.47µs med=41.94ms max=322.83ms p(90)=105.83ms p(95)=130.53ms p(99.9)=182.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 279011
     http_req_receiving.............: avg=335.93µs min=25.98µs  med=52.68µs max=213.68ms p(90)=211.14µs p(95)=377.25µs p(99.9)=46.03ms 
     http_req_sending...............: avg=143.67µs min=4.14µs   med=8.79µs  max=165.62ms p(90)=18.2µs   p(95)=120.08µs p(99.9)=26.19ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.27ms  min=848.05µs med=41.58ms max=322.43ms p(90)=104.82ms p(95)=129.32ms p(99.9)=178.11ms
     http_reqs......................: 279011  4565.555041/s
     iteration_duration.............: avg=51.24ms  min=1.51ms   med=42.8ms  max=330.68ms p(90)=109.39ms p(95)=135.46ms p(99.9)=199.55ms
     iterations.....................: 278011  4549.191689/s
     success_rate...................: 100.00% ✓ 278011      ✗ 0     
     vus............................: 62      min=0         max=497 
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

     checks.........................: 100.00% ✓ 819078      ✗ 0     
     data_received..................: 24 GB   392 MB/s
     data_sent......................: 329 MB  5.4 MB/s
     http_req_blocked...............: avg=69.06µs  min=821ns    med=2.61µs  max=171.15ms p(90)=4.33µs   p(95)=5.6µs    p(99.9)=24.91ms 
     http_req_connecting............: avg=64.44µs  min=0s       med=0s      max=136.85ms p(90)=0s       p(95)=0s       p(99.9)=24.28ms 
     http_req_duration..............: avg=50.3ms   min=900.04µs med=41.91ms max=314.34ms p(90)=107.93ms p(95)=133.53ms p(99.9)=192.63ms
       { expected_response:true }...: avg=50.3ms   min=900.04µs med=41.91ms max=314.34ms p(90)=107.93ms p(95)=133.53ms p(99.9)=192.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 274026
     http_req_receiving.............: avg=389.11µs min=26.28µs  med=53.93µs max=172.02ms p(90)=230.3µs  p(95)=390.85µs p(99.9)=56.27ms 
     http_req_sending...............: avg=159.04µs min=3.98µs   med=9.36µs  max=136.01ms p(90)=19.37µs  p(95)=127µs    p(99.9)=29.09ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.75ms  min=826.96µs med=41.58ms max=314.1ms  p(90)=106.74ms p(95)=132.19ms p(99.9)=183.72ms
     http_reqs......................: 274026  4483.904925/s
     iteration_duration.............: avg=52.12ms  min=1.45ms   med=42.75ms max=333.29ms p(90)=111.96ms p(95)=139.31ms p(99.9)=214.77ms
     iterations.....................: 273026  4467.541861/s
     success_rate...................: 100.00% ✓ 273026      ✗ 0     
     vus............................: 62      min=0         max=497 
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

     checks.........................: 100.00% ✓ 813027      ✗ 0     
     data_received..................: 24 GB   390 MB/s
     data_sent......................: 327 MB  5.4 MB/s
     http_req_blocked...............: avg=56.94µs  min=822ns    med=2.25µs  max=206.53ms p(90)=3.98µs   p(95)=5.14µs   p(99.9)=19.85ms 
     http_req_connecting............: avg=52.17µs  min=0s       med=0s      max=139.53ms p(90)=0s       p(95)=0s       p(99.9)=18.76ms 
     http_req_duration..............: avg=50.98ms  min=832.09µs med=41.99ms max=319.07ms p(90)=109.89ms p(95)=137.19ms p(99.9)=191.49ms
       { expected_response:true }...: avg=50.98ms  min=832.09µs med=41.99ms max=319.07ms p(90)=109.89ms p(95)=137.19ms p(99.9)=191.49ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 272009
     http_req_receiving.............: avg=305.29µs min=25.05µs  med=50.26µs max=101.78ms p(90)=218.04µs p(95)=388.09µs p(99.9)=43.88ms 
     http_req_sending...............: avg=132.65µs min=4.2µs    med=8.67µs  max=152.68ms p(90)=17.59µs  p(95)=128.04µs p(99.9)=23.09ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.54ms  min=790.31µs med=41.72ms max=318.89ms p(90)=108.86ms p(95)=135.95ms p(99.9)=188ms   
     http_reqs......................: 272009  4456.984162/s
     iteration_duration.............: avg=52.56ms  min=1.39ms   med=42.98ms max=362.65ms p(90)=112.95ms p(95)=141ms    p(99.9)=215.54ms
     iterations.....................: 271009  4440.598733/s
     success_rate...................: 100.00% ✓ 271009      ✗ 0     
     vus............................: 58      min=0         max=498 
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

     checks.........................: 100.00% ✓ 807843     ✗ 0     
     data_received..................: 24 GB   387 MB/s
     data_sent......................: 325 MB  5.3 MB/s
     http_req_blocked...............: avg=47.57µs min=811ns    med=2.07µs  max=130.63ms p(90)=3.8µs    p(95)=5.04µs   p(99.9)=15.4ms  
     http_req_connecting............: avg=43.83µs min=0s       med=0s      max=112.33ms p(90)=0s       p(95)=0s       p(99.9)=15ms    
     http_req_duration..............: avg=51.74ms min=981.54µs med=43.81ms max=302.87ms p(90)=110.75ms p(95)=135.66ms p(99.9)=190.22ms
       { expected_response:true }...: avg=51.74ms min=981.54µs med=43.81ms max=302.87ms p(90)=110.75ms p(95)=135.66ms p(99.9)=190.22ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 270281
     http_req_receiving.............: avg=284µs   min=25.14µs  med=49.89µs max=171.18ms p(90)=218.08µs p(95)=379.4µs  p(99.9)=37.22ms 
     http_req_sending...............: avg=117.1µs min=4.09µs   med=8.38µs  max=74.82ms  p(90)=18.35µs  p(95)=124.29µs p(99.9)=21.05ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.34ms min=926.9µs  med=43.57ms max=302.26ms p(90)=109.9ms  p(95)=134.67ms p(99.9)=187.51ms
     http_reqs......................: 270281  4418.30802/s
     iteration_duration.............: avg=52.9ms  min=1.58ms   med=44.42ms max=328.93ms p(90)=113.01ms p(95)=138.32ms p(99.9)=216.22ms
     iterations.....................: 269281  4401.96093/s
     success_rate...................: 100.00% ✓ 269281     ✗ 0     
     vus............................: 66      min=0        max=496 
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 783117      ✗ 0     
     data_received..................: 23 GB   375 MB/s
     data_sent......................: 315 MB  5.1 MB/s
     http_req_blocked...............: avg=53.58µs  min=951ns    med=2.65µs  max=117.36ms p(90)=4.31µs   p(95)=5.47µs   p(99.9)=17.91ms 
     http_req_connecting............: avg=49.9µs   min=0s       med=0s      max=97.33ms  p(90)=0s       p(95)=0s       p(99.9)=17.47ms 
     http_req_duration..............: avg=53.05ms  min=985.53µs med=44.47ms max=287.05ms p(90)=113.72ms p(95)=140.51ms p(99.9)=191.27ms
       { expected_response:true }...: avg=53.05ms  min=985.53µs med=44.47ms max=287.05ms p(90)=113.72ms p(95)=140.51ms p(99.9)=191.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 262039
     http_req_receiving.............: avg=317.25µs min=26.22µs  med=52.15µs max=87.21ms  p(90)=233.8µs  p(95)=407.45µs p(99.9)=42.32ms 
     http_req_sending...............: avg=136.41µs min=4.33µs   med=9.43µs  max=147.22ms p(90)=19.27µs  p(95)=133.8µs  p(99.9)=24.69ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=52.6ms   min=921.35µs med=44.19ms max=286.6ms  p(90)=112.78ms p(95)=139.48ms p(99.9)=187.1ms 
     http_reqs......................: 262039  4281.839599/s
     iteration_duration.............: avg=54.58ms  min=1.61ms   med=45.35ms max=316.79ms p(90)=116.85ms p(95)=144.24ms p(99.9)=231.48ms
     iterations.....................: 261039  4265.499132/s
     success_rate...................: 100.00% ✓ 261039      ✗ 0     
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

     checks.........................: 100.00% ✓ 755721      ✗ 0     
     data_received..................: 22 GB   363 MB/s
     data_sent......................: 304 MB  5.0 MB/s
     http_req_blocked...............: avg=54.34µs  min=862ns    med=2.68µs  max=116.92ms p(90)=4.47µs   p(95)=5.65µs   p(99.9)=17.19ms 
     http_req_connecting............: avg=50.26µs  min=0s       med=0s      max=112.19ms p(90)=0s       p(95)=0s       p(99.9)=17.01ms 
     http_req_duration..............: avg=54.84ms  min=708.34µs med=45.67ms max=294.69ms p(90)=117.69ms p(95)=148.22ms p(99.9)=223.07ms
       { expected_response:true }...: avg=54.84ms  min=708.34µs med=45.67ms max=294.69ms p(90)=117.69ms p(95)=148.22ms p(99.9)=223.07ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 252907
     http_req_receiving.............: avg=318.26µs min=26.14µs  med=53.89µs max=100.72ms p(90)=227.25µs p(95)=406.05µs p(99.9)=49.03ms 
     http_req_sending...............: avg=135.38µs min=3.99µs   med=9.68µs  max=135.42ms p(90)=19.52µs  p(95)=136.46µs p(99.9)=23.38ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=54.38ms  min=657.65µs med=45.37ms max=292.49ms p(90)=116.59ms p(95)=146.99ms p(99.9)=219.23ms
     http_reqs......................: 252907  4150.38471/s
     iteration_duration.............: avg=56.55ms  min=1.47ms   med=46.81ms max=364.46ms p(90)=121.44ms p(95)=152.89ms p(99.9)=244.28ms
     iterations.....................: 251907  4133.973995/s
     success_rate...................: 100.00% ✓ 251907      ✗ 0     
     vus............................: 54      min=0         max=499 
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

     checks.........................: 100.00% ✓ 498996      ✗ 0     
     data_received..................: 15 GB   238 MB/s
     data_sent......................: 201 MB  3.3 MB/s
     http_req_blocked...............: avg=15.28µs  min=862ns  med=2.44µs  max=51.08ms  p(90)=4.34µs   p(95)=5.57µs   p(99.9)=959.96µs
     http_req_connecting............: avg=12.07µs  min=0s     med=0s      max=51.02ms  p(90)=0s       p(95)=0s       p(99.9)=893.44µs
     http_req_duration..............: avg=84.95ms  min=1.3ms  med=78.1ms  max=325.79ms p(90)=165.8ms  p(95)=182.53ms p(99.9)=238.13ms
       { expected_response:true }...: avg=84.95ms  min=1.3ms  med=78.1ms  max=325.79ms p(90)=165.8ms  p(95)=182.53ms p(99.9)=238.13ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 167332
     http_req_receiving.............: avg=130.46µs min=24.9µs med=54.74µs max=41.96ms  p(90)=167.91µs p(95)=354.2µs  p(99.9)=10.98ms 
     http_req_sending...............: avg=68.97µs  min=4.34µs med=10.63µs max=61.01ms  p(90)=21.71µs  p(95)=124.38µs p(99.9)=9.01ms  
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=84.75ms  min=1.26ms med=77.91ms max=325.41ms p(90)=165.56ms p(95)=182.32ms p(99.9)=236.87ms
     http_reqs......................: 167332  2716.169364/s
     iteration_duration.............: avg=85.7ms   min=3.56ms med=78.96ms max=354.57ms p(90)=166.26ms p(95)=183ms    p(99.9)=238.76ms
     iterations.....................: 166332  2699.937146/s
     success_rate...................: 100.00% ✓ 166332      ✗ 0     
     vus............................: 84      min=0         max=494 
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

     checks.........................: 100.00% ✓ 252051      ✗ 0    
     data_received..................: 7.4 GB  119 MB/s
     data_sent......................: 102 MB  1.6 MB/s
     http_req_blocked...............: avg=5.02µs   min=942ns   med=2.34µs   max=6.28ms   p(90)=3.98µs   p(95)=4.92µs   p(99.9)=304.11µs
     http_req_connecting............: avg=1.95µs   min=0s      med=0s       max=6.23ms   p(90)=0s       p(95)=0s       p(99.9)=179.25µs
     http_req_duration..............: avg=167.74ms min=2ms     med=166.52ms max=446.57ms p(90)=318.95ms p(95)=339.98ms p(99.9)=403.81ms
       { expected_response:true }...: avg=167.74ms min=2ms     med=166.52ms max=446.57ms p(90)=318.95ms p(95)=339.98ms p(99.9)=403.81ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 85017
     http_req_receiving.............: avg=73.57µs  min=27.56µs med=58.75µs  max=147.43ms p(90)=95.44µs  p(95)=110µs    p(99.9)=1ms     
     http_req_sending...............: avg=28.92µs  min=4.89µs  med=10.65µs  max=64.55ms  p(90)=17.31µs  p(95)=20.71µs  p(99.9)=3.28ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=167.63ms min=1.92ms  med=166.44ms max=446.51ms p(90)=318.83ms p(95)=339.87ms p(99.9)=403.74ms
     http_reqs......................: 85017   1362.745686/s
     iteration_duration.............: avg=169.96ms min=4.07ms  med=169.02ms max=446.75ms p(90)=319.77ms p(95)=340.52ms p(99.9)=404.61ms
     iterations.....................: 84017   1346.71659/s
     success_rate...................: 100.00% ✓ 84017       ✗ 0    
     vus............................: 75      min=0         max=494
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

     checks.........................: 100.00% ✓ 250593      ✗ 0    
     data_received..................: 7.4 GB  118 MB/s
     data_sent......................: 102 MB  1.6 MB/s
     http_req_blocked...............: avg=5.96µs   min=932ns   med=2.5µs    max=13.47ms  p(90)=4.28µs   p(95)=5.19µs   p(99.9)=353.27µs
     http_req_connecting............: avg=2.76µs   min=0s      med=0s       max=13.41ms  p(90)=0s       p(95)=0s       p(99.9)=221.28µs
     http_req_duration..............: avg=168.8ms  min=2.01ms  med=136.41ms max=1.07s    p(90)=361.15ms p(95)=429.32ms p(99.9)=733.71ms
       { expected_response:true }...: avg=168.8ms  min=2.01ms  med=136.41ms max=1.07s    p(90)=361.15ms p(95)=429.32ms p(99.9)=733.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 84531
     http_req_receiving.............: avg=74.72µs  min=29.07µs med=60.05µs  max=93.84ms  p(90)=97.1µs   p(95)=113.43µs p(99.9)=1.33ms  
     http_req_sending...............: avg=30.47µs  min=4.82µs  med=11.07µs  max=175.76ms p(90)=17.9µs   p(95)=21.39µs  p(99.9)=3.2ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=168.69ms min=1.94ms  med=136.29ms max=1.07s    p(90)=361.02ms p(95)=429.25ms p(99.9)=733.65ms
     http_reqs......................: 84531   1353.443992/s
     iteration_duration.............: avg=171.05ms min=6.59ms  med=138.61ms max=1.07s    p(90)=362.7ms  p(95)=430.57ms p(99.9)=734.31ms
     iterations.....................: 83531   1337.432777/s
     success_rate...................: 100.00% ✓ 83531       ✗ 0    
     vus............................: 78      min=0         max=493
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

     checks.........................: 100.00% ✓ 93651      ✗ 0    
     data_received..................: 2.8 GB  44 MB/s
     data_sent......................: 39 MB   598 kB/s
     http_req_blocked...............: avg=8.9µs    min=1.08µs  med=2.72µs   max=10.73ms  p(90)=4.4µs    p(95)=5.37µs   p(99.9)=1.55ms  
     http_req_connecting............: avg=5.18µs   min=0s      med=0s       max=10.66ms  p(90)=0s       p(95)=0s       p(99.9)=1.53ms  
     http_req_duration..............: avg=445.53ms min=3.89ms  med=413.48ms max=2.04s    p(90)=883.8ms  p(95)=960.6ms  p(99.9)=1.39s   
       { expected_response:true }...: avg=445.53ms min=3.89ms  med=413.48ms max=2.04s    p(90)=883.8ms  p(95)=960.6ms  p(99.9)=1.39s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 32217
     http_req_receiving.............: avg=82.45µs  min=27.83µs med=69.84µs  max=62.43ms  p(90)=107.96µs p(95)=122.65µs p(99.9)=822.91µs
     http_req_sending...............: avg=31.33µs  min=5.18µs  med=13.7µs   max=112.28ms p(90)=20.12µs  p(95)=22.55µs  p(99.9)=2.31ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=445.42ms min=3.82ms  med=413.39ms max=2.04s    p(90)=883.69ms p(95)=960.48ms p(99.9)=1.39s   
     http_reqs......................: 32217   497.883053/s
     iteration_duration.............: avg=460ms    min=14.07ms med=432.91ms max=2.04s    p(90)=888.12ms p(95)=963.56ms p(99.9)=1.39s   
     iterations.....................: 31217   482.429005/s
     success_rate...................: 100.00% ✓ 31217      ✗ 0    
     vus............................: 87      min=0        max=500
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

     checks.........................: 100.00% ✓ 47871      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 20 MB   303 kB/s
     http_req_blocked...............: avg=11.58µs  min=1.09µs  med=3.21µs   max=2.83ms  p(90)=4.95µs  p(95)=6.6µs    p(99.9)=1.46ms
     http_req_connecting............: avg=6.8µs    min=0s      med=0s       max=2.78ms  p(90)=0s      p(95)=0s       p(99.9)=1.44ms
     http_req_duration..............: avg=857ms    min=5.6ms   med=770.64ms max=4.5s    p(90)=1.71s   p(95)=1.97s    p(99.9)=3.77s 
       { expected_response:true }...: avg=857ms    min=5.6ms   med=770.64ms max=4.5s    p(90)=1.71s   p(95)=1.97s    p(99.9)=3.77s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16957
     http_req_receiving.............: avg=103.22µs min=31.33µs med=91.67µs  max=31.85ms p(90)=130.8µs p(95)=147.18µs p(99.9)=1.48ms
     http_req_sending...............: avg=51.56µs  min=5.22µs  med=16.99µs  max=137.3ms p(90)=21.88µs p(95)=25.1µs   p(99.9)=3.24ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s      p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=856.84ms min=5.5ms   med=770.52ms max=4.5s    p(90)=1.71s   p(95)=1.97s    p(99.9)=3.77s 
     http_reqs......................: 16957   252.16305/s
     iteration_duration.............: avg=910.74ms min=27.6ms  med=830.75ms max=4.51s   p(90)=1.74s   p(95)=2s       p(99.9)=3.78s 
     iterations.....................: 15957   237.292315/s
     success_rate...................: 100.00% ✓ 15957      ✗ 0    
     vus............................: 67      min=0        max=498
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

     checks.........................: 100.00% ✓ 45498      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 19 MB   283 kB/s
     http_req_blocked...............: avg=10.98µs  min=1.13µs  med=3.18µs   max=6.4ms   p(90)=4.82µs   p(95)=6.27µs   p(99.9)=1.13ms
     http_req_connecting............: avg=6.17µs   min=0s      med=0s       max=6.35ms  p(90)=0s       p(95)=0s       p(99.9)=1.1ms 
     http_req_duration..............: avg=899ms    min=7.72ms  med=818.7ms  max=3.13s   p(90)=1.81s    p(95)=1.95s    p(99.9)=2.68s 
       { expected_response:true }...: avg=899ms    min=7.72ms  med=818.7ms  max=3.13s   p(90)=1.81s    p(95)=1.95s    p(99.9)=2.68s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16166
     http_req_receiving.............: avg=105.39µs min=32.61µs med=84.68µs  max=56.27ms p(90)=122.25µs p(95)=138.05µs p(99.9)=3.02ms
     http_req_sending...............: avg=24.82µs  min=5.65µs  med=16.33µs  max=25.71ms p(90)=21.21µs  p(95)=24.73µs  p(99.9)=2.69ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=898.87ms min=7.59ms  med=818.57ms max=3.13s   p(90)=1.81s    p(95)=1.95s    p(99.9)=2.68s 
     http_reqs......................: 16166   235.54003/s
     iteration_duration.............: avg=958.21ms min=56.89ms med=909.72ms max=3.14s   p(90)=1.83s    p(95)=1.97s    p(99.9)=2.69s 
     iterations.....................: 15166   220.969943/s
     success_rate...................: 100.00% ✓ 15166      ✗ 0    
     vus............................: 88      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

