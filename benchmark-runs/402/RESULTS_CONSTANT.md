## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s**.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly | 16.7.0-p.28 | 2,653 | 2,793 | 2,642 | 2.0% |  |
| fusion-nightly-net11 | 16.7.0-p.28 | 2,652 | 2,815 | 2,631 | 2.7% |  |
| fusion-nightly-fed | 16.7.0-p.28 | 2,571 | 2,708 | 2,553 | 2.1% |  |
| hive-router | v0.3.5 | 2,523 | 2,719 | 2,453 | 3.2% |  |
| fusion | 16.6.8 | 2,398 | 2,536 | 2,389 | 2.2% |  |
| grafbase | 0.53.5 | 1,679 | 1,736 | 1,671 | 1.3% |  |
| cosmo | 0.359.0 | 1,422 | 1,473 | 1,418 | 1.3% |  |
| caliban | 3.2.0 | 1,289 | 1,358 | 1,283 | 2.0% |  |
| feddi | e91d605ed222 | 1,131 | 1,174 | 1,116 | 1.7% |  |
| hive-gateway-router-runtime | 2.15.2 | 521 | 541 | 518 | 1.5% |  |
| apollo-router | v2.18.0 | 446 | 465 | 441 | 1.7% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 377 | 396 | 374 | 2.2% |  |
| apollo-gateway | 2.14.4 | 264 | 269 | 262 | 0.9% |  |
| hive-gateway | 2.15.2 | 261 | 268 | 261 | 0.9% |  |


### Details

<details>
  <summary>Summary for: fusion-nightly (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 956313      ✗ 0     
     data_received..................: 28 GB   233 MB/s
     data_sent......................: 383 MB  3.2 MB/s
     http_req_blocked...............: avg=2.89µs   min=882ns   med=2.11µs  max=19.32ms  p(90)=3.58µs  p(95)=4.3µs   p(99.9)=29.03µs 
     http_req_connecting............: avg=278ns    min=0s      med=0s      max=3.62ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=18.59ms  min=1.44ms  med=16.46ms max=274.71ms p(90)=29.16ms p(95)=34.88ms p(99.9)=101.46ms
       { expected_response:true }...: avg=18.59ms  min=1.44ms  med=16.46ms max=274.71ms p(90)=29.16ms p(95)=34.88ms p(99.9)=101.46ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 318871
     http_req_receiving.............: avg=647.16µs min=51.47µs med=91.52µs max=203.41ms p(90)=1.42ms  p(95)=2.56ms  p(99.9)=26.98ms 
     http_req_sending...............: avg=45.51µs  min=4.77µs  med=8.77µs  max=94.02ms  p(90)=17.01µs p(95)=92.74µs p(99.9)=4.72ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=17.9ms   min=1.36ms  med=15.84ms max=274.16ms p(90)=28.07ms p(95)=33.63ms p(99.9)=100.09ms
     http_reqs......................: 318871  2653.042724/s
     iteration_duration.............: avg=18.81ms  min=2.4ms   med=16.66ms max=295.2ms  p(90)=29.38ms p(95)=35.13ms p(99.9)=102.67ms
     iterations.....................: 318771  2652.210713/s
     success_rate...................: 100.00% ✓ 318771      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net11 (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 956229      ✗ 0     
     data_received..................: 28 GB   233 MB/s
     data_sent......................: 383 MB  3.2 MB/s
     http_req_blocked...............: avg=3.25µs  min=861ns   med=2.34µs   max=19.4ms   p(90)=3.98µs  p(95)=4.76µs  p(99.9)=33.97µs
     http_req_connecting............: avg=272ns   min=0s      med=0s       max=3.52ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=18.59ms min=1.43ms  med=17.58ms  max=272.24ms p(90)=26.66ms p(95)=30.27ms p(99.9)=52.82ms
       { expected_response:true }...: avg=18.59ms min=1.43ms  med=17.58ms  max=272.24ms p(90)=26.66ms p(95)=30.27ms p(99.9)=52.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 318843
     http_req_receiving.............: avg=1.11ms  min=51.85µs med=114.72µs max=184.52ms p(90)=3.02ms  p(95)=4.32ms  p(99.9)=26.8ms 
     http_req_sending...............: avg=50.12µs min=4.46µs  med=8.96µs   max=101.78ms p(90)=18.32µs p(95)=99.23µs p(99.9)=6.39ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.42ms min=1.32ms  med=16.42ms  max=271.64ms p(90)=25.07ms p(95)=28.7ms  p(99.9)=50.4ms 
     http_reqs......................: 318843  2652.980747/s
     iteration_duration.............: avg=18.81ms min=2.43ms  med=17.78ms  max=295.59ms p(90)=26.88ms p(95)=30.52ms p(99.9)=53.4ms 
     iterations.....................: 318743  2652.148683/s
     success_rate...................: 100.00% ✓ 318743      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 927054      ✗ 0     
     data_received..................: 27 GB   225 MB/s
     data_sent......................: 371 MB  3.1 MB/s
     http_req_blocked...............: avg=3.85µs  min=1.06µs  med=2.77µs  max=16.66ms  p(90)=4.6µs   p(95)=5.43µs   p(99.9)=40.77µs
     http_req_connecting............: avg=437ns   min=0s      med=0s      max=7.09ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=19.17ms min=1.69ms  med=17.32ms max=282.48ms p(90)=29.92ms p(95)=35.39ms  p(99.9)=77.16ms
       { expected_response:true }...: avg=19.17ms min=1.69ms  med=17.32ms max=282.48ms p(90)=29.92ms p(95)=35.39ms  p(99.9)=77.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 309118
     http_req_receiving.............: avg=636.3µs min=49.32µs med=98.05µs max=222.48ms p(90)=1.44ms  p(95)=2.62ms   p(99.9)=26.47ms
     http_req_sending...............: avg=52.27µs min=4.71µs  med=10.47µs max=106.92ms p(90)=21.05µs p(95)=111.71µs p(99.9)=4.97ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=18.48ms min=1.6ms   med=16.69ms max=273.88ms p(90)=28.9ms  p(95)=34.26ms  p(99.9)=75.98ms
     http_reqs......................: 309118  2571.057212/s
     iteration_duration.............: avg=19.4ms  min=2.8ms   med=17.54ms max=300.06ms p(90)=30.16ms p(95)=35.66ms  p(99.9)=78.09ms
     iterations.....................: 309018  2570.225472/s
     success_rate...................: 100.00% ✓ 309018      ✗ 0     
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

     checks.........................: 100.00% ✓ 909636      ✗ 0     
     data_received..................: 27 GB   221 MB/s
     data_sent......................: 365 MB  3.0 MB/s
     http_req_blocked...............: avg=3.75µs  min=1.02µs  med=2.72µs  max=17.11ms  p(90)=4.45µs  p(95)=5.27µs   p(99.9)=39.05µs
     http_req_connecting............: avg=343ns   min=0s      med=0s      max=4.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=19.55ms min=1.68ms  med=19.07ms max=274.54ms p(90)=27.31ms p(95)=30.06ms  p(99.9)=50.63ms
       { expected_response:true }...: avg=19.55ms min=1.68ms  med=19.07ms max=274.54ms p(90)=27.31ms p(95)=30.06ms  p(99.9)=50.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 303312
     http_req_receiving.............: avg=99.88µs min=25.29µs med=51.19µs max=149.87ms p(90)=94.91µs p(95)=155.75µs p(99.9)=8.34ms 
     http_req_sending...............: avg=47.46µs min=4.88µs  med=10.53µs max=47.14ms  p(90)=18.36µs p(95)=99.55µs  p(99.9)=5.07ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=19.4ms  min=1.58ms  med=18.94ms max=274.09ms p(90)=27.14ms p(95)=29.81ms  p(99.9)=49.9ms 
     http_reqs......................: 303312  2523.01436/s
     iteration_duration.............: avg=19.77ms min=2.95ms  med=19.28ms max=293.83ms p(90)=27.53ms p(95)=30.3ms   p(99.9)=51.08ms
     iterations.....................: 303212  2522.182539/s
     success_rate...................: 100.00% ✓ 303212      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 864525      ✗ 0     
     data_received..................: 25 GB   210 MB/s
     data_sent......................: 346 MB  2.9 MB/s
     http_req_blocked...............: avg=3.51µs   min=1.02µs  med=2.54µs  max=16.19ms  p(90)=4.03µs  p(95)=4.72µs  p(99.9)=37.74µs 
     http_req_connecting............: avg=311ns    min=0s      med=0s      max=3.53ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=20.59ms  min=1.58ms  med=17.31ms max=322.38ms p(90)=33.93ms p(95)=41.5ms  p(99.9)=139.64ms
       { expected_response:true }...: avg=20.59ms  min=1.58ms  med=17.31ms max=322.38ms p(90)=33.93ms p(95)=41.5ms  p(99.9)=139.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288275
     http_req_receiving.............: avg=621.26µs min=52.23µs med=98.57µs max=184.95ms p(90)=1.16ms  p(95)=2.1ms   p(99.9)=28.62ms 
     http_req_sending...............: avg=45.12µs  min=4.84µs  med=9.61µs  max=145.32ms p(90)=17.2µs  p(95)=94.21µs p(99.9)=3.74ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=19.92ms  min=1.49ms  med=16.73ms max=322.27ms p(90)=32.87ms p(95)=40.24ms p(99.9)=138.52ms
     http_reqs......................: 288275  2398.039257/s
     iteration_duration.............: avg=20.81ms  min=2.53ms  med=17.52ms max=322.59ms p(90)=34.15ms p(95)=41.75ms p(99.9)=140.71ms
     iterations.....................: 288175  2397.207398/s
     success_rate...................: 100.00% ✓ 288175      ✗ 0     
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

     checks.........................: 100.00% ✓ 605745      ✗ 0     
     data_received..................: 18 GB   147 MB/s
     data_sent......................: 243 MB  2.0 MB/s
     http_req_blocked...............: avg=3.48µs  min=821ns   med=2.29µs  max=7.38ms   p(90)=4.82µs  p(95)=5.95µs   p(99.9)=45.18µs
     http_req_connecting............: avg=428ns   min=0s      med=0s      max=5.31ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=29.45ms min=2.25ms  med=29.03ms max=279.4ms  p(90)=39.09ms p(95)=42.41ms  p(99.9)=64.03ms
       { expected_response:true }...: avg=29.45ms min=2.25ms  med=29.03ms max=279.4ms  p(90)=39.09ms p(95)=42.41ms  p(99.9)=64.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 202015
     http_req_receiving.............: avg=97.32µs min=26.44µs med=54.04µs max=121.95ms p(90)=125.6µs p(95)=214.34µs p(99.9)=4.91ms 
     http_req_sending...............: avg=46.33µs min=4.41µs  med=9.54µs  max=179.24ms p(90)=24µs    p(95)=116.2µs  p(99.9)=3.74ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=29.31ms min=2.15ms  med=28.9ms  max=278.96ms p(90)=38.93ms p(95)=42.23ms  p(99.9)=62.66ms
     http_reqs......................: 202015  1679.496743/s
     iteration_duration.............: avg=29.7ms  min=5.36ms  med=29.25ms max=320.15ms p(90)=39.32ms p(95)=42.63ms  p(99.9)=64.55ms
     iterations.....................: 201915  1678.66537/s
     success_rate...................: 100.00% ✓ 201915      ✗ 0     
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

     checks.........................: 100.00% ✓ 513081      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 206 MB  1.7 MB/s
     http_req_blocked...............: avg=4.09µs  min=912ns   med=2.42µs  max=9.67ms   p(90)=4.21µs   p(95)=4.96µs   p(99.9)=32.37µs
     http_req_connecting............: avg=1.19µs  min=0s      med=0s      max=9.64ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.84ms min=2.41ms  med=33.88ms max=291.86ms p(90)=49.88ms  p(95)=54.93ms  p(99.9)=79.22ms
       { expected_response:true }...: avg=34.84ms min=2.41ms  med=33.88ms max=291.86ms p(90)=49.88ms  p(95)=54.93ms  p(99.9)=79.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 171127
     http_req_receiving.............: avg=78.91µs min=24.91µs med=60.83µs max=165.25ms p(90)=102.46µs p(95)=122.12µs p(99.9)=1.2ms  
     http_req_sending...............: avg=27.12µs min=4.53µs  med=10.44µs max=177.79ms p(90)=18.13µs  p(95)=22.8µs   p(99.9)=1.21ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.73ms min=2.34ms  med=33.78ms max=283.76ms p(90)=49.76ms  p(95)=54.83ms  p(99.9)=78.88ms
     http_reqs......................: 171127  1422.412737/s
     iteration_duration.............: avg=35.07ms min=4.62ms  med=34.09ms max=306.05ms p(90)=50.09ms  p(95)=55.15ms  p(99.9)=79.67ms
     iterations.....................: 171027  1421.581534/s
     success_rate...................: 100.00% ✓ 171027      ✗ 0     
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

     checks.........................: 100.00% ✓ 465405      ✗ 0     
     data_received..................: 14 GB   113 MB/s
     data_sent......................: 187 MB  1.5 MB/s
     http_req_blocked...............: avg=4.15µs  min=1.06µs  med=3.15µs  max=10.14ms  p(90)=4.83µs   p(95)=5.57µs   p(99.9)=41.2µs 
     http_req_connecting............: avg=595ns   min=0s      med=0s      max=4.5ms    p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=38.41ms min=2.76ms  med=37.32ms max=283.79ms p(90)=54.86ms  p(95)=60.6ms   p(99.9)=90.68ms
       { expected_response:true }...: avg=38.41ms min=2.76ms  med=37.32ms max=283.79ms p(90)=54.86ms  p(95)=60.6ms   p(99.9)=90.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 155235
     http_req_receiving.............: avg=79.21µs min=28.55µs med=64.05µs max=111ms    p(90)=101.67µs p(95)=119.05µs p(99.9)=1.21ms 
     http_req_sending...............: avg=27.51µs min=5.47µs  med=13.05µs max=103.22ms p(90)=19.65µs  p(95)=23.59µs  p(99.9)=1.12ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=38.3ms  min=2.66ms  med=37.22ms max=283.01ms p(90)=54.75ms  p(95)=60.48ms  p(99.9)=90.33ms
     http_reqs......................: 155235  1289.955448/s
     iteration_duration.............: avg=38.66ms min=6.45ms  med=37.55ms max=296.16ms p(90)=55.09ms  p(95)=60.82ms  p(99.9)=91.2ms 
     iterations.....................: 155135  1289.124479/s
     success_rate...................: 100.00% ✓ 155135      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 407889      ✗ 0     
     data_received..................: 12 GB   99 MB/s
     data_sent......................: 164 MB  1.4 MB/s
     http_req_blocked...............: avg=4.1µs   min=1.03µs  med=3.12µs  max=3.87ms   p(90)=4.81µs   p(95)=5.53µs   p(99.9)=37.98µs 
     http_req_connecting............: avg=692ns   min=0s      med=0s      max=3.83ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=43.85ms min=1.82ms  med=43.5ms  max=304.17ms p(90)=63.06ms  p(95)=69.93ms  p(99.9)=105.63ms
       { expected_response:true }...: avg=43.85ms min=1.82ms  med=43.5ms  max=304.17ms p(90)=63.06ms  p(95)=69.93ms  p(99.9)=105.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 136063
     http_req_receiving.............: avg=79.91µs min=27.28µs med=63.33µs max=98.42ms  p(90)=101.92µs p(95)=118.72µs p(99.9)=1.86ms  
     http_req_sending...............: avg=27.11µs min=5.15µs  med=12.98µs max=132.88ms p(90)=20.13µs  p(95)=23.74µs  p(99.9)=1.03ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=43.74ms min=1.72ms  med=43.4ms  max=301.25ms p(90)=62.96ms  p(95)=69.82ms  p(99.9)=105.22ms
     http_reqs......................: 136063  1131.340417/s
     iteration_duration.............: avg=44.12ms min=2.84ms  med=43.75ms max=315.83ms p(90)=63.29ms  p(95)=70.17ms  p(99.9)=106.29ms
     iterations.....................: 135963  1130.508934/s
     success_rate...................: 100.00% ✓ 135963      ✗ 0     
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

     checks.........................: 100.00% ✓ 188220     ✗ 0    
     data_received..................: 5.5 GB  46 MB/s
     data_sent......................: 76 MB   626 kB/s
     http_req_blocked...............: avg=4.09µs  min=951ns   med=2.91µs  max=2.8ms    p(90)=4.39µs   p(95)=4.97µs   p(99.9)=52.13µs 
     http_req_connecting............: avg=984ns   min=0s      med=0s      max=2.77ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=95.24ms min=4.58ms  med=92.56ms max=297.67ms p(90)=114.49ms p(95)=125.24ms p(99.9)=219.33ms
       { expected_response:true }...: avg=95.24ms min=4.58ms  med=92.56ms max=297.67ms p(90)=114.49ms p(95)=125.24ms p(99.9)=219.33ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 62840
     http_req_receiving.............: avg=83.53µs min=27.23µs med=74.71µs max=79.89ms  p(90)=109.05µs p(95)=121.97µs p(99.9)=619.49µs
     http_req_sending...............: avg=20.66µs min=4.81µs  med=14.48µs max=55.47ms  p(90)=20.34µs  p(95)=22.38µs  p(99.9)=574.34µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=95.14ms min=4.51ms  med=92.45ms max=297.58ms p(90)=114.37ms p(95)=125.12ms p(99.9)=218.97ms
     http_reqs......................: 62840   521.053193/s
     iteration_duration.............: avg=95.65ms min=34.69ms med=92.82ms max=309.84ms p(90)=114.77ms p(95)=125.53ms p(99.9)=221.16ms
     iterations.....................: 62740   520.224019/s
     success_rate...................: 100.00% ✓ 62740      ✗ 0    
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

     checks.........................: 100.00% ✓ 161223     ✗ 0    
     data_received..................: 4.7 GB  39 MB/s
     data_sent......................: 65 MB   536 kB/s
     http_req_blocked...............: avg=8.81µs   min=1.18µs  med=3.24µs   max=8.49ms   p(90)=4.79µs   p(95)=5.34µs   p(99.9)=128.49µs
     http_req_connecting............: avg=5.24µs   min=0s      med=0s       max=8.34ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=111.19ms min=5.17ms  med=109.05ms max=319.38ms p(90)=146.94ms p(95)=157.94ms p(99.9)=201.36ms
       { expected_response:true }...: avg=111.19ms min=5.17ms  med=109.05ms max=319.38ms p(90)=146.94ms p(95)=157.94ms p(99.9)=201.36ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 53841
     http_req_receiving.............: avg=87.31µs  min=28.17µs med=81.18µs  max=117.1ms  p(90)=111.12µs p(95)=123.03µs p(99.9)=541.12µs
     http_req_sending...............: avg=25.82µs  min=5.11µs  med=16.44µs  max=103.03ms p(90)=21.63µs  p(95)=23.47µs  p(99.9)=1.17ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=111.07ms min=5ms     med=108.94ms max=318.61ms p(90)=146.82ms p(95)=157.82ms p(99.9)=200.68ms
     http_reqs......................: 53841   446.249191/s
     iteration_duration.............: avg=111.67ms min=27.32ms med=109.37ms max=333.5ms  p(90)=147.23ms p(95)=158.33ms p(99.9)=203.58ms
     iterations.....................: 53741   445.420363/s
     success_rate...................: 100.00% ✓ 53741      ✗ 0    
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

     checks.........................: 100.00% ✓ 136512     ✗ 0    
     data_received..................: 4.0 GB  33 MB/s
     data_sent......................: 55 MB   454 kB/s
     http_req_blocked...............: avg=5.63µs   min=1.41µs  med=3.55µs   max=4.1ms    p(90)=5.01µs   p(95)=5.63µs   p(99.9)=358.68µs
     http_req_connecting............: avg=1.83µs   min=0s      med=0s       max=4.06ms   p(90)=0s       p(95)=0s       p(99.9)=328.9µs 
     http_req_duration..............: avg=131.34ms min=6.2ms   med=128.88ms max=327.18ms p(90)=171.88ms p(95)=185.21ms p(99.9)=241.89ms
       { expected_response:true }...: avg=131.34ms min=6.2ms   med=128.88ms max=327.18ms p(90)=171.88ms p(95)=185.21ms p(99.9)=241.89ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 45604
     http_req_receiving.............: avg=89.98µs  min=31.64µs med=83.44µs  max=114.14ms p(90)=113.85µs p(95)=125.6µs  p(99.9)=541.56µs
     http_req_sending...............: avg=24.99µs  min=5.92µs  med=17.47µs  max=72.55ms  p(90)=22.53µs  p(95)=24.41µs  p(99.9)=581.59µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=131.22ms min=5.99ms  med=128.78ms max=327.02ms p(90)=171.76ms p(95)=185.09ms p(99.9)=241.4ms 
     http_reqs......................: 45604   377.67788/s
     iteration_duration.............: avg=131.89ms min=27.62ms med=129.24ms max=341.9ms  p(90)=172.19ms p(95)=185.56ms p(99.9)=243.98ms
     iterations.....................: 45504   376.849711/s
     success_rate...................: 100.00% ✓ 45504      ✗ 0    
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

     checks.........................: 100.00% ✓ 95538      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   317 kB/s
     http_req_blocked...............: avg=6.83µs   min=1.24µs  med=3.61µs   max=4.28ms   p(90)=4.99µs   p(95)=5.56µs   p(99.9)=1.37ms  
     http_req_connecting............: avg=2.94µs   min=0s      med=0s       max=4.23ms   p(90)=0s       p(95)=0s       p(99.9)=1.24ms  
     http_req_duration..............: avg=187.64ms min=7.92ms  med=186.54ms max=405.76ms p(90)=198.19ms p(95)=202.97ms p(99.9)=277.88ms
       { expected_response:true }...: avg=187.64ms min=7.92ms  med=186.54ms max=405.76ms p(90)=198.19ms p(95)=202.97ms p(99.9)=277.88ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31946
     http_req_receiving.............: avg=98.14µs  min=33.49µs med=87.52µs  max=141.57ms p(90)=118.2µs  p(95)=129.89µs p(99.9)=570.16µs
     http_req_sending...............: avg=31.09µs  min=5.09µs  med=17.11µs  max=98.92ms  p(90)=21.85µs  p(95)=23.67µs  p(99.9)=525.61µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=187.51ms min=7.77ms  med=186.42ms max=405.19ms p(90)=198.06ms p(95)=202.85ms p(99.9)=277.72ms
     http_reqs......................: 31946   264.002796/s
     iteration_duration.............: avg=188.53ms min=48.96ms med=186.87ms max=426.5ms  p(90)=198.47ms p(95)=203.27ms p(99.9)=284.59ms
     iterations.....................: 31846   263.176393/s
     success_rate...................: 100.00% ✓ 31846      ✗ 0    
     vus............................: 12      min=12       max=50 
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

     checks.........................: 100.00% ✓ 94734      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   314 kB/s
     http_req_blocked...............: avg=6.7µs    min=1.15µs  med=3.3µs    max=4.1ms    p(90)=4.69µs   p(95)=5.29µs   p(99.9)=1.58ms  
     http_req_connecting............: avg=3.2µs    min=0s      med=0s       max=4.06ms   p(90)=0s       p(95)=0s       p(99.9)=1.56ms  
     http_req_duration..............: avg=189.25ms min=6.11ms  med=172.61ms max=706.76ms p(90)=218.04ms p(95)=262.54ms p(99.9)=596.95ms
       { expected_response:true }...: avg=189.25ms min=6.11ms  med=172.61ms max=706.76ms p(90)=218.04ms p(95)=262.54ms p(99.9)=596.95ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31678
     http_req_receiving.............: avg=96.92µs  min=32.26µs med=91.25µs  max=20.8ms   p(90)=122.5µs  p(95)=135.42µs p(99.9)=1.15ms  
     http_req_sending...............: avg=28.73µs  min=5.36µs  med=17.39µs  max=178.03ms p(90)=21.8µs   p(95)=23.66µs  p(99.9)=524.99µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=189.12ms min=5.98ms  med=172.5ms  max=706.64ms p(90)=217.9ms  p(95)=262.39ms p(99.9)=596.86ms
     http_reqs......................: 31678   261.824835/s
     iteration_duration.............: avg=190.12ms min=44.48ms med=172.97ms max=707.03ms p(90)=218.45ms p(95)=264.04ms p(99.9)=597.22ms
     iterations.....................: 31578   260.998316/s
     success_rate...................: 100.00% ✓ 31578      ✗ 0    
     vus............................: 2       min=2        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

