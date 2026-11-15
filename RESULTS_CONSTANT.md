## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-fed-net-11 | 16.8.0-p.12 | 5,399 | 5,413 | 5,314 | 0.7% | 397 MB | 75.3 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.12 | 5,290 | 5,326 | 5,283 | 0.3% | 368 MB | 71.2 KB |  |
| fusion-net-11 | 16.7.5 | 5,105 | 5,147 | 5,061 | 0.7% | 386 MB | 77.3 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.12 | 5,086 | 5,099 | 5,053 | 0.4% | 127 MB | 25.6 KB |  |
| fusion-fed-net-11 | 16.7.5 | 4,921 | 4,931 | 4,913 | 0.1% | 404 MB | 84.0 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.12 | 4,902 | 4,909 | 4,891 | 0.1% | 130 MB | 27.1 KB |  |
| fusion-aot-11 | 16.7.5 | 4,831 | 4,838 | 4,805 | 0.3% | 125 MB | 26.4 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 4,595 | 4,604 | 4,588 | 0.2% | 126 MB | 28.1 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,353 | 4,525 | 3,968 | 4.7% | 2,290 MB | 538.7 KB |  |
| hive-router | v0.3.10 | 3,051 | 3,058 | 3,036 | 0.3% | 87 MB | 29.1 KB |  |
| grafbase | 0.53.5 | 1,882 | 1,884 | 1,881 | 0.1% | 116 MB | 63.0 KB |  |
| cosmo | 0.365.2 | 1,429 | 1,430 | 1,427 | 0.1% | 165 MB | 118.2 KB |  |
| caliban | 3.2.0 | 1,392 | 1,392 | 1,388 | 0.1% | 4,309 MB | 3,169.5 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 537 | 538 | 537 | 0.1% | 2,756 MB | 5,255.2 KB |  |
| apollo-router | v2.19.0 | 481 | 482 | 480 | 0.2% | 177 MB | 376.0 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 416 | 416 | 416 | 0.0% | 199 MB | 489.8 KB |  |
| hive-gateway | 2.15.6 | 275 | 277 | 274 | 0.4% | 3,575 MB | 13,310.5 KB |  |
| apollo-gateway | 2.14.4 | 268 | 270 | 267 | 0.4% | 2,147 MB | 8,204.5 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.12)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1945524     ✗ 0     
     data_received..................: 57 GB   473 MB/s
     data_sent......................: 780 MB  6.5 MB/s
     http_req_blocked...............: avg=2.56µs  min=812ns    med=1.95µs  max=11.6ms   p(90)=3.12µs  p(95)=3.77µs   p(99.9)=28.43µs
     http_req_connecting............: avg=150ns   min=0s       med=0s      max=3.74ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.04ms  min=799.97µs med=8.09ms  max=281.42ms p(90)=14.5ms  p(95)=17.72ms  p(99.9)=30.46ms
       { expected_response:true }...: avg=9.04ms  min=799.97µs med=8.09ms  max=281.42ms p(90)=14.5ms  p(95)=17.72ms  p(99.9)=30.46ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 648608
     http_req_receiving.............: avg=93.02µs min=24.7µs   med=46.04µs max=100.99ms p(90)=88.14µs p(95)=190.53µs p(99.9)=6.04ms 
     http_req_sending...............: avg=41.96µs min=4.43µs   med=8.27µs  max=200.66ms p(90)=14.31µs p(95)=101.54µs p(99.9)=4.65ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.91ms  min=754.48µs med=7.99ms  max=270.79ms p(90)=14.27ms p(95)=17.44ms  p(99.9)=29.95ms
     http_reqs......................: 648608  5399.974454/s
     iteration_duration.............: avg=9.24ms  min=1.03ms   med=8.28ms  max=293.51ms p(90)=14.71ms p(95)=17.94ms  p(99.9)=30.73ms
     iterations.....................: 648508  5399.141906/s
     success_rate...................: 100.00% ✓ 648508      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.12)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1905825     ✗ 0     
     data_received..................: 56 GB   463 MB/s
     data_sent......................: 764 MB  6.4 MB/s
     http_req_blocked...............: avg=3.26µs  min=952ns    med=2.43µs  max=8.95ms   p(90)=3.69µs  p(95)=4.33µs   p(99.9)=32.59µs
     http_req_connecting............: avg=396ns   min=0s       med=0s      max=8.9ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.23ms  min=802.91µs med=8.26ms  max=311.33ms p(90)=14.99ms p(95)=18.3ms   p(99.9)=31.23ms
       { expected_response:true }...: avg=9.23ms  min=802.91µs med=8.26ms  max=311.33ms p(90)=14.99ms p(95)=18.3ms   p(99.9)=31.23ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 635375
     http_req_receiving.............: avg=98.19µs min=25.8µs   med=47.66µs max=21.1ms   p(90)=89.51µs p(95)=199.49µs p(99.9)=6.44ms 
     http_req_sending...............: avg=43.49µs min=4.45µs   med=8.93µs  max=146.34ms p(90)=14.84µs p(95)=105.24µs p(99.9)=4.74ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.09ms  min=740.19µs med=8.15ms  max=310.41ms p(90)=14.74ms p(95)=18.01ms  p(99.9)=30.71ms
     http_reqs......................: 635375  5290.076279/s
     iteration_duration.............: avg=9.43ms  min=1.09ms   med=8.45ms  max=332.21ms p(90)=15.2ms  p(95)=18.52ms  p(99.9)=31.51ms
     iterations.....................: 635275  5289.243688/s
     success_rate...................: 100.00% ✓ 635275      ✗ 0     
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

     checks.........................: 100.00% ✓ 1839273     ✗ 0     
     data_received..................: 54 GB   447 MB/s
     data_sent......................: 737 MB  6.1 MB/s
     http_req_blocked...............: avg=2.67µs  min=801ns    med=1.94µs  max=8.66ms   p(90)=3.04µs  p(95)=3.67µs   p(99.9)=26.72µs
     http_req_connecting............: avg=360ns   min=0s       med=0s      max=8.43ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.57ms  min=813.64µs med=8.7ms   max=267.69ms p(90)=14.9ms  p(95)=17.8ms   p(99.9)=30.34ms
       { expected_response:true }...: avg=9.57ms  min=813.64µs med=8.7ms   max=267.69ms p(90)=14.9ms  p(95)=17.8ms   p(99.9)=30.34ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 613191
     http_req_receiving.............: avg=93.67µs min=24.77µs  med=46.33µs max=167.65ms p(90)=89.29µs p(95)=194.39µs p(99.9)=5.84ms 
     http_req_sending...............: avg=42.16µs min=4.26µs   med=8.15µs  max=226.3ms  p(90)=14.11µs p(95)=98.62µs  p(99.9)=4.6ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.44ms  min=744.36µs med=8.59ms  max=258.21ms p(90)=14.68ms p(95)=17.54ms  p(99.9)=29.99ms
     http_reqs......................: 613191  5105.364323/s
     iteration_duration.............: avg=9.77ms  min=1.19ms   med=8.89ms  max=279.01ms p(90)=15.1ms  p(95)=18.01ms  p(99.9)=30.67ms
     iterations.....................: 613091  5104.531734/s
     success_rate...................: 100.00% ✓ 613091      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.12)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1832499     ✗ 0     
     data_received..................: 54 GB   445 MB/s
     data_sent......................: 734 MB  6.1 MB/s
     http_req_blocked...............: avg=2.95µs  min=892ns    med=2.38µs  max=6.92ms   p(90)=3.63µs  p(95)=4.25µs   p(99.9)=33.87µs
     http_req_connecting............: avg=130ns   min=0s       med=0s      max=3.41ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.61ms  min=879.44µs med=8.66ms  max=226.71ms p(90)=15.43ms p(95)=18.75ms  p(99.9)=31.52ms
       { expected_response:true }...: avg=9.61ms  min=879.44µs med=8.66ms  max=226.71ms p(90)=15.43ms p(95)=18.75ms  p(99.9)=31.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 610933
     http_req_receiving.............: avg=95.96µs min=25.71µs  med=46.78µs max=72.34ms  p(90)=91.95µs p(95)=215.57µs p(99.9)=5.85ms 
     http_req_sending...............: avg=43.88µs min=4.59µs   med=8.73µs  max=158.26ms p(90)=14.88µs p(95)=112.46µs p(99.9)=4.71ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.47ms  min=821.38µs med=8.55ms  max=225.46ms p(90)=15.19ms p(95)=18.48ms  p(99.9)=31.06ms
     http_reqs......................: 610933  5086.207524/s
     iteration_duration.............: avg=9.81ms  min=1.21ms   med=8.85ms  max=352.55ms p(90)=15.64ms p(95)=18.97ms  p(99.9)=31.85ms
     iterations.....................: 610833  5085.374993/s
     success_rate...................: 100.00% ✓ 610833      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1773315     ✗ 0     
     data_received..................: 52 GB   431 MB/s
     data_sent......................: 711 MB  5.9 MB/s
     http_req_blocked...............: avg=2.5µs    min=781ns    med=1.92µs  max=8.26ms   p(90)=3.17µs  p(95)=3.93µs   p(99.9)=28.88µs
     http_req_connecting............: avg=161ns    min=0s       med=0s      max=3.8ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.94ms   min=977.09µs med=9.11ms  max=287.01ms p(90)=15.29ms p(95)=18.05ms  p(99.9)=30.79ms
       { expected_response:true }...: avg=9.94ms   min=977.09µs med=9.11ms  max=287.01ms p(90)=15.29ms p(95)=18.05ms  p(99.9)=30.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 591205
     http_req_receiving.............: avg=101.03µs min=25.12µs  med=47.01µs max=172.32ms p(90)=94.97µs p(95)=197.79µs p(99.9)=6.85ms 
     http_req_sending...............: avg=43.68µs  min=4.17µs   med=8.16µs  max=199.79ms p(90)=15.37µs p(95)=99.91µs  p(99.9)=4.97ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.79ms   min=899.94µs med=8.99ms  max=286.82ms p(90)=15.07ms p(95)=17.78ms  p(99.9)=30.12ms
     http_reqs......................: 591205  4921.250789/s
     iteration_duration.............: avg=10.14ms  min=1.24ms   med=9.31ms  max=306.28ms p(90)=15.49ms p(95)=18.27ms  p(99.9)=31.07ms
     iterations.....................: 591105  4920.418379/s
     success_rate...................: 100.00% ✓ 591105      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.12)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1766349     ✗ 0     
     data_received..................: 52 GB   429 MB/s
     data_sent......................: 708 MB  5.9 MB/s
     http_req_blocked...............: avg=2.92µs  min=952ns    med=2.36µs  max=5.42ms   p(90)=3.63µs  p(95)=4.26µs   p(99.9)=30.36µs
     http_req_connecting............: avg=167ns   min=0s       med=0s      max=3.75ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.98ms  min=870.31µs med=9.1ms   max=336.98ms p(90)=15.89ms p(95)=18.83ms  p(99.9)=31.48ms
       { expected_response:true }...: avg=9.98ms  min=870.31µs med=9.1ms   max=336.98ms p(90)=15.89ms p(95)=18.83ms  p(99.9)=31.48ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 588883
     http_req_receiving.............: avg=94.14µs min=24.69µs  med=47.08µs max=127.49ms p(90)=89.76µs p(95)=207.65µs p(99.9)=5.52ms 
     http_req_sending...............: avg=41.66µs min=4.6µs    med=8.75µs  max=212.02ms p(90)=14.81µs p(95)=108.09µs p(99.9)=4.23ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.85ms  min=822.87µs med=8.98ms  max=336.54ms p(90)=15.69ms p(95)=18.59ms  p(99.9)=31.1ms 
     http_reqs......................: 588883  4902.419197/s
     iteration_duration.............: avg=10.18ms min=1.03ms   med=9.29ms  max=353.44ms p(90)=16.09ms p(95)=19.05ms  p(99.9)=31.72ms
     iterations.....................: 588783  4901.586702/s
     success_rate...................: 100.00% ✓ 588783      ✗ 0     
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

     checks.........................: 100.00% ✓ 1740831     ✗ 0     
     data_received..................: 51 GB   423 MB/s
     data_sent......................: 698 MB  5.8 MB/s
     http_req_blocked...............: avg=6.93µs  min=832ns    med=1.95µs  max=200.29ms p(90)=3.13µs  p(95)=3.74µs   p(99.9)=28.68µs
     http_req_connecting............: avg=4.54µs  min=0s       med=0s      max=200.13ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.13ms min=934.21µs med=9.37ms  max=205.53ms p(90)=15.22ms p(95)=17.92ms  p(99.9)=29.61ms
       { expected_response:true }...: avg=10.13ms min=934.21µs med=9.37ms  max=205.53ms p(90)=15.22ms p(95)=17.92ms  p(99.9)=29.61ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 580377
     http_req_receiving.............: avg=95.29µs min=23.93µs  med=44.86µs max=126.27ms p(90)=92.88µs p(95)=210.71µs p(99.9)=6.04ms 
     http_req_sending...............: avg=41.62µs min=4.35µs   med=8.17µs  max=188.6ms  p(90)=14.44µs p(95)=104.5µs  p(99.9)=4.36ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.99ms  min=855.26µs med=9.26ms  max=179.8ms  p(90)=15.02ms p(95)=17.67ms  p(99.9)=29.25ms
     http_reqs......................: 580377  4831.711657/s
     iteration_duration.............: avg=10.33ms min=1.52ms   med=9.55ms  max=282.15ms p(90)=15.42ms p(95)=18.14ms  p(99.9)=29.88ms
     iterations.....................: 580277  4830.879144/s
     success_rate...................: 100.00% ✓ 580277      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1656117     ✗ 0     
     data_received..................: 48 GB   402 MB/s
     data_sent......................: 664 MB  5.5 MB/s
     http_req_blocked...............: avg=2.57µs  min=831ns    med=1.96µs  max=4.37ms   p(90)=3.15µs  p(95)=3.79µs   p(99.9)=27.36µs
     http_req_connecting............: avg=178ns   min=0s       med=0s      max=3.89ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.66ms min=1.06ms   med=10.03ms max=297.57ms p(90)=15.64ms p(95)=18.12ms  p(99.9)=30.19ms
       { expected_response:true }...: avg=10.66ms min=1.06ms   med=10.03ms max=297.57ms p(90)=15.64ms p(95)=18.12ms  p(99.9)=30.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 552139
     http_req_receiving.............: avg=97.32µs min=24.18µs  med=46.82µs max=112.05ms p(90)=95.74µs p(95)=207.66µs p(99.9)=6.02ms 
     http_req_sending...............: avg=39.59µs min=4.34µs   med=8.27µs  max=153.5ms  p(90)=15.23µs p(95)=102.07µs p(99.9)=4.04ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.52ms min=986.33µs med=9.91ms  max=297.09ms p(90)=15.44ms p(95)=17.89ms  p(99.9)=29.7ms 
     http_reqs......................: 552139  4595.809313/s
     iteration_duration.............: avg=10.85ms min=1.28ms   med=10.22ms max=323.14ms p(90)=15.84ms p(95)=18.34ms  p(99.9)=30.44ms
     iterations.....................: 552039  4594.976949/s
     success_rate...................: 100.00% ✓ 552039      ✗ 0     
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

     checks.........................: 100.00% ✓ 1568253     ✗ 0     
     data_received..................: 46 GB   381 MB/s
     data_sent......................: 628 MB  5.2 MB/s
     http_req_blocked...............: avg=3.32µs  min=952ns    med=2.68µs  max=5.1ms    p(90)=4.22µs  p(95)=4.96µs   p(99.9)=39.13µs
     http_req_connecting............: avg=191ns   min=0s       med=0s      max=4ms      p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.26ms min=737.43µs med=10.7ms  max=274.11ms p(90)=16.85ms p(95)=19.63ms  p(99.9)=31.6ms 
       { expected_response:true }...: avg=11.26ms min=737.43µs med=10.7ms  max=274.11ms p(90)=16.85ms p(95)=19.63ms  p(99.9)=31.6ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 522851
     http_req_receiving.............: avg=92.98µs min=25.53µs  med=49.33µs max=74.49ms  p(90)=98.01µs p(95)=221.63µs p(99.9)=5.17ms 
     http_req_sending...............: avg=45.27µs min=4.95µs   med=9.82µs  max=231.21ms p(90)=17.33µs p(95)=120.85µs p(99.9)=4.37ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.12ms min=679.75µs med=10.58ms max=273.86ms p(90)=16.65ms p(95)=19.36ms  p(99.9)=31.24ms
     http_reqs......................: 522851  4353.26378/s
     iteration_duration.............: avg=11.46ms min=1.22ms   med=10.9ms  max=288.92ms p(90)=17.06ms p(95)=19.87ms  p(99.9)=31.87ms
     iterations.....................: 522751  4352.431178/s
     success_rate...................: 100.00% ✓ 522751      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1100103     ✗ 0     
     data_received..................: 32 GB   267 MB/s
     data_sent......................: 441 MB  3.7 MB/s
     http_req_blocked...............: avg=3.15µs  min=882ns   med=2.21µs  max=11ms     p(90)=3.61µs  p(95)=4.32µs   p(99.9)=27.7µs 
     http_req_connecting............: avg=603ns   min=0s      med=0s      max=10.69ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.15ms min=1.27ms  med=16.15ms max=270.97ms p(90)=21.68ms p(95)=23.17ms  p(99.9)=30.47ms
       { expected_response:true }...: avg=16.15ms min=1.27ms  med=16.15ms max=270.97ms p(90)=21.68ms p(95)=23.17ms  p(99.9)=30.47ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 366801
     http_req_receiving.............: avg=73.88µs min=25.28µs med=51.38µs max=114.26ms p(90)=93.65µs p(95)=172.72µs p(99.9)=1.37ms 
     http_req_sending...............: avg=35.31µs min=4.68µs  med=10.03µs max=161.62ms p(90)=18.31µs p(95)=107.18µs p(99.9)=1.43ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.04ms min=1.19ms  med=16.04ms max=260.88ms p(90)=21.57ms p(95)=23.06ms  p(99.9)=30.29ms
     http_reqs......................: 366801  3051.943337/s
     iteration_duration.............: avg=16.35ms min=2.52ms  med=16.34ms max=282.83ms p(90)=21.88ms p(95)=23.37ms  p(99.9)=30.68ms
     iterations.....................: 366701  3051.111293/s
     success_rate...................: 100.00% ✓ 366701      ✗ 0     
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

     checks.........................: 100.00% ✓ 678903      ✗ 0     
     data_received..................: 20 GB   165 MB/s
     data_sent......................: 272 MB  2.3 MB/s
     http_req_blocked...............: avg=3.63µs  min=831ns   med=2.24µs  max=9.78ms   p(90)=4.21µs   p(95)=5.23µs   p(99.9)=40.7µs 
     http_req_connecting............: avg=801ns   min=0s      med=0s      max=7.27ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.27ms min=1.86ms  med=25.83ms max=289.06ms p(90)=34.24ms  p(95)=36.91ms  p(99.9)=49.98ms
       { expected_response:true }...: avg=26.27ms min=1.86ms  med=25.83ms max=289.06ms p(90)=34.24ms  p(95)=36.91ms  p(99.9)=49.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 226401
     http_req_receiving.............: avg=81.13µs min=26.05µs med=53.23µs max=43.7ms   p(90)=116.36µs p(95)=189.35µs p(99.9)=1.7ms  
     http_req_sending...............: avg=33.03µs min=4.62µs  med=9.37µs  max=182.59ms p(90)=21.98µs  p(95)=100.41µs p(99.9)=1.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.15ms min=1.8ms   med=25.72ms max=288.72ms p(90)=34.12ms  p(95)=36.78ms  p(99.9)=49.69ms
     http_reqs......................: 226401  1882.646769/s
     iteration_duration.............: avg=26.5ms  min=7.05ms  med=26.04ms max=312.01ms p(90)=34.45ms  p(95)=37.12ms  p(99.9)=50.32ms
     iterations.....................: 226301  1881.815215/s
     success_rate...................: 100.00% ✓ 226301      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 515406      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=3.08µs  min=822ns   med=2.21µs  max=3.96ms   p(90)=3.75µs  p(95)=4.42µs   p(99.9)=30.7µs  
     http_req_connecting............: avg=553ns   min=0s      med=0s      max=3.92ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.69ms min=2.04ms  med=33.71ms max=280.32ms p(90)=50.27ms p(95)=55.31ms  p(99.9)=78.88ms 
       { expected_response:true }...: avg=34.69ms min=2.04ms  med=33.71ms max=280.32ms p(90)=50.27ms p(95)=55.31ms  p(99.9)=78.88ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 171902
     http_req_receiving.............: avg=70.36µs min=27.43µs med=59.81µs max=48.02ms  p(90)=96.35µs p(95)=112.63µs p(99.9)=675.53µs
     http_req_sending...............: avg=19.56µs min=4.62µs  med=10.18µs max=109.08ms p(90)=16.5µs  p(95)=20.1µs   p(99.9)=725.74µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.6ms  min=1.98ms  med=33.62ms max=279.92ms p(90)=50.19ms p(95)=55.21ms  p(99.9)=78.65ms 
     http_reqs......................: 171902  1429.319234/s
     iteration_duration.............: avg=34.91ms min=4.44ms  med=33.91ms max=304.06ms p(90)=50.47ms p(95)=55.5ms   p(99.9)=79.36ms 
     iterations.....................: 171802  1428.48776/s
     success_rate...................: 100.00% ✓ 171802      ✗ 0     
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

     checks.........................: 100.00% ✓ 502509      ✗ 0     
     data_received..................: 15 GB   122 MB/s
     data_sent......................: 201 MB  1.7 MB/s
     http_req_blocked...............: avg=3.61µs  min=1.1µs   med=2.76µs  max=4.17ms   p(90)=4.27µs  p(95)=4.95µs   p(99.9)=35.8µs  
     http_req_connecting............: avg=569ns   min=0s      med=0s      max=4.13ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.57ms min=2.21ms  med=34.58ms max=284.39ms p(90)=50.83ms p(95)=56.11ms  p(99.9)=86.25ms 
       { expected_response:true }...: avg=35.57ms min=2.21ms  med=34.58ms max=284.39ms p(90)=50.83ms p(95)=56.11ms  p(99.9)=86.25ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 167603
     http_req_receiving.............: avg=69.77µs min=27.22µs med=58.64µs max=78.64ms  p(90)=92.57µs p(95)=107.17µs p(99.9)=814.51µs
     http_req_sending...............: avg=21.56µs min=5.15µs  med=11.72µs max=115.97ms p(90)=17.23µs p(95)=20.56µs  p(99.9)=740.61µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=35.48ms min=2.16ms  med=34.49ms max=284.18ms p(90)=50.74ms p(95)=56.02ms  p(99.9)=85.94ms 
     http_reqs......................: 167603  1392.935378/s
     iteration_duration.............: avg=35.81ms min=5.33ms  med=34.79ms max=299.45ms p(90)=51.04ms p(95)=56.33ms  p(99.9)=86.79ms 
     iterations.....................: 167503  1392.104285/s
     success_rate...................: 100.00% ✓ 167503      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 194067     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   645 kB/s
     http_req_blocked...............: avg=4.6µs   min=1.13µs  med=2.87µs  max=4.1ms    p(90)=4.29µs   p(95)=4.89µs   p(99.9)=45.41µs 
     http_req_connecting............: avg=1.45µs  min=0s      med=0s      max=4.06ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.4ms  min=3.89ms  med=89.32ms max=370.94ms p(90)=111.82ms p(95)=123.33ms p(99.9)=234.35ms
       { expected_response:true }...: avg=92.4ms  min=3.89ms  med=89.32ms max=370.94ms p(90)=111.82ms p(95)=123.33ms p(99.9)=234.35ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64789
     http_req_receiving.............: avg=75.43µs min=29.26µs med=68.06µs max=11.78ms  p(90)=100.46µs p(95)=112.99µs p(99.9)=599.94µs
     http_req_sending...............: avg=18.48µs min=4.98µs  med=13.49µs max=47.82ms  p(90)=19.36µs  p(95)=21.37µs  p(99.9)=558.38µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.3ms  min=3.78ms  med=89.22ms max=365.82ms p(90)=111.72ms p(95)=123.24ms p(99.9)=234.06ms
     http_reqs......................: 64789   537.429522/s
     iteration_duration.............: avg=92.76ms min=33.07ms med=89.57ms max=377.34ms p(90)=112.04ms p(95)=123.59ms p(99.9)=238.8ms 
     iterations.....................: 64689   536.600014/s
     success_rate...................: 100.00% ✓ 64689      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 173955     ✗ 0    
     data_received..................: 5.1 GB  42 MB/s
     data_sent......................: 70 MB   578 kB/s
     http_req_blocked...............: avg=4.87µs   min=1.25µs  med=3.12µs   max=3.45ms   p(90)=4.52µs   p(95)=5.11µs   p(99.9)=50.57µs 
     http_req_connecting............: avg=1.54µs   min=0s      med=0s       max=3.44ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=103.08ms min=4.35ms  med=101.06ms max=307.34ms p(90)=138.95ms p(95)=150.13ms p(99.9)=197.25ms
       { expected_response:true }...: avg=103.08ms min=4.35ms  med=101.06ms max=307.34ms p(90)=138.95ms p(95)=150.13ms p(99.9)=197.25ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 58085
     http_req_receiving.............: avg=77.17µs  min=29.85µs med=71.02µs  max=38.28ms  p(90)=101.49µs p(95)=113.93µs p(99.9)=505.22µs
     http_req_sending...............: avg=25.66µs  min=5.24µs  med=14.35µs  max=104.77ms p(90)=19.71µs  p(95)=21.59µs  p(99.9)=540.96µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=102.98ms min=4.28ms  med=100.97ms max=306.92ms p(90)=138.85ms p(95)=150.03ms p(99.9)=196.85ms
     http_reqs......................: 58085   481.649544/s
     iteration_duration.............: avg=103.5ms  min=15.82ms med=101.35ms max=330.47ms p(90)=139.23ms p(95)=150.46ms p(99.9)=200.4ms 
     iterations.....................: 57985   480.820329/s
     success_rate...................: 100.00% ✓ 57985      ✗ 0    
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

     checks.........................: 100.00% ✓ 150651     ✗ 0    
     data_received..................: 4.4 GB  37 MB/s
     data_sent......................: 60 MB   501 kB/s
     http_req_blocked...............: avg=4.94µs   min=1.08µs  med=3µs      max=3.6ms    p(90)=4.39µs   p(95)=4.9µs    p(99.9)=205.87µs
     http_req_connecting............: avg=1.75µs   min=0s      med=0s       max=3.56ms   p(90)=0s       p(95)=0s       p(99.9)=56.42µs 
     http_req_duration..............: avg=119.04ms min=5.33ms  med=116.6ms  max=330.56ms p(90)=156.12ms p(95)=168.21ms p(99.9)=217.94ms
       { expected_response:true }...: avg=119.04ms min=5.33ms  med=116.6ms  max=330.56ms p(90)=156.12ms p(95)=168.21ms p(99.9)=217.94ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 50317
     http_req_receiving.............: avg=77.53µs  min=27.99µs med=74.55µs  max=37.77ms  p(90)=103.54µs p(95)=115.44µs p(99.9)=425.72µs
     http_req_sending...............: avg=26.44µs  min=5.1µs   med=14.89µs  max=147.14ms p(90)=19.57µs  p(95)=21.34µs  p(99.9)=446.88µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=118.94ms min=5.24ms  med=116.5ms  max=329.69ms p(90)=156.02ms p(95)=168.08ms p(99.9)=217.82ms
     http_reqs......................: 50317   416.930339/s
     iteration_duration.............: avg=119.52ms min=27.81ms med=116.88ms max=345.91ms p(90)=156.4ms  p(95)=168.48ms p(99.9)=219.85ms
     iterations.....................: 50217   416.101732/s
     success_rate...................: 100.00% ✓ 50217      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 99699      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   331 kB/s
     http_req_blocked...............: avg=6.42µs   min=1.1µs   med=3.18µs   max=4.25ms   p(90)=4.53µs   p(95)=5.09µs   p(99.9)=1.39ms  
     http_req_connecting............: avg=3.06µs   min=0s      med=0s       max=4.21ms   p(90)=0s       p(95)=0s       p(99.9)=1.37ms  
     http_req_duration..............: avg=179.85ms min=5.62ms  med=161.69ms max=803.63ms p(90)=205.47ms p(95)=232.27ms p(99.9)=686.96ms
       { expected_response:true }...: avg=179.85ms min=5.62ms  med=161.69ms max=803.63ms p(90)=205.47ms p(95)=232.27ms p(99.9)=686.96ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33333
     http_req_receiving.............: avg=91.25µs  min=32.14µs med=88.29µs  max=8.09ms   p(90)=117.95µs p(95)=129.87µs p(99.9)=728.3µs 
     http_req_sending...............: avg=24.68µs  min=5.32µs  med=17.18µs  max=66.78ms  p(90)=21.36µs  p(95)=23.08µs  p(99.9)=462.9µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=179.74ms min=5.54ms  med=161.56ms max=803.52ms p(90)=205.38ms p(95)=232.19ms p(99.9)=686.84ms
     http_reqs......................: 33333   275.484934/s
     iteration_duration.............: avg=180.65ms min=32.63ms med=162.03ms max=803.87ms p(90)=205.86ms p(95)=232.84ms p(99.9)=687.21ms
     iterations.....................: 33233   274.658471/s
     success_rate...................: 100.00% ✓ 33233      ✗ 0    
     vus............................: 2       min=2        max=50 
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

     checks.........................: 100.00% ✓ 97185      ✗ 0    
     data_received..................: 2.8 GB  24 MB/s
     data_sent......................: 39 MB   323 kB/s
     http_req_blocked...............: avg=6.16µs   min=1.09µs  med=2.89µs   max=4.07ms   p(90)=4.09µs   p(95)=4.6µs    p(99.9)=1.45ms  
     http_req_connecting............: avg=3.1µs    min=0s      med=0s       max=4.03ms   p(90)=0s       p(95)=0s       p(99.9)=1.43ms  
     http_req_duration..............: avg=184.51ms min=7.55ms  med=184.85ms max=403.72ms p(90)=209ms    p(95)=214.88ms p(99.9)=285.05ms
       { expected_response:true }...: avg=184.51ms min=7.55ms  med=184.85ms max=403.72ms p(90)=209ms    p(95)=214.88ms p(99.9)=285.05ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32495
     http_req_receiving.............: avg=90.65µs  min=28.11µs med=80.98µs  max=222.3ms  p(90)=109.98µs p(95)=120.49µs p(99.9)=531.6µs 
     http_req_sending...............: avg=27.38µs  min=5.17µs  med=15.41µs  max=85.88ms  p(90)=19.29µs  p(95)=20.93µs  p(99.9)=479.59µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.39ms min=7.47ms  med=184.73ms max=403.59ms p(90)=208.89ms p(95)=214.74ms p(99.9)=284.39ms
     http_reqs......................: 32495   268.604748/s
     iteration_duration.............: avg=185.33ms min=44.58ms med=185.32ms max=414.15ms p(90)=209.25ms p(95)=215.16ms p(99.9)=285.89ms
     iterations.....................: 32395   267.778144/s
     success_rate...................: 100.00% ✓ 32395      ✗ 0    
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

