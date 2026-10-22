## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| feddi-gateway | 3c75a7db8876 | 2,453 | 2,554 | 2,438 | 1.5% |  |
| fusion-nightly-net-10 | 16.7.0-p.32 | 2,351 | 2,436 | 2,344 | 1.3% |  |
| fusion-nightly-net-11 | 16.7.0-p.32 | 2,329 | 2,425 | 2,318 | 1.5% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.32 | 1,960 | 2,013 | 1,946 | 1.1% |  |
| fusion-net-10 | 16.6.9 | 1,904 | 1,946 | 1,893 | 0.9% |  |
| hive-router | v0.3.5 | 1,874 | 1,938 | 1,858 | 1.4% |  |
| caliban | 3.2.0 | 1,417 | 1,474 | 1,413 | 1.6% |  |
| cosmo | 0.359.0 | 1,353 | 1,392 | 1,333 | 1.6% |  |
| grafbase | 0.53.5 | 1,324 | 1,350 | 1,319 | 0.8% |  |
| hive-gateway-router-runtime | 2.15.2 | 506 | 520 | 502 | 1.0% |  |
| apollo-router | v2.18.0 | 397 | 417 | 394 | 2.1% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 385 | 403 | 379 | 2.1% |  |
| apollo-gateway | 2.14.4 | 261 | 263 | 258 | 0.7% |  |
| hive-gateway | 2.15.2 | 250 | 258 | 249 | 1.4% |  |


### Details

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 893238      ✗ 0     
     data_received..................: 26 GB   214 MB/s
     data_sent......................: 358 MB  2.9 MB/s
     http_req_blocked...............: avg=2.95µs  min=841ns   med=2.01µs  max=10.39ms  p(90)=3.54µs  p(95)=4.45µs   p(99.9)=32.89µs
     http_req_connecting............: avg=441ns   min=0s      med=0s      max=7.31ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=19.93ms min=12.33ms med=19.22ms max=278.35ms p(90)=23.88ms p(95)=26ms     p(99.9)=44.97ms
       { expected_response:true }...: avg=19.93ms min=12.33ms med=19.22ms max=278.35ms p(90)=23.88ms p(95)=26ms     p(99.9)=44.97ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 297846
     http_req_receiving.............: avg=81.34µs min=24.8µs  med=46.54µs max=84.79ms  p(90)=94.23µs p(95)=151.58µs p(99.9)=4.09ms 
     http_req_sending...............: avg=41.65µs min=4.46µs  med=8.65µs  max=76.54ms  p(90)=17.91µs p(95)=88.09µs  p(99.9)=3.62ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=19.81ms min=12.26ms med=19.13ms max=276.91ms p(90)=23.73ms p(95)=25.79ms  p(99.9)=44.39ms
     http_reqs......................: 297846  2453.000187/s
     iteration_duration.............: avg=20.14ms min=12.51ms med=19.42ms max=295.69ms p(90)=24.08ms p(95)=26.22ms  p(99.9)=45.31ms
     iterations.....................: 297746  2452.176607/s
     success_rate...................: 100.00% ✓ 297746      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-10 (HotChocolate subgraphs) (16.7.0-p.32)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 856482      ✗ 0     
     data_received..................: 25 GB   206 MB/s
     data_sent......................: 343 MB  2.8 MB/s
     http_req_blocked...............: avg=2.56µs  min=782ns   med=1.81µs  max=5.7ms    p(90)=3.35µs  p(95)=4.2µs   p(99.9)=27.38µs
     http_req_connecting............: avg=304ns   min=0s      med=0s      max=3.53ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=20.8ms  min=12.45ms med=20.02ms max=287.5ms  p(90)=25.54ms p(95)=27.73ms p(99.9)=47.48ms
       { expected_response:true }...: avg=20.8ms  min=12.45ms med=20.02ms max=287.5ms  p(90)=25.54ms p(95)=27.73ms p(99.9)=47.48ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 285594
     http_req_receiving.............: avg=482.3µs min=48.9µs  med=84.21µs max=219.91ms p(90)=1.42ms  p(95)=2.33ms  p(99.9)=17.15ms
     http_req_sending...............: avg=40.25µs min=4.37µs  med=7.72µs  max=165.79ms p(90)=17.53µs p(95)=81.5µs  p(99.9)=3.97ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=20.27ms min=12.36ms med=19.53ms max=286.94ms p(90)=24.8ms  p(95)=26.94ms p(99.9)=45.64ms
     http_reqs......................: 285594  2351.453162/s
     iteration_duration.............: avg=21ms    min=12.66ms med=20.22ms max=303.08ms p(90)=25.74ms p(95)=27.94ms p(99.9)=47.84ms
     iterations.....................: 285494  2350.629806/s
     success_rate...................: 100.00% ✓ 285494      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.32)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 848514      ✗ 0     
     data_received..................: 25 GB   204 MB/s
     data_sent......................: 340 MB  2.8 MB/s
     http_req_blocked...............: avg=2.65µs   min=781ns   med=1.82µs  max=12.86ms  p(90)=3.33µs  p(95)=4.2µs   p(99.9)=29.37µs
     http_req_connecting............: avg=319ns    min=0s      med=0s      max=4.03ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=20.99ms  min=13.03ms med=20.28ms max=277.01ms p(90)=25.55ms p(95)=27.66ms p(99.9)=48.57ms
       { expected_response:true }...: avg=20.99ms  min=13.03ms med=20.28ms max=277.01ms p(90)=25.55ms p(95)=27.66ms p(99.9)=48.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 282938
     http_req_receiving.............: avg=456.02µs min=48.49µs med=83.7µs  max=137.33ms p(90)=1.33ms  p(95)=2.31ms  p(99.9)=14.69ms
     http_req_sending...............: avg=39.05µs  min=4.3µs   med=7.68µs  max=179.64ms p(90)=17.34µs p(95)=84.04µs p(99.9)=3.52ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=20.5ms   min=12.2ms  med=19.82ms max=276.26ms p(90)=24.86ms p(95)=26.91ms p(99.9)=46.92ms
     http_reqs......................: 282938  2329.557961/s
     iteration_duration.............: avg=21.2ms   min=13.21ms med=20.48ms max=307.46ms p(90)=25.75ms p(95)=27.87ms p(99.9)=48.91ms
     iterations.....................: 282838  2328.734615/s
     success_rate...................: 100.00% ✓ 282838      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-10 (HotChocolate subgraphs) (16.7.0-p.32)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 716742      ✗ 0     
     data_received..................: 21 GB   172 MB/s
     data_sent......................: 287 MB  2.4 MB/s
     http_req_blocked...............: avg=2.78µs   min=811ns   med=1.9µs   max=4.58ms   p(90)=3.61µs  p(95)=4.44µs  p(99.9)=28.53µs
     http_req_connecting............: avg=452ns    min=0s      med=0s      max=4.54ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=24.89ms  min=17.09ms med=24.29ms max=278.76ms p(90)=29.23ms p(95)=31.01ms p(99.9)=49.54ms
       { expected_response:true }...: avg=24.89ms  min=17.09ms med=24.29ms max=278.76ms p(90)=29.23ms p(95)=31.01ms p(99.9)=49.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 239014
     http_req_receiving.............: avg=406.23µs min=49.81µs med=91.06µs max=104.38ms p(90)=1.21ms  p(95)=1.94ms  p(99.9)=9.47ms 
     http_req_sending...............: avg=36.47µs  min=4.31µs  med=8.02µs  max=218.22ms p(90)=18.34µs p(95)=56.93µs p(99.9)=2.23ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=24.44ms  min=16.81ms med=23.87ms max=278.32ms p(90)=28.62ms p(95)=30.33ms p(99.9)=47.56ms
     http_reqs......................: 239014  1960.152464/s
     iteration_duration.............: avg=25.1ms   min=17.28ms med=24.49ms max=297.85ms p(90)=29.42ms p(95)=31.21ms p(99.9)=49.87ms
     iterations.....................: 238914  1959.332365/s
     success_rate...................: 100.00% ✓ 238914      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-10 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 696267      ✗ 0     
     data_received..................: 20 GB   167 MB/s
     data_sent......................: 279 MB  2.3 MB/s
     http_req_blocked...............: avg=3.78µs   min=941ns   med=2.48µs   max=8.07ms   p(90)=4.18µs  p(95)=4.95µs  p(99.9)=34.61µs
     http_req_connecting............: avg=869ns    min=0s      med=0s       max=7.97ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.62ms  min=16.3ms  med=24.98ms  max=296.64ms p(90)=30.09ms p(95)=31.99ms p(99.9)=50.18ms
       { expected_response:true }...: avg=25.62ms  min=16.3ms  med=24.98ms  max=296.64ms p(90)=30.09ms p(95)=31.99ms p(99.9)=50.18ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 232189
     http_req_receiving.............: avg=444.93µs min=50.3µs  med=101.09µs max=181.68ms p(90)=1.23ms  p(95)=1.89ms  p(99.9)=10.74ms
     http_req_sending...............: avg=34.74µs  min=4.82µs  med=9.56µs   max=32.62ms  p(90)=19.4µs  p(95)=66.52µs p(99.9)=2.07ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.14ms  min=16.2ms  med=24.52ms  max=295.32ms p(90)=29.46ms p(95)=31.31ms p(99.9)=48.77ms
     http_reqs......................: 232189  1904.30459/s
     iteration_duration.............: avg=25.84ms  min=16.48ms med=25.19ms  max=317.75ms p(90)=30.3ms  p(95)=32.21ms p(99.9)=50.61ms
     iterations.....................: 232089  1903.484437/s
     success_rate...................: 100.00% ✓ 232089      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 685539      ✗ 0     
     data_received..................: 20 GB   164 MB/s
     data_sent......................: 275 MB  2.3 MB/s
     http_req_blocked...............: avg=2.87µs  min=932ns   med=2.07µs  max=4.15ms   p(90)=3.74µs  p(95)=4.53µs   p(99.9)=27.43µs
     http_req_connecting............: avg=409ns   min=0s      med=0s      max=4.11ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.04ms min=18.07ms med=25.59ms max=310.66ms p(90)=29.64ms p(95)=31.05ms  p(99.9)=48.87ms
       { expected_response:true }...: avg=26.04ms min=18.07ms med=25.59ms max=310.66ms p(90)=29.64ms p(95)=31.05ms  p(99.9)=48.87ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 228613
     http_req_receiving.............: avg=74.18µs min=25.37µs med=51.02µs max=122.32ms p(90)=93.59µs p(95)=120.38µs p(99.9)=1.67ms 
     http_req_sending...............: avg=31.86µs min=4.65µs  med=8.91µs  max=106.57ms p(90)=17.18µs p(95)=25.21µs  p(99.9)=1.47ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=25.93ms min=17.94ms med=25.5ms  max=310.06ms p(90)=29.53ms p(95)=30.92ms  p(99.9)=48.08ms
     http_reqs......................: 228613  1874.808015/s
     iteration_duration.............: avg=26.24ms min=18.3ms  med=25.79ms max=319.89ms p(90)=29.84ms p(95)=31.25ms  p(99.9)=49.11ms
     iterations.....................: 228513  1873.987936/s
     success_rate...................: 100.00% ✓ 228513      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 518589      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 208 MB  1.7 MB/s
     http_req_blocked...............: avg=4.74µs   min=1.13µs  med=3.57µs  max=7.37ms   p(90)=5.77µs   p(95)=6.72µs   p(99.9)=44.75µs
     http_req_connecting............: avg=734ns    min=0s      med=0s      max=7.25ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.44ms  min=18.94ms med=33.9ms  max=307.35ms p(90)=40.22ms  p(95)=42.47ms  p(99.9)=61.46ms
       { expected_response:true }...: avg=34.44ms  min=18.94ms med=33.9ms  max=307.35ms p(90)=40.22ms  p(95)=42.47ms  p(99.9)=61.46ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 172963
     http_req_receiving.............: avg=113.33µs min=26.67µs med=68.27µs max=254.7ms  p(90)=116.83µs p(95)=144.56µs p(99.9)=2.59ms 
     http_req_sending...............: avg=33.55µs  min=5.3µs   med=14.1µs  max=147.5ms  p(90)=23.67µs  p(95)=29.85µs  p(99.9)=1.5ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.29ms  min=18.84ms med=33.79ms max=132.28ms p(90)=40.09ms  p(95)=42.32ms  p(99.9)=60.5ms 
     http_reqs......................: 172963  1417.258949/s
     iteration_duration.............: avg=34.69ms  min=20.79ms med=34.15ms max=317.77ms p(90)=40.46ms  p(95)=42.7ms   p(99.9)=61.87ms
     iterations.....................: 172863  1416.439549/s
     success_rate...................: 100.00% ✓ 172863      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 495294      ✗ 0     
     data_received..................: 15 GB   118 MB/s
     data_sent......................: 199 MB  1.6 MB/s
     http_req_blocked...............: avg=3.29µs  min=961ns   med=2.34µs  max=4.04ms   p(90)=4.13µs   p(95)=4.92µs   p(99.9)=35.27µs
     http_req_connecting............: avg=568ns   min=0s      med=0s      max=4ms      p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=36.11ms min=18.92ms med=35.5ms  max=291.36ms p(90)=43.18ms  p(95)=45.66ms  p(99.9)=59.42ms
       { expected_response:true }...: avg=36.11ms min=18.92ms med=35.5ms  max=291.36ms p(90)=43.18ms  p(95)=45.66ms  p(99.9)=59.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 165198
     http_req_receiving.............: avg=76.64µs min=26.04µs med=59.96µs max=99.49ms  p(90)=102.73µs p(95)=123.75µs p(99.9)=1.18ms 
     http_req_sending...............: avg=28.6µs  min=4.89µs  med=10.71µs max=204.23ms p(90)=18.95µs  p(95)=23.38µs  p(99.9)=1.14ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=36ms    min=18.8ms  med=35.41ms max=290.94ms p(90)=43.07ms  p(95)=45.54ms  p(99.9)=58.86ms
     http_reqs......................: 165198  1353.692825/s
     iteration_duration.............: avg=36.33ms min=21.11ms med=35.71ms max=308.95ms p(90)=43.38ms  p(95)=45.87ms  p(99.9)=59.76ms
     iterations.....................: 165098  1352.873388/s
     success_rate...................: 100.00% ✓ 165098      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 484506      ✗ 0     
     data_received..................: 14 GB   116 MB/s
     data_sent......................: 194 MB  1.6 MB/s
     http_req_blocked...............: avg=4.2µs   min=1.05µs  med=2.99µs  max=6.1ms    p(90)=5.5µs    p(95)=6.54µs   p(99.9)=44.59µs
     http_req_connecting............: avg=594ns   min=0s      med=0s      max=3.94ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=36.87ms min=18.15ms med=36.51ms max=304.31ms p(90)=43.49ms  p(95)=45.54ms  p(99.9)=63.5ms 
       { expected_response:true }...: avg=36.87ms min=18.15ms med=36.51ms max=304.31ms p(90)=43.49ms  p(95)=45.54ms  p(99.9)=63.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 161602
     http_req_receiving.............: avg=122.5µs min=27.54µs med=62.23µs max=244.94ms p(90)=132.87µs p(95)=182.74µs p(99.9)=2.8ms  
     http_req_sending...............: avg=37.94µs min=4.36µs  med=11.3µs  max=95.52ms  p(90)=24.73µs  p(95)=68.85µs  p(99.9)=2.11ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=36.71ms min=18.05ms med=36.39ms max=173.87ms p(90)=43.36ms  p(95)=45.39ms  p(99.9)=60.66ms
     http_reqs......................: 161602  1324.691256/s
     iteration_duration.............: avg=37.13ms min=20.29ms med=36.76ms max=327.56ms p(90)=43.72ms  p(95)=45.78ms  p(99.9)=63.93ms
     iterations.....................: 161502  1323.871531/s
     success_rate...................: 100.00% ✓ 161502      ✗ 0     
     vus............................: 12      min=0         max=50  
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

     checks.........................: 100.00% ✓ 185532     ✗ 0    
     data_received..................: 5.4 GB  44 MB/s
     data_sent......................: 74 MB   608 kB/s
     http_req_blocked...............: avg=4.77µs  min=982ns   med=2.91µs  max=4.54ms   p(90)=4.46µs   p(95)=5.08µs   p(99.9)=47.21µs 
     http_req_connecting............: avg=1.65µs  min=0s      med=0s      max=4.5ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=96.66ms min=21.23ms med=95ms    max=311.69ms p(90)=114.62ms p(95)=124.13ms p(99.9)=217.29ms
       { expected_response:true }...: avg=96.66ms min=21.23ms med=95ms    max=311.69ms p(90)=114.62ms p(95)=124.13ms p(99.9)=217.29ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 61944
     http_req_receiving.............: avg=83.35µs min=29.9µs  med=75.5µs  max=94.31ms  p(90)=110.21µs p(95)=122.86µs p(99.9)=582.45µs
     http_req_sending...............: avg=25.8µs  min=4.96µs  med=14.42µs max=136.61ms p(90)=20.44µs  p(95)=22.55µs  p(99.9)=534.66µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=96.55ms min=21.14ms med=94.9ms  max=310.99ms p(90)=114.52ms p(95)=124ms    p(99.9)=217.06ms
     http_reqs......................: 61944   506.551923/s
     iteration_duration.............: avg=97.03ms min=35.93ms med=95.27ms max=328.36ms p(90)=114.88ms p(95)=124.41ms p(99.9)=217.81ms
     iterations.....................: 61844   505.734165/s
     success_rate...................: 100.00% ✓ 61844      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 145506     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 58 MB   477 kB/s
     http_req_blocked...............: avg=5.04µs   min=1.05µs  med=2.88µs   max=4.13ms   p(90)=4.35µs   p(95)=4.89µs   p(99.9)=401.31µs
     http_req_connecting............: avg=1.93µs   min=0s      med=0s       max=4.09ms   p(90)=0s       p(95)=0s       p(99.9)=319.44µs
     http_req_duration..............: avg=123.27ms min=20.92ms med=121.11ms max=332.13ms p(90)=154.53ms p(95)=165.05ms p(99.9)=210.84ms
       { expected_response:true }...: avg=123.27ms min=20.92ms med=121.11ms max=332.13ms p(90)=154.53ms p(95)=165.05ms p(99.9)=210.84ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48602
     http_req_receiving.............: avg=91.14µs  min=29.19µs med=78.19µs  max=83.4ms   p(90)=110.18µs p(95)=121.96µs p(99.9)=583.96µs
     http_req_sending...............: avg=25.31µs  min=5.04µs  med=15.13µs  max=140.85ms p(90)=20.58µs  p(95)=22.43µs  p(99.9)=493.82µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=123.15ms min=20.82ms med=121.02ms max=331.55ms p(90)=154.41ms p(95)=164.92ms p(99.9)=210.76ms
     http_reqs......................: 48602   397.248134/s
     iteration_duration.............: avg=123.75ms min=36.73ms med=121.42ms max=340ms    p(90)=154.79ms p(95)=165.36ms p(99.9)=213.93ms
     iterations.....................: 48502   396.430785/s
     success_rate...................: 100.00% ✓ 48502      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 141348     ✗ 0    
     data_received..................: 4.1 GB  34 MB/s
     data_sent......................: 57 MB   463 kB/s
     http_req_blocked...............: avg=5.29µs   min=1.08µs  med=3.15µs   max=3.65ms   p(90)=4.68µs   p(95)=5.26µs   p(99.9)=338.69µs
     http_req_connecting............: avg=1.95µs   min=0s      med=0s       max=3.62ms   p(90)=0s       p(95)=0s       p(99.9)=204.64µs
     http_req_duration..............: avg=126.89ms min=21.95ms med=125.15ms max=323.72ms p(90)=157.34ms p(95)=167.91ms p(99.9)=217.25ms
       { expected_response:true }...: avg=126.89ms min=21.95ms med=125.15ms max=323.72ms p(90)=157.34ms p(95)=167.91ms p(99.9)=217.25ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 47216
     http_req_receiving.............: avg=174.57µs min=27.79µs med=81.15µs  max=180.33ms p(90)=113.03µs p(95)=125.59µs p(99.9)=2.2ms   
     http_req_sending...............: avg=20.49µs  min=4.98µs  med=15.43µs  max=24.12ms  p(90)=21.09µs  p(95)=23.07µs  p(99.9)=558.83µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=126.69ms min=21.77ms med=125.03ms max=246.14ms p(90)=157.13ms p(95)=167.62ms p(99.9)=210.76ms
     http_reqs......................: 47216   385.744356/s
     iteration_duration.............: avg=127.39ms min=24.93ms med=125.46ms max=360.69ms p(90)=157.64ms p(95)=168.2ms  p(99.9)=221.22ms
     iterations.....................: 47116   384.927378/s
     success_rate...................: 100.00% ✓ 47116      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 95973      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   314 kB/s
     http_req_blocked...............: avg=7.1µs    min=1.49µs  med=3.52µs   max=3.96ms   p(90)=5.09µs   p(95)=5.74µs   p(99.9)=1.86ms  
     http_req_connecting............: avg=3.27µs   min=0s      med=0s       max=3.92ms   p(90)=0s       p(95)=0s       p(99.9)=1.83ms  
     http_req_duration..............: avg=186.82ms min=22.6ms  med=188.77ms max=388.2ms  p(90)=201.82ms p(95)=207.08ms p(99.9)=273.79ms
       { expected_response:true }...: avg=186.82ms min=22.6ms  med=188.77ms max=388.2ms  p(90)=201.82ms p(95)=207.08ms p(99.9)=273.79ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32091
     http_req_receiving.............: avg=105.75µs min=34.37µs med=91.13µs  max=161.25ms p(90)=122.81µs p(95)=135.5µs  p(99.9)=593.15µs
     http_req_sending...............: avg=21.37µs  min=6.23µs  med=17.85µs  max=5.11ms   p(90)=22.91µs  p(95)=24.73µs  p(99.9)=497.8µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=186.69ms min=22.42ms med=188.65ms max=387.83ms p(90)=201.7ms  p(95)=206.97ms p(99.9)=273.34ms
     http_reqs......................: 32091   261.576422/s
     iteration_duration.............: avg=187.65ms min=50.15ms med=189.1ms  max=402.49ms p(90)=202.12ms p(95)=207.42ms p(99.9)=280.26ms
     iterations.....................: 31991   260.761314/s
     success_rate...................: 100.00% ✓ 31991      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 91494      ✗ 0    
     data_received..................: 2.7 GB  22 MB/s
     data_sent......................: 37 MB   301 kB/s
     http_req_blocked...............: avg=12.61µs  min=1.37µs  med=3.76µs   max=9.12ms   p(90)=5.29µs   p(95)=5.93µs   p(99.9)=3.98ms  
     http_req_connecting............: avg=8.39µs   min=0s      med=0s       max=8.97ms   p(90)=0s       p(95)=0s       p(99.9)=3.8ms   
     http_req_duration..............: avg=195.97ms min=18.17ms med=181.39ms max=807.98ms p(90)=225.78ms p(95)=245.79ms p(99.9)=745.72ms
       { expected_response:true }...: avg=195.97ms min=18.17ms med=181.39ms max=807.98ms p(90)=225.78ms p(95)=245.79ms p(99.9)=745.72ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 30598
     http_req_receiving.............: avg=97.19µs  min=36.66µs med=90.96µs  max=15.26ms  p(90)=123.15µs p(95)=135.98µs p(99.9)=899.55µs
     http_req_sending...............: avg=39.42µs  min=6.51µs  med=17.96µs  max=130.71ms p(90)=22.78µs  p(95)=24.69µs  p(99.9)=2ms     
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=195.84ms min=18.02ms med=181.28ms max=807.85ms p(90)=225.65ms p(95)=245.64ms p(99.9)=745.6ms 
     http_reqs......................: 30598   250.541653/s
     iteration_duration.............: avg=196.85ms min=39.92ms med=181.84ms max=808.26ms p(90)=226.13ms p(95)=246.35ms p(99.9)=745.98ms
     iterations.....................: 30498   249.722836/s
     success_rate...................: 100.00% ✓ 30498      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

