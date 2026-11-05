## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 4,715 | 4,725 | 4,593 | 1.2% | 433 MB | 94.1 KB |  |
| fusion-net-11 | 16.7.3 | 4,618 | 4,765 | 4,611 | 1.4% | 423 MB | 93.8 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,582 | 4,624 | 4,496 | 1.4% | 398 MB | 88.9 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,496 | 4,512 | 4,491 | 0.2% | 182 MB | 41.5 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,466 | 4,569 | 4,444 | 1.4% | 420 MB | 96.3 KB |  |
| fusion-aot-11 | 16.7.3 | 4,446 | 4,487 | 4,381 | 1.0% | 203 MB | 46.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,368 | 4,412 | 4,310 | 0.8% | 166 MB | 38.9 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,295 | 4,377 | 4,284 | 0.9% | 162 MB | 38.7 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,186 | 4,200 | 4,183 | 0.2% | 2,298 MB | 562.2 KB |  |
| hive-router | v0.3.10 | 2,597 | 2,612 | 2,593 | 0.3% | 165 MB | 65.1 KB |  |
| caliban | 3.2.0 | 1,332 | 1,344 | 1,297 | 1.4% | 10,734 MB | 8,251.9 KB |  |
| cosmo | 0.365.2 | 1,291 | 1,295 | 1,285 | 0.3% | 641 MB | 508.6 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 493 | 493 | 489 | 0.4% | 3,168 MB | 6,581.0 KB |  |
| hive-gateway | 2.15.6 | 244 | 246 | 241 | 0.7% | 3,937 MB | 16,521.2 KB |  |
| apollo-gateway | 2.14.4 | 238 | 239 | 236 | 0.5% | 2,460 MB | 10,586.3 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (3256 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (7377 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (143594 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 859206      ✗ 0     
     data_received..................: 25 GB   413 MB/s
     data_sent......................: 345 MB  5.7 MB/s
     http_req_blocked...............: avg=61.72µs  min=771ns    med=2µs     max=122.25ms p(90)=3.6µs    p(95)=4.74µs   p(99.9)=21.92ms 
     http_req_connecting............: avg=57.97µs  min=0s       med=0s      max=122.12ms p(90)=0s       p(95)=0s       p(99.9)=21.41ms 
     http_req_duration..............: avg=47.93ms  min=748.63µs med=40.44ms max=325.5ms  p(90)=100.88ms p(95)=125.22ms p(99.9)=177.16ms
       { expected_response:true }...: avg=47.93ms  min=748.63µs med=40.44ms max=325.5ms  p(90)=100.88ms p(95)=125.22ms p(99.9)=177.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 287402
     http_req_receiving.............: avg=334.57µs min=24.48µs  med=51.96µs max=170.07ms p(90)=210.4µs  p(95)=364.38µs p(99.9)=44.36ms 
     http_req_sending...............: avg=145.17µs min=4.14µs   med=8.42µs  max=175.3ms  p(90)=16.6µs   p(95)=116.6µs  p(99.9)=25.78ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.45ms  min=699.78µs med=40.13ms max=309.29ms p(90)=99.78ms  p(95)=123.83ms p(99.9)=172.35ms
     http_reqs......................: 287402  4715.450517/s
     iteration_duration.............: avg=49.73ms  min=1.15ms   med=41.27ms max=337.14ms p(90)=104.86ms p(95)=130.66ms p(99.9)=201.26ms
     iterations.....................: 286402  4699.043357/s
     success_rate...................: 100.00% ✓ 286402      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 841275      ✗ 0     
     data_received..................: 25 GB   404 MB/s
     data_sent......................: 338 MB  5.5 MB/s
     http_req_blocked...............: avg=72.7µs   min=952ns    med=2.55µs  max=140.73ms p(90)=4.14µs   p(95)=5.34µs   p(99.9)=26.83ms 
     http_req_connecting............: avg=68.94µs  min=0s       med=0s      max=140.67ms p(90)=0s       p(95)=0s       p(99.9)=26.55ms 
     http_req_duration..............: avg=48.83ms  min=764.33µs med=40.92ms max=297.96ms p(90)=102.84ms p(95)=127.47ms p(99.9)=182.36ms
       { expected_response:true }...: avg=48.83ms  min=764.33µs med=40.92ms max=297.96ms p(90)=102.84ms p(95)=127.47ms p(99.9)=182.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 281425
     http_req_receiving.............: avg=348.86µs min=25.19µs  med=53.94µs max=123.97ms p(90)=217.87µs p(95)=381.72µs p(99.9)=47.83ms 
     http_req_sending...............: avg=158.92µs min=3.96µs   med=8.93µs  max=147.5ms  p(90)=17.6µs   p(95)=122.84µs p(99.9)=28.37ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.32ms  min=710.98µs med=40.56ms max=271.91ms p(90)=101.64ms p(95)=126.22ms p(99.9)=178.22ms
     http_reqs......................: 281425  4618.005099/s
     iteration_duration.............: avg=50.79ms  min=997.7µs  med=41.87ms max=366.29ms p(90)=107.81ms p(95)=133.95ms p(99.9)=207.4ms 
     iterations.....................: 280425  4601.595735/s
     success_rate...................: 100.00% ✓ 280425      ✗ 0     
     vus............................: 55      min=0         max=499 
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

     checks.........................: 100.00% ✓ 837012      ✗ 0     
     data_received..................: 25 GB   401 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=66.93µs  min=801ns    med=2.19µs  max=138.53ms p(90)=3.91µs   p(95)=5.14µs   p(99.9)=23.47ms 
     http_req_connecting............: avg=63.51µs  min=0s       med=0s      max=138.27ms p(90)=0s       p(95)=0s       p(99.9)=22.7ms  
     http_req_duration..............: avg=49.31ms  min=907.25µs med=41.42ms max=286.31ms p(90)=103.91ms p(95)=129.48ms p(99.9)=184.1ms 
       { expected_response:true }...: avg=49.31ms  min=907.25µs med=41.42ms max=286.31ms p(90)=103.91ms p(95)=129.48ms p(99.9)=184.1ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 280004
     http_req_receiving.............: avg=315.46µs min=26.1µs   med=52.64µs max=116.58ms p(90)=210.25µs p(95)=367.4µs  p(99.9)=43.23ms 
     http_req_sending...............: avg=150.92µs min=4.19µs   med=8.61µs  max=187.34ms p(90)=17.91µs  p(95)=119.3µs  p(99.9)=26.56ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.84ms  min=864.58µs med=41.1ms  max=281.77ms p(90)=102.68ms p(95)=128.31ms p(99.9)=179.57ms
     http_reqs......................: 280004  4582.227584/s
     iteration_duration.............: avg=51.05ms  min=1.46ms   med=42.14ms max=392.68ms p(90)=107.94ms p(95)=134.89ms p(99.9)=211.65ms
     iterations.....................: 279004  4565.862719/s
     success_rate...................: 100.00% ✓ 279004      ✗ 0     
     vus............................: 61      min=0         max=497 
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

     checks.........................: 100.00% ✓ 820632      ✗ 0     
     data_received..................: 24 GB   393 MB/s
     data_sent......................: 330 MB  5.4 MB/s
     http_req_blocked...............: avg=41.54µs  min=801ns    med=1.97µs  max=101.13ms p(90)=3.49µs   p(95)=4.57µs   p(99.9)=11.98ms 
     http_req_connecting............: avg=38.59µs  min=0s       med=0s      max=100.96ms p(90)=0s       p(95)=0s       p(99.9)=11.78ms 
     http_req_duration..............: avg=50.86ms  min=838.64µs med=42.5ms  max=291.11ms p(90)=107.61ms p(95)=133.33ms p(99.9)=186.5ms 
       { expected_response:true }...: avg=50.86ms  min=838.64µs med=42.5ms  max=291.11ms p(90)=107.61ms p(95)=133.33ms p(99.9)=186.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 274544
     http_req_receiving.............: avg=257.19µs min=24.83µs  med=49.29µs max=67.28ms  p(90)=219.15µs p(95)=373.52µs p(99.9)=34.25ms 
     http_req_sending...............: avg=116.41µs min=3.98µs   med=8.3µs   max=148.38ms p(90)=16.93µs  p(95)=120.96µs p(99.9)=20.48ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.48ms  min=799.46µs med=42.25ms max=261.28ms p(90)=106.78ms p(95)=132.45ms p(99.9)=183.18ms
     http_reqs......................: 274544  4496.308897/s
     iteration_duration.............: avg=52.08ms  min=1.38ms   med=43.5ms  max=321.99ms p(90)=110.2ms  p(95)=135.79ms p(99.9)=201.73ms
     iterations.....................: 273544  4479.931526/s
     success_rate...................: 100.00% ✓ 273544      ✗ 0     
     vus............................: 59      min=0         max=497 
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

     checks.........................: 100.00% ✓ 815817      ✗ 0     
     data_received..................: 24 GB   391 MB/s
     data_sent......................: 328 MB  5.4 MB/s
     http_req_blocked...............: avg=66.74µs  min=861ns    med=2.59µs  max=140.19ms p(90)=4.23µs   p(95)=5.42µs   p(99.9)=25.59ms 
     http_req_connecting............: avg=63.23µs  min=0s       med=0s      max=140.11ms p(90)=0s       p(95)=0s       p(99.9)=25.21ms 
     http_req_duration..............: avg=50.79ms  min=897.62µs med=42.58ms max=317.05ms p(90)=107.85ms p(95)=134.6ms  p(99.9)=188.47ms
       { expected_response:true }...: avg=50.79ms  min=897.62µs med=42.58ms max=317.05ms p(90)=107.85ms p(95)=134.6ms  p(99.9)=188.47ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 272939
     http_req_receiving.............: avg=385.41µs min=27.15µs  med=54.75µs max=181.49ms p(90)=227.43µs p(95)=395.65µs p(99.9)=55.27ms 
     http_req_sending...............: avg=152.26µs min=4.04µs   med=9.15µs  max=194.35ms p(90)=18.27µs  p(95)=125.22µs p(99.9)=26.47ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.25ms  min=854.45µs med=42.23ms max=299.37ms p(90)=106.59ms p(95)=133.25ms p(99.9)=183.75ms
     http_reqs......................: 272939  4466.2028/s
     iteration_duration.............: avg=52.38ms  min=1.43ms   med=43.38ms max=347.26ms p(90)=111.46ms p(95)=139.52ms p(99.9)=215.79ms
     iterations.....................: 271939  4449.839426/s
     success_rate...................: 100.00% ✓ 271939      ✗ 0     
     vus............................: 62      min=0         max=497 
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

     checks.........................: 100.00% ✓ 811113      ✗ 0     
     data_received..................: 24 GB   389 MB/s
     data_sent......................: 326 MB  5.3 MB/s
     http_req_blocked...............: avg=43.23µs  min=772ns    med=2.2µs   max=91.54ms  p(90)=3.8µs    p(95)=4.96µs   p(99.9)=13.44ms 
     http_req_connecting............: avg=40.35µs  min=0s       med=0s      max=88.88ms  p(90)=0s       p(95)=0s       p(99.9)=13.32ms 
     http_req_duration..............: avg=51.53ms  min=838.99µs med=43.28ms max=332.86ms p(90)=109.59ms p(95)=136.02ms p(99.9)=187.71ms
       { expected_response:true }...: avg=51.53ms  min=838.99µs med=43.28ms max=332.86ms p(90)=109.59ms p(95)=136.02ms p(99.9)=187.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 271371
     http_req_receiving.............: avg=260.17µs min=24.78µs  med=50.61µs max=106.16ms p(90)=222.59µs p(95)=384.25µs p(99.9)=33.08ms 
     http_req_sending...............: avg=120.98µs min=4µs      med=8.48µs  max=203.83ms p(90)=17.3µs   p(95)=124.9µs  p(99.9)=21.33ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.14ms  min=791.87µs med=42.99ms max=332.54ms p(90)=108.89ms p(95)=135.14ms p(99.9)=185.34ms
     http_reqs......................: 271371  4446.316126/s
     iteration_duration.............: avg=52.69ms  min=1.43ms   med=44.11ms max=342.9ms  p(90)=111.9ms  p(95)=139.02ms p(99.9)=207.64ms
     iterations.....................: 270371  4429.931486/s
     success_rate...................: 100.00% ✓ 270371      ✗ 0     
     vus............................: 58      min=0         max=498 
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

     checks.........................: 100.00% ✓ 799029      ✗ 0     
     data_received..................: 23 GB   382 MB/s
     data_sent......................: 321 MB  5.2 MB/s
     http_req_blocked...............: avg=58.87µs  min=942ns    med=2.54µs  max=121.75ms p(90)=4.31µs   p(95)=5.55µs   p(99.9)=19.71ms 
     http_req_connecting............: avg=55.26µs  min=0s       med=0s      max=121.7ms  p(90)=0s       p(95)=0s       p(99.9)=19.65ms 
     http_req_duration..............: avg=52.3ms   min=984.71µs med=43.26ms max=313.34ms p(90)=113.07ms p(95)=139.93ms p(99.9)=192.18ms
       { expected_response:true }...: avg=52.3ms   min=984.71µs med=43.26ms max=313.34ms p(90)=113.07ms p(95)=139.93ms p(99.9)=192.18ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 267343
     http_req_receiving.............: avg=293.55µs min=25.82µs  med=51.72µs max=182.27ms p(90)=229.63µs p(95)=403.3µs  p(99.9)=39.54ms 
     http_req_sending...............: avg=139.4µs  min=4.3µs    med=9.1µs   max=262.64ms p(90)=19.45µs  p(95)=132.56µs p(99.9)=25ms    
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.87ms  min=941.35µs med=42.99ms max=312.71ms p(90)=112.18ms p(95)=138.96ms p(99.9)=188.72ms
     http_reqs......................: 267343  4368.744432/s
     iteration_duration.............: avg=53.49ms  min=1.61ms   med=44.08ms max=347.09ms p(90)=115.14ms p(95)=142.7ms  p(99.9)=208.7ms 
     iterations.....................: 266343  4352.403086/s
     success_rate...................: 100.00% ✓ 266343      ✗ 0     
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

     checks.........................: 100.00% ✓ 785673      ✗ 0     
     data_received..................: 23 GB   376 MB/s
     data_sent......................: 316 MB  5.2 MB/s
     http_req_blocked...............: avg=58.59µs  min=942ns    med=2.56µs  max=156.49ms p(90)=4.41µs   p(95)=5.72µs   p(99.9)=20.42ms 
     http_req_connecting............: avg=54.55µs  min=0s       med=0s      max=109.22ms p(90)=0s       p(95)=0s       p(99.9)=19.79ms 
     http_req_duration..............: avg=52.89ms  min=994.92µs med=43.8ms  max=315.26ms p(90)=114.68ms p(95)=142.79ms p(99.9)=204.67ms
       { expected_response:true }...: avg=52.89ms  min=994.92µs med=43.8ms  max=315.26ms p(90)=114.68ms p(95)=142.79ms p(99.9)=204.67ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 262891
     http_req_receiving.............: avg=340.4µs  min=25.33µs  med=52.33µs max=142.06ms p(90)=238.85µs p(95)=417.57µs p(99.9)=50.77ms 
     http_req_sending...............: avg=144.88µs min=4.34µs   med=9.12µs  max=143.59ms p(90)=20.25µs  p(95)=136.33µs p(99.9)=25.51ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=52.41ms  min=949.57µs med=43.52ms max=287.63ms p(90)=113.6ms  p(95)=141.71ms p(99.9)=193.16ms
     http_reqs......................: 262891  4295.194121/s
     iteration_duration.............: avg=54.39ms  min=1.55ms   med=44.67ms max=396.64ms p(90)=117.67ms p(95)=146.54ms p(99.9)=229.14ms
     iterations.....................: 261891  4278.855813/s
     success_rate...................: 100.00% ✓ 261891      ✗ 0     
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

     checks.........................: 100.00% ✓ 762969      ✗ 0     
     data_received..................: 22 GB   366 MB/s
     data_sent......................: 307 MB  5.0 MB/s
     http_req_blocked...............: avg=43.59µs  min=821ns    med=2.08µs  max=110.98ms p(90)=3.73µs   p(95)=4.87µs   p(99.9)=11.07ms 
     http_req_connecting............: avg=39.75µs  min=0s       med=0s      max=93.94ms  p(90)=0s       p(95)=0s       p(99.9)=10.82ms 
     http_req_duration..............: avg=54.75ms  min=722.64µs med=45.93ms max=301.51ms p(90)=115.24ms p(95)=143.05ms p(99.9)=217.29ms
       { expected_response:true }...: avg=54.75ms  min=722.64µs med=45.93ms max=301.51ms p(90)=115.24ms p(95)=143.05ms p(99.9)=217.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 255323
     http_req_receiving.............: avg=270.69µs min=24.73µs  med=50.18µs max=104.51ms p(90)=214.11µs p(95)=372.41µs p(99.9)=40.55ms 
     http_req_sending...............: avg=120.61µs min=4.43µs   med=8.85µs  max=122.16ms p(90)=18.34µs  p(95)=124.97µs p(99.9)=21.68ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=54.36ms  min=670.5µs  med=45.62ms max=297.76ms p(90)=114.37ms p(95)=141.91ms p(99.9)=213.76ms
     http_reqs......................: 255323  4186.736468/s
     iteration_duration.............: avg=56.02ms  min=1.27ms   med=46.83ms max=330.89ms p(90)=117.8ms  p(95)=146.65ms p(99.9)=228.24ms
     iterations.....................: 254323  4170.338664/s
     success_rate...................: 100.00% ✓ 254323      ✗ 0     
     vus............................: 57      min=0         max=498 
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

     checks.........................: 100.00% ✓ 477294      ✗ 0     
     data_received..................: 14 GB   227 MB/s
     data_sent......................: 192 MB  3.1 MB/s
     http_req_blocked...............: avg=12.53µs  min=882ns   med=2.31µs  max=41.35ms  p(90)=3.98µs   p(95)=5.21µs   p(99.9)=570.04µs
     http_req_connecting............: avg=9.56µs   min=0s      med=0s      max=41.23ms  p(90)=0s       p(95)=0s       p(99.9)=528.71µs
     http_req_duration..............: avg=88.82ms  min=1.32ms  med=83.8ms  max=327.49ms p(90)=174.18ms p(95)=187.86ms p(99.9)=230.66ms
       { expected_response:true }...: avg=88.82ms  min=1.32ms  med=83.8ms  max=327.49ms p(90)=174.18ms p(95)=187.86ms p(99.9)=230.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 160098
     http_req_receiving.............: avg=115.78µs min=26.38µs med=54.37µs max=167.72ms p(90)=155.43µs p(95)=340.6µs  p(99.9)=7.65ms  
     http_req_sending...............: avg=62.66µs  min=4.32µs  med=10.07µs max=274.86ms p(90)=19.7µs   p(95)=119.45µs p(99.9)=7.59ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=88.64ms  min=1.24ms  med=83.62ms max=310.04ms p(90)=173.96ms p(95)=187.66ms p(99.9)=229.79ms
     http_reqs......................: 160098  2597.842901/s
     iteration_duration.............: avg=89.61ms  min=4.46ms  med=84.74ms max=337.19ms p(90)=174.56ms p(95)=188.28ms p(99.9)=231.92ms
     iterations.....................: 159098  2581.616322/s
     success_rate...................: 100.00% ✓ 159098      ✗ 0     
     vus............................: 85      min=0         max=495 
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

     checks.........................: 100.00% ✓ 246861      ✗ 0    
     data_received..................: 7.3 GB  117 MB/s
     data_sent......................: 100 MB  1.6 MB/s
     http_req_blocked...............: avg=6.76µs   min=1.12µs  med=2.9µs    max=25.12ms  p(90)=4.59µs   p(95)=5.55µs   p(99.9)=387.93µs
     http_req_connecting............: avg=3.21µs   min=0s      med=0s       max=25.05ms  p(90)=0s       p(95)=0s       p(99.9)=307.06µs
     http_req_duration..............: avg=171.27ms min=1.99ms  med=143.47ms max=926.55ms p(90)=353.93ms p(95)=413.42ms p(99.9)=701.2ms 
       { expected_response:true }...: avg=171.27ms min=1.99ms  med=143.47ms max=926.55ms p(90)=353.93ms p(95)=413.42ms p(99.9)=701.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 83287
     http_req_receiving.............: avg=80.32µs  min=28.44µs med=62.97µs  max=180.81ms p(90)=98.8µs   p(95)=113.85µs p(99.9)=1.64ms  
     http_req_sending...............: avg=31.17µs  min=5.3µs   med=12.56µs  max=57.98ms  p(90)=18.45µs  p(95)=21.88µs  p(99.9)=3.97ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=171.16ms min=1.94ms  med=143.33ms max=926.47ms p(90)=353.81ms p(95)=413.32ms p(99.9)=700.78ms
     http_reqs......................: 83287   1332.953032/s
     iteration_duration.............: avg=173.6ms  min=5.36ms  med=146.08ms max=926.75ms p(90)=355.3ms  p(95)=414.54ms p(99.9)=702.28ms
     iterations.....................: 82287   1316.948697/s
     success_rate...................: 100.00% ✓ 82287       ✗ 0    
     vus............................: 79      min=0         max=493
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

     checks.........................: 100.00% ✓ 238899      ✗ 0    
     data_received..................: 7.1 GB  113 MB/s
     data_sent......................: 97 MB   1.6 MB/s
     http_req_blocked...............: avg=5.92µs   min=1.1µs   med=2.74µs   max=19.11ms  p(90)=4.35µs   p(95)=5.24µs   p(99.9)=355.36µs
     http_req_connecting............: avg=2.57µs   min=0s      med=0s       max=19.06ms  p(90)=0s       p(95)=0s       p(99.9)=256.04µs
     http_req_duration..............: avg=176.92ms min=2.01ms  med=173.07ms max=588.58ms p(90)=334.7ms  p(95)=359.23ms p(99.9)=460.37ms
       { expected_response:true }...: avg=176.92ms min=2.01ms  med=173.07ms max=588.58ms p(90)=334.7ms  p(95)=359.23ms p(99.9)=460.37ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 80633
     http_req_receiving.............: avg=77.55µs  min=28.21µs med=61.7µs   max=89.21ms  p(90)=99.01µs  p(95)=115.03µs p(99.9)=1.31ms  
     http_req_sending...............: avg=29.73µs  min=4.87µs  med=11.31µs  max=117.37ms p(90)=17.25µs  p(95)=20.68µs  p(99.9)=3.21ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=176.81ms min=1.95ms  med=172.98ms max=588.49ms p(90)=334.6ms  p(95)=359.13ms p(99.9)=460.26ms
     http_reqs......................: 80633   1291.19649/s
     iteration_duration.............: avg=179.38ms min=5.29ms  med=175.82ms max=588.78ms p(90)=335.55ms p(95)=359.92ms p(99.9)=460.85ms
     iterations.....................: 79633   1275.183239/s
     success_rate...................: 100.00% ✓ 79633       ✗ 0    
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

     checks.........................: 100.00% ✓ 92574      ✗ 0    
     data_received..................: 2.8 GB  43 MB/s
     data_sent......................: 38 MB   592 kB/s
     http_req_blocked...............: avg=6.65µs   min=1.02µs  med=2.42µs   max=6.67ms  p(90)=4.09µs   p(95)=5.06µs   p(99.9)=587.96µs
     http_req_connecting............: avg=3.19µs   min=0s      med=0s       max=6.59ms  p(90)=0s       p(95)=0s       p(99.9)=561.15µs
     http_req_duration..............: avg=450.93ms min=3.75ms  med=415.4ms  max=1.66s   p(90)=893.07ms p(95)=972.61ms p(99.9)=1.44s   
       { expected_response:true }...: avg=450.93ms min=3.75ms  med=415.4ms  max=1.66s   p(90)=893.07ms p(95)=972.61ms p(99.9)=1.44s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 31858
     http_req_receiving.............: avg=77.3µs   min=30.29µs med=67.69µs  max=8.34ms  p(90)=104.79µs p(95)=118.59µs p(99.9)=896.82µs
     http_req_sending...............: avg=23.87µs  min=5.15µs  med=12.3µs   max=50.35ms p(90)=18.76µs  p(95)=21.12µs  p(99.9)=2.19ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=450.83ms min=3.7ms   med=415.28ms max=1.66s   p(90)=892.97ms p(95)=972.5ms  p(99.9)=1.44s   
     http_reqs......................: 31858   493.486369/s
     iteration_duration.............: avg=465.76ms min=29.37ms med=434.89ms max=1.66s   p(90)=897.46ms p(95)=976.46ms p(99.9)=1.44s   
     iterations.....................: 30858   477.996182/s
     success_rate...................: 100.00% ✓ 30858      ✗ 0    
     vus............................: 83      min=0        max=500
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

     checks.........................: 100.00% ✓ 46392      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   293 kB/s
     http_req_blocked...............: avg=11.96µs  min=1.01µs  med=3.08µs   max=10.66ms p(90)=4.81µs   p(95)=6.34µs   p(99.9)=1.67ms  
     http_req_connecting............: avg=7.32µs   min=0s      med=0s       max=10.58ms p(90)=0s       p(95)=0s       p(99.9)=1.64ms  
     http_req_duration..............: avg=884.64ms min=5.58ms  med=804.53ms max=5.07s   p(90)=1.78s    p(95)=1.97s    p(99.9)=4.04s   
       { expected_response:true }...: avg=884.64ms min=5.58ms  med=804.53ms max=5.07s   p(90)=1.78s    p(95)=1.97s    p(99.9)=4.04s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16464
     http_req_receiving.............: avg=91.67µs  min=34.28µs med=86.96µs  max=6.89ms  p(90)=121.98µs p(95)=136.68µs p(99.9)=846.22µs
     http_req_sending...............: avg=24.04µs  min=5.37µs  med=16.3µs   max=9.23ms  p(90)=21.34µs  p(95)=24.47µs  p(99.9)=2.76ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=884.53ms min=5.49ms  med=803.9ms  max=5.07s   p(90)=1.78s    p(95)=1.97s    p(99.9)=4.04s   
     http_reqs......................: 16464   244.3856/s
     iteration_duration.............: avg=941.82ms min=43.13ms med=864.32ms max=5.08s   p(90)=1.79s    p(95)=1.98s    p(99.9)=4.09s   
     iterations.....................: 15464   229.541966/s
     success_rate...................: 100.00% ✓ 15464      ✗ 0    
     vus............................: 75      min=0        max=500
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

     checks.........................: 100.00% ✓ 46032      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   286 kB/s
     http_req_blocked...............: avg=10.76µs  min=1.12µs  med=3.04µs   max=10.85ms  p(90)=4.59µs   p(95)=6.01µs   p(99.9)=1.02ms  
     http_req_connecting............: avg=6.18µs   min=0s      med=0s       max=10.79ms  p(90)=0s       p(95)=0s       p(99.9)=988.57µs
     http_req_duration..............: avg=888.12ms min=7.57ms  med=808.43ms max=3.09s    p(90)=1.78s    p(95)=1.93s    p(99.9)=2.77s   
       { expected_response:true }...: avg=888.12ms min=7.57ms  med=808.43ms max=3.09s    p(90)=1.78s    p(95)=1.93s    p(99.9)=2.77s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16344
     http_req_receiving.............: avg=88.81µs  min=31.88µs med=83.76µs  max=4.53ms   p(90)=121.05µs p(95)=135.04µs p(99.9)=956.59µs
     http_req_sending...............: avg=36.7µs   min=5.1µs   med=15.72µs  max=107.53ms p(90)=20.54µs  p(95)=24.15µs  p(99.9)=4.02ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=887.99ms min=7.5ms   med=808.33ms max=3.09s    p(90)=1.78s    p(95)=1.93s    p(99.9)=2.77s   
     http_reqs......................: 16344   238.481377/s
     iteration_duration.............: avg=945.94ms min=20.63ms med=873.39ms max=3.1s     p(90)=1.81s    p(95)=1.94s    p(99.9)=2.78s   
     iterations.....................: 15344   223.890005/s
     success_rate...................: 100.00% ✓ 15344      ✗ 0    
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

