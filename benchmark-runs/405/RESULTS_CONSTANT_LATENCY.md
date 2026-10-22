## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| feddi-gateway | 3c75a7db8876 | 2,446 | 2,536 | 2,439 | 1.5% |  |
| fusion-nightly-net-11 | 16.7.0-p.29 | 1,941 | 2,003 | 1,933 | 1.2% |  |
| fusion-nightly-net-10 | 16.7.0-p.29 | 1,931 | 1,980 | 1,917 | 1.1% |  |
| fusion-net-10 | 16.6.8 | 1,885 | 1,937 | 1,871 | 1.2% |  |
| hive-router | v0.3.5 | 1,877 | 1,935 | 1,862 | 1.3% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.29 | 1,833 | 1,896 | 1,820 | 1.3% |  |
| cosmo | 0.359.0 | 1,360 | 1,402 | 1,352 | 1.3% |  |
| caliban | 3.2.0 | 1,288 | 1,347 | 1,282 | 1.8% |  |
| grafbase | 0.53.5 | 1,284 | 1,322 | 1,278 | 1.1% |  |
| hive-gateway-router-runtime | 2.15.2 | 506 | 521 | 504 | 1.4% |  |
| apollo-router | v2.18.0 | 435 | 453 | 434 | 1.6% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 391 | 405 | 384 | 1.5% |  |
| apollo-gateway | 2.14.4 | 261 | 264 | 259 | 0.7% |  |
| hive-gateway | 2.15.2 | 257 | 264 | 255 | 1.1% |  |


### Details

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 890586      ✗ 0     
     data_received..................: 26 GB   214 MB/s
     data_sent......................: 357 MB  2.9 MB/s
     http_req_blocked...............: avg=2.82µs  min=912ns   med=2.03µs  max=7.51ms   p(90)=3.59µs  p(95)=4.52µs   p(99.9)=28.47µs
     http_req_connecting............: avg=345ns   min=0s      med=0s      max=3.76ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=19.99ms min=12.43ms med=19.34ms max=296.7ms  p(90)=23.78ms p(95)=25.88ms  p(99.9)=44.63ms
       { expected_response:true }...: avg=19.99ms min=12.43ms med=19.34ms max=296.7ms  p(90)=23.78ms p(95)=25.88ms  p(99.9)=44.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 296962
     http_req_receiving.............: avg=80.68µs min=24.97µs med=46.14µs max=53.75ms  p(90)=92.6µs  p(95)=146.86µs p(99.9)=4.15ms 
     http_req_sending...............: avg=42.83µs min=4.71µs  med=8.88µs  max=208.54ms p(90)=18.26µs p(95)=88µs     p(99.9)=3.46ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=19.86ms min=12.32ms med=19.24ms max=296.6ms  p(90)=23.64ms p(95)=25.67ms  p(99.9)=43.9ms 
     http_reqs......................: 296962  2446.129729/s
     iteration_duration.............: avg=20.2ms  min=12.63ms med=19.53ms max=326.87ms p(90)=23.99ms p(95)=26.1ms   p(99.9)=45.09ms
     iterations.....................: 296862  2445.306011/s
     success_rate...................: 100.00% ✓ 296862      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.29)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 709620      ✗ 0     
     data_received..................: 21 GB   170 MB/s
     data_sent......................: 284 MB  2.3 MB/s
     http_req_blocked...............: avg=2.78µs   min=831ns   med=1.94µs  max=3.55ms   p(90)=3.76µs  p(95)=4.53µs  p(99.9)=30.14µs
     http_req_connecting............: avg=366ns    min=0s      med=0s      max=3.5ms    p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.14ms  min=17.05ms med=24.58ms max=324.47ms p(90)=29.18ms p(95)=30.94ms p(99.9)=47.89ms
       { expected_response:true }...: avg=25.14ms  min=17.05ms med=24.58ms max=324.47ms p(90)=29.18ms p(95)=30.94ms p(99.9)=47.89ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 236640
     http_req_receiving.............: avg=394.93µs min=50.3µs  med=89.11µs max=65.59ms  p(90)=1.17ms  p(95)=1.92ms  p(99.9)=9.47ms 
     http_req_sending...............: avg=33.01µs  min=4.35µs  med=7.99µs  max=56.7ms   p(90)=18.69µs p(95)=42.95µs p(99.9)=2.06ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=24.71ms  min=16.74ms med=24.18ms max=323.9ms  p(90)=28.58ms p(95)=30.28ms p(99.9)=46.18ms
     http_reqs......................: 236640  1941.193868/s
     iteration_duration.............: avg=25.35ms  min=17.26ms med=24.78ms max=333.54ms p(90)=29.38ms p(95)=31.15ms p(99.9)=48.32ms
     iterations.....................: 236540  1940.373552/s
     success_rate...................: 100.00% ✓ 236540      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-10 (HotChocolate subgraphs) (16.7.0-p.29)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 706161      ✗ 0     
     data_received..................: 21 GB   169 MB/s
     data_sent......................: 283 MB  2.3 MB/s
     http_req_blocked...............: avg=3.23µs   min=841ns   med=1.91µs  max=8.47ms   p(90)=3.57µs  p(95)=4.38µs  p(99.9)=27.84µs
     http_req_connecting............: avg=821ns    min=0s      med=0s      max=8.06ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.26ms  min=16.94ms med=24.66ms max=287.73ms p(90)=29.57ms p(95)=31.37ms p(99.9)=48.42ms
       { expected_response:true }...: avg=25.26ms  min=16.94ms med=24.66ms max=287.73ms p(90)=29.57ms p(95)=31.37ms p(99.9)=48.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 235487
     http_req_receiving.............: avg=360.06µs min=50.29µs med=88.89µs max=57.6ms   p(90)=1.01ms  p(95)=1.69ms  p(99.9)=8.58ms 
     http_req_sending...............: avg=32.76µs  min=4.56µs  med=8.1µs   max=48.38ms  p(90)=17.88µs p(95)=57.3µs  p(99.9)=2.2ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=24.87ms  min=16.57ms med=24.29ms max=283.59ms p(90)=29.07ms p(95)=30.82ms p(99.9)=47.21ms
     http_reqs......................: 235487  1931.823108/s
     iteration_duration.............: avg=25.48ms  min=17.11ms med=24.87ms max=315.84ms p(90)=29.78ms p(95)=31.57ms p(99.9)=48.77ms
     iterations.....................: 235387  1931.002755/s
     success_rate...................: 100.00% ✓ 235387      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 689193      ✗ 0     
     data_received..................: 20 GB   165 MB/s
     data_sent......................: 276 MB  2.3 MB/s
     http_req_blocked...............: avg=2.83µs   min=812ns   med=1.96µs  max=8.29ms   p(90)=3.57µs   p(95)=4.33µs  p(99.9)=29.95µs
     http_req_connecting............: avg=428ns    min=0s      med=0s      max=4.02ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.89ms  min=17.13ms med=25.3ms  max=293.18ms p(90)=30.29ms  p(95)=32.14ms p(99.9)=49.53ms
       { expected_response:true }...: avg=25.89ms  min=17.13ms med=25.3ms  max=293.18ms p(90)=30.29ms  p(95)=32.14ms p(99.9)=49.53ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 229831
     http_req_receiving.............: avg=293.31µs min=49.3µs  med=90.34µs max=192.14ms p(90)=725.67µs p(95)=1.21ms  p(99.9)=8.27ms 
     http_req_sending...............: avg=32.93µs  min=4.36µs  med=8.14µs  max=175.16ms p(90)=17.48µs  p(95)=31.53µs p(99.9)=1.65ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.57ms  min=17.05ms med=25ms    max=292.99ms p(90)=29.89ms  p(95)=31.7ms  p(99.9)=48.3ms 
     http_reqs......................: 229831  1885.002293/s
     iteration_duration.............: avg=26.11ms  min=17.27ms med=25.5ms  max=304.87ms p(90)=30.48ms  p(95)=32.34ms p(99.9)=50.2ms 
     iterations.....................: 229731  1884.182124/s
     success_rate...................: 100.00% ✓ 229731      ✗ 0     
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

     checks.........................: 100.00% ✓ 686361      ✗ 0     
     data_received..................: 20 GB   164 MB/s
     data_sent......................: 275 MB  2.3 MB/s
     http_req_blocked...............: avg=3.18µs  min=852ns   med=2.21µs  max=6.63ms   p(90)=4.21µs  p(95)=5µs      p(99.9)=36.84µs
     http_req_connecting............: avg=465ns   min=0s      med=0s      max=3.85ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26ms    min=17.88ms med=25.53ms max=299.72ms p(90)=29.69ms p(95)=31.12ms  p(99.9)=47.74ms
       { expected_response:true }...: avg=26ms    min=17.88ms med=25.53ms max=299.72ms p(90)=29.69ms p(95)=31.12ms  p(99.9)=47.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 228887
     http_req_receiving.............: avg=75.73µs min=24.84µs med=48.43µs max=130.08ms p(90)=96.35µs p(95)=125.07µs p(99.9)=2.38ms 
     http_req_sending...............: avg=32.19µs min=4.5µs   med=9.06µs  max=189.21ms p(90)=18.7µs  p(95)=26.55µs  p(99.9)=1.44ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=25.89ms min=17.74ms med=25.44ms max=291.03ms p(90)=29.58ms p(95)=31ms     p(99.9)=46.42ms
     http_reqs......................: 228887  1877.324202/s
     iteration_duration.............: avg=26.21ms min=18.28ms med=25.74ms max=308.51ms p(90)=29.9ms  p(95)=31.33ms  p(99.9)=48.35ms
     iterations.....................: 228787  1876.504005/s
     success_rate...................: 100.00% ✓ 228787      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-10 (HotChocolate subgraphs) (16.7.0-p.29)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 670533      ✗ 0     
     data_received..................: 20 GB   161 MB/s
     data_sent......................: 269 MB  2.2 MB/s
     http_req_blocked...............: avg=4.11µs   min=1µs     med=2.57µs  max=9.54ms   p(90)=4.38µs  p(95)=5.18µs  p(99.9)=35.85µs
     http_req_connecting............: avg=1.1µs    min=0s      med=0s      max=9.27ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=26.61ms  min=17.37ms med=25.98ms max=305.87ms p(90)=31.24ms p(95)=33.2ms  p(99.9)=52.5ms 
       { expected_response:true }...: avg=26.61ms  min=17.37ms med=25.98ms max=305.87ms p(90)=31.24ms p(95)=33.2ms  p(99.9)=52.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 223611
     http_req_receiving.............: avg=385.09µs min=50.84µs med=99.91µs max=54.13ms  p(90)=1.07ms  p(95)=1.71ms  p(99.9)=9.79ms 
     http_req_sending...............: avg=37.61µs  min=4.71µs  med=9.52µs  max=181.79ms p(90)=19.42µs p(95)=68.35µs p(99.9)=2.18ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=26.18ms  min=17.17ms med=25.57ms max=305.15ms p(90)=30.71ms p(95)=32.63ms p(99.9)=50.88ms
     http_reqs......................: 223611  1833.671901/s
     iteration_duration.............: avg=26.83ms  min=17.54ms med=26.2ms  max=330.11ms p(90)=31.46ms p(95)=33.41ms p(99.9)=52.8ms 
     iterations.....................: 223511  1832.851873/s
     success_rate...................: 100.00% ✓ 223511      ✗ 0     
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

     checks.........................: 100.00% ✓ 497685      ✗ 0     
     data_received..................: 15 GB   119 MB/s
     data_sent......................: 199 MB  1.6 MB/s
     http_req_blocked...............: avg=3.18µs  min=962ns   med=2.5µs   max=2.57ms   p(90)=4.31µs   p(95)=5.11µs   p(99.9)=38.75µs
     http_req_connecting............: avg=311ns   min=0s      med=0s      max=2.54ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=35.93ms min=19.47ms med=35.31ms max=330.57ms p(90)=42.92ms  p(95)=45.43ms  p(99.9)=59.11ms
       { expected_response:true }...: avg=35.93ms min=19.47ms med=35.31ms max=330.57ms p(90)=42.92ms  p(95)=45.43ms  p(99.9)=59.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 165995
     http_req_receiving.............: avg=78.21µs min=25.87µs med=61.24µs max=22.97ms  p(90)=105.04µs p(95)=126.03µs p(99.9)=1.24ms 
     http_req_sending...............: avg=28.31µs min=4.89µs  med=11.13µs max=156.87ms p(90)=19.2µs   p(95)=24.03µs  p(99.9)=1.15ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=35.83ms min=19.37ms med=35.21ms max=329.76ms p(90)=42.81ms  p(95)=45.32ms  p(99.9)=58.46ms
     http_reqs......................: 165995  1360.215484/s
     iteration_duration.............: avg=36.16ms min=21.23ms med=35.52ms max=343.77ms p(90)=43.13ms  p(95)=45.65ms  p(99.9)=59.44ms
     iterations.....................: 165895  1359.396052/s
     success_rate...................: 100.00% ✓ 165895      ✗ 0     
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

     checks.........................: 100.00% ✓ 471402      ✗ 0     
     data_received..................: 14 GB   113 MB/s
     data_sent......................: 189 MB  1.5 MB/s
     http_req_blocked...............: avg=3.39µs  min=952ns   med=2.42µs  max=3.45ms   p(90)=4.2µs    p(95)=4.98µs   p(99.9)=32.69µs
     http_req_connecting............: avg=605ns   min=0s      med=0s      max=3.41ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=37.95ms min=18.83ms med=37.36ms max=304.73ms p(90)=45.18ms  p(95)=47.78ms  p(99.9)=63.03ms
       { expected_response:true }...: avg=37.95ms min=18.83ms med=37.36ms max=304.73ms p(90)=45.18ms  p(95)=47.78ms  p(99.9)=63.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 157234
     http_req_receiving.............: avg=94.89µs min=27.42µs med=61.4µs  max=243.67ms p(90)=100.69µs p(95)=119.56µs p(99.9)=1.29ms 
     http_req_sending...............: avg=24.53µs min=4.43µs  med=11.06µs max=198.79ms p(90)=18.68µs  p(95)=22.78µs  p(99.9)=1.03ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=37.83ms min=18.72ms med=37.27ms max=304.15ms p(90)=45.07ms  p(95)=47.66ms  p(99.9)=61.61ms
     http_reqs......................: 157234  1288.429266/s
     iteration_duration.............: avg=38.17ms min=21.38ms med=37.57ms max=314.34ms p(90)=45.38ms  p(95)=47.98ms  p(99.9)=63.54ms
     iterations.....................: 157134  1287.609832/s
     success_rate...................: 100.00% ✓ 157134      ✗ 0     
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

     checks.........................: 100.00% ✓ 469932      ✗ 0     
     data_received..................: 14 GB   113 MB/s
     data_sent......................: 188 MB  1.5 MB/s
     http_req_blocked...............: avg=4.54µs  min=952ns   med=3.05µs  max=6.3ms    p(90)=5.42µs   p(95)=6.46µs   p(99.9)=45.01µs
     http_req_connecting............: avg=942ns   min=0s      med=0s      max=6.19ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=38.02ms min=18.29ms med=37.7ms  max=321.77ms p(90)=44.89ms  p(95)=47.08ms  p(99.9)=63.88ms
       { expected_response:true }...: avg=38.02ms min=18.29ms med=37.7ms  max=321.77ms p(90)=44.89ms  p(95)=47.08ms  p(99.9)=63.88ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 156744
     http_req_receiving.............: avg=93µs    min=28.14µs med=62.01µs max=77.47ms  p(90)=129.85µs p(95)=177.79µs p(99.9)=2.28ms 
     http_req_sending...............: avg=37.5µs  min=4.74µs  med=11.6µs  max=139.57ms p(90)=25.06µs  p(95)=58.83µs  p(99.9)=2.23ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=37.89ms min=18.14ms med=37.58ms max=320.09ms p(90)=44.76ms  p(95)=46.93ms  p(99.9)=62.76ms
     http_reqs......................: 156744  1284.931996/s
     iteration_duration.............: avg=38.29ms min=21.59ms med=37.96ms max=332.18ms p(90)=45.12ms  p(95)=47.31ms  p(99.9)=64.56ms
     iterations.....................: 156644  1284.112231/s
     success_rate...................: 100.00% ✓ 156644      ✗ 0     
     vus............................: 4       min=0         max=50  
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

     checks.........................: 100.00% ✓ 185547     ✗ 0    
     data_received..................: 5.4 GB  44 MB/s
     data_sent......................: 74 MB   608 kB/s
     http_req_blocked...............: avg=5.03µs  min=1.09µs  med=3.07µs  max=4.31ms   p(90)=4.61µs   p(95)=5.25µs   p(99.9)=47.73µs 
     http_req_connecting............: avg=1.68µs  min=0s      med=0s      max=4.29ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=96.62ms min=21.23ms med=94.94ms max=314.18ms p(90)=114.48ms p(95)=123.02ms p(99.9)=217.74ms
       { expected_response:true }...: avg=96.62ms min=21.23ms med=94.94ms max=314.18ms p(90)=114.48ms p(95)=123.02ms p(99.9)=217.74ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 61949
     http_req_receiving.............: avg=86.27µs min=26.13µs med=78.91µs max=108.38ms p(90)=112.3µs  p(95)=124.67µs p(99.9)=590.39µs
     http_req_sending...............: avg=26.31µs min=5µs     med=15.24µs max=100.16ms p(90)=21.05µs  p(95)=23.03µs  p(99.9)=575.32µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=96.51ms min=21.06ms med=94.83ms max=313.59ms p(90)=114.36ms p(95)=122.9ms  p(99.9)=217.54ms
     http_reqs......................: 61949   506.59727/s
     iteration_duration.............: avg=97.02ms min=42.09ms med=95.21ms max=342.2ms  p(90)=114.76ms p(95)=123.31ms p(99.9)=220.91ms
     iterations.....................: 61849   505.779505/s
     success_rate...................: 100.00% ✓ 61849      ✗ 0    
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

     checks.........................: 100.00% ✓ 159432     ✗ 0    
     data_received..................: 4.7 GB  38 MB/s
     data_sent......................: 64 MB   523 kB/s
     http_req_blocked...............: avg=4.77µs   min=1.09µs  med=3.31µs   max=2.81ms   p(90)=4.9µs    p(95)=5.51µs   p(99.9)=66.31µs 
     http_req_connecting............: avg=1.24µs   min=0s      med=0s       max=2.78ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=112.47ms min=21.22ms med=110.65ms max=327.57ms p(90)=139.95ms p(95)=149.15ms p(99.9)=190.39ms
       { expected_response:true }...: avg=112.47ms min=21.22ms med=110.65ms max=327.57ms p(90)=139.95ms p(95)=149.15ms p(99.9)=190.39ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 53244
     http_req_receiving.............: avg=91.74µs  min=31.4µs  med=83.74µs  max=114.51ms p(90)=116.47µs p(95)=129.73µs p(99.9)=587.44µs
     http_req_sending...............: avg=29.36µs  min=5.23µs  med=16.77µs  max=202.87ms p(90)=22.36µs  p(95)=24.31µs  p(99.9)=619.04µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=112.35ms min=21.13ms med=110.54ms max=314.45ms p(90)=139.83ms p(95)=149.01ms p(99.9)=189.2ms 
     http_reqs......................: 53244   435.262221/s
     iteration_duration.............: avg=112.92ms min=40ms    med=110.96ms max=344.46ms p(90)=140.22ms p(95)=149.48ms p(99.9)=192.37ms
     iterations.....................: 53144   434.444735/s
     success_rate...................: 100.00% ✓ 53144      ✗ 0    
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

     checks.........................: 100.00% ✓ 143397     ✗ 0    
     data_received..................: 4.2 GB  34 MB/s
     data_sent......................: 58 MB   470 kB/s
     http_req_blocked...............: avg=5.08µs   min=1.02µs  med=3.24µs   max=3.26ms   p(90)=4.77µs   p(95)=5.39µs   p(99.9)=179.71µs
     http_req_connecting............: avg=1.63µs   min=0s      med=0s       max=3.23ms   p(90)=0s       p(95)=0s       p(99.9)=91.84µs 
     http_req_duration..............: avg=125.06ms min=21.73ms med=123.34ms max=326.82ms p(90)=154.53ms p(95)=164.64ms p(99.9)=209.79ms
       { expected_response:true }...: avg=125.06ms min=21.73ms med=123.34ms max=326.82ms p(90)=154.53ms p(95)=164.64ms p(99.9)=209.79ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 47899
     http_req_receiving.............: avg=87.48µs  min=29.13µs med=81.3µs   max=94.52ms  p(90)=112.11µs p(95)=124.26µs p(99.9)=525.36µs
     http_req_sending...............: avg=20.82µs  min=5.13µs  med=16.44µs  max=27.12ms  p(90)=21.78µs  p(95)=23.79µs  p(99.9)=526.46µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=124.96ms min=21.59ms med=123.24ms max=326.44ms p(90)=154.4ms  p(95)=164.56ms p(99.9)=208.74ms
     http_reqs......................: 47899   391.377407/s
     iteration_duration.............: avg=125.55ms min=47.35ms med=123.64ms max=339.74ms p(90)=154.82ms p(95)=164.94ms p(99.9)=211.48ms
     iterations.....................: 47799   390.560318/s
     success_rate...................: 100.00% ✓ 47799      ✗ 0    
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

     checks.........................: 100.00% ✓ 95976      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   314 kB/s
     http_req_blocked...............: avg=7.21µs   min=1.43µs  med=3.66µs   max=4.51ms   p(90)=5.2µs    p(95)=5.85µs   p(99.9)=1.57ms  
     http_req_connecting............: avg=3.25µs   min=0s      med=0s       max=4.47ms   p(90)=0s       p(95)=0s       p(99.9)=1.55ms  
     http_req_duration..............: avg=186.83ms min=23.45ms med=202.29ms max=395.48ms p(90)=240.64ms p(95)=247.71ms p(99.9)=321.51ms
       { expected_response:true }...: avg=186.83ms min=23.45ms med=202.29ms max=395.48ms p(90)=240.64ms p(95)=247.71ms p(99.9)=321.51ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32092
     http_req_receiving.............: avg=92.91µs  min=36.82µs med=87.81µs  max=6.07ms   p(90)=120.34µs p(95)=132.66µs p(99.9)=563.18µs
     http_req_sending...............: avg=33.12µs  min=6.48µs  med=17.59µs  max=106.63ms p(90)=22.72µs  p(95)=24.59µs  p(99.9)=592.4µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=186.71ms min=23.3ms  med=202.12ms max=395.41ms p(90)=240.53ms p(95)=247.59ms p(99.9)=321.39ms
     http_reqs......................: 32092   261.60708/s
     iteration_duration.............: avg=187.64ms min=39.36ms med=206.34ms max=405.06ms p(90)=240.96ms p(95)=248.02ms p(99.9)=323.15ms
     iterations.....................: 31992   260.791901/s
     success_rate...................: 100.00% ✓ 31992      ✗ 0    
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

     checks.........................: 100.00% ✓ 94152      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   309 kB/s
     http_req_blocked...............: avg=6.64µs   min=1.18µs  med=3.39µs   max=4.21ms   p(90)=4.89µs   p(95)=5.51µs   p(99.9)=1.39ms  
     http_req_connecting............: avg=2.99µs   min=0s      med=0s       max=4.17ms   p(90)=0s       p(95)=0s       p(99.9)=1.37ms  
     http_req_duration..............: avg=190.45ms min=17.84ms med=177.25ms max=844.58ms p(90)=220.9ms  p(95)=242.2ms  p(99.9)=749.91ms
       { expected_response:true }...: avg=190.45ms min=17.84ms med=177.25ms max=844.58ms p(90)=220.9ms  p(95)=242.2ms  p(99.9)=749.91ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31484
     http_req_receiving.............: avg=100.38µs min=32.33µs med=91.54µs  max=135.62ms p(90)=122.03µs p(95)=134.94µs p(99.9)=533.58µs
     http_req_sending...............: avg=29.07µs  min=5.68µs  med=17.56µs  max=90.41ms  p(90)=22.32µs  p(95)=24.22µs  p(99.9)=570.82µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=190.32ms min=17.7ms  med=177.11ms max=844.48ms p(90)=220.77ms p(95)=242.05ms p(99.9)=749.83ms
     http_reqs......................: 31484   257.642991/s
     iteration_duration.............: avg=191.29ms min=48.48ms med=177.63ms max=844.83ms p(90)=221.3ms  p(95)=242.76ms p(99.9)=750.26ms
     iterations.....................: 31384   256.824661/s
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

