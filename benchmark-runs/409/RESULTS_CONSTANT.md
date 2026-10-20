## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s**.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| feddi-gateway | 3c75a7db8876 | 3,107 | 3,293 | 3,068 | 2.3% |  |
| fusion-nightly-net11 | 16.7.0-p.30 | 3,015 | 3,186 | 2,997 | 2.1% |  |
| fusion-nightly | 16.7.0-p.30 | 2,839 | 3,022 | 2,826 | 2.3% |  |
| fusion-nightly-fed | 16.7.0-p.30 | 2,591 | 2,728 | 2,577 | 2.0% |  |
| hive-router | v0.3.5 | 2,566 | 2,747 | 2,508 | 3.0% |  |
| fusion | 16.6.9 | 2,398 | 2,523 | 2,385 | 2.0% |  |
| grafbase | 0.53.5 | 1,651 | 1,712 | 1,648 | 1.4% |  |
| cosmo | 0.359.0 | 1,435 | 1,484 | 1,425 | 1.3% |  |
| caliban | 3.2.0 | 1,280 | 1,341 | 1,274 | 2.0% |  |
| hive-gateway-router-runtime | 2.15.2 | 522 | 541 | 521 | 1.3% |  |
| apollo-router | v2.18.0 | 408 | 430 | 406 | 2.3% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 379 | 398 | 376 | 2.0% |  |
| apollo-gateway | 2.14.4 | 264 | 269 | 264 | 0.7% |  |
| hive-gateway | 2.15.2 | 249 | 257 | 248 | 1.2% |  |


### Details

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1119651     ✗ 0     
     data_received..................: 33 GB   272 MB/s
     data_sent......................: 449 MB  3.7 MB/s
     http_req_blocked...............: avg=3.53µs   min=821ns    med=2.21µs  max=22.7ms   p(90)=3.92µs  p(95)=4.81µs   p(99.9)=35.87µs
     http_req_connecting............: avg=651ns    min=0s       med=0s      max=7.87ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=15.85ms  min=968.01µs med=15.26ms max=321.72ms p(90)=23.54ms p(95)=27.06ms  p(99.9)=48.36ms
       { expected_response:true }...: avg=15.85ms  min=968.01µs med=15.26ms max=321.72ms p(90)=23.54ms p(95)=27.06ms  p(99.9)=48.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 373317
     http_req_receiving.............: avg=102.69µs min=25.04µs  med=47.72µs max=28.82ms  p(90)=95.04µs p(95)=197.26µs p(99.9)=8.64ms 
     http_req_sending...............: avg=57.83µs  min=4.7µs    med=9.22µs  max=298.69ms p(90)=17.11µs p(95)=108.51µs p(99.9)=10.58ms
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=15.69ms  min=920.83µs med=15.14ms max=310.98ms p(90)=23.34ms p(95)=26.73ms  p(99.9)=47.14ms
     http_reqs......................: 373317  3107.457046/s
     iteration_duration.............: avg=16.06ms  min=1.48ms   med=15.46ms max=324.86ms p(90)=23.75ms p(95)=27.31ms  p(99.9)=49.25ms
     iterations.....................: 373217  3106.624655/s
     success_rate...................: 100.00% ✓ 373217      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net11 (HotChocolate subgraphs) (16.7.0-p.30)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1086666     ✗ 0     
     data_received..................: 32 GB   264 MB/s
     data_sent......................: 435 MB  3.6 MB/s
     http_req_blocked...............: avg=2.71µs  min=821ns   med=1.92µs  max=17.48ms  p(90)=3.31µs  p(95)=4.09µs  p(99.9)=29.96µs
     http_req_connecting............: avg=241ns   min=0s      med=0s      max=3.61ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=16.33ms min=1.29ms  med=15.12ms max=294.67ms p(90)=24.2ms  p(95)=28.3ms  p(99.9)=51.66ms
       { expected_response:true }...: avg=16.33ms min=1.29ms  med=15.12ms max=294.67ms p(90)=24.2ms  p(95)=28.3ms  p(99.9)=51.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 362322
     http_req_receiving.............: avg=1.03ms  min=49.36µs med=88.2µs  max=125.85ms p(90)=3.11ms  p(95)=4.76ms  p(99.9)=27.36ms
     http_req_sending...............: avg=55.05µs min=4.43µs  med=8.06µs  max=134.39ms p(90)=16.38µs p(95)=93.51µs p(99.9)=10.07ms
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=15.24ms min=1.17ms  med=14.08ms max=294.16ms p(90)=22.65ms p(95)=26.63ms p(99.9)=48.66ms
     http_reqs......................: 362322  3015.049426/s
     iteration_duration.............: avg=16.55ms min=2.17ms  med=15.32ms max=309.83ms p(90)=24.41ms p(95)=28.55ms p(99.9)=52.4ms 
     iterations.....................: 362222  3014.217279/s
     success_rate...................: 100.00% ✓ 362222      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly (HotChocolate subgraphs) (16.7.0-p.30)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1023393     ✗ 0     
     data_received..................: 30 GB   249 MB/s
     data_sent......................: 410 MB  3.4 MB/s
     http_req_blocked...............: avg=2.87µs   min=851ns   med=1.96µs  max=15.77ms  p(90)=3.35µs  p(95)=4.05µs  p(99.9)=31.61µs
     http_req_connecting............: avg=256ns    min=0s      med=0s      max=3.58ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=17.36ms  min=1.38ms  med=15.26ms max=270.05ms p(90)=28.05ms p(95)=33.59ms p(99.9)=80.03ms
       { expected_response:true }...: avg=17.36ms  min=1.38ms  med=15.26ms max=270.05ms p(90)=28.05ms p(95)=33.59ms p(99.9)=80.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 341231
     http_req_receiving.............: avg=672.84µs min=49.67µs med=87.82µs max=144.71ms p(90)=1.57ms  p(95)=2.91ms  p(99.9)=26.21ms
     http_req_sending...............: avg=49.2µs   min=4.65µs  med=8.26µs  max=123.5ms  p(90)=16.79µs p(95)=92.6µs  p(99.9)=6.53ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=16.64ms  min=1.29ms  med=14.6ms  max=269.42ms p(90)=27.03ms p(95)=32.38ms p(99.9)=78.53ms
     http_reqs......................: 341231  2839.095121/s
     iteration_duration.............: avg=17.57ms  min=2.24ms  med=15.46ms max=294.15ms p(90)=28.28ms p(95)=33.84ms p(99.9)=80.67ms
     iterations.....................: 341131  2838.263105/s
     success_rate...................: 100.00% ✓ 341131      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed (HotChocolate subgraphs) (16.7.0-p.30)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 934509      ✗ 0     
     data_received..................: 27 GB   227 MB/s
     data_sent......................: 374 MB  3.1 MB/s
     http_req_blocked...............: avg=3.23µs   min=802ns   med=2.18µs  max=22.18ms  p(90)=4.15µs  p(95)=5.06µs  p(99.9)=34.1µs 
     http_req_connecting............: avg=328ns    min=0s      med=0s      max=3.67ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=19.02ms  min=1.7ms   med=17.23ms max=296.89ms p(90)=29.45ms p(95)=34.83ms p(99.9)=83.74ms
       { expected_response:true }...: avg=19.02ms  min=1.7ms   med=17.23ms max=296.89ms p(90)=29.45ms p(95)=34.83ms p(99.9)=83.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 311603
     http_req_receiving.............: avg=624.92µs min=50.92µs med=94.96µs max=162.23ms p(90)=1.45ms  p(95)=2.59ms  p(99.9)=24.47ms
     http_req_sending...............: avg=47.83µs  min=4.32µs  med=9.07µs  max=116.59ms p(90)=19.96µs p(95)=99.77µs p(99.9)=4.75ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=18.35ms  min=1.59ms  med=16.62ms max=287.32ms p(90)=28.47ms p(95)=33.74ms p(99.9)=82.53ms
     http_reqs......................: 311603  2591.939061/s
     iteration_duration.............: avg=19.25ms  min=2.85ms  med=17.44ms max=308.01ms p(90)=29.67ms p(95)=35.09ms p(99.9)=84.59ms
     iterations.....................: 311503  2591.107253/s
     success_rate...................: 100.00% ✓ 311503      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 925404      ✗ 0     
     data_received..................: 27 GB   225 MB/s
     data_sent......................: 371 MB  3.1 MB/s
     http_req_blocked...............: avg=3.92µs  min=1.02µs  med=2.65µs  max=9.83ms   p(90)=4.29µs  p(95)=5.08µs   p(99.9)=40.64µs
     http_req_connecting............: avg=784ns   min=0s      med=0s      max=7.98ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=19.21ms min=1.58ms  med=18.9ms  max=283.78ms p(90)=26.69ms p(95)=29.23ms  p(99.9)=48.98ms
       { expected_response:true }...: avg=19.21ms min=1.58ms  med=18.9ms  max=283.78ms p(90)=26.69ms p(95)=29.23ms  p(99.9)=48.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 308568
     http_req_receiving.............: avg=94.96µs min=26.86µs med=54.36µs max=163.81ms p(90)=97.29µs p(95)=152.13µs p(99.9)=6.88ms 
     http_req_sending...............: avg=46.81µs min=4.79µs  med=10.55µs max=234.73ms p(90)=18.64µs p(95)=99.9µs   p(99.9)=3.62ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=19.07ms min=1.53ms  med=18.77ms max=280.47ms p(90)=26.53ms p(95)=29.02ms  p(99.9)=48.2ms 
     http_reqs......................: 308568  2566.852541/s
     iteration_duration.............: avg=19.44ms min=3.15ms  med=19.11ms max=308.13ms p(90)=26.9ms  p(95)=29.46ms  p(99.9)=49.74ms
     iterations.....................: 308468  2566.020682/s
     success_rate...................: 100.00% ✓ 308468      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 864714      ✗ 0     
     data_received..................: 25 GB   210 MB/s
     data_sent......................: 347 MB  2.9 MB/s
     http_req_blocked...............: avg=2.95µs   min=891ns   med=2.05µs  max=18.55ms  p(90)=3.48µs  p(95)=4.18µs  p(99.9)=29.99µs 
     http_req_connecting............: avg=321ns    min=0s      med=0s      max=3.94ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=20.59ms  min=1.59ms  med=17.18ms max=353.53ms p(90)=33.9ms  p(95)=41.59ms p(99.9)=151.22ms
       { expected_response:true }...: avg=20.59ms  min=1.59ms  med=17.18ms max=353.53ms p(90)=33.9ms  p(95)=41.59ms p(99.9)=151.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288338
     http_req_receiving.............: avg=608.45µs min=51.41µs med=95.74µs max=199.5ms  p(90)=1.14ms  p(95)=1.99ms  p(99.9)=27.05ms 
     http_req_sending...............: avg=42.34µs  min=4.72µs  med=8.57µs  max=146.75ms p(90)=16.14µs p(95)=75.83µs p(99.9)=3.6ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=19.94ms  min=1.5ms   med=16.62ms max=353.4ms  p(90)=32.82ms p(95)=40.38ms p(99.9)=149.68ms
     http_reqs......................: 288338  2398.525589/s
     iteration_duration.............: avg=20.8ms   min=2.27ms  med=17.38ms max=353.75ms p(90)=34.14ms p(95)=41.81ms p(99.9)=152.21ms
     iterations.....................: 288238  2397.693744/s
     success_rate...................: 100.00% ✓ 288238      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: grafbase (HotChocolate subgraphs) (0.53.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 595818      ✗ 0     
     data_received..................: 17 GB   145 MB/s
     data_sent......................: 239 MB  2.0 MB/s
     http_req_blocked...............: avg=3.32µs  min=841ns   med=2.21µs  max=6.94ms   p(90)=4.53µs   p(95)=5.66µs   p(99.9)=41.87µs
     http_req_connecting............: avg=482ns   min=0s      med=0s      max=3.97ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=29.95ms min=2.28ms  med=29.42ms max=292.38ms p(90)=39.55ms  p(95)=42.88ms  p(99.9)=65.63ms
       { expected_response:true }...: avg=29.95ms min=2.28ms  med=29.42ms max=292.38ms p(90)=39.55ms  p(95)=42.88ms  p(99.9)=65.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 198706
     http_req_receiving.............: avg=97.72µs min=27.81µs med=55.04µs max=153.81ms p(90)=125.77µs p(95)=205.84µs p(99.9)=3.87ms 
     http_req_sending...............: avg=43.06µs min=4.47µs  med=9.21µs  max=118.38ms p(90)=23.58µs  p(95)=110.12µs p(99.9)=3.18ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=29.81ms min=2.2ms   med=29.3ms  max=292.04ms p(90)=39.4ms   p(95)=42.7ms   p(99.9)=64.97ms
     http_reqs......................: 198706  1651.986237/s
     iteration_duration.............: avg=30.2ms  min=4.76ms  med=29.64ms max=317.78ms p(90)=39.77ms  p(95)=43.1ms   p(99.9)=66.03ms
     iterations.....................: 198606  1651.154865/s
     success_rate...................: 100.00% ✓ 198606      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.359.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 517698      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 208 MB  1.7 MB/s
     http_req_blocked...............: avg=3.25µs  min=872ns   med=2.33µs  max=4.13ms   p(90)=4.02µs   p(95)=4.8µs    p(99.9)=34.94µs
     http_req_connecting............: avg=563ns   min=0s      med=0s      max=4.09ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.52ms min=2.25ms  med=33.6ms  max=299.99ms p(90)=49.38ms  p(95)=54.35ms  p(99.9)=78.42ms
       { expected_response:true }...: avg=34.52ms min=2.25ms  med=33.6ms  max=299.99ms p(90)=49.38ms  p(95)=54.35ms  p(99.9)=78.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 172666
     http_req_receiving.............: avg=79.99µs min=27.46µs med=61.22µs max=168.23ms p(90)=102.32µs p(95)=122.64µs p(99.9)=1.42ms 
     http_req_sending...............: avg=27.57µs min=4.87µs  med=10.7µs  max=165.26ms p(90)=18.33µs  p(95)=23.1µs   p(99.9)=1.18ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.42ms min=2.18ms  med=33.49ms max=299.69ms p(90)=49.27ms  p(95)=54.24ms  p(99.9)=78.14ms
     http_reqs......................: 172666  1435.353824/s
     iteration_duration.............: avg=34.76ms min=4.59ms  med=33.81ms max=311.5ms  p(90)=49.59ms  p(95)=54.56ms  p(99.9)=78.84ms
     iterations.....................: 172566  1434.522535/s
     success_rate...................: 100.00% ✓ 172566      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 462144      ✗ 0     
     data_received..................: 14 GB   112 MB/s
     data_sent......................: 185 MB  1.5 MB/s
     http_req_blocked...............: avg=3.56µs  min=1.17µs  med=2.97µs  max=2.02ms   p(90)=4.63µs   p(95)=5.37µs   p(99.9)=33.7µs 
     http_req_connecting............: avg=284ns   min=0s      med=0s      max=1.98ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=38.68ms min=2.75ms  med=37.6ms  max=294.01ms p(90)=55.13ms  p(95)=60.86ms  p(99.9)=92.02ms
       { expected_response:true }...: avg=38.68ms min=2.75ms  med=37.6ms  max=294.01ms p(90)=55.13ms  p(95)=60.86ms  p(99.9)=92.02ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 154148
     http_req_receiving.............: avg=79.37µs min=29.33µs med=64.25µs max=214.44ms p(90)=101.72µs p(95)=119.02µs p(99.9)=1.2ms  
     http_req_sending...............: avg=26.87µs min=5.57µs  med=12.78µs max=105.13ms p(90)=19.26µs  p(95)=23.2µs   p(99.9)=1.05ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=38.58ms min=2.65ms  med=37.5ms  max=293.62ms p(90)=55.02ms  p(95)=60.73ms  p(99.9)=91.8ms 
     http_reqs......................: 154148  1280.957821/s
     iteration_duration.............: avg=38.94ms min=6.13ms  med=37.83ms max=302.82ms p(90)=55.35ms  p(95)=61.1ms   p(99.9)=92.43ms
     iterations.....................: 154048  1280.126829/s
     success_rate...................: 100.00% ✓ 154048      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 188574     ✗ 0    
     data_received..................: 5.5 GB  46 MB/s
     data_sent......................: 76 MB   627 kB/s
     http_req_blocked...............: avg=4.59µs  min=942ns   med=3.02µs  max=3.58ms   p(90)=4.51µs   p(95)=5.15µs   p(99.9)=52.44µs 
     http_req_connecting............: avg=1.37µs  min=0s      med=0s      max=3.55ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=95.06ms min=4.5ms   med=92.26ms max=340.46ms p(90)=114.51ms p(95)=125.09ms p(99.9)=220.2ms 
       { expected_response:true }...: avg=95.06ms min=4.5ms   med=92.26ms max=340.46ms p(90)=114.51ms p(95)=125.09ms p(99.9)=220.2ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 62958
     http_req_receiving.............: avg=84.17µs min=28.2µs  med=77.19µs max=75.2ms   p(90)=110.95µs p(95)=123.9µs  p(99.9)=611.38µs
     http_req_sending...............: avg=23.28µs min=4.59µs  med=14.11µs max=159.13ms p(90)=19.93µs  p(95)=22.05µs  p(99.9)=587.44µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.96ms min=4.41ms  med=92.16ms max=339.93ms p(90)=114.4ms  p(95)=124.96ms p(99.9)=219.92ms
     http_reqs......................: 62958   522.180569/s
     iteration_duration.............: avg=95.46ms min=27.23ms med=92.51ms max=349.01ms p(90)=114.77ms p(95)=125.39ms p(99.9)=223.53ms
     iterations.....................: 62858   521.351158/s
     success_rate...................: 100.00% ✓ 62858      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.18.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 147558     ✗ 0    
     data_received..................: 4.3 GB  36 MB/s
     data_sent......................: 59 MB   490 kB/s
     http_req_blocked...............: avg=6.12µs   min=1.35µs  med=3.81µs   max=4.2ms    p(90)=5.42µs   p(95)=6.04µs   p(99.9)=608.65µs
     http_req_connecting............: avg=2.04µs   min=0s      med=0s       max=4.14ms   p(90)=0s       p(95)=0s       p(99.9)=561.48µs
     http_req_duration..............: avg=121.49ms min=5.31ms  med=119.27ms max=325.75ms p(90)=160.31ms p(95)=172.75ms p(99.9)=218.34ms
       { expected_response:true }...: avg=121.49ms min=5.31ms  med=119.27ms max=325.75ms p(90)=160.31ms p(95)=172.75ms p(99.9)=218.34ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49286
     http_req_receiving.............: avg=90.2µs   min=32.82µs med=83.26µs  max=135.91ms p(90)=113.91µs p(95)=126.33µs p(99.9)=571.45µs
     http_req_sending...............: avg=29.33µs  min=6.2µs   med=17.74µs  max=129.21ms p(90)=22.87µs  p(95)=24.84µs  p(99.9)=563.68µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=121.37ms min=5.17ms  med=119.15ms max=325.18ms p(90)=160.18ms p(95)=172.63ms p(99.9)=218.12ms
     http_reqs......................: 49286   408.416203/s
     iteration_duration.............: avg=122.02ms min=24.47ms med=119.63ms max=334.09ms p(90)=160.64ms p(95)=173.05ms p(99.9)=221.76ms
     iterations.....................: 49186   407.587537/s
     success_rate...................: 100.00% ✓ 49186      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-v3 (HotChocolate subgraphs) (v3.0.0-preview.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 137232     ✗ 0    
     data_received..................: 4.0 GB  33 MB/s
     data_sent......................: 55 MB   456 kB/s
     http_req_blocked...............: avg=5.86µs   min=1.37µs  med=3.48µs   max=4.02ms   p(90)=4.95µs   p(95)=5.56µs   p(99.9)=936.69µs
     http_req_connecting............: avg=2.13µs   min=0s      med=0s       max=3.98ms   p(90)=0s       p(95)=0s       p(99.9)=904.92µs
     http_req_duration..............: avg=130.66ms min=5.46ms  med=128.26ms max=317.05ms p(90)=170.73ms p(95)=183.7ms  p(99.9)=236.3ms 
       { expected_response:true }...: avg=130.66ms min=5.46ms  med=128.26ms max=317.05ms p(90)=170.73ms p(95)=183.7ms  p(99.9)=236.3ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 45844
     http_req_receiving.............: avg=84.49µs  min=31.8µs  med=79.53µs  max=34.29ms  p(90)=111.17µs p(95)=123.6µs  p(99.9)=572.16µs
     http_req_sending...............: avg=26.94µs  min=6.03µs  med=16.7µs   max=96.01ms  p(90)=22.08µs  p(95)=23.96µs  p(99.9)=519.44µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=130.55ms min=5.38ms  med=128.15ms max=316.82ms p(90)=170.62ms p(95)=183.57ms p(99.9)=236.15ms
     http_reqs......................: 45844   379.74026/s
     iteration_duration.............: avg=131.22ms min=27.12ms med=128.57ms max=332.67ms p(90)=171.06ms p(95)=184.11ms p(99.9)=238.91ms
     iterations.....................: 45744   378.911929/s
     success_rate...................: 100.00% ✓ 45744      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 95685      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   318 kB/s
     http_req_blocked...............: avg=10.57µs  min=1.13µs  med=3.13µs   max=9.89ms   p(90)=4.44µs   p(95)=4.98µs   p(99.9)=3.76ms  
     http_req_connecting............: avg=7.05µs   min=0s      med=0s       max=9.84ms   p(90)=0s       p(95)=0s       p(99.9)=3.58ms  
     http_req_duration..............: avg=187.37ms min=7.75ms  med=188.57ms max=385.82ms p(90)=197.05ms p(95)=201.91ms p(99.9)=268.61ms
       { expected_response:true }...: avg=187.37ms min=7.75ms  med=188.57ms max=385.82ms p(90)=197.05ms p(95)=201.91ms p(99.9)=268.61ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31995
     http_req_receiving.............: avg=89.98µs  min=32.29µs med=86.88µs  max=20.55ms  p(90)=116.18µs p(95)=126.6µs  p(99.9)=652.25µs
     http_req_sending...............: avg=30.58µs  min=5.06µs  med=16.34µs  max=99.37ms  p(90)=20.7µs   p(95)=22.45µs  p(99.9)=1.55ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=187.25ms min=7.62ms  med=188.46ms max=385.28ms p(90)=196.92ms p(95)=201.78ms p(99.9)=268.21ms
     http_reqs......................: 31995   264.45758/s
     iteration_duration.............: avg=188.23ms min=51.77ms med=188.92ms max=400.03ms p(90)=197.34ms p(95)=202.2ms  p(99.9)=269.44ms
     iterations.....................: 31895   263.631021/s
     success_rate...................: 100.00% ✓ 31895      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 90066      ✗ 0    
     data_received..................: 2.6 GB  22 MB/s
     data_sent......................: 36 MB   299 kB/s
     http_req_blocked...............: avg=6.39µs   min=1.08µs  med=3.02µs   max=4.03ms   p(90)=4.31µs   p(95)=4.83µs   p(99.9)=1.43ms  
     http_req_connecting............: avg=3.19µs   min=0s      med=0s       max=3.99ms   p(90)=0s       p(95)=0s       p(99.9)=1.41ms  
     http_req_duration..............: avg=199.04ms min=6.44ms  med=181.07ms max=762.93ms p(90)=232.15ms p(95)=272.44ms p(99.9)=689.76ms
       { expected_response:true }...: avg=199.04ms min=6.44ms  med=181.07ms max=762.93ms p(90)=232.15ms p(95)=272.44ms p(99.9)=689.76ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 30122
     http_req_receiving.............: avg=93.32µs  min=33.04µs med=87.24µs  max=102.83ms p(90)=116.78µs p(95)=127.94µs p(99.9)=618.56µs
     http_req_sending...............: avg=26.81µs  min=5.43µs  med=16.53µs  max=60.12ms  p(90)=20.63µs  p(95)=22.25µs  p(99.9)=510.83µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=198.92ms min=6.32ms  med=180.95ms max=762.83ms p(90)=232.04ms p(95)=272.31ms p(99.9)=689.65ms
     http_reqs......................: 30122   249.174119/s
     iteration_duration.............: avg=199.95ms min=43.02ms med=181.41ms max=763.16ms p(90)=232.55ms p(95)=273.91ms p(99.9)=690.4ms 
     iterations.....................: 30022   248.346902/s
     success_rate...................: 100.00% ✓ 30022      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

