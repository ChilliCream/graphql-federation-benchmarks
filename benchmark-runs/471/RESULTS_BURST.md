## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 4,713 | 4,747 | 4,693 | 0.5% | 417 MB | 90.7 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 4,602 | 4,617 | 4,574 | 0.4% | 416 MB | 92.5 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,588 | 4,616 | 4,581 | 0.3% | 416 MB | 92.9 KB |  |
| fusion-aot-11 | 16.7.3 | 4,482 | 4,522 | 4,420 | 0.9% | 163 MB | 37.2 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,481 | 4,511 | 4,469 | 0.4% | 414 MB | 94.7 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,397 | 4,402 | 4,390 | 0.1% | 161 MB | 37.5 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,325 | 4,383 | 4,308 | 0.7% | 180 MB | 42.6 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,304 | 4,324 | 4,278 | 0.4% | 158 MB | 37.6 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,180 | 4,238 | 4,022 | 2.0% | 2,293 MB | 561.8 KB |  |
| hive-router | v0.3.10 | 2,587 | 2,591 | 2,581 | 0.2% | 168 MB | 66.4 KB |  |
| caliban | 3.2.0 | 1,364 | 1,366 | 1,363 | 0.1% | 10,927 MB | 8,203.6 KB |  |
| cosmo | 0.365.2 | 1,290 | 1,293 | 1,289 | 0.1% | 575 MB | 456.8 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 486 | 487 | 480 | 0.6% | 3,161 MB | 6,659.9 KB |  |
| hive-gateway | 2.15.6 | 245 | 247 | 242 | 0.9% | 4,035 MB | 16,862.8 KB |  |
| apollo-gateway | 2.14.4 | 241 | 242 | 240 | 0.3% | 2,458 MB | 10,445.6 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (4484 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (8814 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (207285 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 859020      ✗ 0     
     data_received..................: 25 GB   412 MB/s
     data_sent......................: 345 MB  5.7 MB/s
     http_req_blocked...............: avg=57.51µs  min=841ns    med=2.03µs  max=125.52ms p(90)=3.57µs   p(95)=4.62µs   p(99.9)=20.33ms 
     http_req_connecting............: avg=54.15µs  min=0s       med=0s      max=125.46ms p(90)=0s       p(95)=0s       p(99.9)=19.98ms 
     http_req_duration..............: avg=48.14ms  min=764.36µs med=40.55ms max=290.42ms p(90)=101.35ms p(95)=125.31ms p(99.9)=176.1ms 
       { expected_response:true }...: avg=48.14ms  min=764.36µs med=40.55ms max=290.42ms p(90)=101.35ms p(95)=125.31ms p(99.9)=176.1ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 287340
     http_req_receiving.............: avg=301.1µs  min=22.17µs  med=50.98µs max=163.37ms p(90)=205.95µs p(95)=360.93µs p(99.9)=40.21ms 
     http_req_sending...............: avg=144.32µs min=4.18µs   med=8.43µs  max=170.19ms p(90)=16.35µs  p(95)=115.82µs p(99.9)=25.7ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.69ms  min=717.06µs med=40.26ms max=270.46ms p(90)=100.34ms p(95)=124.25ms p(99.9)=172.21ms
     http_reqs......................: 287340  4713.227982/s
     iteration_duration.............: avg=49.75ms  min=1.31ms   med=41.31ms max=319.22ms p(90)=104.92ms p(95)=130.35ms p(99.9)=199.68ms
     iterations.....................: 286340  4696.825017/s
     success_rate...................: 100.00% ✓ 286340      ✗ 0     
     vus............................: 55      min=0         max=498 
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

     checks.........................: 100.00% ✓ 838815      ✗ 0     
     data_received..................: 25 GB   403 MB/s
     data_sent......................: 337 MB  5.5 MB/s
     http_req_blocked...............: avg=60.7µs   min=801ns    med=2.09µs  max=131.59ms p(90)=3.7µs    p(95)=4.79µs   p(99.9)=21.57ms 
     http_req_connecting............: avg=57.03µs  min=0s       med=0s      max=131.45ms p(90)=0s       p(95)=0s       p(99.9)=21.27ms 
     http_req_duration..............: avg=49.32ms  min=774.37µs med=41.6ms  max=257.78ms p(90)=104.37ms p(95)=128.36ms p(99.9)=183.48ms
       { expected_response:true }...: avg=49.32ms  min=774.37µs med=41.6ms  max=257.78ms p(90)=104.37ms p(95)=128.36ms p(99.9)=183.48ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280605
     http_req_receiving.............: avg=345.41µs min=25.58µs  med=52.62µs max=109.5ms  p(90)=218.34µs p(95)=379.61µs p(99.9)=50.02ms 
     http_req_sending...............: avg=143.02µs min=4.07µs   med=8.76µs  max=134.69ms p(90)=17.13µs  p(95)=119.73µs p(99.9)=25.08ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.83ms  min=732.51µs med=41.3ms  max=257.71ms p(90)=103.27ms p(95)=127.23ms p(99.9)=174.85ms
     http_reqs......................: 280605  4602.989209/s
     iteration_duration.............: avg=50.94ms  min=1.24ms   med=42.42ms max=369.67ms p(90)=107.9ms  p(95)=133.6ms  p(99.9)=206.69ms
     iterations.....................: 279605  4586.585406/s
     success_rate...................: 100.00% ✓ 279605      ✗ 0     
     vus............................: 55      min=0         max=498 
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

     checks.........................: 100.00% ✓ 837993      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 337 MB  5.5 MB/s
     http_req_blocked...............: avg=61.96µs  min=832ns    med=2.12µs  max=135.56ms p(90)=3.83µs   p(95)=5.01µs   p(99.9)=23.55ms 
     http_req_connecting............: avg=58.82µs  min=0s       med=0s      max=135.36ms p(90)=0s       p(95)=0s       p(99.9)=23.28ms 
     http_req_duration..............: avg=49.38ms  min=884.13µs med=41.8ms  max=310.31ms p(90)=104.38ms p(95)=129.83ms p(99.9)=181.47ms
       { expected_response:true }...: avg=49.38ms  min=884.13µs med=41.8ms  max=310.31ms p(90)=104.38ms p(95)=129.83ms p(99.9)=181.47ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280331
     http_req_receiving.............: avg=315.17µs min=21.9µs   med=52.6µs  max=144.88ms p(90)=211.36µs p(95)=374.87µs p(99.9)=42.35ms 
     http_req_sending...............: avg=140.01µs min=4.19µs   med=8.64µs  max=112.65ms p(90)=17.76µs  p(95)=120µs    p(99.9)=25.49ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.92ms  min=843.85µs med=41.49ms max=309.83ms p(90)=103.3ms  p(95)=128.61ms p(99.9)=175.65ms
     http_reqs......................: 280331  4588.735431/s
     iteration_duration.............: avg=50.99ms  min=1.4ms    med=42.51ms max=321.62ms p(90)=107.88ms p(95)=134.69ms p(99.9)=207.45ms
     iterations.....................: 279331  4572.366441/s
     success_rate...................: 100.00% ✓ 279331      ✗ 0     
     vus............................: 61      min=0         max=497 
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

     checks.........................: 100.00% ✓ 817764      ✗ 0     
     data_received..................: 24 GB   392 MB/s
     data_sent......................: 329 MB  5.4 MB/s
     http_req_blocked...............: avg=51.43µs  min=811ns    med=2.31µs  max=125.24ms p(90)=3.91µs   p(95)=5.06µs   p(99.9)=17.12ms 
     http_req_connecting............: avg=48.26µs  min=0s       med=0s      max=125.2ms  p(90)=0s       p(95)=0s       p(99.9)=16.99ms 
     http_req_duration..............: avg=50.87ms  min=840.79µs med=42.55ms max=311.69ms p(90)=108.85ms p(95)=133.6ms  p(99.9)=186.74ms
       { expected_response:true }...: avg=50.87ms  min=840.79µs med=42.55ms max=311.69ms p(90)=108.85ms p(95)=133.6ms  p(99.9)=186.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 273588
     http_req_receiving.............: avg=323.48µs min=25.91µs  med=50.44µs max=183.54ms p(90)=221.39µs p(95)=386.72µs p(99.9)=42.02ms 
     http_req_sending...............: avg=135.16µs min=4.35µs   med=8.82µs  max=219.09ms p(90)=17.52µs  p(95)=124.53µs p(99.9)=24.14ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.41ms  min=793.25µs med=42.29ms max=271.54ms p(90)=107.94ms p(95)=132.49ms p(99.9)=181.96ms
     http_reqs......................: 273588  4482.778801/s
     iteration_duration.............: avg=52.26ms  min=1.41ms   med=43.39ms max=323.36ms p(90)=111.59ms p(95)=137.33ms p(99.9)=217.09ms
     iterations.....................: 272588  4466.393656/s
     success_rate...................: 100.00% ✓ 272588      ✗ 0     
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

     checks.........................: 100.00% ✓ 818520      ✗ 0     
     data_received..................: 24 GB   392 MB/s
     data_sent......................: 329 MB  5.4 MB/s
     http_req_blocked...............: avg=67.4µs   min=792ns    med=2.62µs  max=134.04ms p(90)=4.24µs   p(95)=5.42µs   p(99.9)=24.63ms 
     http_req_connecting............: avg=63.67µs  min=0s       med=0s      max=133.96ms p(90)=0s       p(95)=0s       p(99.9)=24.16ms 
     http_req_duration..............: avg=50.47ms  min=913.41µs med=42.41ms max=326.84ms p(90)=107.52ms p(95)=133.31ms p(99.9)=186.9ms 
       { expected_response:true }...: avg=50.47ms  min=913.41µs med=42.41ms max=326.84ms p(90)=107.52ms p(95)=133.31ms p(99.9)=186.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 273840
     http_req_receiving.............: avg=386.37µs min=27.15µs  med=54.55µs max=123.04ms p(90)=222.24µs p(95)=389.86µs p(99.9)=57.14ms 
     http_req_sending...............: avg=155.4µs  min=4.18µs   med=9.16µs  max=122.5ms  p(90)=18.13µs  p(95)=125.56µs p(99.9)=28.24ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.93ms  min=861.9µs  med=42.06ms max=326.28ms p(90)=106.14ms p(95)=131.83ms p(99.9)=182.17ms
     http_reqs......................: 273840  4481.481272/s
     iteration_duration.............: avg=52.21ms  min=1.5ms    med=43.31ms max=348.92ms p(90)=111.75ms p(95)=138.46ms p(99.9)=221.64ms
     iterations.....................: 272840  4465.115945/s
     success_rate...................: 100.00% ✓ 272840      ✗ 0     
     vus............................: 61      min=0         max=498 
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

     checks.........................: 100.00% ✓ 802209      ✗ 0     
     data_received..................: 24 GB   385 MB/s
     data_sent......................: 323 MB  5.3 MB/s
     http_req_blocked...............: avg=59.66µs  min=1.02µs   med=2.58µs  max=147.83ms p(90)=4.27µs   p(95)=5.5µs    p(99.9)=20.88ms 
     http_req_connecting............: avg=54.86µs  min=0s       med=0s      max=144.88ms p(90)=0s       p(95)=0s       p(99.9)=19.77ms 
     http_req_duration..............: avg=51.79ms  min=844.36µs med=43.05ms max=286.39ms p(90)=111.4ms  p(95)=137.89ms p(99.9)=190.61ms
       { expected_response:true }...: avg=51.79ms  min=844.36µs med=43.05ms max=286.39ms p(90)=111.4ms  p(95)=137.89ms p(99.9)=190.61ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 268403
     http_req_receiving.............: avg=306.97µs min=26.58µs  med=52.08µs max=121.68ms p(90)=228.84µs p(95)=407.66µs p(99.9)=40.55ms 
     http_req_sending...............: avg=142.9µs  min=4.22µs   med=9.08µs  max=252.4ms  p(90)=18.45µs  p(95)=133.17µs p(99.9)=25.45ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.34ms  min=800.46µs med=42.76ms max=285.85ms p(90)=110.49ms p(95)=136.77ms p(99.9)=185.42ms
     http_reqs......................: 268403  4397.827413/s
     iteration_duration.............: avg=53.27ms  min=1.35ms   med=43.9ms  max=403.98ms p(90)=114.05ms p(95)=141.88ms p(99.9)=223.26ms
     iterations.....................: 267403  4381.442248/s
     success_rate...................: 100.00% ✓ 267403      ✗ 0     
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

     checks.........................: 100.00% ✓ 791079      ✗ 0     
     data_received..................: 23 GB   379 MB/s
     data_sent......................: 318 MB  5.2 MB/s
     http_req_blocked...............: avg=60.06µs  min=942ns    med=2.61µs  max=128.08ms p(90)=4.39µs   p(95)=5.64µs   p(99.9)=21.51ms 
     http_req_connecting............: avg=55.8µs   min=0s       med=0s      max=123.41ms p(90)=0s       p(95)=0s       p(99.9)=21.27ms 
     http_req_duration..............: avg=52.67ms  min=987.3µs  med=43.65ms max=293.18ms p(90)=114.25ms p(95)=141.04ms p(99.9)=202.2ms 
       { expected_response:true }...: avg=52.67ms  min=987.3µs  med=43.65ms max=293.18ms p(90)=114.25ms p(95)=141.04ms p(99.9)=202.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 264693
     http_req_receiving.............: avg=339.29µs min=25.78µs  med=51.86µs max=134.62ms p(90)=229.38µs p(95)=408.95µs p(99.9)=49.38ms 
     http_req_sending...............: avg=141.3µs  min=4.48µs   med=9.27µs  max=233.11ms p(90)=20.33µs  p(95)=134.76µs p(99.9)=25.86ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=52.19ms  min=928.36µs med=43.36ms max=273ms    p(90)=113.26ms p(95)=139.97ms p(99.9)=191.27ms
     http_reqs......................: 264693  4325.689175/s
     iteration_duration.............: avg=54.02ms  min=1.52ms   med=44.49ms max=362.54ms p(90)=116.69ms p(95)=144.52ms p(99.9)=218.89ms
     iterations.....................: 263693  4309.346887/s
     success_rate...................: 100.00% ✓ 263693      ✗ 0     
     vus............................: 66      min=0         max=496 
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

     checks.........................: 100.00% ✓ 787176      ✗ 0     
     data_received..................: 23 GB   377 MB/s
     data_sent......................: 316 MB  5.2 MB/s
     http_req_blocked...............: avg=60.39µs  min=931ns    med=2.62µs  max=127.84ms p(90)=4.4µs    p(95)=5.64µs   p(99.9)=20.17ms 
     http_req_connecting............: avg=56.67µs  min=0s       med=0s      max=127.75ms p(90)=0s       p(95)=0s       p(99.9)=20.1ms  
     http_req_duration..............: avg=52.71ms  min=992.33µs med=43.82ms max=338.72ms p(90)=113.82ms p(95)=140.41ms p(99.9)=193.78ms
       { expected_response:true }...: avg=52.71ms  min=992.33µs med=43.82ms max=338.72ms p(90)=113.82ms p(95)=140.41ms p(99.9)=193.78ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 263392
     http_req_receiving.............: avg=316.04µs min=24.32µs  med=52.69µs max=120.82ms p(90)=234.43µs p(95)=412.19µs p(99.9)=45.41ms 
     http_req_sending...............: avg=145.97µs min=4.28µs   med=9.31µs  max=195.91ms p(90)=19.5µs   p(95)=135.49µs p(99.9)=25.86ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=52.24ms  min=950.29µs med=43.54ms max=338.36ms p(90)=112.65ms p(95)=139.32ms p(99.9)=189.3ms 
     http_reqs......................: 263392  4304.066407/s
     iteration_duration.............: avg=54.29ms  min=1.63ms   med=44.65ms max=352.15ms p(90)=116.88ms p(95)=144.18ms p(99.9)=231.15ms
     iterations.....................: 262392  4287.725491/s
     success_rate...................: 100.00% ✓ 262392      ✗ 0     
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

     checks.........................: 100.00% ✓ 761643      ✗ 0     
     data_received..................: 22 GB   365 MB/s
     data_sent......................: 306 MB  5.0 MB/s
     http_req_blocked...............: avg=52.12µs  min=852ns    med=2.63µs  max=108.61ms p(90)=4.41µs   p(95)=5.62µs   p(99.9)=13.89ms 
     http_req_connecting............: avg=48.37µs  min=0s       med=0s      max=108.44ms p(90)=0s       p(95)=0s       p(99.9)=13.43ms 
     http_req_duration..............: avg=54.78ms  min=709.85µs med=45.93ms max=344.39ms p(90)=115.94ms p(95)=145.44ms p(99.9)=234.85ms
       { expected_response:true }...: avg=54.78ms  min=709.85µs med=45.93ms max=344.39ms p(90)=115.94ms p(95)=145.44ms p(99.9)=234.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 254881
     http_req_receiving.............: avg=355.16µs min=24.93µs  med=52.91µs max=128.56ms p(90)=224.6µs  p(95)=409.19µs p(99.9)=54.02ms 
     http_req_sending...............: avg=128.12µs min=4.12µs   med=9.67µs  max=184.9ms  p(90)=19.65µs  p(95)=133.95µs p(99.9)=22.54ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=54.3ms   min=665.57µs med=45.62ms max=344.3ms  p(90)=114.86ms p(95)=144.13ms p(99.9)=220.99ms
     http_reqs......................: 254881  4180.925778/s
     iteration_duration.............: avg=56.12ms  min=1.5ms    med=46.82ms max=365.66ms p(90)=118.84ms p(95)=149.41ms p(99.9)=244ms   
     iterations.....................: 253881  4164.522336/s
     success_rate...................: 100.00% ✓ 253881      ✗ 0     
     vus............................: 55      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 474267      ✗ 0     
     data_received..................: 14 GB   226 MB/s
     data_sent......................: 191 MB  3.1 MB/s
     http_req_blocked...............: avg=14.53µs min=912ns   med=2.68µs  max=38.55ms  p(90)=4.56µs   p(95)=5.79µs   p(99.9)=1.28ms  
     http_req_connecting............: avg=11.13µs min=0s      med=0s      max=38.47ms  p(90)=0s       p(95)=0s       p(99.9)=1.1ms   
     http_req_duration..............: avg=89.38ms min=1.22ms  med=83.66ms max=349.37ms p(90)=174.86ms p(95)=187.46ms p(99.9)=222.34ms
       { expected_response:true }...: avg=89.38ms min=1.22ms  med=83.66ms max=349.37ms p(90)=174.86ms p(95)=187.46ms p(99.9)=222.34ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 159089
     http_req_receiving.............: avg=129.9µs min=25.59µs med=57.05µs max=191.58ms p(90)=171.9µs  p(95)=364.83µs p(99.9)=9.4ms   
     http_req_sending...............: avg=69.52µs min=4.56µs  med=10.78µs max=196.33ms p(90)=21.35µs  p(95)=129.04µs p(99.9)=8.31ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=89.18ms min=1.19ms  med=83.47ms max=349.28ms p(90)=174.66ms p(95)=187.21ms p(99.9)=221.97ms
     http_reqs......................: 159089  2587.662173/s
     iteration_duration.............: avg=90.19ms min=3.4ms   med=84.59ms max=356.55ms p(90)=175.32ms p(95)=187.83ms p(99.9)=223.3ms 
     iterations.....................: 158089  2571.396673/s
     success_rate...................: 100.00% ✓ 158089      ✗ 0     
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

     checks.........................: 100.00% ✓ 252489      ✗ 0    
     data_received..................: 7.4 GB  119 MB/s
     data_sent......................: 102 MB  1.6 MB/s
     http_req_blocked...............: avg=7.13µs   min=1.04µs  med=3µs      max=34.7ms   p(90)=4.75µs   p(95)=5.69µs   p(99.9)=716.45µs
     http_req_connecting............: avg=3.38µs   min=0s      med=0s       max=30.31ms  p(90)=0s       p(95)=0s       p(99.9)=649.7µs 
     http_req_duration..............: avg=167.55ms min=1.98ms  med=131.62ms max=1.27s    p(90)=352.43ms p(95)=458.32ms p(99.9)=925.83ms
       { expected_response:true }...: avg=167.55ms min=1.98ms  med=131.62ms max=1.27s    p(90)=352.43ms p(95)=458.32ms p(99.9)=925.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 85163
     http_req_receiving.............: avg=81.39µs  min=28.71µs med=61.15µs  max=189.39ms p(90)=97.9µs   p(95)=115.27µs p(99.9)=2.15ms  
     http_req_sending...............: avg=34.11µs  min=5.26µs  med=12.69µs  max=75.92ms  p(90)=18.98µs  p(95)=22.89µs  p(99.9)=4.16ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=167.43ms min=1.93ms  med=131.5ms  max=1.27s    p(90)=352.17ms p(95)=458.2ms  p(99.9)=925.74ms
     http_reqs......................: 85163   1364.323997/s
     iteration_duration.............: avg=169.79ms min=7.39ms  med=133.92ms max=1.27s    p(90)=354.61ms p(95)=460.42ms p(99.9)=928.87ms
     iterations.....................: 84163   1348.303848/s
     success_rate...................: 100.00% ✓ 84163       ✗ 0    
     vus............................: 77      min=0         max=493
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

     checks.........................: 100.00% ✓ 238839      ✗ 0    
     data_received..................: 7.1 GB  113 MB/s
     data_sent......................: 97 MB   1.5 MB/s
     http_req_blocked...............: avg=6.19µs   min=1.16µs  med=2.85µs   max=10.46ms  p(90)=4.58µs   p(95)=5.53µs   p(99.9)=543.09µs
     http_req_connecting............: avg=2.67µs   min=0s      med=0s       max=10.38ms  p(90)=0s       p(95)=0s       p(99.9)=454.58µs
     http_req_duration..............: avg=176.97ms min=2.04ms  med=174.58ms max=598.86ms p(90)=334.63ms p(95)=361.12ms p(99.9)=510.29ms
       { expected_response:true }...: avg=176.97ms min=2.04ms  med=174.58ms max=598.86ms p(90)=334.63ms p(95)=361.12ms p(99.9)=510.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 80613
     http_req_receiving.............: avg=78.61µs  min=26.81µs med=62.96µs  max=46.9ms   p(90)=101.62µs p(95)=117.88µs p(99.9)=1.3ms   
     http_req_sending...............: avg=29.16µs  min=4.83µs  med=11.79µs  max=84.19ms  p(90)=18.07µs  p(95)=21.54µs  p(99.9)=3.37ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=176.86ms min=1.95ms  med=174.46ms max=598.79ms p(90)=334.56ms p(95)=361.03ms p(99.9)=510.1ms 
     http_reqs......................: 80613   1290.247421/s
     iteration_duration.............: avg=179.43ms min=4.95ms  med=177.31ms max=599.06ms p(90)=335.56ms p(95)=361.8ms  p(99.9)=511.47ms
     iterations.....................: 79613   1274.24197/s
     success_rate...................: 100.00% ✓ 79613       ✗ 0    
     vus............................: 79      min=0         max=493
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

     checks.........................: 100.00% ✓ 91311      ✗ 0    
     data_received..................: 2.8 GB  43 MB/s
     data_sent......................: 38 MB   584 kB/s
     http_req_blocked...............: avg=8.48µs   min=1.07µs  med=2.76µs   max=8.6ms   p(90)=4.4µs    p(95)=5.31µs   p(99.9)=1.5ms 
     http_req_connecting............: avg=4.78µs   min=0s      med=0s       max=8.54ms  p(90)=0s       p(95)=0s       p(99.9)=1.48ms
     http_req_duration..............: avg=457.02ms min=3.77ms  med=420.62ms max=1.9s    p(90)=907.95ms p(95)=981.75ms p(99.9)=1.44s 
       { expected_response:true }...: avg=457.02ms min=3.77ms  med=420.62ms max=1.9s    p(90)=907.95ms p(95)=981.75ms p(99.9)=1.44s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 31437
     http_req_receiving.............: avg=78.69µs  min=27.52µs med=68.36µs  max=22.94ms p(90)=105.36µs p(95)=119.41µs p(99.9)=1.08ms
     http_req_sending...............: avg=29.4µs   min=4.83µs  med=13.04µs  max=76.59ms p(90)=19.46µs  p(95)=21.8µs   p(99.9)=2.42ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=456.91ms min=3.72ms  med=420.56ms max=1.9s    p(90)=907.87ms p(95)=981.67ms p(99.9)=1.44s 
     http_reqs......................: 31437   486.67531/s
     iteration_duration.............: avg=472.24ms min=18.56ms med=440.05ms max=1.91s   p(90)=911.46ms p(95)=985.34ms p(99.9)=1.44s 
     iterations.....................: 30437   471.194338/s
     success_rate...................: 100.00% ✓ 30437      ✗ 0    
     vus............................: 86      min=0        max=499
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

     checks.........................: 100.00% ✓ 46848      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 20 MB   295 kB/s
     http_req_blocked...............: avg=14.74µs  min=1.49µs  med=3.62µs   max=16.77ms p(90)=5.43µs   p(95)=7.09µs   p(99.9)=2.19ms  
     http_req_connecting............: avg=9.43µs   min=0s      med=0s       max=16.71ms p(90)=0s       p(95)=0s       p(99.9)=2.17ms  
     http_req_duration..............: avg=875.13ms min=5.89ms  med=785.42ms max=5.06s   p(90)=1.72s    p(95)=2s       p(99.9)=4.04s   
       { expected_response:true }...: avg=875.13ms min=5.89ms  med=785.42ms max=5.06s   p(90)=1.72s    p(95)=2s       p(99.9)=4.04s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16616
     http_req_receiving.............: avg=100.1µs  min=39.36µs med=91.8µs   max=23.74ms p(90)=130.49µs p(95)=147.38µs p(99.9)=906.51µs
     http_req_sending...............: avg=29.26µs  min=6.21µs  med=18.06µs  max=39.22ms p(90)=23.45µs  p(95)=26.92µs  p(99.9)=2.75ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=875ms    min=5.81ms  med=785.3ms  max=5.06s   p(90)=1.72s    p(95)=2s       p(99.9)=4.04s   
     http_reqs......................: 16616   245.886539/s
     iteration_duration.............: avg=931.19ms min=86.45ms med=855.23ms max=5.07s   p(90)=1.76s    p(95)=2.02s    p(99.9)=4.06s   
     iterations.....................: 15616   231.08836/s
     success_rate...................: 100.00% ✓ 15616      ✗ 0    
     vus............................: 83      min=0        max=500
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

     checks.........................: 100.00% ✓ 46671      ✗ 0    
     data_received..................: 1.5 GB  21 MB/s
     data_sent......................: 20 MB   290 kB/s
     http_req_blocked...............: avg=15.21µs  min=1.18µs  med=3.5µs    max=13.47ms p(90)=5.3µs    p(95)=6.84µs   p(99.9)=2.14ms
     http_req_connecting............: avg=9.94µs   min=0s      med=0s       max=13.41ms p(90)=0s       p(95)=0s       p(99.9)=2.12ms
     http_req_duration..............: avg=876.87ms min=7.53ms  med=806.75ms max=2.84s   p(90)=1.8s     p(95)=1.92s    p(99.9)=2.58s 
       { expected_response:true }...: avg=876.87ms min=7.53ms  med=806.75ms max=2.84s   p(90)=1.8s     p(95)=1.92s    p(99.9)=2.58s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16557
     http_req_receiving.............: avg=100.58µs min=32.66µs med=89.43µs  max=47.96ms p(90)=129.07µs p(95)=145.74µs p(99.9)=1.17ms
     http_req_sending...............: avg=35.89µs  min=5.36µs  med=17.44µs  max=86.19ms p(90)=22.74µs  p(95)=26.4µs   p(99.9)=2.36ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=876.74ms min=7.45ms  med=806.54ms max=2.84s   p(90)=1.8s     p(95)=1.92s    p(99.9)=2.58s 
     http_reqs......................: 16557   241.66924/s
     iteration_duration.............: avg=933.2ms  min=30.75ms med=866.17ms max=2.84s   p(90)=1.82s    p(95)=1.93s    p(99.9)=2.59s 
     iterations.....................: 15557   227.073042/s
     success_rate...................: 100.00% ✓ 15557      ✗ 0    
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

