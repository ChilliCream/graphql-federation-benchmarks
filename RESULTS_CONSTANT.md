## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly | 16.7.0-p.31 | 3,085 | 3,260 | 3,054 | 2.2% |  |
| feddi-gateway | 3c75a7db8876 | 3,010 | 3,178 | 2,988 | 2.2% |  |
| fusion-nightly-net11 | 16.7.0-p.31 | 2,957 | 3,142 | 2,934 | 2.4% |  |
| fusion-nightly-fed | 16.7.0-p.31 | 2,778 | 2,963 | 2,751 | 2.5% |  |
| hive-router | v0.3.5 | 2,593 | 2,746 | 2,537 | 2.5% |  |
| fusion | 16.6.9 | 2,559 | 2,660 | 2,546 | 1.5% |  |
| grafbase | 0.53.5 | 1,680 | 1,741 | 1,672 | 1.4% |  |
| caliban | 3.2.0 | 1,464 | 1,519 | 1,457 | 1.5% |  |
| cosmo | 0.359.0 | 1,420 | 1,480 | 1,415 | 1.6% |  |
| hive-gateway-router-runtime | 2.15.2 | 510 | 531 | 507 | 1.5% |  |
| apollo-router | v2.18.0 | 450 | 463 | 447 | 1.3% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 379 | 398 | 376 | 2.0% |  |
| apollo-gateway | 2.14.4 | 265 | 272 | 263 | 1.1% |  |
| hive-gateway | 2.15.2 | 256 | 265 | 255 | 1.4% |  |


### Details

<details>
  <summary>Summary for: fusion-nightly (HotChocolate subgraphs) (16.7.0-p.31)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1112073     ✗ 0     
     data_received..................: 33 GB   271 MB/s
     data_sent......................: 446 MB  3.7 MB/s
     http_req_blocked...............: avg=2.92µs  min=872ns   med=1.97µs   max=25.54ms  p(90)=3.33µs  p(95)=4.14µs  p(99.9)=30.08µs
     http_req_connecting............: avg=238ns   min=0s      med=0s       max=3.54ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=15.96ms min=1.24ms  med=15.02ms  max=282.19ms p(90)=22.75ms p(95)=26.59ms p(99.9)=50.4ms 
       { expected_response:true }...: avg=15.96ms min=1.24ms  med=15.02ms  max=282.19ms p(90)=22.75ms p(95)=26.59ms p(99.9)=50.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 370791
     http_req_receiving.............: avg=1.27ms  min=52.13µs med=102.78µs max=246.32ms p(90)=3.53ms  p(95)=5.32ms  p(99.9)=30.09ms
     http_req_sending...............: avg=55.87µs min=4.55µs  med=8.28µs   max=157.48ms p(90)=16.91µs p(95)=95.18µs p(99.9)=9.95ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=14.63ms min=1.16ms  med=13.71ms  max=281.5ms  p(90)=21.05ms p(95)=24.72ms p(99.9)=46.92ms
     http_reqs......................: 370791  3085.244221/s
     iteration_duration.............: avg=16.17ms min=2.11ms  med=15.22ms  max=296.41ms p(90)=22.97ms p(95)=26.82ms p(99.9)=51.1ms 
     iterations.....................: 370691  3084.41215/s
     success_rate...................: 100.00% ✓ 370691      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1084644     ✗ 0     
     data_received..................: 32 GB   263 MB/s
     data_sent......................: 435 MB  3.6 MB/s
     http_req_blocked...............: avg=4.62µs  min=1.02µs   med=2.68µs  max=35.13ms  p(90)=4.22µs  p(95)=4.97µs   p(99.9)=39.1µs 
     http_req_connecting............: avg=933ns   min=0s       med=0s      max=35.09ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.36ms min=999.72µs med=15.75ms max=271.06ms p(90)=23.33ms p(95)=26.97ms  p(99.9)=49.44ms
       { expected_response:true }...: avg=16.36ms min=999.72µs med=15.75ms max=271.06ms p(90)=23.33ms p(95)=26.97ms  p(99.9)=49.44ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 361648
     http_req_receiving.............: avg=109.3µs min=26.18µs  med=50.53µs max=116.77ms p(90)=99.02µs p(95)=224.42µs p(99.9)=8.89ms 
     http_req_sending...............: avg=58.41µs min=4.6µs    med=9.82µs  max=122.87ms p(90)=17.07µs p(95)=116.34µs p(99.9)=10.02ms
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.19ms min=950.55µs med=15.62ms max=246.33ms p(90)=23.12ms p(95)=26.6ms   p(99.9)=48.26ms
     http_reqs......................: 361648  3010.261092/s
     iteration_duration.............: avg=16.58ms min=1.69ms   med=15.95ms max=287.84ms p(90)=23.55ms p(95)=27.24ms  p(99.9)=50.41ms
     iterations.....................: 361548  3009.428719/s
     success_rate...................: 100.00% ✓ 361548      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net11 (HotChocolate subgraphs) (16.7.0-p.31)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1065789     ✗ 0     
     data_received..................: 31 GB   259 MB/s
     data_sent......................: 427 MB  3.6 MB/s
     http_req_blocked...............: avg=3.08µs  min=762ns   med=1.99µs   max=18.55ms  p(90)=3.46µs  p(95)=4.3µs   p(99.9)=29.95µs
     http_req_connecting............: avg=367ns   min=0s      med=0s       max=4.93ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=16.66ms min=1.28ms  med=15.77ms  max=287.61ms p(90)=23.49ms p(95)=27.03ms p(99.9)=51.05ms
       { expected_response:true }...: avg=16.66ms min=1.28ms  med=15.77ms  max=287.61ms p(90)=23.49ms p(95)=27.03ms p(99.9)=51.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 355363
     http_req_receiving.............: avg=1.82ms  min=50.59µs med=323.02µs max=253.75ms p(90)=4.59ms  p(95)=6.26ms  p(99.9)=31.04ms
     http_req_sending...............: avg=51.3µs  min=4.39µs  med=8.28µs   max=200.15ms p(90)=17.36µs p(95)=94.83µs p(99.9)=6.59ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=14.78ms min=1.17ms  med=13.86ms  max=122.01ms p(90)=20.95ms p(95)=24.4ms  p(99.9)=45.82ms
     http_reqs......................: 355363  2957.326531/s
     iteration_duration.............: avg=16.87ms min=2.1ms   med=15.96ms  max=299.95ms p(90)=23.7ms  p(95)=27.28ms p(99.9)=51.71ms
     iterations.....................: 355263  2956.494332/s
     success_rate...................: 100.00% ✓ 355263      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed (HotChocolate subgraphs) (16.7.0-p.31)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1001679     ✗ 0     
     data_received..................: 29 GB   244 MB/s
     data_sent......................: 401 MB  3.3 MB/s
     http_req_blocked...............: avg=3.47µs  min=871ns   med=2.26µs   max=16.05ms  p(90)=3.96µs  p(95)=4.77µs   p(99.9)=29.2µs 
     http_req_connecting............: avg=628ns   min=0s      med=0s       max=7ms      p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.73ms min=1.65ms  med=16.89ms  max=285.93ms p(90)=24.87ms p(95)=28.34ms  p(99.9)=51.8ms 
       { expected_response:true }...: avg=17.73ms min=1.65ms  med=16.89ms  max=285.93ms p(90)=24.87ms p(95)=28.34ms  p(99.9)=51.8ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 333993
     http_req_receiving.............: avg=1.21ms  min=50.38µs med=208.88µs max=248.68ms p(90)=3.06ms  p(95)=4.46ms   p(99.9)=27.7ms 
     http_req_sending...............: avg=60.48µs min=4.63µs  med=9.18µs   max=224.57ms p(90)=19.94µs p(95)=104.05µs p(99.9)=7.98ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.46ms min=1.56ms  med=15.62ms  max=283.63ms p(90)=23.32ms p(95)=26.71ms  p(99.9)=48.61ms
     http_reqs......................: 333993  2778.25465/s
     iteration_duration.............: avg=17.95ms min=2.44ms  med=17.1ms   max=300.93ms p(90)=25.09ms p(95)=28.59ms  p(99.9)=52.71ms
     iterations.....................: 333893  2777.422819/s
     success_rate...................: 100.00% ✓ 333893      ✗ 0     
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

     checks.........................: 100.00% ✓ 934962      ✗ 0     
     data_received..................: 27 GB   227 MB/s
     data_sent......................: 375 MB  3.1 MB/s
     http_req_blocked...............: avg=3.62µs   min=952ns   med=2.78µs  max=13.53ms  p(90)=4.54µs   p(95)=5.39µs   p(99.9)=40.22µs
     http_req_connecting............: avg=309ns    min=0s      med=0s      max=4.18ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=19.01ms  min=1.61ms  med=18.58ms max=271.64ms p(90)=26.48ms  p(95)=29.16ms  p(99.9)=49.65ms
       { expected_response:true }...: avg=19.01ms  min=1.61ms  med=18.58ms max=271.64ms p(90)=26.48ms  p(95)=29.16ms  p(99.9)=49.65ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 311754
     http_req_receiving.............: avg=100.34µs min=26.34µs med=54.79µs max=36.67ms  p(90)=101.99µs p(95)=180.86µs p(99.9)=7.64ms 
     http_req_sending...............: avg=49.72µs  min=5.06µs  med=11.06µs max=152.01ms p(90)=19.79µs  p(95)=114.26µs p(99.9)=4.17ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=18.86ms  min=1.52ms  med=18.46ms max=271.18ms p(90)=26.31ms  p(95)=28.92ms  p(99.9)=48.72ms
     http_reqs......................: 311754  2593.438436/s
     iteration_duration.............: avg=19.24ms  min=3.62ms  med=18.79ms max=288.12ms p(90)=26.7ms   p(95)=29.39ms  p(99.9)=50.38ms
     iterations.....................: 311654  2592.60655/s
     success_rate...................: 100.00% ✓ 311654      ✗ 0     
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

     checks.........................: 100.00% ✓ 922488      ✗ 0     
     data_received..................: 27 GB   224 MB/s
     data_sent......................: 370 MB  3.1 MB/s
     http_req_blocked...............: avg=2.94µs  min=821ns   med=1.95µs   max=17.86ms  p(90)=3.58µs  p(95)=4.4µs   p(99.9)=32.27µs
     http_req_connecting............: avg=302ns   min=0s      med=0s       max=3.57ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=19.28ms min=1.51ms  med=18.65ms  max=304.7ms  p(90)=26.28ms p(95)=29.33ms p(99.9)=49.71ms
       { expected_response:true }...: avg=19.28ms min=1.51ms  med=18.65ms  max=304.7ms  p(90)=26.28ms p(95)=29.33ms p(99.9)=49.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 307596
     http_req_receiving.............: avg=1.42ms  min=51.46µs med=980.07µs max=288.05ms p(90)=3.23ms  p(95)=4.27ms  p(99.9)=25.33ms
     http_req_sending...............: avg=46.07µs min=4.49µs  med=8.2µs    max=144.31ms p(90)=18.39µs p(95)=91.35µs p(99.9)=5.18ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.81ms min=1.41ms  med=17.14ms  max=303.19ms p(90)=24.59ms p(95)=27.54ms p(99.9)=46.77ms
     http_reqs......................: 307596  2559.101368/s
     iteration_duration.............: avg=19.5ms  min=2.72ms  med=18.85ms  max=313.52ms p(90)=26.49ms p(95)=29.56ms p(99.9)=50.22ms
     iterations.....................: 307496  2558.2694/s
     success_rate...................: 100.00% ✓ 307496      ✗ 0     
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

     checks.........................: 100.00% ✓ 606204      ✗ 0     
     data_received..................: 18 GB   147 MB/s
     data_sent......................: 243 MB  2.0 MB/s
     http_req_blocked...............: avg=3.43µs  min=852ns   med=2.29µs  max=8.27ms   p(90)=4.81µs   p(95)=5.92µs   p(99.9)=45.7µs 
     http_req_connecting............: avg=463ns   min=0s      med=0s      max=3.58ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=29.43ms min=2.2ms   med=29.2ms  max=307.81ms p(90)=38.43ms  p(95)=41.42ms  p(99.9)=62.28ms
       { expected_response:true }...: avg=29.43ms min=2.2ms   med=29.2ms  max=307.81ms p(90)=38.43ms  p(95)=41.42ms  p(99.9)=62.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 202168
     http_req_receiving.............: avg=97.46µs min=27.11µs med=54.6µs  max=164.13ms p(90)=126.14µs p(95)=209.45µs p(99.9)=4.05ms 
     http_req_sending...............: avg=43.37µs min=4.67µs  med=9.51µs  max=196.94ms p(90)=23.94µs  p(95)=114.75µs p(99.9)=3.25ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=29.29ms min=2.13ms  med=29.07ms max=307.24ms p(90)=38.29ms  p(95)=41.25ms  p(99.9)=61.81ms
     http_reqs......................: 202168  1680.641216/s
     iteration_duration.............: avg=29.68ms min=4.63ms  med=29.42ms max=319.37ms p(90)=38.66ms  p(95)=41.65ms  p(99.9)=62.95ms
     iterations.....................: 202068  1679.809907/s
     success_rate...................: 100.00% ✓ 202068      ✗ 0     
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

     checks.........................: 100.00% ✓ 528198      ✗ 0     
     data_received..................: 15 GB   128 MB/s
     data_sent......................: 212 MB  1.8 MB/s
     http_req_blocked...............: avg=3.94µs  min=992ns   med=2.96µs  max=3.74ms   p(90)=5.1µs    p(95)=5.97µs   p(99.9)=41.31µs
     http_req_connecting............: avg=583ns   min=0s      med=0s      max=3.7ms    p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.81ms min=2.42ms  med=32.91ms max=299.79ms p(90)=47.58ms  p(95)=52.38ms  p(99.9)=77.38ms
       { expected_response:true }...: avg=33.81ms min=2.42ms  med=32.91ms max=299.79ms p(90)=47.58ms  p(95)=52.38ms  p(99.9)=77.38ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 176166
     http_req_receiving.............: avg=86.9µs  min=27.08µs med=66.94µs max=157.28ms p(90)=112.41µs p(95)=136.51µs p(99.9)=1.82ms 
     http_req_sending...............: avg=33.74µs min=4.97µs  med=13.52µs max=124.7ms  p(90)=22.43µs  p(95)=27.85µs  p(99.9)=1.4ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.69ms min=2.3ms   med=32.8ms  max=299.59ms p(90)=47.46ms  p(95)=52.24ms  p(99.9)=77.08ms
     http_reqs......................: 176166  1464.365076/s
     iteration_duration.............: avg=34.06ms min=6.19ms  med=33.14ms max=312.92ms p(90)=47.82ms  p(95)=52.62ms  p(99.9)=77.79ms
     iterations.....................: 176066  1463.533835/s
     success_rate...................: 100.00% ✓ 176066      ✗ 0     
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

     checks.........................: 100.00% ✓ 512469      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 205 MB  1.7 MB/s
     http_req_blocked...............: avg=3.92µs  min=1.12µs  med=2.87µs  max=10.5ms   p(90)=4.63µs   p(95)=5.44µs   p(99.9)=37.51µs
     http_req_connecting............: avg=530ns   min=0s      med=0s      max=5.21ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.86ms min=2.46ms  med=33.93ms max=299.93ms p(90)=50.01ms  p(95)=54.97ms  p(99.9)=79.16ms
       { expected_response:true }...: avg=34.86ms min=2.46ms  med=33.93ms max=299.93ms p(90)=50.01ms  p(95)=54.97ms  p(99.9)=79.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 170923
     http_req_receiving.............: avg=84.42µs min=28.05µs med=66.89µs max=122.21ms p(90)=109.45µs p(95)=130.05µs p(99.9)=1.42ms 
     http_req_sending...............: avg=31.18µs min=5.1µs   med=12.04µs max=152.05ms p(90)=19.3µs   p(95)=24.46µs  p(99.9)=1.36ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.75ms min=2.38ms  med=33.81ms max=298.42ms p(90)=49.9ms   p(95)=54.86ms  p(99.9)=79.01ms
     http_reqs......................: 170923  1420.583496/s
     iteration_duration.............: avg=35.11ms min=4.85ms  med=34.15ms max=312.2ms  p(90)=50.23ms  p(95)=55.19ms  p(99.9)=79.98ms
     iterations.....................: 170823  1419.752371/s
     success_rate...................: 100.00% ✓ 170823      ✗ 0     
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

     checks.........................: 100.00% ✓ 184236     ✗ 0    
     data_received..................: 5.4 GB  45 MB/s
     data_sent......................: 74 MB   613 kB/s
     http_req_blocked...............: avg=7.79µs   min=1.1µs   med=3.32µs  max=9ms      p(90)=4.85µs   p(95)=5.51µs   p(99.9)=51.7µs  
     http_req_connecting............: avg=4.06µs   min=0s      med=0s      max=8.83ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=97.29ms  min=4.38ms  med=94.32ms max=338.46ms p(90)=116.98ms p(95)=128.56ms p(99.9)=227.94ms
       { expected_response:true }...: avg=97.29ms  min=4.38ms  med=94.32ms max=338.46ms p(90)=116.98ms p(95)=128.56ms p(99.9)=227.94ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 61512
     http_req_receiving.............: avg=124.38µs min=29.66µs med=77.52µs max=187.15ms p(90)=112.21µs p(95)=125.15µs p(99.9)=803.57µs
     http_req_sending...............: avg=25.23µs  min=5.57µs  med=15.07µs max=193.35ms p(90)=20.94µs  p(95)=23.04µs  p(99.9)=702.77µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=97.14ms  min=4.3ms   med=94.21ms max=337.79ms p(90)=116.82ms p(95)=128.31ms p(99.9)=225.06ms
     http_reqs......................: 61512   510.112929/s
     iteration_duration.............: avg=97.71ms  min=31.82ms med=94.58ms max=350.23ms p(90)=117.25ms p(95)=128.87ms p(99.9)=230.71ms
     iterations.....................: 61412   509.283639/s
     success_rate...................: 100.00% ✓ 61412      ✗ 0    
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

     checks.........................: 100.00% ✓ 162609     ✗ 0    
     data_received..................: 4.7 GB  39 MB/s
     data_sent......................: 65 MB   541 kB/s
     http_req_blocked...............: avg=5.19µs   min=1.53µs  med=3.77µs   max=2.75ms   p(90)=5.4µs    p(95)=6.03µs   p(99.9)=65.42µs 
     http_req_connecting............: avg=1.12µs   min=0s      med=0s       max=2.72ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=110.23ms min=4.96ms  med=108.02ms max=302.89ms p(90)=145.44ms p(95)=156.49ms p(99.9)=200.59ms
       { expected_response:true }...: avg=110.23ms min=4.96ms  med=108.02ms max=302.89ms p(90)=145.44ms p(95)=156.49ms p(99.9)=200.59ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 54303
     http_req_receiving.............: avg=93.26µs  min=34.45µs med=86.38µs  max=70.55ms  p(90)=118.12µs p(95)=130.75µs p(99.9)=580.72µs
     http_req_sending...............: avg=22.94µs  min=6.5µs   med=17.91µs  max=29.08ms  p(90)=23.26µs  p(95)=25.31µs  p(99.9)=572.99µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=110.11ms min=4.88ms  med=107.9ms  max=293.67ms p(90)=145.34ms p(95)=156.38ms p(99.9)=200.17ms
     http_reqs......................: 54303   450.089533/s
     iteration_duration.............: avg=110.72ms min=23.56ms med=108.35ms max=312.2ms  p(90)=145.74ms p(95)=156.81ms p(99.9)=202.73ms
     iterations.....................: 54203   449.260685/s
     success_rate...................: 100.00% ✓ 54203      ✗ 0    
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

     checks.........................: 100.00% ✓ 136998     ✗ 0    
     data_received..................: 4.0 GB  33 MB/s
     data_sent......................: 55 MB   455 kB/s
     http_req_blocked...............: avg=5.25µs   min=1.39µs  med=3.68µs   max=2.78ms   p(90)=5.19µs   p(95)=5.77µs   p(99.9)=188.88µs
     http_req_connecting............: avg=1.33µs   min=0s      med=0s       max=2.75ms   p(90)=0s       p(95)=0s       p(99.9)=131.06µs
     http_req_duration..............: avg=130.85ms min=5.7ms   med=128.15ms max=344.68ms p(90)=171.74ms p(95)=184.79ms p(99.9)=240.36ms
       { expected_response:true }...: avg=130.85ms min=5.7ms   med=128.15ms max=344.68ms p(90)=171.74ms p(95)=184.79ms p(99.9)=240.36ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 45766
     http_req_receiving.............: avg=87.02µs  min=32.65µs med=82.77µs  max=65.4ms   p(90)=113.04µs p(95)=124.6µs  p(99.9)=525.89µs
     http_req_sending...............: avg=33.13µs  min=6.1µs   med=17.09µs  max=145.36ms p(90)=21.98µs  p(95)=23.78µs  p(99.9)=526.02µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=130.73ms min=5.56ms  med=128.04ms max=344.36ms p(90)=171.63ms p(95)=184.66ms p(99.9)=240.04ms
     http_reqs......................: 45766   379.044944/s
     iteration_duration.............: avg=131.42ms min=24.77ms med=128.52ms max=353ms    p(90)=172.07ms p(95)=185.11ms p(99.9)=244.7ms 
     iterations.....................: 45666   378.21672/s
     success_rate...................: 100.00% ✓ 45666      ✗ 0    
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

     checks.........................: 100.00% ✓ 95937      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   318 kB/s
     http_req_blocked...............: avg=6.75µs   min=1.46µs  med=3.6µs    max=4.12ms   p(90)=5.04µs   p(95)=5.64µs   p(99.9)=1.22ms  
     http_req_connecting............: avg=2.87µs   min=0s      med=0s       max=4.08ms   p(90)=0s       p(95)=0s       p(99.9)=1.2ms   
     http_req_duration..............: avg=186.85ms min=7.78ms  med=185.92ms max=389.17ms p(90)=200.57ms p(95)=206.14ms p(99.9)=280.64ms
       { expected_response:true }...: avg=186.85ms min=7.78ms  med=185.92ms max=389.17ms p(90)=200.57ms p(95)=206.14ms p(99.9)=280.64ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32079
     http_req_receiving.............: avg=99.29µs  min=36.18µs med=89.46µs  max=102.57ms p(90)=120.27µs p(95)=131.34µs p(99.9)=620.36µs
     http_req_sending...............: avg=30.44µs  min=6.33µs  med=17.68µs  max=101.45ms p(90)=22.41µs  p(95)=24.29µs  p(99.9)=546.29µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=186.72ms min=7.63ms  med=185.8ms  max=366.64ms p(90)=200.45ms p(95)=206ms    p(99.9)=280.35ms
     http_reqs......................: 32079   265.179852/s
     iteration_duration.............: avg=187.73ms min=42.9ms  med=186.22ms max=397.96ms p(90)=200.86ms p(95)=206.47ms p(99.9)=281.58ms
     iterations.....................: 31979   264.353205/s
     success_rate...................: 100.00% ✓ 31979      ✗ 0    
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

     checks.........................: 100.00% ✓ 92598      ✗ 0    
     data_received..................: 2.7 GB  22 MB/s
     data_sent......................: 37 MB   308 kB/s
     http_req_blocked...............: avg=6.54µs   min=1.04µs  med=3.17µs   max=4.21ms   p(90)=4.52µs   p(95)=5.05µs   p(99.9)=1.5ms   
     http_req_connecting............: avg=3.2µs    min=0s      med=0s       max=4.17ms   p(90)=0s       p(95)=0s       p(99.9)=1.47ms  
     http_req_duration..............: avg=193.6ms  min=6.31ms  med=175.4ms  max=848.67ms p(90)=219.13ms p(95)=249.72ms p(99.9)=743.37ms
       { expected_response:true }...: avg=193.6ms  min=6.31ms  med=175.4ms  max=848.67ms p(90)=219.13ms p(95)=249.72ms p(99.9)=743.37ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 30966
     http_req_receiving.............: avg=92.22µs  min=32.54µs med=86.64µs  max=85.12ms  p(90)=116.44µs p(95)=128.1µs  p(99.9)=542.98µs
     http_req_sending...............: avg=36.58µs  min=5.31µs  med=16.32µs  max=124.89ms p(90)=20.56µs  p(95)=22.34µs  p(99.9)=572.98µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=193.47ms min=6.18ms  med=175.3ms  max=848.51ms p(90)=218.97ms p(95)=249.6ms  p(99.9)=743.27ms
     http_reqs......................: 30966   256.215829/s
     iteration_duration.............: avg=194.49ms min=50.7ms  med=175.76ms max=848.95ms p(90)=219.53ms p(95)=250.76ms p(99.9)=743.64ms
     iterations.....................: 30866   255.388419/s
     success_rate...................: 100.00% ✓ 30866      ✗ 0    
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

