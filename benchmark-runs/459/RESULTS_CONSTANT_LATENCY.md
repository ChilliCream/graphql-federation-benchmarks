## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.7 | 3,427 | 3,442 | 3,406 | 0.4% | 388 MB | 115.9 KB |  |
| fusion-net-11 | 16.7.3 | 3,416 | 3,442 | 3,414 | 0.4% | 380 MB | 113.9 KB |  |
| fusion-aot-11 | 16.7.3 | 3,412 | 3,432 | 3,398 | 0.4% | 135 MB | 40.6 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.7 | 3,361 | 3,374 | 3,329 | 0.5% | 131 MB | 40.0 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,259 | 3,295 | 3,248 | 0.6% | 2,308 MB | 725.1 KB |  |
| fusion-fed-net-11 | 16.7.3 | 2,799 | 2,804 | 2,789 | 0.2% | 397 MB | 145.3 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.7 | 2,787 | 2,790 | 2,784 | 0.1% | 405 MB | 148.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.7 | 2,742 | 2,751 | 2,737 | 0.2% | 134 MB | 50.1 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 2,739 | 2,743 | 2,729 | 0.2% | 133 MB | 49.8 KB |  |
| hive-router | v0.3.6 | 2,054 | 2,059 | 2,044 | 0.3% | 93 MB | 46.5 KB |  |
| caliban | 3.2.0 | 1,460 | 1,461 | 1,456 | 0.1% | 5,959 MB | 4,179.2 KB |  |
| grafbase | 0.53.5 | 1,445 | 1,450 | 1,439 | 0.3% | 100 MB | 70.8 KB |  |
| cosmo | 0.363.0 | 1,424 | 1,425 | 1,422 | 0.1% | 147 MB | 105.8 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 523 | 525 | 523 | 0.2% | 2,756 MB | 5,395.9 KB |  |
| apollo-router | v2.19.0 | 484 | 488 | 484 | 0.4% | 180 MB | 379.9 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 390 | 390 | 389 | 0.1% | 207 MB | 542.5 KB |  |
| apollo-gateway | 2.14.4 | 271 | 271 | 269 | 0.3% | 2,153 MB | 8,137.2 KB |  |
| hive-gateway | 2.15.3 | 267 | 267 | 266 | 0.2% | 3,557 MB | 13,641.2 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1243596     ✗ 0     
     data_received..................: 36 GB   300 MB/s
     data_sent......................: 498 MB  4.1 MB/s
     http_req_blocked...............: avg=2.39µs  min=801ns   med=1.82µs  max=7.54ms   p(90)=3µs     p(95)=3.73µs   p(99.9)=26.09µs
     http_req_connecting............: avg=193ns   min=0s      med=0s      max=3.69ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.26ms min=8.28ms  med=13.83ms max=301.22ms p(90)=17.75ms p(95)=19.15ms  p(99.9)=27.79ms
       { expected_response:true }...: avg=14.26ms min=8.28ms  med=13.83ms max=301.22ms p(90)=17.75ms p(95)=19.15ms  p(99.9)=27.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 414632
     http_req_receiving.............: avg=68.52µs min=24.45µs med=42.93µs max=9.84ms   p(90)=91.72µs p(95)=174.83µs p(99.9)=1.96ms 
     http_req_sending...............: avg=32.04µs min=4.11µs  med=7.82µs  max=279.28ms p(90)=16.29µs p(95)=93.06µs  p(99.9)=2.06ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.16ms min=8.23ms  med=13.73ms max=300.72ms p(90)=17.65ms p(95)=19.03ms  p(99.9)=27.59ms
     http_reqs......................: 414632  3427.995852/s
     iteration_duration.............: avg=14.46ms min=8.46ms  med=14.03ms max=325.67ms p(90)=17.94ms p(95)=19.34ms  p(99.9)=28.02ms
     iterations.....................: 414532  3427.169096/s
     success_rate...................: 100.00% ✓ 414532      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1239321     ✗ 0     
     data_received..................: 36 GB   299 MB/s
     data_sent......................: 497 MB  4.1 MB/s
     http_req_blocked...............: avg=2.34µs  min=771ns   med=1.76µs  max=3.44ms   p(90)=3.03µs  p(95)=3.85µs   p(99.9)=24.36µs
     http_req_connecting............: avg=206ns   min=0s      med=0s      max=3.41ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.32ms min=8.35ms  med=13.9ms  max=288.4ms  p(90)=17.76ms p(95)=19.1ms   p(99.9)=27.24ms
       { expected_response:true }...: avg=14.32ms min=8.35ms  med=13.9ms  max=288.4ms  p(90)=17.76ms p(95)=19.1ms   p(99.9)=27.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 413207
     http_req_receiving.............: avg=68.52µs min=23.61µs med=42.52µs max=131.64ms p(90)=92.22µs p(95)=168.82µs p(99.9)=2.04ms 
     http_req_sending...............: avg=31.7µs  min=4.1µs   med=7.63µs  max=256.76ms p(90)=16.81µs p(95)=90.71µs  p(99.9)=1.85ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.22ms min=8.28ms  med=13.8ms  max=286.52ms p(90)=17.66ms p(95)=18.99ms  p(99.9)=26.9ms 
     http_reqs......................: 413207  3416.123395/s
     iteration_duration.............: avg=14.51ms min=8.48ms  med=14.09ms max=306.13ms p(90)=17.95ms p(95)=19.29ms  p(99.9)=27.48ms
     iterations.....................: 413107  3415.296661/s
     success_rate...................: 100.00% ✓ 413107      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1238079     ✗ 0     
     data_received..................: 36 GB   299 MB/s
     data_sent......................: 496 MB  4.1 MB/s
     http_req_blocked...............: avg=2.44µs  min=841ns   med=1.85µs  max=10.43ms  p(90)=3.03µs  p(95)=3.77µs   p(99.9)=24.42µs
     http_req_connecting............: avg=224ns   min=0s      med=0s      max=3.76ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.33ms min=8.35ms  med=13.88ms max=282.5ms  p(90)=17.72ms p(95)=19.1ms   p(99.9)=27.41ms
       { expected_response:true }...: avg=14.33ms min=8.35ms  med=13.88ms max=282.5ms  p(90)=17.72ms p(95)=19.1ms   p(99.9)=27.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 412793
     http_req_receiving.............: avg=66.69µs min=24.42µs med=42.12µs max=111.76ms p(90)=88.3µs  p(95)=168.66µs p(99.9)=1.76ms 
     http_req_sending...............: avg=30.88µs min=4.44µs  med=7.87µs  max=224.41ms p(90)=16.34µs p(95)=92µs     p(99.9)=1.76ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.23ms min=8.28ms  med=13.79ms max=281.99ms p(90)=17.62ms p(95)=18.99ms  p(99.9)=27.13ms
     http_reqs......................: 412793  3412.72075/s
     iteration_duration.............: avg=14.53ms min=8.51ms  med=14.08ms max=291.74ms p(90)=17.91ms p(95)=19.29ms  p(99.9)=27.62ms
     iterations.....................: 412693  3411.894011/s
     success_rate...................: 100.00% ✓ 412693      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1219593     ✗ 0     
     data_received..................: 36 GB   294 MB/s
     data_sent......................: 489 MB  4.0 MB/s
     http_req_blocked...............: avg=2.9µs   min=872ns   med=2.28µs  max=4.09ms   p(90)=3.72µs  p(95)=4.52µs   p(99.9)=31.54µs
     http_req_connecting............: avg=245ns   min=0s      med=0s      max=4.05ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.55ms min=8.38ms  med=14.1ms  max=299.64ms p(90)=17.99ms p(95)=19.38ms  p(99.9)=28.78ms
       { expected_response:true }...: avg=14.55ms min=8.38ms  med=14.1ms  max=299.64ms p(90)=17.99ms p(95)=19.38ms  p(99.9)=28.78ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 406631
     http_req_receiving.............: avg=83.61µs min=24.71µs med=45.53µs max=235.11ms p(90)=97.06µs p(95)=181.63µs p(99.9)=2.02ms 
     http_req_sending...............: avg=33.45µs min=4.26µs  med=8.57µs  max=238.66ms p(90)=18.25µs p(95)=99.03µs  p(99.9)=1.91ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.43ms min=8.32ms  med=14ms    max=75.62ms  p(90)=17.88ms p(95)=19.26ms  p(99.9)=28.59ms
     http_reqs......................: 406631  3361.507119/s
     iteration_duration.............: avg=14.75ms min=8.67ms  med=14.3ms  max=313.4ms  p(90)=18.18ms p(95)=19.58ms  p(99.9)=29.02ms
     iterations.....................: 406531  3360.680446/s
     success_rate...................: 100.00% ✓ 406531      ✗ 0     
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

     checks.........................: 100.00% ✓ 1182588     ✗ 0     
     data_received..................: 35 GB   285 MB/s
     data_sent......................: 474 MB  3.9 MB/s
     http_req_blocked...............: avg=2.5µs   min=782ns   med=1.92µs  max=4.24ms   p(90)=3.13µs  p(95)=3.85µs   p(99.9)=24.34µs
     http_req_connecting............: avg=246ns   min=0s      med=0s      max=4.21ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=15.01ms min=8.9ms   med=14.68ms max=315.85ms p(90)=18.09ms p(95)=19.29ms  p(99.9)=26.41ms
       { expected_response:true }...: avg=15.01ms min=8.9ms   med=14.68ms max=315.85ms p(90)=18.09ms p(95)=19.29ms  p(99.9)=26.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 394296
     http_req_receiving.............: avg=75.05µs min=24.45µs med=44.41µs max=183.71ms p(90)=88.08µs p(95)=158.02µs p(99.9)=1.55ms 
     http_req_sending...............: avg=29.4µs  min=4.43µs  med=8.19µs  max=62.77ms  p(90)=16.04µs p(95)=90.41µs  p(99.9)=1.56ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.91ms min=8.82ms  med=14.59ms max=146.49ms p(90)=17.99ms p(95)=19.18ms  p(99.9)=26.19ms
     http_reqs......................: 394296  3259.347024/s
     iteration_duration.............: avg=15.21ms min=9.04ms  med=14.87ms max=326.11ms p(90)=18.28ms p(95)=19.48ms  p(99.9)=26.59ms
     iterations.....................: 394196  3258.5204/s
     success_rate...................: 100.00% ✓ 394196      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1019358     ✗ 0     
     data_received..................: 30 GB   245 MB/s
     data_sent......................: 408 MB  3.4 MB/s
     http_req_blocked...............: avg=3.23µs  min=852ns   med=2.24µs  max=9.24ms   p(90)=3.76µs  p(95)=4.55µs   p(99.9)=32.89µs
     http_req_connecting............: avg=563ns   min=0s      med=0s      max=9.05ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.43ms min=11.7ms  med=16.99ms max=281.43ms p(90)=20.49ms p(95)=21.76ms  p(99.9)=29.03ms
       { expected_response:true }...: avg=17.43ms min=11.7ms  med=16.99ms max=281.43ms p(90)=20.49ms p(95)=21.76ms  p(99.9)=29.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 339886
     http_req_receiving.............: avg=69.96µs min=24.5µs  med=45.52µs max=84.87ms  p(90)=96.25µs p(95)=160.87µs p(99.9)=1.63ms 
     http_req_sending...............: avg=30.91µs min=4.21µs  med=8.42µs  max=160.42ms p(90)=17.61µs p(95)=89.67µs  p(99.9)=1.6ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.33ms min=11.59ms med=16.9ms  max=272.57ms p(90)=20.38ms p(95)=21.64ms  p(99.9)=28.78ms
     http_reqs......................: 339886  2799.919798/s
     iteration_duration.............: avg=17.64ms min=11.91ms med=17.19ms max=292.31ms p(90)=20.69ms p(95)=21.96ms  p(99.9)=29.25ms
     iterations.....................: 339786  2799.096016/s
     success_rate...................: 100.00% ✓ 339786      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1014942     ✗ 0     
     data_received..................: 30 GB   244 MB/s
     data_sent......................: 407 MB  3.3 MB/s
     http_req_blocked...............: avg=2.54µs  min=821ns   med=1.84µs  max=4.45ms   p(90)=3.18µs  p(95)=4.02µs  p(99.9)=26.62µs
     http_req_connecting............: avg=331ns   min=0s      med=0s      max=4.39ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=17.52ms min=11.64ms med=17.09ms max=284.28ms p(90)=20.57ms p(95)=21.81ms p(99.9)=28.99ms
       { expected_response:true }...: avg=17.52ms min=11.64ms med=17.09ms max=284.28ms p(90)=20.57ms p(95)=21.81ms p(99.9)=28.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 338414
     http_req_receiving.............: avg=66.14µs min=24.42µs med=44.21µs max=120.05ms p(90)=89.49µs p(95)=141.1µs p(99.9)=1.44ms 
     http_req_sending...............: avg=27.44µs min=4.29µs  med=7.82µs  max=119.32ms p(90)=15.96µs p(95)=79.94µs p(99.9)=1.49ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.43ms min=11.57ms med=17ms    max=283.61ms p(90)=20.47ms p(95)=21.69ms p(99.9)=28.78ms
     http_reqs......................: 338414  2787.666034/s
     iteration_duration.............: avg=17.72ms min=11.9ms  med=17.29ms max=300.15ms p(90)=20.77ms p(95)=22ms    p(99.9)=29.2ms 
     iterations.....................: 338314  2786.84229/s
     success_rate...................: 100.00% ✓ 338314      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 998589      ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 400 MB  3.3 MB/s
     http_req_blocked...............: avg=2.46µs  min=792ns   med=1.82µs  max=4.03ms   p(90)=3.12µs  p(95)=3.92µs   p(99.9)=25.1µs 
     http_req_connecting............: avg=274ns   min=0s      med=0s      max=3.99ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.81ms min=11.98ms med=17.41ms max=285.35ms p(90)=20.78ms p(95)=22ms     p(99.9)=29.11ms
       { expected_response:true }...: avg=17.81ms min=11.98ms med=17.41ms max=285.35ms p(90)=20.78ms p(95)=22ms     p(99.9)=29.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 332963
     http_req_receiving.............: avg=66.07µs min=23.31µs med=43.38µs max=170.43ms p(90)=90µs    p(95)=140.07µs p(99.9)=1.42ms 
     http_req_sending...............: avg=25.73µs min=4.26µs  med=7.83µs  max=24.65ms  p(90)=16.17µs p(95)=77.67µs  p(99.9)=1.27ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.72ms min=11.92ms med=17.33ms max=285.23ms p(90)=20.68ms p(95)=21.89ms  p(99.9)=28.85ms
     http_reqs......................: 332963  2742.626101/s
     iteration_duration.............: avg=18.01ms min=12.14ms med=17.61ms max=294.13ms p(90)=20.98ms p(95)=22.19ms  p(99.9)=29.41ms
     iterations.....................: 332863  2741.802398/s
     success_rate...................: 100.00% ✓ 332863      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 997401      ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 400 MB  3.3 MB/s
     http_req_blocked...............: avg=2.49µs  min=802ns   med=1.87µs  max=4.04ms   p(90)=3.11µs  p(95)=3.85µs   p(99.9)=23.37µs
     http_req_connecting............: avg=273ns   min=0s      med=0s      max=4ms      p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.83ms min=11.88ms med=17.42ms max=268.19ms p(90)=20.87ms p(95)=22.09ms  p(99.9)=28.74ms
       { expected_response:true }...: avg=17.83ms min=11.88ms med=17.42ms max=268.19ms p(90)=20.87ms p(95)=22.09ms  p(99.9)=28.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 332567
     http_req_receiving.............: avg=66.06µs min=24.71µs med=45.31µs max=159.94ms p(90)=88.94µs p(95)=135.14µs p(99.9)=1.29ms 
     http_req_sending...............: avg=27.21µs min=4.41µs  med=8.02µs  max=154.07ms p(90)=15.56µs p(95)=76.3µs   p(99.9)=1.37ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.74ms min=11.82ms med=17.33ms max=267.66ms p(90)=20.77ms p(95)=21.98ms  p(99.9)=28.53ms
     http_reqs......................: 332567  2739.284752/s
     iteration_duration.............: avg=18.03ms min=12.07ms med=17.61ms max=295.97ms p(90)=21.06ms p(95)=22.29ms  p(99.9)=28.96ms
     iterations.....................: 332467  2738.461073/s
     success_rate...................: 100.00% ✓ 332467      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 751032      ✗ 0     
     data_received..................: 22 GB   180 MB/s
     data_sent......................: 301 MB  2.5 MB/s
     http_req_blocked...............: avg=2.83µs  min=842ns   med=2.08µs  max=4.12ms   p(90)=3.75µs  p(95)=4.47µs   p(99.9)=30.49µs 
     http_req_connecting............: avg=372ns   min=0s      med=0s      max=4.09ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.75ms min=17.4ms  med=23.4ms  max=295.72ms p(90)=26.73ms p(95)=27.79ms  p(99.9)=33.18ms 
       { expected_response:true }...: avg=23.75ms min=17.4ms  med=23.4ms  max=295.72ms p(90)=26.73ms p(95)=27.79ms  p(99.9)=33.18ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 250444
     http_req_receiving.............: avg=62.79µs min=23.45µs med=47.83µs max=49.95ms  p(90)=89.86µs p(95)=112.18µs p(99.9)=852.71µs
     http_req_sending...............: avg=23.81µs min=4.22µs  med=9.09µs  max=113ms    p(90)=17.37µs p(95)=23.09µs  p(99.9)=882.27µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.66ms min=17.33ms med=23.32ms max=295.1ms  p(90)=26.64ms p(95)=27.7ms   p(99.9)=33.01ms 
     http_reqs......................: 250444  2054.914218/s
     iteration_duration.............: avg=23.95ms min=17.67ms med=23.61ms max=303.79ms p(90)=26.93ms p(95)=27.99ms  p(99.9)=33.38ms 
     iterations.....................: 250344  2054.093709/s
     success_rate...................: 100.00% ✓ 250344      ✗ 0     
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

     checks.........................: 100.00% ✓ 534042      ✗ 0     
     data_received..................: 16 GB   128 MB/s
     data_sent......................: 214 MB  1.8 MB/s
     http_req_blocked...............: avg=3.28µs  min=852ns   med=2.39µs  max=4.19ms   p(90)=4.16µs   p(95)=4.94µs   p(99.9)=30.2µs  
     http_req_connecting............: avg=550ns   min=0s      med=0s      max=4.15ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.47ms min=18.37ms med=32.97ms max=305.91ms p(90)=39.07ms  p(95)=41.19ms  p(99.9)=55.51ms 
       { expected_response:true }...: avg=33.47ms min=18.37ms med=32.97ms max=305.91ms p(90)=39.07ms  p(95)=41.19ms  p(99.9)=55.51ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 178114
     http_req_receiving.............: avg=74.44µs min=26.32µs med=60.88µs max=160.8ms  p(90)=101.46µs p(95)=120.49µs p(99.9)=869.77µs
     http_req_sending...............: avg=22.13µs min=4.76µs  med=10.95µs max=129.7ms  p(90)=18.6µs   p(95)=22.73µs  p(99.9)=769.78µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.37ms min=18.26ms med=32.88ms max=305.6ms  p(90)=38.97ms  p(95)=41.09ms  p(99.9)=55.32ms 
     http_reqs......................: 178114  1460.388805/s
     iteration_duration.............: avg=33.69ms min=21.5ms  med=33.18ms max=324.76ms p(90)=39.28ms  p(95)=41.4ms   p(99.9)=55.98ms 
     iterations.....................: 178014  1459.568886/s
     success_rate...................: 100.00% ✓ 178014      ✗ 0     
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

     checks.........................: 100.00% ✓ 528426     ✗ 0     
     data_received..................: 15 GB   127 MB/s
     data_sent......................: 212 MB  1.7 MB/s
     http_req_blocked...............: avg=3.34µs  min=821ns   med=2.15µs  max=4.85ms   p(90)=4.64µs   p(95)=5.63µs  p(99.9)=36.51µs
     http_req_connecting............: avg=554ns   min=0s      med=0s      max=4.25ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=33.8ms  min=17.53ms med=33.43ms max=287.57ms p(90)=39.35ms  p(95)=41.06ms p(99.9)=49.48ms
       { expected_response:true }...: avg=33.8ms  min=17.53ms med=33.43ms max=287.57ms p(90)=39.35ms  p(95)=41.06ms p(99.9)=49.48ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 176242
     http_req_receiving.............: avg=79.83µs min=26.42µs med=56.29µs max=238.2ms  p(90)=118.48µs p(95)=155.9µs p(99.9)=1.26ms 
     http_req_sending...............: avg=26.97µs min=4.47µs  med=9.29µs  max=152.68ms p(90)=21.76µs  p(95)=31.08µs p(99.9)=1.06ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=33.7ms  min=17.47ms med=33.33ms max=287.21ms p(90)=39.25ms  p(95)=40.96ms p(99.9)=49.23ms
     http_reqs......................: 176242  1445.43249/s
     iteration_duration.............: avg=34.05ms min=21ms    med=33.66ms max=307.85ms p(90)=39.57ms  p(95)=41.28ms p(99.9)=49.77ms
     iterations.....................: 176142  1444.61235/s
     success_rate...................: 100.00% ✓ 176142     ✗ 0     
     vus............................: 50      min=0        max=50  
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.363.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 520821      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 209 MB  1.7 MB/s
     http_req_blocked...............: avg=2.76µs  min=972ns   med=2.06µs  max=3.58ms   p(90)=3.54µs  p(95)=4.23µs   p(99.9)=27.09µs 
     http_req_connecting............: avg=363ns   min=0s      med=0s      max=3.55ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.34ms min=18.2ms  med=33.79ms max=284.13ms p(90)=40.96ms p(95)=43.21ms  p(99.9)=55.02ms 
       { expected_response:true }...: avg=34.34ms min=18.2ms  med=33.79ms max=284.13ms p(90)=40.96ms p(95)=43.21ms  p(99.9)=55.02ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 173707
     http_req_receiving.............: avg=71.63µs min=25.46µs med=59.55µs max=116.72ms p(90)=97.47µs p(95)=114.56µs p(99.9)=709.95µs
     http_req_sending...............: avg=21.14µs min=4.7µs   med=9.9µs   max=144.16ms p(90)=16.25µs p(95)=19.98µs  p(99.9)=757.61µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.25ms min=18.04ms med=33.7ms  max=283.22ms p(90)=40.87ms p(95)=43.12ms  p(99.9)=54.87ms 
     http_reqs......................: 173707  1424.297873/s
     iteration_duration.............: avg=34.55ms min=20.71ms med=33.98ms max=302.82ms p(90)=41.15ms p(95)=43.41ms  p(99.9)=55.26ms 
     iterations.....................: 173607  1423.47793/s
     success_rate...................: 100.00% ✓ 173607      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 191871     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   629 kB/s
     http_req_blocked...............: avg=5.08µs  min=1.32µs  med=3.32µs  max=4.04ms   p(90)=4.83µs   p(95)=5.48µs   p(99.9)=44.96µs 
     http_req_connecting............: avg=1.52µs  min=0s      med=0s      max=4ms      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.46ms min=20.36ms med=91.39ms max=351.08ms p(90)=112.69ms p(95)=121.39ms p(99.9)=220.24ms
       { expected_response:true }...: avg=93.46ms min=20.36ms med=91.39ms max=351.08ms p(90)=112.69ms p(95)=121.39ms p(99.9)=220.24ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64057
     http_req_receiving.............: avg=89.67µs min=29.41µs med=77.34µs max=138.17ms p(90)=110.46µs p(95)=122.65µs p(99.9)=614.21µs
     http_req_sending...............: avg=22.7µs  min=5.66µs  med=14.83µs max=58.27ms  p(90)=20.61µs  p(95)=22.77µs  p(99.9)=576.81µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.35ms min=20.25ms med=91.29ms max=317.99ms p(90)=112.57ms p(95)=121.23ms p(99.9)=219.51ms
     http_reqs......................: 64057   523.969215/s
     iteration_duration.............: avg=93.83ms min=35ms    med=91.65ms max=361.95ms p(90)=112.95ms p(95)=121.67ms p(99.9)=221.34ms
     iterations.....................: 63957   523.151241/s
     success_rate...................: 100.00% ✓ 63957      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 177501     ✗ 0    
     data_received..................: 5.2 GB  42 MB/s
     data_sent......................: 71 MB   582 kB/s
     http_req_blocked...............: avg=4.98µs   min=982ns   med=2.59µs  max=7.58ms   p(90)=4.01µs   p(95)=4.59µs   p(99.9)=55.98µs 
     http_req_connecting............: avg=1.95µs   min=0s      med=0s      max=5.14ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=101.05ms min=19.85ms med=99.21ms max=304.24ms p(90)=128.06ms p(95)=137.13ms p(99.9)=177.86ms
       { expected_response:true }...: avg=101.05ms min=19.85ms med=99.21ms max=304.24ms p(90)=128.06ms p(95)=137.13ms p(99.9)=177.86ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 59267
     http_req_receiving.............: avg=78.02µs  min=28.19µs med=68.39µs max=132.37ms p(90)=101.46µs p(95)=113.76µs p(99.9)=480.66µs
     http_req_sending...............: avg=20.05µs  min=4.9µs   med=13.06µs max=106.3ms  p(90)=18.93µs  p(95)=20.84µs  p(99.9)=502.48µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=100.95ms min=19.7ms  med=99.13ms max=303.82ms p(90)=127.96ms p(95)=137.06ms p(99.9)=177.28ms
     http_reqs......................: 59267   484.966075/s
     iteration_duration.............: avg=101.43ms min=31.01ms med=99.48ms max=315.26ms p(90)=128.29ms p(95)=137.37ms p(99.9)=179.35ms
     iterations.....................: 59167   484.147802/s
     success_rate...................: 100.00% ✓ 59167      ✗ 0    
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

     checks.........................: 100.00% ✓ 142965     ✗ 0    
     data_received..................: 4.2 GB  34 MB/s
     data_sent......................: 57 MB   469 kB/s
     http_req_blocked...............: avg=4.75µs   min=1.07µs  med=2.78µs   max=3.54ms   p(90)=4.17µs   p(95)=4.7µs    p(99.9)=181.48µs
     http_req_connecting............: avg=1.79µs   min=0s      med=0s       max=3.49ms   p(90)=0s       p(95)=0s       p(99.9)=108.58µs
     http_req_duration..............: avg=125.48ms min=20.96ms med=123.71ms max=340.07ms p(90)=155.43ms p(95)=166.17ms p(99.9)=216.03ms
       { expected_response:true }...: avg=125.48ms min=20.96ms med=123.71ms max=340.07ms p(90)=155.43ms p(95)=166.17ms p(99.9)=216.03ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 47755
     http_req_receiving.............: avg=75.35µs  min=27.54µs med=71.18µs  max=2.69ms   p(90)=102.75µs p(95)=114.38µs p(99.9)=433.27µs
     http_req_sending...............: avg=24.87µs  min=5.13µs  med=14.02µs  max=118.36ms p(90)=19.24µs  p(95)=20.94µs  p(99.9)=508.37µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=125.38ms min=20.82ms med=123.62ms max=339.48ms p(90)=155.34ms p(95)=166.08ms p(99.9)=215.34ms
     http_reqs......................: 47755   390.3285/s
     iteration_duration.............: avg=125.94ms min=27.31ms med=124ms    max=351.09ms p(90)=155.68ms p(95)=166.46ms p(99.9)=218.39ms
     iterations.....................: 47655   389.511144/s
     success_rate...................: 100.00% ✓ 47655      ✗ 0    
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

     checks.........................: 100.00% ✓ 99417      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   326 kB/s
     http_req_blocked...............: avg=6.67µs   min=1.15µs  med=3.5µs    max=4.32ms   p(90)=4.96µs   p(95)=5.58µs   p(99.9)=1.18ms  
     http_req_connecting............: avg=2.86µs   min=0s      med=0s       max=4.27ms   p(90)=0s       p(95)=0s       p(99.9)=1.16ms  
     http_req_duration..............: avg=180.36ms min=22.02ms med=184.58ms max=388.39ms p(90)=193.28ms p(95)=197.98ms p(99.9)=262.03ms
       { expected_response:true }...: avg=180.36ms min=22.02ms med=184.58ms max=388.39ms p(90)=193.28ms p(95)=197.98ms p(99.9)=262.03ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33239
     http_req_receiving.............: avg=103.58µs min=35.98µs med=88.61µs  max=164.58ms p(90)=119µs    p(95)=130.89µs p(99.9)=591.06µs
     http_req_sending...............: avg=29.05µs  min=5.69µs  med=17.82µs  max=110.13ms p(90)=22.51µs  p(95)=24.43µs  p(99.9)=521.83µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=180.23ms min=21.89ms med=184.47ms max=388.31ms p(90)=193.15ms p(95)=197.87ms p(99.9)=261.32ms
     http_reqs......................: 33239   271.118821/s
     iteration_duration.............: avg=181.14ms min=43.07ms med=184.87ms max=396.5ms  p(90)=193.57ms p(95)=198.28ms p(99.9)=263.01ms
     iterations.....................: 33139   270.303156/s
     success_rate...................: 100.00% ✓ 33139      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 97545      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   321 kB/s
     http_req_blocked...............: avg=6.07µs   min=1.1µs   med=3.24µs   max=3.49ms   p(90)=4.69µs   p(95)=5.29µs   p(99.9)=1.24ms  
     http_req_connecting............: avg=2.63µs   min=0s      med=0s       max=3.45ms   p(90)=0s       p(95)=0s       p(99.9)=1.22ms  
     http_req_duration..............: avg=183.85ms min=17.05ms med=171.16ms max=742.25ms p(90)=213.29ms p(95)=236.13ms p(99.9)=678.97ms
       { expected_response:true }...: avg=183.85ms min=17.05ms med=171.16ms max=742.25ms p(90)=213.29ms p(95)=236.13ms p(99.9)=678.97ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32615
     http_req_receiving.............: avg=91.39µs  min=30.48µs med=87.38µs  max=12.03ms  p(90)=117.05µs p(95)=128.71µs p(99.9)=724.86µs
     http_req_sending...............: avg=22.57µs  min=4.99µs  med=17.41µs  max=33.92ms  p(90)=21.76µs  p(95)=23.52µs  p(99.9)=459.27µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.74ms min=16.92ms med=171.03ms max=742.16ms p(90)=213.18ms p(95)=236.04ms p(99.9)=678.87ms
     http_reqs......................: 32615   267.018384/s
     iteration_duration.............: avg=184.62ms min=76.65ms med=171.52ms max=742.47ms p(90)=213.6ms  p(95)=236.81ms p(99.9)=679.4ms 
     iterations.....................: 32515   266.199685/s
     success_rate...................: 100.00% ✓ 32515      ✗ 0    
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

