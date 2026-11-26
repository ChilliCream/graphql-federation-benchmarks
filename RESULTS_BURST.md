## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.21 | 4,934 | 4,944 | 4,929 | 0.1% | 387 MB | 80.4 KB |  |
| fusion-fed-net-11 | 16.7.7 | 4,838 | 4,847 | 4,814 | 0.3% | 415 MB | 87.9 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.21 | 4,790 | 4,806 | 4,685 | 1.0% | 136 MB | 29.0 KB |  |
| fusion-aot-11 | 16.7.7 | 4,773 | 4,778 | 4,763 | 0.1% | 159 MB | 34.1 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 4,764 | 4,766 | 4,757 | 0.1% | 157 MB | 33.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.21 | 4,762 | 4,779 | 4,752 | 0.3% | 374 MB | 80.4 KB |  |
| fusion-net-11 | 16.7.7 | 4,749 | 4,810 | 4,729 | 0.7% | 389 MB | 83.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.21 | 4,635 | 4,779 | 4,619 | 1.4% | 142 MB | 31.5 KB |  |
| feddi-gateway | 2026-11-22-1912 | 4,526 | 4,553 | 4,491 | 0.5% | 2,316 MB | 524.1 KB |  |
| hive-router | v0.3.17 | 4,149 | 4,167 | 4,112 | 0.5% | 194 MB | 47.8 KB |  |
| hive-router-nightly | v0.3.20-nightly.2b115870 | 3,949 | 3,970 | 3,902 | 0.7% | 188 MB | 48.7 KB |  |
| caliban | 3.2.1 | 1,544 | 1,544 | 1,541 | 0.1% | 11,028 MB | 7,313.6 KB |  |
| cosmo | 0.373.0 | 1,307 | 1,309 | 1,306 | 0.1% | 570 MB | 446.5 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 566 | 569 | 558 | 0.7% | 3,032 MB | 5,485.4 KB |  |
| hive-gateway | 2.15.10 | 268 | 270 | 266 | 0.6% | 3,744 MB | 14,307.0 KB |  |
| apollo-gateway | 2.14.4 | 237 | 237 | 236 | 0.2% | 2,441 MB | 10,547.2 KB |  |
| apollo-router | v2.19.1 | — | — | — | — | — | — | non-compatible response (7863 across 5/5 runs) |
| apollo-router-nightly | v3.0.0-preview.0-nightly.36cc3633 | — | — | — | — | — | — | non-compatible response (5662 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (10052 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (165345 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 898692      ✗ 0     
     data_received..................: 26 GB   432 MB/s
     data_sent......................: 361 MB  5.9 MB/s
     http_req_blocked...............: avg=67.39µs  min=811ns    med=2.05µs  max=148.89ms p(90)=3.6µs    p(95)=4.68µs   p(99.9)=24.7ms  
     http_req_connecting............: avg=63.9µs   min=0s       med=0s      max=142.9ms  p(90)=0s       p(95)=0s       p(99.9)=24.35ms 
     http_req_duration..............: avg=45.3ms   min=730.43µs med=38.3ms  max=307.57ms p(90)=94.54ms  p(95)=116.45ms p(99.9)=174.25ms
       { expected_response:true }...: avg=45.3ms   min=730.43µs med=38.3ms  max=307.57ms p(90)=94.54ms  p(95)=116.45ms p(99.9)=174.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 300564
     http_req_receiving.............: avg=349.17µs min=24.86µs  med=51.8µs  max=122.98ms p(90)=202.35µs p(95)=343.39µs p(99.9)=49ms    
     http_req_sending...............: avg=162.59µs min=4.02µs   med=8.44µs  max=212.29ms p(90)=15.96µs  p(95)=109.67µs p(99.9)=29.55ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=44.78ms  min=690.58µs med=37.96ms max=307.37ms p(90)=93.31ms  p(95)=115.17ms p(99.9)=166.87ms
     http_reqs......................: 300564  4934.123193/s
     iteration_duration.............: avg=47.53ms  min=1.21ms   med=39.31ms max=333.23ms p(90)=100.24ms p(95)=124.21ms p(99.9)=199.9ms 
     iterations.....................: 299564  4917.706978/s
     success_rate...................: 100.00% ✓ 299564      ✗ 0     
     vus............................: 53      min=0         max=499 
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

     checks.........................: 100.00% ✓ 881487      ✗ 0     
     data_received..................: 26 GB   423 MB/s
     data_sent......................: 354 MB  5.8 MB/s
     http_req_blocked...............: avg=68.28µs  min=762ns    med=2.06µs  max=145.01ms p(90)=3.71µs   p(95)=4.87µs   p(99.9)=24.5ms  
     http_req_connecting............: avg=64.55µs  min=0s       med=0s      max=139.89ms p(90)=0s       p(95)=0s       p(99.9)=24.17ms 
     http_req_duration..............: avg=46.33ms  min=741.6µs  med=39.12ms max=336.83ms p(90)=97.11ms  p(95)=120.71ms p(99.9)=173.43ms
       { expected_response:true }...: avg=46.33ms  min=741.6µs  med=39.12ms max=336.83ms p(90)=97.11ms  p(95)=120.71ms p(99.9)=173.43ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 294829
     http_req_receiving.............: avg=332.89µs min=25.61µs  med=52.15µs max=193.53ms p(90)=203.51µs p(95)=351.22µs p(99.9)=44.01ms 
     http_req_sending...............: avg=159.02µs min=3.97µs   med=8.5µs   max=212.62ms p(90)=16.37µs  p(95)=113µs    p(99.9)=28.48ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=45.84ms  min=707.18µs med=38.79ms max=322.76ms p(90)=95.82ms  p(95)=119.37ms p(99.9)=169.15ms
     http_reqs......................: 294829  4838.712499/s
     iteration_duration.............: avg=48.48ms  min=1.25ms   med=40.21ms max=352.67ms p(90)=102.68ms p(95)=128.72ms p(99.9)=208.11ms
     iterations.....................: 293829  4822.300571/s
     success_rate...................: 100.00% ✓ 293829      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 873069      ✗ 0     
     data_received..................: 26 GB   419 MB/s
     data_sent......................: 351 MB  5.8 MB/s
     http_req_blocked...............: avg=65.4µs   min=772ns    med=2.05µs  max=140.25ms p(90)=3.59µs   p(95)=4.68µs   p(99.9)=23.89ms 
     http_req_connecting............: avg=62.12µs  min=0s       med=0s      max=140.2ms  p(90)=0s       p(95)=0s       p(99.9)=23.75ms 
     http_req_duration..............: avg=47.2ms   min=771.3µs  med=39.82ms max=319.54ms p(90)=100.12ms p(95)=124.24ms p(99.9)=176.78ms
       { expected_response:true }...: avg=47.2ms   min=771.3µs  med=39.82ms max=319.54ms p(90)=100.12ms p(95)=124.24ms p(99.9)=176.78ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 292023
     http_req_receiving.............: avg=318.8µs  min=23.11µs  med=51.61µs max=115.87ms p(90)=205.02µs p(95)=359.11µs p(99.9)=44.23ms 
     http_req_sending...............: avg=146.94µs min=4.23µs   med=8.57µs  max=112.65ms p(90)=16.11µs  p(95)=114.18µs p(99.9)=26.75ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.74ms  min=734.97µs med=39.5ms  max=314.01ms p(90)=99ms     p(95)=123.07ms p(99.9)=173.52ms
     http_reqs......................: 292023  4790.713419/s
     iteration_duration.............: avg=48.94ms  min=1.35ms   med=40.68ms max=358.75ms p(90)=103.68ms p(95)=129.78ms p(99.9)=202.01ms
     iterations.....................: 291023  4774.308158/s
     success_rate...................: 100.00% ✓ 291023      ✗ 0     
     vus............................: 55      min=0         max=499 
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

     checks.........................: 100.00% ✓ 869760      ✗ 0     
     data_received..................: 26 GB   418 MB/s
     data_sent......................: 350 MB  5.7 MB/s
     http_req_blocked...............: avg=57.7µs   min=782ns    med=1.99µs  max=144.74ms p(90)=3.51µs   p(95)=4.58µs   p(99.9)=19.81ms 
     http_req_connecting............: avg=54.12µs  min=0s       med=0s      max=115.93ms p(90)=0s       p(95)=0s       p(99.9)=19.48ms 
     http_req_duration..............: avg=47.61ms  min=771.56µs med=40.14ms max=320.37ms p(90)=101.96ms p(95)=126.19ms p(99.9)=179.07ms
       { expected_response:true }...: avg=47.61ms  min=771.56µs med=40.14ms max=320.37ms p(90)=101.96ms p(95)=126.19ms p(99.9)=179.07ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 290920
     http_req_receiving.............: avg=313.36µs min=21.87µs  med=51.04µs max=115.84ms p(90)=208.95µs p(95)=368.98µs p(99.9)=43.69ms 
     http_req_sending...............: avg=135.97µs min=4.05µs   med=8.38µs  max=182.13ms p(90)=15.85µs  p(95)=116.66µs p(99.9)=24.59ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.16ms  min=722.22µs med=39.85ms max=311.83ms p(90)=100.97ms p(95)=125.15ms p(99.9)=173.99ms
     http_reqs......................: 290920  4773.54453/s
     iteration_duration.............: avg=49.13ms  min=1.31ms   med=40.82ms max=330.61ms p(90)=105.42ms p(95)=130.66ms p(99.9)=208.29ms
     iterations.....................: 289920  4757.136086/s
     success_rate...................: 100.00% ✓ 289920      ✗ 0     
     vus............................: 55      min=0         max=499 
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

     checks.........................: 100.00% ✓ 868362      ✗ 0     
     data_received..................: 25 GB   417 MB/s
     data_sent......................: 349 MB  5.7 MB/s
     http_req_blocked...............: avg=58.66µs  min=782ns    med=2.06µs  max=137.19ms p(90)=3.65µs   p(95)=4.74µs   p(99.9)=20.65ms 
     http_req_connecting............: avg=55.4µs   min=0s       med=0s      max=122.78ms p(90)=0s       p(95)=0s       p(99.9)=20.56ms 
     http_req_duration..............: avg=47.66ms  min=762.56µs med=40.01ms max=315.58ms p(90)=101.82ms p(95)=126.65ms p(99.9)=180.96ms
       { expected_response:true }...: avg=47.66ms  min=762.56µs med=40.01ms max=315.58ms p(90)=101.82ms p(95)=126.65ms p(99.9)=180.96ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 290454
     http_req_receiving.............: avg=360.56µs min=22.81µs  med=50.62µs max=101.73ms p(90)=212.59µs p(95)=371.23µs p(99.9)=49.22ms 
     http_req_sending...............: avg=132.83µs min=3.97µs   med=8.46µs  max=194.21ms p(90)=16.25µs  p(95)=116.98µs p(99.9)=22.93ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.17ms  min=724.03µs med=39.71ms max=315.23ms p(90)=100.7ms  p(95)=125.2ms  p(99.9)=174.78ms
     http_reqs......................: 290454  4764.968103/s
     iteration_duration.............: avg=49.21ms  min=1.34ms   med=40.78ms max=335.18ms p(90)=105.14ms p(95)=131.55ms p(99.9)=210.2ms 
     iterations.....................: 289454  4748.562861/s
     success_rate...................: 100.00% ✓ 289454      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 867300      ✗ 0     
     data_received..................: 25 GB   417 MB/s
     data_sent......................: 349 MB  5.7 MB/s
     http_req_blocked...............: avg=76.52µs  min=941ns    med=2.61µs  max=155.47ms p(90)=4.11µs   p(95)=5.27µs   p(99.9)=30.36ms 
     http_req_connecting............: avg=72.39µs  min=0s       med=0s      max=155.39ms p(90)=0s       p(95)=0s       p(99.9)=29.54ms 
     http_req_duration..............: avg=46.78ms  min=737.39µs med=39.95ms max=295.01ms p(90)=96.83ms  p(95)=120.53ms p(99.9)=179.62ms
       { expected_response:true }...: avg=46.78ms  min=737.39µs med=39.95ms max=295.01ms p(90)=96.83ms  p(95)=120.53ms p(99.9)=179.62ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 290100
     http_req_receiving.............: avg=372.89µs min=23.06µs  med=54.89µs max=133.85ms p(90)=208.44µs p(95)=361.02µs p(99.9)=51.31ms 
     http_req_sending...............: avg=176.32µs min=3.88µs   med=9.12µs  max=209.7ms  p(90)=17.18µs  p(95)=117.42µs p(99.9)=32.13ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.23ms  min=692.21µs med=39.57ms max=293.4ms  p(90)=95.46ms  p(95)=119.07ms p(99.9)=175.16ms
     http_reqs......................: 290100  4762.688556/s
     iteration_duration.............: avg=49.26ms  min=1.12ms   med=41ms    max=346.51ms p(90)=104.24ms p(95)=129.79ms p(99.9)=209.13ms
     iterations.....................: 289100  4746.271153/s
     success_rate...................: 100.00% ✓ 289100      ✗ 0     
     vus............................: 53      min=0         max=499 
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

     checks.........................: 100.00% ✓ 864903      ✗ 0     
     data_received..................: 25 GB   416 MB/s
     data_sent......................: 348 MB  5.7 MB/s
     http_req_blocked...............: avg=71.1µs   min=891ns    med=2.56µs  max=165.69ms p(90)=4.07µs   p(95)=5.21µs   p(99.9)=26.59ms 
     http_req_connecting............: avg=66.89µs  min=0s       med=0s      max=165.62ms p(90)=0s       p(95)=0s       p(99.9)=26.19ms 
     http_req_duration..............: avg=47.35ms  min=737.36µs med=39.85ms max=314.38ms p(90)=99.62ms  p(95)=124.8ms  p(99.9)=181.87ms
       { expected_response:true }...: avg=47.35ms  min=737.36µs med=39.85ms max=314.38ms p(90)=99.62ms  p(95)=124.8ms  p(99.9)=181.87ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 289301
     http_req_receiving.............: avg=346.89µs min=26.26µs  med=53.02µs max=171.93ms p(90)=215.25µs p(95)=368.38µs p(99.9)=48.38ms 
     http_req_sending...............: avg=157.05µs min=3.9µs    med=9.09µs  max=126.81ms p(90)=17.19µs  p(95)=120.11µs p(99.9)=28.15ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.84ms  min=697.92µs med=39.52ms max=313.88ms p(90)=98.41ms  p(95)=123.49ms p(99.9)=177.89ms
     http_reqs......................: 289301  4749.765506/s
     iteration_duration.............: avg=49.41ms  min=1.14ms   med=40.61ms max=334.04ms p(90)=104.76ms p(95)=132.48ms p(99.9)=217.43ms
     iterations.....................: 288301  4733.347431/s
     success_rate...................: 100.00% ✓ 288301      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 845127      ✗ 0     
     data_received..................: 25 GB   406 MB/s
     data_sent......................: 340 MB  5.6 MB/s
     http_req_blocked...............: avg=70.32µs  min=922ns    med=2.6µs   max=174.51ms p(90)=4.14µs   p(95)=5.29µs   p(99.9)=26.15ms 
     http_req_connecting............: avg=65.66µs  min=0s       med=0s      max=146.4ms  p(90)=0s       p(95)=0s       p(99.9)=25.52ms 
     http_req_duration..............: avg=48.33ms  min=799.28µs med=39.89ms max=273.69ms p(90)=103.02ms p(95)=129.4ms  p(99.9)=193.8ms 
       { expected_response:true }...: avg=48.33ms  min=799.28µs med=39.89ms max=273.69ms p(90)=103.02ms p(95)=129.4ms  p(99.9)=193.8ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 282709
     http_req_receiving.............: avg=392.64µs min=22.35µs  med=52.93µs max=175.53ms p(90)=221.03µs p(95)=384.63µs p(99.9)=59.66ms 
     http_req_sending...............: avg=156.96µs min=4.14µs   med=9.13µs  max=182.52ms p(90)=17.88µs  p(95)=123.99µs p(99.9)=27.65ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.78ms  min=750.91µs med=39.54ms max=272.8ms  p(90)=101.79ms p(95)=128ms    p(99.9)=184.21ms
     http_reqs......................: 282709  4635.092685/s
     iteration_duration.............: avg=50.56ms  min=1.25ms   med=41.17ms max=341.13ms p(90)=108.35ms p(95)=135.94ms p(99.9)=224.24ms
     iterations.....................: 281709  4618.697406/s
     success_rate...................: 100.00% ✓ 281709      ✗ 0     
     vus............................: 56      min=0         max=498 
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

     checks.........................: 100.00% ✓ 825048      ✗ 0     
     data_received..................: 24 GB   396 MB/s
     data_sent......................: 332 MB  5.4 MB/s
     http_req_blocked...............: avg=78.89µs  min=842ns    med=2.68µs  max=162.57ms p(90)=4.41µs   p(95)=5.6µs    p(99.9)=32.3ms  
     http_req_connecting............: avg=74.35µs  min=0s       med=0s      max=146.68ms p(90)=0s       p(95)=0s       p(99.9)=30.29ms 
     http_req_duration..............: avg=49.32ms  min=750.33µs med=41.52ms max=293.48ms p(90)=104ms    p(95)=128.52ms p(99.9)=195.71ms
       { expected_response:true }...: avg=49.32ms  min=750.33µs med=41.52ms max=293.48ms p(90)=104ms    p(95)=128.52ms p(99.9)=195.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 276016
     http_req_receiving.............: avg=362.48µs min=25.8µs   med=55µs    max=156.99ms p(90)=212.32µs p(95)=379.81µs p(99.9)=50.39ms 
     http_req_sending...............: avg=168.35µs min=3.97µs   med=9.73µs  max=114.76ms p(90)=18.37µs  p(95)=123.82µs p(99.9)=30.35ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.79ms  min=710.35µs med=41.17ms max=275.44ms p(90)=102.83ms p(95)=127.13ms p(99.9)=189.96ms
     http_reqs......................: 276016  4526.81846/s
     iteration_duration.............: avg=51.79ms  min=1.22ms   med=42.66ms max=400.87ms p(90)=110.36ms p(95)=137.32ms p(99.9)=219.23ms
     iterations.....................: 275016  4510.417895/s
     success_rate...................: 100.00% ✓ 275016      ✗ 0     
     vus............................: 56      min=0         max=498 
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

     checks.........................: 100.00% ✓ 757218      ✗ 0     
     data_received..................: 22 GB   363 MB/s
     data_sent......................: 304 MB  5.0 MB/s
     http_req_blocked...............: avg=49.84µs  min=801ns    med=2.28µs  max=144.62ms p(90)=4.1µs    p(95)=5.41µs   p(99.9)=11.75ms 
     http_req_connecting............: avg=46.21µs  min=0s       med=0s      max=119.28ms p(90)=0s       p(95)=0s       p(99.9)=11.08ms 
     http_req_duration..............: avg=55.09ms  min=871.51µs med=47.02ms max=306.19ms p(90)=117.33ms p(95)=146.41ms p(99.9)=205.83ms
       { expected_response:true }...: avg=55.09ms  min=871.51µs med=47.02ms max=306.19ms p(90)=117.33ms p(95)=146.41ms p(99.9)=205.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 253406
     http_req_receiving.............: avg=258.34µs min=24.7µs   med=53.22µs max=137.63ms p(90)=212.97µs p(95)=380.98µs p(99.9)=36.51ms 
     http_req_sending...............: avg=124.15µs min=4.22µs   med=9.29µs  max=126.08ms p(90)=18.83µs  p(95)=126.31µs p(99.9)=22.16ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=54.71ms  min=821.4µs  med=46.76ms max=306.01ms p(90)=116.48ms p(95)=145.49ms p(99.9)=202.54ms
     http_reqs......................: 253406  4149.210334/s
     iteration_duration.............: avg=56.44ms  min=1.49ms   med=47.97ms max=325.32ms p(90)=120.38ms p(95)=150.04ms p(99.9)=222.46ms
     iterations.....................: 252406  4132.836569/s
     success_rate...................: 100.00% ✓ 252406      ✗ 0     
     vus............................: 60      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.20-nightly.2b115870)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 721254      ✗ 0     
     data_received..................: 21 GB   346 MB/s
     data_sent......................: 290 MB  4.7 MB/s
     http_req_blocked...............: avg=39.43µs  min=781ns    med=2.16µs  max=95.2ms   p(90)=3.83µs   p(95)=5.06µs   p(99.9)=5.86ms  
     http_req_connecting............: avg=35.66µs  min=0s       med=0s      max=93.09ms  p(90)=0s       p(95)=0s       p(99.9)=3.88ms  
     http_req_duration..............: avg=58.21ms  min=880.77µs med=49.38ms max=294.22ms p(90)=120.36ms p(95)=147.52ms p(99.9)=208.9ms 
       { expected_response:true }...: avg=58.21ms  min=880.77µs med=49.38ms max=294.22ms p(90)=120.36ms p(95)=147.52ms p(99.9)=208.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 241418
     http_req_receiving.............: avg=275.13µs min=25.96µs  med=52.97µs max=114.86ms p(90)=215.06µs p(95)=376.61µs p(99.9)=42.04ms 
     http_req_sending...............: avg=110.15µs min=4.18µs   med=9.04µs  max=133.31ms p(90)=17.6µs   p(95)=125.11µs p(99.9)=20.52ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=57.82ms  min=832.73µs med=49.1ms  max=294.11ms p(90)=119.72ms p(95)=146.56ms p(99.9)=200.72ms
     http_reqs......................: 241418  3949.970633/s
     iteration_duration.............: avg=59.27ms  min=1.42ms   med=50.29ms max=323.35ms p(90)=122.23ms p(95)=149.8ms  p(99.9)=222.61ms
     iterations.....................: 240418  3933.609092/s
     success_rate...................: 100.00% ✓ 240418      ✗ 0     
     vus............................: 62      min=0         max=497 
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

     checks.........................: 100.00% ✓ 285690      ✗ 0    
     data_received..................: 8.4 GB  135 MB/s
     data_sent......................: 116 MB  1.9 MB/s
     http_req_blocked...............: avg=6.28µs   min=892ns   med=2.58µs   max=17.21ms  p(90)=4.59µs   p(95)=5.71µs   p(99.9)=492.55µs
     http_req_connecting............: avg=3.01µs   min=0s      med=0s       max=16.95ms  p(90)=0s       p(95)=0s       p(99.9)=416.59µs
     http_req_duration..............: avg=148.13ms min=1.89ms  med=124.16ms max=1.15s    p(90)=305.33ms p(95)=377.76ms p(99.9)=705.99ms
       { expected_response:true }...: avg=148.13ms min=1.89ms  med=124.16ms max=1.15s    p(90)=305.33ms p(95)=377.76ms p(99.9)=705.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 96230
     http_req_receiving.............: avg=79.26µs  min=25.42µs med=60.04µs  max=14.72ms  p(90)=103.03µs p(95)=125.54µs p(99.9)=2.23ms  
     http_req_sending...............: avg=35.91µs  min=4.9µs   med=12.07µs  max=145.86ms p(90)=20.31µs  p(95)=24.87µs  p(99.9)=4.3ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=148.02ms min=1.83ms  med=124.04ms max=1.15s    p(90)=305.26ms p(95)=377.58ms p(99.9)=705.87ms
     http_reqs......................: 96230   1544.970718/s
     iteration_duration.............: avg=149.95ms min=5.81ms  med=126.07ms max=1.15s    p(90)=306.72ms p(95)=379.04ms p(99.9)=707.63ms
     iterations.....................: 95230   1528.915738/s
     success_rate...................: 100.00% ✓ 95230       ✗ 0    
     vus............................: 70      min=0         max=495
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

     checks.........................: 100.00% ✓ 241866      ✗ 0    
     data_received..................: 7.1 GB  114 MB/s
     data_sent......................: 98 MB   1.6 MB/s
     http_req_blocked...............: avg=5.08µs   min=942ns   med=2.09µs   max=17.49ms  p(90)=3.58µs   p(95)=4.43µs   p(99.9)=369.82µs
     http_req_connecting............: avg=2.4µs    min=0s      med=0s       max=17.42ms  p(90)=0s       p(95)=0s       p(99.9)=318.84µs
     http_req_duration..............: avg=174.78ms min=2ms     med=172.66ms max=465.62ms p(90)=332.73ms p(95)=357.19ms p(99.9)=427.02ms
       { expected_response:true }...: avg=174.78ms min=2ms     med=172.66ms max=465.62ms p(90)=332.73ms p(95)=357.19ms p(99.9)=427.02ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 81622
     http_req_receiving.............: avg=70.22µs  min=25.19µs med=56.61µs  max=59.16ms  p(90)=92.53µs  p(95)=107.67µs p(99.9)=1.03ms  
     http_req_sending...............: avg=30µs     min=4.77µs  med=10.05µs  max=148.58ms p(90)=16.1µs   p(95)=19.43µs  p(99.9)=3.23ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=174.68ms min=1.9ms   med=172.57ms max=465.54ms p(90)=332.63ms p(95)=357.09ms p(99.9)=426.86ms
     http_reqs......................: 81622   1307.323294/s
     iteration_duration.............: avg=177.17ms min=5.26ms  med=175.46ms max=465.76ms p(90)=333.45ms p(95)=357.9ms  p(99.9)=427.29ms
     iterations.....................: 80622   1291.306493/s
     success_rate...................: 100.00% ✓ 80622       ✗ 0    
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

     checks.........................: 100.00% ✓ 105945     ✗ 0    
     data_received..................: 3.2 GB  50 MB/s
     data_sent......................: 44 MB   680 kB/s
     http_req_blocked...............: avg=8.77µs   min=1.22µs  med=3.06µs   max=11.91ms  p(90)=4.79µs   p(95)=5.85µs   p(99.9)=1.26ms  
     http_req_connecting............: avg=4.71µs   min=0s      med=0s       max=11.85ms  p(90)=0s       p(95)=0s       p(99.9)=1.24ms  
     http_req_duration..............: avg=394.8ms  min=3.37ms  med=364.47ms max=1.52s    p(90)=780.35ms p(95)=846.94ms p(99.9)=1.29s   
       { expected_response:true }...: avg=394.8ms  min=3.37ms  med=364.47ms max=1.52s    p(90)=780.35ms p(95)=846.94ms p(99.9)=1.29s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 36315
     http_req_receiving.............: avg=82.11µs  min=29.22µs med=70.65µs  max=54.24ms  p(90)=108.31µs p(95)=122.94µs p(99.9)=903.85µs
     http_req_sending...............: avg=28.93µs  min=5.42µs  med=14.17µs  max=135.85ms p(90)=20.92µs  p(95)=23.7µs   p(99.9)=3.03ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=394.69ms min=3.31ms  med=364.34ms max=1.52s    p(90)=780.25ms p(95)=846.82ms p(99.9)=1.29s   
     http_reqs......................: 36315   566.577163/s
     iteration_duration.............: avg=406.21ms min=22.14ms med=379.73ms max=1.52s    p(90)=783.97ms p(95)=849.53ms p(99.9)=1.29s   
     iterations.....................: 35315   550.975424/s
     success_rate...................: 100.00% ✓ 35315      ✗ 0    
     vus............................: 61      min=0        max=497
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

     checks.........................: 100.00% ✓ 50931      ✗ 0    
     data_received..................: 1.6 GB  24 MB/s
     data_sent......................: 22 MB   322 kB/s
     http_req_blocked...............: avg=10.84µs  min=1.19µs  med=3.54µs   max=11.93ms p(90)=5.36µs   p(95)=6.85µs p(99.9)=887.81µs
     http_req_connecting............: avg=5.73µs   min=0s      med=0s       max=11.86ms p(90)=0s       p(95)=0s     p(99.9)=848.54µs
     http_req_duration..............: avg=806.78ms min=5.1ms   med=723.11ms max=3.91s   p(90)=1.61s    p(95)=1.91s  p(99.9)=3.15s   
       { expected_response:true }...: avg=806.78ms min=5.1ms   med=723.11ms max=3.91s   p(90)=1.61s    p(95)=1.91s  p(99.9)=3.15s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 17977
     http_req_receiving.............: avg=98.22µs  min=30.48µs med=87.54µs  max=65.26ms p(90)=124.81µs p(95)=141µs  p(99.9)=1.06ms  
     http_req_sending...............: avg=29.59µs  min=5.99µs  med=17.36µs  max=41.47ms p(90)=22.88µs  p(95)=26µs   p(99.9)=2.55ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s     p(99.9)=0s      
     http_req_waiting...............: avg=806.65ms min=4.99ms  med=722.99ms max=3.91s   p(90)=1.61s    p(95)=1.91s  p(99.9)=3.15s   
     http_reqs......................: 17977   268.546189/s
     iteration_duration.............: avg=854.37ms min=36.25ms med=782.83ms max=3.92s   p(90)=1.64s    p(95)=1.92s  p(99.9)=3.19s   
     iterations.....................: 16977   253.607869/s
     success_rate...................: 100.00% ✓ 16977      ✗ 0    
     vus............................: 42      min=0        max=500
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

     checks.........................: 100.00% ✓ 45711      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   285 kB/s
     http_req_blocked...............: avg=13.46µs  min=1.21µs  med=3.31µs   max=4.54ms   p(90)=5.02µs   p(95)=6.81µs   p(99.9)=1.9ms 
     http_req_connecting............: avg=8.12µs   min=0s      med=0s       max=3.96ms   p(90)=0s       p(95)=0s       p(99.9)=1.86ms
     http_req_duration..............: avg=894.16ms min=7.46ms  med=813.98ms max=3s       p(90)=1.81s    p(95)=1.95s    p(99.9)=2.61s 
       { expected_response:true }...: avg=894.16ms min=7.46ms  med=813.98ms max=3s       p(90)=1.81s    p(95)=1.95s    p(99.9)=2.61s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16237
     http_req_receiving.............: avg=95.3µs   min=32.6µs  med=85.13µs  max=36.1ms   p(90)=123.94µs p(95)=139.82µs p(99.9)=1.19ms
     http_req_sending...............: avg=44.18µs  min=5.4µs   med=16.29µs  max=161.62ms p(90)=21.71µs  p(95)=25.41µs  p(99.9)=4.25ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=894.02ms min=7.38ms  med=813.91ms max=3s       p(90)=1.81s    p(95)=1.95s    p(99.9)=2.61s 
     http_reqs......................: 16237   237.183005/s
     iteration_duration.............: avg=952.86ms min=23.32ms med=882.66ms max=3.01s    p(90)=1.83s    p(95)=1.97s    p(99.9)=2.63s 
     iterations.....................: 15237   222.575441/s
     success_rate...................: 100.00% ✓ 15237      ✗ 0    
     vus............................: 79      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

