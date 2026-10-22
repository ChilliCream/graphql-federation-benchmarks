## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s**.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-net-11 | 16.7.0-p.27 | 2,565 | 2,678 | 2,546 | 1.7% |  |
| fusion-nightly-net-10 | 16.7.0-p.27 | 2,529 | 2,656 | 2,516 | 1.9% |  |
| hive-router | v0.3.5 | 2,501 | 2,707 | 2,464 | 3.1% |  |
| fusion-net-10 | 16.6.8 | 2,413 | 2,524 | 2,395 | 1.8% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.27 | 2,255 | 2,370 | 2,243 | 1.9% |  |
| grafbase | 0.53.5 | 1,660 | 1,715 | 1,656 | 1.2% |  |
| caliban | 3.2.0 | 1,454 | 1,521 | 1,449 | 1.7% |  |
| cosmo | 0.359.0 | 1,434 | 1,491 | 1,428 | 1.5% |  |
| feddi-gateway | e91d605ed222 | 934 | 974 | 924 | 1.7% |  |
| hive-gateway-router-runtime | 2.15.2 | 515 | 535 | 511 | 1.5% |  |
| apollo-router | v2.18.0 | 446 | 462 | 439 | 1.5% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 379 | 397 | 375 | 2.1% |  |
| apollo-gateway | 2.14.4 | 266 | 271 | 265 | 0.7% |  |
| hive-gateway | 2.15.2 | 262 | 269 | 260 | 1.0% |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.27)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 924687      ✗ 0     
     data_received..................: 27 GB   225 MB/s
     data_sent......................: 371 MB  3.1 MB/s
     http_req_blocked...............: avg=2.9µs   min=861ns   med=2.07µs  max=13.41ms  p(90)=3.66µs  p(95)=4.48µs  p(99.9)=29.31µs
     http_req_connecting............: avg=319ns   min=0s      med=0s      max=4.13ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=19.23ms min=1.49ms  med=18.18ms max=288.19ms p(90)=27.87ms p(95)=31.61ms p(99.9)=52.57ms
       { expected_response:true }...: avg=19.23ms min=1.49ms  med=18.18ms max=288.19ms p(90)=27.87ms p(95)=31.61ms p(99.9)=52.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 308329
     http_req_receiving.............: avg=1.18ms  min=51.38µs med=144.8µs max=240.54ms p(90)=3.07ms  p(95)=4.2ms   p(99.9)=25.24ms
     http_req_sending...............: avg=45.12µs min=4.69µs  med=8.61µs  max=135.85ms p(90)=18.78µs p(95)=92.06µs p(99.9)=4.39ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=18ms    min=1.37ms  med=16.91ms max=287.79ms p(90)=26.39ms p(95)=30.03ms p(99.9)=49.73ms
     http_reqs......................: 308329  2565.308677/s
     iteration_duration.............: avg=19.45ms min=2.77ms  med=18.38ms max=301.34ms p(90)=28.09ms p(95)=31.85ms p(99.9)=53.11ms
     iterations.....................: 308229  2564.476674/s
     success_rate...................: 100.00% ✓ 308229      ✗ 0     
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

     checks.........................: 100.00% ✓ 912066      ✗ 0     
     data_received..................: 27 GB   222 MB/s
     data_sent......................: 365 MB  3.0 MB/s
     http_req_blocked...............: avg=2.8µs    min=852ns   med=2.08µs  max=12.22ms  p(90)=3.51µs  p(95)=4.22µs  p(99.9)=30.23µs 
     http_req_connecting............: avg=293ns    min=0s      med=0s      max=3.51ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=19.51ms  min=1.61ms  med=16.59ms max=273.76ms p(90)=31.73ms p(95)=38.62ms p(99.9)=130.73ms
       { expected_response:true }...: avg=19.51ms  min=1.61ms  med=16.59ms max=273.76ms p(90)=31.73ms p(95)=38.62ms p(99.9)=130.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 304122
     http_req_receiving.............: avg=545.71µs min=50.05µs med=89.67µs max=177.31ms p(90)=1.05ms  p(95)=1.86ms  p(99.9)=26.14ms 
     http_req_sending...............: avg=45.22µs  min=4.67µs  med=8.49µs  max=194.72ms p(90)=16.13µs p(95)=84.07µs p(99.9)=4.4ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=18.92ms  min=1.52ms  med=16.09ms max=273.22ms p(90)=30.79ms p(95)=37.55ms p(99.9)=129.16ms
     http_reqs......................: 304122  2529.673521/s
     iteration_duration.............: avg=19.72ms  min=2.55ms  med=16.79ms max=303.94ms p(90)=31.95ms p(95)=38.86ms p(99.9)=131.5ms 
     iterations.....................: 304022  2528.841726/s
     success_rate...................: 100.00% ✓ 304022      ✗ 0     
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

     checks.........................: 100.00% ✓ 901788      ✗ 0     
     data_received..................: 26 GB   219 MB/s
     data_sent......................: 361 MB  3.0 MB/s
     http_req_blocked...............: avg=3.24µs  min=892ns   med=2.5µs   max=7.86ms   p(90)=4.16µs  p(95)=4.94µs   p(99.9)=37.39µs
     http_req_connecting............: avg=316ns   min=0s      med=0s      max=4.3ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=19.73ms min=1.57ms  med=19.54ms max=293.37ms p(90)=27.14ms p(95)=29.48ms  p(99.9)=49.22ms
       { expected_response:true }...: avg=19.73ms min=1.57ms  med=19.54ms max=293.37ms p(90)=27.14ms p(95)=29.48ms  p(99.9)=49.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 300696
     http_req_receiving.............: avg=90.82µs min=26.24µs med=54.1µs  max=32.28ms  p(90)=95.4µs  p(95)=137.97µs p(99.9)=6.51ms 
     http_req_sending...............: avg=45.4µs  min=4.61µs  med=10.1µs  max=199.55ms p(90)=17.25µs p(95)=87.63µs  p(99.9)=2.95ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=19.6ms  min=1.51ms  med=19.42ms max=293.22ms p(90)=26.99ms p(95)=29.29ms  p(99.9)=48.27ms
     http_reqs......................: 300696  2501.355419/s
     iteration_duration.............: avg=19.95ms min=3.69ms  med=19.74ms max=304.29ms p(90)=27.35ms p(95)=29.7ms   p(99.9)=49.82ms
     iterations.....................: 300596  2500.523563/s
     success_rate...................: 100.00% ✓ 300596      ✗ 0     
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

     checks.........................: 100.00% ✓ 870111      ✗ 0     
     data_received..................: 25 GB   212 MB/s
     data_sent......................: 349 MB  2.9 MB/s
     http_req_blocked...............: avg=3.2µs    min=872ns   med=1.98µs  max=16.52ms  p(90)=3.4µs   p(95)=4.1µs   p(99.9)=28.75µs 
     http_req_connecting............: avg=753ns    min=0s      med=0s      max=8.03ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=20.46ms  min=1.59ms  med=17.09ms max=344.24ms p(90)=33.84ms p(95)=41.36ms p(99.9)=149.13ms
       { expected_response:true }...: avg=20.46ms  min=1.59ms  med=17.09ms max=344.24ms p(90)=33.84ms p(95)=41.36ms p(99.9)=149.13ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 290137
     http_req_receiving.............: avg=609.17µs min=50.35µs med=93.87µs max=213.83ms p(90)=1.13ms  p(95)=1.99ms  p(99.9)=28.08ms 
     http_req_sending...............: avg=40.98µs  min=4.36µs  med=8.22µs  max=88.72ms  p(90)=15.4µs  p(95)=66.37µs p(99.9)=4ms     
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=19.81ms  min=1.47ms  med=16.54ms max=344.08ms p(90)=32.78ms p(95)=40.14ms p(99.9)=146.26ms
     http_reqs......................: 290137  2413.447284/s
     iteration_duration.............: avg=20.68ms  min=2.63ms  med=17.29ms max=344.43ms p(90)=34.06ms p(95)=41.6ms  p(99.9)=150.3ms 
     iterations.....................: 290037  2412.615454/s
     success_rate...................: 100.00% ✓ 290037      ✗ 0     
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

     checks.........................: 100.00% ✓ 813105      ✗ 0     
     data_received..................: 24 GB   198 MB/s
     data_sent......................: 326 MB  2.7 MB/s
     http_req_blocked...............: avg=3.07µs   min=822ns   med=2.1µs   max=16.5ms   p(90)=3.58µs  p(95)=4.3µs   p(99.9)=34.62µs 
     http_req_connecting............: avg=345ns    min=0s      med=0s      max=4.04ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=21.9ms   min=1.85ms  med=18.52ms max=672.04ms p(90)=35.73ms p(95)=44.1ms  p(99.9)=149.78ms
       { expected_response:true }...: avg=21.9ms   min=1.85ms  med=18.52ms max=672.04ms p(90)=35.73ms p(95)=44.1ms  p(99.9)=149.78ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 271135
     http_req_receiving.............: avg=612.39µs min=52.01µs med=99.74µs max=268.57ms p(90)=1.14ms  p(95)=1.96ms  p(99.9)=29.11ms 
     http_req_sending...............: avg=39.27µs  min=4.59µs  med=8.99µs  max=138.48ms p(90)=17.14µs p(95)=63.63µs p(99.9)=2.69ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=21.25ms  min=1.77ms  med=17.95ms max=671.92ms p(90)=34.74ms p(95)=42.91ms p(99.9)=147.82ms
     http_reqs......................: 271135  2255.032553/s
     iteration_duration.............: avg=22.12ms  min=2.83ms  med=18.72ms max=672.23ms p(90)=35.95ms p(95)=44.33ms p(99.9)=150.96ms
     iterations.....................: 271035  2254.200852/s
     success_rate...................: 100.00% ✓ 271035      ✗ 0     
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

     checks.........................: 100.00% ✓ 599067      ✗ 0     
     data_received..................: 18 GB   146 MB/s
     data_sent......................: 240 MB  2.0 MB/s
     http_req_blocked...............: avg=3.43µs  min=842ns  med=2.26µs  max=14.01ms  p(90)=4.65µs   p(95)=5.81µs   p(99.9)=44.3µs 
     http_req_connecting............: avg=435ns   min=0s     med=0s      max=3.77ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=29.79ms min=2.24ms med=29.25ms max=297.11ms p(90)=39.43ms  p(95)=42.88ms  p(99.9)=65.32ms
       { expected_response:true }...: avg=29.79ms min=2.24ms med=29.25ms max=297.11ms p(90)=39.43ms  p(95)=42.88ms  p(99.9)=65.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 199789
     http_req_receiving.............: avg=98.14µs min=26.5µs med=55.16µs max=45.29ms  p(90)=127.34µs p(95)=217.62µs p(99.9)=4.66ms 
     http_req_sending...............: avg=43.51µs min=4.45µs med=9.2µs   max=133.07ms p(90)=23.89µs  p(95)=119.41µs p(99.9)=3.22ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=29.65ms min=2.14ms med=29.12ms max=296.55ms p(90)=39.26ms  p(95)=42.7ms   p(99.9)=64.41ms
     http_reqs......................: 199789  1660.883368/s
     iteration_duration.............: avg=30.03ms min=6.53ms med=29.47ms max=307.11ms p(90)=39.66ms  p(95)=43.1ms   p(99.9)=65.87ms
     iterations.....................: 199689  1660.052049/s
     success_rate...................: 100.00% ✓ 199689      ✗ 0     
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

     checks.........................: 100.00% ✓ 524781      ✗ 0     
     data_received..................: 15 GB   127 MB/s
     data_sent......................: 210 MB  1.7 MB/s
     http_req_blocked...............: avg=5.89µs  min=1.05µs  med=3.71µs  max=9.7ms    p(90)=5.86µs   p(95)=6.77µs   p(99.9)=43.93µs
     http_req_connecting............: avg=1.76µs  min=0s      med=0s      max=9.66ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.02ms min=2.45ms  med=33.06ms max=299.63ms p(90)=47.99ms  p(95)=52.95ms  p(99.9)=78.76ms
       { expected_response:true }...: avg=34.02ms min=2.45ms  med=33.06ms max=299.63ms p(90)=47.99ms  p(95)=52.95ms  p(99.9)=78.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 175027
     http_req_receiving.............: avg=88.88µs min=26.27µs med=67.65µs max=77.36ms  p(90)=112.67µs p(95)=136.61µs p(99.9)=1.96ms 
     http_req_sending...............: avg=35.92µs min=5.42µs  med=14.71µs max=105.86ms p(90)=23.12µs  p(95)=28.8µs   p(99.9)=1.59ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.89ms min=2.34ms  med=32.94ms max=298.8ms  p(90)=47.86ms  p(95)=52.81ms  p(99.9)=78.59ms
     http_reqs......................: 175027  1454.640999/s
     iteration_duration.............: avg=34.28ms min=5.75ms  med=33.31ms max=318.83ms p(90)=48.24ms  p(95)=53.21ms  p(99.9)=79.34ms
     iterations.....................: 174927  1453.809904/s
     success_rate...................: 100.00% ✓ 174927      ✗ 0     
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

     checks.........................: 100.00% ✓ 517509      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=3.87µs  min=982ns   med=2.27µs  max=8.02ms   p(90)=3.9µs   p(95)=4.65µs   p(99.9)=35.56µs
     http_req_connecting............: avg=1.14µs  min=0s      med=0s      max=7.99ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.54ms min=2.34ms  med=33.6ms  max=281.33ms p(90)=49.44ms p(95)=54.42ms  p(99.9)=78.14ms
       { expected_response:true }...: avg=34.54ms min=2.34ms  med=33.6ms  max=281.33ms p(90)=49.44ms p(95)=54.42ms  p(99.9)=78.14ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 172603
     http_req_receiving.............: avg=77.08µs min=26.08µs med=58.88µs max=146.84ms p(90)=98.45µs p(95)=117.55µs p(99.9)=1.17ms 
     http_req_sending...............: avg=29.4µs  min=4.97µs  med=10.42µs max=134.85ms p(90)=17.96µs p(95)=22.8µs   p(99.9)=1.42ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.44ms min=2.27ms  med=33.51ms max=278.98ms p(90)=49.33ms p(95)=54.32ms  p(99.9)=77.69ms
     http_reqs......................: 172603  1434.732742/s
     iteration_duration.............: avg=34.77ms min=4.86ms  med=33.81ms max=300.06ms p(90)=49.65ms p(95)=54.63ms  p(99.9)=78.45ms
     iterations.....................: 172503  1433.901509/s
     success_rate...................: 100.00% ✓ 172503      ✗ 0     
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

     checks.........................: 100.00% ✓ 336774     ✗ 0     
     data_received..................: 9.8 GB  82 MB/s
     data_sent......................: 135 MB  1.1 MB/s
     http_req_blocked...............: avg=4.04µs  min=1.19µs  med=2.93µs  max=3.72ms   p(90)=4.55µs  p(95)=5.23µs   p(99.9)=41.68µs 
     http_req_connecting............: avg=816ns   min=0s      med=0s      max=3.68ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=53.16ms min=1.82ms  med=52ms    max=297.44ms p(90)=87.79ms p(95)=97.38ms  p(99.9)=146.96ms
       { expected_response:true }...: avg=53.16ms min=1.82ms  med=52ms    max=297.44ms p(90)=87.79ms p(95)=97.38ms  p(99.9)=146.96ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 112358
     http_req_receiving.............: avg=70.92µs min=27.67µs med=59.98µs max=146.13ms p(90)=94.43µs p(95)=107.94µs p(99.9)=672.62µs
     http_req_sending...............: avg=24.97µs min=5.44µs  med=12.48µs max=217.06ms p(90)=18.34µs p(95)=21.31µs  p(99.9)=772.35µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.07ms min=1.72ms  med=51.91ms max=281.51ms p(90)=87.7ms  p(95)=97.29ms  p(99.9)=145.93ms
     http_reqs......................: 112358  934.097577/s
     iteration_duration.............: avg=53.44ms min=2.21ms  med=52.23ms max=306.13ms p(90)=88.01ms p(95)=97.61ms  p(99.9)=147.84ms
     iterations.....................: 112258  933.266219/s
     success_rate...................: 100.00% ✓ 112258     ✗ 0     
     vus............................: 50      min=50       max=50  
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 186330     ✗ 0    
     data_received..................: 5.4 GB  45 MB/s
     data_sent......................: 75 MB   620 kB/s
     http_req_blocked...............: avg=5.26µs  min=1.18µs  med=3.34µs  max=4.22ms   p(90)=4.94µs   p(95)=5.59µs   p(99.9)=50.27µs 
     http_req_connecting............: avg=1.66µs  min=0s      med=0s      max=4.18ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=96.2ms  min=4.42ms  med=93.63ms max=343.57ms p(90)=117.24ms p(95)=129.21ms p(99.9)=227.93ms
       { expected_response:true }...: avg=96.2ms  min=4.42ms  med=93.63ms max=343.57ms p(90)=117.24ms p(95)=129.21ms p(99.9)=227.93ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 62210
     http_req_receiving.............: avg=86.88µs min=30.49µs med=77.05µs max=102.66ms p(90)=112.22µs p(95)=125.59µs p(99.9)=669.32µs
     http_req_sending...............: avg=22.18µs min=5.39µs  med=15.37µs max=72.69ms  p(90)=21.54µs  p(95)=23.64µs  p(99.9)=589.95µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=96.09ms min=4.29ms  med=93.54ms max=343.04ms p(90)=117.14ms p(95)=129.09ms p(99.9)=227.27ms
     http_reqs......................: 62210   515.93022/s
     iteration_duration.............: avg=96.61ms min=27.27ms med=93.9ms  max=356.93ms p(90)=117.51ms p(95)=129.52ms p(99.9)=230.84ms
     iterations.....................: 62110   515.100884/s
     success_rate...................: 100.00% ✓ 62110      ✗ 0    
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

     checks.........................: 100.00% ✓ 161184     ✗ 0    
     data_received..................: 4.7 GB  39 MB/s
     data_sent......................: 65 MB   536 kB/s
     http_req_blocked...............: avg=8.61µs   min=1.12µs  med=3.27µs   max=8.6ms    p(90)=4.83µs   p(95)=5.43µs   p(99.9)=145.44µs
     http_req_connecting............: avg=4.83µs   min=0s      med=0s       max=8.56ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=111.22ms min=5.25ms  med=109.16ms max=321.3ms  p(90)=146.85ms p(95)=158.09ms p(99.9)=203.58ms
       { expected_response:true }...: avg=111.22ms min=5.25ms  med=109.16ms max=321.3ms  p(90)=146.85ms p(95)=158.09ms p(99.9)=203.58ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 53828
     http_req_receiving.............: avg=88.52µs  min=29.63µs med=84.05µs  max=67.37ms  p(90)=113.76µs p(95)=126.26µs p(99.9)=592.19µs
     http_req_sending...............: avg=23.36µs  min=5.17µs  med=16.42µs  max=78.39ms  p(90)=21.59µs  p(95)=23.47µs  p(99.9)=736.57µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=111.1ms  min=5.12ms  med=109.05ms max=320.23ms p(90)=146.75ms p(95)=157.97ms p(99.9)=203.37ms
     http_reqs......................: 53828   446.100606/s
     iteration_duration.............: avg=111.69ms min=20.37ms med=109.48ms max=331.88ms p(90)=147.16ms p(95)=158.43ms p(99.9)=205.63ms
     iterations.....................: 53728   445.271854/s
     success_rate...................: 100.00% ✓ 53728      ✗ 0    
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

     checks.........................: 100.00% ✓ 137025     ✗ 0    
     data_received..................: 4.0 GB  33 MB/s
     data_sent......................: 55 MB   455 kB/s
     http_req_blocked...............: avg=5.31µs   min=1.08µs  med=3.06µs   max=3.98ms   p(90)=4.47µs   p(95)=5.01µs   p(99.9)=924.76µs
     http_req_connecting............: avg=2.06µs   min=0s      med=0s       max=3.95ms   p(90)=0s       p(95)=0s       p(99.9)=786.45µs
     http_req_duration..............: avg=130.87ms min=6.05ms  med=128.38ms max=322.66ms p(90)=170.64ms p(95)=183.99ms p(99.9)=240.1ms 
       { expected_response:true }...: avg=130.87ms min=6.05ms  med=128.38ms max=322.66ms p(90)=170.64ms p(95)=183.99ms p(99.9)=240.1ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 45775
     http_req_receiving.............: avg=86.02µs  min=28.88µs med=78.42µs  max=90.96ms  p(90)=108.81µs p(95)=121.05µs p(99.9)=534.92µs
     http_req_sending...............: avg=24.98µs  min=5.18µs  med=15.32µs  max=163.71ms p(90)=20.36µs  p(95)=22.16µs  p(99.9)=522.87µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=130.76ms min=5.9ms   med=128.27ms max=322.18ms p(90)=170.52ms p(95)=183.89ms p(99.9)=239.14ms
     http_reqs......................: 45775   379.130189/s
     iteration_duration.............: avg=131.4ms  min=29.58ms med=128.72ms max=330.53ms p(90)=170.94ms p(95)=184.28ms p(99.9)=241.88ms
     iterations.....................: 45675   378.301942/s
     success_rate...................: 100.00% ✓ 45675      ✗ 0    
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

     checks.........................: 100.00% ✓ 96552      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   320 kB/s
     http_req_blocked...............: avg=6µs      min=1.13µs  med=3.12µs   max=3.56ms   p(90)=4.45µs   p(95)=4.98µs   p(99.9)=1.26ms  
     http_req_connecting............: avg=2.67µs   min=0s      med=0s       max=3.53ms   p(90)=0s       p(95)=0s       p(99.9)=1.24ms  
     http_req_duration..............: avg=185.67ms min=7.72ms  med=181.37ms max=375.63ms p(90)=206.73ms p(95)=211.56ms p(99.9)=280.51ms
       { expected_response:true }...: avg=185.67ms min=7.72ms  med=181.37ms max=375.63ms p(90)=206.73ms p(95)=211.56ms p(99.9)=280.51ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32284
     http_req_receiving.............: avg=91.46µs  min=30.77µs med=87.5µs   max=65.44ms  p(90)=116.79µs p(95)=127.8µs  p(99.9)=432.04µs
     http_req_sending...............: avg=22.4µs   min=4.91µs  med=16.96µs  max=52.08ms  p(90)=21.25µs  p(95)=23.05µs  p(99.9)=436.97µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=185.55ms min=7.58ms  med=181.27ms max=375.1ms  p(90)=206.64ms p(95)=211.46ms p(99.9)=280.33ms
     http_reqs......................: 32284   266.884497/s
     iteration_duration.............: avg=186.52ms min=42.89ms med=182.45ms max=394.34ms p(90)=207.02ms p(95)=211.88ms p(99.9)=284.56ms
     iterations.....................: 32184   266.05782/s
     success_rate...................: 100.00% ✓ 32184      ✗ 0    
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

     checks.........................: 100.00% ✓ 94974      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   315 kB/s
     http_req_blocked...............: avg=7.17µs   min=1.25µs  med=3.82µs   max=3.93ms   p(90)=5.34µs   p(95)=5.98µs   p(99.9)=1.6ms   
     http_req_connecting............: avg=3.1µs    min=0s      med=0s       max=3.89ms   p(90)=0s       p(95)=0s       p(99.9)=1.57ms  
     http_req_duration..............: avg=188.77ms min=6.35ms  med=170.79ms max=818.32ms p(90)=212.67ms p(95)=240.01ms p(99.9)=752.21ms
       { expected_response:true }...: avg=188.77ms min=6.35ms  med=170.79ms max=818.32ms p(90)=212.67ms p(95)=240.01ms p(99.9)=752.21ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31758
     http_req_receiving.............: avg=96.84µs  min=37.42µs med=90.81µs  max=56.07ms  p(90)=121.32µs p(95)=133.29µs p(99.9)=832.94µs
     http_req_sending...............: avg=28.33µs  min=5.75µs  med=17.7µs   max=57.69ms  p(90)=22.3µs   p(95)=24.2µs   p(99.9)=540.32µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=188.64ms min=6.22ms  med=170.67ms max=818.21ms p(90)=212.57ms p(95)=239.9ms  p(99.9)=752.1ms 
     http_reqs......................: 31758   262.304331/s
     iteration_duration.............: avg=189.62ms min=51.84ms med=171.13ms max=818.51ms p(90)=213.04ms p(95)=240.61ms p(99.9)=752.49ms
     iterations.....................: 31658   261.478384/s
     success_rate...................: 100.00% ✓ 31658      ✗ 0    
     vus............................: 38      min=38       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

