## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.10 | 4,776 | 4,778 | 4,754 | 0.2% | 409 MB | 87.8 KB |  |
| fusion-net-11 | 16.7.5 | 4,642 | 4,778 | 4,601 | 1.5% | 421 MB | 92.9 KB |  |
| fusion-fed-net-11 | 16.7.5 | 4,591 | 4,604 | 4,463 | 1.5% | 421 MB | 93.9 KB |  |
| fusion-aot-11 | 16.7.5 | 4,582 | 4,623 | 4,523 | 0.8% | 160 MB | 35.7 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.10 | 4,436 | 4,450 | 4,432 | 0.2% | 183 MB | 42.3 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.10 | 4,393 | 4,432 | 4,373 | 0.5% | 411 MB | 95.7 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.10 | 4,384 | 4,404 | 4,376 | 0.2% | 192 MB | 44.8 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 4,308 | 4,315 | 4,297 | 0.2% | 167 MB | 39.7 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,997 | 4,049 | 3,941 | 1.2% | 2,294 MB | 587.6 KB |  |
| hive-router | v0.3.10 | 2,606 | 2,636 | 2,597 | 0.6% | 169 MB | 66.4 KB |  |
| cosmo | 0.365.2 | 1,333 | 1,339 | 1,320 | 0.6% | 542 MB | 416.7 KB |  |
| caliban | 3.2.0 | 1,324 | 1,325 | 1,324 | 0.0% | 11,056 MB | 8,550.9 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 495 | 496 | 490 | 0.5% | 3,167 MB | 6,551.9 KB |  |
| hive-gateway | 2.15.6 | 245 | 246 | 243 | 0.5% | 3,851 MB | 16,096.1 KB |  |
| apollo-gateway | 2.14.4 | 241 | 243 | 241 | 0.4% | 2,490 MB | 10,580.8 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (7073 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (6075 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (162408 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 870621      ✗ 0     
     data_received..................: 26 GB   418 MB/s
     data_sent......................: 350 MB  5.7 MB/s
     http_req_blocked...............: avg=64.25µs  min=792ns    med=2.05µs  max=132.39ms p(90)=3.65µs   p(95)=4.78µs   p(99.9)=24.26ms 
     http_req_connecting............: avg=60.1µs   min=0s       med=0s      max=124.98ms p(90)=0s       p(95)=0s       p(99.9)=23.7ms  
     http_req_duration..............: avg=47.19ms  min=776.56µs med=39.79ms max=295.07ms p(90)=98.99ms  p(95)=122.19ms p(99.9)=178.34ms
       { expected_response:true }...: avg=47.19ms  min=776.56µs med=39.79ms max=295.07ms p(90)=98.99ms  p(95)=122.19ms p(99.9)=178.34ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 291207
     http_req_receiving.............: avg=328.93µs min=25.36µs  med=51.28µs max=181.98ms p(90)=205.61µs p(95)=357.21µs p(99.9)=45.33ms 
     http_req_sending...............: avg=150.24µs min=4.01µs   med=8.46µs  max=250.02ms p(90)=16.37µs  p(95)=115.05µs p(99.9)=26.33ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.71ms  min=734.83µs med=39.48ms max=286.62ms p(90)=97.93ms  p(95)=120.92ms p(99.9)=172.46ms
     http_reqs......................: 291207  4776.443195/s
     iteration_duration.............: avg=49.08ms  min=1.39ms   med=40.64ms max=330.92ms p(90)=103.77ms p(95)=128.24ms p(99.9)=200.62ms
     iterations.....................: 290207  4760.040969/s
     success_rate...................: 100.00% ✓ 290207      ✗ 0     
     vus............................: 55      min=0         max=498 
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

     checks.........................: 100.00% ✓ 845703      ✗ 0     
     data_received..................: 25 GB   406 MB/s
     data_sent......................: 340 MB  5.6 MB/s
     http_req_blocked...............: avg=72.46µs  min=982ns    med=2.59µs  max=135.89ms p(90)=4.12µs   p(95)=5.32µs   p(99.9)=27.29ms 
     http_req_connecting............: avg=68.22µs  min=0s       med=0s      max=135.84ms p(90)=0s       p(95)=0s       p(99.9)=26.84ms 
     http_req_duration..............: avg=48.6ms   min=759.89µs med=41.09ms max=341.15ms p(90)=101.44ms p(95)=125.63ms p(99.9)=183.8ms 
       { expected_response:true }...: avg=48.6ms   min=759.89µs med=41.09ms max=341.15ms p(90)=101.44ms p(95)=125.63ms p(99.9)=183.8ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 282901
     http_req_receiving.............: avg=378.81µs min=24.97µs  med=53.52µs max=154.79ms p(90)=218.77µs p(95)=372.41µs p(99.9)=49.63ms 
     http_req_sending...............: avg=169.29µs min=4.18µs   med=9.29µs  max=208.63ms p(90)=17.58µs  p(95)=120.2µs  p(99.9)=31.22ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.05ms  min=715.37µs med=40.75ms max=340.93ms p(90)=100.11ms p(95)=124.11ms p(99.9)=178.14ms
     http_reqs......................: 282901  4642.668917/s
     iteration_duration.............: avg=50.53ms  min=1.21ms   med=41.86ms max=359.85ms p(90)=106.15ms p(95)=132.86ms p(99.9)=209.34ms
     iterations.....................: 281901  4626.257986/s
     success_rate...................: 100.00% ✓ 281901      ✗ 0     
     vus............................: 54      min=0         max=499 
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

     checks.........................: 100.00% ✓ 838683      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 337 MB  5.5 MB/s
     http_req_blocked...............: avg=60.85µs  min=791ns    med=2.14µs  max=125.99ms p(90)=3.81µs   p(95)=4.97µs   p(99.9)=22.69ms 
     http_req_connecting............: avg=57.51µs  min=0s       med=0s      max=125.95ms p(90)=0s       p(95)=0s       p(99.9)=22.3ms  
     http_req_duration..............: avg=49.14ms  min=898.79µs med=41.35ms max=268.58ms p(90)=103.68ms p(95)=128.52ms p(99.9)=179.39ms
       { expected_response:true }...: avg=49.14ms  min=898.79µs med=41.35ms max=268.58ms p(90)=103.68ms p(95)=128.52ms p(99.9)=179.39ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280561
     http_req_receiving.............: avg=351.69µs min=22.32µs  med=52.32µs max=138.47ms p(90)=216.28µs p(95)=374.43µs p(99.9)=52.94ms 
     http_req_sending...............: avg=147.53µs min=4.4µs    med=8.85µs  max=177.27ms p(90)=18.12µs  p(95)=120.25µs p(99.9)=26.24ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.64ms  min=856.47µs med=41.03ms max=254.04ms p(90)=102.31ms p(95)=127.29ms p(99.9)=175.2ms 
     http_reqs......................: 280561  4591.815711/s
     iteration_duration.............: avg=50.95ms  min=1.45ms   med=42.2ms  max=379.11ms p(90)=107.93ms p(95)=134.79ms p(99.9)=205.89ms
     iterations.....................: 279561  4575.449161/s
     success_rate...................: 100.00% ✓ 279561      ✗ 0     
     vus............................: 61      min=0         max=497 
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

     checks.........................: 100.00% ✓ 835842      ✗ 0     
     data_received..................: 25 GB   401 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=53.1µs   min=831ns    med=2.03µs  max=120.32ms p(90)=3.61µs   p(95)=4.71µs   p(99.9)=16.8ms  
     http_req_connecting............: avg=49.69µs  min=0s       med=0s      max=120.04ms p(90)=0s       p(95)=0s       p(99.9)=16.53ms 
     http_req_duration..............: avg=49.73ms  min=839.22µs med=41.86ms max=301.43ms p(90)=105.57ms p(95)=129.91ms p(99.9)=182.83ms
       { expected_response:true }...: avg=49.73ms  min=839.22µs med=41.86ms max=301.43ms p(90)=105.57ms p(95)=129.91ms p(99.9)=182.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 279614
     http_req_receiving.............: avg=283.04µs min=24.96µs  med=49.35µs max=169.61ms p(90)=216.09µs p(95)=372.35µs p(99.9)=39.3ms  
     http_req_sending...............: avg=126.32µs min=4.15µs   med=8.46µs  max=206.41ms p(90)=17.25µs  p(95)=122.02µs p(99.9)=22.21ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.32ms  min=792.31µs med=41.6ms  max=284.3ms  p(90)=104.69ms p(95)=128.85ms p(99.9)=178.88ms
     http_reqs......................: 279614  4582.363013/s
     iteration_duration.............: avg=51.12ms  min=1.24ms   med=42.69ms max=330.64ms p(90)=108.23ms p(95)=133.46ms p(99.9)=200.27ms
     iterations.....................: 278614  4565.974838/s
     success_rate...................: 100.00% ✓ 278614      ✗ 0     
     vus............................: 58      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 809469      ✗ 0     
     data_received..................: 24 GB   388 MB/s
     data_sent......................: 325 MB  5.3 MB/s
     http_req_blocked...............: avg=43.2µs   min=802ns    med=2.01µs  max=88.74ms  p(90)=3.5µs    p(95)=4.58µs   p(99.9)=12.65ms 
     http_req_connecting............: avg=39.93µs  min=0s       med=0s      max=88.68ms  p(90)=0s       p(95)=0s       p(99.9)=11.86ms 
     http_req_duration..............: avg=51.78ms  min=859.06µs med=43.73ms max=278.03ms p(90)=109.29ms p(95)=135.12ms p(99.9)=186.28ms
       { expected_response:true }...: avg=51.78ms  min=859.06µs med=43.73ms max=278.03ms p(90)=109.29ms p(95)=135.12ms p(99.9)=186.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 270823
     http_req_receiving.............: avg=259.99µs min=25.39µs  med=50.13µs max=117.31ms p(90)=220.09µs p(95)=373.23µs p(99.9)=33.25ms 
     http_req_sending...............: avg=113.24µs min=4.25µs   med=8.49µs  max=90ms     p(90)=16.73µs  p(95)=121.43µs p(99.9)=19.96ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.41ms  min=817.48µs med=43.46ms max=277.63ms p(90)=108.5ms  p(95)=134.16ms p(99.9)=183.71ms
     http_reqs......................: 270823  4436.22588/s
     iteration_duration.............: avg=52.8ms   min=1.44ms   med=44.52ms max=308.78ms p(90)=111.11ms p(95)=137.41ms p(99.9)=204.19ms
     iterations.....................: 269823  4419.845344/s
     success_rate...................: 100.00% ✓ 269823      ✗ 0     
     vus............................: 60      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 802752      ✗ 0     
     data_received..................: 24 GB   385 MB/s
     data_sent......................: 323 MB  5.3 MB/s
     http_req_blocked...............: avg=69.85µs min=911ns    med=2.74µs  max=150.54ms p(90)=4.41µs   p(95)=5.58µs   p(99.9)=27.32ms 
     http_req_connecting............: avg=65.11µs min=0s       med=0s      max=150.48ms p(90)=0s       p(95)=0s       p(99.9)=26.14ms 
     http_req_duration..............: avg=51.06ms min=915.64µs med=42.49ms max=289.55ms p(90)=108.47ms p(95)=135.71ms p(99.9)=189.63ms
       { expected_response:true }...: avg=51.06ms min=915.64µs med=42.49ms max=289.55ms p(90)=108.47ms p(95)=135.71ms p(99.9)=189.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 268584
     http_req_receiving.............: avg=353.7µs min=22.12µs  med=55.3µs  max=113.13ms p(90)=223.93µs p(95)=400.2µs  p(99.9)=46.87ms 
     http_req_sending...............: avg=154.2µs min=4.15µs   med=9.61µs  max=143.32ms p(90)=18.63µs  p(95)=127.62µs p(99.9)=27.39ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.55ms min=876.83µs med=42.19ms max=289.22ms p(90)=107.2ms  p(95)=134.32ms p(99.9)=182.16ms
     http_reqs......................: 268584  4393.891423/s
     iteration_duration.............: avg=53.22ms min=1.36ms   med=43.7ms  max=348.47ms p(90)=113.28ms p(95)=142.12ms p(99.9)=230ms   
     iterations.....................: 267584  4377.531955/s
     success_rate...................: 100.00% ✓ 267584      ✗ 0     
     vus............................: 63      min=0         max=496 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 802014      ✗ 0     
     data_received..................: 24 GB   384 MB/s
     data_sent......................: 322 MB  5.3 MB/s
     http_req_blocked...............: avg=44.96µs  min=811ns    med=2.01µs  max=101.03ms p(90)=3.65µs   p(95)=4.77µs   p(99.9)=13ms    
     http_req_connecting............: avg=41.42µs  min=0s       med=0s      max=100.88ms p(90)=0s       p(95)=0s       p(99.9)=12.46ms 
     http_req_duration..............: avg=52.03ms  min=1.01ms   med=43.64ms max=333.99ms p(90)=110.6ms  p(95)=137.12ms p(99.9)=191.7ms 
       { expected_response:true }...: avg=52.03ms  min=1.01ms   med=43.64ms max=333.99ms p(90)=110.6ms  p(95)=137.12ms p(99.9)=191.7ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 268338
     http_req_receiving.............: avg=262.11µs min=24.8µs   med=49.94µs max=227.74ms p(90)=220.17µs p(95)=378.85µs p(99.9)=36.63ms 
     http_req_sending...............: avg=119.37µs min=3.95µs   med=8.4µs   max=88.71ms  p(90)=17.92µs  p(95)=126.13µs p(99.9)=21.02ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.64ms  min=941.31µs med=43.38ms max=308.07ms p(90)=109.75ms p(95)=136.01ms p(99.9)=188.64ms
     http_reqs......................: 268338  4384.145866/s
     iteration_duration.............: avg=53.29ms  min=1.7ms    med=44.52ms max=344.35ms p(90)=112.95ms p(95)=139.83ms p(99.9)=213.65ms
     iterations.....................: 267338  4367.807718/s
     success_rate...................: 100.00% ✓ 267338      ✗ 0     
     vus............................: 67      min=0         max=496 
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

     checks.........................: 100.00% ✓ 787986      ✗ 0     
     data_received..................: 23 GB   377 MB/s
     data_sent......................: 317 MB  5.2 MB/s
     http_req_blocked...............: avg=57.13µs  min=971ns    med=2.56µs  max=122.07ms p(90)=4.34µs   p(95)=5.64µs   p(99.9)=18.59ms 
     http_req_connecting............: avg=53.59µs  min=0s       med=0s      max=121.77ms p(90)=0s       p(95)=0s       p(99.9)=18.53ms 
     http_req_duration..............: avg=52.62ms  min=985.25µs med=44.09ms max=280.01ms p(90)=113.66ms p(95)=141.08ms p(99.9)=194.61ms
       { expected_response:true }...: avg=52.62ms  min=985.25µs med=44.09ms max=280.01ms p(90)=113.66ms p(95)=141.08ms p(99.9)=194.61ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 263662
     http_req_receiving.............: avg=317.84µs min=25.63µs  med=52.07µs max=238.94ms p(90)=232.46µs p(95)=413.59µs p(99.9)=42.16ms 
     http_req_sending...............: avg=143.66µs min=4.5µs    med=9.3µs   max=93.46ms  p(90)=20.36µs  p(95)=135.74µs p(99.9)=24.45ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=52.16ms  min=924.57µs med=43.79ms max=279.95ms p(90)=112.6ms  p(95)=139.87ms p(99.9)=190.63ms
     http_reqs......................: 263662  4308.313051/s
     iteration_duration.............: avg=54.23ms  min=1.51ms   med=44.92ms max=342.26ms p(90)=117.07ms p(95)=145.36ms p(99.9)=219.48ms
     iterations.....................: 262662  4291.972763/s
     success_rate...................: 100.00% ✓ 262662      ✗ 0     
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

     checks.........................: 100.00% ✓ 728178      ✗ 0     
     data_received..................: 21 GB   349 MB/s
     data_sent......................: 293 MB  4.8 MB/s
     http_req_blocked...............: avg=50.85µs  min=891ns    med=2.72µs  max=104.65ms p(90)=4.41µs   p(95)=5.56µs   p(99.9)=14.14ms 
     http_req_connecting............: avg=46.7µs   min=0s       med=0s      max=100.07ms p(90)=0s       p(95)=0s       p(99.9)=13.56ms 
     http_req_duration..............: avg=57.47ms  min=733.07µs med=48.17ms max=345.98ms p(90)=122.49ms p(95)=152.85ms p(99.9)=224.7ms 
       { expected_response:true }...: avg=57.47ms  min=733.07µs med=48.17ms max=345.98ms p(90)=122.49ms p(95)=152.85ms p(99.9)=224.7ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 243726
     http_req_receiving.............: avg=267.59µs min=23.1µs   med=54.13µs max=154.63ms p(90)=228.87µs p(95)=407.94µs p(99.9)=37.47ms 
     http_req_sending...............: avg=131.71µs min=4.6µs    med=9.65µs  max=191.17ms p(90)=19.27µs  p(95)=138.1µs  p(99.9)=23.47ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=57.07ms  min=680.38µs med=47.88ms max=345.47ms p(90)=121.59ms p(95)=151.85ms p(99.9)=221.1ms 
     http_reqs......................: 243726  3997.526198/s
     iteration_duration.............: avg=58.7ms   min=1.42ms   med=48.93ms max=355.98ms p(90)=125.21ms p(95)=155.96ms p(99.9)=239.02ms
     iterations.....................: 242726  3981.124476/s
     success_rate...................: 100.00% ✓ 242726      ✗ 0     
     vus............................: 56      min=0         max=498 
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

     checks.........................: 100.00% ✓ 478536      ✗ 0     
     data_received..................: 14 GB   228 MB/s
     data_sent......................: 193 MB  3.1 MB/s
     http_req_blocked...............: avg=17.67µs  min=902ns   med=2.75µs  max=58.38ms  p(90)=4.47µs   p(95)=5.69µs   p(99.9)=871.91µs
     http_req_connecting............: avg=14.04µs  min=0s      med=0s      max=58.24ms  p(90)=0s       p(95)=0s       p(99.9)=766.38µs
     http_req_duration..............: avg=88.57ms  min=1.31ms  med=82.86ms max=301.98ms p(90)=173.16ms p(95)=187.98ms p(99.9)=234.12ms
       { expected_response:true }...: avg=88.57ms  min=1.31ms  med=82.86ms max=301.98ms p(90)=173.16ms p(95)=187.98ms p(99.9)=234.12ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 160512
     http_req_receiving.............: avg=146.01µs min=27.78µs med=57.05µs max=149.12ms p(90)=192.38µs p(95)=384.19µs p(99.9)=12.71ms 
     http_req_sending...............: avg=72.78µs  min=4.71µs  med=10.71µs max=191ms    p(90)=20.57µs  p(95)=135.47µs p(99.9)=9.16ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=88.35ms  min=1.25ms  med=82.65ms max=287.09ms p(90)=172.91ms p(95)=187.69ms p(99.9)=233.27ms
     http_reqs......................: 160512  2606.642909/s
     iteration_duration.............: avg=89.38ms  min=4.03ms  med=83.76ms max=357.03ms p(90)=173.64ms p(95)=188.39ms p(99.9)=235.81ms
     iterations.....................: 159512  2590.403357/s
     success_rate...................: 100.00% ✓ 159512      ✗ 0     
     vus............................: 83      min=0         max=493 
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

     checks.........................: 100.00% ✓ 246942      ✗ 0    
     data_received..................: 7.3 GB  117 MB/s
     data_sent......................: 100 MB  1.6 MB/s
     http_req_blocked...............: avg=6.59µs   min=1.03µs med=2.8µs    max=25.37ms  p(90)=4.55µs   p(95)=5.51µs   p(99.9)=428.46µs
     http_req_connecting............: avg=3.04µs   min=0s     med=0s       max=21.23ms  p(90)=0s       p(95)=0s       p(99.9)=367.34µs
     http_req_duration..............: avg=171.18ms min=2.01ms med=170.19ms max=534.51ms p(90)=324.38ms p(95)=348.12ms p(99.9)=418.28ms
       { expected_response:true }...: avg=171.18ms min=2.01ms med=170.19ms max=534.51ms p(90)=324.38ms p(95)=348.12ms p(99.9)=418.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 83314
     http_req_receiving.............: avg=81.2µs   min=26.8µs med=61.5µs   max=129.91ms p(90)=99.69µs  p(95)=115.93µs p(99.9)=1.45ms  
     http_req_sending...............: avg=33.35µs  min=4.76µs med=11.62µs  max=143.81ms p(90)=18.48µs  p(95)=22.32µs  p(99.9)=3.68ms  
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=171.06ms min=1.95ms med=170.04ms max=534.45ms p(90)=324.29ms p(95)=348.03ms p(99.9)=418.22ms
     http_reqs......................: 83314   1333.722645/s
     iteration_duration.............: avg=173.5ms  min=4.5ms  med=172.71ms max=534.7ms  p(90)=325.19ms p(95)=348.72ms p(99.9)=418.58ms
     iterations.....................: 82314   1317.71426/s
     success_rate...................: 100.00% ✓ 82314       ✗ 0    
     vus............................: 78      min=0         max=493
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

     checks.........................: 100.00% ✓ 245208      ✗ 0    
     data_received..................: 7.2 GB  116 MB/s
     data_sent......................: 99 MB   1.6 MB/s
     http_req_blocked...............: avg=4.32µs   min=941ns   med=2.21µs   max=9.19ms   p(90)=3.68µs   p(95)=4.52µs   p(99.9)=228.36µs
     http_req_connecting............: avg=1.53µs   min=0s      med=0s       max=9.11ms   p(90)=0s       p(95)=0s       p(99.9)=166.41µs
     http_req_duration..............: avg=172.49ms min=1.97ms  med=139.16ms max=950.13ms p(90)=365.09ms p(95)=431.07ms p(99.9)=694.5ms 
       { expected_response:true }...: avg=172.49ms min=1.97ms  med=139.16ms max=950.13ms p(90)=365.09ms p(95)=431.07ms p(99.9)=694.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 82736
     http_req_receiving.............: avg=71.25µs  min=28.03µs med=56.28µs  max=134.11ms p(90)=88.38µs  p(95)=102.51µs p(99.9)=1.83ms  
     http_req_sending...............: avg=26.09µs  min=4.87µs  med=10.29µs  max=89.14ms  p(90)=15.97µs  p(95)=19.11µs  p(99.9)=3.32ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=172.4ms  min=1.92ms  med=139.06ms max=950.05ms p(90)=364.94ms p(95)=431ms    p(99.9)=694.42ms
     http_reqs......................: 82736   1324.746371/s
     iteration_duration.............: avg=174.83ms min=7.17ms  med=142.03ms max=950.29ms p(90)=366.57ms p(95)=432.59ms p(99.9)=695.55ms
     iterations.....................: 81736   1308.734642/s
     success_rate...................: 100.00% ✓ 81736       ✗ 0    
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

     checks.........................: 100.00% ✓ 93264      ✗ 0    
     data_received..................: 2.8 GB  43 MB/s
     data_sent......................: 39 MB   595 kB/s
     http_req_blocked...............: avg=10.23µs  min=1.26µs  med=3.31µs   max=23.5ms   p(90)=5µs      p(95)=6.07µs   p(99.9)=1.71ms
     http_req_connecting............: avg=5.82µs   min=0s      med=0s       max=23.43ms  p(90)=0s       p(95)=0s       p(99.9)=1.66ms
     http_req_duration..............: avg=447.58ms min=3.87ms  med=413.94ms max=2.04s    p(90)=893.87ms p(95)=975.71ms p(99.9)=1.44s 
       { expected_response:true }...: avg=447.58ms min=3.87ms  med=413.94ms max=2.04s    p(90)=893.87ms p(95)=975.71ms p(99.9)=1.44s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 32088
     http_req_receiving.............: avg=152.77µs min=29.92µs med=73.55µs  max=144.83ms p(90)=111.01µs p(95)=125.9µs  p(99.9)=25.3ms
     http_req_sending...............: avg=30.63µs  min=5.71µs  med=14.67µs  max=85.03ms  p(90)=21.19µs  p(95)=23.95µs  p(99.9)=2.18ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=447.39ms min=3.79ms  med=413.83ms max=2.04s    p(90)=893.74ms p(95)=975.61ms p(99.9)=1.44s 
     http_reqs......................: 32088   495.95913/s
     iteration_duration.............: avg=462.2ms  min=16.78ms med=431.94ms max=2.04s    p(90)=897.71ms p(95)=979.22ms p(99.9)=1.45s 
     iterations.....................: 31088   480.502911/s
     success_rate...................: 100.00% ✓ 31088      ✗ 0    
     vus............................: 88      min=0        max=500
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

     checks.........................: 100.00% ✓ 46920      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 20 MB   295 kB/s
     http_req_blocked...............: avg=14.83µs  min=1.12µs  med=3.27µs   max=14.89ms p(90)=5.03µs   p(95)=6.55µs   p(99.9)=2.24ms
     http_req_connecting............: avg=10µs     min=0s      med=0s       max=14.83ms p(90)=0s       p(95)=0s       p(99.9)=2.22ms
     http_req_duration..............: avg=875.43ms min=5.77ms  med=781.52ms max=4.9s    p(90)=1.75s    p(95)=1.94s    p(99.9)=4.04s 
       { expected_response:true }...: avg=875.43ms min=5.77ms  med=781.52ms max=4.9s    p(90)=1.75s    p(95)=1.94s    p(99.9)=4.04s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16640
     http_req_receiving.............: avg=109.19µs min=33.72µs med=88.79µs  max=90.63ms p(90)=126.11µs p(95)=141.98µs p(99.9)=1.43ms
     http_req_sending...............: avg=30.73µs  min=5.15µs  med=16.41µs  max=27.34ms p(90)=21.54µs  p(95)=25.09µs  p(99.9)=4.04ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=875.29ms min=5.69ms  med=781.43ms max=4.9s    p(90)=1.75s    p(95)=1.94s    p(99.9)=4.04s 
     http_reqs......................: 16640   245.443275/s
     iteration_duration.............: avg=931.42ms min=47.39ms med=845.83ms max=4.91s   p(90)=1.77s    p(95)=1.96s    p(99.9)=4.08s 
     iterations.....................: 15640   230.693078/s
     success_rate...................: 100.00% ✓ 15640      ✗ 0    
     vus............................: 85      min=0        max=500
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

     checks.........................: 100.00% ✓ 46545      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   290 kB/s
     http_req_blocked...............: avg=15.8µs   min=1.13µs  med=2.98µs   max=33.62ms  p(90)=4.64µs   p(95)=6.13µs   p(99.9)=2.15ms
     http_req_connecting............: avg=11.15µs  min=0s      med=0s       max=33.2ms   p(90)=0s       p(95)=0s       p(99.9)=2.06ms
     http_req_duration..............: avg=878.45ms min=7.51ms  med=801.79ms max=2.93s    p(90)=1.79s    p(95)=1.92s    p(99.9)=2.66s 
       { expected_response:true }...: avg=878.45ms min=7.51ms  med=801.79ms max=2.93s    p(90)=1.79s    p(95)=1.92s    p(99.9)=2.66s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16515
     http_req_receiving.............: avg=112.33µs min=30.89µs med=84.7µs   max=179.85ms p(90)=123.35µs p(95)=139.76µs p(99.9)=1.09ms
     http_req_sending...............: avg=46.27µs  min=5.52µs  med=15.83µs  max=144.36ms p(90)=21.03µs  p(95)=24.4µs   p(99.9)=1.51ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=878.29ms min=7.42ms  med=801.6ms  max=2.93s    p(90)=1.79s    p(95)=1.92s    p(99.9)=2.66s 
     http_reqs......................: 16515   241.217667/s
     iteration_duration.............: avg=935.08ms min=29.43ms med=878.12ms max=2.94s    p(90)=1.8s     p(95)=1.93s    p(99.9)=2.68s 
     iterations.....................: 15515   226.611693/s
     success_rate...................: 100.00% ✓ 15515      ✗ 0    
     vus............................: 80      min=0        max=499
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

