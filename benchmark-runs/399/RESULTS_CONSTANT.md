## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 2 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 1 runs are measured. Results are ranked by **median RPS** across the 1 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s**.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| hive-router | v0.3.5 | 2,740 | 2,740 | 2,740 | 0.0% |  |
| fusion-nightly-net-11 | 16.7.0-p.27 | 2,643 | 2,643 | 2,643 | 0.0% |  |
| fusion-nightly-net-10 | 16.7.0-p.27 | 2,615 | 2,615 | 2,615 | 0.0% |  |
| fusion-net-10 | 16.6.8 | 2,575 | 2,575 | 2,575 | 0.0% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.27 | 2,337 | 2,337 | 2,337 | 0.0% |  |
| grafbase | 0.53.5 | 1,727 | 1,727 | 1,727 | 0.0% |  |
| cosmo | 0.359.0 | 1,502 | 1,502 | 1,502 | 0.0% |  |
| caliban | 3.2.0 | 1,438 | 1,438 | 1,438 | 0.0% |  |
| feddi-gateway | e91d605ed222 | 1,157 | 1,157 | 1,157 | 0.0% |  |
| hive-gateway-router-runtime | 2.15.2 | 527 | 527 | 527 | 0.0% |  |
| apollo-router | v2.18.0 | 456 | 456 | 456 | 0.0% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 430 | 430 | 430 | 0.0% |  |
| apollo-gateway | 2.14.4 | 279 | 279 | 279 | 0.0% |  |
| hive-gateway | 2.15.2 | 276 | 276 | 276 | 0.0% |  |


### Details

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 987741      ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 396 MB  3.3 MB/s
     http_req_blocked...............: avg=2.74µs  min=882ns   med=2.11µs  max=7.91ms   p(90)=3.46µs  p(95)=4.16µs   p(99.9)=29.38µs
     http_req_connecting............: avg=283ns   min=0s      med=0s      max=4.08ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=18.01ms min=1.35ms  med=17.93ms max=276.04ms p(90)=24.44ms p(95)=26.3ms   p(99.9)=42.12ms
       { expected_response:true }...: avg=18.01ms min=1.35ms  med=17.93ms max=276.04ms p(90)=24.44ms p(95)=26.3ms   p(99.9)=42.12ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 329347
     http_req_receiving.............: avg=71.38µs min=24.51µs med=48.92µs max=78.18ms  p(90)=85.95µs p(95)=123.73µs p(99.9)=1.7ms  
     http_req_sending...............: avg=35.39µs min=4.59µs  med=9.17µs  max=245.13ms p(90)=16.11µs p(95)=85.97µs  p(99.9)=1.5ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.9ms  min=1.3ms   med=17.83ms max=275.67ms p(90)=24.33ms p(95)=26.18ms  p(99.9)=41.14ms
     http_reqs......................: 329347  2740.355752/s
     iteration_duration.............: avg=18.21ms min=3.05ms  med=18.12ms max=293.87ms p(90)=24.63ms p(95)=26.5ms   p(99.9)=42.66ms
     iterations.....................: 329247  2739.523694/s
     success_rate...................: 100.00% ✓ 329247      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.27)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 952764      ✗ 0     
     data_received..................: 28 GB   232 MB/s
     data_sent......................: 382 MB  3.2 MB/s
     http_req_blocked...............: avg=3.24µs  min=992ns   med=2.53µs   max=11.68ms  p(90)=4.11µs  p(95)=4.86µs   p(99.9)=33.3µs 
     http_req_connecting............: avg=273ns   min=0s      med=0s       max=3.55ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=18.65ms min=1.37ms  med=17.73ms  max=280.52ms p(90)=26.73ms p(95)=30.1ms   p(99.9)=50.23ms
       { expected_response:true }...: avg=18.65ms min=1.37ms  med=17.73ms  max=280.52ms p(90)=26.73ms p(95)=30.1ms   p(99.9)=50.23ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 317688
     http_req_receiving.............: avg=1.13ms  min=51.08µs med=304.11µs max=113.91ms p(90)=2.89ms  p(95)=3.81ms   p(99.9)=19.29ms
     http_req_sending...............: avg=40.79µs min=4.7µs   med=9.63µs   max=119.93ms p(90)=20.05µs p(95)=104.64µs p(99.9)=2.72ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.48ms min=1.3ms   med=16.51ms  max=279.88ms p(90)=25.31ms p(95)=28.64ms  p(99.9)=47.93ms
     http_reqs......................: 317688  2643.297868/s
     iteration_duration.............: avg=18.88ms min=2.42ms  med=17.94ms  max=300.29ms p(90)=26.94ms p(95)=30.33ms  p(99.9)=50.91ms
     iterations.....................: 317588  2642.465826/s
     success_rate...................: 100.00% ✓ 317588      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-10 (HotChocolate subgraphs) (16.7.0-p.27)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 942792      ✗ 0     
     data_received..................: 28 GB   229 MB/s
     data_sent......................: 378 MB  3.1 MB/s
     http_req_blocked...............: avg=2.68µs   min=901ns   med=2.05µs  max=8.82ms   p(90)=3.36µs   p(95)=4µs     p(99.9)=26.1µs  
     http_req_connecting............: avg=282ns    min=0s      med=0s      max=3.46ms   p(90)=0s       p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=18.88ms  min=1.49ms  med=15.67ms max=365.83ms p(90)=30.79ms  p(95)=37.98ms p(99.9)=150.99ms
       { expected_response:true }...: avg=18.88ms  min=1.49ms  med=15.67ms max=365.83ms p(90)=30.79ms  p(95)=37.98ms p(99.9)=150.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 314364
     http_req_receiving.............: avg=526.58µs min=47.87µs med=93.49µs max=282.76ms p(90)=981.17µs p(95)=1.59ms  p(99.9)=24.64ms 
     http_req_sending...............: avg=34.17µs  min=4.59µs  med=8.63µs  max=287.58ms p(90)=15.79µs  p(95)=83.16µs p(99.9)=1.67ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=18.31ms  min=1.4ms   med=15.21ms max=363.89ms p(90)=29.94ms  p(95)=36.98ms p(99.9)=146.15ms
     http_reqs......................: 314364  2615.227033/s
     iteration_duration.............: avg=19.08ms  min=2.59ms  med=15.86ms max=366.01ms p(90)=30.99ms  p(95)=38.19ms p(99.9)=151.26ms
     iterations.....................: 314264  2614.395122/s
     success_rate...................: 100.00% ✓ 314264      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-10 (HotChocolate subgraphs) (16.6.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 928647      ✗ 0     
     data_received..................: 27 GB   226 MB/s
     data_sent......................: 372 MB  3.1 MB/s
     http_req_blocked...............: avg=3.23µs   min=962ns   med=2.61µs   max=3.46ms   p(90)=4.1µs   p(95)=4.78µs  p(99.9)=35.1µs  
     http_req_connecting............: avg=283ns    min=0s      med=0s       max=3.42ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=19.15ms  min=1.49ms  med=16.07ms  max=308.99ms p(90)=31.21ms p(95)=38.39ms p(99.9)=143.47ms
       { expected_response:true }...: avg=19.15ms  min=1.49ms  med=16.07ms  max=308.99ms p(90)=31.21ms p(95)=38.39ms p(99.9)=143.47ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 309649
     http_req_receiving.............: avg=538.44µs min=49.83µs med=100.44µs max=273.95ms p(90)=1.03ms  p(95)=1.7ms   p(99.9)=24.77ms 
     http_req_sending...............: avg=37.71µs  min=4.57µs  med=9.93µs   max=105.41ms p(90)=17.76µs p(95)=97.56µs p(99.9)=1.88ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=18.58ms  min=1.4ms   med=15.57ms  max=308.88ms p(90)=30.32ms p(95)=37.36ms p(99.9)=141.84ms
     http_reqs......................: 309649  2575.884677/s
     iteration_duration.............: avg=19.37ms  min=2.41ms  med=16.27ms  max=309.25ms p(90)=31.42ms p(95)=38.63ms p(99.9)=144.53ms
     iterations.....................: 309549  2575.052804/s
     success_rate...................: 100.00% ✓ 309549      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-10 (HotChocolate subgraphs) (16.7.0-p.27)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 842970      ✗ 0     
     data_received..................: 25 GB   205 MB/s
     data_sent......................: 338 MB  2.8 MB/s
     http_req_blocked...............: avg=6.51µs   min=842ns   med=2.13µs   max=50.92ms  p(90)=3.58µs  p(95)=4.23µs  p(99.9)=27.59µs 
     http_req_connecting............: avg=4.02µs   min=0s      med=0s       max=50.73ms  p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=21.13ms  min=1.7ms   med=17.7ms   max=382.26ms p(90)=34.34ms p(95)=42.61ms p(99.9)=161.24ms
       { expected_response:true }...: avg=21.13ms  min=1.7ms   med=17.7ms   max=382.26ms p(90)=34.34ms p(95)=42.61ms p(99.9)=161.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 281090
     http_req_receiving.............: avg=576.17µs min=50.33µs med=103.24µs max=366.12ms p(90)=1.07ms  p(95)=1.76ms  p(99.9)=27.41ms 
     http_req_sending...............: avg=32.88µs  min=4.51µs  med=8.92µs   max=112.47ms p(90)=16.44µs p(95)=41.88µs p(99.9)=1.71ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=20.52ms  min=1.6ms   med=17.19ms  max=355.1ms  p(90)=33.39ms p(95)=41.47ms p(99.9)=159.7ms 
     http_reqs......................: 281090  2337.80514/s
     iteration_duration.............: avg=21.34ms  min=2.81ms  med=17.9ms   max=382.44ms p(90)=34.55ms p(95)=42.82ms p(99.9)=162.67ms
     iterations.....................: 280990  2336.973447/s
     success_rate...................: 100.00% ✓ 280990      ✗ 0     
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

     checks.........................: 100.00% ✓ 622908      ✗ 0     
     data_received..................: 18 GB   151 MB/s
     data_sent......................: 250 MB  2.1 MB/s
     http_req_blocked...............: avg=3.46µs  min=822ns   med=2.15µs  max=4.92ms   p(90)=4.3µs    p(95)=5.38µs   p(99.9)=38.81µs
     http_req_connecting............: avg=748ns   min=0s      med=0s      max=4.9ms    p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=28.65ms min=1.98ms  med=28.2ms  max=288.49ms p(90)=37.71ms  p(95)=40.69ms  p(99.9)=57.91ms
       { expected_response:true }...: avg=28.65ms min=1.98ms  med=28.2ms  max=288.49ms p(90)=37.71ms  p(95)=40.69ms  p(99.9)=57.91ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 207736
     http_req_receiving.............: avg=84.85µs min=26.83µs med=53.39µs max=69.1ms   p(90)=121.67µs p(95)=201.04µs p(99.9)=2.17ms 
     http_req_sending...............: avg=37.47µs min=4.26µs  med=8.9µs   max=241.84ms p(90)=22.78µs  p(95)=106.42µs p(99.9)=2.7ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=28.53ms min=1.93ms  med=28.09ms max=285.39ms p(90)=37.59ms  p(95)=40.54ms  p(99.9)=57.33ms
     http_reqs......................: 207736  1727.306626/s
     iteration_duration.............: avg=28.88ms min=6.7ms   med=28.42ms max=302.61ms p(90)=37.93ms  p(95)=40.9ms   p(99.9)=58.35ms
     iterations.....................: 207636  1726.475135/s
     success_rate...................: 100.00% ✓ 207636      ✗ 0     
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

     checks.........................: 100.00% ✓ 541926      ✗ 0     
     data_received..................: 16 GB   132 MB/s
     data_sent......................: 217 MB  1.8 MB/s
     http_req_blocked...............: avg=4.74µs  min=1.1µs   med=2.69µs  max=23.16ms  p(90)=4.27µs  p(95)=5µs      p(99.9)=34.66µs 
     http_req_connecting............: avg=1.7µs   min=0s      med=0s      max=23.06ms  p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.97ms min=2.08ms  med=32.07ms max=290.93ms p(90)=47.26ms p(95)=52.11ms  p(99.9)=74.02ms 
       { expected_response:true }...: avg=32.97ms min=2.08ms  med=32.07ms max=290.93ms p(90)=47.26ms p(95)=52.11ms  p(99.9)=74.02ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 180742
     http_req_receiving.............: avg=86.37µs min=27.02µs med=61.43µs max=176.65ms p(90)=98.69µs p(95)=115.42µs p(99.9)=872.14µs
     http_req_sending...............: avg=27.75µs min=4.95µs  med=11.06µs max=107.35ms p(90)=17.36µs p(95)=21.86µs  p(99.9)=967.1µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.86ms min=2.03ms  med=31.97ms max=209.91ms p(90)=47.15ms p(95)=52ms     p(99.9)=73.44ms 
     http_reqs......................: 180742  1502.759591/s
     iteration_duration.............: avg=33.2ms  min=3.95ms  med=32.28ms max=309.14ms p(90)=47.47ms p(95)=52.32ms  p(99.9)=74.33ms 
     iterations.....................: 180642  1501.928152/s
     success_rate...................: 100.00% ✓ 180642      ✗ 0     
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

     checks.........................: 100.00% ✓ 518682      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 208 MB  1.7 MB/s
     http_req_blocked...............: avg=3.3µs   min=982ns   med=2.46µs  max=4.16ms   p(90)=4.15µs  p(95)=4.89µs   p(99.9)=32.45µs 
     http_req_connecting............: avg=505ns   min=0s      med=0s      max=4.12ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.46ms min=2.2ms   med=33.5ms  max=248.98ms p(90)=48.91ms p(95)=54.03ms  p(99.9)=81.6ms  
       { expected_response:true }...: avg=34.46ms min=2.2ms   med=33.5ms  max=248.98ms p(90)=48.91ms p(95)=54.03ms  p(99.9)=81.6ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 172994
     http_req_receiving.............: avg=70.84µs min=26.52µs med=57.48µs max=146.76ms p(90)=94.14µs p(95)=110.95µs p(99.9)=902.41µs
     http_req_sending...............: avg=24.23µs min=4.9µs   med=11.21µs max=157.5ms  p(90)=18.12µs p(95)=21.86µs  p(99.9)=833.17µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.37ms min=2.14ms  med=33.41ms max=248.28ms p(90)=48.81ms p(95)=53.93ms  p(99.9)=80.96ms 
     http_reqs......................: 172994  1438.137474/s
     iteration_duration.............: avg=34.69ms min=6.23ms  med=33.71ms max=318.03ms p(90)=49.11ms p(95)=54.24ms  p(99.9)=81.86ms 
     iterations.....................: 172894  1437.306152/s
     success_rate...................: 100.00% ✓ 172894      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (e91d605ed222)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 417312      ✗ 0     
     data_received..................: 12 GB   101 MB/s
     data_sent......................: 167 MB  1.4 MB/s
     http_req_blocked...............: avg=3.93µs  min=1.06µs  med=3.03µs  max=3.57ms   p(90)=4.52µs  p(95)=5.16µs   p(99.9)=39.11µs 
     http_req_connecting............: avg=634ns   min=0s      med=0s      max=3.53ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=42.86ms min=1.71ms  med=42.42ms max=303.43ms p(90)=62.37ms p(95)=69.08ms  p(99.9)=106.96ms
       { expected_response:true }...: avg=42.86ms min=1.71ms  med=42.42ms max=303.43ms p(90)=62.37ms p(95)=69.08ms  p(99.9)=106.96ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 139204
     http_req_receiving.............: avg=76.44µs min=27.34µs med=59.97µs max=120.25ms p(90)=96.56µs p(95)=111.93µs p(99.9)=1.66ms  
     http_req_sending...............: avg=24.15µs min=5.05µs  med=12.46µs max=178.61ms p(90)=18.66µs p(95)=21.88µs  p(99.9)=763.48µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=42.76ms min=1.63ms  med=42.32ms max=302.85ms p(90)=62.28ms p(95)=68.98ms  p(99.9)=106.52ms
     http_reqs......................: 139204  1157.404491/s
     iteration_duration.............: avg=43.12ms min=2.84ms  med=42.65ms max=312.76ms p(90)=62.6ms  p(95)=69.31ms  p(99.9)=107.48ms
     iterations.....................: 139104  1156.573047/s
     success_rate...................: 100.00% ✓ 139104      ✗ 0     
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

     checks.........................: 100.00% ✓ 190389     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 76 MB   633 kB/s
     http_req_blocked...............: avg=5.13µs  min=1.14µs  med=3.05µs  max=4.24ms   p(90)=4.49µs   p(95)=5.12µs   p(99.9)=45.72µs 
     http_req_connecting............: avg=1.81µs  min=0s      med=0s      max=4.2ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=94.16ms min=4.12ms  med=91.4ms  max=322.85ms p(90)=113.23ms p(95)=123.65ms p(99.9)=221.54ms
       { expected_response:true }...: avg=94.16ms min=4.12ms  med=91.4ms  max=322.85ms p(90)=113.23ms p(95)=123.65ms p(99.9)=221.54ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63563
     http_req_receiving.............: avg=79.12µs min=30.45µs med=70.68µs max=66.33ms  p(90)=103.16µs p(95)=115.32µs p(99.9)=583.76µs
     http_req_sending...............: avg=24.49µs min=5.29µs  med=14.03µs max=172.31ms p(90)=19.69µs  p(95)=21.72µs  p(99.9)=653.53µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.06ms min=4.05ms  med=91.31ms max=322.68ms p(90)=113.13ms p(95)=123.53ms p(99.9)=220.68ms
     http_reqs......................: 63563   527.276683/s
     iteration_duration.............: avg=94.55ms min=19.62ms med=91.66ms max=339.17ms p(90)=113.48ms p(95)=123.93ms p(99.9)=223.85ms
     iterations.....................: 63463   526.447149/s
     success_rate...................: 100.00% ✓ 63463      ✗ 0    
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

     checks.........................: 100.00% ✓ 164931     ✗ 0    
     data_received..................: 4.8 GB  40 MB/s
     data_sent......................: 66 MB   548 kB/s
     http_req_blocked...............: avg=4.81µs   min=1.07µs  med=2.9µs    max=3.7ms    p(90)=4.3µs    p(95)=4.84µs   p(99.9)=60.57µs 
     http_req_connecting............: avg=1.71µs   min=0s      med=0s       max=3.66ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=108.71ms min=4.83ms  med=106.51ms max=310.82ms p(90)=144.07ms p(95)=155.13ms p(99.9)=198.91ms
       { expected_response:true }...: avg=108.71ms min=4.83ms  med=106.51ms max=310.82ms p(90)=144.07ms p(95)=155.13ms p(99.9)=198.91ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 55077
     http_req_receiving.............: avg=80.69µs  min=28.29µs med=73.19µs  max=75.91ms  p(90)=104.27µs p(95)=116.69µs p(99.9)=514.63µs
     http_req_sending...............: avg=20.82µs  min=5.15µs  med=14.85µs  max=42.01ms  p(90)=20.15µs  p(95)=21.94µs  p(99.9)=467.43µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=108.61ms min=4.71ms  med=106.41ms max=310.54ms p(90)=143.97ms p(95)=155.03ms p(99.9)=198.79ms
     http_reqs......................: 55077   456.625672/s
     iteration_duration.............: avg=109.16ms min=28.18ms med=106.81ms max=321.51ms p(90)=144.34ms p(95)=155.41ms p(99.9)=201.41ms
     iterations.....................: 54977   455.796604/s
     success_rate...................: 100.00% ✓ 54977      ✗ 0    
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

     checks.........................: 100.00% ✓ 155373     ✗ 0    
     data_received..................: 4.5 GB  38 MB/s
     data_sent......................: 62 MB   516 kB/s
     http_req_blocked...............: avg=6.17µs   min=1.23µs  med=3.51µs   max=4.62ms   p(90)=5.02µs   p(95)=5.62µs   p(99.9)=124.66µs
     http_req_connecting............: avg=2.41µs   min=0s      med=0s       max=4.58ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=115.39ms min=5.48ms  med=113.14ms max=318.95ms p(90)=150.72ms p(95)=162.72ms p(99.9)=210.4ms 
       { expected_response:true }...: avg=115.39ms min=5.48ms  med=113.14ms max=318.95ms p(90)=150.72ms p(95)=162.72ms p(99.9)=210.4ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 51891
     http_req_receiving.............: avg=81.86µs  min=29.54µs med=77.81µs  max=62.54ms  p(90)=106.61µs p(95)=117.88µs p(99.9)=522.22µs
     http_req_sending...............: avg=23.84µs  min=5.73µs  med=16.49µs  max=55.63ms  p(90)=21.62µs  p(95)=23.51µs  p(99.9)=625.42µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=115.29ms min=5.38ms  med=113.03ms max=317.4ms  p(90)=150.62ms p(95)=162.61ms p(99.9)=209.9ms 
     http_reqs......................: 51891   430.01891/s
     iteration_duration.............: avg=115.87ms min=31.13ms med=113.45ms max=332.57ms p(90)=151.04ms p(95)=163.06ms p(99.9)=212.56ms
     iterations.....................: 51791   429.190213/s
     success_rate...................: 100.00% ✓ 51791      ✗ 0    
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

     checks.........................: 100.00% ✓ 101070    ✗ 0    
     data_received..................: 3.0 GB  25 MB/s
     data_sent......................: 41 MB   335 kB/s
     http_req_blocked...............: avg=11.99µs  min=1.34µs  med=3.49µs   max=9.35ms   p(90)=4.88µs   p(95)=5.48µs   p(99.9)=4.42ms  
     http_req_connecting............: avg=7.97µs   min=0s      med=0s       max=9.21ms   p(90)=0s       p(95)=0s       p(99.9)=4.08ms  
     http_req_duration..............: avg=177.39ms min=7.55ms  med=178.58ms max=375.7ms  p(90)=188ms    p(95)=192.86ms p(99.9)=258.65ms
       { expected_response:true }...: avg=177.39ms min=7.55ms  med=178.58ms max=375.7ms  p(90)=188ms    p(95)=192.86ms p(99.9)=258.65ms
     http_req_failed................: 0.00%   ✓ 0         ✗ 33790
     http_req_receiving.............: avg=95.68µs  min=34.7µs  med=85.51µs  max=60.02ms  p(90)=116.22µs p(95)=127.43µs p(99.9)=509.47µs
     http_req_sending...............: avg=22.58µs  min=6.13µs  med=16.96µs  max=43.36ms  p(90)=21.66µs  p(95)=23.55µs  p(99.9)=712.82µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=177.27ms min=7.47ms  med=178.47ms max=374.93ms p(90)=187.89ms p(95)=192.76ms p(99.9)=257.49ms
     http_reqs......................: 33790   279.31177/s
     iteration_duration.............: avg=178.18ms min=28.42ms med=178.9ms  max=390.04ms p(90)=188.28ms p(95)=193.16ms p(99.9)=264.82ms
     iterations.....................: 33690   278.48516/s
     success_rate...................: 100.00% ✓ 33690     ✗ 0    
     vus............................: 50      min=50      max=50 
     vus_max........................: 50      min=50      max=50
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

     checks.........................: 100.00% ✓ 99849      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   332 kB/s
     http_req_blocked...............: avg=4.81µs   min=1.13µs  med=3.22µs   max=2.81ms   p(90)=4.61µs   p(95)=5.17µs   p(99.9)=471.57µs
     http_req_connecting............: avg=1.36µs   min=0s      med=0s       max=2.77ms   p(90)=0s       p(95)=0s       p(99.9)=415.15µs
     http_req_duration..............: avg=179.59ms min=5.79ms  med=162.3ms  max=761.61ms p(90)=206.97ms p(95)=235.65ms p(99.9)=687.72ms
       { expected_response:true }...: avg=179.59ms min=5.79ms  med=162.3ms  max=761.61ms p(90)=206.97ms p(95)=235.65ms p(99.9)=687.72ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33383
     http_req_receiving.............: avg=90.75µs  min=29.25µs med=85.7µs   max=56.66ms  p(90)=114.86µs p(95)=125.67µs p(99.9)=679.32µs
     http_req_sending...............: avg=23.69µs  min=5.38µs  med=16.79µs  max=40.82ms  p(90)=20.94µs  p(95)=22.62µs  p(99.9)=413.1µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=179.47ms min=5.66ms  med=162.19ms max=761.46ms p(90)=206.84ms p(95)=235.49ms p(99.9)=687.61ms
     http_reqs......................: 33383   276.281659/s
     iteration_duration.............: avg=180.38ms min=59.38ms med=162.62ms max=761.88ms p(90)=207.38ms p(95)=236.27ms p(99.9)=687.99ms
     iterations.....................: 33283   275.454047/s
     success_rate...................: 100.00% ✓ 33283      ✗ 0    
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

