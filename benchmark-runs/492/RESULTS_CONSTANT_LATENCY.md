## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-aot-11 | 16.7.6 | 3,617 | 3,627 | 3,592 | 0.4% | 119 MB | 33.6 KB |  |
| fusion-net-11 | 16.7.6 | 3,600 | 3,616 | 3,589 | 0.3% | 366 MB | 104.1 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.17 | 3,581 | 3,599 | 3,564 | 0.4% | 112 MB | 31.9 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.17 | 3,572 | 3,595 | 3,560 | 0.4% | 365 MB | 104.6 KB |  |
| fusion-fed-aot-11 | 16.7.6 | 3,548 | 3,551 | 3,536 | 0.2% | 118 MB | 34.0 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.17 | 3,542 | 3,559 | 3,521 | 0.5% | 117 MB | 33.8 KB |  |
| fusion-fed-net-11 | 16.7.6 | 3,539 | 3,545 | 3,526 | 0.2% | 373 MB | 108.0 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.17 | 3,524 | 3,534 | 3,517 | 0.2% | 366 MB | 106.4 KB |  |
| feddi-gateway | 2026-11-03-0517 | 3,446 | 3,464 | 3,433 | 0.4% | 2,298 MB | 682.8 KB |  |
| hive-router-nightly | v0.3.19-nightly.9815b25d | 3,384 | 3,399 | 3,378 | 0.2% | 93 MB | 28.1 KB |  |
| hive-router | v0.3.17 | 3,333 | 3,359 | 3,323 | 0.4% | 103 MB | 31.5 KB |  |
| caliban | 3.2.1 | 1,527 | 1,528 | 1,526 | 0.0% | 5,984 MB | 4,012.9 KB |  |
| grafbase | 0.53.5 | 1,452 | 1,460 | 1,447 | 0.4% | 99 MB | 69.6 KB |  |
| cosmo | 0.373.0 | 1,401 | 1,413 | 1,396 | 0.6% | 152 MB | 111.1 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 582 | 584 | 580 | 0.3% | 2,614 MB | 4,599.5 KB |  |
| apollo-router | v2.19.1 | 534 | 535 | 533 | 0.2% | 178 MB | 341.9 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.b787dc86 | 514 | 515 | 514 | 0.1% | 196 MB | 390.8 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 387 | 393 | 385 | 0.8% | 202 MB | 535.0 KB |  |
| hive-gateway | 2.15.10 | 293 | 293 | 292 | 0.2% | 3,206 MB | 11,204.6 KB |  |
| apollo-gateway | 2.14.4 | 267 | 267 | 266 | 0.2% | 2,137 MB | 8,196.5 KB |  |


### Details

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1312218     ✗ 0     
     data_received..................: 38 GB   317 MB/s
     data_sent......................: 526 MB  4.3 MB/s
     http_req_blocked...............: avg=2.45µs  min=802ns   med=1.86µs  max=4.07ms   p(90)=3.05µs  p(95)=3.75µs   p(99.9)=24.42µs
     http_req_connecting............: avg=238ns   min=0s      med=0s      max=4.01ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.51ms min=8.1ms   med=13.1ms  max=279.05ms p(90)=16.51ms p(95)=17.74ms  p(99.9)=25.25ms
       { expected_response:true }...: avg=13.51ms min=8.1ms   med=13.1ms  max=279.05ms p(90)=16.51ms p(95)=17.74ms  p(99.9)=25.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 437506
     http_req_receiving.............: avg=68.97µs min=25.15µs med=44.58µs max=181.18ms p(90)=90.29µs p(95)=168.19µs p(99.9)=1.68ms 
     http_req_sending...............: avg=30.8µs  min=4.24µs  med=7.92µs  max=148.54ms p(90)=15.68µs p(95)=92.52µs  p(99.9)=1.66ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.41ms min=8.03ms  med=13.01ms max=277.75ms p(90)=16.41ms p(95)=17.62ms  p(99.9)=25.01ms
     http_reqs......................: 437506  3617.066869/s
     iteration_duration.............: avg=13.7ms  min=8.27ms  med=13.29ms max=296.78ms p(90)=16.7ms  p(95)=17.93ms  p(99.9)=25.48ms
     iterations.....................: 437406  3616.240122/s
     success_rate...................: 100.00% ✓ 437406      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1306335     ✗ 0     
     data_received..................: 38 GB   315 MB/s
     data_sent......................: 523 MB  4.3 MB/s
     http_req_blocked...............: avg=2.82µs  min=902ns   med=2.23µs  max=3.8ms    p(90)=3.56µs   p(95)=4.3µs    p(99.9)=31.94µs
     http_req_connecting............: avg=204ns   min=0s      med=0s      max=3.5ms    p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.57ms min=8.17ms  med=13.1ms  max=274.1ms  p(90)=16.78ms  p(95)=18.14ms  p(99.9)=25.9ms 
       { expected_response:true }...: avg=13.57ms min=8.17ms  med=13.1ms  max=274.1ms  p(90)=16.78ms  p(95)=18.14ms  p(99.9)=25.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 435545
     http_req_receiving.............: avg=75.46µs min=25.54µs med=47.24µs max=110.39ms p(90)=100.62µs p(95)=192.86µs p(99.9)=1.88ms 
     http_req_sending...............: avg=33.83µs min=4.41µs  med=8.45µs  max=122.59ms p(90)=17.4µs   p(95)=103.97µs p(99.9)=1.86ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.46ms min=8.11ms  med=13ms    max=242.51ms p(90)=16.66ms  p(95)=18.01ms  p(99.9)=25.66ms
     http_reqs......................: 435545  3600.986008/s
     iteration_duration.............: avg=13.77ms min=8.36ms  med=13.3ms  max=291.96ms p(90)=16.98ms  p(95)=18.34ms  p(99.9)=26.11ms
     iterations.....................: 435445  3600.15923/s
     success_rate...................: 100.00% ✓ 435445      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1299171     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 521 MB  4.3 MB/s
     http_req_blocked...............: avg=2.34µs  min=792ns   med=1.81µs  max=3.58ms   p(90)=2.87µs  p(95)=3.48µs  p(99.9)=24.71µs
     http_req_connecting............: avg=212ns   min=0s      med=0s      max=3.53ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.65ms min=8.25ms  med=13.25ms max=281.04ms p(90)=16.72ms p(95)=17.96ms p(99.9)=25.25ms
       { expected_response:true }...: avg=13.65ms min=8.25ms  med=13.25ms max=281.04ms p(90)=16.72ms p(95)=17.96ms p(99.9)=25.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 433157
     http_req_receiving.............: avg=68.26µs min=23.31µs med=43.89µs max=141.73ms p(90)=89µs    p(95)=173.4µs p(99.9)=1.73ms 
     http_req_sending...............: avg=30.43µs min=4.24µs  med=7.78µs  max=199.92ms p(90)=15.04µs p(95)=92.22µs p(99.9)=1.61ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.56ms min=8.16ms  med=13.15ms max=271.99ms p(90)=16.61ms p(95)=17.84ms p(99.9)=24.98ms
     http_reqs......................: 433157  3581.079502/s
     iteration_duration.............: avg=13.84ms min=8.44ms  med=13.44ms max=292.84ms p(90)=16.91ms p(95)=18.15ms p(99.9)=25.46ms
     iterations.....................: 433057  3580.252763/s
     success_rate...................: 100.00% ✓ 433057      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1295997     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 519 MB  4.3 MB/s
     http_req_blocked...............: avg=2.84µs  min=811ns   med=1.92µs  max=7.73ms   p(90)=3.25µs  p(95)=4.09µs  p(99.9)=29.7µs 
     http_req_connecting............: avg=528ns   min=0s      med=0s      max=7.69ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.68ms min=8.21ms  med=13.25ms max=282.33ms p(90)=16.86ms p(95)=18.14ms p(99.9)=25.71ms
       { expected_response:true }...: avg=13.68ms min=8.21ms  med=13.25ms max=282.33ms p(90)=16.86ms p(95)=18.14ms p(99.9)=25.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 432099
     http_req_receiving.............: avg=70.59µs min=24.37µs med=43.84µs max=143.1ms  p(90)=95.48µs p(95)=176.9µs p(99.9)=1.9ms  
     http_req_sending...............: avg=31.9µs  min=4.48µs  med=8.09µs  max=57.77ms  p(90)=17.54µs p(95)=96.36µs p(99.9)=1.85ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.57ms min=8.17ms  med=13.15ms max=280.71ms p(90)=16.74ms p(95)=18.02ms p(99.9)=25.48ms
     http_reqs......................: 432099  3572.581473/s
     iteration_duration.............: avg=13.88ms min=8.38ms  med=13.44ms max=292.68ms p(90)=17.05ms p(95)=18.34ms p(99.9)=25.93ms
     iterations.....................: 431999  3571.754676/s
     success_rate...................: 100.00% ✓ 431999      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1287189     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 516 MB  4.3 MB/s
     http_req_blocked...............: avg=2.38µs  min=792ns   med=1.85µs  max=4.37ms   p(90)=2.97µs  p(95)=3.62µs   p(99.9)=23.52µs
     http_req_connecting............: avg=216ns   min=0s      med=0s      max=4.32ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.78ms min=8.17ms  med=13.38ms max=314.77ms p(90)=16.86ms p(95)=18.08ms  p(99.9)=25.56ms
       { expected_response:true }...: avg=13.78ms min=8.17ms  med=13.38ms max=314.77ms p(90)=16.86ms p(95)=18.08ms  p(99.9)=25.56ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429163
     http_req_receiving.............: avg=69.23µs min=23.89µs med=45.11µs max=96.68ms  p(90)=91.49µs p(95)=172.66µs p(99.9)=1.62ms 
     http_req_sending...............: avg=31.99µs min=4.14µs  med=7.91µs  max=194ms    p(90)=15.31µs p(95)=93.43µs  p(99.9)=1.7ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.68ms min=8.12ms  med=13.29ms max=306.07ms p(90)=16.75ms p(95)=17.97ms  p(99.9)=25.3ms 
     http_reqs......................: 429163  3548.003133/s
     iteration_duration.............: avg=13.97ms min=8.32ms  med=13.57ms max=324.23ms p(90)=17.05ms p(95)=18.27ms  p(99.9)=25.79ms
     iterations.....................: 429063  3547.176407/s
     success_rate...................: 100.00% ✓ 429063      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1285317     ✗ 0     
     data_received..................: 38 GB   310 MB/s
     data_sent......................: 515 MB  4.3 MB/s
     http_req_blocked...............: avg=2.99µs  min=881ns   med=2.35µs  max=4.19ms   p(90)=3.85µs   p(95)=4.71µs   p(99.9)=34.09µs
     http_req_connecting............: avg=238ns   min=0s      med=0s      max=4.16ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.79ms min=8.15ms  med=13.33ms max=274.44ms p(90)=17ms     p(95)=18.33ms  p(99.9)=26.18ms
       { expected_response:true }...: avg=13.79ms min=8.15ms  med=13.33ms max=274.44ms p(90)=17ms     p(95)=18.33ms  p(99.9)=26.18ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 428539
     http_req_receiving.............: avg=75.62µs min=24.93µs med=47.61µs max=212.16ms p(90)=100.43µs p(95)=194.87µs p(99.9)=1.87ms 
     http_req_sending...............: avg=35.64µs min=4.57µs  med=8.81µs  max=237.42ms p(90)=18.81µs  p(95)=106.14µs p(99.9)=2.01ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.68ms min=8.09ms  med=13.23ms max=266.48ms p(90)=16.88ms  p(95)=18.19ms  p(99.9)=25.96ms
     http_reqs......................: 428539  3542.756032/s
     iteration_duration.............: avg=13.99ms min=8.3ms   med=13.53ms max=298.86ms p(90)=17.21ms  p(95)=18.53ms  p(99.9)=26.43ms
     iterations.....................: 428439  3541.929326/s
     success_rate...................: 100.00% ✓ 428439      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1284162     ✗ 0     
     data_received..................: 38 GB   310 MB/s
     data_sent......................: 515 MB  4.3 MB/s
     http_req_blocked...............: avg=2.88µs  min=902ns   med=2.29µs  max=3.76ms   p(90)=3.7µs    p(95)=4.52µs   p(99.9)=29.77µs
     http_req_connecting............: avg=222ns   min=0s      med=0s      max=3.72ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.8ms  min=8.11ms  med=13.35ms max=274.1ms  p(90)=17.06ms  p(95)=18.39ms  p(99.9)=25.95ms
       { expected_response:true }...: avg=13.8ms  min=8.11ms  med=13.35ms max=274.1ms  p(90)=17.06ms  p(95)=18.39ms  p(99.9)=25.95ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 428154
     http_req_receiving.............: avg=75.3µs  min=24.69µs med=46.74µs max=135.61ms p(90)=101.64µs p(95)=188.91µs p(99.9)=2.01ms 
     http_req_sending...............: avg=34.36µs min=4.32µs  med=8.75µs  max=122.51ms p(90)=18.81µs  p(95)=102.38µs p(99.9)=1.96ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.69ms min=8.06ms  med=13.25ms max=273.92ms p(90)=16.94ms  p(95)=18.25ms  p(99.9)=25.71ms
     http_reqs......................: 428154  3539.925385/s
     iteration_duration.............: avg=14ms    min=8.28ms  med=13.55ms max=282.91ms p(90)=17.26ms  p(95)=18.59ms  p(99.9)=26.17ms
     iterations.....................: 428054  3539.098598/s
     success_rate...................: 100.00% ✓ 428054      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1278756     ✗ 0     
     data_received..................: 37 GB   308 MB/s
     data_sent......................: 512 MB  4.2 MB/s
     http_req_blocked...............: avg=3.08µs  min=931ns   med=2.29µs  max=7.13ms   p(90)=3.73µs  p(95)=4.5µs    p(99.9)=31.92µs
     http_req_connecting............: avg=403ns   min=0s      med=0s      max=7.1ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.86ms min=8.18ms  med=13.43ms max=258.69ms p(90)=17.14ms p(95)=18.48ms  p(99.9)=26.61ms
       { expected_response:true }...: avg=13.86ms min=8.18ms  med=13.43ms max=258.69ms p(90)=17.14ms p(95)=18.48ms  p(99.9)=26.61ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 426352
     http_req_receiving.............: avg=74.82µs min=25.28µs med=46.55µs max=112.05ms p(90)=98.41µs p(95)=190.21µs p(99.9)=2.01ms 
     http_req_sending...............: avg=34.19µs min=4.55µs  med=8.63µs  max=157.32ms p(90)=17.59µs p(95)=103.22µs p(99.9)=1.99ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.75ms min=8.13ms  med=13.32ms max=255.19ms p(90)=17.02ms p(95)=18.33ms  p(99.9)=26.36ms
     http_reqs......................: 426352  3524.872418/s
     iteration_duration.............: avg=14.06ms min=8.31ms  med=13.63ms max=290.88ms p(90)=17.34ms p(95)=18.68ms  p(99.9)=26.81ms
     iterations.....................: 426252  3524.045666/s
     success_rate...................: 100.00% ✓ 426252      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-11-03-0517)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1250283     ✗ 0     
     data_received..................: 36 GB   301 MB/s
     data_sent......................: 501 MB  4.1 MB/s
     http_req_blocked...............: avg=2.45µs  min=821ns   med=1.91µs  max=4.14ms   p(90)=3.12µs  p(95)=3.84µs   p(99.9)=25.42µs
     http_req_connecting............: avg=221ns   min=0s      med=0s      max=4.06ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.19ms min=8.37ms  med=13.84ms max=287.44ms p(90)=17.17ms p(95)=18.34ms  p(99.9)=25.56ms
       { expected_response:true }...: avg=14.19ms min=8.37ms  med=13.84ms max=287.44ms p(90)=17.17ms p(95)=18.34ms  p(99.9)=25.56ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 416861
     http_req_receiving.............: avg=65.29µs min=22.97µs med=42.77µs max=79.8ms   p(90)=86.2µs  p(95)=158.93µs p(99.9)=1.57ms 
     http_req_sending...............: avg=30.32µs min=4.29µs  med=8.15µs  max=83.76ms  p(90)=15.7µs  p(95)=91.07µs  p(99.9)=1.71ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.1ms  min=8.32ms  med=13.75ms max=286.88ms p(90)=17.07ms p(95)=18.23ms  p(99.9)=25.34ms
     http_reqs......................: 416861  3446.626711/s
     iteration_duration.............: avg=14.38ms min=8.54ms  med=14.03ms max=299.21ms p(90)=17.36ms p(95)=18.53ms  p(99.9)=25.79ms
     iterations.....................: 416761  3445.799906/s
     success_rate...................: 100.00% ✓ 416761      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.19-nightly.9815b25d)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1227864     ✗ 0     
     data_received..................: 36 GB   296 MB/s
     data_sent......................: 492 MB  4.1 MB/s
     http_req_blocked...............: avg=2.94µs  min=932ns   med=2.35µs  max=3.45ms   p(90)=3.82µs   p(95)=4.61µs   p(99.9)=33.03µs
     http_req_connecting............: avg=209ns   min=0s      med=0s      max=3.42ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.45ms min=8.34ms  med=14.04ms max=279.18ms p(90)=17.58ms  p(95)=18.89ms  p(99.9)=26.46ms
       { expected_response:true }...: avg=14.45ms min=8.34ms  med=14.04ms max=279.18ms p(90)=17.58ms  p(95)=18.89ms  p(99.9)=26.46ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 409388
     http_req_receiving.............: avg=76.02µs min=24.75µs med=48.79µs max=99.21ms  p(90)=100.67µs p(95)=198.11µs p(99.9)=1.77ms 
     http_req_sending...............: avg=33.96µs min=4.31µs  med=8.8µs   max=150.2ms  p(90)=17.75µs  p(95)=105.94µs p(99.9)=1.8ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.34ms min=8.28ms  med=13.94ms max=278.55ms p(90)=17.45ms  p(95)=18.75ms  p(99.9)=26.2ms 
     http_reqs......................: 409388  3384.085559/s
     iteration_duration.............: avg=14.65ms min=8.48ms  med=14.24ms max=294.8ms  p(90)=17.77ms  p(95)=19.09ms  p(99.9)=26.7ms 
     iterations.....................: 409288  3383.258938/s
     success_rate...................: 100.00% ✓ 409288      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1209588     ✗ 0     
     data_received..................: 35 GB   292 MB/s
     data_sent......................: 485 MB  4.0 MB/s
     http_req_blocked...............: avg=2.51µs  min=792ns   med=1.93µs  max=3.66ms   p(90)=3.21µs  p(95)=3.97µs   p(99.9)=25.8µs 
     http_req_connecting............: avg=241ns   min=0s      med=0s      max=3.61ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.67ms min=8.63ms  med=14.33ms max=280.67ms p(90)=17.72ms p(95)=18.95ms  p(99.9)=26.34ms
       { expected_response:true }...: avg=14.67ms min=8.63ms  med=14.33ms max=280.67ms p(90)=17.72ms p(95)=18.95ms  p(99.9)=26.34ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 403296
     http_req_receiving.............: avg=69.91µs min=23.06µs med=45.26µs max=179.68ms p(90)=94.24µs p(95)=170.51µs p(99.9)=1.55ms 
     http_req_sending...............: avg=31.61µs min=4.35µs  med=8.23µs  max=188.96ms p(90)=16.78µs p(95)=96.33µs  p(99.9)=1.63ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.57ms min=8.51ms  med=14.24ms max=276.46ms p(90)=17.62ms p(95)=18.84ms  p(99.9)=26.13ms
     http_reqs......................: 403296  3333.523107/s
     iteration_duration.............: avg=14.87ms min=8.82ms  med=14.52ms max=292.61ms p(90)=17.91ms p(95)=19.14ms  p(99.9)=26.55ms
     iterations.....................: 403196  3332.696537/s
     success_rate...................: 100.00% ✓ 403196      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: caliban (HotChocolate subgraphs) (3.2.1)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 558645     ✗ 0     
     data_received..................: 16 GB   134 MB/s
     data_sent......................: 224 MB  1.8 MB/s
     http_req_blocked...............: avg=3.58µs  min=922ns   med=2.7µs   max=3.96ms   p(90)=4.77µs  p(95)=5.61µs  p(99.9)=34.64µs 
     http_req_connecting............: avg=490ns   min=0s      med=0s      max=3.92ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=31.98ms min=18.14ms med=31.49ms max=292.67ms p(90)=37.04ms p(95)=39.06ms p(99.9)=54.63ms 
       { expected_response:true }...: avg=31.98ms min=18.14ms med=31.49ms max=292.67ms p(90)=37.04ms p(95)=39.06ms p(99.9)=54.63ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 186315
     http_req_receiving.............: avg=78.57µs min=25.34µs med=59.52µs max=211.32ms p(90)=102.4µs p(95)=122.9µs p(99.9)=904.89µs
     http_req_sending...............: avg=25.63µs min=4.93µs  med=11.91µs max=138.18ms p(90)=20.55µs p(95)=24.9µs  p(99.9)=811.73µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=31.87ms min=18.03ms med=31.4ms  max=254.08ms p(90)=36.94ms p(95)=38.95ms p(99.9)=54.29ms 
     http_reqs......................: 186315  1527.57686/s
     iteration_duration.............: avg=32.21ms min=19.45ms med=31.71ms max=311.55ms p(90)=37.26ms p(95)=39.27ms p(99.9)=55.31ms 
     iterations.....................: 186215  1526.75697/s
     success_rate...................: 100.00% ✓ 186215     ✗ 0     
     vus............................: 50      min=0        max=50  
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 530823      ✗ 0     
     data_received..................: 16 GB   127 MB/s
     data_sent......................: 213 MB  1.7 MB/s
     http_req_blocked...............: avg=3.22µs  min=832ns   med=2.15µs  max=4.21ms   p(90)=4.36µs   p(95)=5.27µs   p(99.9)=34µs   
     http_req_connecting............: avg=534ns   min=0s      med=0s      max=4.15ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.65ms min=18.12ms med=33.33ms max=293.87ms p(90)=39.24ms  p(95)=40.96ms  p(99.9)=49.2ms 
       { expected_response:true }...: avg=33.65ms min=18.12ms med=33.33ms max=293.87ms p(90)=39.24ms  p(95)=40.96ms  p(99.9)=49.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 177041
     http_req_receiving.............: avg=79.35µs min=25.43µs med=54.33µs max=188.1ms  p(90)=116.99µs p(95)=157.19µs p(99.9)=1.18ms 
     http_req_sending...............: avg=30.79µs min=4.22µs  med=9.15µs  max=197.04ms p(90)=21.04µs  p(95)=31.98µs  p(99.9)=1.19ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.54ms min=17.98ms med=33.22ms max=280.41ms p(90)=39.14ms  p(95)=40.86ms  p(99.9)=48.91ms
     http_reqs......................: 177041  1452.033045/s
     iteration_duration.............: avg=33.9ms  min=20.41ms med=33.56ms max=325.82ms p(90)=39.45ms  p(95)=41.18ms  p(99.9)=49.5ms 
     iterations.....................: 176941  1451.212877/s
     success_rate...................: 100.00% ✓ 176941      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.373.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 512346      ✗ 0     
     data_received..................: 15 GB   123 MB/s
     data_sent......................: 205 MB  1.7 MB/s
     http_req_blocked...............: avg=3.49µs  min=1.08µs  med=2.58µs  max=3.98ms   p(90)=4.13µs   p(95)=4.84µs   p(99.9)=35.71µs 
     http_req_connecting............: avg=595ns   min=0s      med=0s      max=3.95ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.9ms  min=18.14ms med=34.34ms max=293.51ms p(90)=41.67ms  p(95)=44ms     p(99.9)=56.13ms 
       { expected_response:true }...: avg=34.9ms  min=18.14ms med=34.34ms max=293.51ms p(90)=41.67ms  p(95)=44ms     p(99.9)=56.13ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 170882
     http_req_receiving.............: avg=77.75µs min=25.84µs med=62.08µs max=163.69ms p(90)=101.81µs p(95)=120.83µs p(99.9)=769.62µs
     http_req_sending...............: avg=23.74µs min=4.87µs  med=11.16µs max=181.06ms p(90)=17.66µs  p(95)=21.77µs  p(99.9)=786.88µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.8ms  min=18ms    med=34.24ms max=292.58ms p(90)=41.58ms  p(95)=43.9ms   p(99.9)=56.01ms 
     http_reqs......................: 170882  1401.148317/s
     iteration_duration.............: avg=35.12ms min=20.48ms med=34.54ms max=323.28ms p(90)=41.87ms  p(95)=44.2ms   p(99.9)=56.43ms 
     iterations.....................: 170782  1400.328366/s
     success_rate...................: 100.00% ✓ 170782      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 213108     ✗ 0    
     data_received..................: 6.2 GB  51 MB/s
     data_sent......................: 85 MB   699 kB/s
     http_req_blocked...............: avg=3.37µs  min=1.04µs  med=2.46µs  max=2.85ms   p(90)=3.96µs   p(95)=4.57µs   p(99.9)=41.33µs 
     http_req_connecting............: avg=641ns   min=0s      med=0s      max=2.81ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=84.16ms min=20.17ms med=82ms    max=331.6ms  p(90)=99.37ms  p(95)=106.94ms p(99.9)=214.39ms
       { expected_response:true }...: avg=84.16ms min=20.17ms med=82ms    max=331.6ms  p(90)=99.37ms  p(95)=106.94ms p(99.9)=214.39ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 71136
     http_req_receiving.............: avg=78.12µs min=26.76µs med=66.68µs max=99.88ms  p(90)=100.14µs p(95)=112.24µs p(99.9)=502.27µs
     http_req_sending...............: avg=19.53µs min=4.62µs  med=12.23µs max=83.03ms  p(90)=17.97µs  p(95)=19.93µs  p(99.9)=533.16µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=84.06ms min=19.96ms med=81.92ms max=331.06ms p(90)=99.28ms  p(95)=106.82ms p(99.9)=213.52ms
     http_reqs......................: 71136   582.223784/s
     iteration_duration.............: avg=84.47ms min=35.21ms med=82.24ms max=340.14ms p(90)=99.59ms  p(95)=107.19ms p(99.9)=214.84ms
     iterations.....................: 71036   581.405318/s
     success_rate...................: 100.00% ✓ 71036      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.19.1)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 195750     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 79 MB   642 kB/s
     http_req_blocked...............: avg=5.07µs  min=1.23µs  med=3.42µs  max=4.09ms   p(90)=4.97µs   p(95)=5.61µs   p(99.9)=48.51µs 
     http_req_connecting............: avg=1.4µs   min=0s      med=0s      max=4.05ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=91.59ms min=20.01ms med=89.91ms max=325.44ms p(90)=115.32ms p(95)=123.21ms p(99.9)=159.99ms
       { expected_response:true }...: avg=91.59ms min=20.01ms med=89.91ms max=325.44ms p(90)=115.32ms p(95)=123.21ms p(99.9)=159.99ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 65350
     http_req_receiving.............: avg=85.17µs min=30.76µs med=75.78µs max=146.92ms p(90)=108.32µs p(95)=120.31µs p(99.9)=532.96µs
     http_req_sending...............: avg=24.29µs min=4.64µs  med=15.77µs max=126.14ms p(90)=21.56µs  p(95)=23.64µs  p(99.9)=597.56µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.48ms min=19.89ms med=89.81ms max=324.85ms p(90)=115.22ms p(95)=123.09ms p(99.9)=159.32ms
     http_reqs......................: 65350   534.822/s
     iteration_duration.............: avg=91.96ms min=30.49ms med=90.19ms max=338.91ms p(90)=115.59ms p(95)=123.46ms p(99.9)=161.1ms 
     iterations.....................: 65250   534.003603/s
     success_rate...................: 100.00% ✓ 65250      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-nightly (HotChocolate subgraphs) (v3.0.0-preview.0-nightly.b787dc86)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 188259     ✗ 0    
     data_received..................: 5.5 GB  45 MB/s
     data_sent......................: 76 MB   618 kB/s
     http_req_blocked...............: avg=4.47µs  min=1.04µs  med=2.88µs  max=3.89ms   p(90)=4.38µs   p(95)=4.95µs   p(99.9)=48.55µs 
     http_req_connecting............: avg=1.38µs  min=0s      med=0s      max=3.85ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=95.25ms min=20.11ms med=93.79ms max=343.14ms p(90)=119.05ms p(95)=127.32ms p(99.9)=165.88ms
       { expected_response:true }...: avg=95.25ms min=20.11ms med=93.79ms max=343.14ms p(90)=119.05ms p(95)=127.32ms p(99.9)=165.88ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 62853
     http_req_receiving.............: avg=80.4µs  min=25.65µs med=69.24µs max=204.8ms  p(90)=102.81µs p(95)=115.45µs p(99.9)=501.08µs
     http_req_sending...............: avg=25.38µs min=4.81µs  med=13.57µs max=160.4ms  p(90)=19.54µs  p(95)=21.59µs  p(99.9)=488.23µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=95.15ms min=20.05ms med=93.69ms max=342.72ms p(90)=118.96ms p(95)=127.21ms p(99.9)=164.93ms
     http_reqs......................: 62853   514.218455/s
     iteration_duration.............: avg=95.63ms min=36.76ms med=94.04ms max=353.16ms p(90)=119.32ms p(95)=127.57ms p(99.9)=168.22ms
     iterations.....................: 62753   513.400326/s
     success_rate...................: 100.00% ✓ 62753      ✗ 0    
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

     checks.........................: 100.00% ✓ 141870     ✗ 0    
     data_received..................: 4.1 GB  34 MB/s
     data_sent......................: 57 MB   465 kB/s
     http_req_blocked...............: avg=5.33µs   min=1.17µs  med=3.31µs   max=3.55ms   p(90)=4.8µs    p(95)=5.4µs    p(99.9)=197.28µs
     http_req_connecting............: avg=1.83µs   min=0s      med=0s       max=3.51ms   p(90)=0s       p(95)=0s       p(99.9)=154.37µs
     http_req_duration..............: avg=126.43ms min=21.02ms med=124.64ms max=338.43ms p(90)=157.15ms p(95)=167.64ms p(99.9)=213.35ms
       { expected_response:true }...: avg=126.43ms min=21.02ms med=124.64ms max=338.43ms p(90)=157.15ms p(95)=167.64ms p(99.9)=213.35ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 47390
     http_req_receiving.............: avg=78.54µs  min=29.78µs med=73.58µs  max=7.32ms   p(90)=105.53µs p(95)=117.49µs p(99.9)=543.85µs
     http_req_sending...............: avg=24.63µs  min=5.32µs  med=14.59µs  max=97.6ms   p(90)=20.15µs  p(95)=22.1µs   p(99.9)=524.88µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=126.32ms min=20.93ms med=124.55ms max=337.9ms  p(90)=157.05ms p(95)=167.54ms p(99.9)=213.28ms
     http_reqs......................: 47390   387.416781/s
     iteration_duration.............: avg=126.91ms min=28.42ms med=124.94ms max=356.69ms p(90)=157.43ms p(95)=167.94ms p(99.9)=217.38ms
     iterations.....................: 47290   386.599274/s
     success_rate...................: 100.00% ✓ 47290      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 107022     ✗ 0    
     data_received..................: 3.1 GB  26 MB/s
     data_sent......................: 43 MB   352 kB/s
     http_req_blocked...............: avg=6.27µs   min=1.35µs  med=3.65µs   max=3.66ms   p(90)=5.2µs    p(95)=5.87µs   p(99.9)=1.1ms   
     http_req_connecting............: avg=2.29µs   min=0s      med=0s       max=3.62ms   p(90)=0s       p(95)=0s       p(99.9)=1.05ms  
     http_req_duration..............: avg=167.57ms min=16.65ms med=152.15ms max=734.3ms  p(90)=196.3ms  p(95)=214.09ms p(99.9)=693.19ms
       { expected_response:true }...: avg=167.57ms min=16.65ms med=152.15ms max=734.3ms  p(90)=196.3ms  p(95)=214.09ms p(99.9)=693.19ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 35774
     http_req_receiving.............: avg=94.3µs   min=36.81µs med=89.63µs  max=11.93ms  p(90)=119.79µs p(95)=131.57µs p(99.9)=646.57µs
     http_req_sending...............: avg=26.26µs  min=6.39µs  med=17.86µs  max=85.62ms  p(90)=22.79µs  p(95)=24.73µs  p(99.9)=565.53µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=167.45ms min=16.47ms med=152.03ms max=734.18ms p(90)=196.18ms p(95)=213.98ms p(99.9)=693.09ms
     http_reqs......................: 35774   293.200715/s
     iteration_duration.............: avg=168.28ms min=39.12ms med=152.5ms  max=734.52ms p(90)=196.66ms p(95)=214.54ms p(99.9)=693.47ms
     iterations.....................: 35674   292.381124/s
     success_rate...................: 100.00% ✓ 35674      ✗ 0    
     vus............................: 10      min=0        max=50 
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

     checks.........................: 100.00% ✓ 98049      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   321 kB/s
     http_req_blocked...............: avg=6.41µs   min=1.06µs  med=3.11µs   max=4.19ms   p(90)=4.45µs   p(95)=5µs      p(99.9)=1.46ms  
     http_req_connecting............: avg=3.08µs   min=0s      med=0s       max=4.15ms   p(90)=0s       p(95)=0s       p(99.9)=1.43ms  
     http_req_duration..............: avg=182.88ms min=22.45ms med=182.66ms max=374.65ms p(90)=208.98ms p(95)=215.13ms p(99.9)=280.91ms
       { expected_response:true }...: avg=182.88ms min=22.45ms med=182.66ms max=374.65ms p(90)=208.98ms p(95)=215.13ms p(99.9)=280.91ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32783
     http_req_receiving.............: avg=95.29µs  min=30.64µs med=86.79µs  max=123.7ms  p(90)=115.65µs p(95)=127.04µs p(99.9)=585.95µs
     http_req_sending...............: avg=28.05µs  min=5.11µs  med=16.48µs  max=80.45ms  p(90)=20.83µs  p(95)=22.59µs  p(99.9)=551.17µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=182.75ms min=22.35ms med=182.55ms max=374.48ms p(90)=208.88ms p(95)=215.02ms p(99.9)=278.93ms
     http_reqs......................: 32783   267.444103/s
     iteration_duration.............: avg=183.66ms min=61.21ms med=183.02ms max=392.91ms p(90)=209.27ms p(95)=215.45ms p(99.9)=284.63ms
     iterations.....................: 32683   266.628302/s
     success_rate...................: 100.00% ✓ 32683      ✗ 0    
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

