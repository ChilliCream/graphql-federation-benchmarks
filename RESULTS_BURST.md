## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.10 | 4,776 | 4,782 | 4,755 | 0.2% | 417 MB | 89.5 KB |  |
| fusion-net-11 | 16.7.5 | 4,716 | 4,736 | 4,608 | 1.2% | 405 MB | 87.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.10 | 4,576 | 4,613 | 4,526 | 0.8% | 426 MB | 95.3 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.10 | 4,565 | 4,579 | 4,477 | 0.9% | 156 MB | 34.9 KB |  |
| fusion-fed-net-11 | 16.7.5 | 4,524 | 4,549 | 4,507 | 0.3% | 415 MB | 94.0 KB |  |
| fusion-aot-11 | 16.7.5 | 4,438 | 4,439 | 4,426 | 0.1% | 155 MB | 35.8 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.10 | 4,383 | 4,398 | 4,379 | 0.2% | 166 MB | 38.9 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 4,333 | 4,408 | 4,327 | 0.8% | 162 MB | 38.3 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,117 | 4,166 | 4,042 | 1.1% | 2,308 MB | 574.0 KB |  |
| hive-router | v0.3.10 | 2,621 | 2,635 | 2,614 | 0.3% | 167 MB | 65.2 KB |  |
| caliban | 3.2.0 | 1,405 | 1,408 | 1,397 | 0.3% | 10,980 MB | 8,002.5 KB |  |
| cosmo | 0.365.2 | 1,345 | 1,347 | 1,343 | 0.1% | 625 MB | 475.5 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 493 | 495 | 488 | 0.5% | 3,161 MB | 6,564.7 KB |  |
| hive-gateway | 2.15.6 | 241 | 243 | 238 | 0.9% | 4,093 MB | 17,392.1 KB |  |
| apollo-gateway | 2.14.4 | 238 | 239 | 237 | 0.4% | 2,457 MB | 10,572.5 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (7061 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (4310 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (136124 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 870543      ✗ 0     
     data_received..................: 26 GB   418 MB/s
     data_sent......................: 350 MB  5.7 MB/s
     http_req_blocked...............: avg=67.93µs  min=822ns    med=2.14µs  max=140.33ms p(90)=3.73µs   p(95)=4.85µs   p(99.9)=25.37ms 
     http_req_connecting............: avg=64.31µs  min=0s       med=0s      max=126.96ms p(90)=0s       p(95)=0s       p(99.9)=24.69ms 
     http_req_duration..............: avg=47ms     min=790.15µs med=39.7ms  max=308ms    p(90)=98.16ms  p(95)=121.45ms p(99.9)=173.75ms
       { expected_response:true }...: avg=47ms     min=790.15µs med=39.7ms  max=308ms    p(90)=98.16ms  p(95)=121.45ms p(99.9)=173.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 291181
     http_req_receiving.............: avg=333.57µs min=23.84µs  med=51.79µs max=172.65ms p(90)=205.11µs p(95)=353.13µs p(99.9)=44.51ms 
     http_req_sending...............: avg=153.87µs min=4.18µs   med=8.71µs  max=184.99ms p(90)=16.51µs  p(95)=113.42µs p(99.9)=27.79ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.51ms  min=732.86µs med=39.35ms max=285.19ms p(90)=97.01ms  p(95)=120.1ms  p(99.9)=167.9ms 
     http_reqs......................: 291181  4776.640451/s
     iteration_duration.............: avg=49.09ms  min=1.28ms   med=40.61ms max=343.67ms p(90)=103.37ms p(95)=128.29ms p(99.9)=202.69ms
     iterations.....................: 290181  4760.236082/s
     success_rate...................: 100.00% ✓ 290181      ✗ 0     
     vus............................: 56      min=0         max=498 
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

     checks.........................: 100.00% ✓ 859377      ✗ 0     
     data_received..................: 25 GB   413 MB/s
     data_sent......................: 345 MB  5.7 MB/s
     http_req_blocked...............: avg=60.48µs  min=801ns    med=2.03µs  max=131.92ms p(90)=3.65µs   p(95)=4.82µs   p(99.9)=21.11ms 
     http_req_connecting............: avg=57.22µs  min=0s       med=0s      max=131.88ms p(90)=0s       p(95)=0s       p(99.9)=20.82ms 
     http_req_duration..............: avg=47.94ms  min=768.97µs med=40.16ms max=336.43ms p(90)=101.4ms  p(95)=125.79ms p(99.9)=176.91ms
       { expected_response:true }...: avg=47.94ms  min=768.97µs med=40.16ms max=336.43ms p(90)=101.4ms  p(95)=125.79ms p(99.9)=176.91ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 287459
     http_req_receiving.............: avg=323.99µs min=25.12µs  med=50.73µs max=189.31ms p(90)=208.82µs p(95)=364.08µs p(99.9)=44.67ms 
     http_req_sending...............: avg=142.7µs  min=4.3µs    med=8.38µs  max=204.52ms p(90)=16.74µs  p(95)=116.73µs p(99.9)=26.09ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.48ms  min=724.1µs  med=39.89ms max=325.5ms  p(90)=100.32ms p(95)=124.7ms  p(99.9)=170ms   
     http_reqs......................: 287459  4716.081637/s
     iteration_duration.............: avg=49.72ms  min=1.33ms   med=41.17ms max=358.75ms p(90)=105.29ms p(95)=130.75ms p(99.9)=200.16ms
     iterations.....................: 286459  4699.675535/s
     success_rate...................: 100.00% ✓ 286459      ✗ 0     
     vus............................: 55      min=0         max=498 
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

     checks.........................: 100.00% ✓ 836187      ✗ 0     
     data_received..................: 25 GB   401 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=59.48µs  min=741ns    med=2.16µs  max=137.41ms p(90)=3.93µs   p(95)=5.13µs   p(99.9)=20.73ms 
     http_req_connecting............: avg=56.27µs  min=0s       med=0s      max=120.53ms p(90)=0s       p(95)=0s       p(99.9)=20.33ms 
     http_req_duration..............: avg=49.46ms  min=926.31µs med=41.42ms max=323.16ms p(90)=105.61ms p(95)=130.07ms p(99.9)=183.47ms
       { expected_response:true }...: avg=49.46ms  min=926.31µs med=41.42ms max=323.16ms p(90)=105.61ms p(95)=130.07ms p(99.9)=183.47ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 279729
     http_req_receiving.............: avg=348.38µs min=26.78µs  med=51.89µs max=194.44ms p(90)=211.39µs p(95)=372.89µs p(99.9)=50.89ms 
     http_req_sending...............: avg=146.59µs min=4.19µs   med=8.83µs  max=287.86ms p(90)=18.42µs  p(95)=121.64µs p(99.9)=26.16ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.96ms  min=881.32µs med=41.14ms max=299.16ms p(90)=104.36ms p(95)=128.62ms p(99.9)=179.86ms
     http_reqs......................: 279729  4576.733191/s
     iteration_duration.............: avg=51.11ms  min=1.44ms   med=42.34ms max=362.06ms p(90)=108.98ms p(95)=134.33ms p(99.9)=208.03ms
     iterations.....................: 278729  4560.37188/s
     success_rate...................: 100.00% ✓ 278729      ✗ 0     
     vus............................: 63      min=0         max=497 
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

     checks.........................: 100.00% ✓ 832785      ✗ 0     
     data_received..................: 24 GB   400 MB/s
     data_sent......................: 335 MB  5.5 MB/s
     http_req_blocked...............: avg=52.6µs   min=861ns    med=2.08µs  max=121.72ms p(90)=3.67µs   p(95)=4.81µs   p(99.9)=17.88ms 
     http_req_connecting............: avg=49.4µs   min=0s       med=0s      max=121.56ms p(90)=0s       p(95)=0s       p(99.9)=17.61ms 
     http_req_duration..............: avg=49.8ms   min=845.99µs med=41.49ms max=319.23ms p(90)=107.06ms p(95)=131.46ms p(99.9)=184.43ms
       { expected_response:true }...: avg=49.8ms   min=845.99µs med=41.49ms max=319.23ms p(90)=107.06ms p(95)=131.46ms p(99.9)=184.43ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 278595
     http_req_receiving.............: avg=293.94µs min=24.22µs  med=49.24µs max=217.97ms p(90)=218.01µs p(95)=374.98µs p(99.9)=39.6ms  
     http_req_sending...............: avg=127.96µs min=4.17µs   med=8.54µs  max=274.89ms p(90)=17.19µs  p(95)=122.52µs p(99.9)=22.89ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.38ms  min=783.32µs med=41.23ms max=287.68ms p(90)=106.15ms p(95)=130.57ms p(99.9)=178.99ms
     http_reqs......................: 278595  4565.70272/s
     iteration_duration.............: avg=51.31ms  min=1.45ms   med=42.42ms max=329.79ms p(90)=110.04ms p(95)=135.25ms p(99.9)=203.71ms
     iterations.....................: 277595  4549.314404/s
     success_rate...................: 100.00% ✓ 277595      ✗ 0     
     vus............................: 58      min=0         max=498 
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

     checks.........................: 100.00% ✓ 826605      ✗ 0     
     data_received..................: 24 GB   396 MB/s
     data_sent......................: 332 MB  5.4 MB/s
     http_req_blocked...............: avg=62.21µs  min=811ns    med=2.1µs   max=162.26ms p(90)=3.77µs   p(95)=4.94µs   p(99.9)=23.32ms 
     http_req_connecting............: avg=58.91µs  min=0s       med=0s      max=162.17ms p(90)=0s       p(95)=0s       p(99.9)=22.98ms 
     http_req_duration..............: avg=50.13ms  min=914.88µs med=42.35ms max=312.29ms p(90)=106.41ms p(95)=131.34ms p(99.9)=182.25ms
       { expected_response:true }...: avg=50.13ms  min=914.88µs med=42.35ms max=312.29ms p(90)=106.41ms p(95)=131.34ms p(99.9)=182.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 276535
     http_req_receiving.............: avg=334.06µs min=21.87µs  med=53.18µs max=100.44ms p(90)=217.87µs p(95)=382.15µs p(99.9)=45.89ms 
     http_req_sending...............: avg=147.96µs min=3.85µs   med=8.9µs   max=111.77ms p(90)=17.88µs  p(95)=121.64µs p(99.9)=26.52ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.65ms  min=869.57µs med=42.03ms max=304.79ms p(90)=105.32ms p(95)=130.07ms p(99.9)=178.34ms
     http_reqs......................: 276535  4524.825088/s
     iteration_duration.............: avg=51.7ms   min=1.34ms   med=43.18ms max=346.63ms p(90)=109.7ms  p(95)=135.79ms p(99.9)=207.6ms 
     iterations.....................: 275535  4508.462511/s
     success_rate...................: 100.00% ✓ 275535      ✗ 0     
     vus............................: 62      min=0         max=497 
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

     checks.........................: 100.00% ✓ 809706     ✗ 0     
     data_received..................: 24 GB   388 MB/s
     data_sent......................: 326 MB  5.3 MB/s
     http_req_blocked...............: avg=57.9µs   min=841ns    med=2.58µs  max=177.18ms p(90)=4.19µs   p(95)=5.35µs   p(99.9)=20.26ms 
     http_req_connecting............: avg=54.43µs  min=0s       med=0s      max=176.97ms p(90)=0s       p(95)=0s       p(99.9)=20.04ms 
     http_req_duration..............: avg=51.12ms  min=846.6µs  med=42.41ms max=314.59ms p(90)=110.49ms p(95)=136.82ms p(99.9)=191.66ms
       { expected_response:true }...: avg=51.12ms  min=846.6µs  med=42.41ms max=314.59ms p(90)=110.49ms p(95)=136.82ms p(99.9)=191.66ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 270902
     http_req_receiving.............: avg=304.73µs min=26.17µs  med=51.22µs max=185.24ms p(90)=223.88µs p(95)=398.39µs p(99.9)=41.53ms 
     http_req_sending...............: avg=139.46µs min=4.15µs   med=9.1µs   max=94.85ms  p(90)=18.12µs  p(95)=130.46µs p(99.9)=25.12ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.68ms  min=801.71µs med=42.15ms max=302.48ms p(90)=109.53ms p(95)=135.6ms  p(99.9)=187.74ms
     http_reqs......................: 270902  4438.12515/s
     iteration_duration.............: avg=52.78ms  min=1.46ms   med=43.37ms max=334.25ms p(90)=113.94ms p(95)=140.99ms p(99.9)=213.92ms
     iterations.....................: 269902  4421.74238/s
     success_rate...................: 100.00% ✓ 269902     ✗ 0     
     vus............................: 59      min=0        max=497 
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 801837      ✗ 0     
     data_received..................: 24 GB   384 MB/s
     data_sent......................: 322 MB  5.3 MB/s
     http_req_blocked...............: avg=49.58µs  min=812ns    med=2.1µs   max=106.99ms p(90)=3.75µs   p(95)=4.94µs   p(99.9)=17.23ms 
     http_req_connecting............: avg=45.76µs  min=0s       med=0s      max=106.84ms p(90)=0s       p(95)=0s       p(99.9)=16.53ms 
     http_req_duration..............: avg=51.93ms  min=985.95µs med=43.75ms max=294.09ms p(90)=110.31ms p(95)=135.71ms p(99.9)=194.28ms
       { expected_response:true }...: avg=51.93ms  min=985.95µs med=43.75ms max=294.09ms p(90)=110.31ms p(95)=135.71ms p(99.9)=194.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 268279
     http_req_receiving.............: avg=320.84µs min=25.06µs  med=50.62µs max=142.66ms p(90)=224.54µs p(95)=385.62µs p(99.9)=44.78ms 
     http_req_sending...............: avg=123.34µs min=4.15µs   med=8.89µs  max=94.25ms  p(90)=18.44µs  p(95)=125.64µs p(99.9)=21.9ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.49ms  min=934.12µs med=43.49ms max=256.67ms p(90)=109.56ms p(95)=134.82ms p(99.9)=185.64ms
     http_reqs......................: 268279  4383.66778/s
     iteration_duration.............: avg=53.3ms   min=1.56ms   med=44.7ms  max=399.65ms p(90)=112.76ms p(95)=138.87ms p(99.9)=224.05ms
     iterations.....................: 267279  4367.327822/s
     success_rate...................: 100.00% ✓ 267279      ✗ 0     
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

     checks.........................: 100.00% ✓ 792300      ✗ 0     
     data_received..................: 23 GB   379 MB/s
     data_sent......................: 319 MB  5.2 MB/s
     http_req_blocked...............: avg=57.53µs  min=972ns    med=2.6µs   max=126.37ms p(90)=4.39µs   p(95)=5.68µs   p(99.9)=18.98ms 
     http_req_connecting............: avg=53.42µs  min=0s       med=0s      max=126.13ms p(90)=0s       p(95)=0s       p(99.9)=17.94ms 
     http_req_duration..............: avg=52.17ms  min=984.53µs med=43.35ms max=319.2ms  p(90)=112.66ms p(95)=140.74ms p(99.9)=197.95ms
       { expected_response:true }...: avg=52.17ms  min=984.53µs med=43.35ms max=319.2ms  p(90)=112.66ms p(95)=140.74ms p(99.9)=197.95ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 265100
     http_req_receiving.............: avg=365.63µs min=26.69µs  med=51.82µs max=190.51ms p(90)=238.49µs p(95)=416.27µs p(99.9)=51.82ms 
     http_req_sending...............: avg=147.37µs min=4.37µs   med=9.11µs  max=160.67ms p(90)=19.76µs  p(95)=135.05µs p(99.9)=26.91ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.66ms  min=939.15µs med=43.04ms max=318.67ms p(90)=111.38ms p(95)=139.37ms p(99.9)=191.04ms
     http_reqs......................: 265100  4333.048102/s
     iteration_duration.............: avg=53.94ms  min=1.57ms   med=44.35ms max=357.08ms p(90)=116.33ms p(95)=144.93ms p(99.9)=231.25ms
     iterations.....................: 264100  4316.703145/s
     success_rate...................: 100.00% ✓ 264100      ✗ 0     
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

     checks.........................: 100.00% ✓ 750105      ✗ 0     
     data_received..................: 22 GB   360 MB/s
     data_sent......................: 302 MB  4.9 MB/s
     http_req_blocked...............: avg=48.19µs  min=1.03µs   med=2.72µs  max=100.72ms p(90)=4.37µs   p(95)=5.52µs   p(99.9)=13.46ms 
     http_req_connecting............: avg=44.06µs  min=0s       med=0s      max=100.5ms  p(90)=0s       p(95)=0s       p(99.9)=12.57ms 
     http_req_duration..............: avg=55.8ms   min=687.71µs med=46.61ms max=334.11ms p(90)=118.78ms p(95)=147.91ms p(99.9)=226.21ms
       { expected_response:true }...: avg=55.8ms   min=687.71µs med=46.61ms max=334.11ms p(90)=118.78ms p(95)=147.91ms p(99.9)=226.21ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 251035
     http_req_receiving.............: avg=283.98µs min=25.21µs  med=52.07µs max=94.27ms  p(90)=225.77µs p(95)=398.03µs p(99.9)=39.7ms  
     http_req_sending...............: avg=123.99µs min=4.11µs   med=9.46µs  max=239.67ms p(90)=18.39µs  p(95)=134.03µs p(99.9)=22.09ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=55.39ms  min=650.64µs med=46.31ms max=329.54ms p(90)=117.84ms p(95)=146.85ms p(99.9)=221.57ms
     http_reqs......................: 251035  4117.92648/s
     iteration_duration.............: avg=56.98ms  min=1.35ms   med=47.28ms max=340.64ms p(90)=121.36ms p(95)=151.09ms p(99.9)=236.93ms
     iterations.....................: 250035  4101.522686/s
     success_rate...................: 100.00% ✓ 250035      ✗ 0     
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

     checks.........................: 100.00% ✓ 480138      ✗ 0     
     data_received..................: 14 GB   229 MB/s
     data_sent......................: 193 MB  3.1 MB/s
     http_req_blocked...............: avg=17.11µs  min=941ns   med=2.86µs  max=50.25ms  p(90)=4.62µs   p(95)=5.86µs   p(99.9)=1.22ms  
     http_req_connecting............: avg=13.35µs  min=0s      med=0s      max=44.87ms  p(90)=0s       p(95)=0s       p(99.9)=1.09ms  
     http_req_duration..............: avg=88.26ms  min=1.2ms   med=83.09ms max=266.25ms p(90)=172.44ms p(95)=187.36ms p(99.9)=231.6ms 
       { expected_response:true }...: avg=88.26ms  min=1.2ms   med=83.09ms max=266.25ms p(90)=172.44ms p(95)=187.36ms p(99.9)=231.6ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 161046
     http_req_receiving.............: avg=137.35µs min=26.36µs med=57.1µs  max=100.21ms p(90)=186.09µs p(95)=379.28µs p(99.9)=10.88ms 
     http_req_sending...............: avg=70.63µs  min=4.41µs  med=11.05µs max=90.6ms   p(90)=21.05µs  p(95)=132.85µs p(99.9)=9.27ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=88.05ms  min=1.15ms  med=82.9ms  max=266.19ms p(90)=172.16ms p(95)=187.09ms p(99.9)=230.84ms
     http_reqs......................: 161046  2621.147886/s
     iteration_duration.............: avg=89.08ms  min=2.71ms  med=84.03ms max=382.28ms p(90)=172.85ms p(95)=187.79ms p(99.9)=232.8ms 
     iterations.....................: 160046  2604.872114/s
     success_rate...................: 100.00% ✓ 160046      ✗ 0     
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

     checks.........................: 100.00% ✓ 260112      ✗ 0    
     data_received..................: 7.7 GB  123 MB/s
     data_sent......................: 105 MB  1.7 MB/s
     http_req_blocked...............: avg=6.3µs    min=1.19µs  med=3.37µs   max=16.78ms  p(90)=5.32µs   p(95)=6.41µs   p(99.9)=340.53µs
     http_req_connecting............: avg=2.28µs   min=0s      med=0s       max=16.7ms   p(90)=0s       p(95)=0s       p(99.9)=266.32µs
     http_req_duration..............: avg=162.58ms min=1.99ms  med=137.43ms max=986.56ms p(90)=333.7ms  p(95)=403.1ms  p(99.9)=715.97ms
       { expected_response:true }...: avg=162.58ms min=1.99ms  med=137.43ms max=986.56ms p(90)=333.7ms  p(95)=403.1ms  p(99.9)=715.97ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 87704
     http_req_receiving.............: avg=86.61µs  min=27.57µs med=65.37µs  max=80.92ms  p(90)=107.19µs p(95)=128.54µs p(99.9)=2.17ms  
     http_req_sending...............: avg=38.73µs  min=5.07µs  med=13.4µs   max=126.76ms p(90)=20.71µs  p(95)=25.36µs  p(99.9)=4.52ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=162.45ms min=1.93ms  med=137.3ms  max=986.49ms p(90)=333.57ms p(95)=403.01ms p(99.9)=715.87ms
     http_reqs......................: 87704   1405.595175/s
     iteration_duration.............: avg=164.71ms min=5.61ms  med=139.74ms max=986.74ms p(90)=335.24ms p(95)=404.41ms p(99.9)=716.71ms
     iterations.....................: 86704   1389.568595/s
     success_rate...................: 100.00% ✓ 86704       ✗ 0    
     vus............................: 75      min=0         max=494
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

     checks.........................: 100.00% ✓ 249039      ✗ 0    
     data_received..................: 7.3 GB  118 MB/s
     data_sent......................: 101 MB  1.6 MB/s
     http_req_blocked...............: avg=4.52µs   min=1.01µs  med=2.27µs   max=12.3ms   p(90)=3.89µs   p(95)=4.83µs   p(99.9)=246.26µs
     http_req_connecting............: avg=1.51µs   min=0s      med=0s       max=12.24ms  p(90)=0s       p(95)=0s       p(99.9)=183.24µs
     http_req_duration..............: avg=169.79ms min=2ms     med=168.62ms max=454.45ms p(90)=322.63ms p(95)=347.04ms p(99.9)=412.12ms
       { expected_response:true }...: avg=169.79ms min=2ms     med=168.62ms max=454.45ms p(90)=322.63ms p(95)=347.04ms p(99.9)=412.12ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 84013
     http_req_receiving.............: avg=74.51µs  min=26.27µs med=59.32µs  max=123.1ms  p(90)=96.22µs  p(95)=110.75µs p(99.9)=1.09ms  
     http_req_sending...............: avg=28µs     min=4.68µs  med=10.79µs  max=108.98ms p(90)=17.26µs  p(95)=20.61µs  p(99.9)=3.15ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=169.68ms min=1.95ms  med=168.52ms max=454.4ms  p(90)=322.53ms p(95)=346.94ms p(99.9)=412.06ms
     http_reqs......................: 84013   1345.208419/s
     iteration_duration.............: avg=172.06ms min=4.9ms   med=171.29ms max=454.66ms p(90)=323.44ms p(95)=347.57ms p(99.9)=412.8ms 
     iterations.....................: 83013   1329.196511/s
     success_rate...................: 100.00% ✓ 83013       ✗ 0    
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

     checks.........................: 100.00% ✓ 92562      ✗ 0    
     data_received..................: 2.8 GB  43 MB/s
     data_sent......................: 38 MB   592 kB/s
     http_req_blocked...............: avg=9.16µs   min=962ns   med=2.69µs   max=10.97ms  p(90)=4.36µs   p(95)=5.34µs   p(99.9)=1.75ms  
     http_req_connecting............: avg=5.52µs   min=0s      med=0s       max=10.92ms  p(90)=0s       p(95)=0s       p(99.9)=1.73ms  
     http_req_duration..............: avg=450.78ms min=3.73ms  med=414.02ms max=1.71s    p(90)=894.53ms p(95)=970.67ms p(99.9)=1.48s   
       { expected_response:true }...: avg=450.78ms min=3.73ms  med=414.02ms max=1.71s    p(90)=894.53ms p(95)=970.67ms p(99.9)=1.48s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 31854
     http_req_receiving.............: avg=85.44µs  min=27.55µs med=70.03µs  max=122.51ms p(90)=109.18µs p(95)=123.81µs p(99.9)=942.54µs
     http_req_sending...............: avg=26.96µs  min=5.06µs  med=13.22µs  max=98.79ms  p(90)=19.53µs  p(95)=21.89µs  p(99.9)=1.89ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=450.67ms min=3.66ms  med=413.93ms max=1.71s    p(90)=894.44ms p(95)=970.6ms  p(99.9)=1.48s   
     http_reqs......................: 31854   493.006923/s
     iteration_duration.............: avg=465.61ms min=21.48ms med=433.68ms max=1.72s    p(90)=898.17ms p(95)=973.53ms p(99.9)=1.48s   
     iterations.....................: 30854   477.529842/s
     success_rate...................: 100.00% ✓ 30854      ✗ 0    
     vus............................: 85      min=0        max=499
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

     checks.........................: 100.00% ✓ 45999      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   289 kB/s
     http_req_blocked...............: avg=14.26µs  min=1.19µs  med=3.19µs   max=9.21ms  p(90)=4.89µs   p(95)=6.51µs   p(99.9)=2.2ms 
     http_req_connecting............: avg=9.44µs   min=0s      med=0s       max=9.15ms  p(90)=0s       p(95)=0s       p(99.9)=2.18ms
     http_req_duration..............: avg=891.82ms min=5.79ms  med=799.51ms max=5.02s   p(90)=1.79s    p(95)=2.04s    p(99.9)=4.29s 
       { expected_response:true }...: avg=891.82ms min=5.79ms  med=799.51ms max=5.02s   p(90)=1.79s    p(95)=2.04s    p(99.9)=4.29s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16333
     http_req_receiving.............: avg=93.66µs  min=35.32µs med=88.04µs  max=6.04ms  p(90)=124.08µs p(95)=138.71µs p(99.9)=1.27ms
     http_req_sending...............: avg=28.02µs  min=5.73µs  med=17.33µs  max=21.11ms p(90)=22.63µs  p(95)=26.13µs  p(99.9)=2.51ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=891.7ms  min=5.67ms  med=799.38ms max=5.02s   p(90)=1.79s    p(95)=2.03s    p(99.9)=4.29s 
     http_reqs......................: 16333   241.009174/s
     iteration_duration.............: avg=949.97ms min=49.22ms med=873.59ms max=5.03s   p(90)=1.82s    p(95)=2.05s    p(99.9)=4.31s 
     iterations.....................: 15333   226.253209/s
     success_rate...................: 100.00% ✓ 15333      ✗ 0    
     vus............................: 98      min=0        max=500
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

     checks.........................: 100.00% ✓ 46092      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   287 kB/s
     http_req_blocked...............: avg=15.19µs  min=1.39µs  med=3.46µs   max=10.92ms p(90)=5.23µs  p(95)=6.82µs   p(99.9)=2.31ms
     http_req_connecting............: avg=9.96µs   min=0s      med=0s       max=10.53ms p(90)=0s      p(95)=0s       p(99.9)=2.29ms
     http_req_duration..............: avg=887.09ms min=7.53ms  med=805.22ms max=2.96s   p(90)=1.81s   p(95)=1.95s    p(99.9)=2.66s 
       { expected_response:true }...: avg=887.09ms min=7.53ms  med=805.22ms max=2.96s   p(90)=1.81s   p(95)=1.95s    p(99.9)=2.66s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16364
     http_req_receiving.............: avg=95.49µs  min=36.7µs  med=86.99µs  max=16.46ms p(90)=125.4µs p(95)=140.98µs p(99.9)=1.17ms
     http_req_sending...............: avg=29.77µs  min=6.05µs  med=16.92µs  max=76.85ms p(90)=22.46µs p(95)=25.89µs  p(99.9)=1.9ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s      p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=886.96ms min=7.46ms  med=805.11ms max=2.96s   p(90)=1.8s    p(95)=1.95s    p(99.9)=2.66s 
     http_reqs......................: 16364   238.869819/s
     iteration_duration.............: avg=944.83ms min=43.24ms med=896.74ms max=2.97s   p(90)=1.82s   p(95)=1.96s    p(99.9)=2.68s 
     iterations.....................: 15364   224.272544/s
     success_rate...................: 100.00% ✓ 15364      ✗ 0    
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

