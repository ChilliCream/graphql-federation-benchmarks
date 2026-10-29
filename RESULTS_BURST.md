## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.2 | 4,751 | 4,777 | 4,738 | 0.3% | 418 MB | 90.2 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.7 | 4,666 | 4,697 | 4,577 | 1.1% | 416 MB | 91.2 KB |  |
| fusion-aot-11 | 16.7.2 | 4,577 | 4,581 | 4,562 | 0.2% | 177 MB | 39.6 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.7 | 4,541 | 4,622 | 4,512 | 1.1% | 177 MB | 40.0 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.7 | 4,477 | 4,545 | 4,447 | 0.8% | 411 MB | 94.1 KB |  |
| fusion-fed-net-11 | 16.7.2 | 4,461 | 4,464 | 4,454 | 0.1% | 412 MB | 94.5 KB |  |
| fusion-fed-aot-11 | 16.7.2 | 4,372 | 4,426 | 4,356 | 0.7% | 179 MB | 41.8 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.7 | 4,257 | 4,269 | 4,206 | 0.6% | 190 MB | 45.7 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,113 | 4,187 | 4,106 | 1.0% | 2,308 MB | 574.6 KB |  |
| hive-router | v0.3.6 | 2,736 | 2,744 | 2,702 | 0.6% | 167 MB | 62.6 KB |  |
| caliban | 3.2.0 | 1,473 | 1,478 | 1,470 | 0.2% | 11,059 MB | 7,687.7 KB |  |
| cosmo | 0.363.0 | 1,368 | 1,371 | 1,363 | 0.2% | 685 MB | 512.5 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 481 | 482 | 475 | 0.6% | 3,160 MB | 6,726.4 KB |  |
| hive-gateway | 2.15.3 | 247 | 251 | 246 | 0.8% | 4,080 MB | 16,916.2 KB |  |
| apollo-gateway | 2.14.4 | 237 | 238 | 235 | 0.5% | 2,443 MB | 10,554.6 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (3891 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (7561 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (165534 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 865560      ✗ 0     
     data_received..................: 25 GB   416 MB/s
     data_sent......................: 348 MB  5.7 MB/s
     http_req_blocked...............: avg=59.18µs  min=782ns    med=1.99µs  max=130.69ms p(90)=3.57µs   p(95)=4.69µs   p(99.9)=21.52ms 
     http_req_connecting............: avg=55.9µs   min=0s       med=0s      max=130.36ms p(90)=0s       p(95)=0s       p(99.9)=21.21ms 
     http_req_duration..............: avg=47.8ms   min=756.34µs med=40.25ms max=312.84ms p(90)=100.65ms p(95)=124.87ms p(99.9)=177.32ms
       { expected_response:true }...: avg=47.8ms   min=756.34µs med=40.25ms max=312.84ms p(90)=100.65ms p(95)=124.87ms p(99.9)=177.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 289520
     http_req_receiving.............: avg=362.15µs min=25.48µs  med=51.18µs max=221.09ms p(90)=210.49µs p(95)=363.03µs p(99.9)=53.59ms 
     http_req_sending...............: avg=149.85µs min=4.06µs   med=8.47µs  max=142.75ms p(90)=16.36µs  p(95)=114.91µs p(99.9)=28.44ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.29ms  min=702.36µs med=39.92ms max=312.47ms p(90)=99.29ms  p(95)=123.44ms p(99.9)=170.84ms
     http_reqs......................: 289520  4751.824613/s
     iteration_duration.............: avg=49.37ms  min=1.28ms   med=41.02ms max=322.11ms p(90)=103.96ms p(95)=129.79ms p(99.9)=194.37ms
     iterations.....................: 288520  4735.411845/s
     success_rate...................: 100.00% ✓ 288520      ✗ 0     
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

     checks.........................: 100.00% ✓ 850329      ✗ 0     
     data_received..................: 25 GB   408 MB/s
     data_sent......................: 342 MB  5.6 MB/s
     http_req_blocked...............: avg=59.9µs   min=771ns    med=2.14µs  max=112.93ms p(90)=3.82µs   p(95)=4.98µs   p(99.9)=20.21ms 
     http_req_connecting............: avg=56.38µs  min=0s       med=0s      max=112.83ms p(90)=0s       p(95)=0s       p(99.9)=19.52ms 
     http_req_duration..............: avg=48.09ms  min=759.95µs med=40.06ms max=327.41ms p(90)=101.9ms  p(95)=127.56ms p(99.9)=188.79ms
       { expected_response:true }...: avg=48.09ms  min=759.95µs med=40.06ms max=327.41ms p(90)=101.9ms  p(95)=127.56ms p(99.9)=188.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 284443
     http_req_receiving.............: avg=339.01µs min=25.91µs  med=51.66µs max=195.65ms p(90)=211.43µs p(95)=370.98µs p(99.9)=50.62ms 
     http_req_sending...............: avg=146.87µs min=4.11µs   med=8.59µs  max=124.3ms  p(90)=17.37µs  p(95)=119.46µs p(99.9)=26.15ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.61ms  min=706.03µs med=39.75ms max=278.06ms p(90)=100.74ms p(95)=126.36ms p(99.9)=179.42ms
     http_reqs......................: 284443  4666.418555/s
     iteration_duration.............: avg=50.25ms  min=1.24ms   med=41.21ms max=376.84ms p(90)=106.79ms p(95)=133.64ms p(99.9)=231.18ms
     iterations.....................: 283443  4650.013094/s
     success_rate...................: 100.00% ✓ 283443      ✗ 0     
     vus............................: 55      min=0         max=499 
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

     checks.........................: 100.00% ✓ 835035      ✗ 0     
     data_received..................: 24 GB   401 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=49.98µs  min=802ns    med=2.04µs  max=158.38ms p(90)=3.66µs   p(95)=4.81µs   p(99.9)=16.31ms 
     http_req_connecting............: avg=46.87µs  min=0s       med=0s      max=158.28ms p(90)=0s       p(95)=0s       p(99.9)=16.18ms 
     http_req_duration..............: avg=49.81ms  min=830.12µs med=41.85ms max=311.67ms p(90)=105.83ms p(95)=131.22ms p(99.9)=187.55ms
       { expected_response:true }...: avg=49.81ms  min=830.12µs med=41.85ms max=311.67ms p(90)=105.83ms p(95)=131.22ms p(99.9)=187.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 279345
     http_req_receiving.............: avg=300.15µs min=25.45µs  med=48.98µs max=113.7ms  p(90)=215.43µs p(95)=373.99µs p(99.9)=43.26ms 
     http_req_sending...............: avg=127.2µs  min=4µs      med=8.34µs  max=125.83ms p(90)=17.04µs  p(95)=120.86µs p(99.9)=22.59ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.38ms  min=790.26µs med=41.58ms max=297.85ms p(90)=104.93ms p(95)=130.17ms p(99.9)=182.01ms
     http_reqs......................: 279345  4577.308141/s
     iteration_duration.............: avg=51.18ms  min=1.39ms   med=42.65ms max=327.4ms  p(90)=108.74ms p(95)=134.85ms p(99.9)=207.56ms
     iterations.....................: 278345  4560.92228/s
     success_rate...................: 100.00% ✓ 278345      ✗ 0     
     vus............................: 58      min=0         max=498 
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

     checks.........................: 100.00% ✓ 828459      ✗ 0     
     data_received..................: 24 GB   397 MB/s
     data_sent......................: 333 MB  5.5 MB/s
     http_req_blocked...............: avg=56.61µs  min=812ns    med=2.38µs  max=126.73ms p(90)=4.07µs   p(95)=5.23µs   p(99.9)=19.81ms 
     http_req_connecting............: avg=52.87µs  min=0s       med=0s      max=119.36ms p(90)=0s       p(95)=0s       p(99.9)=19.45ms 
     http_req_duration..............: avg=50.13ms  min=826.17µs med=41.71ms max=315ms    p(90)=107.33ms p(95)=134.92ms p(99.9)=186.83ms
       { expected_response:true }...: avg=50.13ms  min=826.17µs med=41.71ms max=315ms    p(90)=107.33ms p(95)=134.92ms p(99.9)=186.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 277153
     http_req_receiving.............: avg=318.21µs min=24.09µs  med=50.29µs max=103.44ms p(90)=217.72µs p(95)=386.4µs  p(99.9)=42.43ms 
     http_req_sending...............: avg=130.41µs min=4.06µs   med=8.83µs  max=87.08ms  p(90)=18.06µs  p(95)=126.16µs p(99.9)=23.09ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.68ms  min=766.38µs med=41.45ms max=314.45ms p(90)=106.16ms p(95)=133.77ms p(99.9)=183.21ms
     http_reqs......................: 277153  4541.730038/s
     iteration_duration.............: avg=51.58ms  min=1.36ms   med=42.41ms max=339.13ms p(90)=110.31ms p(95)=139.31ms p(99.9)=204.5ms 
     iterations.....................: 276153  4525.342952/s
     success_rate...................: 100.00% ✓ 276153      ✗ 0     
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

     checks.........................: 100.00% ✓ 817920      ✗ 0     
     data_received..................: 24 GB   392 MB/s
     data_sent......................: 329 MB  5.4 MB/s
     http_req_blocked...............: avg=71.8µs   min=941ns    med=2.7µs   max=143.51ms p(90)=4.41µs   p(95)=5.7µs    p(99.9)=28.42ms 
     http_req_connecting............: avg=67.72µs  min=0s       med=0s      max=142.46ms p(90)=0s       p(95)=0s       p(99.9)=27.16ms 
     http_req_duration..............: avg=50.06ms  min=902.63µs med=41.99ms max=321.44ms p(90)=105.78ms p(95)=130.77ms p(99.9)=188.23ms
       { expected_response:true }...: avg=50.06ms  min=902.63µs med=41.99ms max=321.44ms p(90)=105.78ms p(95)=130.77ms p(99.9)=188.23ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 273640
     http_req_receiving.............: avg=348.88µs min=24.19µs  med=55.18µs max=147.61ms p(90)=222.11µs p(95)=385.42µs p(99.9)=47.44ms 
     http_req_sending...............: avg=158.9µs  min=4.15µs   med=9.28µs  max=212.32ms p(90)=18.81µs  p(95)=124.06µs p(99.9)=27.67ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.56ms  min=857.16µs med=41.62ms max=315.12ms p(90)=104.63ms p(95)=129.38ms p(99.9)=183.76ms
     http_reqs......................: 273640  4477.441701/s
     iteration_duration.............: avg=52.25ms  min=1.46ms   med=42.92ms max=337.68ms p(90)=110.72ms p(95)=138.25ms p(99.9)=223ms   
     iterations.....................: 272640  4461.079174/s
     success_rate...................: 100.00% ✓ 272640      ✗ 0     
     vus............................: 62      min=0         max=497 
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

     checks.........................: 100.00% ✓ 815316      ✗ 0     
     data_received..................: 24 GB   390 MB/s
     data_sent......................: 328 MB  5.4 MB/s
     http_req_blocked...............: avg=65.75µs  min=911ns    med=2.65µs  max=129.03ms p(90)=4.3µs    p(95)=5.49µs   p(99.9)=23.84ms 
     http_req_connecting............: avg=61.79µs  min=0s       med=0s      max=128.74ms p(90)=0s       p(95)=0s       p(99.9)=23.16ms 
     http_req_duration..............: avg=50.8ms   min=913.12µs med=42.36ms max=345.23ms p(90)=108.69ms p(95)=135.3ms  p(99.9)=196.1ms 
       { expected_response:true }...: avg=50.8ms   min=913.12µs med=42.36ms max=345.23ms p(90)=108.69ms p(95)=135.3ms  p(99.9)=196.1ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 272772
     http_req_receiving.............: avg=370.72µs min=22.08µs  med=54.56µs max=121.46ms p(90)=225.93µs p(95)=404.02µs p(99.9)=54.19ms 
     http_req_sending...............: avg=151.54µs min=4.32µs   med=9.05µs  max=166.41ms p(90)=18.4µs   p(95)=127.52µs p(99.9)=25.77ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.28ms  min=861.15µs med=42.03ms max=301.74ms p(90)=107.52ms p(95)=134.01ms p(99.9)=183.59ms
     http_reqs......................: 272772  4461.873339/s
     iteration_duration.............: avg=52.42ms  min=1.28ms   med=43.16ms max=354.57ms p(90)=112.26ms p(95)=140.59ms p(99.9)=214.81ms
     iterations.....................: 271772  4445.51582/s
     success_rate...................: 100.00% ✓ 271772      ✗ 0     
     vus............................: 62      min=0         max=497 
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

     checks.........................: 100.00% ✓ 799599      ✗ 0     
     data_received..................: 23 GB   383 MB/s
     data_sent......................: 321 MB  5.3 MB/s
     http_req_blocked...............: avg=56.51µs  min=782ns    med=2.4µs   max=143.44ms p(90)=4.27µs   p(95)=5.53µs   p(99.9)=19.09ms 
     http_req_connecting............: avg=52.92µs  min=0s       med=0s      max=143.39ms p(90)=0s       p(95)=0s       p(99.9)=18.89ms 
     http_req_duration..............: avg=52.01ms  min=978.35µs med=43.1ms  max=309.38ms p(90)=113.29ms p(95)=140.7ms  p(99.9)=198.91ms
       { expected_response:true }...: avg=52.01ms  min=978.35µs med=43.1ms  max=309.38ms p(90)=113.29ms p(95)=140.7ms  p(99.9)=198.91ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 267533
     http_req_receiving.............: avg=376.31µs min=25.64µs  med=51.34µs max=147.22ms p(90)=228.6µs  p(95)=405.72µs p(99.9)=61.92ms 
     http_req_sending...............: avg=136.59µs min=4.23µs   med=8.76µs  max=206.98ms p(90)=19.35µs  p(95)=133.45µs p(99.9)=23.94ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.49ms  min=933.29µs med=42.84ms max=299.23ms p(90)=112.01ms p(95)=139.08ms p(99.9)=193ms   
     http_reqs......................: 267533  4372.446698/s
     iteration_duration.............: avg=53.45ms  min=1.67ms   med=43.99ms max=319.22ms p(90)=115.93ms p(95)=144.41ms p(99.9)=223.55ms
     iterations.....................: 266533  4356.103119/s
     success_rate...................: 100.00% ✓ 266533      ✗ 0     
     vus............................: 65      min=0         max=496 
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

     checks.........................: 100.00% ✓ 778635      ✗ 0     
     data_received..................: 23 GB   373 MB/s
     data_sent......................: 313 MB  5.1 MB/s
     http_req_blocked...............: avg=51.08µs  min=962ns    med=2.6µs   max=111.93ms p(90)=4.31µs   p(95)=5.51µs   p(99.9)=18.37ms 
     http_req_connecting............: avg=47.07µs  min=0s       med=0s      max=111.7ms  p(90)=0s       p(95)=0s       p(99.9)=18.29ms 
     http_req_duration..............: avg=53.59ms  min=988.74µs med=44.84ms max=301.04ms p(90)=114.98ms p(95)=142.21ms p(99.9)=201.66ms
       { expected_response:true }...: avg=53.59ms  min=988.74µs med=44.84ms max=301.04ms p(90)=114.98ms p(95)=142.21ms p(99.9)=201.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 260545
     http_req_receiving.............: avg=327.16µs min=26.29µs  med=52.2µs  max=102.65ms p(90)=241.75µs p(95)=409.94µs p(99.9)=42.63ms 
     http_req_sending...............: avg=130.29µs min=4.2µs    med=9.19µs  max=173.52ms p(90)=18.98µs  p(95)=133.22µs p(99.9)=22.72ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.13ms  min=948.18µs med=44.59ms max=281.1ms  p(90)=114.01ms p(95)=141.18ms p(99.9)=193.98ms
     http_reqs......................: 260545  4257.398286/s
     iteration_duration.............: avg=54.89ms  min=1.55ms   med=45.7ms  max=346.44ms p(90)=117.43ms p(95)=145.27ms p(99.9)=228.1ms 
     iterations.....................: 259545  4241.057929/s
     success_rate...................: 100.00% ✓ 259545      ✗ 0     
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

     checks.........................: 100.00% ✓ 749160      ✗ 0     
     data_received..................: 22 GB   360 MB/s
     data_sent......................: 301 MB  4.9 MB/s
     http_req_blocked...............: avg=51.76µs  min=871ns    med=2.61µs  max=116.38ms p(90)=4.34µs   p(95)=5.47µs   p(99.9)=14.85ms 
     http_req_connecting............: avg=48.09µs  min=0s       med=0s      max=116.11ms p(90)=0s       p(95)=0s       p(99.9)=13.98ms 
     http_req_duration..............: avg=55.47ms  min=689.72µs med=46.21ms max=379.92ms p(90)=119.66ms p(95)=149.64ms p(99.9)=225.45ms
       { expected_response:true }...: avg=55.47ms  min=689.72µs med=46.21ms max=379.92ms p(90)=119.66ms p(95)=149.64ms p(99.9)=225.45ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 250720
     http_req_receiving.............: avg=296.9µs  min=25.26µs  med=52.7µs  max=95.68ms  p(90)=227.22µs p(95)=405.22µs p(99.9)=40.14ms 
     http_req_sending...............: avg=125.81µs min=4.23µs   med=9.48µs  max=154.2ms  p(90)=19.8µs   p(95)=135.93µs p(99.9)=22.53ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=55.05ms  min=655.45µs med=45.91ms max=336.49ms p(90)=118.7ms  p(95)=148.53ms p(99.9)=221.92ms
     http_reqs......................: 250720  4113.369758/s
     iteration_duration.............: avg=57.05ms  min=1.4ms    med=47.36ms max=432.25ms p(90)=123.19ms p(95)=153.81ms p(99.9)=241.94ms
     iterations.....................: 249720  4096.963529/s
     success_rate...................: 100.00% ✓ 249720      ✗ 0     
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

     checks.........................: 100.00% ✓ 502518      ✗ 0     
     data_received..................: 15 GB   239 MB/s
     data_sent......................: 202 MB  3.3 MB/s
     http_req_blocked...............: avg=16.54µs  min=881ns  med=2.34µs  max=54.45ms  p(90)=4.12µs   p(95)=5.4µs    p(99.9)=1.16ms  
     http_req_connecting............: avg=13.46µs  min=0s     med=0s      max=54.25ms  p(90)=0s       p(95)=0s       p(99.9)=1.08ms  
     http_req_duration..............: avg=84.34ms  min=1.31ms med=79.19ms max=254.92ms p(90)=164.05ms p(95)=178.63ms p(99.9)=226.82ms
       { expected_response:true }...: avg=84.34ms  min=1.31ms med=79.19ms max=254.92ms p(90)=164.05ms p(95)=178.63ms p(99.9)=226.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 168506
     http_req_receiving.............: avg=147.58µs min=27.6µs med=56.2µs  max=52.53ms  p(90)=179.84µs p(95)=364.65µs p(99.9)=14.24ms 
     http_req_sending...............: avg=68.98µs  min=4.1µs  med=10.23µs max=193.52ms p(90)=20.6µs   p(95)=125.59µs p(99.9)=9.02ms  
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=84.13ms  min=1.25ms med=78.99ms max=254.85ms p(90)=163.78ms p(95)=178.33ms p(99.9)=224.67ms
     http_reqs......................: 168506  2736.352262/s
     iteration_duration.............: avg=85.1ms   min=3.83ms med=80.1ms  max=360.15ms p(90)=164.5ms  p(95)=179.05ms p(99.9)=227.98ms
     iterations.....................: 167506  2720.11336/s
     success_rate...................: 100.00% ✓ 167506      ✗ 0     
     vus............................: 83      min=0         max=492 
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

     checks.........................: 100.00% ✓ 273300      ✗ 0    
     data_received..................: 8.1 GB  129 MB/s
     data_sent......................: 111 MB  1.8 MB/s
     http_req_blocked...............: avg=5.89µs   min=962ns   med=2.67µs   max=13.44ms  p(90)=4.75µs   p(95)=5.79µs   p(99.9)=373.26µs
     http_req_connecting............: avg=2.48µs   min=0s      med=0s       max=13.37ms  p(90)=0s       p(95)=0s       p(99.9)=216.59µs
     http_req_duration..............: avg=154.81ms min=2.02ms  med=125.92ms max=865.49ms p(90)=324.98ms p(95)=383ms    p(99.9)=647.59ms
       { expected_response:true }...: avg=154.81ms min=2.02ms  med=125.92ms max=865.49ms p(90)=324.98ms p(95)=383ms    p(99.9)=647.59ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 92100
     http_req_receiving.............: avg=80.59µs  min=28.42µs med=62.2µs   max=31.01ms  p(90)=103.31µs p(95)=123.09µs p(99.9)=2.32ms  
     http_req_sending...............: avg=36.21µs  min=5.04µs  med=12.23µs  max=91.25ms  p(90)=20.68µs  p(95)=24.86µs  p(99.9)=4.3ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=154.7ms  min=1.91ms  med=125.8ms  max=865.42ms p(90)=324.88ms p(95)=382.92ms p(99.9)=647.5ms 
     http_reqs......................: 92100   1473.95725/s
     iteration_duration.............: avg=156.76ms min=5.64ms  med=128.02ms max=865.66ms p(90)=326.17ms p(95)=384.33ms p(99.9)=647.91ms
     iterations.....................: 91100   1457.953371/s
     success_rate...................: 100.00% ✓ 91100       ✗ 0    
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

     checks.........................: 100.00% ✓ 253299      ✗ 0    
     data_received..................: 7.5 GB  120 MB/s
     data_sent......................: 103 MB  1.6 MB/s
     http_req_blocked...............: avg=4.64µs   min=871ns   med=2.33µs   max=11.17ms  p(90)=4.11µs   p(95)=5.06µs   p(99.9)=331.12µs
     http_req_connecting............: avg=1.68µs   min=0s      med=0s       max=11.1ms   p(90)=0s       p(95)=0s       p(99.9)=222.98µs
     http_req_duration..............: avg=166.92ms min=2.01ms  med=165.7ms  max=440.56ms p(90)=315.66ms p(95)=337.25ms p(99.9)=399.59ms
       { expected_response:true }...: avg=166.92ms min=2.01ms  med=165.7ms  max=440.56ms p(90)=315.66ms p(95)=337.25ms p(99.9)=399.59ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 85433
     http_req_receiving.............: avg=76.7µs   min=26.28µs med=60.76µs  max=102ms    p(90)=98.06µs  p(95)=113.09µs p(99.9)=1.38ms  
     http_req_sending...............: avg=29.03µs  min=4.72µs  med=10.68µs  max=103.81ms p(90)=17.51µs  p(95)=21.06µs  p(99.9)=3.1ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=166.82ms min=1.95ms  med=165.6ms  max=440.49ms p(90)=315.6ms  p(95)=337.17ms p(99.9)=399.48ms
     http_reqs......................: 85433   1368.067395/s
     iteration_duration.............: avg=169.12ms min=5.11ms  med=167.91ms max=440.77ms p(90)=316.35ms p(95)=337.89ms p(99.9)=400.09ms
     iterations.....................: 84433   1352.054058/s
     success_rate...................: 100.00% ✓ 84433       ✗ 0    
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

     checks.........................: 100.00% ✓ 90492      ✗ 0    
     data_received..................: 2.7 GB  42 MB/s
     data_sent......................: 37 MB   578 kB/s
     http_req_blocked...............: avg=8.73µs   min=1.08µs  med=2.4µs    max=15.39ms  p(90)=4.06µs   p(95)=4.96µs   p(99.9)=1.58ms  
     http_req_connecting............: avg=5.3µs    min=0s      med=0s       max=15.34ms  p(90)=0s       p(95)=0s       p(99.9)=1.48ms  
     http_req_duration..............: avg=461.07ms min=3.82ms  med=430.27ms max=2.09s    p(90)=916.53ms p(95)=998.75ms p(99.9)=1.46s   
       { expected_response:true }...: avg=461.07ms min=3.82ms  med=430.27ms max=2.09s    p(90)=916.53ms p(95)=998.75ms p(99.9)=1.46s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 31164
     http_req_receiving.............: avg=79.61µs  min=29.38µs med=68.04µs  max=97.55ms  p(90)=105.91µs p(95)=119.73µs p(99.9)=801.32µs
     http_req_sending...............: avg=32.64µs  min=5.29µs  med=12.32µs  max=106.87ms p(90)=19.02µs  p(95)=21.31µs  p(99.9)=2.65ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=460.96ms min=3.77ms  med=430.2ms  max=2.09s    p(90)=916.47ms p(95)=998.66ms p(99.9)=1.46s   
     http_reqs......................: 31164   481.842044/s
     iteration_duration.............: avg=476.56ms min=23.02ms med=450.02ms max=2.09s    p(90)=922.06ms p(95)=1s       p(99.9)=1.47s   
     iterations.....................: 30164   466.380549/s
     success_rate...................: 100.00% ✓ 30164      ✗ 0    
     vus............................: 88      min=0        max=500
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

     checks.........................: 100.00% ✓ 47010      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 20 MB   297 kB/s
     http_req_blocked...............: avg=11.92µs  min=1.12µs  med=3.3µs    max=22.76ms p(90)=5.01µs   p(95)=6.6µs    p(99.9)=993.24µs
     http_req_connecting............: avg=6.96µs   min=0s      med=0s       max=22.66ms p(90)=0s       p(95)=0s       p(99.9)=945.21µs
     http_req_duration..............: avg=872.91ms min=5.65ms  med=789.33ms max=4.5s    p(90)=1.73s    p(95)=2s       p(99.9)=3.84s   
       { expected_response:true }...: avg=872.91ms min=5.65ms  med=789.33ms max=4.5s    p(90)=1.73s    p(95)=2s       p(99.9)=3.84s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16670
     http_req_receiving.............: avg=101.63µs min=31.33µs med=89.7µs   max=34.07ms p(90)=128.35µs p(95)=142.99µs p(99.9)=1.86ms  
     http_req_sending...............: avg=34.66µs  min=5.64µs  med=17.48µs  max=46.26ms p(90)=22.51µs  p(95)=26.3µs   p(99.9)=3.08ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=872.77ms min=5.56ms  med=789.22ms max=4.5s    p(90)=1.73s    p(95)=2s       p(99.9)=3.84s   
     http_reqs......................: 16670   247.213525/s
     iteration_duration.............: avg=928.62ms min=48.46ms med=849.54ms max=4.5s    p(90)=1.75s    p(95)=2.02s    p(99.9)=3.89s   
     iterations.....................: 15670   232.383679/s
     success_rate...................: 100.00% ✓ 15670      ✗ 0    
     vus............................: 79      min=0        max=500
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

     checks.........................: 100.00% ✓ 45720      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   285 kB/s
     http_req_blocked...............: avg=15.4µs   min=1.31µs  med=3.58µs   max=15.07ms p(90)=5.33µs   p(95)=6.81µs  p(99.9)=2.47ms  
     http_req_connecting............: avg=9.96µs   min=0s      med=0s       max=15ms    p(90)=0s       p(95)=0s      p(99.9)=2.45ms  
     http_req_duration..............: avg=893.8ms  min=7.5ms   med=804.56ms max=3.02s   p(90)=1.83s    p(95)=1.94s   p(99.9)=2.71s   
       { expected_response:true }...: avg=893.8ms  min=7.5ms   med=804.56ms max=3.02s   p(90)=1.83s    p(95)=1.94s   p(99.9)=2.71s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16240
     http_req_receiving.............: avg=92.84µs  min=35.46µs med=86.42µs  max=6.07ms  p(90)=123.87µs p(95)=139µs   p(99.9)=812.65µs
     http_req_sending...............: avg=42.88µs  min=5.74µs  med=17.08µs  max=98.56ms p(90)=22.57µs  p(95)=26.15µs p(99.9)=4.99ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=893.67ms min=7.42ms  med=804.47ms max=3.02s   p(90)=1.83s    p(95)=1.94s   p(99.9)=2.71s   
     http_reqs......................: 16240   237.01959/s
     iteration_duration.............: avg=952.42ms min=45.17ms med=881.91ms max=3.03s   p(90)=1.84s    p(95)=1.95s   p(99.9)=2.73s   
     iterations.....................: 15240   222.424788/s
     success_rate...................: 100.00% ✓ 15240      ✗ 0    
     vus............................: 81      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

