## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-aot-11 | 16.8.0-p.15 | 4,763 | 4,780 | 4,731 | 0.4% | 158 MB | 33.9 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.15 | 4,739 | 4,812 | 4,692 | 1.0% | 388 MB | 83.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.15 | 4,712 | 4,717 | 4,680 | 0.4% | 432 MB | 93.8 KB |  |
| fusion-net-11 | 16.7.5 | 4,694 | 4,699 | 4,500 | 1.9% | 412 MB | 89.9 KB |  |
| feddi-gateway | 2026-11-03-0517 | 4,597 | 4,601 | 4,576 | 0.2% | 2,284 MB | 508.8 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.15 | 4,592 | 4,714 | 4,571 | 1.3% | 159 MB | 35.5 KB |  |
| fusion-fed-net-11 | 16.7.5 | 4,545 | 4,565 | 4,542 | 0.2% | 416 MB | 93.7 KB |  |
| fusion-aot-11 | 16.7.5 | 4,458 | 4,576 | 4,405 | 1.4% | 160 MB | 36.7 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 4,215 | 4,233 | 4,203 | 0.3% | 171 MB | 41.5 KB |  |
| hive-router | v0.3.13 | 2,678 | 2,697 | 2,670 | 0.4% | 176 MB | 67.4 KB |  |
| caliban | 3.2.1 | 1,440 | 1,441 | 1,424 | 0.5% | 11,117 MB | 7,905.3 KB |  |
| cosmo | 0.372.0 | 1,365 | 1,368 | 1,363 | 0.1% | 672 MB | 503.8 KB |  |
| hive-gateway-router-runtime | 2.15.8 | 559 | 561 | 551 | 0.7% | 3,011 MB | 5,516.3 KB |  |
| hive-gateway | 2.15.8 | 267 | 267 | 263 | 0.7% | 3,602 MB | 13,815.0 KB |  |
| apollo-gateway | 2.14.4 | 239 | 239 | 238 | 0.2% | 2,422 MB | 10,375.1 KB |  |
| apollo-router | v2.19.1 | — | — | — | — | — | — | non-compatible response (15292 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (5231 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (153823 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 868236      ✗ 0     
     data_received..................: 25 GB   417 MB/s
     data_sent......................: 349 MB  5.7 MB/s
     http_req_blocked...............: avg=59.87µs  min=821ns    med=2.06µs  max=124.92ms p(90)=3.65µs   p(95)=4.73µs   p(99.9)=21.14ms 
     http_req_connecting............: avg=56.88µs  min=0s       med=0s      max=124.86ms p(90)=0s       p(95)=0s       p(99.9)=20.42ms 
     http_req_duration..............: avg=47.71ms  min=778.93µs med=39.81ms max=309.56ms p(90)=101.78ms p(95)=126.72ms p(99.9)=178.68ms
       { expected_response:true }...: avg=47.71ms  min=778.93µs med=39.81ms max=309.56ms p(90)=101.78ms p(95)=126.72ms p(99.9)=178.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 290412
     http_req_receiving.............: avg=325.44µs min=25.1µs   med=50.85µs max=146.15ms p(90)=209.06µs p(95)=369.9µs  p(99.9)=43.14ms 
     http_req_sending...............: avg=143.6µs  min=4.06µs   med=8.48µs  max=120.67ms p(90)=16.65µs  p(95)=118.05µs p(99.9)=25.53ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.24ms  min=742.63µs med=39.51ms max=309.1ms  p(90)=100.66ms p(95)=125.48ms p(99.9)=174.4ms 
     http_reqs......................: 290412  4763.187548/s
     iteration_duration.............: avg=49.22ms  min=1.28ms   med=40.53ms max=384.67ms p(90)=105.24ms p(95)=131.66ms p(99.9)=197.34ms
     iterations.....................: 289412  4746.786065/s
     success_rate...................: 100.00% ✓ 289412      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 863313      ✗ 0     
     data_received..................: 25 GB   415 MB/s
     data_sent......................: 347 MB  5.7 MB/s
     http_req_blocked...............: avg=66.72µs  min=831ns    med=2.36µs  max=171.63ms p(90)=3.9µs    p(95)=4.96µs   p(99.9)=24.92ms 
     http_req_connecting............: avg=62.82µs  min=0s       med=0s      max=171.55ms p(90)=0s       p(95)=0s       p(99.9)=24.29ms 
     http_req_duration..............: avg=47.33ms  min=730.97µs med=39.91ms max=323.35ms p(90)=100.25ms p(95)=124.65ms p(99.9)=182.39ms
       { expected_response:true }...: avg=47.33ms  min=730.97µs med=39.91ms max=323.35ms p(90)=100.25ms p(95)=124.65ms p(99.9)=182.39ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288771
     http_req_receiving.............: avg=360.16µs min=23.94µs  med=52.26µs max=115.39ms p(90)=210.92µs p(95)=371.62µs p(99.9)=48.42ms 
     http_req_sending...............: avg=156.96µs min=3.93µs   med=8.89µs  max=215.24ms p(90)=16.86µs  p(95)=118.38µs p(99.9)=27.08ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.81ms  min=693.14µs med=39.55ms max=300.57ms p(90)=99.01ms  p(95)=123.31ms p(99.9)=178.13ms
     http_reqs......................: 288771  4739.427379/s
     iteration_duration.............: avg=49.5ms   min=1.06ms   med=40.95ms max=362.65ms p(90)=105.48ms p(95)=131.77ms p(99.9)=211.32ms
     iterations.....................: 287771  4723.014972/s
     success_rate...................: 100.00% ✓ 287771      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 858759      ✗ 0     
     data_received..................: 25 GB   412 MB/s
     data_sent......................: 345 MB  5.7 MB/s
     http_req_blocked...............: avg=76.94µs  min=822ns    med=2.55µs  max=166.52ms p(90)=4.11µs   p(95)=5.29µs   p(99.9)=33.28ms 
     http_req_connecting............: avg=73µs     min=0s       med=0s      max=136.77ms p(90)=0s       p(95)=0s       p(99.9)=32.91ms 
     http_req_duration..............: avg=47.64ms  min=754µs    med=40.49ms max=271.76ms p(90)=99.41ms  p(95)=123.19ms p(99.9)=184.17ms
       { expected_response:true }...: avg=47.64ms  min=754µs    med=40.49ms max=271.76ms p(90)=99.41ms  p(95)=123.19ms p(99.9)=184.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 287253
     http_req_receiving.............: avg=388.28µs min=26.06µs  med=54.19µs max=126.01ms p(90)=204.95µs p(95)=366.07µs p(99.9)=58.05ms 
     http_req_sending...............: avg=172.49µs min=4.13µs   med=9.22µs  max=184.63ms p(90)=17.44µs  p(95)=118.47µs p(99.9)=30.92ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.08ms  min=717.08µs med=40.11ms max=264.94ms p(90)=98.19ms  p(95)=121.59ms p(99.9)=175.36ms
     http_reqs......................: 287253  4712.923839/s
     iteration_duration.............: avg=49.76ms  min=1.15ms   med=41.39ms max=361.09ms p(90)=105.31ms p(95)=130.99ms p(99.9)=209.38ms
     iterations.....................: 286253  4696.516965/s
     success_rate...................: 100.00% ✓ 286253      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 855678      ✗ 0     
     data_received..................: 25 GB   411 MB/s
     data_sent......................: 344 MB  5.6 MB/s
     http_req_blocked...............: avg=61.69µs  min=822ns    med=2.09µs  max=121.23ms p(90)=3.71µs   p(95)=4.87µs   p(99.9)=21.34ms 
     http_req_connecting............: avg=57.94µs  min=0s       med=0s      max=121.1ms  p(90)=0s       p(95)=0s       p(99.9)=20.88ms 
     http_req_duration..............: avg=48.26ms  min=762.67µs med=41.13ms max=308.25ms p(90)=101.43ms p(95)=125.19ms p(99.9)=176.02ms
       { expected_response:true }...: avg=48.26ms  min=762.67µs med=41.13ms max=308.25ms p(90)=101.43ms p(95)=125.19ms p(99.9)=176.02ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 286226
     http_req_receiving.............: avg=321.71µs min=25.56µs  med=51.68µs max=124.4ms  p(90)=209.48µs p(95)=363.61µs p(99.9)=41.58ms 
     http_req_sending...............: avg=145µs    min=4.05µs   med=8.55µs  max=175.14ms p(90)=16.9µs   p(95)=116.48µs p(99.9)=25.3ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.8ms   min=725.14µs med=40.81ms max=307.71ms p(90)=100.36ms p(95)=124.05ms p(99.9)=171.65ms
     http_reqs......................: 286226  4694.836291/s
     iteration_duration.............: avg=49.94ms  min=1.27ms   med=41.78ms max=359.46ms p(90)=105.28ms p(95)=131.59ms p(99.9)=208.62ms
     iterations.....................: 285226  4678.433741/s
     success_rate...................: 100.00% ✓ 285226      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-11-03-0517)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 836427      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=53.28µs  min=811ns    med=2.06µs  max=120.25ms p(90)=3.66µs   p(95)=4.69µs   p(99.9)=18.67ms 
     http_req_connecting............: avg=50.21µs  min=0s       med=0s      max=108.18ms p(90)=0s       p(95)=0s       p(99.9)=18.38ms 
     http_req_duration..............: avg=49.83ms  min=661.71µs med=41.78ms max=262.48ms p(90)=106.59ms p(95)=132.33ms p(99.9)=201.61ms
       { expected_response:true }...: avg=49.83ms  min=661.71µs med=41.78ms max=262.48ms p(90)=106.59ms p(95)=132.33ms p(99.9)=201.61ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 279809
     http_req_receiving.............: avg=290.67µs min=25.99µs  med=50.64µs max=110.77ms p(90)=203.66µs p(95)=370.06µs p(99.9)=41.75ms 
     http_req_sending...............: avg=125.9µs  min=4.07µs   med=8.61µs  max=181.63ms p(90)=16.68µs  p(95)=119.78µs p(99.9)=22.18ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.41ms  min=612.77µs med=41.51ms max=261.9ms  p(90)=105.74ms p(95)=131.47ms p(99.9)=192.87ms
     http_reqs......................: 279809  4597.240668/s
     iteration_duration.............: avg=51.09ms  min=1.05ms   med=42.43ms max=348.29ms p(90)=109.2ms  p(95)=135.8ms  p(99.9)=220.01ms
     iterations.....................: 278809  4580.810744/s
     success_rate...................: 100.00% ✓ 278809      ✗ 0     
     vus............................: 52      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 837129      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=72.52µs  min=1µs      med=2.66µs  max=190.97ms p(90)=4.24µs   p(95)=5.41µs   p(99.9)=26.23ms 
     http_req_connecting............: avg=68.51µs  min=0s       med=0s      max=190.85ms p(90)=0s       p(95)=0s       p(99.9)=26.05ms 
     http_req_duration..............: avg=49.17ms  min=790.22µs med=41.29ms max=270.46ms p(90)=104.09ms p(95)=130.8ms  p(99.9)=186.62ms
       { expected_response:true }...: avg=49.17ms  min=790.22µs med=41.29ms max=270.46ms p(90)=104.09ms p(95)=130.8ms  p(99.9)=186.62ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280043
     http_req_receiving.............: avg=343.59µs min=26.19µs  med=54.33µs max=167.12ms p(90)=221.45µs p(95)=385.05µs p(99.9)=45.12ms 
     http_req_sending...............: avg=157.63µs min=4.38µs   med=9.48µs  max=102.53ms p(90)=17.78µs  p(95)=124.19µs p(99.9)=27.16ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.67ms  min=753.15µs med=40.94ms max=267.43ms p(90)=102.84ms p(95)=129.59ms p(99.9)=182.03ms
     http_reqs......................: 280043  4592.05723/s
     iteration_duration.............: avg=51.05ms  min=1.19ms   med=42.11ms max=319.53ms p(90)=108.89ms p(95)=137.72ms p(99.9)=211.74ms
     iterations.....................: 279043  4575.659543/s
     success_rate...................: 100.00% ✓ 279043      ✗ 0     
     vus............................: 56      min=0         max=499 
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

     checks.........................: 100.00% ✓ 830496      ✗ 0     
     data_received..................: 24 GB   398 MB/s
     data_sent......................: 334 MB  5.5 MB/s
     http_req_blocked...............: avg=60.31µs  min=832ns    med=2.09µs  max=141.82ms p(90)=3.74µs   p(95)=4.89µs   p(99.9)=20.89ms 
     http_req_connecting............: avg=56.83µs  min=0s       med=0s      max=139.04ms p(90)=0s       p(95)=0s       p(99.9)=20.76ms 
     http_req_duration..............: avg=49.92ms  min=915.16µs med=42.27ms max=302.53ms p(90)=105.81ms p(95)=130.42ms p(99.9)=181.93ms
       { expected_response:true }...: avg=49.92ms  min=915.16µs med=42.27ms max=302.53ms p(90)=105.81ms p(95)=130.42ms p(99.9)=181.93ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 277832
     http_req_receiving.............: avg=299.44µs min=24.85µs  med=52.62µs max=107.73ms p(90)=216.73µs p(95)=374.26µs p(99.9)=40.42ms 
     http_req_sending...............: avg=142.7µs  min=4.09µs   med=8.8µs   max=246.56ms p(90)=18.28µs  p(95)=121.65µs p(99.9)=25.21ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.48ms  min=869.62µs med=41.96ms max=301.82ms p(90)=104.84ms p(95)=129.34ms p(99.9)=176.38ms
     http_reqs......................: 277832  4545.29411/s
     iteration_duration.............: avg=51.45ms  min=1.46ms   med=43.05ms max=328.23ms p(90)=108.99ms p(95)=134.83ms p(99.9)=203.87ms
     iterations.....................: 276832  4528.934245/s
     success_rate...................: 100.00% ✓ 276832      ✗ 0     
     vus............................: 63      min=0         max=496 
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

     checks.........................: 100.00% ✓ 813405      ✗ 0     
     data_received..................: 24 GB   390 MB/s
     data_sent......................: 327 MB  5.4 MB/s
     http_req_blocked...............: avg=63.08µs  min=992ns    med=2.51µs  max=126.81ms p(90)=4.26µs   p(95)=5.48µs   p(99.9)=22.69ms 
     http_req_connecting............: avg=59.39µs  min=0s       med=0s      max=126.62ms p(90)=0s       p(95)=0s       p(99.9)=22.63ms 
     http_req_duration..............: avg=51.08ms  min=846.06µs med=42.7ms  max=321.12ms p(90)=109.82ms p(95)=136.91ms p(99.9)=187.9ms 
       { expected_response:true }...: avg=51.08ms  min=846.06µs med=42.7ms  max=321.12ms p(90)=109.82ms p(95)=136.91ms p(99.9)=187.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 272135
     http_req_receiving.............: avg=331.37µs min=22.49µs  med=51.65µs max=211.5ms  p(90)=232.34µs p(95)=407.92µs p(99.9)=41.77ms 
     http_req_sending...............: avg=146.97µs min=4.2µs    med=9.05µs  max=178.83ms p(90)=18.95µs  p(95)=130.5µs  p(99.9)=26.24ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.6ms   min=803.64µs med=42.37ms max=320.61ms p(90)=108.65ms p(95)=135.8ms  p(99.9)=183.66ms
     http_reqs......................: 272135  4458.712368/s
     iteration_duration.............: avg=52.54ms  min=1.4ms    med=43.47ms max=341.91ms p(90)=112.83ms p(95)=140.97ms p(99.9)=212.33ms
     iterations.....................: 271135  4442.328175/s
     success_rate...................: 100.00% ✓ 271135      ✗ 0     
     vus............................: 59      min=0         max=498 
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

     checks.........................: 100.00% ✓ 770931      ✗ 0     
     data_received..................: 23 GB   369 MB/s
     data_sent......................: 310 MB  5.1 MB/s
     http_req_blocked...............: avg=48.81µs  min=992ns    med=2.62µs  max=94.63ms  p(90)=4.31µs   p(95)=5.5µs    p(99.9)=15.49ms 
     http_req_connecting............: avg=44.92µs  min=0s       med=0s      max=94.55ms  p(90)=0s       p(95)=0s       p(99.9)=15.17ms 
     http_req_duration..............: avg=54.06ms  min=987.19µs med=45.24ms max=308.38ms p(90)=115.92ms p(95)=143.73ms p(99.9)=205.34ms
       { expected_response:true }...: avg=54.06ms  min=987.19µs med=45.24ms max=308.38ms p(90)=115.92ms p(95)=143.73ms p(99.9)=205.34ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 257977
     http_req_receiving.............: avg=306.08µs min=25.7µs   med=52.11µs max=123.68ms p(90)=245.77µs p(95)=414.02µs p(99.9)=40.91ms 
     http_req_sending...............: avg=133.77µs min=4.18µs   med=9.17µs  max=228.85ms p(90)=19.18µs  p(95)=134.3µs  p(99.9)=24.19ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.62ms  min=937.23µs med=44.96ms max=281.59ms p(90)=115.04ms p(95)=142.83ms p(99.9)=198.95ms
     http_reqs......................: 257977  4215.471821/s
     iteration_duration.............: avg=55.44ms  min=1.71ms   med=46.21ms max=324.12ms p(90)=118.68ms p(95)=146.61ms p(99.9)=234.32ms
     iterations.....................: 256977  4199.131326/s
     success_rate...................: 100.00% ✓ 256977      ✗ 0     
     vus............................: 66      min=0         max=496 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.13)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 490635      ✗ 0     
     data_received..................: 14 GB   234 MB/s
     data_sent......................: 198 MB  3.2 MB/s
     http_req_blocked...............: avg=13.16µs  min=882ns   med=2.26µs  max=49.36ms  p(90)=3.82µs   p(95)=5µs      p(99.9)=613.72µs
     http_req_connecting............: avg=10.16µs  min=0s      med=0s      max=49.26ms  p(90)=0s       p(95)=0s       p(99.9)=512.77µs
     http_req_duration..............: avg=86.39ms  min=1.17ms  med=80.88ms max=262.79ms p(90)=167.86ms p(95)=181.96ms p(99.9)=225.14ms
       { expected_response:true }...: avg=86.39ms  min=1.17ms  med=80.88ms max=262.79ms p(90)=167.86ms p(95)=181.96ms p(99.9)=225.14ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 164545
     http_req_receiving.............: avg=126.02µs min=26.98µs med=55.37µs max=36.11ms  p(90)=155.76µs p(95)=347.06µs p(99.9)=10.44ms 
     http_req_sending...............: avg=64.22µs  min=4.51µs  med=9.95µs  max=148.44ms p(90)=19.88µs  p(95)=121.33µs p(99.9)=8.29ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=86.2ms   min=1.12ms  med=80.68ms max=262.59ms p(90)=167.6ms  p(95)=181.7ms  p(99.9)=224.7ms 
     http_reqs......................: 164545  2678.707857/s
     iteration_duration.............: avg=87.17ms  min=3.08ms  med=81.73ms max=362.43ms p(90)=168.28ms p(95)=182.33ms p(99.9)=226.28ms
     iterations.....................: 163545  2662.428372/s
     success_rate...................: 100.00% ✓ 163545      ✗ 0     
     vus............................: 75      min=0         max=493 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: caliban (HotChocolate subgraphs) (3.2.1)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 266250      ✗ 0    
     data_received..................: 7.8 GB  126 MB/s
     data_sent......................: 108 MB  1.7 MB/s
     http_req_blocked...............: avg=11.17µs  min=982ns   med=2.57µs   max=45.67ms  p(90)=4.49µs   p(95)=5.54µs   p(99.9)=403.13µs
     http_req_connecting............: avg=7.91µs   min=0s      med=0s       max=45.58ms  p(90)=0s       p(95)=0s       p(99.9)=343.34µs
     http_req_duration..............: avg=158.95ms min=1.93ms  med=127.54ms max=1.03s    p(90)=335.85ms p(95)=410.77ms p(99.9)=751.64ms
       { expected_response:true }...: avg=158.95ms min=1.93ms  med=127.54ms max=1.03s    p(90)=335.85ms p(95)=410.77ms p(99.9)=751.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 89750
     http_req_receiving.............: avg=77.53µs  min=26.29µs med=60.48µs  max=115.35ms p(90)=98.57µs  p(95)=116.24µs p(99.9)=1.86ms  
     http_req_sending...............: avg=32.62µs  min=4.96µs  med=11.25µs  max=121.94ms p(90)=18.54µs  p(95)=22.47µs  p(99.9)=3.83ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=158.84ms min=1.87ms  med=127.43ms max=1.03s    p(90)=335.75ms p(95)=410.68ms p(99.9)=751.57ms
     http_reqs......................: 89750   1440.835753/s
     iteration_duration.............: avg=160.99ms min=6.49ms  med=129.82ms max=1.03s    p(90)=337.4ms  p(95)=412.14ms p(99.9)=753.25ms
     iterations.....................: 88750   1424.781873/s
     success_rate...................: 100.00% ✓ 88750       ✗ 0    
     vus............................: 69      min=0         max=495
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.372.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 252687      ✗ 0    
     data_received..................: 7.5 GB  120 MB/s
     data_sent......................: 102 MB  1.6 MB/s
     http_req_blocked...............: avg=5.47µs   min=971ns   med=2.21µs   max=27.13ms  p(90)=3.86µs   p(95)=4.79µs   p(99.9)=449.12µs
     http_req_connecting............: avg=2.62µs   min=0s      med=0s       max=26.97ms  p(90)=0s       p(95)=0s       p(99.9)=357.98µs
     http_req_duration..............: avg=167.32ms min=1.96ms  med=164.64ms max=505.69ms p(90)=317.12ms p(95)=341.65ms p(99.9)=433.43ms
       { expected_response:true }...: avg=167.32ms min=1.96ms  med=164.64ms max=505.69ms p(90)=317.12ms p(95)=341.65ms p(99.9)=433.43ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 85229
     http_req_receiving.............: avg=75.12µs  min=26.37µs med=58.52µs  max=206.2ms  p(90)=95.94µs  p(95)=111.58µs p(99.9)=1.26ms  
     http_req_sending...............: avg=29.25µs  min=4.87µs  med=10.46µs  max=224.88ms p(90)=16.91µs  p(95)=20.45µs  p(99.9)=3.27ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=167.21ms min=1.91ms  med=164.56ms max=505.61ms p(90)=317.04ms p(95)=341.54ms p(99.9)=433.38ms
     http_reqs......................: 85229   1365.972459/s
     iteration_duration.............: avg=169.54ms min=4.24ms  med=167.18ms max=505.88ms p(90)=317.98ms p(95)=342.29ms p(99.9)=433.87ms
     iterations.....................: 84229   1349.945373/s
     success_rate...................: 100.00% ✓ 84229       ✗ 0    
     vus............................: 76      min=0         max=494
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 104625     ✗ 0    
     data_received..................: 3.1 GB  49 MB/s
     data_sent......................: 43 MB   672 kB/s
     http_req_blocked...............: avg=7.64µs   min=1.07µs  med=3.2µs    max=13.92ms p(90)=4.97µs   p(95)=6.03µs   p(99.9)=601.86µs
     http_req_connecting............: avg=3.38µs   min=0s      med=0s       max=13.86ms p(90)=0s       p(95)=0s       p(99.9)=551.04µs
     http_req_duration..............: avg=399.88ms min=3.4ms   med=367.63ms max=1.64s   p(90)=791.24ms p(95)=863.31ms p(99.9)=1.29s   
       { expected_response:true }...: avg=399.88ms min=3.4ms   med=367.63ms max=1.64s   p(90)=791.24ms p(95)=863.31ms p(99.9)=1.29s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 35875
     http_req_receiving.............: avg=86.63µs  min=29.21µs med=71.85µs  max=64.45ms p(90)=109.73µs p(95)=124.61µs p(99.9)=1.37ms  
     http_req_sending...............: avg=37.5µs   min=5.19µs  med=14.7µs   max=131.7ms p(90)=21.47µs  p(95)=24.26µs  p(99.9)=3.09ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=399.76ms min=3.34ms  med=367.55ms max=1.64s   p(90)=791.16ms p(95)=863.19ms p(99.9)=1.29s   
     http_reqs......................: 35875   559.385856/s
     iteration_duration.............: avg=411.57ms min=25.28ms med=383.24ms max=1.65s   p(90)=794.58ms p(95)=866.85ms p(99.9)=1.29s   
     iterations.....................: 34875   543.793219/s
     success_rate...................: 100.00% ✓ 34875      ✗ 0    
     vus............................: 63      min=0        max=497
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 51060      ✗ 0    
     data_received..................: 1.6 GB  24 MB/s
     data_sent......................: 22 MB   322 kB/s
     http_req_blocked...............: avg=14.39µs  min=1.43µs  med=3.37µs   max=18.39ms  p(90)=5.11µs   p(95)=6.5µs    p(99.9)=2.28ms
     http_req_connecting............: avg=9.43µs   min=0s      med=0s       max=18.24ms  p(90)=0s       p(95)=0s       p(99.9)=2.26ms
     http_req_duration..............: avg=804.52ms min=5.3ms   med=717.46ms max=3.76s    p(90)=1.61s    p(95)=1.88s    p(99.9)=3.04s 
       { expected_response:true }...: avg=804.52ms min=5.3ms   med=717.46ms max=3.76s    p(90)=1.61s    p(95)=1.88s    p(99.9)=3.04s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 18020
     http_req_receiving.............: avg=100.82µs min=33.58µs med=83.79µs  max=116.55ms p(90)=123.27µs p(95)=138.76µs p(99.9)=1.22ms
     http_req_sending...............: avg=36.48µs  min=5.88µs  med=16.08µs  max=122.71ms p(90)=21.75µs  p(95)=24.92µs  p(99.9)=2.66ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=804.38ms min=5.22ms  med=717.34ms max=3.76s    p(90)=1.61s    p(95)=1.88s    p(99.9)=3.04s 
     http_reqs......................: 18020   267.94003/s
     iteration_duration.............: avg=851.9ms  min=33.16ms med=773.79ms max=3.76s    p(90)=1.64s    p(95)=1.9s     p(99.9)=3.06s 
     iterations.....................: 17020   253.070994/s
     success_rate...................: 100.00% ✓ 17020      ✗ 0    
     vus............................: 67      min=0        max=499
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

     checks.........................: 100.00% ✓ 46191      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   287 kB/s
     http_req_blocked...............: avg=12.27µs  min=1.15µs  med=3.07µs   max=13.36ms p(90)=4.74µs   p(95)=6.24µs   p(99.9)=1.55ms  
     http_req_connecting............: avg=7.61µs   min=0s      med=0s       max=13.28ms p(90)=0s       p(95)=0s       p(99.9)=1.52ms  
     http_req_duration..............: avg=886.04ms min=7.59ms  med=825.06ms max=3.02s   p(90)=1.79s    p(95)=1.91s    p(99.9)=2.64s   
       { expected_response:true }...: avg=886.04ms min=7.59ms  med=825.06ms max=3.02s   p(90)=1.79s    p(95)=1.91s    p(99.9)=2.64s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16397
     http_req_receiving.............: avg=108.73µs min=32.05µs med=87.27µs  max=79.5ms  p(90)=125.05µs p(95)=141.45µs p(99.9)=864.07µs
     http_req_sending...............: avg=40.7µs   min=5.14µs  med=16.22µs  max=95.5ms  p(90)=21.1µs   p(95)=24.36µs  p(99.9)=4.21ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=885.89ms min=7.51ms  med=824.75ms max=3.02s   p(90)=1.79s    p(95)=1.91s    p(99.9)=2.64s   
     http_reqs......................: 16397   239.2728/s
     iteration_duration.............: avg=943.54ms min=44.91ms med=882.36ms max=3.02s   p(90)=1.81s    p(95)=1.92s    p(99.9)=2.66s   
     iterations.....................: 15397   224.680325/s
     success_rate...................: 100.00% ✓ 15397      ✗ 0    
     vus............................: 85      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

