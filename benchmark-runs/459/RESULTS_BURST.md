## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.7 | 4,750 | 4,762 | 4,745 | 0.1% | 439 MB | 94.7 KB |  |
| fusion-net-11 | 16.7.3 | 4,691 | 4,708 | 4,594 | 1.0% | 436 MB | 95.1 KB |  |
| fusion-aot-11 | 16.7.3 | 4,597 | 4,604 | 4,580 | 0.2% | 173 MB | 38.5 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,580 | 4,591 | 4,578 | 0.1% | 425 MB | 95.1 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.7 | 4,544 | 4,569 | 4,529 | 0.4% | 408 MB | 92.0 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.7 | 4,458 | 4,486 | 4,441 | 0.4% | 192 MB | 44.1 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,404 | 4,414 | 4,377 | 0.3% | 179 MB | 41.6 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.7 | 4,333 | 4,342 | 4,322 | 0.2% | 178 MB | 42.2 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,090 | 4,159 | 4,008 | 1.6% | 2,292 MB | 574.0 KB |  |
| hive-router | v0.3.6 | 2,575 | 2,583 | 2,570 | 0.2% | 199 MB | 79.1 KB |  |
| caliban | 3.2.0 | 1,385 | 1,386 | 1,383 | 0.1% | 10,809 MB | 7,991.6 KB |  |
| cosmo | 0.363.0 | 1,371 | 1,374 | 1,365 | 0.2% | 690 MB | 515.0 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 497 | 500 | 493 | 0.5% | 3,186 MB | 6,564.9 KB |  |
| hive-gateway | 2.15.3 | 246 | 247 | 242 | 0.9% | 3,848 MB | 16,018.0 KB |  |
| apollo-gateway | 2.14.4 | 241 | 241 | 239 | 0.4% | 2,412 MB | 10,249.6 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (9936 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (3455 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (110087 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 865845      ✗ 0     
     data_received..................: 25 GB   416 MB/s
     data_sent......................: 348 MB  5.7 MB/s
     http_req_blocked...............: avg=62.41µs  min=791ns    med=2.04µs  max=147.1ms  p(90)=3.6µs    p(95)=4.68µs   p(99.9)=22.5ms  
     http_req_connecting............: avg=58.97µs  min=0s       med=0s      max=143.88ms p(90)=0s       p(95)=0s       p(99.9)=21.83ms 
     http_req_duration..............: avg=47.57ms  min=778.9µs  med=40.23ms max=314.56ms p(90)=99.98ms  p(95)=123.88ms p(99.9)=175.3ms 
       { expected_response:true }...: avg=47.57ms  min=778.9µs  med=40.23ms max=314.56ms p(90)=99.98ms  p(95)=123.88ms p(99.9)=175.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 289615
     http_req_receiving.............: avg=341.62µs min=25.12µs  med=51.16µs max=185.72ms p(90)=208.19µs p(95)=360.34µs p(99.9)=45.35ms 
     http_req_sending...............: avg=145.56µs min=4.17µs   med=8.65µs  max=276.1ms  p(90)=16.74µs  p(95)=114.07µs p(99.9)=25.58ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.09ms  min=725.96µs med=39.93ms max=301.4ms  p(90)=98.86ms  p(95)=122.54ms p(99.9)=169.22ms
     http_reqs......................: 289615  4750.459969/s
     iteration_duration.............: avg=49.33ms  min=1.3ms    med=40.93ms max=350.48ms p(90)=104.21ms p(95)=129.56ms p(99.9)=200.01ms
     iterations.....................: 288615  4734.057297/s
     success_rate...................: 100.00% ✓ 288615      ✗ 0     
     vus............................: 56      min=0         max=498 
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

     checks.........................: 100.00% ✓ 854655      ✗ 0     
     data_received..................: 25 GB   411 MB/s
     data_sent......................: 344 MB  5.6 MB/s
     http_req_blocked...............: avg=62.74µs  min=832ns    med=2.09µs  max=135.03ms p(90)=3.63µs   p(95)=4.71µs   p(99.9)=21.72ms 
     http_req_connecting............: avg=59.37µs  min=0s       med=0s      max=134.92ms p(90)=0s       p(95)=0s       p(99.9)=21.35ms 
     http_req_duration..............: avg=48.05ms  min=758.51µs med=40.57ms max=330.89ms p(90)=101.16ms p(95)=125.18ms p(99.9)=182.92ms
       { expected_response:true }...: avg=48.05ms  min=758.51µs med=40.57ms max=330.89ms p(90)=101.16ms p(95)=125.18ms p(99.9)=182.92ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 285885
     http_req_receiving.............: avg=364.48µs min=22.76µs  med=51.78µs max=200.42ms p(90)=210.08µs p(95)=367.49µs p(99.9)=51.15ms 
     http_req_sending...............: avg=148.55µs min=4.13µs   med=8.56µs  max=258.23ms p(90)=16.64µs  p(95)=116µs    p(99.9)=26.46ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.54ms  min=720.2µs  med=40.26ms max=330.44ms p(90)=99.99ms  p(95)=123.74ms p(99.9)=175.94ms
     http_reqs......................: 285885  4691.415016/s
     iteration_duration.............: avg=50ms     min=1.24ms   med=41.6ms  max=340.09ms p(90)=105.35ms p(95)=130.92ms p(99.9)=213.24ms
     iterations.....................: 284885  4675.004868/s
     success_rate...................: 100.00% ✓ 284885      ✗ 0     
     vus............................: 54      min=0         max=499 
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

     checks.........................: 100.00% ✓ 838524      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 337 MB  5.5 MB/s
     http_req_blocked...............: avg=55.56µs  min=811ns    med=2.08µs  max=139.94ms p(90)=3.73µs   p(95)=4.87µs   p(99.9)=19.6ms  
     http_req_connecting............: avg=52.33µs  min=0s       med=0s      max=139.71ms p(90)=0s       p(95)=0s       p(99.9)=17.97ms 
     http_req_duration..............: avg=49.18ms  min=826.13µs med=41.16ms max=323.93ms p(90)=105.31ms p(95)=130.54ms p(99.9)=181.52ms
       { expected_response:true }...: avg=49.18ms  min=826.13µs med=41.16ms max=323.93ms p(90)=105.31ms p(95)=130.54ms p(99.9)=181.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280508
     http_req_receiving.............: avg=300.65µs min=24.31µs  med=49.45µs max=93.06ms  p(90)=215.78µs p(95)=373.34µs p(99.9)=41.51ms 
     http_req_sending...............: avg=131.82µs min=4.1µs    med=8.62µs  max=262ms    p(90)=17.28µs  p(95)=121.03µs p(99.9)=24.25ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.75ms  min=782.92µs med=40.9ms  max=303.22ms p(90)=104.4ms  p(95)=129.51ms p(99.9)=176.75ms
     http_reqs......................: 280508  4597.109962/s
     iteration_duration.............: avg=50.95ms  min=1.23ms   med=42.22ms max=333.15ms p(90)=109.06ms p(95)=134.77ms p(99.9)=217.7ms 
     iterations.....................: 279508  4580.721445/s
     success_rate...................: 100.00% ✓ 279508      ✗ 0     
     vus............................: 58      min=0         max=498 
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

     checks.........................: 100.00% ✓ 837033      ✗ 0     
     data_received..................: 25 GB   401 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=55.37µs  min=791ns    med=2.02µs  max=196.04ms p(90)=3.63µs   p(95)=4.8µs    p(99.9)=19.64ms 
     http_req_connecting............: avg=52.06µs  min=0s       med=0s      max=195.95ms p(90)=0s       p(95)=0s       p(99.9)=19.07ms 
     http_req_duration..............: avg=49.45ms  min=899.9µs  med=41.55ms max=264.08ms p(90)=105.2ms  p(95)=130.46ms p(99.9)=180.79ms
       { expected_response:true }...: avg=49.45ms  min=899.9µs  med=41.55ms max=264.08ms p(90)=105.2ms  p(95)=130.46ms p(99.9)=180.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280011
     http_req_receiving.............: avg=337.45µs min=25.18µs  med=51.57µs max=86.91ms  p(90)=215.6µs  p(95)=375.94µs p(99.9)=47.21ms 
     http_req_sending...............: avg=137.17µs min=4.16µs   med=8.47µs  max=231.62ms p(90)=17.81µs  p(95)=120.09µs p(99.9)=25.01ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.98ms  min=861.59µs med=41.24ms max=255.11ms p(90)=104ms    p(95)=129.3ms  p(99.9)=176.26ms
     http_reqs......................: 280011  4580.256048/s
     iteration_duration.............: avg=51.05ms  min=1.41ms   med=42.48ms max=343.51ms p(90)=108.64ms p(95)=134.8ms  p(99.9)=212.89ms
     iterations.....................: 279011  4563.898633/s
     success_rate...................: 100.00% ✓ 279011      ✗ 0     
     vus............................: 62      min=0         max=497 
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

     checks.........................: 100.00% ✓ 830397      ✗ 0     
     data_received..................: 24 GB   398 MB/s
     data_sent......................: 334 MB  5.5 MB/s
     http_req_blocked...............: avg=60.54µs  min=751ns    med=2.13µs  max=127.2ms  p(90)=3.83µs   p(95)=5µs      p(99.9)=22.08ms 
     http_req_connecting............: avg=57.38µs  min=0s       med=0s      max=124.68ms p(90)=0s       p(95)=0s       p(99.9)=21.21ms 
     http_req_duration..............: avg=49.61ms  min=903.34µs med=41.78ms max=285.37ms p(90)=104.63ms p(95)=129.63ms p(99.9)=179.09ms
       { expected_response:true }...: avg=49.61ms  min=903.34µs med=41.78ms max=285.37ms p(90)=104.63ms p(95)=129.63ms p(99.9)=179.09ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 277799
     http_req_receiving.............: avg=317.12µs min=22.64µs  med=53.48µs max=134.7ms  p(90)=212.55µs p(95)=373.91µs p(99.9)=45.3ms  
     http_req_sending...............: avg=150.71µs min=4.37µs   med=8.89µs  max=154.71ms p(90)=17.85µs  p(95)=119.9µs  p(99.9)=26.84ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.14ms  min=859.49µs med=41.48ms max=284.8ms  p(90)=103.56ms p(95)=128.42ms p(99.9)=174.17ms
     http_reqs......................: 277799  4544.70325/s
     iteration_duration.............: avg=51.46ms  min=1.49ms   med=42.7ms  max=364.1ms  p(90)=109.05ms p(95)=136.32ms p(99.9)=205.18ms
     iterations.....................: 276799  4528.343568/s
     success_rate...................: 100.00% ✓ 276799      ✗ 0     
     vus............................: 62      min=0         max=496 
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

     checks.........................: 100.00% ✓ 813396      ✗ 0     
     data_received..................: 24 GB   390 MB/s
     data_sent......................: 327 MB  5.4 MB/s
     http_req_blocked...............: avg=54.88µs  min=831ns    med=2.33µs  max=152.65ms p(90)=3.98µs   p(95)=5.11µs   p(99.9)=16.97ms 
     http_req_connecting............: avg=51.51µs  min=0s       med=0s      max=152.59ms p(90)=0s       p(95)=0s       p(99.9)=16.79ms 
     http_req_duration..............: avg=50.8ms   min=833.45µs med=42.28ms max=294.42ms p(90)=109.42ms p(95)=135.81ms p(99.9)=189.52ms
       { expected_response:true }...: avg=50.8ms   min=833.45µs med=42.28ms max=294.42ms p(90)=109.42ms p(95)=135.81ms p(99.9)=189.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 272132
     http_req_receiving.............: avg=297.01µs min=22.59µs  med=50.35µs max=104.03ms p(90)=216.07µs p(95)=390.85µs p(99.9)=40.87ms 
     http_req_sending...............: avg=136.02µs min=4.09µs   med=8.63µs  max=162.17ms p(90)=17.73µs  p(95)=128.88µs p(99.9)=24.32ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.37ms  min=784.04µs med=42ms    max=263.3ms  p(90)=108.51ms p(95)=134.65ms p(99.9)=186.39ms
     http_reqs......................: 272132  4458.652633/s
     iteration_duration.............: avg=52.52ms  min=1.44ms   med=43.28ms max=323.13ms p(90)=112.55ms p(95)=140.23ms p(99.9)=225.43ms
     iterations.....................: 271132  4442.268479/s
     success_rate...................: 100.00% ✓ 271132      ✗ 0     
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

     checks.........................: 100.00% ✓ 805515      ✗ 0     
     data_received..................: 24 GB   385 MB/s
     data_sent......................: 324 MB  5.3 MB/s
     http_req_blocked...............: avg=51.37µs  min=821ns    med=2.11µs  max=143.75ms p(90)=3.84µs   p(95)=5.07µs   p(99.9)=17.41ms 
     http_req_connecting............: avg=47.86µs  min=0s       med=0s      max=110.03ms p(90)=0s       p(95)=0s       p(99.9)=17.3ms  
     http_req_duration..............: avg=51.79ms  min=987.13µs med=43.56ms max=325.82ms p(90)=110.09ms p(95)=135.76ms p(99.9)=202.51ms
       { expected_response:true }...: avg=51.79ms  min=987.13µs med=43.56ms max=325.82ms p(90)=110.09ms p(95)=135.76ms p(99.9)=202.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 269505
     http_req_receiving.............: avg=340.05µs min=26.83µs  med=50.11µs max=205.16ms p(90)=225.68µs p(95)=384.79µs p(99.9)=48.16ms 
     http_req_sending...............: avg=130.17µs min=4.05µs   med=8.64µs  max=139.41ms p(90)=19.06µs  p(95)=126.52µs p(99.9)=23.35ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.32ms  min=945.58µs med=43.32ms max=325.47ms p(90)=109.14ms p(95)=134.7ms  p(99.9)=184.21ms
     http_reqs......................: 269505  4404.44766/s
     iteration_duration.............: avg=53.05ms  min=1.53ms   med=44.39ms max=343.26ms p(90)=112.63ms p(95)=138.66ms p(99.9)=220ms   
     iterations.....................: 268505  4388.104929/s
     success_rate...................: 100.00% ✓ 268505      ✗ 0     
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

     checks.........................: 100.00% ✓ 792609      ✗ 0     
     data_received..................: 23 GB   379 MB/s
     data_sent......................: 319 MB  5.2 MB/s
     http_req_blocked...............: avg=56.38µs  min=832ns    med=2.59µs  max=108.13ms p(90)=4.39µs   p(95)=5.61µs   p(99.9)=17.89ms 
     http_req_connecting............: avg=52.43µs  min=0s       med=0s      max=108.08ms p(90)=0s       p(95)=0s       p(99.9)=17.6ms  
     http_req_duration..............: avg=52.5ms   min=988.78µs med=43.86ms max=298.84ms p(90)=113.95ms p(95)=140.97ms p(99.9)=194.89ms
       { expected_response:true }...: avg=52.5ms   min=988.78µs med=43.86ms max=298.84ms p(90)=113.95ms p(95)=140.97ms p(99.9)=194.89ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 265203
     http_req_receiving.............: avg=321.22µs min=25.01µs  med=51.76µs max=174.25ms p(90)=232.7µs  p(95)=408.72µs p(99.9)=43.29ms 
     http_req_sending...............: avg=135.81µs min=4.01µs   med=9.12µs  max=284.48ms p(90)=19.41µs  p(95)=133.82µs p(99.9)=24.1ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=52.04ms  min=941.89µs med=43.56ms max=298.34ms p(90)=112.99ms p(95)=139.81ms p(99.9)=189.57ms
     http_reqs......................: 265203  4333.991272/s
     iteration_duration.............: avg=53.92ms  min=1.5ms    med=44.58ms max=328.19ms p(90)=116.7ms  p(95)=143.74ms p(99.9)=214.01ms
     iterations.....................: 264203  4317.649107/s
     success_rate...................: 100.00% ✓ 264203      ✗ 0     
     vus............................: 65      min=0         max=496 
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

     checks.........................: 100.00% ✓ 745452      ✗ 0     
     data_received..................: 22 GB   358 MB/s
     data_sent......................: 300 MB  4.9 MB/s
     http_req_blocked...............: avg=43.06µs  min=792ns    med=2.15µs  max=93.58ms  p(90)=3.81µs   p(95)=4.95µs   p(99.9)=8.67ms  
     http_req_connecting............: avg=39.85µs  min=0s       med=0s      max=93.35ms  p(90)=0s       p(95)=0s       p(99.9)=8.06ms  
     http_req_duration..............: avg=56.1ms   min=715.74µs med=46.63ms max=296.17ms p(90)=118.28ms p(95)=146.66ms p(99.9)=223.72ms
       { expected_response:true }...: avg=56.1ms   min=715.74µs med=46.63ms max=296.17ms p(90)=118.28ms p(95)=146.66ms p(99.9)=223.72ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 249484
     http_req_receiving.............: avg=239.45µs min=26.08µs  med=51.2µs  max=146.15ms p(90)=211.63µs p(95)=373.51µs p(99.9)=34.2ms  
     http_req_sending...............: avg=118.08µs min=4.24µs   med=8.91µs  max=135.48ms p(90)=18.57µs  p(95)=126.96µs p(99.9)=21.87ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=55.74ms  min=668.62µs med=46.37ms max=294.3ms  p(90)=117.62ms p(95)=145.76ms p(99.9)=221.86ms
     http_reqs......................: 249484  4090.331158/s
     iteration_duration.............: avg=57.34ms  min=1.4ms    med=47.5ms  max=354.44ms p(90)=120.68ms p(95)=149.97ms p(99.9)=240.26ms
     iterations.....................: 248484  4073.935994/s
     success_rate...................: 100.00% ✓ 248484      ✗ 0     
     vus............................: 56      min=0         max=498 
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

     checks.........................: 100.00% ✓ 471717      ✗ 0     
     data_received..................: 14 GB   225 MB/s
     data_sent......................: 190 MB  3.1 MB/s
     http_req_blocked...............: avg=10.92µs  min=871ns  med=2.29µs  max=46.83ms  p(90)=3.93µs   p(95)=5.11µs   p(99.9)=528.92µs
     http_req_connecting............: avg=7.94µs   min=0s     med=0s      max=46.77ms  p(90)=0s       p(95)=0s       p(99.9)=438.46µs
     http_req_duration..............: avg=89.87ms  min=1.21ms med=85.16ms max=284.91ms p(90)=175.09ms p(95)=188.23ms p(99.9)=224ms   
       { expected_response:true }...: avg=89.87ms  min=1.21ms med=85.16ms max=284.91ms p(90)=175.09ms p(95)=188.23ms p(99.9)=224ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 158239
     http_req_receiving.............: avg=114.03µs min=27.7µs med=56.2µs  max=141.71ms p(90)=152.1µs  p(95)=344.9µs  p(99.9)=7.21ms  
     http_req_sending...............: avg=67.56µs  min=4.33µs med=9.83µs  max=238ms    p(90)=20.21µs  p(95)=119.61µs p(99.9)=7.48ms  
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=89.69ms  min=1.17ms med=84.97ms max=284.76ms p(90)=174.89ms p(95)=188ms    p(99.9)=223.45ms
     http_reqs......................: 158239  2575.377463/s
     iteration_duration.............: avg=90.67ms  min=3.42ms med=86.14ms max=333.18ms p(90)=175.51ms p(95)=188.57ms p(99.9)=224.7ms 
     iterations.....................: 157239  2559.102225/s
     success_rate...................: 100.00% ✓ 157239      ✗ 0     
     vus............................: 77      min=0         max=493 
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

     checks.........................: 100.00% ✓ 256494      ✗ 0    
     data_received..................: 7.6 GB  121 MB/s
     data_sent......................: 104 MB  1.7 MB/s
     http_req_blocked...............: avg=5.42µs   min=962ns  med=2.63µs   max=8.98ms   p(90)=4.51µs   p(95)=5.5µs    p(99.9)=259.22µs
     http_req_connecting............: avg=2.15µs   min=0s     med=0s       max=8.81ms   p(90)=0s       p(95)=0s       p(99.9)=194.51µs
     http_req_duration..............: avg=164.91ms min=1.96ms med=137.92ms max=918.69ms p(90)=341.67ms p(95)=400.56ms p(99.9)=667.1ms 
       { expected_response:true }...: avg=164.91ms min=1.96ms med=137.92ms max=918.69ms p(90)=341.67ms p(95)=400.56ms p(99.9)=667.1ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 86498
     http_req_receiving.............: avg=74.28µs  min=27.4µs med=59.65µs  max=32.91ms  p(90)=96.55µs  p(95)=112.13µs p(99.9)=1.69ms  
     http_req_sending...............: avg=30.47µs  min=4.75µs med=11.47µs  max=72.99ms  p(90)=18.15µs  p(95)=21.76µs  p(99.9)=3.26ms  
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=164.8ms  min=1.91ms med=137.82ms max=918.57ms p(90)=341.56ms p(95)=400.45ms p(99.9)=667ms   
     http_reqs......................: 86498   1385.980194/s
     iteration_duration.............: avg=167.07ms min=7.47ms med=140.24ms max=918.9ms  p(90)=343.22ms p(95)=401.74ms p(99.9)=667.85ms
     iterations.....................: 85498   1369.956931/s
     success_rate...................: 100.00% ✓ 85498       ✗ 0    
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

     checks.........................: 100.00% ✓ 253839      ✗ 0    
     data_received..................: 7.5 GB  120 MB/s
     data_sent......................: 103 MB  1.6 MB/s
     http_req_blocked...............: avg=5.1µs    min=1µs     med=2.28µs   max=11.89ms  p(90)=3.93µs   p(95)=4.83µs   p(99.9)=280.31µs
     http_req_connecting............: avg=2.2µs    min=0s      med=0s       max=11.74ms  p(90)=0s       p(95)=0s       p(99.9)=193.14µs
     http_req_duration..............: avg=166.56ms min=1.98ms  med=166.64ms max=498.47ms p(90)=313.49ms p(95)=334.54ms p(99.9)=430.4ms 
       { expected_response:true }...: avg=166.56ms min=1.98ms  med=166.64ms max=498.47ms p(90)=313.49ms p(95)=334.54ms p(99.9)=430.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 85613
     http_req_receiving.............: avg=72.9µs   min=26.21µs med=57.38µs  max=124.77ms p(90)=94µs     p(95)=108.75µs p(99.9)=1.03ms  
     http_req_sending...............: avg=32.34µs  min=4.83µs  med=10.63µs  max=174.58ms p(90)=17.32µs  p(95)=20.78µs  p(99.9)=3.52ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=166.46ms min=1.92ms  med=166.5ms  max=498.4ms  p(90)=313.34ms p(95)=334.44ms p(99.9)=430.32ms
     http_reqs......................: 85613   1371.629326/s
     iteration_duration.............: avg=168.76ms min=4.95ms  med=169.13ms max=498.62ms p(90)=314.06ms p(95)=335.02ms p(99.9)=430.76ms
     iterations.....................: 84613   1355.608052/s
     success_rate...................: 100.00% ✓ 84613       ✗ 0    
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

     checks.........................: 100.00% ✓ 93615      ✗ 0    
     data_received..................: 2.8 GB  44 MB/s
     data_sent......................: 39 MB   598 kB/s
     http_req_blocked...............: avg=6.76µs   min=1.03µs  med=2.6µs    max=5.35ms  p(90)=4.26µs   p(95)=5.31µs   p(99.9)=620.1µs 
     http_req_connecting............: avg=3.06µs   min=0s      med=0s       max=5.29ms  p(90)=0s       p(95)=0s       p(99.9)=565.06µs
     http_req_duration..............: avg=446.02ms min=3.83ms  med=414.26ms max=1.7s    p(90)=883.56ms p(95)=954.62ms p(99.9)=1.47s   
       { expected_response:true }...: avg=446.02ms min=3.83ms  med=414.26ms max=1.7s    p(90)=883.56ms p(95)=954.62ms p(99.9)=1.47s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 32205
     http_req_receiving.............: avg=78.67µs  min=29.22µs med=70.71µs  max=13.76ms p(90)=107.89µs p(95)=121.77µs p(99.9)=829.25µs
     http_req_sending...............: avg=31.48µs  min=5.21µs  med=13.15µs  max=151.4ms p(90)=20.03µs  p(95)=22.56µs  p(99.9)=2.47ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=445.91ms min=3.76ms  med=414.19ms max=1.7s    p(90)=883.41ms p(95)=954.54ms p(99.9)=1.47s   
     http_reqs......................: 32205   497.923244/s
     iteration_duration.............: avg=460.53ms min=19.01ms med=435.16ms max=1.7s    p(90)=888.23ms p(95)=958ms    p(99.9)=1.47s   
     iterations.....................: 31205   482.46219/s
     success_rate...................: 100.00% ✓ 31205      ✗ 0    
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

     checks.........................: 100.00% ✓ 46974      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 20 MB   296 kB/s
     http_req_blocked...............: avg=11.34µs  min=1.2µs   med=3.09µs   max=8.66ms  p(90)=4.76µs   p(95)=6.17µs   p(99.9)=942.69µs
     http_req_connecting............: avg=6.68µs   min=0s      med=0s       max=8.6ms   p(90)=0s       p(95)=0s       p(99.9)=921.67µs
     http_req_duration..............: avg=873.6ms  min=5.56ms  med=781.03ms max=4.48s   p(90)=1.73s    p(95)=1.98s    p(99.9)=3.89s   
       { expected_response:true }...: avg=873.6ms  min=5.56ms  med=781.03ms max=4.48s   p(90)=1.73s    p(95)=1.98s    p(99.9)=3.89s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16658
     http_req_receiving.............: avg=96.85µs  min=32.89µs med=87.38µs  max=23.52ms p(90)=123.38µs p(95)=138.68µs p(99.9)=1.6ms   
     http_req_sending...............: avg=33.29µs  min=5.38µs  med=16.76µs  max=68.74ms p(90)=21.57µs  p(95)=24.85µs  p(99.9)=2.41ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=873.47ms min=5.48ms  med=780.93ms max=4.48s   p(90)=1.73s    p(95)=1.98s    p(99.9)=3.89s   
     http_reqs......................: 16658   246.90084/s
     iteration_duration.............: avg=929.4ms  min=78.77ms med=854.48ms max=4.48s   p(90)=1.76s    p(95)=2s       p(99.9)=3.91s   
     iterations.....................: 15658   232.079083/s
     success_rate...................: 100.00% ✓ 15658      ✗ 0    
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

     checks.........................: 100.00% ✓ 46638      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   290 kB/s
     http_req_blocked...............: avg=13.93µs  min=1.02µs  med=3.1µs    max=11.32ms p(90)=4.82µs  p(95)=6.24µs   p(99.9)=2.47ms
     http_req_connecting............: avg=9.06µs   min=0s      med=0s       max=11.19ms p(90)=0s      p(95)=0s       p(99.9)=2.34ms
     http_req_duration..............: avg=877.3ms  min=7.58ms  med=816.94ms max=2.84s   p(90)=1.79s   p(95)=1.91s    p(99.9)=2.61s 
       { expected_response:true }...: avg=877.3ms  min=7.58ms  med=816.94ms max=2.84s   p(90)=1.79s   p(95)=1.91s    p(99.9)=2.61s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16546
     http_req_receiving.............: avg=94.98µs  min=34.08µs med=87.05µs  max=38.56ms p(90)=121.8µs p(95)=138.08µs p(99.9)=1.06ms
     http_req_sending...............: avg=26.57µs  min=5.38µs  med=16.41µs  max=7.07ms  p(90)=21.57µs p(95)=25.09µs  p(99.9)=3.62ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s      p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=877.18ms min=7.47ms  med=816.84ms max=2.84s   p(90)=1.79s   p(95)=1.91s    p(99.9)=2.61s 
     http_reqs......................: 16546   241.26568/s
     iteration_duration.............: avg=933.66ms min=31.23ms med=872.79ms max=2.84s   p(90)=1.8s    p(95)=1.92s    p(99.9)=2.62s 
     iterations.....................: 15546   226.684169/s
     success_rate...................: 100.00% ✓ 15546      ✗ 0    
     vus............................: 84      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

