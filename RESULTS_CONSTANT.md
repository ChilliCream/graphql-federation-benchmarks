## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 5,079 | 5,107 | 5,046 | 0.5% | 379 MB | 76.4 KB |  |
| fusion-net-11 | 16.7.3 | 5,051 | 5,069 | 5,020 | 0.4% | 385 MB | 78.1 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,778 | 4,789 | 4,750 | 0.4% | 131 MB | 28.0 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,740 | 4,767 | 4,726 | 0.4% | 380 MB | 82.1 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,689 | 4,711 | 4,661 | 0.4% | 392 MB | 85.6 KB |  |
| fusion-aot-11 | 16.7.3 | 4,673 | 4,690 | 4,663 | 0.3% | 134 MB | 29.4 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,543 | 4,559 | 4,529 | 0.2% | 132 MB | 29.8 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,522 | 4,528 | 4,515 | 0.1% | 128 MB | 29.0 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,266 | 4,464 | 4,072 | 3.7% | 2,293 MB | 550.3 KB |  |
| hive-router | v0.3.6 | 2,911 | 2,912 | 2,885 | 0.4% | 92 MB | 32.3 KB |  |
| grafbase | 0.53.5 | 1,825 | 1,828 | 1,823 | 0.1% | 103 MB | 57.8 KB |  |
| cosmo | 0.363.0 | 1,451 | 1,457 | 1,447 | 0.3% | 163 MB | 114.8 KB |  |
| caliban | 3.2.0 | 1,420 | 1,421 | 1,418 | 0.1% | 4,342 MB | 3,131.4 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 536 | 538 | 535 | 0.2% | 2,743 MB | 5,241.3 KB |  |
| apollo-router | v2.19.0 | 527 | 527 | 526 | 0.1% | 173 MB | 336.9 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 401 | 405 | 399 | 0.8% | 191 MB | 488.3 KB |  |
| apollo-gateway | 2.14.4 | 275 | 276 | 274 | 0.3% | 2,154 MB | 8,022.1 KB |  |
| hive-gateway | 2.15.3 | 267 | 267 | 266 | 0.2% | 3,602 MB | 13,813.9 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1829994     ✗ 0     
     data_received..................: 53 GB   445 MB/s
     data_sent......................: 733 MB  6.1 MB/s
     http_req_blocked...............: avg=3.05µs  min=771ns    med=1.91µs  max=91.3ms   p(90)=2.98µs  p(95)=3.57µs   p(99.9)=25.65µs
     http_req_connecting............: avg=742ns   min=0s       med=0s      max=91.23ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.62ms  min=794.21µs med=8.82ms  max=264.75ms p(90)=14.76ms p(95)=17.46ms  p(99.9)=29.39ms
       { expected_response:true }...: avg=9.62ms  min=794.21µs med=8.82ms  max=264.75ms p(90)=14.76ms p(95)=17.46ms  p(99.9)=29.39ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 610098
     http_req_receiving.............: avg=89.25µs min=25.09µs  med=45.95µs max=172.12ms p(90)=87.71µs p(95)=189.22µs p(99.9)=5.42ms 
     http_req_sending...............: avg=40.92µs min=4.37µs   med=8.17µs  max=206.7ms  p(90)=14.33µs p(95)=99.2µs   p(99.9)=4.53ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.49ms  min=750.65µs med=8.72ms  max=243.77ms p(90)=14.56ms p(95)=17.22ms  p(99.9)=29ms   
     http_reqs......................: 610098  5079.765219/s
     iteration_duration.............: avg=9.82ms  min=1.23ms   med=9.01ms  max=318.77ms p(90)=14.97ms p(95)=17.68ms  p(99.9)=29.8ms 
     iterations.....................: 609998  5078.932605/s
     success_rate...................: 100.00% ✓ 609998      ✗ 0     
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

     checks.........................: 100.00% ✓ 1820097     ✗ 0     
     data_received..................: 53 GB   442 MB/s
     data_sent......................: 729 MB  6.1 MB/s
     http_req_blocked...............: avg=2.53µs  min=801ns    med=1.95µs max=5.83ms   p(90)=3.11µs  p(95)=3.75µs   p(99.9)=28.32µs
     http_req_connecting............: avg=156ns   min=0s       med=0s     max=4ms      p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.68ms  min=839.01µs med=8.86ms max=281.44ms p(90)=14.92ms p(95)=17.7ms   p(99.9)=29.32ms
       { expected_response:true }...: avg=9.68ms  min=839.01µs med=8.86ms max=281.44ms p(90)=14.92ms p(95)=17.7ms   p(99.9)=29.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 606799
     http_req_receiving.............: avg=92.6µs  min=24.07µs  med=45.3µs max=215.39ms p(90)=89.28µs p(95)=190.18µs p(99.9)=6.12ms 
     http_req_sending...............: avg=41.39µs min=4.32µs   med=8.18µs max=29.7ms   p(90)=14.76µs p(95)=100.67µs p(99.9)=4.68ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.54ms  min=782.59µs med=8.75ms max=280.82ms p(90)=14.7ms  p(95)=17.45ms  p(99.9)=28.85ms
     http_reqs......................: 606799  5051.709729/s
     iteration_duration.............: avg=9.88ms  min=969.14µs med=9.05ms max=291.09ms p(90)=15.12ms p(95)=17.91ms  p(99.9)=29.64ms
     iterations.....................: 606699  5050.877211/s
     success_rate...................: 100.00% ✓ 606699      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1721646     ✗ 0     
     data_received..................: 50 GB   418 MB/s
     data_sent......................: 690 MB  5.7 MB/s
     http_req_blocked...............: avg=2.89µs  min=932ns    med=2.31µs  max=6.58ms   p(90)=3.58µs  p(95)=4.18µs   p(99.9)=31.79µs
     http_req_connecting............: avg=158ns   min=0s       med=0s      max=3.48ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.25ms min=909.7µs  med=9.54ms  max=313.66ms p(90)=15.33ms p(95)=18.02ms  p(99.9)=29.7ms 
       { expected_response:true }...: avg=10.25ms min=909.7µs  med=9.54ms  max=313.66ms p(90)=15.33ms p(95)=18.02ms  p(99.9)=29.7ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 573982
     http_req_receiving.............: avg=92.7µs  min=24.41µs  med=45.85µs max=31.34ms  p(90)=92.55µs p(95)=209.73µs p(99.9)=5.7ms  
     http_req_sending...............: avg=40.7µs  min=4.55µs   med=8.44µs  max=159.58ms p(90)=15.07µs p(95)=107.34µs p(99.9)=4.05ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.12ms min=850.87µs med=9.42ms  max=313.05ms p(90)=15.13ms p(95)=17.77ms  p(99.9)=29.16ms
     http_reqs......................: 573982  4778.225178/s
     iteration_duration.............: avg=10.44ms min=1.36ms   med=9.72ms  max=354.46ms p(90)=15.54ms p(95)=18.23ms  p(99.9)=29.96ms
     iterations.....................: 573882  4777.392709/s
     success_rate...................: 100.00% ✓ 573882      ✗ 0     
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

     checks.........................: 100.00% ✓ 1708326     ✗ 0     
     data_received..................: 50 GB   415 MB/s
     data_sent......................: 685 MB  5.7 MB/s
     http_req_blocked...............: avg=3.14µs  min=932ns    med=2.48µs  max=8.3ms    p(90)=3.82µs  p(95)=4.54µs   p(99.9)=35.06µs
     http_req_connecting............: avg=155ns   min=0s       med=0s      max=3.35ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.31ms min=992.46µs med=9.47ms  max=290.64ms p(90)=15.82ms p(95)=18.67ms  p(99.9)=31.87ms
       { expected_response:true }...: avg=10.31ms min=992.46µs med=9.47ms  max=290.64ms p(90)=15.82ms p(95)=18.67ms  p(99.9)=31.87ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 569542
     http_req_receiving.............: avg=104.9µs min=25.4µs   med=49.08µs max=88.95ms  p(90)=99.35µs p(95)=210.39µs p(99.9)=6.94ms 
     http_req_sending...............: avg=45.1µs  min=4.36µs   med=8.95µs  max=46.94ms  p(90)=16.61µs p(95)=108.7µs  p(99.9)=4.88ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.16ms min=913.96µs med=9.35ms  max=280.58ms p(90)=15.59ms p(95)=18.38ms  p(99.9)=31.43ms
     http_reqs......................: 569542  4740.946937/s
     iteration_duration.............: avg=10.52ms min=1.27ms   med=9.67ms  max=300.71ms p(90)=16.04ms p(95)=18.89ms  p(99.9)=32.22ms
     iterations.....................: 569442  4740.114524/s
     success_rate...................: 100.00% ✓ 569442      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1689768     ✗ 0     
     data_received..................: 49 GB   410 MB/s
     data_sent......................: 677 MB  5.6 MB/s
     http_req_blocked...............: avg=2.52µs  min=771ns    med=1.91µs  max=7.04ms   p(90)=3.14µs  p(95)=3.87µs   p(99.9)=28.12µs
     http_req_connecting............: avg=151ns   min=0s       med=0s      max=3.38ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.44ms min=978.11µs med=9.73ms  max=287.79ms p(90)=15.64ms p(95)=18.18ms  p(99.9)=30.66ms
       { expected_response:true }...: avg=10.44ms min=978.11µs med=9.73ms  max=287.79ms p(90)=15.64ms p(95)=18.18ms  p(99.9)=30.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 563356
     http_req_receiving.............: avg=95.11µs min=25.58µs  med=47.98µs max=41.07ms  p(90)=96.65µs p(95)=199.78µs p(99.9)=5.8ms  
     http_req_sending...............: avg=41.62µs min=4.25µs   med=8.14µs  max=125.15ms p(90)=15.62µs p(95)=102.03µs p(99.9)=4.3ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.3ms  min=897.66µs med=9.61ms  max=287.24ms p(90)=15.44ms p(95)=17.94ms  p(99.9)=30.21ms
     http_reqs......................: 563356  4689.586037/s
     iteration_duration.............: avg=10.64ms min=1.3ms    med=9.92ms  max=303.41ms p(90)=15.84ms p(95)=18.39ms  p(99.9)=30.93ms
     iterations.....................: 563256  4688.753599/s
     success_rate...................: 100.00% ✓ 563256      ✗ 0     
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

     checks.........................: 100.00% ✓ 1683945     ✗ 0     
     data_received..................: 49 GB   409 MB/s
     data_sent......................: 675 MB  5.6 MB/s
     http_req_blocked...............: avg=2.87µs  min=902ns    med=2.35µs  max=5.64ms   p(90)=3.62µs  p(95)=4.27µs   p(99.9)=28.96µs
     http_req_connecting............: avg=117ns   min=0s       med=0s      max=2.63ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.48ms min=937.4µs  med=9.74ms  max=293.95ms p(90)=15.72ms p(95)=18.53ms  p(99.9)=30.55ms
       { expected_response:true }...: avg=10.48ms min=937.4µs  med=9.74ms  max=293.95ms p(90)=15.72ms p(95)=18.53ms  p(99.9)=30.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 561415
     http_req_receiving.............: avg=99.13µs min=25.76µs  med=48.78µs max=137.53ms p(90)=95.33µs p(95)=217.3µs  p(99.9)=6.07ms 
     http_req_sending...............: avg=42.43µs min=4.57µs   med=8.61µs  max=114.15ms p(90)=15.21µs p(95)=109.17µs p(99.9)=4.39ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.33ms min=856.04µs med=9.62ms  max=272.7ms  p(90)=15.5ms  p(95)=18.28ms  p(99.9)=30.13ms
     http_reqs......................: 561415  4673.50869/s
     iteration_duration.............: avg=10.68ms min=1.46ms   med=9.93ms  max=304.37ms p(90)=15.93ms p(95)=18.75ms  p(99.9)=30.85ms
     iterations.....................: 561315  4672.676238/s
     success_rate...................: 100.00% ✓ 561315      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1637286     ✗ 0     
     data_received..................: 48 GB   398 MB/s
     data_sent......................: 656 MB  5.5 MB/s
     http_req_blocked...............: avg=3.37µs  min=831ns    med=2.31µs  max=85.67ms  p(90)=3.65µs  p(95)=4.36µs   p(99.9)=34.75µs
     http_req_connecting............: avg=580ns   min=0s       med=0s      max=84.78ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.78ms min=1.06ms   med=10.15ms max=266.11ms p(90)=15.82ms p(95)=18.41ms  p(99.9)=30.63ms
       { expected_response:true }...: avg=10.78ms min=1.06ms   med=10.15ms max=266.11ms p(90)=15.82ms p(95)=18.41ms  p(99.9)=30.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 545862
     http_req_receiving.............: avg=96.13µs min=25.59µs  med=47.89µs max=159.8ms  p(90)=98.18µs p(95)=211.18µs p(99.9)=5.56ms 
     http_req_sending...............: avg=42.76µs min=4.49µs   med=8.74µs  max=154.49ms p(90)=16.25µs p(95)=106.77µs p(99.9)=4.41ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.64ms min=981.02µs med=10.04ms max=261.75ms p(90)=15.62ms p(95)=18.16ms  p(99.9)=30.27ms
     http_reqs......................: 545862  4543.674243/s
     iteration_duration.............: avg=10.98ms min=1.24ms   med=10.35ms max=279.26ms p(90)=16.03ms p(95)=18.64ms  p(99.9)=30.93ms
     iterations.....................: 545762  4542.841858/s
     success_rate...................: 100.00% ✓ 545762      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1629873     ✗ 0     
     data_received..................: 48 GB   396 MB/s
     data_sent......................: 653 MB  5.4 MB/s
     http_req_blocked...............: avg=2.5µs   min=761ns    med=1.94µs  max=5.64ms   p(90)=3.1µs   p(95)=3.74µs   p(99.9)=25.5µs 
     http_req_connecting............: avg=164ns   min=0s       med=0s      max=3.84ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.83ms min=1.01ms   med=10.29ms max=272.67ms p(90)=15.64ms p(95)=17.93ms  p(99.9)=29.41ms
       { expected_response:true }...: avg=10.83ms min=1.01ms   med=10.29ms max=272.67ms p(90)=15.64ms p(95)=17.93ms  p(99.9)=29.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 543391
     http_req_receiving.............: avg=92.53µs min=24.02µs  med=45.82µs max=126.86ms p(90)=92.75µs p(95)=202.78µs p(99.9)=5.53ms 
     http_req_sending...............: avg=39.88µs min=4.21µs   med=8.1µs   max=137.42ms p(90)=14.89µs p(95)=101.39µs p(99.9)=3.86ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.7ms  min=964.39µs med=10.18ms max=272.34ms p(90)=15.44ms p(95)=17.7ms   p(99.9)=29.06ms
     http_reqs......................: 543391  4522.998823/s
     iteration_duration.............: avg=11.03ms min=1.67ms   med=10.47ms max=295.51ms p(90)=15.84ms p(95)=18.14ms  p(99.9)=29.65ms
     iterations.....................: 543291  4522.166457/s
     success_rate...................: 100.00% ✓ 543291      ✗ 0     
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

     checks.........................: 100.00% ✓ 1537263     ✗ 0     
     data_received..................: 45 GB   373 MB/s
     data_sent......................: 616 MB  5.1 MB/s
     http_req_blocked...............: avg=3.1µs   min=972ns    med=2.51µs  max=5.02ms   p(90)=3.83µs  p(95)=4.48µs   p(99.9)=35.36µs
     http_req_connecting............: avg=191ns   min=0s       med=0s      max=4.08ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.5ms  min=742.4µs  med=11.28ms max=278.69ms p(90)=17.55ms p(95)=19.84ms  p(99.9)=31ms   
       { expected_response:true }...: avg=11.5ms  min=742.4µs  med=11.28ms max=278.69ms p(90)=17.55ms p(95)=19.84ms  p(99.9)=31ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 512521
     http_req_receiving.............: avg=91.07µs min=26.27µs  med=49.71µs max=179ms    p(90)=98.08µs p(95)=219.78µs p(99.9)=4.59ms 
     http_req_sending...............: avg=41.25µs min=4.65µs   med=9.12µs  max=80.2ms   p(90)=15.94µs p(95)=117.3µs  p(99.9)=3.52ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.37ms min=671.62µs med=11.16ms max=278.34ms p(90)=17.37ms p(95)=19.63ms  p(99.9)=30.7ms 
     http_reqs......................: 512521  4266.94733/s
     iteration_duration.............: avg=11.69ms min=1.25ms   med=11.47ms max=291.74ms p(90)=17.75ms p(95)=20.05ms  p(99.9)=31.26ms
     iterations.....................: 512421  4266.114789/s
     success_rate...................: 100.00% ✓ 512421      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1049589     ✗ 0     
     data_received..................: 31 GB   255 MB/s
     data_sent......................: 421 MB  3.5 MB/s
     http_req_blocked...............: avg=2.63µs  min=872ns   med=2.08µs  max=3.99ms   p(90)=3.36µs  p(95)=4.01µs   p(99.9)=27.63µs
     http_req_connecting............: avg=252ns   min=0s      med=0s      max=3.95ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.95ms min=1.34ms  med=17.02ms max=285.68ms p(90)=22.86ms p(95)=24.41ms  p(99.9)=31.56ms
       { expected_response:true }...: avg=16.95ms min=1.34ms  med=17.02ms max=285.68ms p(90)=22.86ms p(95)=24.41ms  p(99.9)=31.56ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 349963
     http_req_receiving.............: avg=69.91µs min=25.09µs med=52.32µs max=134.14ms p(90)=87.59µs p(95)=130.26µs p(99.9)=1.1ms  
     http_req_sending...............: avg=30.46µs min=4.64µs  med=9.35µs  max=174.57ms p(90)=15.76µs p(95)=91.69µs  p(99.9)=1.16ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.85ms min=1.27ms  med=16.92ms max=269.02ms p(90)=22.75ms p(95)=24.31ms  p(99.9)=31.41ms
     http_reqs......................: 349963  2911.916067/s
     iteration_duration.............: avg=17.14ms min=3.15ms  med=17.2ms  max=295.33ms p(90)=23.04ms p(95)=24.6ms   p(99.9)=31.78ms
     iterations.....................: 349863  2911.084003/s
     success_rate...................: 100.00% ✓ 349863      ✗ 0     
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

     checks.........................: 100.00% ✓ 658143      ✗ 0     
     data_received..................: 19 GB   160 MB/s
     data_sent......................: 264 MB  2.2 MB/s
     http_req_blocked...............: avg=4.19µs  min=1.05µs  med=3.13µs  max=4.3ms    p(90)=5.32µs   p(95)=6.38µs  p(99.9)=43.5µs 
     http_req_connecting............: avg=563ns   min=0s      med=0s      max=4.28ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=27.09ms min=1.8ms   med=26.45ms max=283.47ms p(90)=35.01ms  p(95)=37.83ms p(99.9)=51.91ms
       { expected_response:true }...: avg=27.09ms min=1.8ms   med=26.45ms max=283.47ms p(90)=35.01ms  p(95)=37.83ms p(99.9)=51.91ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 219481
     http_req_receiving.............: avg=91.44µs min=27.81µs med=65.14µs max=242.31ms p(90)=122.85µs p(95)=183.5µs p(99.9)=1.39ms 
     http_req_sending...............: avg=35.09µs min=4.84µs  med=11.82µs max=122.63ms p(90)=23.06µs  p(95)=101.5µs p(99.9)=1.51ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=26.97ms min=1.75ms  med=26.33ms max=267.18ms p(90)=34.88ms  p(95)=37.7ms  p(99.9)=51.78ms
     http_reqs......................: 219481  1825.184822/s
     iteration_duration.............: avg=27.33ms min=8.09ms  med=26.67ms max=305.02ms p(90)=35.24ms  p(95)=38.05ms p(99.9)=52.21ms
     iterations.....................: 219381  1824.353231/s
     success_rate...................: 100.00% ✓ 219381      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 523278      ✗ 0     
     data_received..................: 15 GB   127 MB/s
     data_sent......................: 210 MB  1.7 MB/s
     http_req_blocked...............: avg=3.22µs  min=982ns   med=2.41µs  max=3.9ms    p(90)=3.9µs   p(95)=4.55µs   p(99.9)=33.85µs 
     http_req_connecting............: avg=523ns   min=0s      med=0s      max=3.85ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.17ms min=2.03ms  med=33.29ms max=270.48ms p(90)=49.53ms p(95)=54.6ms   p(99.9)=78.2ms  
       { expected_response:true }...: avg=34.17ms min=2.03ms  med=33.29ms max=270.48ms p(90)=49.53ms p(95)=54.6ms   p(99.9)=78.2ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 174526
     http_req_receiving.............: avg=72.54µs min=27.47µs med=62.28µs max=52.23ms  p(90)=99.17µs p(95)=115.21µs p(99.9)=673µs   
     http_req_sending...............: avg=22.62µs min=4.63µs  med=10.76µs max=144.83ms p(90)=16.91µs p(95)=20.54µs  p(99.9)=746.35µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.07ms min=1.96ms  med=33.2ms  max=269.94ms p(90)=49.44ms p(95)=54.5ms   p(99.9)=77.94ms 
     http_reqs......................: 174526  1451.069826/s
     iteration_duration.............: avg=34.39ms min=4.13ms  med=33.49ms max=296.14ms p(90)=49.72ms p(95)=54.8ms   p(99.9)=78.81ms 
     iterations.....................: 174426  1450.238391/s
     success_rate...................: 100.00% ✓ 174426      ✗ 0     
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

     checks.........................: 100.00% ✓ 512334      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 205 MB  1.7 MB/s
     http_req_blocked...............: avg=4.52µs  min=1.09µs  med=2.82µs  max=9.13ms   p(90)=4.39µs  p(95)=5.1µs    p(99.9)=33.42µs 
     http_req_connecting............: avg=1.37µs  min=0s      med=0s      max=9.05ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.88ms min=2.26ms  med=33.9ms  max=286.46ms p(90)=49.71ms p(95)=55.04ms  p(99.9)=82.44ms 
       { expected_response:true }...: avg=34.88ms min=2.26ms  med=33.9ms  max=286.46ms p(90)=49.71ms p(95)=55.04ms  p(99.9)=82.44ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 170878
     http_req_receiving.............: avg=76.3µs  min=28.75µs med=62.36µs max=212.22ms p(90)=97.5µs  p(95)=112.49µs p(99.9)=822.76µs
     http_req_sending...............: avg=20.92µs min=5.11µs  med=12.14µs max=54.9ms   p(90)=18.14µs p(95)=21.71µs  p(99.9)=768.62µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.78ms min=2.16ms  med=33.81ms max=285.53ms p(90)=49.62ms p(95)=54.95ms  p(99.9)=82.17ms 
     http_reqs......................: 170878  1420.624828/s
     iteration_duration.............: avg=35.12ms min=5.92ms  med=34.12ms max=309.95ms p(90)=49.93ms p(95)=55.26ms  p(99.9)=82.97ms 
     iterations.....................: 170778  1419.79346/s
     success_rate...................: 100.00% ✓ 170778      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 193668     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   644 kB/s
     http_req_blocked...............: avg=4.18µs  min=1µs     med=2.58µs  max=3.86ms   p(90)=3.94µs   p(95)=4.51µs   p(99.9)=46.48µs 
     http_req_connecting............: avg=1.38µs  min=0s      med=0s      max=3.82ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.58ms min=3.93ms  med=89.88ms max=329.93ms p(90)=111.99ms p(95)=122.7ms  p(99.9)=222.2ms 
       { expected_response:true }...: avg=92.58ms min=3.93ms  med=89.88ms max=329.93ms p(90)=111.99ms p(95)=122.7ms  p(99.9)=222.2ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 64656
     http_req_receiving.............: avg=75.7µs  min=28.08µs med=69.02µs max=7.83ms   p(90)=103.77µs p(95)=116.37µs p(99.9)=542.16µs
     http_req_sending...............: avg=21.58µs min=4.91µs  med=12.65µs max=129.26ms p(90)=18.67µs  p(95)=20.57µs  p(99.9)=547.63µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.48ms min=3.86ms  med=89.79ms max=329.27ms p(90)=111.89ms p(95)=122.59ms p(99.9)=222.12ms
     http_reqs......................: 64656   536.273594/s
     iteration_duration.............: avg=92.96ms min=22.33ms med=90.11ms max=348.06ms p(90)=112.25ms p(95)=122.99ms p(99.9)=225.14ms
     iterations.....................: 64556   535.444168/s
     success_rate...................: 100.00% ✓ 64556      ✗ 0    
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

     checks.........................: 100.00% ✓ 190398     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 76 MB   633 kB/s
     http_req_blocked...............: avg=7.46µs  min=1.07µs  med=2.82µs  max=10.33ms  p(90)=4.28µs   p(95)=4.85µs   p(99.9)=51.55µs 
     http_req_connecting............: avg=4.38µs  min=0s      med=0s      max=10.29ms  p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=94.17ms min=4.44ms  med=92.17ms max=294.99ms p(90)=127.1ms  p(95)=137.33ms p(99.9)=180.58ms
       { expected_response:true }...: avg=94.17ms min=4.44ms  med=92.17ms max=294.99ms p(90)=127.1ms  p(95)=137.33ms p(99.9)=180.58ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63566
     http_req_receiving.............: avg=76.67µs min=26.4µs  med=70.73µs max=97.82ms  p(90)=101.33µs p(95)=114.07µs p(99.9)=543.25µs
     http_req_sending...............: avg=25.88µs min=4.76µs  med=14.01µs max=177.46ms p(90)=19.26µs  p(95)=21.08µs  p(99.9)=592.82µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.06ms min=4.37ms  med=92.08ms max=293.84ms p(90)=126.99ms p(95)=137.23ms p(99.9)=180.11ms
     http_reqs......................: 63566   527.192289/s
     iteration_duration.............: avg=94.55ms min=24.78ms med=92.44ms max=324.98ms p(90)=127.35ms p(95)=137.6ms  p(99.9)=181.44ms
     iterations.....................: 63466   526.362927/s
     success_rate...................: 100.00% ✓ 63466      ✗ 0    
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

     checks.........................: 100.00% ✓ 145143     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   482 kB/s
     http_req_blocked...............: avg=5.45µs   min=1.25µs  med=3.32µs   max=4.39ms   p(90)=4.68µs   p(95)=5.25µs   p(99.9)=354.04µs
     http_req_connecting............: avg=1.91µs   min=0s      med=0s       max=4.36ms   p(90)=0s       p(95)=0s       p(99.9)=265.27µs
     http_req_duration..............: avg=123.55ms min=5.28ms  med=121.02ms max=310ms    p(90)=162.32ms p(95)=174.8ms  p(99.9)=222.15ms
       { expected_response:true }...: avg=123.55ms min=5.28ms  med=121.02ms max=310ms    p(90)=162.32ms p(95)=174.8ms  p(99.9)=222.15ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48481
     http_req_receiving.............: avg=80.23µs  min=30.58µs med=76.24µs  max=42.23ms  p(90)=104.85µs p(95)=116.02µs p(99.9)=489.24µs
     http_req_sending...............: avg=24.47µs  min=5.38µs  med=15.54µs  max=90.94ms  p(90)=20.31µs  p(95)=22.14µs  p(99.9)=566.88µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=123.45ms min=5.21ms  med=120.93ms max=309.44ms p(90)=162.21ms p(95)=174.7ms  p(99.9)=222.05ms
     http_reqs......................: 48481   401.698879/s
     iteration_duration.............: avg=124.05ms min=28.89ms med=121.33ms max=338.43ms p(90)=162.65ms p(95)=175.07ms p(99.9)=225.78ms
     iterations.....................: 48381   400.87031/s
     success_rate...................: 100.00% ✓ 48381      ✗ 0    
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

     checks.........................: 100.00% ✓ 99693      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   331 kB/s
     http_req_blocked...............: avg=11.23µs  min=1.1µs   med=3.19µs   max=9.1ms    p(90)=4.49µs   p(95)=5.04µs   p(99.9)=3.68ms  
     http_req_connecting............: avg=7.54µs   min=0s      med=0s       max=9.02ms   p(90)=0s       p(95)=0s       p(99.9)=3.44ms  
     http_req_duration..............: avg=179.82ms min=7.46ms  med=180.83ms max=389.47ms p(90)=189.04ms p(95)=193.12ms p(99.9)=272.15ms
       { expected_response:true }...: avg=179.82ms min=7.46ms  med=180.83ms max=389.47ms p(90)=189.04ms p(95)=193.12ms p(99.9)=272.15ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33331
     http_req_receiving.............: avg=90.18µs  min=30.56µs med=84.35µs  max=116.48ms p(90)=112.92µs p(95)=123.49µs p(99.9)=557.5µs 
     http_req_sending...............: avg=28.23µs  min=5.1µs   med=16.47µs  max=73.9ms   p(90)=20.61µs  p(95)=22.5µs   p(99.9)=912µs   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=179.7ms  min=7.39ms  med=180.74ms max=379.23ms p(90)=188.94ms p(95)=193ms    p(99.9)=270.67ms
     http_reqs......................: 33331   275.608362/s
     iteration_duration.............: avg=180.64ms min=51.05ms med=181.15ms max=402.01ms p(90)=189.31ms p(95)=193.38ms p(99.9)=277.14ms
     iterations.....................: 33231   274.781479/s
     success_rate...................: 100.00% ✓ 33231      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 96648      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   321 kB/s
     http_req_blocked...............: avg=11.27µs  min=1.26µs  med=3.45µs   max=9.38ms   p(90)=4.84µs   p(95)=5.45µs   p(99.9)=3.8ms   
     http_req_connecting............: avg=7.16µs   min=0s      med=0s       max=9.26ms   p(90)=0s       p(95)=0s       p(99.9)=3.53ms  
     http_req_duration..............: avg=185.55ms min=6.1ms   med=168.49ms max=828.59ms p(90)=215.74ms p(95)=250.41ms p(99.9)=687.86ms
       { expected_response:true }...: avg=185.55ms min=6.1ms   med=168.49ms max=828.59ms p(90)=215.74ms p(95)=250.41ms p(99.9)=687.86ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32316
     http_req_receiving.............: avg=92.57µs  min=34.83µs med=86.24µs  max=60.45ms  p(90)=115.39µs p(95)=126.69µs p(99.9)=618.53µs
     http_req_sending...............: avg=23.17µs  min=5.89µs  med=17.29µs  max=40.58ms  p(90)=21.78µs  p(95)=23.47µs  p(99.9)=652.12µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=185.43ms min=5.94ms  med=168.38ms max=828.49ms p(90)=215.62ms p(95)=250.29ms p(99.9)=687.77ms
     http_reqs......................: 32316   267.041213/s
     iteration_duration.............: avg=186.37ms min=44.86ms med=168.86ms max=828.83ms p(90)=216.1ms  p(95)=251.25ms p(99.9)=688.49ms
     iterations.....................: 32216   266.214869/s
     success_rate...................: 100.00% ✓ 32216      ✗ 0    
     vus............................: 7       min=7        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

