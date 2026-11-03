## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 4,720 | 4,767 | 4,684 | 0.7% | 400 MB | 86.8 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 4,658 | 4,680 | 4,652 | 0.2% | 416 MB | 91.3 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,574 | 4,578 | 4,571 | 0.1% | 439 MB | 98.3 KB |  |
| fusion-aot-11 | 16.7.3 | 4,557 | 4,609 | 4,521 | 0.8% | 155 MB | 34.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,474 | 4,502 | 4,433 | 0.6% | 409 MB | 93.6 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,459 | 4,465 | 4,379 | 0.8% | 173 MB | 39.7 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,450 | 4,458 | 4,429 | 0.3% | 187 MB | 42.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,252 | 4,322 | 4,238 | 0.9% | 181 MB | 43.5 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,143 | 4,147 | 3,969 | 1.9% | 2,310 MB | 570.9 KB |  |
| hive-router | v0.3.6 | 2,761 | 2,771 | 2,749 | 0.3% | 165 MB | 61.2 KB |  |
| caliban | 3.2.0 | 1,380 | 1,381 | 1,379 | 0.1% | 10,791 MB | 8,007.2 KB |  |
| cosmo | 0.363.0 | 1,364 | 1,364 | 1,362 | 0.1% | 664 MB | 498.6 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 479 | 480 | 475 | 0.4% | 3,164 MB | 6,763.1 KB |  |
| hive-gateway | 2.15.3 | 252 | 253 | 248 | 0.8% | 4,090 MB | 16,619.2 KB |  |
| apollo-gateway | 2.14.4 | 239 | 240 | 236 | 0.7% | 2,473 MB | 10,593.9 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (8837 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (4862 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (146495 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 860025      ✗ 0     
     data_received..................: 25 GB   413 MB/s
     data_sent......................: 346 MB  5.7 MB/s
     http_req_blocked...............: avg=65.64µs  min=812ns    med=2.2µs   max=135.48ms p(90)=3.76µs   p(95)=4.9µs    p(99.9)=22.58ms 
     http_req_connecting............: avg=61.99µs  min=0s       med=0s      max=135.41ms p(90)=0s       p(95)=0s       p(99.9)=22.24ms 
     http_req_duration..............: avg=48.04ms  min=742.15µs med=39.99ms max=299.59ms p(90)=101.28ms p(95)=126.59ms p(99.9)=181.83ms
       { expected_response:true }...: avg=48.04ms  min=742.15µs med=39.99ms max=299.59ms p(90)=101.28ms p(95)=126.59ms p(99.9)=181.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 287675
     http_req_receiving.............: avg=330.38µs min=24.13µs  med=51.52µs max=182.47ms p(90)=207.08µs p(95)=360.05µs p(99.9)=42.92ms 
     http_req_sending...............: avg=145.77µs min=4.15µs   med=8.69µs  max=269.85ms p(90)=16.64µs  p(95)=114.74µs p(99.9)=26.05ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.56ms  min=700.79µs med=39.67ms max=281.88ms p(90)=100.09ms p(95)=125.42ms p(99.9)=176.74ms
     http_reqs......................: 287675  4720.464904/s
     iteration_duration.............: avg=49.69ms  min=1.23ms   med=40.78ms max=356.25ms p(90)=105.47ms p(95)=132.48ms p(99.9)=199.9ms 
     iterations.....................: 286675  4704.055884/s
     success_rate...................: 100.00% ✓ 286675      ✗ 0     
     vus............................: 55      min=0         max=499 
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

     checks.........................: 100.00% ✓ 848751      ✗ 0     
     data_received..................: 25 GB   408 MB/s
     data_sent......................: 341 MB  5.6 MB/s
     http_req_blocked...............: avg=70.8µs   min=921ns    med=2.55µs  max=145.86ms p(90)=4.12µs   p(95)=5.31µs   p(99.9)=26.54ms 
     http_req_connecting............: avg=66.67µs  min=0s       med=0s      max=137.78ms p(90)=0s       p(95)=0s       p(99.9)=25.6ms  
     http_req_duration..............: avg=48.28ms  min=763.75µs med=40.71ms max=278.24ms p(90)=101.24ms p(95)=126.35ms p(99.9)=182.2ms 
       { expected_response:true }...: avg=48.28ms  min=763.75µs med=40.71ms max=278.24ms p(90)=101.24ms p(95)=126.35ms p(99.9)=182.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 283917
     http_req_receiving.............: avg=406.83µs min=24.95µs  med=52.76µs max=136.8ms  p(90)=218.09µs p(95)=373.78µs p(99.9)=61.84ms 
     http_req_sending...............: avg=159.29µs min=3.71µs   med=9.08µs  max=193.65ms p(90)=17.68µs  p(95)=119.74µs p(99.9)=29.57ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.71ms  min=706.48µs med=40.32ms max=277.82ms p(90)=99.85ms  p(95)=124.87ms p(99.9)=174.8ms 
     http_reqs......................: 283917  4658.248856/s
     iteration_duration.............: avg=50.34ms  min=1.15ms   med=41.63ms max=344.22ms p(90)=106.26ms p(95)=133.24ms p(99.9)=211.34ms
     iterations.....................: 282917  4641.841776/s
     success_rate...................: 100.00% ✓ 282917      ✗ 0     
     vus............................: 54      min=0         max=499 
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

     checks.........................: 100.00% ✓ 835752      ✗ 0     
     data_received..................: 25 GB   400 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=54.96µs  min=782ns    med=2.01µs  max=125.61ms p(90)=3.63µs   p(95)=4.77µs   p(99.9)=19.18ms 
     http_req_connecting............: avg=51.63µs  min=0s       med=0s      max=125.4ms  p(90)=0s       p(95)=0s       p(99.9)=19.09ms 
     http_req_duration..............: avg=49.66ms  min=904.48µs med=41.49ms max=321.04ms p(90)=105.84ms p(95)=129.96ms p(99.9)=184.33ms
       { expected_response:true }...: avg=49.66ms  min=904.48µs med=41.49ms max=321.04ms p(90)=105.84ms p(95)=129.96ms p(99.9)=184.33ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 279584
     http_req_receiving.............: avg=343.72µs min=22.34µs  med=51.45µs max=146.02ms p(90)=216.92µs p(95)=376.91µs p(99.9)=49.45ms 
     http_req_sending...............: avg=130.66µs min=4.03µs   med=8.5µs   max=151.38ms p(90)=17.55µs  p(95)=121.48µs p(99.9)=23.09ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.18ms  min=861.91µs med=41.16ms max=320.61ms p(90)=104.82ms p(95)=128.76ms p(99.9)=173.8ms 
     http_reqs......................: 279584  4574.695434/s
     iteration_duration.............: avg=51.13ms  min=1.39ms   med=42.44ms max=330.47ms p(90)=108.72ms p(95)=133.56ms p(99.9)=211.44ms
     iterations.....................: 278584  4558.332926/s
     success_rate...................: 100.00% ✓ 278584      ✗ 0     
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

     checks.........................: 100.00% ✓ 831525      ✗ 0     
     data_received..................: 24 GB   399 MB/s
     data_sent......................: 334 MB  5.5 MB/s
     http_req_blocked...............: avg=58.69µs min=791ns    med=2.34µs  max=133.03ms p(90)=4µs      p(95)=5.21µs   p(99.9)=19.13ms 
     http_req_connecting............: avg=55.49µs min=0s       med=0s      max=132.77ms p(90)=0s       p(95)=0s       p(99.9)=18.43ms 
     http_req_duration..............: avg=49.78ms min=840.6µs  med=40.72ms max=326.61ms p(90)=107.46ms p(95)=134.8ms  p(99.9)=187.8ms 
       { expected_response:true }...: avg=49.78ms min=840.6µs  med=40.72ms max=326.61ms p(90)=107.46ms p(95)=134.8ms  p(99.9)=187.8ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 278175
     http_req_receiving.............: avg=356.6µs min=23.07µs  med=49.99µs max=178.28ms p(90)=222.53µs p(95)=389.55µs p(99.9)=52.44ms 
     http_req_sending...............: avg=139.2µs min=4.11µs   med=8.64µs  max=211.97ms p(90)=17.92µs  p(95)=125.99µs p(99.9)=24.22ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.29ms min=795.07µs med=40.41ms max=317.76ms p(90)=106.17ms p(95)=133.29ms p(99.9)=184.09ms
     http_reqs......................: 278175  4557.55221/s
     iteration_duration.............: avg=51.39ms min=1.4ms    med=41.68ms max=339.39ms p(90)=110.81ms p(95)=139.28ms p(99.9)=212.76ms
     iterations.....................: 277175  4541.168451/s
     success_rate...................: 100.00% ✓ 277175      ✗ 0     
     vus............................: 59      min=0         max=498 
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

     checks.........................: 100.00% ✓ 817251      ✗ 0     
     data_received..................: 24 GB   392 MB/s
     data_sent......................: 329 MB  5.4 MB/s
     http_req_blocked...............: avg=66.06µs  min=982ns    med=2.64µs  max=162.96ms p(90)=4.35µs   p(95)=5.6µs    p(99.9)=24.62ms 
     http_req_connecting............: avg=61.89µs  min=0s       med=0s      max=119.95ms p(90)=0s       p(95)=0s       p(99.9)=24.22ms 
     http_req_duration..............: avg=50.48ms  min=903.81µs med=42.1ms  max=327.95ms p(90)=108.47ms p(95)=133.69ms p(99.9)=188.12ms
       { expected_response:true }...: avg=50.48ms  min=903.81µs med=42.1ms  max=327.95ms p(90)=108.47ms p(95)=133.69ms p(99.9)=188.12ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 273417
     http_req_receiving.............: avg=332.33µs min=26.02µs  med=53.61µs max=157.66ms p(90)=225.27µs p(95)=393.93µs p(99.9)=44.6ms  
     http_req_sending...............: avg=159.36µs min=4.14µs   med=9.09µs  max=147.63ms p(90)=18.9µs   p(95)=128.01µs p(99.9)=28.9ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.99ms  min=856.95µs med=41.77ms max=327.61ms p(90)=107.41ms p(95)=132.48ms p(99.9)=181.13ms
     http_reqs......................: 273417  4474.130092/s
     iteration_duration.............: avg=52.28ms  min=1.42ms   med=43.05ms max=350.85ms p(90)=112.39ms p(95)=138.68ms p(99.9)=221.52ms
     iterations.....................: 272417  4457.766332/s
     success_rate...................: 100.00% ✓ 272417      ✗ 0     
     vus............................: 62      min=0         max=497 
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

     checks.........................: 100.00% ✓ 813546      ✗ 0     
     data_received..................: 24 GB   390 MB/s
     data_sent......................: 327 MB  5.4 MB/s
     http_req_blocked...............: avg=44.72µs  min=792ns    med=2.05µs  max=117.69ms p(90)=3.6µs    p(95)=4.74µs   p(99.9)=13.83ms 
     http_req_connecting............: avg=41.86µs  min=0s       med=0s      max=117.5ms  p(90)=0s       p(95)=0s       p(99.9)=13.73ms 
     http_req_duration..............: avg=51.37ms  min=851.88µs med=43.38ms max=317.19ms p(90)=109.47ms p(95)=135.05ms p(99.9)=186.16ms
       { expected_response:true }...: avg=51.37ms  min=851.88µs med=43.38ms max=317.19ms p(90)=109.47ms p(95)=135.05ms p(99.9)=186.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 272182
     http_req_receiving.............: avg=258.69µs min=25.86µs  med=50.14µs max=181.84ms p(90)=217.31µs p(95)=376.13µs p(99.9)=33.83ms 
     http_req_sending...............: avg=114.14µs min=4.18µs   med=8.5µs   max=156.47ms p(90)=16.83µs  p(95)=121.51µs p(99.9)=20.19ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.99ms  min=803.19µs med=43.12ms max=316.93ms p(90)=108.71ms p(95)=134.14ms p(99.9)=183.59ms
     http_reqs......................: 272182  4459.153451/s
     iteration_duration.............: avg=52.53ms  min=1.38ms   med=44.11ms max=333.97ms p(90)=111.83ms p(95)=137.57ms p(99.9)=208.15ms
     iterations.....................: 271182  4442.770467/s
     success_rate...................: 100.00% ✓ 271182      ✗ 0     
     vus............................: 59      min=0         max=498 
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

     checks.........................: 100.00% ✓ 814014      ✗ 0     
     data_received..................: 24 GB   389 MB/s
     data_sent......................: 327 MB  5.3 MB/s
     http_req_blocked...............: avg=46.61µs  min=792ns    med=2.02µs  max=98.49ms  p(90)=3.71µs   p(95)=4.9µs    p(99.9)=14.79ms 
     http_req_connecting............: avg=43.33µs  min=0s       med=0s      max=98.4ms   p(90)=0s       p(95)=0s       p(99.9)=14.47ms 
     http_req_duration..............: avg=51.39ms  min=988.74µs med=43.48ms max=304.23ms p(90)=109.56ms p(95)=134.43ms p(99.9)=189.85ms
       { expected_response:true }...: avg=51.39ms  min=988.74µs med=43.48ms max=304.23ms p(90)=109.56ms p(95)=134.43ms p(99.9)=189.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 272338
     http_req_receiving.............: avg=294.39µs min=25.87µs  med=49.94µs max=141.4ms  p(90)=220.87µs p(95)=374.38µs p(99.9)=38.74ms 
     http_req_sending...............: avg=122.69µs min=4.34µs   med=8.41µs  max=241.66ms p(90)=18.1µs   p(95)=123.01µs p(99.9)=21.52ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.97ms  min=930.39µs med=43.23ms max=304.03ms p(90)=108.69ms p(95)=133.43ms p(99.9)=182.15ms
     http_reqs......................: 272338  4450.582903/s
     iteration_duration.............: avg=52.5ms   min=1.71ms   med=44.09ms max=318.05ms p(90)=111.74ms p(95)=136.81ms p(99.9)=207.86ms
     iterations.....................: 271338  4434.240773/s
     success_rate...................: 100.00% ✓ 271338      ✗ 0     
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

     checks.........................: 100.00% ✓ 777750      ✗ 0     
     data_received..................: 23 GB   372 MB/s
     data_sent......................: 313 MB  5.1 MB/s
     http_req_blocked...............: avg=49.24µs  min=832ns    med=2.57µs  max=94.56ms  p(90)=4.3µs    p(95)=5.46µs   p(99.9)=14ms    
     http_req_connecting............: avg=45.35µs  min=0s       med=0s      max=94.35ms  p(90)=0s       p(95)=0s       p(99.9)=13.76ms 
     http_req_duration..............: avg=53.63ms  min=975.49µs med=44.89ms max=294.35ms p(90)=115.54ms p(95)=143.57ms p(99.9)=199.48ms
       { expected_response:true }...: avg=53.63ms  min=975.49µs med=44.89ms max=294.35ms p(90)=115.54ms p(95)=143.57ms p(99.9)=199.48ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 260250
     http_req_receiving.............: avg=314.49µs min=26.46µs  med=51.63µs max=91.66ms  p(90)=236.48µs p(95)=404.84µs p(99.9)=44.67ms 
     http_req_sending...............: avg=127.02µs min=4.12µs   med=9.08µs  max=224.64ms p(90)=19.26µs  p(95)=134.62µs p(99.9)=22.15ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.19ms  min=935.7µs  med=44.62ms max=294.12ms p(90)=114.61ms p(95)=142.29ms p(99.9)=196.02ms
     http_reqs......................: 260250  4252.895676/s
     iteration_duration.............: avg=54.95ms  min=1.62ms   med=45.69ms max=329.23ms p(90)=118.32ms p(95)=146.84ms p(99.9)=224.37ms
     iterations.....................: 259250  4236.554098/s
     success_rate...................: 100.00% ✓ 259250      ✗ 0     
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

     checks.........................: 100.00% ✓ 754389      ✗ 0     
     data_received..................: 22 GB   362 MB/s
     data_sent......................: 303 MB  5.0 MB/s
     http_req_blocked...............: avg=61.83µs  min=1.09µs   med=2.88µs  max=138.91ms p(90)=4.72µs   p(95)=5.98µs   p(99.9)=19.4ms  
     http_req_connecting............: avg=56.99µs  min=0s       med=0s      max=114.48ms p(90)=0s       p(95)=0s       p(99.9)=19.2ms  
     http_req_duration..............: avg=55.09ms  min=707.06µs med=46.21ms max=393.63ms p(90)=118.2ms  p(95)=148.1ms  p(99.9)=216.23ms
       { expected_response:true }...: avg=55.09ms  min=707.06µs med=46.21ms max=393.63ms p(90)=118.2ms  p(95)=148.1ms  p(99.9)=216.23ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 252463
     http_req_receiving.............: avg=320.56µs min=25.38µs  med=54.71µs max=240.51ms p(90)=239.53µs p(95)=421.37µs p(99.9)=42.67ms 
     http_req_sending...............: avg=143.4µs  min=4.33µs   med=10.03µs max=261.9ms  p(90)=20.44µs  p(95)=139.69µs p(99.9)=25.18ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=54.63ms  min=654.03µs med=45.88ms max=375.29ms p(90)=117.1ms  p(95)=147.02ms p(99.9)=211.55ms
     http_reqs......................: 252463  4143.016708/s
     iteration_duration.............: avg=56.65ms  min=1.28ms   med=47.06ms max=403.16ms p(90)=121.46ms p(95)=152.76ms p(99.9)=235.14ms
     iterations.....................: 251463  4126.606316/s
     success_rate...................: 100.00% ✓ 251463      ✗ 0     
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

     checks.........................: 100.00% ✓ 506376      ✗ 0     
     data_received..................: 15 GB   242 MB/s
     data_sent......................: 204 MB  3.3 MB/s
     http_req_blocked...............: avg=17.49µs  min=862ns   med=2.38µs  max=54.41ms  p(90)=4.17µs   p(95)=5.46µs   p(99.9)=911.87µs
     http_req_connecting............: avg=14.3µs   min=0s      med=0s      max=54.24ms  p(90)=0s       p(95)=0s       p(99.9)=831.89µs
     http_req_duration..............: avg=83.72ms  min=1.23ms  med=78.56ms max=250.33ms p(90)=163.5ms  p(95)=177.7ms  p(99.9)=222.93ms
       { expected_response:true }...: avg=83.72ms  min=1.23ms  med=78.56ms max=250.33ms p(90)=163.5ms  p(95)=177.7ms  p(99.9)=222.93ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 169792
     http_req_receiving.............: avg=141.01µs min=26.35µs med=56.03µs max=166.97ms p(90)=179.07µs p(95)=361.62µs p(99.9)=12.99ms 
     http_req_sending...............: avg=72.99µs  min=4.31µs  med=10.34µs max=166.91ms p(90)=21.02µs  p(95)=125.83µs p(99.9)=9.86ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=83.5ms   min=1.16ms  med=78.35ms max=250.07ms p(90)=163.23ms p(95)=177.41ms p(99.9)=222.18ms
     http_reqs......................: 169792  2761.519046/s
     iteration_duration.............: avg=84.46ms  min=4.12ms  med=79.4ms  max=295.85ms p(90)=163.92ms p(95)=178.1ms  p(99.9)=223.65ms
     iterations.....................: 168792  2745.254917/s
     success_rate...................: 100.00% ✓ 168792      ✗ 0     
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

     checks.........................: 100.00% ✓ 255342      ✗ 0    
     data_received..................: 7.5 GB  121 MB/s
     data_sent......................: 103 MB  1.7 MB/s
     http_req_blocked...............: avg=6.56µs   min=1.06µs  med=3.23µs   max=20.08ms  p(90)=5.02µs   p(95)=6.01µs   p(99.9)=600.26µs
     http_req_connecting............: avg=2.71µs   min=0s      med=0s       max=19.9ms   p(90)=0s       p(95)=0s       p(99.9)=530.72µs
     http_req_duration..............: avg=165.62ms min=2ms     med=138.38ms max=820.22ms p(90)=346.07ms p(95)=401.08ms p(99.9)=612.82ms
       { expected_response:true }...: avg=165.62ms min=2ms     med=138.38ms max=820.22ms p(90)=346.07ms p(95)=401.08ms p(99.9)=612.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 86114
     http_req_receiving.............: avg=79.41µs  min=28.65µs med=61.82µs  max=153.22ms p(90)=99.42µs  p(95)=115.71µs p(99.9)=1.93ms  
     http_req_sending...............: avg=34.03µs  min=5.22µs  med=12.9µs   max=79.4ms   p(90)=19.53µs  p(95)=23.48µs  p(99.9)=3.89ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=165.5ms  min=1.93ms  med=138.23ms max=820.14ms p(90)=345.94ms p(95)=401.01ms p(99.9)=612.73ms
     http_reqs......................: 86114   1380.213316/s
     iteration_duration.............: avg=167.82ms min=7.91ms  med=140.81ms max=820.44ms p(90)=347.44ms p(95)=402.28ms p(99.9)=613.28ms
     iterations.....................: 85114   1364.18557/s
     success_rate...................: 100.00% ✓ 85114       ✗ 0    
     vus............................: 75      min=0         max=494
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

     checks.........................: 100.00% ✓ 252615      ✗ 0    
     data_received..................: 7.5 GB  119 MB/s
     data_sent......................: 102 MB  1.6 MB/s
     http_req_blocked...............: avg=4.94µs   min=881ns  med=2.36µs   max=11.06ms  p(90)=4.02µs   p(95)=4.97µs   p(99.9)=283.58µs
     http_req_connecting............: avg=1.96µs   min=0s     med=0s       max=10.86ms  p(90)=0s       p(95)=0s       p(99.9)=204.15µs
     http_req_duration..............: avg=167.38ms min=2.01ms med=167.15ms max=466.64ms p(90)=316.33ms p(95)=338.27ms p(99.9)=412.42ms
       { expected_response:true }...: avg=167.38ms min=2.01ms med=167.15ms max=466.64ms p(90)=316.33ms p(95)=338.27ms p(99.9)=412.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 85205
     http_req_receiving.............: avg=77.55µs  min=27.9µs med=60.72µs  max=70.35ms  p(90)=98.35µs  p(95)=115.28µs p(99.9)=1.56ms  
     http_req_sending...............: avg=31.11µs  min=4.73µs med=10.56µs  max=95.65ms  p(90)=17.28µs  p(95)=21.17µs  p(99.9)=3.44ms  
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=167.28ms min=1.95ms med=167.05ms max=466.57ms p(90)=316.24ms p(95)=338.15ms p(99.9)=412.2ms 
     http_reqs......................: 85205   1364.447699/s
     iteration_duration.............: avg=169.6ms  min=4.78ms med=169.88ms max=466.79ms p(90)=317.02ms p(95)=338.84ms p(99.9)=412.89ms
     iterations.....................: 84205   1348.433994/s
     success_rate...................: 100.00% ✓ 84205       ✗ 0    
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

     checks.........................: 100.00% ✓ 90180      ✗ 0    
     data_received..................: 2.7 GB  42 MB/s
     data_sent......................: 37 MB   576 kB/s
     http_req_blocked...............: avg=8.31µs   min=1.02µs  med=2.76µs   max=12.04ms  p(90)=4.45µs   p(95)=5.46µs   p(99.9)=1.09ms
     http_req_connecting............: avg=4.54µs   min=0s      med=0s       max=11.98ms  p(90)=0s       p(95)=0s       p(99.9)=1.06ms
     http_req_duration..............: avg=462.5ms  min=3.9ms   med=431.11ms max=2.01s    p(90)=916.25ms p(95)=994.35ms p(99.9)=1.48s 
       { expected_response:true }...: avg=462.5ms  min=3.9ms   med=431.11ms max=2.01s    p(90)=916.25ms p(95)=994.35ms p(99.9)=1.48s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 31060
     http_req_receiving.............: avg=93.51µs  min=30.28µs med=71.31µs  max=107.53ms p(90)=108.34µs p(95)=121.59µs p(99.9)=1.02ms
     http_req_sending...............: avg=34.67µs  min=5.06µs  med=13.25µs  max=138.94ms p(90)=19.32µs  p(95)=21.79µs  p(99.9)=2.06ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=462.37ms min=3.8ms   med=431.01ms max=2.01s    p(90)=916.17ms p(95)=994.23ms p(99.9)=1.48s 
     http_reqs......................: 31060   479.769307/s
     iteration_duration.............: avg=478.09ms min=11.91ms med=449.25ms max=2.01s    p(90)=921.73ms p(95)=997.47ms p(99.9)=1.49s 
     iterations.....................: 30060   464.322774/s
     success_rate...................: 100.00% ✓ 30060      ✗ 0    
     vus............................: 91      min=0        max=500
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

     checks.........................: 100.00% ✓ 48096      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 20 MB   303 kB/s
     http_req_blocked...............: avg=17.05µs  min=1.08µs  med=3.21µs   max=7.7ms   p(90)=4.96µs   p(95)=6.4µs    p(99.9)=3.75ms
     http_req_connecting............: avg=12.06µs  min=0s      med=0s       max=7.63ms  p(90)=0s       p(95)=0s       p(99.9)=3.62ms
     http_req_duration..............: avg=853.81ms min=5.56ms  med=760.72ms max=4.22s   p(90)=1.71s    p(95)=1.94s    p(99.9)=3.67s 
       { expected_response:true }...: avg=853.81ms min=5.56ms  med=760.72ms max=4.22s   p(90)=1.71s    p(95)=1.94s    p(99.9)=3.67s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 17032
     http_req_receiving.............: avg=96.7µs   min=28.81µs med=87.82µs  max=30.58ms p(90)=124.77µs p(95)=141.56µs p(99.9)=1.31ms
     http_req_sending...............: avg=32.93µs  min=5.07µs  med=17.23µs  max=37.08ms p(90)=22.29µs  p(95)=25.5µs   p(99.9)=3.77ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=853.68ms min=5.49ms  med=760.6ms  max=4.22s   p(90)=1.71s    p(95)=1.94s    p(99.9)=3.67s 
     http_reqs......................: 17032   252.016536/s
     iteration_duration.............: avg=907.12ms min=52.14ms med=829.61ms max=4.22s   p(90)=1.73s    p(95)=1.96s    p(99.9)=3.69s 
     iterations.....................: 16032   237.219886/s
     success_rate...................: 100.00% ✓ 16032      ✗ 0    
     vus............................: 69      min=0        max=500
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

     checks.........................: 100.00% ✓ 46143      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   287 kB/s
     http_req_blocked...............: avg=11.18µs  min=1.27µs  med=3.47µs   max=12.37ms p(90)=5.14µs   p(95)=6.56µs   p(99.9)=846.48µs
     http_req_connecting............: avg=6.07µs   min=0s      med=0s       max=12.3ms  p(90)=0s       p(95)=0s       p(99.9)=828µs   
     http_req_duration..............: avg=886.44ms min=7.57ms  med=804.26ms max=3.07s   p(90)=1.81s    p(95)=1.92s    p(99.9)=2.74s   
       { expected_response:true }...: avg=886.44ms min=7.57ms  med=804.26ms max=3.07s   p(90)=1.81s    p(95)=1.92s    p(99.9)=2.74s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16381
     http_req_receiving.............: avg=95.2µs   min=32.12µs med=83.11µs  max=67.64ms p(90)=121.33µs p(95)=136.82µs p(99.9)=1.09ms  
     http_req_sending...............: avg=27.17µs  min=5.42µs  med=15.94µs  max=47.28ms p(90)=21.44µs  p(95)=24.65µs  p(99.9)=1.68ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=886.32ms min=7.5ms   med=804.12ms max=3.07s   p(90)=1.81s    p(95)=1.92s    p(99.9)=2.74s   
     http_reqs......................: 16381   239.067598/s
     iteration_duration.............: avg=944.07ms min=41.47ms med=881.99ms max=3.07s   p(90)=1.82s    p(95)=1.93s    p(99.9)=2.76s   
     iterations.....................: 15381   224.473397/s
     success_rate...................: 100.00% ✓ 15381      ✗ 0    
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

