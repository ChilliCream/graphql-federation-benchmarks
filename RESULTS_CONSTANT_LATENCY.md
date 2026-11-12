## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-aot-11 | 16.8.0-p.10 | 3,461 | 3,489 | 3,456 | 0.4% | 141 MB | 41.6 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.10 | 3,448 | 3,476 | 3,435 | 0.5% | 384 MB | 113.9 KB |  |
| fusion-net-11 | 16.7.5 | 3,433 | 3,443 | 3,412 | 0.4% | 393 MB | 117.2 KB |  |
| fusion-aot-11 | 16.7.5 | 3,352 | 3,363 | 3,348 | 0.2% | 152 MB | 46.6 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,227 | 3,260 | 3,217 | 0.6% | 2,309 MB | 732.6 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.10 | 2,812 | 2,830 | 2,798 | 0.6% | 390 MB | 141.9 KB |  |
| fusion-fed-net-11 | 16.7.5 | 2,788 | 2,794 | 2,772 | 0.3% | 383 MB | 140.6 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 2,763 | 2,773 | 2,728 | 0.6% | 145 MB | 53.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.10 | 2,758 | 2,775 | 2,750 | 0.4% | 133 MB | 49.4 KB |  |
| hive-router | v0.3.10 | 2,042 | 2,061 | 2,025 | 0.8% | 93 MB | 46.8 KB |  |
| grafbase | 0.53.5 | 1,427 | 1,439 | 1,423 | 0.4% | 100 MB | 71.8 KB |  |
| cosmo | 0.365.2 | 1,425 | 1,427 | 1,422 | 0.1% | 151 MB | 108.3 KB |  |
| caliban | 3.2.0 | 1,339 | 1,340 | 1,338 | 0.1% | 5,030 MB | 3,847.1 KB |  |
| apollo-router | v2.19.0 | 529 | 529 | 523 | 0.5% | 181 MB | 351.3 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 524 | 526 | 523 | 0.2% | 2,762 MB | 5,397.2 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 401 | 405 | 396 | 1.1% | 203 MB | 519.5 KB |  |
| apollo-gateway | 2.14.4 | 266 | 266 | 265 | 0.2% | 2,158 MB | 8,307.1 KB |  |
| hive-gateway | 2.15.6 | 255 | 256 | 254 | 0.3% | 3,592 MB | 14,426.0 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1255764     ✗ 0     
     data_received..................: 37 GB   303 MB/s
     data_sent......................: 503 MB  4.2 MB/s
     http_req_blocked...............: avg=2.46µs  min=822ns   med=1.88µs  max=4.56ms   p(90)=3.11µs  p(95)=3.9µs    p(99.9)=25.68µs
     http_req_connecting............: avg=215ns   min=0s      med=0s      max=3.95ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.13ms min=8.07ms  med=13.72ms max=274.59ms p(90)=17.27ms p(95)=18.53ms  p(99.9)=25.92ms
       { expected_response:true }...: avg=14.13ms min=8.07ms  med=13.72ms max=274.59ms p(90)=17.27ms p(95)=18.53ms  p(99.9)=25.92ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 418688
     http_req_receiving.............: avg=68.4µs  min=24.55µs med=43.95µs max=158.74ms p(90)=89.73µs p(95)=168.67µs p(99.9)=1.7ms  
     http_req_sending...............: avg=31.46µs min=4.41µs  med=8.08µs  max=136.12ms p(90)=16.24µs p(95)=93.4µs   p(99.9)=1.72ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.03ms min=8.01ms  med=13.62ms max=274.02ms p(90)=17.16ms p(95)=18.41ms  p(99.9)=25.71ms
     http_reqs......................: 418688  3461.270381/s
     iteration_duration.............: avg=14.32ms min=8.21ms  med=13.91ms max=286.18ms p(90)=17.46ms p(95)=18.72ms  p(99.9)=26.14ms
     iterations.....................: 418588  3460.443687/s
     success_rate...................: 100.00% ✓ 418588      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1251135     ✗ 0     
     data_received..................: 37 GB   302 MB/s
     data_sent......................: 501 MB  4.1 MB/s
     http_req_blocked...............: avg=2.4µs   min=832ns   med=1.87µs  max=3.49ms   p(90)=3.05µs  p(95)=3.74µs   p(99.9)=22.81µs
     http_req_connecting............: avg=204ns   min=0s      med=0s      max=3.45ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.18ms min=8.28ms  med=13.77ms max=283.3ms  p(90)=17.48ms p(95)=18.77ms  p(99.9)=25.95ms
       { expected_response:true }...: avg=14.18ms min=8.28ms  med=13.77ms max=283.3ms  p(90)=17.48ms p(95)=18.77ms  p(99.9)=25.95ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 417145
     http_req_receiving.............: avg=68.09µs min=24.04µs med=43.52µs max=192.71ms p(90)=88.74µs p(95)=167.04µs p(99.9)=1.8ms  
     http_req_sending...............: avg=30.56µs min=4.25µs  med=7.95µs  max=116.85ms p(90)=15.47µs p(95)=91.8µs   p(99.9)=1.73ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.08ms min=8.21ms  med=13.67ms max=282.15ms p(90)=17.37ms p(95)=18.65ms  p(99.9)=25.71ms
     http_reqs......................: 417145  3448.507443/s
     iteration_duration.............: avg=14.37ms min=8.48ms  med=13.96ms max=294.2ms  p(90)=17.67ms p(95)=18.96ms  p(99.9)=26.16ms
     iterations.....................: 417045  3447.68075/s
     success_rate...................: 100.00% ✓ 417045      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1245462     ✗ 0     
     data_received..................: 36 GB   300 MB/s
     data_sent......................: 499 MB  4.1 MB/s
     http_req_blocked...............: avg=2.94µs  min=922ns   med=2.28µs  max=6.44ms   p(90)=3.66µs  p(95)=4.47µs   p(99.9)=32.72µs
     http_req_connecting............: avg=248ns   min=0s      med=0s      max=4.34ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.23ms min=8.05ms  med=13.77ms max=288.11ms p(90)=17.76ms p(95)=19.16ms  p(99.9)=27.28ms
       { expected_response:true }...: avg=14.23ms min=8.05ms  med=13.77ms max=288.11ms p(90)=17.76ms p(95)=19.16ms  p(99.9)=27.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 415254
     http_req_receiving.............: avg=74.09µs min=24.73µs med=45.11µs max=107.97ms p(90)=97.76µs p(95)=186.15µs p(99.9)=2.26ms 
     http_req_sending...............: avg=34.63µs min=4.44µs  med=8.72µs  max=125.22ms p(90)=18.3µs  p(95)=101.12µs p(99.9)=2.28ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.12ms min=7.98ms  med=13.67ms max=287.76ms p(90)=17.64ms p(95)=19.03ms  p(99.9)=27.06ms
     http_reqs......................: 415254  3433.208746/s
     iteration_duration.............: avg=14.44ms min=8.19ms  med=13.97ms max=306.25ms p(90)=17.96ms p(95)=19.36ms  p(99.9)=27.53ms
     iterations.....................: 415154  3432.381972/s
     success_rate...................: 100.00% ✓ 415154      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1216188     ✗ 0     
     data_received..................: 36 GB   293 MB/s
     data_sent......................: 487 MB  4.0 MB/s
     http_req_blocked...............: avg=2.87µs  min=881ns   med=2.26µs  max=7.23ms   p(90)=3.67µs  p(95)=4.42µs   p(99.9)=31.06µs
     http_req_connecting............: avg=212ns   min=0s      med=0s      max=3.45ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.58ms min=8.34ms  med=14.13ms max=283.99ms p(90)=18.11ms p(95)=19.53ms  p(99.9)=28.18ms
       { expected_response:true }...: avg=14.58ms min=8.34ms  med=14.13ms max=283.99ms p(90)=18.11ms p(95)=19.53ms  p(99.9)=28.18ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 405496
     http_req_receiving.............: avg=74µs    min=25.62µs med=46.31µs max=88.89ms  p(90)=96.72µs p(95)=187.55µs p(99.9)=2.08ms 
     http_req_sending...............: avg=34.08µs min=4.29µs  med=8.68µs  max=191.99ms p(90)=17.67µs p(95)=100.2µs  p(99.9)=1.94ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.48ms min=8.28ms  med=14.03ms max=283.42ms p(90)=17.99ms p(95)=19.4ms   p(99.9)=27.88ms
     http_reqs......................: 405496  3352.133698/s
     iteration_duration.............: avg=14.79ms min=8.51ms  med=14.33ms max=293.66ms p(90)=18.31ms p(95)=19.73ms  p(99.9)=28.41ms
     iterations.....................: 405396  3351.307023/s
     success_rate...................: 100.00% ✓ 405396      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-10-25-0247)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1170912     ✗ 0     
     data_received..................: 34 GB   282 MB/s
     data_sent......................: 469 MB  3.9 MB/s
     http_req_blocked...............: avg=2.54µs  min=812ns   med=1.94µs  max=3.97ms   p(90)=3.27µs  p(95)=4.06µs  p(99.9)=25.34µs
     http_req_connecting............: avg=235ns   min=0s      med=0s      max=3.9ms    p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=15.16ms min=8.63ms  med=14.83ms max=284.54ms p(90)=18.3ms  p(95)=19.5ms  p(99.9)=27.18ms
       { expected_response:true }...: avg=15.16ms min=8.63ms  med=14.83ms max=284.54ms p(90)=18.3ms  p(95)=19.5ms  p(99.9)=27.18ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 390404
     http_req_receiving.............: avg=68.69µs min=24.22µs med=44.51µs max=101.24ms p(90)=91.19µs p(95)=163µs   p(99.9)=1.65ms 
     http_req_sending...............: avg=30.92µs min=4.42µs  med=8.31µs  max=152.33ms p(90)=16.65µs p(95)=92.18µs p(99.9)=1.72ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=15.06ms min=8.56ms  med=14.74ms max=264.08ms p(90)=18.2ms  p(95)=19.38ms p(99.9)=26.88ms
     http_reqs......................: 390404  3227.627013/s
     iteration_duration.............: avg=15.36ms min=8.8ms   med=15.03ms max=305.17ms p(90)=18.49ms p(95)=19.69ms p(99.9)=27.42ms
     iterations.....................: 390304  3226.800273/s
     success_rate...................: 100.00% ✓ 390304      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1023990     ✗ 0     
     data_received..................: 30 GB   246 MB/s
     data_sent......................: 410 MB  3.4 MB/s
     http_req_blocked...............: avg=2.93µs  min=911ns   med=2.3µs   max=4.29ms   p(90)=3.64µs  p(95)=4.32µs   p(99.9)=28.85µs
     http_req_connecting............: avg=299ns   min=0s      med=0s      max=4.24ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.36ms min=11.57ms med=16.92ms max=298.42ms p(90)=20.34ms p(95)=21.6ms   p(99.9)=28.75ms
       { expected_response:true }...: avg=17.36ms min=11.57ms med=16.92ms max=298.42ms p(90)=20.34ms p(95)=21.6ms   p(99.9)=28.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 341430
     http_req_receiving.............: avg=69.47µs min=24.15µs med=46.5µs  max=243.28ms p(90)=93.33µs p(95)=153.08µs p(99.9)=1.41ms 
     http_req_sending...............: avg=29.48µs min=4.44µs  med=8.86µs  max=38.84ms  p(90)=17µs    p(95)=90.65µs  p(99.9)=1.52ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.26ms min=11.52ms med=16.83ms max=296.28ms p(90)=20.23ms p(95)=21.48ms  p(99.9)=28.55ms
     http_reqs......................: 341430  2812.578761/s
     iteration_duration.............: avg=17.56ms min=11.75ms med=17.13ms max=313.46ms p(90)=20.54ms p(95)=21.8ms   p(99.9)=29.01ms
     iterations.....................: 341330  2811.754997/s
     success_rate...................: 100.00% ✓ 341330      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1015293     ✗ 0     
     data_received..................: 30 GB   244 MB/s
     data_sent......................: 407 MB  3.4 MB/s
     http_req_blocked...............: avg=3.42µs  min=902ns   med=2.27µs  max=9.92ms   p(90)=3.72µs  p(95)=4.52µs   p(99.9)=32.98µs
     http_req_connecting............: avg=717ns   min=0s      med=0s      max=9.15ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.51ms min=11.7ms  med=17.06ms max=286.75ms p(90)=20.59ms p(95)=21.87ms  p(99.9)=29.04ms
       { expected_response:true }...: avg=17.51ms min=11.7ms  med=17.06ms max=286.75ms p(90)=20.59ms p(95)=21.87ms  p(99.9)=29.04ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 338531
     http_req_receiving.............: avg=70.75µs min=25.04µs med=46.7µs  max=142.48ms p(90)=95.8µs  p(95)=160.73µs p(99.9)=1.47ms 
     http_req_sending...............: avg=30.73µs min=4.41µs  med=8.5µs   max=151.49ms p(90)=17.03µs p(95)=90.94µs  p(99.9)=1.59ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.41ms min=11.64ms med=16.96ms max=280.49ms p(90)=20.48ms p(95)=21.75ms  p(99.9)=28.82ms
     http_reqs......................: 338531  2788.490609/s
     iteration_duration.............: avg=17.72ms min=11.83ms med=17.26ms max=306.78ms p(90)=20.79ms p(95)=22.07ms  p(99.9)=29.26ms
     iterations.....................: 338431  2787.666906/s
     success_rate...................: 100.00% ✓ 338431      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1006347     ✗ 0     
     data_received..................: 29 GB   242 MB/s
     data_sent......................: 403 MB  3.3 MB/s
     http_req_blocked...............: avg=2.91µs  min=872ns   med=2.27µs  max=4.41ms   p(90)=3.7µs   p(95)=4.48µs   p(99.9)=29.56µs
     http_req_connecting............: avg=287ns   min=0s      med=0s      max=4.37ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.67ms min=11.77ms med=17.23ms max=291.74ms p(90)=20.66ms p(95)=21.91ms  p(99.9)=28.89ms
       { expected_response:true }...: avg=17.67ms min=11.77ms med=17.23ms max=291.74ms p(90)=20.66ms p(95)=21.91ms  p(99.9)=28.89ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 335549
     http_req_receiving.............: avg=85.46µs min=24.21µs med=47.43µs max=254.32ms p(90)=93.59µs p(95)=150.09µs p(99.9)=1.45ms 
     http_req_sending...............: avg=28.75µs min=4.34µs  med=8.59µs  max=32.41ms  p(90)=17.53µs p(95)=87.28µs  p(99.9)=1.49ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.55ms min=11.71ms med=17.14ms max=227.09ms p(90)=20.54ms p(95)=21.8ms   p(99.9)=28.64ms
     http_reqs......................: 335549  2763.987294/s
     iteration_duration.............: avg=17.87ms min=11.95ms med=17.43ms max=301.28ms p(90)=20.86ms p(95)=22.11ms  p(99.9)=29.11ms
     iterations.....................: 335449  2763.163573/s
     success_rate...................: 100.00% ✓ 335449      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1004256     ✗ 0     
     data_received..................: 29 GB   241 MB/s
     data_sent......................: 402 MB  3.3 MB/s
     http_req_blocked...............: avg=2.54µs  min=831ns   med=1.92µs  max=3.62ms   p(90)=3.33µs  p(95)=4.22µs   p(99.9)=22.41µs
     http_req_connecting............: avg=263ns   min=0s      med=0s      max=3.58ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.71ms min=12ms    med=17.29ms max=283.04ms p(90)=20.66ms p(95)=21.89ms  p(99.9)=29.21ms
       { expected_response:true }...: avg=17.71ms min=12ms    med=17.29ms max=283.04ms p(90)=20.66ms p(95)=21.89ms  p(99.9)=29.21ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 334852
     http_req_receiving.............: avg=64.96µs min=24.02µs med=43.6µs  max=88.07ms  p(90)=89.76µs p(95)=142.04µs p(99.9)=1.3ms  
     http_req_sending...............: avg=28.54µs min=4.38µs  med=8.08µs  max=158.94ms p(90)=16.83µs p(95)=82.74µs  p(99.9)=1.34ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.61ms min=11.95ms med=17.2ms  max=282.38ms p(90)=20.56ms p(95)=21.77ms  p(99.9)=28.93ms
     http_reqs......................: 334852  2758.15851/s
     iteration_duration.............: avg=17.91ms min=12.17ms med=17.49ms max=301.15ms p(90)=20.86ms p(95)=22.09ms  p(99.9)=29.43ms
     iterations.....................: 334752  2757.334815/s
     success_rate...................: 100.00% ✓ 334752      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 746571      ✗ 0     
     data_received..................: 22 GB   179 MB/s
     data_sent......................: 299 MB  2.5 MB/s
     http_req_blocked...............: avg=3.13µs  min=861ns   med=2.09µs  max=9.56ms   p(90)=3.69µs  p(95)=4.41µs   p(99.9)=29.44µs 
     http_req_connecting............: avg=630ns   min=0s      med=0s      max=9.53ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.89ms min=17.04ms med=23.54ms max=290ms    p(90)=26.96ms p(95)=28.07ms  p(99.9)=33.65ms 
       { expected_response:true }...: avg=23.89ms min=17.04ms med=23.54ms max=290ms    p(90)=26.96ms p(95)=28.07ms  p(99.9)=33.65ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 248957
     http_req_receiving.............: avg=63.67µs min=24.94µs med=47.92µs max=54ms     p(90)=90.43µs p(95)=115.03µs p(99.9)=881.7µs 
     http_req_sending...............: avg=25.69µs min=4.46µs  med=9.25µs  max=181.36ms p(90)=17.72µs p(95)=24.99µs  p(99.9)=963.32µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.8ms  min=16.93ms med=23.45ms max=289.33ms p(90)=26.87ms p(95)=27.97ms  p(99.9)=33.47ms 
     http_reqs......................: 248957  2042.938593/s
     iteration_duration.............: avg=24.1ms  min=17.24ms med=23.74ms max=298.31ms p(90)=27.17ms p(95)=28.27ms  p(99.9)=33.86ms 
     iterations.....................: 248857  2042.117994/s
     success_rate...................: 100.00% ✓ 248857      ✗ 0     
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

     checks.........................: 100.00% ✓ 521982      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 209 MB  1.7 MB/s
     http_req_blocked...............: avg=3.55µs  min=1µs     med=2.87µs  max=1.81ms   p(90)=5.01µs   p(95)=5.95µs   p(99.9)=44.63µs
     http_req_connecting............: avg=220ns   min=0s      med=0s      max=1.79ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.21ms min=17.54ms med=33.86ms max=314.1ms  p(90)=40.01ms  p(95)=41.76ms  p(99.9)=50.47ms
       { expected_response:true }...: avg=34.21ms min=17.54ms med=33.86ms max=314.1ms  p(90)=40.01ms  p(95)=41.76ms  p(99.9)=50.47ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 174094
     http_req_receiving.............: avg=85.08µs min=26.34µs med=60.44µs max=103.76ms p(90)=122.07µs p(95)=168.42µs p(99.9)=1.52ms 
     http_req_sending...............: avg=32.01µs min=4.26µs  med=11.05µs max=98.53ms  p(90)=23.39µs  p(95)=69.63µs  p(99.9)=1.48ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.09ms min=17.42ms med=33.75ms max=308.79ms p(90)=39.89ms  p(95)=41.64ms  p(99.9)=50.25ms
     http_reqs......................: 174094  1427.863034/s
     iteration_duration.............: avg=34.47ms min=21.21ms med=34.11ms max=322.63ms p(90)=40.24ms  p(95)=41.98ms  p(99.9)=50.82ms
     iterations.....................: 173994  1427.042866/s
     success_rate...................: 100.00% ✓ 173994      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.365.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 521265      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 209 MB  1.7 MB/s
     http_req_blocked...............: avg=3.59µs  min=1.12µs  med=2.71µs  max=3.85ms   p(90)=4.32µs  p(95)=5.05µs   p(99.9)=33.74µs 
     http_req_connecting............: avg=557ns   min=0s      med=0s      max=3.81ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.3ms  min=18.93ms med=33.74ms max=305.73ms p(90)=40.91ms p(95)=43.21ms  p(99.9)=55.55ms 
       { expected_response:true }...: avg=34.3ms  min=18.93ms med=33.74ms max=305.73ms p(90)=40.91ms p(95)=43.21ms  p(99.9)=55.55ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 173855
     http_req_receiving.............: avg=74.52µs min=27.01µs med=61.29µs max=146.98ms p(90)=99.86µs p(95)=117.48µs p(99.9)=744.08µs
     http_req_sending...............: avg=23.24µs min=4.77µs  med=11.18µs max=146.59ms p(90)=17.88µs p(95)=22.04µs  p(99.9)=786.97µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.2ms  min=18.74ms med=33.64ms max=305.43ms p(90)=40.81ms p(95)=43.12ms  p(99.9)=55.42ms 
     http_reqs......................: 173855  1425.451214/s
     iteration_duration.............: avg=34.52ms min=20.4ms  med=33.94ms max=325.17ms p(90)=41.11ms p(95)=43.41ms  p(99.9)=56.01ms 
     iterations.....................: 173755  1424.631306/s
     success_rate...................: 100.00% ✓ 173755      ✗ 0     
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

     checks.........................: 100.00% ✓ 489816      ✗ 0     
     data_received..................: 14 GB   117 MB/s
     data_sent......................: 196 MB  1.6 MB/s
     http_req_blocked...............: avg=3.3µs   min=892ns   med=2.58µs  max=3.08ms   p(90)=4.05µs  p(95)=4.69µs   p(99.9)=30.56µs 
     http_req_connecting............: avg=446ns   min=0s      med=0s      max=3.04ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=36.53ms min=18.21ms med=35.95ms max=320.18ms p(90)=43.55ms p(95)=46.07ms  p(99.9)=62.55ms 
       { expected_response:true }...: avg=36.53ms min=18.21ms med=35.95ms max=320.18ms p(90)=43.55ms p(95)=46.07ms  p(99.9)=62.55ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 163372
     http_req_receiving.............: avg=68.01µs min=27.6µs  med=57.84µs max=25.62ms  p(90)=90.17µs p(95)=104.12µs p(99.9)=763.31µs
     http_req_sending...............: avg=19.47µs min=4.96µs  med=10.82µs max=72.56ms  p(90)=15.84µs p(95)=18.96µs  p(99.9)=714.76µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=36.44ms min=18.14ms med=35.87ms max=319.41ms p(90)=43.46ms p(95)=45.99ms  p(99.9)=62.46ms 
     http_reqs......................: 163372  1339.106663/s
     iteration_duration.............: avg=36.74ms min=21.38ms med=36.14ms max=328.35ms p(90)=43.75ms p(95)=46.27ms  p(99.9)=63.01ms 
     iterations.....................: 163272  1338.286996/s
     success_rate...................: 100.00% ✓ 163272      ✗ 0     
     vus............................: 37      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.19.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 193797     ✗ 0    
     data_received..................: 5.7 GB  46 MB/s
     data_sent......................: 78 MB   636 kB/s
     http_req_blocked...............: avg=4.41µs  min=1.29µs  med=3.37µs  max=2.31ms   p(90)=4.91µs   p(95)=5.5µs    p(99.9)=49.6µs  
     http_req_connecting............: avg=802ns   min=0s      med=0s      max=2.28ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.52ms min=18.77ms med=90.79ms max=320.88ms p(90)=116.58ms p(95)=124.95ms p(99.9)=159.43ms
       { expected_response:true }...: avg=92.52ms min=18.77ms med=90.79ms max=320.88ms p(90)=116.58ms p(95)=124.95ms p(99.9)=159.43ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64699
     http_req_receiving.............: avg=81.47µs min=31.02µs med=76.16µs max=30.67ms  p(90)=108.85µs p(95)=121.1µs  p(99.9)=531µs   
     http_req_sending...............: avg=25.26µs min=5.52µs  med=16.06µs max=133.86ms p(90)=21.68µs  p(95)=23.82µs  p(99.9)=517.75µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.41ms min=18.68ms med=90.69ms max=320.5ms  p(90)=116.47ms p(95)=124.85ms p(99.9)=159.28ms
     http_reqs......................: 64699   529.369551/s
     iteration_duration.............: avg=92.89ms min=34.54ms med=91.07ms max=335.94ms p(90)=116.84ms p(95)=125.23ms p(99.9)=160.28ms
     iterations.....................: 64599   528.551347/s
     success_rate...................: 100.00% ✓ 64599      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 192099     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   630 kB/s
     http_req_blocked...............: avg=4.71µs  min=1µs     med=2.5µs   max=6.11ms   p(90)=3.98µs   p(95)=4.56µs   p(99.9)=48.01µs 
     http_req_connecting............: avg=1.89µs  min=0s      med=0s      max=5.92ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.39ms min=20.47ms med=89.73ms max=369.75ms p(90)=120.59ms p(95)=131.08ms p(99.9)=231.05ms
       { expected_response:true }...: avg=93.39ms min=20.47ms med=89.73ms max=369.75ms p(90)=120.59ms p(95)=131.08ms p(99.9)=231.05ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64133
     http_req_receiving.............: avg=74.29µs min=27.45µs med=66.54µs max=48.58ms  p(90)=100.22µs p(95)=112.23µs p(99.9)=538.47µs
     http_req_sending...............: avg=18.76µs min=4.85µs  med=12.19µs max=131.7ms  p(90)=18.1µs   p(95)=20.01µs  p(99.9)=578.87µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.29ms min=20.33ms med=89.64ms max=369.67ms p(90)=120.49ms p(95)=130.97ms p(99.9)=230.59ms
     http_reqs......................: 64133   524.622811/s
     iteration_duration.............: avg=93.72ms min=33.43ms med=89.96ms max=388.56ms p(90)=120.81ms p(95)=131.32ms p(99.9)=232.87ms
     iterations.....................: 64033   523.804788/s
     success_rate...................: 100.00% ✓ 64033      ✗ 0    
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

     checks.........................: 100.00% ✓ 147018     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 59 MB   482 kB/s
     http_req_blocked...............: avg=4.9µs    min=1.1µs   med=2.89µs   max=3.9ms    p(90)=4.3µs    p(95)=4.84µs   p(99.9)=305.15µs
     http_req_connecting............: avg=1.82µs   min=0s      med=0s       max=3.86ms   p(90)=0s       p(95)=0s       p(99.9)=277.48µs
     http_req_duration..............: avg=122ms    min=20.99ms med=120.2ms  max=357.99ms p(90)=150.99ms p(95)=160.89ms p(99.9)=208.45ms
       { expected_response:true }...: avg=122ms    min=20.99ms med=120.2ms  max=357.99ms p(90)=150.99ms p(95)=160.89ms p(99.9)=208.45ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49106
     http_req_receiving.............: avg=86.56µs  min=28.71µs med=73.08µs  max=136.47ms p(90)=105.19µs p(95)=116.64µs p(99.9)=485.87µs
     http_req_sending...............: avg=25.86µs  min=5.19µs  med=14.47µs  max=214.5ms  p(90)=19.71µs  p(95)=21.51µs  p(99.9)=483.37µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=121.89ms min=20.86ms med=120.09ms max=357.47ms p(90)=150.89ms p(95)=160.77ms p(99.9)=208.03ms
     http_reqs......................: 49106   401.457111/s
     iteration_duration.............: avg=122.46ms min=41.05ms med=120.47ms max=366.36ms p(90)=151.26ms p(95)=161.14ms p(99.9)=209.13ms
     iterations.....................: 49006   400.639579/s
     success_rate...................: 100.00% ✓ 49006      ✗ 0    
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

     checks.........................: 100.00% ✓ 97566      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   320 kB/s
     http_req_blocked...............: avg=6.78µs   min=1.4µs   med=3.52µs   max=4.24ms   p(90)=4.9µs    p(95)=5.49µs   p(99.9)=1.34ms  
     http_req_connecting............: avg=3.02µs   min=0s      med=0s       max=4.19ms   p(90)=0s       p(95)=0s       p(99.9)=1.31ms  
     http_req_duration..............: avg=183.81ms min=23.06ms med=187.76ms max=375.12ms p(90)=199.54ms p(95)=205ms    p(99.9)=270.44ms
       { expected_response:true }...: avg=183.81ms min=23.06ms med=187.76ms max=375.12ms p(90)=199.54ms p(95)=205ms    p(99.9)=270.44ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32622
     http_req_receiving.............: avg=91.06µs  min=32.8µs  med=85.92µs  max=34.79ms  p(90)=115.29µs p(95)=125.59µs p(99.9)=480.2µs 
     http_req_sending...............: avg=36.46µs  min=5.87µs  med=17.04µs  max=186.02ms p(90)=21.63µs  p(95)=23.42µs  p(99.9)=534.64µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.68ms min=22.97ms med=187.66ms max=374.97ms p(90)=199.43ms p(95)=204.87ms p(99.9)=269.92ms
     http_reqs......................: 32622   266.101744/s
     iteration_duration.............: avg=184.59ms min=42.86ms med=188.06ms max=386.09ms p(90)=199.82ms p(95)=205.32ms p(99.9)=273.36ms
     iterations.....................: 32522   265.286031/s
     success_rate...................: 100.00% ✓ 32522      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 93633      ✗ 0    
     data_received..................: 2.7 GB  22 MB/s
     data_sent......................: 38 MB   307 kB/s
     http_req_blocked...............: avg=5.37µs   min=1.15µs  med=3µs      max=3.3ms    p(90)=4.28µs   p(95)=4.84µs   p(99.9)=1.18ms  
     http_req_connecting............: avg=2.18µs   min=0s      med=0s       max=3.23ms   p(90)=0s       p(95)=0s       p(99.9)=1.12ms  
     http_req_duration..............: avg=191.66ms min=17.69ms med=177.58ms max=772.35ms p(90)=226.54ms p(95)=249.07ms p(99.9)=707.43ms
       { expected_response:true }...: avg=191.66ms min=17.69ms med=177.58ms max=772.35ms p(90)=226.54ms p(95)=249.07ms p(99.9)=707.43ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31311
     http_req_receiving.............: avg=92.62µs  min=31.44µs med=83.08µs  max=69.17ms  p(90)=113.21µs p(95)=124.4µs  p(99.9)=549.85µs
     http_req_sending...............: avg=23.68µs  min=4.57µs  med=16.15µs  max=42.42ms  p(90)=20.31µs  p(95)=21.95µs  p(99.9)=604.82µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=191.55ms min=17.61ms med=177.47ms max=772.25ms p(90)=226.42ms p(95)=248.91ms p(99.9)=707.35ms
     http_reqs......................: 31311   255.953638/s
     iteration_duration.............: avg=192.47ms min=83.46ms med=177.93ms max=772.62ms p(90)=226.88ms p(95)=249.55ms p(99.9)=707.69ms
     iterations.....................: 31211   255.136182/s
     success_rate...................: 100.00% ✓ 31211      ✗ 0    
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

