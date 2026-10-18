## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-net11 | 16.7.0-p.27 | 1,898 | 1,948 | 1,892 | 1.0% |  |
| hive-router | v0.3.5 | 1,889 | 1,954 | 1,876 | 1.4% |  |
| fusion | 16.6.8 | 1,886 | 1,936 | 1,876 | 1.0% |  |
| fusion-nightly | 16.7.0-p.27 | 1,881 | 1,929 | 1,870 | 1.1% |  |
| fusion-nightly-fed | 16.7.0-p.27 | 1,815 | 1,870 | 1,812 | 1.1% |  |
| cosmo | 0.359.0 | 1,352 | 1,402 | 1,345 | 1.5% |  |
| grafbase | 0.53.5 | 1,308 | 1,335 | 1,298 | 1.0% |  |
| caliban | 3.2.0 | 1,277 | 1,330 | 1,267 | 1.8% |  |
| feddi-gateway | e91d605ed222 | 1,120 | 1,158 | 1,114 | 1.2% |  |
| hive-gateway-router-runtime | 2.15.2 | 498 | 514 | 495 | 1.4% |  |
| apollo-router | v2.18.0 | 435 | 452 | 429 | 1.8% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 402 | 418 | 400 | 1.5% |  |
| apollo-gateway | 2.14.4 | 264 | 269 | 262 | 0.9% |  |
| hive-gateway | 2.15.2 | 257 | 263 | 255 | 1.2% |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net11 (HotChocolate subgraphs) (16.7.0-p.27)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 693954      ✗ 0     
     data_received..................: 20 GB   166 MB/s
     data_sent......................: 278 MB  2.3 MB/s
     http_req_blocked...............: avg=2.81µs   min=882ns   med=1.96µs  max=4.18ms   p(90)=3.64µs  p(95)=4.38µs  p(99.9)=28.63µs
     http_req_connecting............: avg=433ns    min=0s      med=0s      max=4.14ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.71ms  min=17.32ms med=25.15ms max=313.76ms p(90)=29.76ms p(95)=31.53ms p(99.9)=49ms   
       { expected_response:true }...: avg=25.71ms  min=17.32ms med=25.15ms max=313.76ms p(90)=29.76ms p(95)=31.53ms p(99.9)=49ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 231418
     http_req_receiving.............: avg=384.07µs min=51.39µs med=91.43µs max=142.77ms p(90)=1.09ms  p(95)=1.77ms  p(99.9)=10.2ms 
     http_req_sending...............: avg=33.45µs  min=4.43µs  med=8.16µs  max=208.43ms p(90)=17.7µs  p(95)=34.93µs p(99.9)=1.96ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.3ms   min=17.16ms med=24.77ms max=313.24ms p(90)=29.21ms p(95)=30.9ms  p(99.9)=47.22ms
     http_reqs......................: 231418  1898.191313/s
     iteration_duration.............: avg=25.93ms  min=17.5ms  med=25.36ms max=334.29ms p(90)=29.96ms p(95)=31.74ms p(99.9)=49.37ms
     iterations.....................: 231318  1897.371069/s
     success_rate...................: 100.00% ✓ 231318      ✗ 0     
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

     checks.........................: 100.00% ✓ 690981      ✗ 0     
     data_received..................: 20 GB   165 MB/s
     data_sent......................: 277 MB  2.3 MB/s
     http_req_blocked...............: avg=3.37µs  min=892ns   med=2.52µs  max=8.11ms   p(90)=4.41µs  p(95)=5.22µs   p(99.9)=35µs   
     http_req_connecting............: avg=417ns   min=0s      med=0s      max=3.71ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=25.81ms min=17.99ms med=25.32ms max=295.95ms p(90)=29.53ms p(95)=30.99ms  p(99.9)=48.71ms
       { expected_response:true }...: avg=25.81ms min=17.99ms med=25.32ms max=295.95ms p(90)=29.53ms p(95)=30.99ms  p(99.9)=48.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 230427
     http_req_receiving.............: avg=78µs    min=24.8µs  med=50.86µs max=129.16ms p(90)=97.13µs p(95)=126.48µs p(99.9)=2.59ms 
     http_req_sending...............: avg=32.89µs min=4.69µs  med=10.03µs max=134.83ms p(90)=19.33µs p(95)=28.7µs   p(99.9)=1.51ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=25.7ms  min=17.93ms med=25.22ms max=283.64ms p(90)=29.41ms p(95)=30.85ms  p(99.9)=47.85ms
     http_reqs......................: 230427  1889.704736/s
     iteration_duration.............: avg=26.04ms min=18.21ms med=25.53ms max=313.24ms p(90)=29.74ms p(95)=31.19ms  p(99.9)=49.29ms
     iterations.....................: 230327  1888.884647/s
     success_rate...................: 100.00% ✓ 230327      ✗ 0     
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

     checks.........................: 100.00% ✓ 689673      ✗ 0     
     data_received..................: 20 GB   165 MB/s
     data_sent......................: 276 MB  2.3 MB/s
     http_req_blocked...............: avg=2.95µs   min=811ns   med=2µs     max=8.34ms   p(90)=3.69µs   p(95)=4.46µs  p(99.9)=33.37µs
     http_req_connecting............: avg=472ns    min=0s      med=0s      max=4.06ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.87ms  min=17.55ms med=25.28ms max=302.82ms p(90)=30.24ms  p(95)=32.07ms p(99.9)=50.71ms
       { expected_response:true }...: avg=25.87ms  min=17.55ms med=25.28ms max=302.82ms p(90)=30.24ms  p(95)=32.07ms p(99.9)=50.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 229991
     http_req_receiving.............: avg=307.34µs min=48.45µs med=91.7µs  max=207.67ms p(90)=779.85µs p(95)=1.27ms  p(99.9)=8.56ms 
     http_req_sending...............: avg=31.27µs  min=4.57µs  med=8.45µs  max=142.21ms p(90)=18.64µs  p(95)=32.87µs p(99.9)=1.67ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.53ms  min=17.18ms med=24.96ms max=302.41ms p(90)=29.83ms  p(95)=31.61ms p(99.9)=49.13ms
     http_reqs......................: 229991  1886.183146/s
     iteration_duration.............: avg=26.09ms  min=17.74ms med=25.49ms max=311.74ms p(90)=30.44ms  p(95)=32.28ms p(99.9)=51.01ms
     iterations.....................: 229891  1885.363035/s
     success_rate...................: 100.00% ✓ 229891      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly (HotChocolate subgraphs) (16.7.0-p.27)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 687996      ✗ 0     
     data_received..................: 20 GB   165 MB/s
     data_sent......................: 276 MB  2.3 MB/s
     http_req_blocked...............: avg=2.88µs   min=902ns   med=1.98µs  max=4.56ms   p(90)=3.57µs   p(95)=4.32µs  p(99.9)=31.06µs
     http_req_connecting............: avg=469ns    min=0s      med=0s      max=4.53ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.94ms  min=16.99ms med=25.32ms max=291.23ms p(90)=30.37ms  p(95)=32.27ms p(99.9)=50.21ms
       { expected_response:true }...: avg=25.94ms  min=16.99ms med=25.32ms max=291.23ms p(90)=30.37ms  p(95)=32.27ms p(99.9)=50.21ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 229432
     http_req_receiving.............: avg=301.06µs min=49.69µs med=91.34µs max=35.56ms  p(90)=755.58µs p(95)=1.26ms  p(99.9)=8.68ms 
     http_req_sending...............: avg=32.73µs  min=4.56µs  med=8.39µs  max=174ms    p(90)=17.58µs  p(95)=31.7µs  p(99.9)=1.69ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.6ms   min=16.91ms med=25.01ms max=290.5ms  p(90)=29.97ms  p(95)=31.83ms p(99.9)=49.16ms
     http_reqs......................: 229432  1881.692509/s
     iteration_duration.............: avg=26.15ms  min=17.16ms med=25.53ms max=317.48ms p(90)=30.57ms  p(95)=32.47ms p(99.9)=50.59ms
     iterations.....................: 229332  1880.872356/s
     success_rate...................: 100.00% ✓ 229332      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed (HotChocolate subgraphs) (16.7.0-p.27)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 664281      ✗ 0     
     data_received..................: 19 GB   159 MB/s
     data_sent......................: 266 MB  2.2 MB/s
     http_req_blocked...............: avg=3.31µs   min=911ns   med=2.5µs   max=3.8ms    p(90)=4.27µs  p(95)=5.02µs  p(99.9)=35.92µs
     http_req_connecting............: avg=399ns    min=0s      med=0s      max=3.59ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=26.86ms  min=17.68ms med=26.28ms max=308.01ms p(90)=31.42ms p(95)=33.31ms p(99.9)=49.74ms
       { expected_response:true }...: avg=26.86ms  min=17.68ms med=26.28ms max=308.01ms p(90)=31.42ms p(95)=33.31ms p(99.9)=49.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 221527
     http_req_receiving.............: avg=328.91µs min=49.38µs med=99.55µs max=195.9ms  p(90)=833.1µs p(95)=1.35ms  p(99.9)=8.59ms 
     http_req_sending...............: avg=32.14µs  min=4.5µs   med=9.61µs  max=91.86ms  p(90)=19.32µs p(95)=36.59µs p(99.9)=1.57ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=26.5ms   min=17.49ms med=25.94ms max=289.67ms p(90)=30.97ms p(95)=32.83ms p(99.9)=48.01ms
     http_reqs......................: 221527  1815.922498/s
     iteration_duration.............: avg=27.08ms  min=17.99ms med=26.49ms max=314.86ms p(90)=31.62ms p(95)=33.52ms p(99.9)=50.19ms
     iterations.....................: 221427  1815.102769/s
     success_rate...................: 100.00% ✓ 221427      ✗ 0     
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

     checks.........................: 100.00% ✓ 494922      ✗ 0     
     data_received..................: 14 GB   118 MB/s
     data_sent......................: 198 MB  1.6 MB/s
     http_req_blocked...............: avg=3.26µs  min=1µs     med=2.35µs  max=3.55ms   p(90)=4.17µs   p(95)=4.96µs   p(99.9)=31.62µs
     http_req_connecting............: avg=528ns   min=0s      med=0s      max=3.51ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=36.13ms min=19.01ms med=35.53ms max=298.86ms p(90)=43.19ms  p(95)=45.7ms   p(99.9)=59.43ms
       { expected_response:true }...: avg=36.13ms min=19.01ms med=35.53ms max=298.86ms p(90)=43.19ms  p(95)=45.7ms   p(99.9)=59.43ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 165074
     http_req_receiving.............: avg=76.52µs min=25.45µs med=60.43µs max=31.82ms  p(90)=103.06µs p(95)=123.96µs p(99.9)=1.14ms 
     http_req_sending...............: avg=26.46µs min=4.57µs  med=10.79µs max=122.46ms p(90)=19.09µs  p(95)=23.72µs  p(99.9)=1.11ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=36.03ms min=18.9ms  med=35.44ms max=298.33ms p(90)=43.09ms  p(95)=45.58ms  p(99.9)=59.04ms
     http_reqs......................: 165074  1352.613042/s
     iteration_duration.............: avg=36.36ms min=20.32ms med=35.74ms max=313.81ms p(90)=43.39ms  p(95)=45.9ms   p(99.9)=59.68ms
     iterations.....................: 164974  1351.793644/s
     success_rate...................: 100.00% ✓ 164974      ✗ 0     
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

     checks.........................: 100.00% ✓ 478692      ✗ 0     
     data_received..................: 14 GB   115 MB/s
     data_sent......................: 192 MB  1.6 MB/s
     http_req_blocked...............: avg=3.39µs  min=881ns   med=2.2µs   max=4.01ms   p(90)=4.63µs   p(95)=5.66µs   p(99.9)=38.74µs
     http_req_connecting............: avg=590ns   min=0s      med=0s      max=3.97ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=37.33ms min=17.68ms med=37.05ms max=319.82ms p(90)=43.85ms  p(95)=45.85ms  p(99.9)=61.82ms
       { expected_response:true }...: avg=37.33ms min=17.68ms med=37.05ms max=319.82ms p(90)=43.85ms  p(95)=45.85ms  p(99.9)=61.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 159664
     http_req_receiving.............: avg=88.85µs min=26.75µs med=55.15µs max=177.78ms p(90)=124.07µs p(95)=166.98µs p(99.9)=2.24ms 
     http_req_sending...............: avg=32.71µs min=4.68µs  med=9.35µs  max=181.46ms p(90)=22.95µs  p(95)=40.16µs  p(99.9)=1.63ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=37.21ms min=17.55ms med=36.95ms max=307.52ms p(90)=43.74ms  p(95)=45.73ms  p(99.9)=60.86ms
     http_reqs......................: 159664  1308.932588/s
     iteration_duration.............: avg=37.59ms min=21.94ms med=37.29ms max=328.25ms p(90)=44.07ms  p(95)=46.07ms  p(99.9)=62.23ms
     iterations.....................: 159564  1308.112784/s
     success_rate...................: 100.00% ✓ 159564      ✗ 0     
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

     checks.........................: 100.00% ✓ 467595      ✗ 0     
     data_received..................: 14 GB   112 MB/s
     data_sent......................: 187 MB  1.5 MB/s
     http_req_blocked...............: avg=3.33µs   min=931ns   med=2.31µs  max=4.96ms   p(90)=3.88µs  p(95)=4.61µs   p(99.9)=38.57µs
     http_req_connecting............: avg=643ns    min=0s      med=0s      max=4.09ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=38.26ms  min=19.01ms med=37.67ms max=314.24ms p(90)=45.68ms p(95)=48.38ms  p(99.9)=64.95ms
       { expected_response:true }...: avg=38.26ms  min=19.01ms med=37.67ms max=314.24ms p(90)=45.68ms p(95)=48.38ms  p(99.9)=64.95ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 155965
     http_req_receiving.............: avg=104.84µs min=27.33µs med=58.51µs max=234.45ms p(90)=95.94µs p(95)=114.36µs p(99.9)=1.47ms 
     http_req_sending...............: avg=24.07µs  min=4.95µs  med=10.84µs max=79.62ms  p(90)=17.47µs p(95)=21.45µs  p(99.9)=1.06ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=38.13ms  min=18.84ms med=37.58ms max=142.18ms p(90)=45.57ms p(95)=48.28ms  p(99.9)=64.29ms
     http_reqs......................: 155965  1277.839685/s
     iteration_duration.............: avg=38.48ms  min=20.81ms med=37.88ms max=323.43ms p(90)=45.89ms p(95)=48.59ms  p(99.9)=65.44ms
     iterations.....................: 155865  1277.020373/s
     success_rate...................: 100.00% ✓ 155865      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 409710      ✗ 0     
     data_received..................: 12 GB   98 MB/s
     data_sent......................: 164 MB  1.3 MB/s
     http_req_blocked...............: avg=3.72µs  min=932ns   med=2.61µs  max=3.92ms   p(90)=4.56µs   p(95)=5.3µs    p(99.9)=41.9µs  
     http_req_connecting............: avg=727ns   min=0s      med=0s      max=3.88ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=43.67ms min=17.26ms med=42.87ms max=305.16ms p(90)=55.6ms   p(95)=59.83ms  p(99.9)=85.45ms 
       { expected_response:true }...: avg=43.67ms min=17.26ms med=42.87ms max=305.16ms p(90)=55.6ms   p(95)=59.83ms  p(99.9)=85.45ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 136670
     http_req_receiving.............: avg=76.43µs min=28.12µs med=64.69µs max=15.2ms   p(90)=107.24µs p(95)=124.29µs p(99.9)=893.04µs
     http_req_sending...............: avg=26.76µs min=4.89µs  med=12.32µs max=112.04ms p(90)=21.06µs  p(95)=24.3µs   p(99.9)=934.08µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=43.56ms min=17.07ms med=42.77ms max=304.83ms p(90)=55.5ms   p(95)=59.73ms  p(99.9)=85.17ms 
     http_reqs......................: 136670  1120.783094/s
     iteration_duration.............: avg=43.92ms min=18.03ms med=43.11ms max=313.9ms  p(90)=55.83ms  p(95)=60.07ms  p(99.9)=86.21ms 
     iterations.....................: 136570  1119.963029/s
     success_rate...................: 100.00% ✓ 136570      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 182616     ✗ 0    
     data_received..................: 5.3 GB  44 MB/s
     data_sent......................: 73 MB   599 kB/s
     http_req_blocked...............: avg=5.52µs  min=1.3µs   med=3.44µs  max=4.59ms   p(90)=5.09µs   p(95)=5.81µs   p(99.9)=51.77µs 
     http_req_connecting............: avg=1.78µs  min=0s      med=0s      max=4.55ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=98.19ms min=21.71ms med=94.06ms max=318.87ms p(90)=129.32ms p(95)=141.29ms p(99.9)=239.76ms
       { expected_response:true }...: avg=98.19ms min=21.71ms med=94.06ms max=318.87ms p(90)=129.32ms p(95)=141.29ms p(99.9)=239.76ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 60972
     http_req_receiving.............: avg=94.59µs min=34.16µs med=82.04µs max=178.44ms p(90)=116.3µs  p(95)=129.84µs p(99.9)=634.5µs 
     http_req_sending...............: avg=22.19µs min=5.18µs  med=16.09µs max=40.08ms  p(90)=22.42µs  p(95)=24.65µs  p(99.9)=638.3µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=98.07ms min=21.56ms med=93.95ms max=318.12ms p(90)=129.2ms  p(95)=141.15ms p(99.9)=239.24ms
     http_reqs......................: 60972   498.452543/s
     iteration_duration.............: avg=98.59ms min=37.47ms med=94.34ms max=348.17ms p(90)=129.61ms p(95)=141.62ms p(99.9)=243.18ms
     iterations.....................: 60872   497.635032/s
     success_rate...................: 100.00% ✓ 60872      ✗ 0    
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

     checks.........................: 100.00% ✓ 159366     ✗ 0    
     data_received..................: 4.7 GB  38 MB/s
     data_sent......................: 64 MB   522 kB/s
     http_req_blocked...............: avg=5.7µs    min=1.15µs  med=3.33µs   max=3.98ms   p(90)=4.86µs   p(95)=5.46µs   p(99.9)=109.36µs
     http_req_connecting............: avg=2.1µs    min=0s      med=0s       max=3.94ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=112.51ms min=21.29ms med=110.8ms  max=326.24ms p(90)=140.16ms p(95)=149.09ms p(99.9)=188.35ms
       { expected_response:true }...: avg=112.51ms min=21.29ms med=110.8ms  max=326.24ms p(90)=140.16ms p(95)=149.09ms p(99.9)=188.35ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 53222
     http_req_receiving.............: avg=91.32µs  min=29.51µs med=85.25µs  max=105.29ms p(90)=116.2µs  p(95)=128.65µs p(99.9)=558.22µs
     http_req_sending...............: avg=22.56µs  min=5.24µs  med=17.03µs  max=78ms     p(90)=22.49µs  p(95)=24.45µs  p(99.9)=521.41µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=112.4ms  min=21.15ms med=110.69ms max=306.41ms p(90)=140.06ms p(95)=148.97ms p(99.9)=188.15ms
     http_reqs......................: 53222   435.068011/s
     iteration_duration.............: avg=112.97ms min=47.13ms med=111.11ms max=343.5ms  p(90)=140.45ms p(95)=149.36ms p(99.9)=190.5ms 
     iterations.....................: 53122   434.250552/s
     success_rate...................: 100.00% ✓ 53122      ✗ 0    
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

     checks.........................: 100.00% ✓ 147447     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 59 MB   483 kB/s
     http_req_blocked...............: avg=5.25µs   min=1.13µs  med=3.24µs   max=3.52ms   p(90)=4.83µs   p(95)=5.43µs   p(99.9)=162.18µs
     http_req_connecting............: avg=1.78µs   min=0s      med=0s       max=3.48ms   p(90)=0s       p(95)=0s       p(99.9)=84.94µs 
     http_req_duration..............: avg=121.62ms min=21.54ms med=120.07ms max=342.83ms p(90)=150.08ms p(95)=159.91ms p(99.9)=204.73ms
       { expected_response:true }...: avg=121.62ms min=21.54ms med=120.07ms max=342.83ms p(90)=150.08ms p(95)=159.91ms p(99.9)=204.73ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49249
     http_req_receiving.............: avg=90.57µs  min=29.4µs  med=84.11µs  max=102.96ms p(90)=115.68µs p(95)=128.7µs  p(99.9)=539.48µs
     http_req_sending...............: avg=24.22µs  min=5.05µs  med=16.38µs  max=102.73ms p(90)=21.67µs  p(95)=23.61µs  p(99.9)=551.99µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=121.5ms  min=21.45ms med=119.96ms max=319.28ms p(90)=149.95ms p(95)=159.8ms  p(99.9)=204.46ms
     http_reqs......................: 49249   402.457002/s
     iteration_duration.............: avg=122.11ms min=28.41ms med=120.37ms max=352.83ms p(90)=150.38ms p(95)=160.21ms p(99.9)=206.67ms
     iterations.....................: 49149   401.639814/s
     success_rate...................: 100.00% ✓ 49149      ✗ 0    
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

     checks.........................: 100.00% ✓ 97014      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   318 kB/s
     http_req_blocked...............: avg=7.59µs   min=1.11µs  med=3.5µs    max=7.68ms   p(90)=5.05µs   p(95)=5.68µs   p(99.9)=1.09ms  
     http_req_connecting............: avg=3.47µs   min=0s      med=0s       max=6.33ms   p(90)=0s       p(95)=0s       p(99.9)=932.86µs
     http_req_duration..............: avg=184.85ms min=23.34ms med=202.95ms max=361.56ms p(90)=241.21ms p(95)=246.86ms p(99.9)=312.52ms
       { expected_response:true }...: avg=184.85ms min=23.34ms med=202.95ms max=361.56ms p(90)=241.21ms p(95)=246.86ms p(99.9)=312.52ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32438
     http_req_receiving.............: avg=97.19µs  min=31.45µs med=91.58µs  max=73.52ms  p(90)=122.23µs p(95)=134.78µs p(99.9)=462.38µs
     http_req_sending...............: avg=28.43µs  min=5.48µs  med=17.17µs  max=68.18ms  p(90)=21.99µs  p(95)=23.9µs   p(99.9)=1.83ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.73ms min=23.23ms med=202.84ms max=359.97ms p(90)=241.08ms p(95)=246.75ms p(99.9)=312.31ms
     http_reqs......................: 32438   264.428783/s
     iteration_duration.............: avg=185.64ms min=62.76ms med=204.16ms max=376.5ms  p(90)=241.49ms p(95)=247.2ms  p(99.9)=314.19ms
     iterations.....................: 32338   263.613601/s
     success_rate...................: 100.00% ✓ 32338      ✗ 0    
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

     checks.........................: 100.00% ✓ 93840      ✗ 0    
     data_received..................: 2.7 GB  23 MB/s
     data_sent......................: 38 MB   309 kB/s
     http_req_blocked...............: avg=7.34µs   min=1.53µs  med=3.8µs    max=4.33ms   p(90)=5.4µs    p(95)=6.09µs   p(99.9)=1.46ms  
     http_req_connecting............: avg=3.24µs   min=0s      med=0s       max=4.29ms   p(90)=0s       p(95)=0s       p(99.9)=1.43ms  
     http_req_duration..............: avg=191.05ms min=18.03ms med=175.17ms max=823.58ms p(90)=239.11ms p(95)=272.27ms p(99.9)=722.2ms 
       { expected_response:true }...: avg=191.05ms min=18.03ms med=175.17ms max=823.58ms p(90)=239.11ms p(95)=272.27ms p(99.9)=722.2ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 31380
     http_req_receiving.............: avg=110.77µs min=34.91µs med=91.22µs  max=101.27ms p(90)=123.89µs p(95)=137.96µs p(99.9)=638.79µs
     http_req_sending...............: avg=28.52µs  min=6.71µs  med=18.47µs  max=135.81ms p(90)=23.71µs  p(95)=25.85µs  p(99.9)=510.8µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=190.91ms min=17.93ms med=175.03ms max=823.48ms p(90)=238.98ms p(95)=272.06ms p(99.9)=722.08ms
     http_reqs......................: 31380   257.015011/s
     iteration_duration.............: avg=191.92ms min=34.52ms med=175.6ms  max=823.84ms p(90)=239.57ms p(95)=273.23ms p(99.9)=722.51ms
     iterations.....................: 31280   256.19597/s
     success_rate...................: 100.00% ✓ 31280      ✗ 0    
     vus............................: 48      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

