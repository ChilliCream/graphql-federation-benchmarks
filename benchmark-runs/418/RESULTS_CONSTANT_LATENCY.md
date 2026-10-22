## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| feddi-gateway | 3c75a7db8876 | 2,488 | 2,583 | 2,473 | 1.5% |  |
| fusion-nightly-net11 | 16.7.0-p.36 | 2,447 | 2,541 | 2,434 | 1.5% |  |
| fusion-nightly-fed | 16.7.0-p.36 | 2,433 | 2,527 | 2,418 | 1.5% |  |
| fusion-nightly | 16.7.0-p.36 | 2,381 | 2,471 | 2,368 | 1.5% |  |
| fusion | 16.6.9 | 1,895 | 1,937 | 1,883 | 0.9% |  |
| hive-router | v0.3.5 | 1,868 | 1,926 | 1,856 | 1.2% |  |
| cosmo | 0.359.0 | 1,359 | 1,406 | 1,353 | 1.3% |  |
| grafbase | 0.53.5 | 1,296 | 1,335 | 1,286 | 1.3% |  |
| caliban | 3.2.0 | 1,264 | 1,317 | 1,254 | 1.9% |  |
| hive-gateway-router-runtime | 2.15.2 | 495 | 511 | 488 | 1.4% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 399 | 417 | 397 | 1.8% |  |
| apollo-router | v2.18.0 | 394 | 416 | 391 | 2.2% |  |
| hive-gateway | 2.15.2 | 258 | 266 | 257 | 1.2% |  |
| apollo-gateway | 2.14.4 | 257 | 262 | 257 | 0.8% |  |


### Details

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 906099      ✗ 0     
     data_received..................: 26 GB   218 MB/s
     data_sent......................: 363 MB  3.0 MB/s
     http_req_blocked...............: avg=2.9µs   min=821ns   med=2.05µs  max=12.66ms  p(90)=3.88µs  p(95)=4.88µs   p(99.9)=32.19µs
     http_req_connecting............: avg=324ns   min=0s      med=0s      max=4.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=19.64ms min=12.51ms med=18.96ms max=281.21ms p(90)=23.35ms p(95)=25.4ms   p(99.9)=45.17ms
       { expected_response:true }...: avg=19.64ms min=12.51ms med=18.96ms max=281.21ms p(90)=23.35ms p(95)=25.4ms   p(99.9)=45.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 302133
     http_req_receiving.............: avg=80.32µs min=24.17µs med=45.72µs max=52.81ms  p(90)=96.32µs p(95)=151.61µs p(99.9)=3.91ms 
     http_req_sending...............: avg=41.92µs min=4.38µs  med=8.58µs  max=154.38ms p(90)=19.71µs p(95)=90.25µs  p(99.9)=3.19ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=19.52ms min=12.42ms med=18.86ms max=280.68ms p(90)=23.21ms p(95)=25.2ms   p(99.9)=44.44ms
     http_reqs......................: 302133  2488.519247/s
     iteration_duration.............: avg=19.85ms min=12.74ms med=19.16ms max=307.22ms p(90)=23.56ms p(95)=25.61ms  p(99.9)=45.43ms
     iterations.....................: 302033  2487.695596/s
     success_rate...................: 100.00% ✓ 302033      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net11 (HotChocolate subgraphs) (16.7.0-p.36)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 891393      ✗ 0     
     data_received..................: 26 GB   215 MB/s
     data_sent......................: 357 MB  2.9 MB/s
     http_req_blocked...............: avg=2.98µs   min=911ns   med=2.24µs  max=8.93ms   p(90)=3.66µs  p(95)=4.38µs  p(99.9)=28.41µs
     http_req_connecting............: avg=307ns    min=0s      med=0s      max=4.11ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=19.97ms  min=11.88ms med=19.13ms max=285.07ms p(90)=24.47ms p(95)=26.89ms p(99.9)=46.66ms
       { expected_response:true }...: avg=19.97ms  min=11.88ms med=19.13ms max=285.07ms p(90)=24.47ms p(95)=26.89ms p(99.9)=46.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 297231
     http_req_receiving.............: avg=429.97µs min=49.98µs med=83.26µs max=264.5ms  p(90)=1.17ms  p(95)=2.2ms   p(99.9)=18.14ms
     http_req_sending...............: avg=42.18µs  min=4.5µs   med=8.3µs   max=187.1ms  p(90)=16.36µs p(95)=87.83µs p(99.9)=3.83ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.5ms   min=11.78ms med=18.7ms  max=284.66ms p(90)=23.8ms  p(95)=26.16ms p(99.9)=44.83ms
     http_reqs......................: 297231  2447.37328/s
     iteration_duration.............: avg=20.18ms  min=12.06ms med=19.33ms max=305.88ms p(90)=24.68ms p(95)=27.11ms p(99.9)=47.11ms
     iterations.....................: 297131  2446.549889/s
     success_rate...................: 100.00% ✓ 297131      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed (HotChocolate subgraphs) (16.7.0-p.36)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 886509      ✗ 0     
     data_received..................: 26 GB   213 MB/s
     data_sent......................: 355 MB  2.9 MB/s
     http_req_blocked...............: avg=2.58µs   min=861ns   med=1.88µs  max=3.53ms   p(90)=3.35µs  p(95)=4.23µs  p(99.9)=27.41µs
     http_req_connecting............: avg=292ns    min=0s      med=0s      max=3.5ms    p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=20.08ms  min=12.36ms med=19.28ms max=269.05ms p(90)=24.63ms p(95)=26.9ms  p(99.9)=46.87ms
       { expected_response:true }...: avg=20.08ms  min=12.36ms med=19.28ms max=269.05ms p(90)=24.63ms p(95)=26.9ms  p(99.9)=46.87ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 295603
     http_req_receiving.............: avg=399.33µs min=49.03µs med=82.08µs max=133.75ms p(90)=1.1ms   p(95)=2.07ms  p(99.9)=15.48ms
     http_req_sending...............: avg=41.75µs  min=4.19µs  med=7.9µs   max=188.75ms p(90)=17.6µs  p(95)=84.92µs p(99.9)=4.05ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.64ms  min=12.15ms med=18.86ms max=268.5ms  p(90)=24.04ms p(95)=26.24ms p(99.9)=44.66ms
     http_reqs......................: 295603  2433.592996/s
     iteration_duration.............: avg=20.29ms  min=12.58ms med=19.48ms max=312.33ms p(90)=24.83ms p(95)=27.12ms p(99.9)=47.25ms
     iterations.....................: 295503  2432.769732/s
     success_rate...................: 100.00% ✓ 295503      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly (HotChocolate subgraphs) (16.7.0-p.36)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 867372      ✗ 0     
     data_received..................: 25 GB   209 MB/s
     data_sent......................: 348 MB  2.9 MB/s
     http_req_blocked...............: avg=3.08µs  min=982ns   med=2.31µs  max=4.84ms   p(90)=3.8µs   p(95)=4.57µs  p(99.9)=32.65µs
     http_req_connecting............: avg=359ns   min=0s      med=0s      max=4.53ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=20.53ms min=12.08ms med=19.74ms max=294.16ms p(90)=25.32ms p(95)=27.57ms p(99.9)=48.76ms
       { expected_response:true }...: avg=20.53ms min=12.08ms med=19.74ms max=294.16ms p(90)=25.32ms p(95)=27.57ms p(99.9)=48.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 289224
     http_req_receiving.............: avg=510.1µs min=50µs    med=88.08µs max=232.93ms p(90)=1.48ms  p(95)=2.45ms  p(99.9)=17.66ms
     http_req_sending...............: avg=40.97µs min=4.45µs  med=8.34µs  max=106.02ms p(90)=17.03µs p(95)=86.21µs p(99.9)=3.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.98ms min=11.95ms med=19.22ms max=144.61ms p(90)=24.59ms p(95)=26.8ms  p(99.9)=47.11ms
     http_reqs......................: 289224  2381.420072/s
     iteration_duration.............: avg=20.74ms min=12.3ms  med=19.93ms max=321.2ms  p(90)=25.52ms p(95)=27.79ms p(99.9)=49.36ms
     iterations.....................: 289124  2380.59669/s
     success_rate...................: 100.00% ✓ 289124      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 693129      ✗ 0     
     data_received..................: 20 GB   166 MB/s
     data_sent......................: 278 MB  2.3 MB/s
     http_req_blocked...............: avg=2.77µs   min=801ns   med=1.92µs   max=4.06ms   p(90)=3.64µs  p(95)=4.37µs  p(99.9)=28.62µs
     http_req_connecting............: avg=407ns    min=0s      med=0s       max=4.02ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.74ms  min=16.96ms med=25.12ms  max=301.05ms p(90)=30.21ms p(95)=32.07ms p(99.9)=49.54ms
       { expected_response:true }...: avg=25.74ms  min=16.96ms med=25.12ms  max=301.05ms p(90)=30.21ms p(95)=32.07ms p(99.9)=49.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 231143
     http_req_receiving.............: avg=443.35µs min=49.1µs  med=101.33µs max=212.02ms p(90)=1.22ms  p(95)=1.82ms  p(99.9)=10.18ms
     http_req_sending...............: avg=32.17µs  min=4.37µs  med=8.11µs   max=134.76ms p(90)=18.07µs p(95)=37.75µs p(99.9)=1.89ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.26ms  min=16.77ms med=24.67ms  max=285.54ms p(90)=29.59ms p(95)=31.39ms p(99.9)=48.17ms
     http_reqs......................: 231143  1895.656461/s
     iteration_duration.............: avg=25.96ms  min=17.35ms med=25.32ms  max=309.1ms  p(90)=30.42ms p(95)=32.28ms p(99.9)=49.93ms
     iterations.....................: 231043  1894.836338/s
     success_rate...................: 100.00% ✓ 231043      ✗ 0     
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

     checks.........................: 100.00% ✓ 683130      ✗ 0     
     data_received..................: 20 GB   163 MB/s
     data_sent......................: 274 MB  2.2 MB/s
     http_req_blocked...............: avg=3.64µs  min=1.03µs  med=2.65µs  max=9.4ms    p(90)=4.29µs  p(95)=5.06µs   p(99.9)=37.38µs
     http_req_connecting............: avg=509ns   min=0s      med=0s      max=7.27ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.11ms min=18.12ms med=25.66ms max=290.41ms p(90)=29.73ms p(95)=31.16ms  p(99.9)=47.74ms
       { expected_response:true }...: avg=26.11ms min=18.12ms med=25.66ms max=290.41ms p(90)=29.73ms p(95)=31.16ms  p(99.9)=47.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 227810
     http_req_receiving.............: avg=79.12µs min=26.16µs med=54.53µs max=152.14ms p(90)=99.08µs p(95)=126.42µs p(99.9)=1.93ms 
     http_req_sending...............: avg=33.57µs min=4.6µs   med=10.5µs  max=171.62ms p(90)=18.82µs p(95)=26.66µs  p(99.9)=1.52ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26ms    min=17.97ms med=25.56ms max=290.15ms p(90)=29.62ms p(95)=31.03ms  p(99.9)=46.85ms
     http_reqs......................: 227810  1868.023985/s
     iteration_duration.............: avg=26.33ms min=18.63ms med=25.87ms max=302.8ms  p(90)=29.95ms p(95)=31.37ms  p(99.9)=47.97ms
     iterations.....................: 227710  1867.203992/s
     success_rate...................: 100.00% ✓ 227710      ✗ 0     
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

     checks.........................: 100.00% ✓ 497259      ✗ 0     
     data_received..................: 15 GB   119 MB/s
     data_sent......................: 199 MB  1.6 MB/s
     http_req_blocked...............: avg=3.24µs  min=942ns   med=2.27µs  max=4.34ms   p(90)=4.01µs   p(95)=4.77µs   p(99.9)=31.65µs
     http_req_connecting............: avg=597ns   min=0s      med=0s      max=4.3ms    p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=35.97ms min=18.84ms med=35.37ms max=327.29ms p(90)=43.03ms  p(95)=45.6ms   p(99.9)=59.06ms
       { expected_response:true }...: avg=35.97ms min=18.84ms med=35.37ms max=327.29ms p(90)=43.03ms  p(95)=45.6ms   p(99.9)=59.06ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 165853
     http_req_receiving.............: avg=75.7µs  min=25.78µs med=59.19µs max=44.75ms  p(90)=101.74µs p(95)=122.54µs p(99.9)=1.15ms 
     http_req_sending...............: avg=25.79µs min=4.62µs  med=10.48µs max=195.18ms p(90)=18.56µs  p(95)=23.09µs  p(99.9)=1.07ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=35.87ms min=18.72ms med=35.27ms max=326.96ms p(90)=42.93ms  p(95)=45.49ms  p(99.9)=58.75ms
     http_reqs......................: 165853  1359.199427/s
     iteration_duration.............: avg=36.19ms min=21.39ms med=35.57ms max=336.15ms p(90)=43.23ms  p(95)=45.8ms   p(99.9)=59.44ms
     iterations.....................: 165753  1358.379907/s
     success_rate...................: 100.00% ✓ 165753      ✗ 0     
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

     checks.........................: 100.00% ✓ 474126      ✗ 0     
     data_received..................: 14 GB   114 MB/s
     data_sent......................: 190 MB  1.6 MB/s
     http_req_blocked...............: avg=4.1µs   min=1.02µs  med=2.99µs  max=3.6ms    p(90)=5.44µs   p(95)=6.53µs   p(99.9)=46.97µs
     http_req_connecting............: avg=569ns   min=0s      med=0s      max=3.56ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=37.69ms min=18.12ms med=37.37ms max=327.04ms p(90)=44.47ms  p(95)=46.52ms  p(99.9)=65.55ms
       { expected_response:true }...: avg=37.69ms min=18.12ms med=37.37ms max=327.04ms p(90)=44.47ms  p(95)=46.52ms  p(99.9)=65.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 158142
     http_req_receiving.............: avg=93.57µs min=27.98µs med=61.64µs max=57.75ms  p(90)=130.38µs p(95)=180.92µs p(99.9)=2.33ms 
     http_req_sending...............: avg=39.04µs min=4.85µs  med=11.41µs max=161.52ms p(90)=24.76µs  p(95)=75.87µs  p(99.9)=2.43ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=37.55ms min=17.97ms med=37.24ms max=326.42ms p(90)=44.34ms  p(95)=46.38ms  p(99.9)=64.56ms
     http_reqs......................: 158142  1296.402447/s
     iteration_duration.............: avg=37.95ms min=21.43ms med=37.62ms max=341.26ms p(90)=44.7ms   p(95)=46.75ms  p(99.9)=66.4ms 
     iterations.....................: 158042  1295.582676/s
     success_rate...................: 100.00% ✓ 158042      ✗ 0     
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

     checks.........................: 100.00% ✓ 462558      ✗ 0     
     data_received..................: 14 GB   111 MB/s
     data_sent......................: 185 MB  1.5 MB/s
     http_req_blocked...............: avg=3.77µs  min=1.15µs  med=3.13µs  max=2.41ms   p(90)=4.89µs   p(95)=5.66µs   p(99.9)=38.05µs
     http_req_connecting............: avg=316ns   min=0s      med=0s      max=2.39ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=38.66ms min=17.92ms med=38.04ms max=314.39ms p(90)=46.3ms   p(95)=49.07ms  p(99.9)=64.46ms
       { expected_response:true }...: avg=38.66ms min=17.92ms med=38.04ms max=314.39ms p(90)=46.3ms   p(95)=49.07ms  p(99.9)=64.46ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 154286
     http_req_receiving.............: avg=80.81µs min=28.41µs med=65.03µs max=172.81ms p(90)=103.48µs p(95)=121.78µs p(99.9)=1.17ms 
     http_req_sending...............: avg=28.65µs min=5.35µs  med=12.56µs max=238.26ms p(90)=19.27µs  p(95)=23.45µs  p(99.9)=1.13ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=38.55ms min=17.78ms med=37.94ms max=314.16ms p(90)=46.19ms  p(95)=48.95ms  p(99.9)=63.92ms
     http_reqs......................: 154286  1264.041977/s
     iteration_duration.............: avg=38.9ms  min=22.87ms med=38.27ms max=322.71ms p(90)=46.52ms  p(95)=49.29ms  p(99.9)=64.89ms
     iterations.....................: 154186  1263.222692/s
     success_rate...................: 100.00% ✓ 154186      ✗ 0     
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

     checks.........................: 100.00% ✓ 181422     ✗ 0    
     data_received..................: 5.3 GB  43 MB/s
     data_sent......................: 73 MB   595 kB/s
     http_req_blocked...............: avg=5.26µs  min=1.29µs  med=3.43µs  max=3.61ms   p(90)=5.09µs   p(95)=5.81µs   p(99.9)=54µs    
     http_req_connecting............: avg=1.51µs  min=0s      med=0s      max=3.59ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=98.84ms min=21.47ms med=94.91ms max=329.63ms p(90)=130.52ms p(95)=142.26ms p(99.9)=240.38ms
       { expected_response:true }...: avg=98.84ms min=21.47ms med=94.91ms max=329.63ms p(90)=130.52ms p(95)=142.26ms p(99.9)=240.38ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 60574
     http_req_receiving.............: avg=93.91µs min=31.59µs med=78.6µs  max=199.41ms p(90)=113.07µs p(95)=126.02µs p(99.9)=597.43µs
     http_req_sending...............: avg=21.63µs min=5.47µs  med=16µs    max=25.71ms  p(90)=22.01µs  p(95)=24.2µs   p(99.9)=615.67µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=98.72ms min=21.29ms med=94.81ms max=328.88ms p(90)=130.43ms p(95)=142.15ms p(99.9)=238.6ms 
     http_reqs......................: 60574   495.150561/s
     iteration_duration.............: avg=99.23ms min=37.6ms  med=95.19ms max=346.65ms p(90)=130.84ms p(95)=142.57ms p(99.9)=242.91ms
     iterations.....................: 60474   494.33313/s
     success_rate...................: 100.00% ✓ 60474      ✗ 0    
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

     checks.........................: 100.00% ✓ 146394     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 59 MB   480 kB/s
     http_req_blocked...............: avg=5.4µs    min=1.12µs  med=3.19µs   max=3.7ms    p(90)=4.74µs   p(95)=5.33µs   p(99.9)=574.8µs 
     http_req_connecting............: avg=2µs      min=0s      med=0s       max=3.66ms   p(90)=0s       p(95)=0s       p(99.9)=475.92µs
     http_req_duration..............: avg=122.5ms  min=21.99ms med=120.81ms max=368.55ms p(90)=151.44ms p(95)=161.14ms p(99.9)=211.24ms
       { expected_response:true }...: avg=122.5ms  min=21.99ms med=120.81ms max=368.55ms p(90)=151.44ms p(95)=161.14ms p(99.9)=211.24ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48898
     http_req_receiving.............: avg=89.45µs  min=28.19µs med=82.57µs  max=96.93ms  p(90)=114.03µs p(95)=126.48µs p(99.9)=540.44µs
     http_req_sending...............: avg=26.85µs  min=5.29µs  med=16.38µs  max=103.36ms p(90)=22.03µs  p(95)=24.11µs  p(99.9)=523.55µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=122.39ms min=21.85ms med=120.7ms  max=368.22ms p(90)=151.33ms p(95)=161.02ms p(99.9)=210.35ms
     http_reqs......................: 48898   399.518823/s
     iteration_duration.............: avg=122.99ms min=36.49ms med=121.11ms max=375.96ms p(90)=151.74ms p(95)=161.44ms p(99.9)=214.29ms
     iterations.....................: 48798   398.701778/s
     success_rate...................: 100.00% ✓ 48798      ✗ 0    
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

     checks.........................: 100.00% ✓ 144375     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   473 kB/s
     http_req_blocked...............: avg=9.26µs   min=1.46µs  med=3.55µs   max=10.68ms  p(90)=5.11µs   p(95)=5.74µs   p(99.9)=673.89µs
     http_req_connecting............: avg=5.37µs   min=0s      med=0s       max=10.65ms  p(90)=0s       p(95)=0s       p(99.9)=567.39µs
     http_req_duration..............: avg=124.2ms  min=21.68ms med=122.11ms max=323.85ms p(90)=155.98ms p(95)=166.3ms  p(99.9)=209.3ms 
       { expected_response:true }...: avg=124.2ms  min=21.68ms med=122.11ms max=323.85ms p(90)=155.98ms p(95)=166.3ms  p(99.9)=209.3ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 48225
     http_req_receiving.............: avg=93.11µs  min=31.96µs med=81.21µs  max=200.65ms p(90)=113.77µs p(95)=126.41µs p(99.9)=468.94µs
     http_req_sending...............: avg=29.65µs  min=5.58µs  med=16.72µs  max=176.79ms p(90)=22.24µs  p(95)=24.22µs  p(99.9)=678.92µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=124.08ms min=21.47ms med=121.99ms max=323.63ms p(90)=155.83ms p(95)=166.18ms p(99.9)=208.46ms
     http_reqs......................: 48225   394.125567/s
     iteration_duration.............: avg=124.7ms  min=42.31ms med=122.43ms max=349.15ms p(90)=156.28ms p(95)=166.69ms p(99.9)=214.55ms
     iterations.....................: 48125   393.308303/s
     success_rate...................: 100.00% ✓ 48125      ✗ 0    
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

     checks.........................: 100.00% ✓ 94344      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   310 kB/s
     http_req_blocked...............: avg=7.31µs   min=1.42µs  med=3.76µs   max=4.07ms   p(90)=5.45µs   p(95)=6.16µs   p(99.9)=1.72ms  
     http_req_connecting............: avg=3.2µs    min=0s      med=0s       max=4.03ms   p(90)=0s       p(95)=0s       p(99.9)=1.7ms   
     http_req_duration..............: avg=190.06ms min=17.89ms med=176.48ms max=765.88ms p(90)=221.05ms p(95)=243.06ms p(99.9)=694.93ms
       { expected_response:true }...: avg=190.06ms min=17.89ms med=176.48ms max=765.88ms p(90)=221.05ms p(95)=243.06ms p(99.9)=694.93ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31548
     http_req_receiving.............: avg=99.68µs  min=36.87µs med=93.82µs  max=34.1ms   p(90)=126.22µs p(95)=140.31µs p(99.9)=644.38µs
     http_req_sending...............: avg=29.6µs   min=5.99µs  med=19.18µs  max=82.89ms  p(90)=24.29µs  p(95)=26.39µs  p(99.9)=485.78µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=189.93ms min=17.79ms med=176.36ms max=765.74ms p(90)=220.92ms p(95)=242.96ms p(99.9)=694.84ms
     http_reqs......................: 31548   258.354847/s
     iteration_duration.............: avg=190.91ms min=42.05ms med=176.95ms max=766.18ms p(90)=221.43ms p(95)=243.92ms p(99.9)=695.29ms
     iterations.....................: 31448   257.535921/s
     success_rate...................: 100.00% ✓ 31448      ✗ 0    
     vus............................: 46      min=0        max=50 
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

     checks.........................: 100.00% ✓ 94284      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   309 kB/s
     http_req_blocked...............: avg=5.6µs    min=1.04µs  med=3.24µs   max=3.44ms   p(90)=4.61µs   p(95)=5.15µs   p(99.9)=853.04µs
     http_req_connecting............: avg=2.09µs   min=0s      med=0s       max=3.42ms   p(90)=0s       p(95)=0s       p(99.9)=814.59µs
     http_req_duration..............: avg=190.15ms min=23.81ms med=190.88ms max=360.87ms p(90)=201.6ms  p(95)=206.65ms p(99.9)=278.48ms
       { expected_response:true }...: avg=190.15ms min=23.81ms med=190.88ms max=360.87ms p(90)=201.6ms  p(95)=206.65ms p(99.9)=278.48ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31528
     http_req_receiving.............: avg=91.65µs  min=30.32µs med=87.99µs  max=25.93ms  p(90)=118.2µs  p(95)=129.96µs p(99.9)=517.16µs
     http_req_sending...............: avg=30.91µs  min=5.33µs  med=16.99µs  max=137.09ms p(90)=21.64µs  p(95)=23.45µs  p(99.9)=431.68µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=190.03ms min=23.7ms  med=190.76ms max=352.23ms p(90)=201.49ms p(95)=206.56ms p(99.9)=278.39ms
     http_reqs......................: 31528   257.037192/s
     iteration_duration.............: avg=190.98ms min=56.97ms med=191.26ms max=385.33ms p(90)=201.9ms  p(95)=206.96ms p(99.9)=280.41ms
     iterations.....................: 31428   256.221926/s
     success_rate...................: 100.00% ✓ 31428      ✗ 0    
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

