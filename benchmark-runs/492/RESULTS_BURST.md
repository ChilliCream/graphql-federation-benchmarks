## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.17 | 4,859 | 4,882 | 4,753 | 1.2% | 411 MB | 86.6 KB | non-compatible response (3 across 1/5 runs) |
| fusion-net-11 | 16.7.6 | 4,853 | 4,899 | 4,804 | 0.9% | 409 MB | 86.4 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.17 | 4,827 | 4,838 | 4,790 | 0.5% | 159 MB | 33.8 KB |  |
| fusion-aot-11 | 16.7.6 | 4,772 | 4,786 | 4,714 | 0.6% | 147 MB | 31.6 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.17 | 4,700 | 4,729 | 4,682 | 0.4% | 411 MB | 89.5 KB |  |
| fusion-fed-net-11 | 16.7.6 | 4,688 | 4,695 | 4,673 | 0.2% | 417 MB | 91.1 KB |  |
| fusion-fed-aot-11 | 16.7.6 | 4,555 | 4,692 | 4,546 | 1.6% | 147 MB | 33.1 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.17 | 4,552 | 4,660 | 4,529 | 1.1% | 149 MB | 33.6 KB |  |
| feddi-gateway | 2026-11-03-0517 | 4,521 | 4,533 | 4,510 | 0.2% | 2,297 MB | 520.2 KB |  |
| hive-router-nightly | v0.3.19-nightly.9815b25d | 4,042 | 4,057 | 3,987 | 0.8% | 224 MB | 56.6 KB |  |
| hive-router | v0.3.17 | 3,994 | 4,009 | 3,987 | 0.2% | 192 MB | 49.3 KB |  |
| caliban | 3.2.1 | 1,424 | 1,429 | 1,423 | 0.2% | 11,608 MB | 8,347.4 KB |  |
| cosmo | 0.373.0 | 1,317 | 1,318 | 1,316 | 0.1% | 571 MB | 443.6 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 564 | 567 | 560 | 0.4% | 3,005 MB | 5,456.5 KB |  |
| hive-gateway | 2.15.10 | 275 | 276 | 271 | 0.9% | 3,702 MB | 13,786.3 KB |  |
| apollo-gateway | 2.14.4 | 237 | 238 | 236 | 0.4% | 2,475 MB | 10,693.1 KB |  |
| apollo-router | v2.19.1 | — | — | — | — | — | — | non-compatible response (5184 across 5/5 runs) |
| apollo-router-nightly | v3.0.0-preview.0-nightly.b787dc86 | — | — | — | — | — | — | non-compatible response (2563 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (4486 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (160107 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 885261      ✗ 0     
     data_received..................: 26 GB   425 MB/s
     data_sent......................: 356 MB  5.8 MB/s
     http_req_blocked...............: avg=61.36µs  min=771ns    med=2.02µs  max=132.18ms p(90)=3.54µs   p(95)=4.59µs   p(99.9)=21.47ms 
     http_req_connecting............: avg=57.82µs  min=0s       med=0s      max=132.05ms p(90)=0s       p(95)=0s       p(99.9)=21.21ms 
     http_req_duration..............: avg=46.55ms  min=736.72µs med=39.28ms max=328.61ms p(90)=97.89ms  p(95)=122.33ms p(99.9)=176.41ms
       { expected_response:true }...: avg=46.55ms  min=736.72µs med=39.28ms max=328.61ms p(90)=97.89ms  p(95)=122.33ms p(99.9)=176.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 296087
     http_req_receiving.............: avg=338.45µs min=22.61µs  med=51.02µs max=211.32ms p(90)=206.85µs p(95)=358.9µs  p(99.9)=45.43ms 
     http_req_sending...............: avg=147.97µs min=3.95µs   med=8.29µs  max=216.15ms p(90)=15.63µs  p(95)=113.63µs p(99.9)=27.11ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.07ms  min=696.48µs med=38.95ms max=328.5ms  p(90)=96.63ms  p(95)=120.98ms p(99.9)=172.64ms
     http_reqs......................: 296087  4859.830839/s
     iteration_duration.............: avg=48.27ms  min=1.2ms    med=40.13ms max=356.4ms  p(90)=102.05ms p(95)=128.2ms  p(99.9)=201.48ms
     iterations.....................: 295087  4843.417316/s
     success_rate...................: 100.00% ✓ 295087      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 883974      ✗ 0     
     data_received..................: 26 GB   425 MB/s
     data_sent......................: 355 MB  5.8 MB/s
     http_req_blocked...............: avg=69.63µs  min=801ns    med=2.1µs   max=134.97ms p(90)=3.63µs   p(95)=4.72µs   p(99.9)=25.54ms 
     http_req_connecting............: avg=65.66µs  min=0s       med=0s      max=134.87ms p(90)=0s       p(95)=0s       p(99.9)=23.97ms 
     http_req_duration..............: avg=46.28ms  min=724.98µs med=39.08ms max=254.85ms p(90)=96.51ms  p(95)=119.37ms p(99.9)=175.7ms 
       { expected_response:true }...: avg=46.28ms  min=724.98µs med=39.08ms max=254.85ms p(90)=96.51ms  p(95)=119.37ms p(99.9)=175.7ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 295658
     http_req_receiving.............: avg=353.82µs min=25.32µs  med=53.24µs max=126.45ms p(90)=196.22µs p(95)=343.63µs p(99.9)=47.58ms 
     http_req_sending...............: avg=155.05µs min=3.9µs    med=8.78µs  max=143.04ms p(90)=15.89µs  p(95)=108.95µs p(99.9)=27.77ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=45.78ms  min=685.49µs med=38.72ms max=254.78ms p(90)=95.42ms  p(95)=118.33ms p(99.9)=169.12ms
     http_reqs......................: 295658  4853.556519/s
     iteration_duration.............: avg=48.33ms  min=1.03ms   med=40.19ms max=344.57ms p(90)=102.05ms p(95)=125.73ms p(99.9)=196.9ms 
     iterations.....................: 294658  4837.140401/s
     success_rate...................: 100.00% ✓ 294658      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 879963      ✗ 0     
     data_received..................: 26 GB   422 MB/s
     data_sent......................: 354 MB  5.8 MB/s
     http_req_blocked...............: avg=64.95µs  min=792ns    med=1.94µs  max=160.49ms p(90)=3.48µs   p(95)=4.56µs   p(99.9)=23.25ms 
     http_req_connecting............: avg=61.74µs  min=0s       med=0s      max=148.41ms p(90)=0s       p(95)=0s       p(99.9)=22.92ms 
     http_req_duration..............: avg=46.84ms  min=775.76µs med=38.83ms max=264.79ms p(90)=100.37ms p(95)=126.09ms p(99.9)=179.54ms
       { expected_response:true }...: avg=46.84ms  min=775.76µs med=38.83ms max=264.79ms p(90)=100.37ms p(95)=126.09ms p(99.9)=179.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 294321
     http_req_receiving.............: avg=328.4µs  min=21.79µs  med=50.11µs max=116.37ms p(90)=203.34µs p(95)=363.47µs p(99.9)=45.57ms 
     http_req_sending...............: avg=137.41µs min=4.03µs   med=8.2µs   max=129.45ms p(90)=15.84µs  p(95)=115.19µs p(99.9)=24.27ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.37ms  min=737.93µs med=38.53ms max=244.16ms p(90)=99.28ms  p(95)=125ms    p(99.9)=173.76ms
     http_reqs......................: 294321  4827.906421/s
     iteration_duration.............: avg=48.56ms  min=1.18ms   med=39.84ms max=330.33ms p(90)=104.05ms p(95)=131.14ms p(99.9)=203.96ms
     iterations.....................: 293321  4811.50288/s
     success_rate...................: 100.00% ✓ 293321      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 869916      ✗ 0     
     data_received..................: 26 GB   418 MB/s
     data_sent......................: 350 MB  5.7 MB/s
     http_req_blocked...............: avg=62.43µs  min=822ns    med=2.06µs  max=128.59ms p(90)=3.67µs   p(95)=4.81µs   p(99.9)=23.18ms 
     http_req_connecting............: avg=58.9µs   min=0s       med=0s      max=128.33ms p(90)=0s       p(95)=0s       p(99.9)=22.35ms 
     http_req_duration..............: avg=47.51ms  min=804.92µs med=39.65ms max=307.8ms  p(90)=101.37ms p(95)=126.98ms p(99.9)=179.47ms
       { expected_response:true }...: avg=47.51ms  min=804.92µs med=39.65ms max=307.8ms  p(90)=101.37ms p(95)=126.98ms p(99.9)=179.47ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 290972
     http_req_receiving.............: avg=328.13µs min=25.76µs  med=51.06µs max=159.59ms p(90)=204.95µs p(95)=364.48µs p(99.9)=47.49ms 
     http_req_sending...............: avg=143.55µs min=3.99µs   med=8.53µs  max=163.93ms p(90)=16.8µs   p(95)=116.68µs p(99.9)=25.16ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.04ms  min=735.98µs med=39.35ms max=307.2ms  p(90)=100.27ms p(95)=125.74ms p(99.9)=175.22ms
     http_reqs......................: 290972  4772.276949/s
     iteration_duration.............: avg=49.12ms  min=1.23ms   med=40.54ms max=322.83ms p(90)=104.93ms p(95)=131.89ms p(99.9)=199.52ms
     iterations.....................: 289972  4755.875794/s
     success_rate...................: 100.00% ✓ 289972      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 856155      ✗ 0     
     data_received..................: 25 GB   411 MB/s
     data_sent......................: 344 MB  5.6 MB/s
     http_req_blocked...............: avg=74.12µs  min=872ns    med=2.63µs  max=139.05ms p(90)=4.15µs   p(95)=5.3µs    p(99.9)=28.57ms 
     http_req_connecting............: avg=69.47µs  min=0s       med=0s      max=139ms    p(90)=0s       p(95)=0s       p(99.9)=27.76ms 
     http_req_duration..............: avg=48.05ms  min=744.43µs med=40.41ms max=317.51ms p(90)=101.4ms  p(95)=125.49ms p(99.9)=181.08ms
       { expected_response:true }...: avg=48.05ms  min=744.43µs med=40.41ms max=317.51ms p(90)=101.4ms  p(95)=125.49ms p(99.9)=181.08ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 286385
     http_req_receiving.............: avg=348.82µs min=23.14µs  med=54.19µs max=218.98ms p(90)=218.44µs p(95)=370.57µs p(99.9)=44.59ms 
     http_req_sending...............: avg=161.14µs min=4.01µs   med=9.26µs  max=246.6ms  p(90)=17.41µs  p(95)=119µs    p(99.9)=28.94ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.54ms  min=709.09µs med=40.07ms max=293.74ms p(90)=100.22ms p(95)=124.19ms p(99.9)=177.46ms
     http_reqs......................: 286385  4700.081253/s
     iteration_duration.............: avg=49.9ms   min=1.19ms   med=41.19ms max=330.16ms p(90)=106.01ms p(95)=132.43ms p(99.9)=204.41ms
     iterations.....................: 285385  4683.669496/s
     success_rate...................: 100.00% ✓ 285385      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 854133      ✗ 0     
     data_received..................: 25 GB   410 MB/s
     data_sent......................: 343 MB  5.6 MB/s
     http_req_blocked...............: avg=74.5µs   min=912ns    med=2.57µs  max=140.02ms p(90)=4.14µs   p(95)=5.32µs   p(99.9)=30.34ms 
     http_req_connecting............: avg=69.75µs  min=0s       med=0s      max=139.96ms p(90)=0s       p(95)=0s       p(99.9)=29.63ms 
     http_req_duration..............: avg=47.84ms  min=742.03µs med=40.4ms  max=301.03ms p(90)=101.22ms p(95)=126.3ms  p(99.9)=185.23ms
       { expected_response:true }...: avg=47.84ms  min=742.03µs med=40.4ms  max=301.03ms p(90)=101.22ms p(95)=126.3ms  p(99.9)=185.23ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 285711
     http_req_receiving.............: avg=364.55µs min=23.42µs  med=53.86µs max=144.39ms p(90)=216.21µs p(95)=375.26µs p(99.9)=50.1ms  
     http_req_sending...............: avg=163.39µs min=4.02µs   med=9.01µs  max=216.51ms p(90)=17.04µs  p(95)=119.89µs p(99.9)=29.93ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.31ms  min=696.1µs  med=40.05ms max=300.49ms p(90)=100ms    p(95)=124.86ms p(99.9)=179.46ms
     http_reqs......................: 285711  4688.865505/s
     iteration_duration.............: avg=50.02ms  min=1.3ms    med=41.46ms max=354.18ms p(90)=106ms    p(95)=132.97ms p(99.9)=218.69ms
     iterations.....................: 284711  4672.454287/s
     success_rate...................: 100.00% ✓ 284711      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 830244      ✗ 0     
     data_received..................: 24 GB   399 MB/s
     data_sent......................: 334 MB  5.5 MB/s
     http_req_blocked...............: avg=67.92µs  min=1µs      med=2.6µs   max=133.36ms p(90)=4.2µs    p(95)=5.36µs   p(99.9)=23.73ms 
     http_req_connecting............: avg=63.8µs   min=0s       med=0s      max=126.16ms p(90)=0s       p(95)=0s       p(99.9)=22.68ms 
     http_req_duration..............: avg=49.28ms  min=792.76µs med=40.69ms max=328.98ms p(90)=106.47ms p(95)=132.48ms p(99.9)=191.24ms
       { expected_response:true }...: avg=49.28ms  min=792.76µs med=40.69ms max=328.98ms p(90)=106.47ms p(95)=132.48ms p(99.9)=191.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 277748
     http_req_receiving.............: avg=371.33µs min=26.26µs  med=53.76µs max=200.99ms p(90)=223.17µs p(95)=392.46µs p(99.9)=50.44ms 
     http_req_sending...............: avg=158.67µs min=4µs      med=9.14µs  max=136.89ms p(90)=17.76µs  p(95)=127.68µs p(99.9)=28.38ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.75ms  min=743.61µs med=40.36ms max=328.38ms p(90)=105.19ms p(95)=131.14ms p(99.9)=184.26ms
     http_reqs......................: 277748  4555.149191/s
     iteration_duration.............: avg=51.44ms  min=1.26ms   med=41.77ms max=337.28ms p(90)=111.21ms p(95)=139.35ms p(99.9)=225.62ms
     iterations.....................: 276748  4538.748896/s
     success_rate...................: 100.00% ✓ 276748      ✗ 0     
     vus............................: 56      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 829818      ✗ 0     
     data_received..................: 24 GB   398 MB/s
     data_sent......................: 334 MB  5.5 MB/s
     http_req_blocked...............: avg=69.3µs   min=822ns    med=2.58µs  max=128.81ms p(90)=4.15µs   p(95)=5.32µs   p(99.9)=25.33ms 
     http_req_connecting............: avg=64.73µs  min=0s       med=0s      max=128.45ms p(90)=0s       p(95)=0s       p(99.9)=24.79ms 
     http_req_duration..............: avg=49.66ms  min=793.68µs med=41.4ms  max=309.17ms p(90)=106.62ms p(95)=132.85ms p(99.9)=190.84ms
       { expected_response:true }...: avg=49.66ms  min=793.68µs med=41.4ms  max=309.17ms p(90)=106.62ms p(95)=132.85ms p(99.9)=190.84ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 277606
     http_req_receiving.............: avg=350.61µs min=24.91µs  med=54.6µs  max=140.34ms p(90)=226.96µs p(95)=397.44µs p(99.9)=46.71ms 
     http_req_sending...............: avg=152.62µs min=3.99µs   med=9.11µs  max=228.04ms p(90)=17.5µs   p(95)=126.84µs p(99.9)=26.75ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.16ms  min=754.31µs med=41.06ms max=308.59ms p(90)=105.37ms p(95)=131.51ms p(99.9)=184.37ms
     http_reqs......................: 277606  4552.658235/s
     iteration_duration.............: avg=51.5ms   min=1.21ms   med=42.32ms max=330.86ms p(90)=110.84ms p(95)=139.26ms p(99.9)=211.36ms
     iterations.....................: 276606  4536.258524/s
     success_rate...................: 100.00% ✓ 276606      ✗ 0     
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

     checks.........................: 100.00% ✓ 822681      ✗ 0     
     data_received..................: 24 GB   395 MB/s
     data_sent......................: 331 MB  5.4 MB/s
     http_req_blocked...............: avg=62.01µs  min=971ns    med=2.66µs  max=149.85ms p(90)=4.26µs   p(95)=5.32µs   p(99.9)=21.16ms 
     http_req_connecting............: avg=58.15µs  min=0s       med=0s      max=122.32ms p(90)=0s       p(95)=0s       p(99.9)=21.08ms 
     http_req_duration..............: avg=50.03ms  min=658.96µs med=41.35ms max=331.67ms p(90)=108.28ms p(95)=135.46ms p(99.9)=200.99ms
       { expected_response:true }...: avg=50.03ms  min=658.96µs med=41.35ms max=331.67ms p(90)=108.28ms p(95)=135.46ms p(99.9)=200.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 275227
     http_req_receiving.............: avg=321.39µs min=22.73µs  med=52.61µs max=126.14ms p(90)=222.02µs p(95)=397.22µs p(99.9)=44.21ms 
     http_req_sending...............: avg=145.17µs min=4.26µs   med=9.27µs  max=113.83ms p(90)=17.62µs  p(95)=128.36µs p(99.9)=26.28ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.57ms  min=610.9µs  med=41.05ms max=321.76ms p(90)=107.22ms p(95)=134.26ms p(99.9)=197.47ms
     http_reqs......................: 275227  4521.098055/s
     iteration_duration.............: avg=51.92ms  min=1.05ms   med=42.42ms max=342.5ms  p(90)=112.54ms p(95)=140.88ms p(99.9)=228.29ms
     iterations.....................: 274227  4504.671258/s
     success_rate...................: 100.00% ✓ 274227      ✗ 0     
     vus............................: 51      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.19-nightly.9815b25d)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 738018      ✗ 0     
     data_received..................: 22 GB   354 MB/s
     data_sent......................: 297 MB  4.9 MB/s
     http_req_blocked...............: avg=45.19µs  min=781ns    med=2.14µs  max=115.32ms p(90)=3.89µs   p(95)=5.18µs   p(99.9)=7.49ms  
     http_req_connecting............: avg=42.22µs  min=0s       med=0s      max=115.15ms p(90)=0s       p(95)=0s       p(99.9)=7.4ms   
     http_req_duration..............: avg=56.7ms   min=885.2µs  med=48.16ms max=323.07ms p(90)=119.27ms p(95)=148.75ms p(99.9)=219.37ms
       { expected_response:true }...: avg=56.7ms   min=885.2µs  med=48.16ms max=323.07ms p(90)=119.27ms p(95)=148.75ms p(99.9)=219.37ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 247006
     http_req_receiving.............: avg=269.44µs min=25.65µs  med=52.9µs  max=156.93ms p(90)=212.04µs p(95)=382.4µs  p(99.9)=39.59ms 
     http_req_sending...............: avg=121.47µs min=4.29µs   med=8.92µs  max=189.56ms p(90)=18.13µs  p(95)=126.96µs p(99.9)=22.48ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=56.3ms   min=826.06µs med=47.89ms max=322.66ms p(90)=118.36ms p(95)=147.75ms p(99.9)=216.15ms
     http_reqs......................: 247006  4042.527268/s
     iteration_duration.............: avg=57.88ms  min=1.37ms   med=49.03ms max=348.79ms p(90)=121.57ms p(95)=151.64ms p(99.9)=232.36ms
     iterations.....................: 246006  4026.161158/s
     success_rate...................: 100.00% ✓ 246006      ✗ 0     
     vus............................: 62      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 728838      ✗ 0     
     data_received..................: 21 GB   349 MB/s
     data_sent......................: 293 MB  4.8 MB/s
     http_req_blocked...............: avg=52.79µs  min=961ns    med=2.79µs  max=139.05ms p(90)=4.61µs   p(95)=5.93µs   p(99.9)=14.67ms 
     http_req_connecting............: avg=49.17µs  min=0s       med=0s      max=138.83ms p(90)=0s       p(95)=0s       p(99.9)=14.52ms 
     http_req_duration..............: avg=57.31ms  min=865.44µs med=47.97ms max=298.98ms p(90)=122.78ms p(95)=153.07ms p(99.9)=218.04ms
       { expected_response:true }...: avg=57.31ms  min=865.44µs med=47.97ms max=298.98ms p(90)=122.78ms p(95)=153.07ms p(99.9)=218.04ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 243946
     http_req_receiving.............: avg=290.9µs  min=26.16µs  med=55.71µs max=153.85ms p(90)=227.99µs p(95)=409.4µs  p(99.9)=40.63ms 
     http_req_sending...............: avg=136.51µs min=4.18µs   med=9.8µs   max=128.27ms p(90)=19.36µs  p(95)=136.09µs p(99.9)=24.58ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=56.88ms  min=823.78µs med=47.66ms max=297.72ms p(90)=121.85ms p(95)=152.18ms p(99.9)=214.53ms
     http_reqs......................: 243946  3994.416088/s
     iteration_duration.............: avg=58.64ms  min=1.62ms   med=48.99ms max=360.55ms p(90)=125.82ms p(95)=156.54ms p(99.9)=228.6ms 
     iterations.....................: 242946  3978.041907/s
     success_rate...................: 100.00% ✓ 242946      ✗ 0     
     vus............................: 60      min=0         max=497 
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

     checks.........................: 100.00% ✓ 263157      ✗ 0    
     data_received..................: 7.8 GB  125 MB/s
     data_sent......................: 107 MB  1.7 MB/s
     http_req_blocked...............: avg=4.91µs   min=871ns   med=2.32µs   max=15.68ms  p(90)=4.02µs   p(95)=5.04µs   p(99.9)=358.96µs
     http_req_connecting............: avg=1.97µs   min=0s      med=0s       max=15.61ms  p(90)=0s       p(95)=0s       p(99.9)=301.27µs
     http_req_duration..............: avg=160.75ms min=1.89ms  med=131.85ms max=949.12ms p(90)=341.45ms p(95)=402.29ms p(99.9)=657.57ms
       { expected_response:true }...: avg=160.75ms min=1.89ms  med=131.85ms max=949.12ms p(90)=341.45ms p(95)=402.29ms p(99.9)=657.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 88719
     http_req_receiving.............: avg=72.96µs  min=27.41µs med=57.59µs  max=72.02ms  p(90)=93.9µs   p(95)=110.14µs p(99.9)=1.74ms  
     http_req_sending...............: avg=29.85µs  min=4.87µs  med=10.64µs  max=94.88ms  p(90)=17µs     p(95)=20.74µs  p(99.9)=3.76ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=160.64ms min=1.84ms  med=131.77ms max=949.06ms p(90)=341.34ms p(95)=402.2ms  p(99.9)=657.49ms
     http_reqs......................: 88719   1424.385765/s
     iteration_duration.............: avg=162.82ms min=7.14ms  med=134.06ms max=949.31ms p(90)=342.86ms p(95)=403.38ms p(99.9)=657.79ms
     iterations.....................: 87719   1408.33074/s
     success_rate...................: 100.00% ✓ 87719       ✗ 0    
     vus............................: 69      min=0         max=495
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.373.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 243762      ✗ 0    
     data_received..................: 7.2 GB  115 MB/s
     data_sent......................: 99 MB   1.6 MB/s
     http_req_blocked...............: avg=6.29µs   min=1.09µs  med=2.78µs   max=20.92ms  p(90)=4.45µs   p(95)=5.41µs   p(99.9)=353.86µs
     http_req_connecting............: avg=2.77µs   min=0s      med=0s       max=20.88ms  p(90)=0s       p(95)=0s       p(99.9)=320.98µs
     http_req_duration..............: avg=173.36ms min=1.99ms  med=170.92ms max=481.68ms p(90)=330.94ms p(95)=354.03ms p(99.9)=421.92ms
       { expected_response:true }...: avg=173.36ms min=1.99ms  med=170.92ms max=481.68ms p(90)=330.94ms p(95)=354.03ms p(99.9)=421.92ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 82254
     http_req_receiving.............: avg=77.94µs  min=26.95µs med=61.64µs  max=35.73ms  p(90)=99.54µs  p(95)=116.12µs p(99.9)=1.56ms  
     http_req_sending...............: avg=32.13µs  min=4.99µs  med=11.67µs  max=176.93ms p(90)=18.41µs  p(95)=22.35µs  p(99.9)=3.24ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=173.25ms min=1.9ms   med=170.81ms max=481.6ms  p(90)=330.79ms p(95)=353.94ms p(99.9)=421.85ms
     http_reqs......................: 82254   1317.636793/s
     iteration_duration.............: avg=175.73ms min=4.48ms  med=173.57ms max=481.89ms p(90)=331.73ms p(95)=354.55ms p(99.9)=422.15ms
     iterations.....................: 81254   1301.617671/s
     success_rate...................: 100.00% ✓ 81254       ✗ 0    
     vus............................: 76      min=0         max=493
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 105696     ✗ 0    
     data_received..................: 3.2 GB  49 MB/s
     data_sent......................: 44 MB   678 kB/s
     http_req_blocked...............: avg=7.63µs   min=1.15µs  med=3.23µs   max=14.85ms  p(90)=5.02µs   p(95)=6.13µs   p(99.9)=561.72µs
     http_req_connecting............: avg=3.38µs   min=0s      med=0s       max=14.76ms  p(90)=0s       p(95)=0s       p(99.9)=527.99µs
     http_req_duration..............: avg=395.87ms min=3.33ms  med=364.4ms  max=1.68s    p(90)=780.49ms p(95)=847.6ms  p(99.9)=1.34s   
       { expected_response:true }...: avg=395.87ms min=3.33ms  med=364.4ms  max=1.68s    p(90)=780.49ms p(95)=847.6ms  p(99.9)=1.34s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 36232
     http_req_receiving.............: avg=88.54µs  min=28.98µs med=72.48µs  max=199.27ms p(90)=109.82µs p(95)=124.5µs  p(99.9)=829.34µs
     http_req_sending...............: avg=30.16µs  min=5.6µs   med=14.25µs  max=96.73ms  p(90)=20.92µs  p(95)=23.69µs  p(99.9)=2.71ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=395.75ms min=3.28ms  med=364.31ms max=1.68s    p(90)=780.41ms p(95)=847.49ms p(99.9)=1.34s   
     http_reqs......................: 36232   564.753248/s
     iteration_duration.............: avg=407.35ms min=24.73ms med=378.2ms  max=1.68s    p(90)=784.28ms p(95)=850.48ms p(99.9)=1.35s   
     iterations.....................: 35232   549.166108/s
     success_rate...................: 100.00% ✓ 35232      ✗ 0    
     vus............................: 62      min=0        max=497
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 52317      ✗ 0    
     data_received..................: 1.6 GB  24 MB/s
     data_sent......................: 22 MB   330 kB/s
     http_req_blocked...............: avg=14.23µs  min=1.19µs  med=3.62µs   max=17.41ms  p(90)=5.41µs   p(95)=6.91µs   p(99.9)=2.08ms
     http_req_connecting............: avg=8.99µs   min=0s      med=0s       max=17.32ms  p(90)=0s       p(95)=0s       p(99.9)=2.04ms
     http_req_duration..............: avg=786.2ms  min=5.22ms  med=705.23ms max=4.17s    p(90)=1.55s    p(95)=1.87s    p(99.9)=3.27s 
       { expected_response:true }...: avg=786.2ms  min=5.22ms  med=705.23ms max=4.17s    p(90)=1.55s    p(95)=1.87s    p(99.9)=3.27s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 18439
     http_req_receiving.............: avg=99.99µs  min=35.76µs med=88.4µs   max=58.62ms  p(90)=126.02µs p(95)=143.34µs p(99.9)=1.28ms
     http_req_sending...............: avg=49.07µs  min=5.8µs   med=17.51µs  max=176.81ms p(90)=22.95µs  p(95)=26.14µs  p(99.9)=2.91ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=786.05ms min=5.13ms  med=705.13ms max=4.17s    p(90)=1.55s    p(95)=1.87s    p(99.9)=3.27s 
     http_reqs......................: 18439   275.318294/s
     iteration_duration.............: avg=831.4ms  min=27.88ms med=776.82ms max=4.17s    p(90)=1.57s    p(95)=1.88s    p(99.9)=3.31s 
     iterations.....................: 17439   260.386991/s
     success_rate...................: 100.00% ✓ 17439      ✗ 0    
     vus............................: 12      min=0        max=500
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

     checks.........................: 100.00% ✓ 45900      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   285 kB/s
     http_req_blocked...............: avg=11.91µs  min=922ns   med=3.07µs   max=9.97ms  p(90)=4.68µs   p(95)=6.03µs   p(99.9)=1.47ms  
     http_req_connecting............: avg=7.29µs   min=0s      med=0s       max=9.92ms  p(90)=0s       p(95)=0s       p(99.9)=1.44ms  
     http_req_duration..............: avg=891.27ms min=7.54ms  med=825.96ms max=3.01s   p(90)=1.82s    p(95)=1.95s    p(99.9)=2.63s   
       { expected_response:true }...: avg=891.27ms min=7.54ms  med=825.96ms max=3.01s   p(90)=1.82s    p(95)=1.95s    p(99.9)=2.63s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16300
     http_req_receiving.............: avg=89.92µs  min=30.73µs med=83.4µs   max=8.99ms  p(90)=119.89µs p(95)=133.03µs p(99.9)=986.85µs
     http_req_sending...............: avg=29.24µs  min=5.14µs  med=15.57µs  max=48.34ms p(90)=20.24µs  p(95)=23.73µs  p(99.9)=3.57ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=891.15ms min=7.47ms  med=825.84ms max=3.01s   p(90)=1.82s    p(95)=1.95s    p(99.9)=2.63s   
     http_reqs......................: 16300   237.820183/s
     iteration_duration.............: avg=949.45ms min=64.52ms med=892.95ms max=3.02s   p(90)=1.83s    p(95)=1.96s    p(99.9)=2.64s   
     iterations.....................: 15300   223.229988/s
     success_rate...................: 100.00% ✓ 15300      ✗ 0    
     vus............................: 83      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

