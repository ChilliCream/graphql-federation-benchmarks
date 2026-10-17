## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-net11 | 16.7.0-p.28 | 2,733 | 2,855 | 2,727 | 1.6% |  |
| fusion-nightly | 16.7.0-p.28 | 2,694 | 2,747 | 2,643 | 1.3% |  |
| fusion | 16.6.8 | 2,448 | 2,548 | 2,433 | 1.6% |  |
| fusion-nightly-fed | 16.7.0-p.28 | 2,386 | 2,515 | 2,371 | 2.1% |  |
| hive-router | v0.3.5 | 2,300 | 2,473 | 2,286 | 2.7% |  |
| cosmo | 0.359.0 | 1,295 | 1,348 | 1,289 | 1.5% |  |
| caliban | 3.2.0 | 1,277 | 1,332 | 1,269 | 1.6% |  |
| feddi | e91d605ed222 | 833 | 868 | 798 | 2.9% |  |
| hive-gateway-router-runtime | 2.15.2 | 471 | 483 | 469 | 1.0% |  |
| hive-gateway | 2.15.2 | 244 | 250 | 242 | 1.0% |  |
| apollo-gateway | 2.14.4 | 231 | 237 | 230 | 1.0% |  |
| apollo-router | v2.18.0 | — | — | — | — | non-compatible response (42282 across 9/9 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | non-compatible response (6313 across 9/9 runs) |
| grafbase | 0.53.5 | — | — | — | — | non-compatible response (365859 across 9/9 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net11 (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 502515      ✗ 0     
     data_received..................: 15 GB   240 MB/s
     data_sent......................: 202 MB  3.3 MB/s
     http_req_blocked...............: avg=27.81µs min=851ns   med=2.33µs   max=114.95ms p(90)=4.42µs   p(95)=5.66µs   p(99.9)=3.33ms  
     http_req_connecting............: avg=24.31µs min=0s      med=0s       max=114.86ms p(90)=0s       p(95)=0s       p(99.9)=3.2ms   
     http_req_duration..............: avg=84.3ms  min=1.31ms  med=78.64ms  max=328.73ms p(90)=162.41ms p(95)=184.01ms p(99.9)=256.62ms
       { expected_response:true }...: avg=84.3ms  min=1.31ms  med=78.64ms  max=328.73ms p(90)=162.41ms p(95)=184.01ms p(99.9)=256.62ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 168505
     http_req_receiving.............: avg=1.5ms   min=53.02µs med=126.71µs max=297.13ms p(90)=3.8ms    p(95)=5.89ms   p(99.9)=40ms    
     http_req_sending...............: avg=82.39µs min=4.67µs  med=9.47µs   max=184.83ms p(90)=22.76µs  p(95)=124.9µs  p(99.9)=11.82ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=82.71ms min=1.25ms  med=76.84ms  max=328.09ms p(90)=160.75ms p(95)=182.62ms p(99.9)=255.28ms
     http_reqs......................: 168505  2733.864247/s
     iteration_duration.............: avg=85.1ms  min=3.23ms  med=79.52ms  max=345.58ms p(90)=163.03ms p(95)=184.64ms p(99.9)=258.17ms
     iterations.....................: 167505  2717.640015/s
     success_rate...................: 100.00% ✓ 167505      ✗ 0     
     vus............................: 85      min=0         max=494 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 496116      ✗ 0     
     data_received..................: 15 GB   236 MB/s
     data_sent......................: 200 MB  3.2 MB/s
     http_req_blocked...............: avg=32.15µs min=821ns   med=2.72µs   max=94.87ms  p(90)=4.76µs   p(95)=6.03µs   p(99.9)=5.4ms   
     http_req_connecting............: avg=28.39µs min=0s      med=0s       max=94.57ms  p(90)=0s       p(95)=0s       p(99.9)=4.93ms  
     http_req_duration..............: avg=85.37ms min=1.4ms   med=71.42ms  max=1.07s    p(90)=169.33ms p(95)=203.78ms p(99.9)=623.65ms
       { expected_response:true }...: avg=85.37ms min=1.4ms   med=71.42ms  max=1.07s    p(90)=169.33ms p(95)=203.78ms p(99.9)=623.65ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 166372
     http_req_receiving.............: avg=2.31ms  min=51.38µs med=102.34µs max=521.42ms p(90)=2.33ms   p(95)=7.43ms   p(99.9)=210.92ms
     http_req_sending...............: avg=92.74µs min=4.73µs  med=10.4µs   max=195.03ms p(90)=22.79µs  p(95)=133.98µs p(99.9)=14.45ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=82.96ms min=1.33ms  med=70.09ms  max=1.07s    p(90)=164.37ms p(95)=196.96ms p(99.9)=573.23ms
     http_reqs......................: 166372  2694.279075/s
     iteration_duration.............: avg=86.22ms min=2.8ms   med=72.18ms  max=1.14s    p(90)=170.09ms p(95)=204.83ms p(99.9)=624.5ms 
     iterations.....................: 165372  2678.084769/s
     success_rate...................: 100.00% ✓ 165372      ✗ 0     
     vus............................: 90      min=0         max=500 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion (HotChocolate subgraphs) (16.6.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 451464      ✗ 0     
     data_received..................: 13 GB   215 MB/s
     data_sent......................: 182 MB  2.9 MB/s
     http_req_blocked...............: avg=19.41µs min=862ns   med=2.26µs  max=56.43ms  p(90)=4µs      p(95)=5.2µs    p(99.9)=2.43ms  
     http_req_connecting............: avg=16.38µs min=0s      med=0s      max=56.38ms  p(90)=0s       p(95)=0s       p(99.9)=2.16ms  
     http_req_duration..............: avg=93.88ms min=1.44ms  med=81.92ms max=1.45s    p(90)=178.31ms p(95)=206.25ms p(99.9)=674.89ms
       { expected_response:true }...: avg=93.88ms min=1.44ms  med=81.92ms max=1.45s    p(90)=178.31ms p(95)=206.25ms p(99.9)=674.89ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 151488
     http_req_receiving.............: avg=1.42ms  min=50.56µs med=99.95µs max=904.2ms  p(90)=1.6ms    p(95)=4.19ms   p(99.9)=83.79ms 
     http_req_sending...............: avg=69.5µs  min=4.48µs  med=9.28µs  max=106.43ms p(90)=19.19µs  p(95)=110.96µs p(99.9)=9.4ms   
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.39ms min=1.38ms  med=80.6ms  max=1.45s    p(90)=176.18ms p(95)=202.83ms p(99.9)=650.54ms
     http_reqs......................: 151488  2448.144375/s
     iteration_duration.............: avg=94.79ms min=2.75ms  med=82.9ms  max=1.45s    p(90)=179.01ms p(95)=207.2ms  p(99.9)=675.53ms
     iterations.....................: 150488  2431.983726/s
     success_rate...................: 100.00% ✓ 150488      ✗ 0     
     vus............................: 0       min=0         max=500 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 441870      ✗ 0     
     data_received..................: 13 GB   209 MB/s
     data_sent......................: 178 MB  2.9 MB/s
     http_req_blocked...............: avg=22.21µs min=862ns   med=2.33µs   max=90.39ms  p(90)=4.4µs    p(95)=5.67µs   p(99.9)=2.32ms  
     http_req_connecting............: avg=18.94µs min=0s      med=0s       max=90.28ms  p(90)=0s       p(95)=0s       p(99.9)=2.26ms  
     http_req_duration..............: avg=95.9ms  min=1.61ms  med=82.62ms  max=1.14s    p(90)=184.92ms p(95)=212.69ms p(99.9)=682.27ms
       { expected_response:true }...: avg=95.9ms  min=1.61ms  med=82.62ms  max=1.14s    p(90)=184.92ms p(95)=212.69ms p(99.9)=682.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 148290
     http_req_receiving.............: avg=2.23ms  min=51.72µs med=109.23µs max=590.13ms p(90)=2.74ms   p(95)=7.35ms   p(99.9)=140ms   
     http_req_sending...............: avg=78.16µs min=4.72µs  med=9.69µs   max=195.27ms p(90)=21.48µs  p(95)=113.3µs  p(99.9)=10.52ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.59ms min=1.5ms   med=80.82ms  max=1.14s    p(90)=181.53ms p(95)=207.54ms p(99.9)=655.2ms 
     http_reqs......................: 148290  2386.352668/s
     iteration_duration.............: avg=96.86ms min=3.06ms  med=83.66ms  max=1.14s    p(90)=185.61ms p(95)=213.49ms p(99.9)=685.35ms
     iterations.....................: 147290  2370.260196/s
     success_rate...................: 100.00% ✓ 147290      ✗ 0     
     vus............................: 64      min=0         max=496 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 423279      ✗ 0     
     data_received..................: 12 GB   201 MB/s
     data_sent......................: 171 MB  2.8 MB/s
     http_req_blocked...............: avg=13.08µs  min=912ns   med=2.36µs  max=60.35ms  p(90)=4.07µs   p(95)=5.32µs   p(99.9)=961.71µs
     http_req_connecting............: avg=9.89µs   min=0s      med=0s      max=60.27ms  p(90)=0s       p(95)=0s       p(99.9)=906.65µs
     http_req_duration..............: avg=100.13ms min=1.47ms  med=94.93ms max=361.1ms  p(90)=193.92ms p(95)=210.32ms p(99.9)=258.16ms
       { expected_response:true }...: avg=100.13ms min=1.47ms  med=94.93ms max=361.1ms  p(90)=193.92ms p(95)=210.32ms p(99.9)=258.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 142093
     http_req_receiving.............: avg=112.61µs min=27.46µs med=56.62µs max=101.28ms p(90)=118.81µs p(95)=329.92µs p(99.9)=7.28ms  
     http_req_sending...............: avg=60.72µs  min=5.03µs  med=10.33µs max=179.39ms p(90)=18.9µs   p(95)=115.03µs p(99.9)=7.61ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=99.96ms  min=1.43ms  med=94.76ms max=360.39ms p(90)=193.72ms p(95)=210.12ms p(99.9)=257.62ms
     http_reqs......................: 142093  2300.968699/s
     iteration_duration.............: avg=101.07ms min=3.78ms  med=96.07ms max=371.22ms p(90)=194.39ms p(95)=210.76ms p(99.9)=258.57ms
     iterations.....................: 141093  2284.7753/s
     success_rate...................: 100.00% ✓ 141093      ✗ 0     
     vus............................: 92      min=0         max=500 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 241209      ✗ 0    
     data_received..................: 7.1 GB  113 MB/s
     data_sent......................: 98 MB   1.6 MB/s
     http_req_blocked...............: avg=6.97µs   min=971ns   med=2.86µs   max=16.71ms  p(90)=4.81µs   p(95)=5.88µs   p(99.9)=846.13µs
     http_req_connecting............: avg=3.25µs   min=0s      med=0s       max=16.63ms  p(90)=0s       p(95)=0s       p(99.9)=755.05µs
     http_req_duration..............: avg=175.21ms min=2.17ms  med=173.6ms  max=473.68ms p(90)=332.62ms p(95)=357.27ms p(99.9)=422.82ms
       { expected_response:true }...: avg=175.21ms min=2.17ms  med=173.6ms  max=473.68ms p(90)=332.62ms p(95)=357.27ms p(99.9)=422.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 81403
     http_req_receiving.............: avg=88.63µs  min=26.48µs med=65.81µs  max=213.86ms p(90)=108.49µs p(95)=129.61µs p(99.9)=2.09ms  
     http_req_sending...............: avg=38.43µs  min=5.08µs  med=12µs     max=178.21ms p(90)=19.56µs  p(95)=24.32µs  p(99.9)=4.22ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=175.08ms min=2.08ms  med=173.47ms max=473.28ms p(90)=332.51ms p(95)=357.11ms p(99.9)=422.73ms
     http_reqs......................: 81403   1295.831951/s
     iteration_duration.............: avg=177.63ms min=6.17ms  med=176.5ms  max=473.92ms p(90)=333.49ms p(95)=357.94ms p(99.9)=423.67ms
     iterations.....................: 80403   1279.913226/s
     success_rate...................: 100.00% ✓ 80403       ✗ 0    
     vus............................: 95      min=0         max=500
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

     checks.........................: 100.00% ✓ 237657      ✗ 0    
     data_received..................: 7.0 GB  112 MB/s
     data_sent......................: 96 MB   1.5 MB/s
     http_req_blocked...............: avg=5.76µs   min=1.02µs  med=2.54µs   max=21.71ms p(90)=4.38µs   p(95)=5.37µs   p(99.9)=472.64µs
     http_req_connecting............: avg=2.51µs   min=0s      med=0s       max=21.63ms p(90)=0s       p(95)=0s       p(99.9)=418.07µs
     http_req_duration..............: avg=177.97ms min=2.36ms  med=147.48ms max=1.1s    p(90)=371.26ms p(95)=436.61ms p(99.9)=763.14ms
       { expected_response:true }...: avg=177.97ms min=2.36ms  med=147.48ms max=1.1s    p(90)=371.26ms p(95)=436.61ms p(99.9)=763.14ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 80219
     http_req_receiving.............: avg=79.32µs  min=29.14µs med=62.47µs  max=54.02ms p(90)=100.29µs p(95)=116.93µs p(99.9)=2.12ms  
     http_req_sending...............: avg=30.76µs  min=5.12µs  med=11.65µs  max=151.9ms p(90)=18.31µs  p(95)=22.06µs  p(99.9)=3.37ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=177.86ms min=2.26ms  med=147.38ms max=1.1s    p(90)=371.18ms p(95)=436.53ms p(99.9)=763.05ms
     http_reqs......................: 80219   1277.083509/s
     iteration_duration.............: avg=180.46ms min=9.1ms   med=150.18ms max=1.1s    p(90)=372.79ms p(95)=438.19ms p(99.9)=765.04ms
     iterations.....................: 79219   1261.163546/s
     success_rate...................: 100.00% ✓ 79219       ✗ 0    
     vus............................: 95      min=0         max=500
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi (HotChocolate subgraphs) (e91d605ed222)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 152562     ✗ 0    
     data_received..................: 4.5 GB  73 MB/s
     data_sent......................: 62 MB   1.0 MB/s
     http_req_blocked...............: avg=7.22µs   min=941ns   med=2.67µs   max=9.2ms    p(90)=4.83µs   p(95)=5.78µs   p(99.9)=1.17ms
     http_req_connecting............: avg=3.54µs   min=0s      med=0s       max=9.06ms   p(90)=0s       p(95)=0s       p(99.9)=1.01ms
     http_req_duration..............: avg=277.34ms min=1.59ms  med=136.28ms max=3.91s    p(90)=765.33ms p(95)=1.04s    p(99.9)=2.24s 
       { expected_response:true }...: avg=277.34ms min=1.59ms  med=136.28ms max=3.91s    p(90)=765.33ms p(95)=1.04s    p(99.9)=2.24s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 51854
     http_req_receiving.............: avg=83.42µs  min=26.42µs med=61.64µs  max=89.48ms  p(90)=106.51µs p(95)=124.65µs p(99.9)=3.03ms
     http_req_sending...............: avg=31.91µs  min=4.87µs  med=12.04µs  max=109.02ms p(90)=21.68µs  p(95)=25.14µs  p(99.9)=3.42ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=277.22ms min=1.53ms  med=136.14ms max=3.91s    p(90)=765.23ms p(95)=1.04s    p(99.9)=2.24s 
     http_reqs......................: 51854   833.698328/s
     iteration_duration.............: avg=283.08ms min=2.27ms  med=140.72ms max=3.92s    p(90)=772.18ms p(95)=1.05s    p(99.9)=2.25s 
     iterations.....................: 50854   817.620526/s
     success_rate...................: 100.00% ✓ 50854      ✗ 0    
     vus............................: 65      min=0        max=498
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 89235      ✗ 0    
     data_received..................: 2.7 GB  41 MB/s
     data_sent......................: 37 MB   566 kB/s
     http_req_blocked...............: avg=9.61µs   min=1.02µs  med=3.07µs   max=6.14ms   p(90)=4.91µs   p(95)=5.9µs    p(99.9)=1.72ms  
     http_req_connecting............: avg=5.44µs   min=0s      med=0s       max=5.93ms   p(90)=0s       p(95)=0s       p(99.9)=1.6ms   
     http_req_duration..............: avg=467.52ms min=4.33ms  med=434.99ms max=1.89s    p(90)=919.12ms p(95)=999.88ms p(99.9)=1.53s   
       { expected_response:true }...: avg=467.52ms min=4.33ms  med=434.99ms max=1.89s    p(90)=919.12ms p(95)=999.88ms p(99.9)=1.53s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 30745
     http_req_receiving.............: avg=85.07µs  min=29.3µs  med=76.76µs  max=8.95ms   p(90)=115.01µs p(95)=130.02µs p(99.9)=887.78µs
     http_req_sending...............: avg=46.16µs  min=5.12µs  med=14.3µs   max=194.08ms p(90)=21.06µs  p(95)=23.82µs  p(99.9)=3.61ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=467.38ms min=4.25ms  med=434.87ms max=1.89s    p(90)=919ms    p(95)=999.8ms  p(99.9)=1.53s   
     http_reqs......................: 30745   471.546501/s
     iteration_duration.............: avg=483.46ms min=19.76ms med=455.19ms max=1.9s     p(90)=923.19ms p(95)=1s       p(99.9)=1.53s   
     iterations.....................: 29745   456.209162/s
     success_rate...................: 100.00% ✓ 29745      ✗ 0    
     vus............................: 66      min=0        max=497
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 46695      ✗ 0    
     data_received..................: 1.5 GB  21 MB/s
     data_sent......................: 20 MB   293 kB/s
     http_req_blocked...............: avg=15µs     min=1.45µs  med=3.91µs   max=4.73ms  p(90)=5.97µs   p(95)=7.77µs  p(99.9)=2.11ms
     http_req_connecting............: avg=9.14µs   min=0s      med=0s       max=4.43ms  p(90)=0s       p(95)=0s      p(99.9)=2.09ms
     http_req_duration..............: avg=878.83ms min=5.84ms  med=785.09ms max=4.96s   p(90)=1.76s    p(95)=2.08s   p(99.9)=4.08s 
       { expected_response:true }...: avg=878.83ms min=5.84ms  med=785.09ms max=4.96s   p(90)=1.76s    p(95)=2.08s   p(99.9)=4.08s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16565
     http_req_receiving.............: avg=106.21µs min=36.68µs med=97.41µs  max=9.05ms  p(90)=137.48µs p(95)=153.9µs p(99.9)=1.67ms
     http_req_sending...............: avg=30.68µs  min=6.55µs  med=19.1µs   max=17.35ms p(90)=24.99µs  p(95)=28.97µs p(99.9)=3.45ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s      p(99.9)=0s    
     http_req_waiting...............: avg=878.69ms min=5.75ms  med=784.96ms max=4.96s   p(90)=1.76s    p(95)=2.08s   p(99.9)=4.08s 
     http_reqs......................: 16565   244.273471/s
     iteration_duration.............: avg=935.29ms min=63.51ms med=856.46ms max=4.97s   p(90)=1.77s    p(95)=2.09s   p(99.9)=4.11s 
     iterations.....................: 15565   229.52711/s
     success_rate...................: 100.00% ✓ 15565      ✗ 0    
     vus............................: 87      min=0        max=500
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

     checks.........................: 100.00% ✓ 44886      ✗ 0    
     data_received..................: 1.4 GB  20 MB/s
     data_sent......................: 19 MB   278 kB/s
     http_req_blocked...............: avg=15.98µs  min=1.41µs  med=3.68µs   max=12.45ms  p(90)=5.55µs   p(95)=7.13µs  p(99.9)=2.45ms
     http_req_connecting............: avg=10.31µs  min=0s      med=0s       max=12.39ms  p(90)=0s       p(95)=0s      p(99.9)=2.42ms
     http_req_duration..............: avg=910.5ms  min=7.81ms  med=815.58ms max=3.3s     p(90)=1.86s    p(95)=1.97s   p(99.9)=2.92s 
       { expected_response:true }...: avg=910.5ms  min=7.81ms  med=815.58ms max=3.3s     p(90)=1.86s    p(95)=1.97s   p(99.9)=2.92s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 15962
     http_req_receiving.............: avg=109.26µs min=37.51µs med=90.11µs  max=117.11ms p(90)=129.81µs p(95)=145.5µs p(99.9)=1.12ms
     http_req_sending...............: avg=47.7µs   min=6.19µs  med=17.35µs  max=90.46ms  p(90)=23.21µs  p(95)=27.1µs  p(99.9)=3.1ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s    
     http_req_waiting...............: avg=910.34ms min=7.68ms  med=815.48ms max=3.3s     p(90)=1.86s    p(95)=1.97s   p(99.9)=2.92s 
     http_reqs......................: 15962   231.99884/s
     iteration_duration.............: avg=971.35ms min=48.48ms med=925.86ms max=3.3s     p(90)=1.87s    p(95)=1.97s   p(99.9)=2.95s 
     iterations.....................: 14962   217.464393/s
     success_rate...................: 100.00% ✓ 14962      ✗ 0    
     vus............................: 94      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

