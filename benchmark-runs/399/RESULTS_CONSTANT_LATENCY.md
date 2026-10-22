## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 2 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 1 runs are measured. Results are ranked by **median RPS** across the 1 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-net-11 | 16.7.0-p.27 | 1,945 | 1,945 | 1,945 | 0.0% |  |
| fusion-nightly-net-10 | 16.7.0-p.27 | 1,941 | 1,941 | 1,941 | 0.0% |  |
| fusion-net-10 | 16.6.8 | 1,940 | 1,940 | 1,940 | 0.0% |  |
| hive-router | v0.3.5 | 1,931 | 1,931 | 1,931 | 0.0% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.27 | 1,872 | 1,872 | 1,872 | 0.0% |  |
| cosmo | 0.359.0 | 1,376 | 1,376 | 1,376 | 0.0% |  |
| caliban | 3.2.0 | 1,374 | 1,374 | 1,374 | 0.0% |  |
| grafbase | 0.53.5 | 1,337 | 1,337 | 1,337 | 0.0% |  |
| feddi-gateway | e91d605ed222 | 1,165 | 1,165 | 1,165 | 0.0% |  |
| hive-gateway-router-runtime | 2.15.2 | 513 | 513 | 513 | 0.0% |  |
| apollo-router | v2.18.0 | 453 | 453 | 453 | 0.0% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 415 | 415 | 415 | 0.0% |  |
| hive-gateway | 2.15.2 | 268 | 268 | 268 | 0.0% |  |
| apollo-gateway | 2.14.4 | 266 | 266 | 266 | 0.0% |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.27)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 711165      ✗ 0     
     data_received..................: 21 GB   171 MB/s
     data_sent......................: 285 MB  2.3 MB/s
     http_req_blocked...............: avg=2.7µs    min=852ns   med=1.93µs  max=4.03ms   p(90)=3.25µs   p(95)=3.9µs   p(99.9)=25.18µs
     http_req_connecting............: avg=435ns    min=0s      med=0s      max=3.99ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.09ms  min=17.05ms med=24.62ms max=296.13ms p(90)=28.87ms  p(95)=30.4ms  p(99.9)=41.94ms
       { expected_response:true }...: avg=25.09ms  min=17.05ms med=24.62ms max=296.13ms p(90)=28.87ms  p(95)=30.4ms  p(99.9)=41.94ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 237155
     http_req_receiving.............: avg=345.78µs min=47.95µs med=91.83µs max=66.8ms   p(90)=992.43µs p(95)=1.57ms  p(99.9)=7.03ms 
     http_req_sending...............: avg=27.03µs  min=4.11µs  med=8.15µs  max=120.8ms  p(90)=16.16µs  p(95)=29.44µs p(99.9)=1.32ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=24.71ms  min=16.97ms med=24.26ms max=295.81ms p(90)=28.36ms  p(95)=29.86ms p(99.9)=40.63ms
     http_reqs......................: 237155  1945.757195/s
     iteration_duration.............: avg=25.3ms   min=17.21ms med=24.82ms max=304.6ms  p(90)=29.07ms  p(95)=30.6ms  p(99.9)=42.28ms
     iterations.....................: 237055  1944.936737/s
     success_rate...................: 100.00% ✓ 237055      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 709584      ✗ 0     
     data_received..................: 21 GB   170 MB/s
     data_sent......................: 284 MB  2.3 MB/s
     http_req_blocked...............: avg=2.65µs  min=881ns   med=1.91µs  max=3.5ms    p(90)=3.27µs  p(95)=3.95µs  p(99.9)=25.99µs
     http_req_connecting............: avg=391ns   min=0s      med=0s      max=3.46ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.14ms min=16.89ms med=24.64ms max=309.28ms p(90)=29.21ms p(95)=30.85ms p(99.9)=43.82ms
       { expected_response:true }...: avg=25.14ms min=16.89ms med=24.64ms max=309.28ms p(90)=29.21ms p(95)=30.85ms p(99.9)=43.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 236628
     http_req_receiving.............: avg=291.8µs min=49.53µs med=95.47µs max=111.19ms p(90)=757.1µs p(95)=1.17ms  p(99.9)=5.6ms  
     http_req_sending...............: avg=26.14µs min=4.51µs  med=8.21µs  max=100.75ms p(90)=15.7µs  p(95)=28.52µs p(99.9)=1.21ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=24.83ms min=16.79ms med=24.34ms max=309.08ms p(90)=28.81ms p(95)=30.43ms p(99.9)=42.13ms
     http_reqs......................: 236628  1941.397469/s
     iteration_duration.............: avg=25.35ms min=17.11ms med=24.84ms max=324.34ms p(90)=29.4ms  p(95)=31.05ms p(99.9)=44.29ms
     iterations.....................: 236528  1940.577026/s
     success_rate...................: 100.00% ✓ 236528      ✗ 0     
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

     checks.........................: 100.00% ✓ 709113      ✗ 0     
     data_received..................: 21 GB   170 MB/s
     data_sent......................: 284 MB  2.3 MB/s
     http_req_blocked...............: avg=3.4µs    min=841ns   med=1.97µs  max=8.94ms   p(90)=3.51µs   p(95)=4.22µs  p(99.9)=27.44µs
     http_req_connecting............: avg=1.04µs   min=0s      med=0s      max=8.75ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.16ms  min=17.07ms med=24.66ms max=288.94ms p(90)=29.2ms   p(95)=30.81ms p(99.9)=43.11ms
       { expected_response:true }...: avg=25.16ms  min=17.07ms med=24.66ms max=288.94ms p(90)=29.2ms   p(95)=30.81ms p(99.9)=43.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 236471
     http_req_receiving.............: avg=293.09µs min=48.59µs med=95.93µs max=223.83ms p(90)=754.47µs p(95)=1.17ms  p(99.9)=5.83ms 
     http_req_sending...............: avg=26.8µs   min=4.51µs  med=8.24µs  max=225.6ms  p(90)=16.55µs  p(95)=25.19µs p(99.9)=1.16ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=24.84ms  min=16.99ms med=24.35ms max=288.01ms p(90)=28.8ms   p(95)=30.42ms p(99.9)=41.54ms
     http_reqs......................: 236471  1940.130962/s
     iteration_duration.............: avg=25.37ms  min=17.2ms  med=24.87ms max=302.36ms p(90)=29.39ms  p(95)=31ms    p(99.9)=43.47ms
     iterations.....................: 236371  1939.31051/s
     success_rate...................: 100.00% ✓ 236371      ✗ 0     
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

     checks.........................: 100.00% ✓ 706038      ✗ 0     
     data_received..................: 21 GB   169 MB/s
     data_sent......................: 283 MB  2.3 MB/s
     http_req_blocked...............: avg=4.11µs  min=961ns   med=2.49µs  max=9.51ms   p(90)=4.1µs   p(95)=4.81µs   p(99.9)=36.35µs
     http_req_connecting............: avg=1.2µs   min=0s      med=0s      max=9.46ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=25.26ms min=17.85ms med=24.86ms max=300.52ms p(90)=28.83ms p(95)=30.11ms  p(99.9)=43.73ms
       { expected_response:true }...: avg=25.26ms min=17.85ms med=24.86ms max=300.52ms p(90)=28.83ms p(95)=30.11ms  p(99.9)=43.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 235446
     http_req_receiving.............: avg=72.48µs min=25.57µs med=51.92µs max=211.41ms p(90)=95.78µs p(95)=122.99µs p(99.9)=1.19ms 
     http_req_sending...............: avg=30.26µs min=4.43µs  med=9.94µs  max=196.32ms p(90)=18.32µs p(95)=26µs     p(99.9)=1.2ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=25.16ms min=17.8ms  med=24.77ms max=295.78ms p(90)=28.73ms p(95)=29.99ms  p(99.9)=42.17ms
     http_reqs......................: 235446  1931.403605/s
     iteration_duration.............: avg=25.48ms min=18.04ms med=25.07ms max=311.61ms p(90)=29.04ms p(95)=30.31ms  p(99.9)=44.06ms
     iterations.....................: 235346  1930.583288/s
     success_rate...................: 100.00% ✓ 235346      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 684450      ✗ 0     
     data_received..................: 20 GB   164 MB/s
     data_sent......................: 274 MB  2.2 MB/s
     http_req_blocked...............: avg=2.73µs   min=832ns   med=1.93µs  max=3.39ms   p(90)=3.55µs   p(95)=4.25µs  p(99.9)=27.39µs
     http_req_connecting............: avg=411ns    min=0s      med=0s      max=3.35ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=26.07ms  min=17.5ms  med=25.6ms  max=283.45ms p(90)=30.24ms  p(95)=31.83ms p(99.9)=43.1ms 
       { expected_response:true }...: avg=26.07ms  min=17.5ms  med=25.6ms  max=283.45ms p(90)=30.24ms  p(95)=31.83ms p(99.9)=43.1ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 228250
     http_req_receiving.............: avg=272.79µs min=48.96µs med=94µs    max=143.33ms p(90)=692.82µs p(95)=1.11ms  p(99.9)=5.7ms  
     http_req_sending...............: avg=26.83µs  min=4.31µs  med=8.3µs   max=143.12ms p(90)=18.22µs  p(95)=28.34µs p(99.9)=1.16ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.77ms  min=17.35ms med=25.31ms max=283.26ms p(90)=29.87ms  p(95)=31.43ms p(99.9)=41.72ms
     http_reqs......................: 228250  1872.23824/s
     iteration_duration.............: avg=26.29ms  min=17.71ms med=25.8ms  max=312ms    p(90)=30.44ms  p(95)=32.03ms p(99.9)=43.36ms
     iterations.....................: 228150  1871.417982/s
     success_rate...................: 100.00% ✓ 228150      ✗ 0     
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

     checks.........................: 100.00% ✓ 503400      ✗ 0     
     data_received..................: 15 GB   120 MB/s
     data_sent......................: 202 MB  1.7 MB/s
     http_req_blocked...............: avg=3.03µs  min=842ns   med=2.1µs   max=3.8ms    p(90)=3.67µs  p(95)=4.38µs   p(99.9)=34.03µs 
     http_req_connecting............: avg=583ns   min=0s      med=0s      max=3.76ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.53ms min=18.12ms med=34.92ms max=315.89ms p(90)=42.56ms p(95)=45.06ms  p(99.9)=57.99ms 
       { expected_response:true }...: avg=35.53ms min=18.12ms med=34.92ms max=315.89ms p(90)=42.56ms p(95)=45.06ms  p(99.9)=57.99ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 167900
     http_req_receiving.............: avg=73.28µs min=24.96µs med=58.49µs max=206.38ms p(90)=99.21µs p(95)=118.65µs p(99.9)=775.19µs
     http_req_sending...............: avg=25.36µs min=4.58µs  med=9.73µs  max=232.15ms p(90)=16.82µs p(95)=21µs     p(99.9)=798.63µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=35.43ms min=17.99ms med=34.83ms max=305.46ms p(90)=42.47ms p(95)=44.96ms  p(99.9)=57.65ms 
     http_reqs......................: 167900  1376.384428/s
     iteration_duration.............: avg=35.75ms min=20.86ms med=35.12ms max=323.76ms p(90)=42.75ms p(95)=45.26ms  p(99.9)=58.28ms 
     iterations.....................: 167800  1375.564664/s
     success_rate...................: 100.00% ✓ 167800      ✗ 0     
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

     checks.........................: 100.00% ✓ 502722      ✗ 0     
     data_received..................: 15 GB   120 MB/s
     data_sent......................: 202 MB  1.7 MB/s
     http_req_blocked...............: avg=4.04µs  min=921ns   med=2.19µs  max=8.47ms   p(90)=3.75µs  p(95)=4.46µs   p(99.9)=33.84µs 
     http_req_connecting............: avg=1.34µs  min=0s      med=0s      max=8.32ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.57ms min=18.76ms med=35.05ms max=279.43ms p(90)=41.96ms p(95)=44.3ms   p(99.9)=56.79ms 
       { expected_response:true }...: avg=35.57ms min=18.76ms med=35.05ms max=279.43ms p(90)=41.96ms p(95)=44.3ms   p(99.9)=56.79ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 167674
     http_req_receiving.............: avg=85.87µs min=26.57µs med=56.51µs max=202.21ms p(90)=92.81µs p(95)=108.73µs p(99.9)=869.97µs
     http_req_sending...............: avg=21.56µs min=4.69µs  med=10.47µs max=90.33ms  p(90)=16.79µs p(95)=20.53µs  p(99.9)=788.5µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=35.47ms min=18.66ms med=34.97ms max=278.47ms p(90)=41.87ms p(95)=44.22ms  p(99.9)=56.49ms 
     http_reqs......................: 167674  1374.232608/s
     iteration_duration.............: avg=35.79ms min=21.43ms med=35.26ms max=319.61ms p(90)=42.16ms p(95)=44.5ms   p(99.9)=57.06ms 
     iterations.....................: 167574  1373.413022/s
     success_rate...................: 100.00% ✓ 167574      ✗ 0     
     vus............................: 49      min=0         max=50  
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

     checks.........................: 100.00% ✓ 488925      ✗ 0     
     data_received..................: 14 GB   117 MB/s
     data_sent......................: 196 MB  1.6 MB/s
     http_req_blocked...............: avg=3.94µs  min=902ns   med=2.82µs  max=5.44ms   p(90)=5.17µs   p(95)=6.18µs   p(99.9)=42.89µs
     http_req_connecting............: avg=570ns   min=0s      med=0s      max=4.08ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=36.54ms min=17.84ms med=36.35ms max=309.33ms p(90)=43.02ms  p(95)=44.96ms  p(99.9)=56.18ms
       { expected_response:true }...: avg=36.54ms min=17.84ms med=36.35ms max=309.33ms p(90)=43.02ms  p(95)=44.96ms  p(99.9)=56.18ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 163075
     http_req_receiving.............: avg=84.25µs min=25.55µs med=57.37µs max=122.9ms  p(90)=121.96µs p(95)=169.63µs p(99.9)=1.76ms 
     http_req_sending...............: avg=35.73µs min=4.69µs  med=10.64µs max=265.07ms p(90)=23.53µs  p(95)=73.53µs  p(99.9)=1.74ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=36.42ms min=17.75ms med=36.24ms max=308.67ms p(90)=42.9ms   p(95)=44.84ms  p(99.9)=55.74ms
     http_reqs......................: 163075  1337.105257/s
     iteration_duration.............: avg=36.8ms  min=20.78ms med=36.6ms  max=327.5ms  p(90)=43.24ms  p(95)=45.18ms  p(99.9)=56.66ms
     iterations.....................: 162975  1336.285324/s
     success_rate...................: 100.00% ✓ 162975      ✗ 0     
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

     checks.........................: 100.00% ✓ 426108      ✗ 0     
     data_received..................: 12 GB   102 MB/s
     data_sent......................: 171 MB  1.4 MB/s
     http_req_blocked...............: avg=3.62µs  min=951ns   med=2.62µs  max=3.85ms   p(90)=4.6µs    p(95)=5.34µs   p(99.9)=40.44µs 
     http_req_connecting............: avg=635ns   min=0s      med=0s      max=3.8ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=41.98ms min=17.69ms med=41.01ms max=291.86ms p(90)=53.03ms  p(95)=57.02ms  p(99.9)=79.8ms  
       { expected_response:true }...: avg=41.98ms min=17.69ms med=41.01ms max=291.86ms p(90)=53.03ms  p(95)=57.02ms  p(99.9)=79.8ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 142136
     http_req_receiving.............: avg=74.85µs min=26.77µs med=62.12µs max=77.99ms  p(90)=103.97µs p(95)=120.94µs p(99.9)=1ms     
     http_req_sending...............: avg=23.39µs min=4.77µs  med=11.98µs max=136.96ms p(90)=20.61µs  p(95)=23.77µs  p(99.9)=757.32µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=41.88ms min=17.55ms med=40.91ms max=291.24ms p(90)=52.92ms  p(95)=56.93ms  p(99.9)=79.52ms 
     http_reqs......................: 142136  1165.702572/s
     iteration_duration.............: avg=42.23ms min=19.71ms med=41.24ms max=312.9ms  p(90)=53.25ms  p(95)=57.25ms  p(99.9)=80.3ms  
     iterations.....................: 142036  1164.88244/s
     success_rate...................: 100.00% ✓ 142036      ✗ 0     
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

     checks.........................: 100.00% ✓ 187977     ✗ 0    
     data_received..................: 5.5 GB  45 MB/s
     data_sent......................: 75 MB   616 kB/s
     http_req_blocked...............: avg=4.51µs  min=1.03µs  med=2.74µs  max=3.53ms   p(90)=4.16µs   p(95)=4.75µs   p(99.9)=50.19µs 
     http_req_connecting............: avg=1.54µs  min=0s      med=0s      max=3.49ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=95.42ms min=20.35ms med=93.62ms max=326.87ms p(90)=113.77ms p(95)=123.66ms p(99.9)=213.42ms
       { expected_response:true }...: avg=95.42ms min=20.35ms med=93.62ms max=326.87ms p(90)=113.77ms p(95)=123.66ms p(99.9)=213.42ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 62759
     http_req_receiving.............: avg=80.93µs min=27.85µs med=72.1µs  max=137.86ms p(90)=105.36µs p(95)=117.18µs p(99.9)=564.25µs
     http_req_sending...............: avg=23.8µs  min=4.76µs  med=13.78µs max=137.76ms p(90)=19.27µs  p(95)=21.19µs  p(99.9)=503.05µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=95.31ms min=20.2ms  med=93.52ms max=326.58ms p(90)=113.67ms p(95)=123.54ms p(99.9)=213.18ms
     http_reqs......................: 62759   513.220478/s
     iteration_duration.............: avg=95.77ms min=35.62ms med=93.87ms max=334.69ms p(90)=114.02ms p(95)=123.92ms p(99.9)=215.92ms
     iterations.....................: 62659   512.402714/s
     success_rate...................: 100.00% ✓ 62659      ✗ 0    
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

     checks.........................: 100.00% ✓ 166014     ✗ 0    
     data_received..................: 4.8 GB  40 MB/s
     data_sent......................: 67 MB   544 kB/s
     http_req_blocked...............: avg=5.14µs   min=1.05µs  med=3.02µs   max=3.89ms   p(90)=4.55µs   p(95)=5.13µs   p(99.9)=90.45µs 
     http_req_connecting............: avg=1.88µs   min=0s      med=0s       max=3.85ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=108.02ms min=20.61ms med=106.45ms max=322.77ms p(90)=133.98ms p(95)=142.79ms p(99.9)=183.06ms
       { expected_response:true }...: avg=108.02ms min=20.61ms med=106.45ms max=322.77ms p(90)=133.98ms p(95)=142.79ms p(99.9)=183.06ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 55438
     http_req_receiving.............: avg=85.45µs  min=29.19µs med=78.59µs  max=162.21ms p(90)=108.41µs p(95)=120.1µs  p(99.9)=514.34µs
     http_req_sending...............: avg=23.59µs  min=5.3µs   med=15.38µs  max=142.56ms p(90)=20.43µs  p(95)=22.3µs   p(99.9)=495.49µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=107.91ms min=20.48ms med=106.36ms max=322.4ms  p(90)=133.88ms p(95)=142.69ms p(99.9)=182.51ms
     http_reqs......................: 55438   453.354256/s
     iteration_duration.............: avg=108.45ms min=36.61ms med=106.73ms max=332.36ms p(90)=134.26ms p(95)=143.08ms p(99.9)=185.48ms
     iterations.....................: 55338   452.536488/s
     success_rate...................: 100.00% ✓ 55338      ✗ 0    
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

     checks.........................: 100.00% ✓ 152169     ✗ 0    
     data_received..................: 4.4 GB  36 MB/s
     data_sent......................: 61 MB   499 kB/s
     http_req_blocked...............: avg=5.06µs   min=1.03µs  med=2.9µs    max=5.05ms   p(90)=4.29µs   p(95)=4.84µs   p(99.9)=164µs   
     http_req_connecting............: avg=1.82µs   min=0s      med=0s       max=4.75ms   p(90)=0s       p(95)=0s       p(99.9)=14.85µs 
     http_req_duration..............: avg=117.86ms min=20.07ms med=116.27ms max=316.1ms  p(90)=145.73ms p(95)=155.25ms p(99.9)=195.78ms
       { expected_response:true }...: avg=117.86ms min=20.07ms med=116.27ms max=316.1ms  p(90)=145.73ms p(95)=155.25ms p(99.9)=195.78ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 50823
     http_req_receiving.............: avg=85.06µs  min=28.17µs med=78.29µs  max=118.94ms p(90)=108.2µs  p(95)=119.93µs p(99.9)=557.92µs
     http_req_sending...............: avg=22.49µs  min=4.91µs  med=15.25µs  max=49.78ms  p(90)=20.1µs   p(95)=21.93µs  p(99.9)=503.78µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=117.75ms min=19.93ms med=116.17ms max=315.76ms p(90)=145.61ms p(95)=155.13ms p(99.9)=194.76ms
     http_reqs......................: 50823   415.482501/s
     iteration_duration.............: avg=118.31ms min=49.74ms med=116.57ms max=331.31ms p(90)=146.01ms p(95)=155.55ms p(99.9)=200.15ms
     iterations.....................: 50723   414.664992/s
     success_rate...................: 100.00% ✓ 50723      ✗ 0    
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

     checks.........................: 100.00% ✓ 98142      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   323 kB/s
     http_req_blocked...............: avg=5.58µs   min=1.44µs  med=3.82µs   max=2.47ms   p(90)=5.49µs   p(95)=6.17µs   p(99.9)=534.96µs
     http_req_connecting............: avg=1.48µs   min=0s      med=0s       max=2.43ms   p(90)=0s       p(95)=0s       p(99.9)=511.56µs
     http_req_duration..............: avg=182.7ms  min=17.13ms med=170.47ms max=947.32ms p(90)=210.49ms p(95)=230.49ms p(99.9)=697.77ms
       { expected_response:true }...: avg=182.7ms  min=17.13ms med=170.47ms max=947.32ms p(90)=210.49ms p(95)=230.49ms p(99.9)=697.77ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32814
     http_req_receiving.............: avg=102.67µs min=36.65µs med=92.41µs  max=85.92ms  p(90)=125.12µs p(95)=139.73µs p(99.9)=996.98µs
     http_req_sending...............: avg=29.46µs  min=6.42µs  med=18.6µs   max=58.84ms  p(90)=23.61µs  p(95)=25.68µs  p(99.9)=561.75µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=182.56ms min=17.03ms med=170.35ms max=947.24ms p(90)=210.36ms p(95)=230.2ms  p(99.9)=697.68ms
     http_reqs......................: 32814   268.909026/s
     iteration_duration.............: avg=183.49ms min=55.25ms med=170.85ms max=947.53ms p(90)=210.77ms p(95)=231ms    p(99.9)=698.11ms
     iterations.....................: 32714   268.089531/s
     success_rate...................: 100.00% ✓ 32714      ✗ 0    
     vus............................: 22      min=0        max=50 
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

     checks.........................: 100.00% ✓ 97815      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   320 kB/s
     http_req_blocked...............: avg=6.64µs   min=1.32µs  med=3.41µs   max=4.27ms   p(90)=4.85µs   p(95)=5.48µs   p(99.9)=1.27ms  
     http_req_connecting............: avg=2.93µs   min=0s      med=0s       max=4.23ms   p(90)=0s       p(95)=0s       p(99.9)=1.24ms  
     http_req_duration..............: avg=183.34ms min=23.02ms med=182.62ms max=390.21ms p(90)=198.02ms p(95)=204.62ms p(99.9)=279.81ms
       { expected_response:true }...: avg=183.34ms min=23.02ms med=182.62ms max=390.21ms p(90)=198.02ms p(95)=204.62ms p(99.9)=279.81ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32705
     http_req_receiving.............: avg=93.5µs   min=35µs    med=87.49µs  max=48.17ms  p(90)=117.49µs p(95)=129.22µs p(99.9)=533.3µs 
     http_req_sending...............: avg=31.42µs  min=6.2µs   med=17.3µs   max=165.18ms p(90)=21.88µs  p(95)=23.74µs  p(99.9)=573.75µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.21ms min=22.87ms med=182.51ms max=389.92ms p(90)=197.9ms  p(95)=204.51ms p(99.9)=278.59ms
     http_reqs......................: 32705   266.737195/s
     iteration_duration.............: avg=184.12ms min=40.69ms med=182.93ms max=404.04ms p(90)=198.31ms p(95)=204.92ms p(99.9)=280.83ms
     iterations.....................: 32605   265.92161/s
     success_rate...................: 100.00% ✓ 32605      ✗ 0    
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

