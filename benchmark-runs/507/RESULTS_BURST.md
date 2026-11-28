## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| nitro-router-fed | 16.8.0-p.25 | 4,907 | 4,918 | 4,790 | 1.1% | 153 MB | 32.0 KB |  |
| fusion-net-11 | 16.7.7 | 4,842 | 4,849 | 4,804 | 0.4% | 387 MB | 81.9 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.25 | 4,839 | 4,877 | 4,770 | 1.0% | 122 MB | 25.7 KB |  |
| nitro-router | 16.8.0-p.25 | 4,827 | 4,968 | 4,816 | 1.3% | 148 MB | 31.5 KB |  |
| fusion-aot-11 | 16.7.7 | 4,803 | 4,804 | 4,785 | 0.2% | 148 MB | 31.5 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 4,778 | 4,809 | 4,725 | 0.7% | 161 MB | 34.4 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.25 | 4,764 | 4,844 | 4,752 | 0.8% | 368 MB | 79.2 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.25 | 4,757 | 4,910 | 4,750 | 1.4% | 373 MB | 80.3 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.25 | 4,723 | 4,729 | 4,713 | 0.1% | 123 MB | 26.6 KB |  |
| feddi-gateway | 2026-11-22-1912 | 4,667 | 4,683 | 4,662 | 0.2% | 2,326 MB | 510.4 KB |  |
| fusion-fed-net-11 | 16.7.7 | 4,667 | 4,799 | 4,661 | 1.3% | 401 MB | 88.0 KB |  |
| hive-router | v0.3.21 | 4,076 | 4,120 | 4,034 | 0.8% | 191 MB | 47.9 KB |  |
| hive-router-nightly | v0.3.21-nightly.f689b548 | 4,057 | 4,081 | 3,993 | 0.9% | 195 MB | 49.3 KB |  |
| caliban | 3.2.1 | 1,444 | 1,448 | 1,424 | 0.7% | 11,404 MB | 8,087.1 KB |  |
| cosmo | 0.378.1 | 1,287 | 1,291 | 1,285 | 0.2% | 576 MB | 458.0 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 562 | 564 | 558 | 0.4% | 3,030 MB | 5,520.4 KB |  |
| hive-gateway | 2.15.10 | 272 | 273 | 271 | 0.4% | 3,697 MB | 13,917.5 KB |  |
| apollo-gateway | 2.14.4 | 241 | 242 | 240 | 0.3% | 2,420 MB | 10,282.6 KB |  |
| apollo-router | v2.19.1 | — | — | — | — | — | — | non-compatible response (9738 across 5/5 runs) |
| apollo-router-nightly | v3.0.0-preview.0-nightly.95b76d0a | — | — | — | — | — | — | non-compatible response (5379 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (172217 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: nitro-router-fed (HotChocolate subgraphs) (16.8.0-p.25)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 893865      ✗ 0     
     data_received..................: 26 GB   429 MB/s
     data_sent......................: 359 MB  5.9 MB/s
     http_req_blocked...............: avg=70.24µs  min=742ns    med=2.1µs   max=135.22ms p(90)=3.69µs   p(95)=4.79µs   p(99.9)=27.68ms 
     http_req_connecting............: avg=66.84µs  min=0s       med=0s      max=135.15ms p(90)=0s       p(95)=0s       p(99.9)=26.23ms 
     http_req_duration..............: avg=45.53ms  min=735.6µs  med=38.45ms max=235.77ms p(90)=94.59ms  p(95)=117.84ms p(99.9)=176.52ms
       { expected_response:true }...: avg=45.53ms  min=735.6µs  med=38.45ms max=235.77ms p(90)=94.59ms  p(95)=117.84ms p(99.9)=176.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 298955
     http_req_receiving.............: avg=377.03µs min=24.83µs  med=52.41µs max=119ms    p(90)=194.33µs p(95)=344.03µs p(99.9)=53.61ms 
     http_req_sending...............: avg=157.96µs min=3.96µs   med=8.63µs  max=95.93ms  p(90)=16.02µs  p(95)=109.42µs p(99.9)=28.07ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=44.99ms  min=691.26µs med=38.08ms max=235.43ms p(90)=93.31ms  p(95)=116.34ms p(99.9)=168ms   
     http_reqs......................: 298955  4907.114132/s
     iteration_duration.............: avg=47.8ms   min=1.17ms   med=39.51ms max=376.47ms p(90)=100.73ms p(95)=125.88ms p(99.9)=207.64ms
     iterations.....................: 297955  4890.699909/s
     success_rate...................: 100.00% ✓ 297955      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 882273      ✗ 0     
     data_received..................: 26 GB   424 MB/s
     data_sent......................: 355 MB  5.8 MB/s
     http_req_blocked...............: avg=64.65µs  min=802ns    med=2.06µs  max=169.57ms p(90)=3.63µs   p(95)=4.72µs   p(99.9)=24.9ms  
     http_req_connecting............: avg=60.25µs  min=0s       med=0s      max=150.09ms p(90)=0s       p(95)=0s       p(99.9)=23.85ms 
     http_req_duration..............: avg=46.6ms   min=732.36µs med=39.23ms max=336.31ms p(90)=98.34ms  p(95)=122.52ms p(99.9)=177.49ms
       { expected_response:true }...: avg=46.6ms   min=732.36µs med=39.23ms max=336.31ms p(90)=98.34ms  p(95)=122.52ms p(99.9)=177.49ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 295091
     http_req_receiving.............: avg=317.95µs min=22.69µs  med=51.39µs max=139.92ms p(90)=200.68µs p(95)=352.41µs p(99.9)=43.31ms 
     http_req_sending...............: avg=144.35µs min=4.09µs   med=8.47µs  max=127.29ms p(90)=16.29µs  p(95)=113.62µs p(99.9)=25.75ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.14ms  min=685.34µs med=38.92ms max=335.9ms  p(90)=97.22ms  p(95)=121.49ms p(99.9)=173.83ms
     http_reqs......................: 295091  4842.924266/s
     iteration_duration.............: avg=48.43ms  min=1.19ms   med=40.09ms max=345.43ms p(90)=102.48ms p(95)=128.38ms p(99.9)=204.03ms
     iterations.....................: 294091  4826.512636/s
     success_rate...................: 100.00% ✓ 294091      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.25)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 881247      ✗ 0     
     data_received..................: 26 GB   423 MB/s
     data_sent......................: 354 MB  5.8 MB/s
     http_req_blocked...............: avg=67.67µs  min=772ns    med=2.06µs  max=126.78ms p(90)=3.61µs   p(95)=4.66µs   p(99.9)=26.23ms 
     http_req_connecting............: avg=63.72µs  min=0s       med=0s      max=126.73ms p(90)=0s       p(95)=0s       p(99.9)=25.44ms 
     http_req_duration..............: avg=46.09ms  min=731.88µs med=38.66ms max=298.77ms p(90)=96.83ms  p(95)=120.68ms p(99.9)=175.9ms 
       { expected_response:true }...: avg=46.09ms  min=731.88µs med=38.66ms max=298.77ms p(90)=96.83ms  p(95)=120.68ms p(99.9)=175.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 294749
     http_req_receiving.............: avg=327.01µs min=23.21µs  med=52.29µs max=130.89ms p(90)=200.22µs p(95)=351.78µs p(99.9)=44.31ms 
     http_req_sending...............: avg=158.04µs min=3.9µs    med=8.61µs  max=199.59ms p(90)=16µs     p(95)=112.64µs p(99.9)=28.01ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=45.6ms   min=688.59µs med=38.29ms max=298.54ms p(90)=95.65ms  p(95)=119.46ms p(99.9)=171.93ms
     http_reqs......................: 294749  4839.004531/s
     iteration_duration.............: avg=48.49ms  min=1.22ms   med=39.97ms max=320.2ms  p(90)=102.93ms p(95)=128.74ms p(99.9)=209.6ms 
     iterations.....................: 293749  4822.587157/s
     success_rate...................: 100.00% ✓ 293749      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: nitro-router (HotChocolate subgraphs) (16.8.0-p.25)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 879177      ✗ 0     
     data_received..................: 26 GB   422 MB/s
     data_sent......................: 353 MB  5.8 MB/s
     http_req_blocked...............: avg=73.53µs  min=802ns    med=2.56µs  max=176.41ms p(90)=4.02µs   p(95)=5.12µs   p(99.9)=29.15ms 
     http_req_connecting............: avg=69.64µs  min=0s       med=0s      max=176.34ms p(90)=0s       p(95)=0s       p(99.9)=28.86ms 
     http_req_duration..............: avg=46.21ms  min=742.71µs med=39.04ms max=304.8ms  p(90)=96.89ms  p(95)=118.9ms  p(99.9)=174.71ms
       { expected_response:true }...: avg=46.21ms  min=742.71µs med=39.04ms max=304.8ms  p(90)=96.89ms  p(95)=118.9ms  p(99.9)=174.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 294059
     http_req_receiving.............: avg=370.38µs min=25.39µs  med=53µs    max=201.1ms  p(90)=213.07µs p(95)=358.31µs p(99.9)=49.85ms 
     http_req_sending...............: avg=159.52µs min=3.99µs   med=8.89µs  max=187.93ms p(90)=16.4µs   p(95)=114.98µs p(99.9)=28.11ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=45.68ms  min=701.54µs med=38.63ms max=304.2ms  p(90)=95.56ms  p(95)=117.56ms p(99.9)=169.76ms
     http_reqs......................: 294059  4827.358625/s
     iteration_duration.............: avg=48.6ms   min=1.1ms    med=40.21ms max=368.26ms p(90)=102.39ms p(95)=127.86ms p(99.9)=209.08ms
     iterations.....................: 293059  4810.942332/s
     success_rate...................: 100.00% ✓ 293059      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 875730      ✗ 0     
     data_received..................: 26 GB   420 MB/s
     data_sent......................: 352 MB  5.8 MB/s
     http_req_blocked...............: avg=60.97µs  min=791ns    med=2.05µs  max=143.5ms  p(90)=3.66µs   p(95)=4.8µs    p(99.9)=21.34ms 
     http_req_connecting............: avg=57.61µs  min=0s       med=0s      max=137.64ms p(90)=0s       p(95)=0s       p(99.9)=20.2ms  
     http_req_duration..............: avg=47.14ms  min=779.69µs med=39.3ms  max=248.12ms p(90)=100.86ms p(95)=125.71ms p(99.9)=177.7ms 
       { expected_response:true }...: avg=47.14ms  min=779.69µs med=39.3ms  max=248.12ms p(90)=100.86ms p(95)=125.71ms p(99.9)=177.7ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 292910
     http_req_receiving.............: avg=313.94µs min=24.29µs  med=50.72µs max=114.56ms p(90)=207.14µs p(95)=363.92µs p(99.9)=41.74ms 
     http_req_sending...............: avg=141.46µs min=3.94µs   med=8.5µs   max=179.5ms  p(90)=16.82µs  p(95)=116.5µs  p(99.9)=24.66ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.69ms  min=738.39µs med=38.97ms max=248.07ms p(90)=99.86ms  p(95)=124.64ms p(99.9)=174.55ms
     http_reqs......................: 292910  4803.108703/s
     iteration_duration.............: avg=48.8ms   min=1.23ms   med=40.14ms max=363.61ms p(90)=104.29ms p(95)=130.6ms  p(99.9)=207.09ms
     iterations.....................: 291910  4786.710803/s
     success_rate...................: 100.00% ✓ 291910      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 871083      ✗ 0     
     data_received..................: 26 GB   418 MB/s
     data_sent......................: 350 MB  5.7 MB/s
     http_req_blocked...............: avg=65.2µs   min=811ns    med=2.11µs  max=128.17ms p(90)=3.72µs   p(95)=4.8µs    p(99.9)=25.56ms 
     http_req_connecting............: avg=61.58µs  min=0s       med=0s      max=128.13ms p(90)=0s       p(95)=0s       p(99.9)=24.93ms 
     http_req_duration..............: avg=47.16ms  min=787.96µs med=40.06ms max=323.31ms p(90)=99.46ms  p(95)=123.92ms p(99.9)=178.45ms
       { expected_response:true }...: avg=47.16ms  min=787.96µs med=40.06ms max=323.31ms p(90)=99.46ms  p(95)=123.92ms p(99.9)=178.45ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 291361
     http_req_receiving.............: avg=321.21µs min=25.12µs  med=51.77µs max=114.09ms p(90)=205.87µs p(95)=359.83µs p(99.9)=44.37ms 
     http_req_sending...............: avg=148.46µs min=3.97µs   med=8.53µs  max=116.95ms p(90)=16.4µs   p(95)=116.08µs p(99.9)=26.04ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.69ms  min=748.44µs med=39.72ms max=322.76ms p(90)=98.33ms  p(95)=122.76ms p(99.9)=173.39ms
     http_reqs......................: 291361  4778.742927/s
     iteration_duration.............: avg=49.05ms  min=1.3ms    med=40.78ms max=332.26ms p(90)=104.31ms p(95)=130.1ms  p(99.9)=212.87ms
     iterations.....................: 290361  4762.341477/s
     success_rate...................: 100.00% ✓ 290361      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.25)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 867582      ✗ 0     
     data_received..................: 25 GB   417 MB/s
     data_sent......................: 349 MB  5.7 MB/s
     http_req_blocked...............: avg=81.59µs  min=861ns    med=2.68µs  max=149.51ms p(90)=4.19µs   p(95)=5.37µs   p(99.9)=33.68ms 
     http_req_connecting............: avg=77.07µs  min=0s       med=0s      max=149.43ms p(90)=0s       p(95)=0s       p(99.9)=32.4ms  
     http_req_duration..............: avg=46.54ms  min=710.86µs med=39.79ms max=330.72ms p(90)=95.81ms  p(95)=117.98ms p(99.9)=181.27ms
       { expected_response:true }...: avg=46.54ms  min=710.86µs med=39.79ms max=330.72ms p(90)=95.81ms  p(95)=117.98ms p(99.9)=181.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 290194
     http_req_receiving.............: avg=392.22µs min=26.27µs  med=55µs    max=180.65ms p(90)=202.96µs p(95)=352.72µs p(99.9)=55.08ms 
     http_req_sending...............: avg=177.05µs min=3.92µs   med=9.56µs  max=133.33ms p(90)=17.5µs   p(95)=114.96µs p(99.9)=31.56ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=45.97ms  min=669.54µs med=39.4ms  max=320.82ms p(90)=94.57ms  p(95)=116.51ms p(99.9)=173.56ms
     http_reqs......................: 290194  4764.285903/s
     iteration_duration.............: avg=49.25ms  min=1.13ms   med=41.06ms max=354.81ms p(90)=103.22ms p(95)=127.72ms p(99.9)=205.73ms
     iterations.....................: 289194  4747.868314/s
     success_rate...................: 100.00% ✓ 289194      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.25)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 866385      ✗ 0     
     data_received..................: 25 GB   416 MB/s
     data_sent......................: 348 MB  5.7 MB/s
     http_req_blocked...............: avg=82.68µs  min=912ns    med=2.59µs  max=151.94ms p(90)=4.06µs   p(95)=5.2µs    p(99.9)=35.29ms 
     http_req_connecting............: avg=78.96µs  min=0s       med=0s      max=151.72ms p(90)=0s       p(95)=0s       p(99.9)=35.03ms 
     http_req_duration..............: avg=46.86ms  min=703.73µs med=40.06ms max=270.14ms p(90)=97.37ms  p(95)=120.6ms  p(99.9)=178.37ms
       { expected_response:true }...: avg=46.86ms  min=703.73µs med=40.06ms max=270.14ms p(90)=97.37ms  p(95)=120.6ms  p(99.9)=178.37ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 289795
     http_req_receiving.............: avg=367.16µs min=26.06µs  med=55µs    max=135.3ms  p(90)=206.28µs p(95)=359.75µs p(99.9)=48.28ms 
     http_req_sending...............: avg=175.63µs min=4.11µs   med=9.18µs  max=133.72ms p(90)=16.99µs  p(95)=116.29µs p(99.9)=31.75ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.31ms  min=669.83µs med=39.69ms max=270.07ms p(90)=96.04ms  p(95)=119.38ms p(99.9)=173.01ms
     http_reqs......................: 289795  4757.515619/s
     iteration_duration.............: avg=49.32ms  min=1.12ms   med=41.02ms max=338.57ms p(90)=104.99ms p(95)=128.85ms p(99.9)=207.71ms
     iterations.....................: 288795  4741.098788/s
     success_rate...................: 100.00% ✓ 288795      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.25)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 860460      ✗ 0     
     data_received..................: 25 GB   413 MB/s
     data_sent......................: 346 MB  5.7 MB/s
     http_req_blocked...............: avg=76.95µs  min=911ns    med=2.68µs  max=149.86ms p(90)=4.25µs   p(95)=5.45µs   p(99.9)=31.21ms 
     http_req_connecting............: avg=73.42µs  min=0s       med=0s      max=149.8ms  p(90)=0s       p(95)=0s       p(99.9)=31.05ms 
     http_req_duration..............: avg=47.07ms  min=735.5µs  med=40.26ms max=250.94ms p(90)=97.62ms  p(95)=120.72ms p(99.9)=176.46ms
       { expected_response:true }...: avg=47.07ms  min=735.5µs  med=40.26ms max=250.94ms p(90)=97.62ms  p(95)=120.72ms p(99.9)=176.46ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 287820
     http_req_receiving.............: avg=375.94µs min=22.33µs  med=54.74µs max=141.99ms p(90)=207.67µs p(95)=361.58µs p(99.9)=48.92ms 
     http_req_sending...............: avg=177.69µs min=3.9µs    med=9.44µs  max=173.28ms p(90)=17.41µs  p(95)=118.59µs p(99.9)=33.3ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.52ms  min=699.34µs med=39.87ms max=237.84ms p(90)=96.36ms  p(95)=119.24ms p(99.9)=171.6ms 
     http_reqs......................: 287820  4723.527593/s
     iteration_duration.............: avg=49.65ms  min=1.11ms   med=41.26ms max=386.92ms p(90)=104.6ms  p(95)=130.15ms p(99.9)=220.44ms
     iterations.....................: 286820  4707.116199/s
     success_rate...................: 100.00% ✓ 286820      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-11-22-1912)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 850491      ✗ 0     
     data_received..................: 25 GB   408 MB/s
     data_sent......................: 342 MB  5.6 MB/s
     http_req_blocked...............: avg=64.88µs  min=782ns    med=2.13µs  max=137.09ms p(90)=3.86µs   p(95)=5.01µs   p(99.9)=22.98ms 
     http_req_connecting............: avg=61.62µs  min=0s       med=0s      max=137.03ms p(90)=0s       p(95)=0s       p(99.9)=22.43ms 
     http_req_duration..............: avg=48.34ms  min=759.61µs med=40.52ms max=320.76ms p(90)=102.21ms p(95)=127.76ms p(99.9)=187.97ms
       { expected_response:true }...: avg=48.34ms  min=759.61µs med=40.52ms max=320.76ms p(90)=102.21ms p(95)=127.76ms p(99.9)=187.97ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 284497
     http_req_receiving.............: avg=337.19µs min=23.98µs  med=53.25µs max=165.23ms p(90)=213.05µs p(95)=373.06µs p(99.9)=45.01ms 
     http_req_sending...............: avg=148.45µs min=4.08µs   med=8.8µs   max=146.2ms  p(90)=16.87µs  p(95)=117.92µs p(99.9)=26.53ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.86ms  min=717.53µs med=40.17ms max=320.31ms p(90)=101.19ms p(95)=126.56ms p(99.9)=183.54ms
     http_reqs......................: 284497  4667.447149/s
     iteration_duration.............: avg=50.24ms  min=1.32ms   med=41.4ms  max=389.81ms p(90)=106.59ms p(95)=134.45ms p(99.9)=222.75ms
     iterations.....................: 283497  4651.041186/s
     success_rate...................: 100.00% ✓ 283497      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 849960      ✗ 0     
     data_received..................: 25 GB   408 MB/s
     data_sent......................: 342 MB  5.6 MB/s
     http_req_blocked...............: avg=75.02µs  min=902ns    med=2.62µs  max=167.33ms p(90)=4.16µs   p(95)=5.33µs   p(99.9)=27.16ms 
     http_req_connecting............: avg=70.32µs  min=0s       med=0s      max=140.62ms p(90)=0s       p(95)=0s       p(99.9)=26.84ms 
     http_req_duration..............: avg=48.08ms  min=733.61µs med=40.46ms max=276.7ms  p(90)=101.02ms p(95)=126.03ms p(99.9)=190.67ms
       { expected_response:true }...: avg=48.08ms  min=733.61µs med=40.46ms max=276.7ms  p(90)=101.02ms p(95)=126.03ms p(99.9)=190.67ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 284320
     http_req_receiving.............: avg=412.72µs min=26.83µs  med=54.78µs max=159.4ms  p(90)=215.85µs p(95)=373.07µs p(99.9)=61.08ms 
     http_req_sending...............: avg=162.72µs min=3.94µs   med=9.1µs   max=122.62ms p(90)=16.76µs  p(95)=118.47µs p(99.9)=29.42ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.51ms  min=695.78µs med=40.1ms  max=276.59ms p(90)=99.65ms  p(95)=124.42ms p(99.9)=180.21ms
     http_reqs......................: 284320  4667.412454/s
     iteration_duration.............: avg=50.27ms  min=1.16ms   med=41.46ms max=359.9ms  p(90)=106.93ms p(95)=134.34ms p(99.9)=210.44ms
     iterations.....................: 283320  4650.9964/s
     success_rate...................: 100.00% ✓ 283320      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 744024      ✗ 0     
     data_received..................: 22 GB   357 MB/s
     data_sent......................: 299 MB  4.9 MB/s
     http_req_blocked...............: avg=48.86µs  min=821ns    med=2.42µs  max=144.86ms p(90)=4.16µs   p(95)=5.42µs   p(99.9)=11.41ms 
     http_req_connecting............: avg=45.11µs  min=0s       med=0s      max=144.76ms p(90)=0s       p(95)=0s       p(99.9)=11.29ms 
     http_req_duration..............: avg=56.14ms  min=869.46µs med=46.89ms max=325.06ms p(90)=119.43ms p(95)=149.53ms p(99.9)=214.58ms
       { expected_response:true }...: avg=56.14ms  min=869.46µs med=46.89ms max=325.06ms p(90)=119.43ms p(95)=149.53ms p(99.9)=214.58ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 249008
     http_req_receiving.............: avg=280.24µs min=25.25µs  med=54.61µs max=208.99ms p(90)=211.07µs p(95)=381.45µs p(99.9)=41.24ms 
     http_req_sending...............: avg=128.17µs min=4.25µs   med=9.36µs  max=199.17ms p(90)=18.5µs   p(95)=127.33µs p(99.9)=23.17ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=55.73ms  min=815.99µs med=46.61ms max=314.67ms p(90)=118.48ms p(95)=148.46ms p(99.9)=211.79ms
     http_reqs......................: 249008  4076.857722/s
     iteration_duration.............: avg=57.45ms  min=1.8ms    med=47.72ms max=361.84ms p(90)=122.26ms p(95)=153.13ms p(99.9)=232.22ms
     iterations.....................: 248008  4060.485326/s
     success_rate...................: 100.00% ✓ 248008      ✗ 0     
     vus............................: 61      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.21-nightly.f689b548)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 740643      ✗ 0     
     data_received..................: 22 GB   355 MB/s
     data_sent......................: 298 MB  4.9 MB/s
     http_req_blocked...............: avg=46.14µs  min=781ns    med=2.12µs  max=167.95ms p(90)=3.81µs   p(95)=5.03µs   p(99.9)=8.15ms  
     http_req_connecting............: avg=42.44µs  min=0s       med=0s      max=167.66ms p(90)=0s       p(95)=0s       p(99.9)=7.41ms  
     http_req_duration..............: avg=56.29ms  min=866.5µs  med=47.67ms max=294.3ms  p(90)=118.3ms  p(95)=147.11ms p(99.9)=211.98ms
       { expected_response:true }...: avg=56.29ms  min=866.5µs  med=47.67ms max=294.3ms  p(90)=118.3ms  p(95)=147.11ms p(99.9)=211.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 247881
     http_req_receiving.............: avg=256.65µs min=21.31µs  med=52.63µs max=108.56ms p(90)=210.67µs p(95)=379.42µs p(99.9)=37.69ms 
     http_req_sending...............: avg=120.18µs min=4.14µs   med=8.98µs  max=148.89ms p(90)=18.2µs   p(95)=127.71µs p(99.9)=21.39ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=55.91ms  min=810.86µs med=47.38ms max=294.23ms p(90)=117.45ms p(95)=146.26ms p(99.9)=208.99ms
     http_reqs......................: 247881  4057.734401/s
     iteration_duration.............: avg=57.71ms  min=1.63ms   med=48.71ms max=319.95ms p(90)=121.39ms p(95)=151.47ms p(99.9)=222.84ms
     iterations.....................: 246881  4041.364713/s
     success_rate...................: 100.00% ✓ 246881      ✗ 0     
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

     checks.........................: 100.00% ✓ 267144      ✗ 0    
     data_received..................: 7.9 GB  126 MB/s
     data_sent......................: 108 MB  1.7 MB/s
     http_req_blocked...............: avg=6.21µs   min=1.2µs   med=3.14µs   max=14.41ms  p(90)=4.93µs   p(95)=5.95µs   p(99.9)=467.18µs
     http_req_connecting............: avg=2.32µs   min=0s      med=0s       max=14.32ms  p(90)=0s       p(95)=0s       p(99.9)=361.31µs
     http_req_duration..............: avg=158.39ms min=1.98ms  med=128.06ms max=1.16s    p(90)=338.06ms p(95)=403.63ms p(99.9)=705.37ms
       { expected_response:true }...: avg=158.39ms min=1.98ms  med=128.06ms max=1.16s    p(90)=338.06ms p(95)=403.63ms p(99.9)=705.37ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 90048
     http_req_receiving.............: avg=84.57µs  min=29.37µs med=63.23µs  max=227.77ms p(90)=101.14µs p(95)=119.49µs p(99.9)=2.14ms  
     http_req_sending...............: avg=35.95µs  min=4.96µs  med=12.71µs  max=138.84ms p(90)=19.1µs   p(95)=23.34µs  p(99.9)=4.4ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=158.27ms min=1.92ms  med=127.95ms max=1.16s    p(90)=337.96ms p(95)=403.55ms p(99.9)=705.32ms
     http_reqs......................: 90048   1444.662539/s
     iteration_duration.............: avg=160.42ms min=7.13ms  med=130.44ms max=1.16s    p(90)=339.41ms p(95)=405.1ms  p(99.9)=705.72ms
     iterations.....................: 89048   1428.619289/s
     success_rate...................: 100.00% ✓ 89048       ✗ 0    
     vus............................: 73      min=0         max=494
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.378.1)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 238065      ✗ 0    
     data_received..................: 7.0 GB  113 MB/s
     data_sent......................: 97 MB   1.5 MB/s
     http_req_blocked...............: avg=4.96µs   min=892ns   med=2.12µs   max=8.71ms   p(90)=3.63µs   p(95)=4.48µs   p(99.9)=295.05µs
     http_req_connecting............: avg=2.19µs   min=0s      med=0s       max=8.65ms   p(90)=0s       p(95)=0s       p(99.9)=191.95µs
     http_req_duration..............: avg=177.53ms min=1.95ms  med=175.55ms max=483.47ms p(90)=336.57ms p(95)=362.01ms p(99.9)=428.85ms
       { expected_response:true }...: avg=177.53ms min=1.95ms  med=175.55ms max=483.47ms p(90)=336.57ms p(95)=362.01ms p(99.9)=428.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 80355
     http_req_receiving.............: avg=69.83µs  min=26.83µs med=57.98µs  max=36.54ms  p(90)=93.16µs  p(95)=107.37µs p(99.9)=1.03ms  
     http_req_sending...............: avg=26.55µs  min=4.79µs  med=10.12µs  max=132.45ms p(90)=15.42µs  p(95)=18.64µs  p(99.9)=2.71ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=177.43ms min=1.89ms  med=175.46ms max=483.41ms p(90)=336.48ms p(95)=361.93ms p(99.9)=428.79ms
     http_reqs......................: 80355   1287.143677/s
     iteration_duration.............: avg=179.99ms min=4.68ms  med=178.28ms max=483.68ms p(90)=337.28ms p(95)=362.59ms p(99.9)=429.26ms
     iterations.....................: 79355   1271.125462/s
     success_rate...................: 100.00% ✓ 79355       ✗ 0    
     vus............................: 78      min=0         max=493
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

     checks.........................: 100.00% ✓ 105273     ✗ 0    
     data_received..................: 3.2 GB  49 MB/s
     data_sent......................: 43 MB   676 kB/s
     http_req_blocked...............: avg=8.01µs   min=1.01µs  med=2.59µs   max=7.58ms  p(90)=4.3µs    p(95)=5.27µs   p(99.9)=1.21ms  
     http_req_connecting............: avg=4.5µs    min=0s      med=0s       max=7.52ms  p(90)=0s       p(95)=0s       p(99.9)=1.19ms  
     http_req_duration..............: avg=397.49ms min=3.37ms  med=364.92ms max=1.69s   p(90)=781.94ms p(95)=858.83ms p(99.9)=1.31s   
       { expected_response:true }...: avg=397.49ms min=3.37ms  med=364.92ms max=1.69s   p(90)=781.94ms p(95)=858.83ms p(99.9)=1.31s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 36091
     http_req_receiving.............: avg=80.97µs  min=29.09µs med=69.58µs  max=46.35ms p(90)=106.91µs p(95)=120.94µs p(99.9)=934.12µs
     http_req_sending...............: avg=23.62µs  min=5.24µs  med=12.89µs  max=80.9ms  p(90)=19.58µs  p(95)=22.08µs  p(99.9)=1.82ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=397.39ms min=3.32ms  med=364.82ms max=1.69s   p(90)=781.86ms p(95)=858.76ms p(99.9)=1.31s   
     http_reqs......................: 36091   562.927779/s
     iteration_duration.............: avg=409.04ms min=15.45ms med=379.41ms max=1.69s   p(90)=785.73ms p(95)=861.98ms p(99.9)=1.31s   
     iterations.....................: 35091   547.330323/s
     success_rate...................: 100.00% ✓ 35091      ✗ 0    
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

     checks.........................: 100.00% ✓ 51876      ✗ 0    
     data_received..................: 1.6 GB  24 MB/s
     data_sent......................: 22 MB   327 kB/s
     http_req_blocked...............: avg=19.4µs   min=1.09µs  med=3.15µs   max=9.44ms  p(90)=4.9µs    p(95)=6.33µs   p(99.9)=5.63ms
     http_req_connecting............: avg=14.29µs  min=0s      med=0s       max=9.35ms  p(90)=0s       p(95)=0s       p(99.9)=5.59ms
     http_req_duration..............: avg=793.29ms min=5.21ms  med=709.55ms max=4.44s   p(90)=1.62s    p(95)=1.87s    p(99.9)=3.21s 
       { expected_response:true }...: avg=793.29ms min=5.21ms  med=709.55ms max=4.44s   p(90)=1.62s    p(95)=1.87s    p(99.9)=3.21s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 18292
     http_req_receiving.............: avg=95.84µs  min=29.48µs med=87.52µs  max=20.41ms p(90)=125.85µs p(95)=141.86µs p(99.9)=1.22ms
     http_req_sending...............: avg=28.75µs  min=5.45µs  med=16.35µs  max=8.31ms  p(90)=21.55µs  p(95)=24.74µs  p(99.9)=3.12ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=793.16ms min=5.1ms   med=709.43ms max=4.44s   p(90)=1.62s    p(95)=1.87s    p(99.9)=3.21s 
     http_reqs......................: 18292   272.347803/s
     iteration_duration.............: avg=839.21ms min=39.11ms med=774.92ms max=4.44s   p(90)=1.65s    p(95)=1.89s    p(99.9)=3.22s 
     iterations.....................: 17292   257.458901/s
     success_rate...................: 100.00% ✓ 17292      ✗ 0    
     vus............................: 63      min=0        max=498
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

     checks.........................: 100.00% ✓ 46464      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   289 kB/s
     http_req_blocked...............: avg=13.8µs   min=1.13µs  med=3.1µs    max=6.72ms   p(90)=4.74µs   p(95)=6.22µs  p(99.9)=2.1ms 
     http_req_connecting............: avg=9.14µs   min=0s      med=0s       max=6.66ms   p(90)=0s       p(95)=0s      p(99.9)=2.08ms
     http_req_duration..............: avg=880.93ms min=7.53ms  med=804.7ms  max=2.89s    p(90)=1.77s    p(95)=1.91s   p(99.9)=2.58s 
       { expected_response:true }...: avg=880.93ms min=7.53ms  med=804.7ms  max=2.89s    p(90)=1.77s    p(95)=1.91s   p(99.9)=2.58s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16488
     http_req_receiving.............: avg=98.64µs  min=32.73µs med=85µs     max=68.87ms  p(90)=122.81µs p(95)=138µs   p(99.9)=1.07ms
     http_req_sending...............: avg=36.46µs  min=5.06µs  med=15.68µs  max=112.42ms p(90)=20.58µs  p(95)=24.06µs p(99.9)=2.81ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s    
     http_req_waiting...............: avg=880.79ms min=7.45ms  med=804.58ms max=2.89s    p(90)=1.77s    p(95)=1.91s   p(99.9)=2.58s 
     http_reqs......................: 16488   241.104789/s
     iteration_duration.............: avg=937.78ms min=30.04ms med=888.68ms max=2.9s     p(90)=1.79s    p(95)=1.92s   p(99.9)=2.59s 
     iterations.....................: 15488   226.481743/s
     success_rate...................: 100.00% ✓ 15488      ✗ 0    
     vus............................: 77      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

