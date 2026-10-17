## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-net11 | 16.7.0-p.28 | 1,947 | 2,002 | 1,943 | 1.1% |  |
| fusion-nightly | 16.7.0-p.28 | 1,929 | 1,978 | 1,921 | 1.0% |  |
| fusion | 16.6.8 | 1,893 | 1,951 | 1,883 | 1.2% |  |
| hive-router | v0.3.5 | 1,873 | 1,928 | 1,860 | 1.2% |  |
| fusion-nightly-fed | 16.7.0-p.28 | 1,837 | 1,878 | 1,819 | 1.0% |  |
| caliban | 3.2.0 | 1,429 | 1,484 | 1,424 | 1.5% |  |
| cosmo | 0.359.0 | 1,363 | 1,409 | 1,360 | 1.2% |  |
| grafbase | 0.53.5 | 1,282 | 1,315 | 1,271 | 1.2% |  |
| feddi | e91d605ed222 | 1,175 | 1,212 | 1,169 | 1.2% |  |
| apollo-router | v2.18.0 | 405 | 428 | 393 | 2.5% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 368 | 385 | 365 | 1.9% |  |
| hive-gateway | 2.15.2 | 262 | 269 | 261 | 1.0% |  |
| apollo-gateway | 2.14.4 | 256 | 262 | 255 | 0.8% |  |
| hive-gateway-router-runtime | — | — | — | — | — | benchmark run failed |


### Details

<details>
  <summary>Summary for: fusion-nightly-net11 (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 711954      ✗ 0     
     data_received..................: 21 GB   171 MB/s
     data_sent......................: 285 MB  2.3 MB/s
     http_req_blocked...............: avg=2.93µs   min=852ns   med=1.99µs  max=4.47ms   p(90)=3.84µs  p(95)=4.63µs  p(99.9)=30.64µs
     http_req_connecting............: avg=455ns    min=0s      med=0s      max=4.43ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.05ms  min=16.34ms med=24.46ms max=293.41ms p(90)=29.08ms p(95)=30.87ms p(99.9)=50ms   
       { expected_response:true }...: avg=25.05ms  min=16.34ms med=24.46ms max=293.41ms p(90)=29.08ms p(95)=30.87ms p(99.9)=50ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 237418
     http_req_receiving.............: avg=396.62µs min=50.4µs  med=90.05µs max=154.47ms p(90)=1.15ms  p(95)=1.87ms  p(99.9)=10.61ms
     http_req_sending...............: avg=35.63µs  min=4.56µs  med=8.18µs  max=169.24ms p(90)=18.66µs p(95)=51.48µs p(99.9)=2.23ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=24.62ms  min=16.16ms med=24.06ms max=278.04ms p(90)=28.48ms p(95)=30.21ms p(99.9)=48.13ms
     http_reqs......................: 237418  1947.649825/s
     iteration_duration.............: avg=25.27ms  min=16.61ms med=24.67ms max=305.65ms p(90)=29.28ms p(95)=31.08ms p(99.9)=50.36ms
     iterations.....................: 237318  1946.829479/s
     success_rate...................: 100.00% ✓ 237318      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 705570      ✗ 0     
     data_received..................: 21 GB   169 MB/s
     data_sent......................: 283 MB  2.3 MB/s
     http_req_blocked...............: avg=2.81µs   min=802ns   med=1.93µs  max=3.93ms   p(90)=3.69µs   p(95)=4.47µs  p(99.9)=29.83µs
     http_req_connecting............: avg=376ns    min=0s      med=0s      max=3.91ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.28ms  min=17.01ms med=24.67ms max=301.65ms p(90)=29.65ms  p(95)=31.49ms p(99.9)=48.17ms
       { expected_response:true }...: avg=25.28ms  min=17.01ms med=24.67ms max=301.65ms p(90)=29.65ms  p(95)=31.49ms p(99.9)=48.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 235290
     http_req_receiving.............: avg=371.52µs min=48.86µs med=90.1µs  max=212.1ms  p(90)=996.76µs p(95)=1.65ms  p(99.9)=10.21ms
     http_req_sending...............: avg=33.95µs  min=4.48µs  med=7.99µs  max=107.88ms p(90)=18.06µs  p(95)=47.26µs p(99.9)=2.09ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=24.88ms  min=16.85ms med=24.3ms  max=301.13ms p(90)=29.15ms  p(95)=30.93ms p(99.9)=46.44ms
     http_reqs......................: 235290  1929.959438/s
     iteration_duration.............: avg=25.5ms   min=17.2ms  med=24.88ms max=315.7ms  p(90)=29.85ms  p(95)=31.69ms p(99.9)=48.49ms
     iterations.....................: 235190  1929.139191/s
     success_rate...................: 100.00% ✓ 235190      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 692286      ✗ 0     
     data_received..................: 20 GB   166 MB/s
     data_sent......................: 277 MB  2.3 MB/s
     http_req_blocked...............: avg=3.67µs   min=821ns   med=1.98µs  max=25.34ms  p(90)=3.77µs   p(95)=4.54µs  p(99.9)=33.21µs
     http_req_connecting............: avg=1.17µs   min=0s      med=0s      max=25.29ms  p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.78ms  min=16.8ms  med=25.19ms max=292.4ms  p(90)=30.11ms  p(95)=31.88ms p(99.9)=49.03ms
       { expected_response:true }...: avg=25.78ms  min=16.8ms  med=25.19ms max=292.4ms  p(90)=30.11ms  p(95)=31.88ms p(99.9)=49.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 230862
     http_req_receiving.............: avg=297.71µs min=47.77µs med=89.43µs max=145.66ms p(90)=756.02µs p(95)=1.27ms  p(99.9)=7.37ms 
     http_req_sending...............: avg=31.17µs  min=4.48µs  med=8.27µs  max=141.23ms p(90)=18.25µs  p(95)=35.88µs p(99.9)=1.61ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.45ms  min=16.66ms med=24.88ms max=290.68ms p(90)=29.71ms  p(95)=31.45ms p(99.9)=47.54ms
     http_reqs......................: 230862  1893.288181/s
     iteration_duration.............: avg=25.99ms  min=17.25ms med=25.39ms max=308.91ms p(90)=30.31ms  p(95)=32.08ms p(99.9)=49.42ms
     iterations.....................: 230762  1892.468086/s
     success_rate...................: 100.00% ✓ 230762      ✗ 0     
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

     checks.........................: 100.00% ✓ 685245      ✗ 0     
     data_received..................: 20 GB   164 MB/s
     data_sent......................: 275 MB  2.3 MB/s
     http_req_blocked...............: avg=3.1µs   min=841ns   med=2.22µs  max=4.04ms   p(90)=4.24µs  p(95)=5.05µs   p(99.9)=31.05µs
     http_req_connecting............: avg=410ns   min=0s      med=0s      max=4ms      p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.04ms min=18.22ms med=25.58ms max=307.12ms p(90)=29.72ms p(95)=31.16ms  p(99.9)=47.21ms
       { expected_response:true }...: avg=26.04ms min=18.22ms med=25.58ms max=307.12ms p(90)=29.72ms p(95)=31.16ms  p(99.9)=47.21ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 228515
     http_req_receiving.............: avg=74.45µs min=24.71µs med=49.09µs max=71.38ms  p(90)=97.72µs p(95)=127.04µs p(99.9)=2.15ms 
     http_req_sending...............: avg=33.68µs min=4.58µs  med=9.38µs  max=131.31ms p(90)=18.49µs p(95)=26.95µs  p(99.9)=1.73ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=25.93ms min=18.08ms med=25.49ms max=280.79ms p(90)=29.62ms p(95)=31.04ms  p(99.9)=46.24ms
     http_reqs......................: 228515  1873.797635/s
     iteration_duration.............: avg=26.26ms min=18.41ms med=25.79ms max=316.48ms p(90)=29.93ms p(95)=31.37ms  p(99.9)=47.59ms
     iterations.....................: 228415  1872.977646/s
     success_rate...................: 100.00% ✓ 228415      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 672156      ✗ 0     
     data_received..................: 20 GB   161 MB/s
     data_sent......................: 269 MB  2.2 MB/s
     http_req_blocked...............: avg=3.38µs   min=852ns   med=2.06µs  max=8.7ms    p(90)=4.01µs  p(95)=4.84µs  p(99.9)=33.45µs
     http_req_connecting............: avg=808ns    min=0s      med=0s      max=8.42ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=26.51ms  min=17.41ms med=25.89ms max=294.29ms p(90)=31.1ms  p(95)=33.01ms p(99.9)=51.76ms
       { expected_response:true }...: avg=26.51ms  min=17.41ms med=25.89ms max=294.29ms p(90)=31.1ms  p(95)=33.01ms p(99.9)=51.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 224152
     http_req_receiving.............: avg=373.58µs min=51.05µs med=91.33µs max=32.95ms  p(90)=1.04ms  p(95)=1.77ms  p(99.9)=9.61ms 
     http_req_sending...............: avg=34.92µs  min=4.47µs  med=8.5µs   max=123.46ms p(90)=19.5µs  p(95)=70.24µs p(99.9)=2.11ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=26.1ms   min=17.24ms med=25.5ms  max=283.45ms p(90)=30.59ms p(95)=32.5ms  p(99.9)=50.1ms 
     http_reqs......................: 224152  1837.948244/s
     iteration_duration.............: avg=26.77ms  min=17.89ms med=26.13ms max=305.57ms p(90)=31.34ms p(95)=33.26ms p(99.9)=52.18ms
     iterations.....................: 224052  1837.128288/s
     success_rate...................: 100.00% ✓ 224052      ✗ 0     
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

     checks.........................: 100.00% ✓ 523182      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 210 MB  1.7 MB/s
     http_req_blocked...............: avg=3.61µs  min=962ns   med=2.57µs  max=3.76ms   p(90)=4.76µs   p(95)=5.68µs   p(99.9)=36.68µs
     http_req_connecting............: avg=583ns   min=0s      med=0s      max=3.71ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.15ms min=18.61ms med=33.63ms max=297.08ms p(90)=39.78ms  p(95)=42.01ms  p(99.9)=59.01ms
       { expected_response:true }...: avg=34.15ms min=18.61ms med=33.63ms max=297.08ms p(90)=39.78ms  p(95)=42.01ms  p(99.9)=59.01ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 174494
     http_req_receiving.............: avg=85.97µs min=26.25µs med=63.55µs max=162.74ms p(90)=111.13µs p(95)=136.91µs p(99.9)=1.76ms 
     http_req_sending...............: avg=29.7µs  min=4.92µs  med=11.72µs max=116.53ms p(90)=21.1µs   p(95)=26.51µs  p(99.9)=1.29ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.03ms min=18.48ms med=33.52ms max=296.55ms p(90)=39.66ms  p(95)=41.87ms  p(99.9)=58.54ms
     http_reqs......................: 174494  1429.917865/s
     iteration_duration.............: avg=34.39ms min=21.03ms med=33.86ms max=317.18ms p(90)=40.01ms  p(95)=42.24ms  p(99.9)=59.62ms
     iterations.....................: 174394  1429.0984/s
     success_rate...................: 100.00% ✓ 174394      ✗ 0     
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

     checks.........................: 100.00% ✓ 498972      ✗ 0     
     data_received..................: 15 GB   119 MB/s
     data_sent......................: 200 MB  1.6 MB/s
     http_req_blocked...............: avg=2.9µs   min=982ns   med=2.25µs  max=2.09ms   p(90)=3.98µs   p(95)=4.77µs   p(99.9)=29.73µs
     http_req_connecting............: avg=274ns   min=0s      med=0s      max=2.05ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=35.84ms min=18.78ms med=35.22ms max=305.59ms p(90)=42.86ms  p(95)=45.42ms  p(99.9)=59.42ms
       { expected_response:true }...: avg=35.84ms min=18.78ms med=35.22ms max=305.59ms p(90)=42.86ms  p(95)=45.42ms  p(99.9)=59.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 166424
     http_req_receiving.............: avg=76.45µs min=26.47µs med=60.61µs max=34.07ms  p(90)=102.98µs p(95)=122.75µs p(99.9)=1.25ms 
     http_req_sending...............: avg=26.61µs min=5.01µs  med=10.45µs max=121.21ms p(90)=18.46µs  p(95)=23.14µs  p(99.9)=1.17ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=35.73ms min=18.67ms med=35.13ms max=305.26ms p(90)=42.76ms  p(95)=45.3ms   p(99.9)=58.99ms
     http_reqs......................: 166424  1363.938646/s
     iteration_duration.............: avg=36.06ms min=20.15ms med=35.43ms max=316.28ms p(90)=43.07ms  p(95)=45.61ms  p(99.9)=59.79ms
     iterations.....................: 166324  1363.11909/s
     success_rate...................: 100.00% ✓ 166324      ✗ 0     
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

     checks.........................: 100.00% ✓ 469239      ✗ 0     
     data_received..................: 14 GB   112 MB/s
     data_sent......................: 188 MB  1.5 MB/s
     http_req_blocked...............: avg=3.24µs  min=832ns   med=2.17µs  max=5.3ms    p(90)=4.47µs   p(95)=5.55µs   p(99.9)=44µs   
     http_req_connecting............: avg=475ns   min=0s      med=0s      max=3.09ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=38.09ms min=18.14ms med=37.84ms max=306.03ms p(90)=44.79ms  p(95)=46.84ms  p(99.9)=62.16ms
       { expected_response:true }...: avg=38.09ms min=18.14ms med=37.84ms max=306.03ms p(90)=44.79ms  p(95)=46.84ms  p(99.9)=62.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 156513
     http_req_receiving.............: avg=84.06µs min=25.88µs med=55.25µs max=227.55ms p(90)=122.13µs p(95)=166.44µs p(99.9)=1.65ms 
     http_req_sending...............: avg=32.23µs min=4.61µs  med=9.07µs  max=110.47ms p(90)=22.85µs  p(95)=36.12µs  p(99.9)=2.09ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=37.98ms min=18ms    med=37.73ms max=295.14ms p(90)=44.67ms  p(95)=46.71ms  p(99.9)=61.27ms
     http_reqs......................: 156513  1282.985399/s
     iteration_duration.............: avg=38.35ms min=21.92ms med=38.07ms max=329.92ms p(90)=45.02ms  p(95)=47.05ms  p(99.9)=62.66ms
     iterations.....................: 156413  1282.165668/s
     success_rate...................: 100.00% ✓ 156413      ✗ 0     
     vus............................: 11      min=0         max=50  
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

     checks.........................: 100.00% ✓ 429909      ✗ 0     
     data_received..................: 13 GB   103 MB/s
     data_sent......................: 172 MB  1.4 MB/s
     http_req_blocked...............: avg=3.98µs   min=932ns   med=2.91µs  max=3.94ms   p(90)=5.05µs   p(95)=5.79µs   p(99.9)=36.79µs
     http_req_connecting............: avg=684ns    min=0s      med=0s      max=3.92ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=41.6ms   min=17.56ms med=40.61ms max=292.12ms p(90)=52.29ms  p(95)=56.09ms  p(99.9)=76.52ms
       { expected_response:true }...: avg=41.6ms   min=17.56ms med=40.61ms max=292.12ms p(90)=52.29ms  p(95)=56.09ms  p(99.9)=76.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 143403
     http_req_receiving.............: avg=107.87µs min=26.22µs med=65.18µs max=239.08ms p(90)=111.63µs p(95)=131.12µs p(99.9)=2.35ms 
     http_req_sending...............: avg=29.53µs  min=4.73µs  med=13.02µs max=177.56ms p(90)=22.07µs  p(95)=25.67µs  p(99.9)=1.13ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=41.46ms  min=17.46ms med=40.5ms  max=279.79ms p(90)=52.16ms  p(95)=55.95ms  p(99.9)=74.83ms
     http_reqs......................: 143403  1175.959241/s
     iteration_duration.............: avg=41.86ms  min=18.98ms med=40.85ms max=317.09ms p(90)=52.53ms  p(95)=56.32ms  p(99.9)=77.19ms
     iterations.....................: 143303  1175.139202/s
     success_rate...................: 100.00% ✓ 143303      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 148659     ✗ 0    
     data_received..................: 4.3 GB  36 MB/s
     data_sent......................: 60 MB   487 kB/s
     http_req_blocked...............: avg=4.98µs   min=1.16µs  med=3.02µs   max=3.61ms   p(90)=4.5µs    p(95)=5.06µs   p(99.9)=165.72µs
     http_req_connecting............: avg=1.74µs   min=0s      med=0s       max=3.57ms   p(90)=0s       p(95)=0s       p(99.9)=82.25µs 
     http_req_duration..............: avg=120.63ms min=21.47ms med=118.43ms max=359.06ms p(90)=151.49ms p(95)=161.64ms p(99.9)=210.26ms
       { expected_response:true }...: avg=120.63ms min=21.47ms med=118.43ms max=359.06ms p(90)=151.49ms p(95)=161.64ms p(99.9)=210.26ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49653
     http_req_receiving.............: avg=85.63µs  min=28.29µs med=80.15µs  max=97.07ms  p(90)=112.33µs p(95)=124.62µs p(99.9)=546.23µs
     http_req_sending...............: avg=28.03µs  min=4.94µs  med=16.32µs  max=133.63ms p(90)=21.65µs  p(95)=23.46µs  p(99.9)=508.34µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=120.51ms min=21.33ms med=118.33ms max=358.44ms p(90)=151.38ms p(95)=161.51ms p(99.9)=209.08ms
     http_reqs......................: 49653   405.803345/s
     iteration_duration.............: avg=121.11ms min=49.65ms med=118.73ms max=370.74ms p(90)=151.78ms p(95)=161.93ms p(99.9)=212.86ms
     iterations.....................: 49553   404.986067/s
     success_rate...................: 100.00% ✓ 49553      ✗ 0    
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

     checks.........................: 100.00% ✓ 135141     ✗ 0    
     data_received..................: 3.9 GB  32 MB/s
     data_sent......................: 54 MB   443 kB/s
     http_req_blocked...............: avg=6.62µs   min=1.07µs  med=3.03µs   max=7.64ms   p(90)=4.51µs   p(95)=5.07µs   p(99.9)=378.58µs
     http_req_connecting............: avg=3.27µs   min=0s      med=0s       max=7.56ms   p(90)=0s       p(95)=0s       p(99.9)=207.51µs
     http_req_duration..............: avg=132.71ms min=21.49ms med=130.88ms max=327.08ms p(90)=164.63ms p(95)=175.51ms p(99.9)=224.1ms 
       { expected_response:true }...: avg=132.71ms min=21.49ms med=130.88ms max=327.08ms p(90)=164.63ms p(95)=175.51ms p(99.9)=224.1ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 45147
     http_req_receiving.............: avg=83.79µs  min=29.22µs med=80.97µs  max=7.79ms   p(90)=112.41µs p(95)=124.55µs p(99.9)=513.96µs
     http_req_sending...............: avg=28.46µs  min=5.12µs  med=15.43µs  max=127.21ms p(90)=20.58µs  p(95)=22.46µs  p(99.9)=788.78µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=132.59ms min=21.39ms med=130.78ms max=326.23ms p(90)=164.52ms p(95)=175.38ms p(99.9)=224.02ms
     http_reqs......................: 45147   368.859627/s
     iteration_duration.............: avg=133.22ms min=29.38ms med=131.2ms  max=347.72ms p(90)=164.92ms p(95)=175.83ms p(99.9)=226.93ms
     iterations.....................: 45047   368.042608/s
     success_rate...................: 100.00% ✓ 45047      ✗ 0    
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

     checks.........................: 100.00% ✓ 95868      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   315 kB/s
     http_req_blocked...............: avg=8.75µs   min=1.12µs  med=3.38µs   max=6.05ms   p(90)=4.83µs   p(95)=5.48µs   p(99.9)=2.4ms   
     http_req_connecting............: avg=5.04µs   min=0s      med=0s       max=6.02ms   p(90)=0s       p(95)=0s       p(99.9)=2.27ms  
     http_req_duration..............: avg=187.14ms min=17.97ms med=173.1ms  max=787.39ms p(90)=215.21ms p(95)=234.43ms p(99.9)=730ms   
       { expected_response:true }...: avg=187.14ms min=17.97ms med=173.1ms  max=787.39ms p(90)=215.21ms p(95)=234.43ms p(99.9)=730ms   
     http_req_failed................: 0.00%   ✓ 0          ✗ 32056
     http_req_receiving.............: avg=165.83µs min=32.15µs med=92.93µs  max=188.15ms p(90)=124.36µs p(95)=137.69µs p(99.9)=3.01ms  
     http_req_sending...............: avg=23.44µs  min=5.39µs  med=17.75µs  max=14.82ms  p(90)=22.53µs  p(95)=24.4µs   p(99.9)=1.4ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=186.95ms min=17.77ms med=172.92ms max=787.29ms p(90)=214.94ms p(95)=233.85ms p(99.9)=729.88ms
     http_reqs......................: 32056   262.252786/s
     iteration_duration.............: avg=187.97ms min=49.68ms med=173.52ms max=787.66ms p(90)=215.58ms p(95)=235.02ms p(99.9)=730.3ms 
     iterations.....................: 31956   261.434678/s
     success_rate...................: 100.00% ✓ 31956      ✗ 0    
     vus............................: 40      min=0        max=50 
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

     checks.........................: 100.00% ✓ 94152      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   308 kB/s
     http_req_blocked...............: avg=6.2µs    min=1.16µs  med=3.1µs    max=3.97ms   p(90)=4.53µs   p(95)=5.07µs   p(99.9)=1.07ms  
     http_req_connecting............: avg=2.84µs   min=0s      med=0s       max=3.94ms   p(90)=0s       p(95)=0s       p(99.9)=1.04ms  
     http_req_duration..............: avg=190.46ms min=23.31ms med=158.09ms max=371.87ms p(90)=282.81ms p(95)=287.69ms p(99.9)=354.12ms
       { expected_response:true }...: avg=190.46ms min=23.31ms med=158.09ms max=371.87ms p(90)=282.81ms p(95)=287.69ms p(99.9)=354.12ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31484
     http_req_receiving.............: avg=93.07µs  min=31.23µs med=86.84µs  max=57.52ms  p(90)=117.33µs p(95)=129.36µs p(99.9)=553µs   
     http_req_sending...............: avg=23.11µs  min=5.37µs  med=17.1µs   max=45.92ms  p(90)=21.78µs  p(95)=23.64µs  p(99.9)=1ms     
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=190.34ms min=23.16ms med=157.96ms max=371.72ms p(90)=282.68ms p(95)=287.57ms p(99.9)=354.02ms
     http_reqs......................: 31484   256.617009/s
     iteration_duration.............: avg=191.27ms min=44.05ms med=169.96ms max=378.39ms p(90)=283.1ms  p(95)=287.98ms p(99.9)=354.87ms
     iterations.....................: 31384   255.801938/s
     success_rate...................: 100.00% ✓ 31384      ✗ 0    
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

