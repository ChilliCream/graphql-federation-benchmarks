## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.7 | 3,614 | 3,627 | 3,606 | 0.2% | 366 MB | 103.8 KB |  |
| fusion-aot-11 | 16.7.7 | 3,611 | 3,638 | 3,607 | 0.4% | 116 MB | 32.9 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.23 | 3,610 | 3,628 | 3,594 | 0.4% | 351 MB | 99.7 KB |  |
| nitro-router | 16.8.0-p.23 | 3,608 | 3,621 | 3,596 | 0.3% | 144 MB | 41.0 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 3,603 | 3,616 | 3,596 | 0.2% | 114 MB | 32.4 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.23 | 3,603 | 3,627 | 3,590 | 0.4% | 96 MB | 27.2 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.23 | 3,585 | 3,602 | 3,566 | 0.4% | 98 MB | 28.0 KB |  |
| nitro-router-fed | 16.8.0-p.23 | 3,582 | 3,592 | 3,575 | 0.2% | 149 MB | 42.7 KB |  |
| fusion-fed-net-11 | 16.7.7 | 3,557 | 3,571 | 3,549 | 0.2% | 367 MB | 105.6 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.23 | 3,557 | 3,563 | 3,547 | 0.2% | 354 MB | 101.8 KB |  |
| feddi-gateway | 2026-11-22-1912 | 3,538 | 3,548 | 3,530 | 0.2% | 2,313 MB | 669.5 KB |  |
| hive-router | v0.3.17 | 3,397 | 3,410 | 3,380 | 0.3% | 90 MB | 27.1 KB |  |
| hive-router-nightly | v0.3.21-nightly.46ee6fa7 | 3,391 | 3,403 | 3,382 | 0.3% | 89 MB | 27.0 KB |  |
| caliban | 3.2.1 | 1,529 | 1,531 | 1,528 | 0.1% | 6,265 MB | 4,195.9 KB |  |
| cosmo | 0.373.0 | 1,437 | 1,439 | 1,432 | 0.2% | 151 MB | 107.6 KB |  |
| grafbase | 0.53.5 | 1,436 | 1,445 | 1,428 | 0.5% | 100 MB | 71.6 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 597 | 600 | 597 | 0.2% | 2,619 MB | 4,493.1 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.b135f054 | 516 | 517 | 515 | 0.2% | 195 MB | 386.2 KB |  |
| apollo-router | v2.19.1 | 490 | 490 | 489 | 0.1% | 179 MB | 373.5 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 388 | 388 | 388 | 0.0% | 207 MB | 545.6 KB |  |
| hive-gateway | 2.15.10 | 292 | 294 | 291 | 0.4% | 3,312 MB | 11,614.1 KB |  |
| apollo-gateway | 2.14.4 | 269 | 269 | 267 | 0.3% | 2,164 MB | 8,237.7 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1311075     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 525 MB  4.3 MB/s
     http_req_blocked...............: avg=2.38µs  min=801ns   med=1.82µs  max=4.39ms   p(90)=2.92µs  p(95)=3.59µs   p(99.9)=24.21µs
     http_req_connecting............: avg=221ns   min=0s      med=0s      max=4.35ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.52ms min=8.19ms  med=13.12ms max=280.22ms p(90)=16.6ms  p(95)=17.83ms  p(99.9)=25.54ms
       { expected_response:true }...: avg=13.52ms min=8.19ms  med=13.12ms max=280.22ms p(90)=16.6ms  p(95)=17.83ms  p(99.9)=25.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 437125
     http_req_receiving.............: avg=69.42µs min=24.44µs med=43.89µs max=101.87ms p(90)=88.5µs  p(95)=167.08µs p(99.9)=1.87ms 
     http_req_sending...............: avg=31.25µs min=4.19µs  med=7.78µs  max=126.19ms p(90)=15.06µs p(95)=90.77µs  p(99.9)=1.68ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.42ms min=8.14ms  med=13.03ms max=271.89ms p(90)=16.49ms p(95)=17.7ms   p(99.9)=25.13ms
     http_reqs......................: 437125  3614.244627/s
     iteration_duration.............: avg=13.72ms min=8.32ms  med=13.31ms max=290.02ms p(90)=16.79ms p(95)=18.02ms  p(99.9)=25.77ms
     iterations.....................: 437025  3613.417806/s
     success_rate...................: 100.00% ✓ 437025      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1310220     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 525 MB  4.3 MB/s
     http_req_blocked...............: avg=2.86µs  min=902ns   med=2.31µs  max=3.65ms   p(90)=3.63µs  p(95)=4.37µs   p(99.9)=30.96µs
     http_req_connecting............: avg=207ns   min=0s      med=0s      max=3.59ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.52ms min=7.81ms  med=13.08ms max=282.29ms p(90)=16.65ms p(95)=17.97ms  p(99.9)=25.65ms
       { expected_response:true }...: avg=13.52ms min=7.81ms  med=13.08ms max=282.29ms p(90)=16.65ms p(95)=17.97ms  p(99.9)=25.65ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 436840
     http_req_receiving.............: avg=73.54µs min=24.71µs med=46.7µs  max=32.97ms  p(90)=96.72µs p(95)=190.08µs p(99.9)=1.91ms 
     http_req_sending...............: avg=34.67µs min=4.49µs  med=8.81µs  max=176.88ms p(90)=17.31µs p(95)=102.78µs p(99.9)=1.82ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.42ms min=7.77ms  med=12.97ms max=281.82ms p(90)=16.52ms p(95)=17.83ms  p(99.9)=25.41ms
     http_reqs......................: 436840  3611.550243/s
     iteration_duration.............: avg=13.72ms min=7.93ms  med=13.27ms max=293ms    p(90)=16.85ms p(95)=18.16ms  p(99.9)=25.89ms
     iterations.....................: 436740  3610.723498/s
     success_rate...................: 100.00% ✓ 436740      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1309581     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 525 MB  4.3 MB/s
     http_req_blocked...............: avg=2.8µs   min=881ns   med=2.27µs  max=4.62ms   p(90)=3.66µs  p(95)=4.46µs   p(99.9)=29.52µs
     http_req_connecting............: avg=165ns   min=0s      med=0s      max=4.59ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.53ms min=8.16ms  med=13.08ms max=271.56ms p(90)=16.74ms p(95)=18.06ms  p(99.9)=25.64ms
       { expected_response:true }...: avg=13.53ms min=8.16ms  med=13.08ms max=271.56ms p(90)=16.74ms p(95)=18.06ms  p(99.9)=25.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 436627
     http_req_receiving.............: avg=74.53µs min=23.01µs med=45.99µs max=156.87ms p(90)=98.28µs p(95)=186.91µs p(99.9)=2.11ms 
     http_req_sending...............: avg=34.42µs min=4.36µs  med=8.63µs  max=148.61ms p(90)=17.72µs p(95)=100.42µs p(99.9)=2.02ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.42ms min=8.03ms  med=12.98ms max=264.34ms p(90)=16.62ms p(95)=17.92ms  p(99.9)=25.43ms
     http_reqs......................: 436627  3610.128594/s
     iteration_duration.............: avg=13.73ms min=8.31ms  med=13.28ms max=295.34ms p(90)=16.94ms p(95)=18.26ms  p(99.9)=25.86ms
     iterations.....................: 436527  3609.301772/s
     success_rate...................: 100.00% ✓ 436527      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: nitro-router (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1309122     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 525 MB  4.3 MB/s
     http_req_blocked...............: avg=2.82µs  min=871ns   med=2.24µs  max=3.78ms   p(90)=3.59µs  p(95)=4.36µs   p(99.9)=31.45µs
     http_req_connecting............: avg=209ns   min=0s      med=0s      max=3.75ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.54ms min=7.95ms  med=13.1ms  max=278.81ms p(90)=16.7ms  p(95)=17.99ms  p(99.9)=25.62ms
       { expected_response:true }...: avg=13.54ms min=7.95ms  med=13.1ms  max=278.81ms p(90)=16.7ms  p(95)=17.99ms  p(99.9)=25.62ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 436474
     http_req_receiving.............: avg=72.61µs min=22.94µs med=43.79µs max=238.88ms p(90)=94.9µs  p(95)=185.74µs p(99.9)=1.9ms  
     http_req_sending...............: avg=33.65µs min=4.41µs  med=8.48µs  max=204.74ms p(90)=17.04µs p(95)=100.7µs  p(99.9)=1.89ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.43ms min=7.89ms  med=13ms    max=278.62ms p(90)=16.58ms p(95)=17.86ms  p(99.9)=25.34ms
     http_reqs......................: 436474  3608.718266/s
     iteration_duration.............: avg=13.74ms min=8.15ms  med=13.3ms  max=292.4ms  p(90)=16.9ms  p(95)=18.19ms  p(99.9)=25.83ms
     iterations.....................: 436374  3607.891477/s
     success_rate...................: 100.00% ✓ 436374      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1307124     ✗ 0     
     data_received..................: 38 GB   315 MB/s
     data_sent......................: 524 MB  4.3 MB/s
     http_req_blocked...............: avg=2.42µs  min=811ns   med=1.89µs  max=4.1ms    p(90)=3.15µs  p(95)=3.92µs   p(99.9)=23.27µs
     http_req_connecting............: avg=196ns   min=0s      med=0s      max=4.07ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.57ms min=8.24ms  med=13.16ms max=275.97ms p(90)=16.59ms p(95)=17.81ms  p(99.9)=25.19ms
       { expected_response:true }...: avg=13.57ms min=8.24ms  med=13.16ms max=275.97ms p(90)=16.59ms p(95)=17.81ms  p(99.9)=25.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 435808
     http_req_receiving.............: avg=68.75µs min=23.06µs med=43.82µs max=246.36ms p(90)=90.84µs p(95)=170.44µs p(99.9)=1.71ms 
     http_req_sending...............: avg=30.84µs min=4.19µs  med=7.95µs  max=94.81ms  p(90)=16.04µs p(95)=92.77µs  p(99.9)=1.76ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.47ms min=8.19ms  med=13.07ms max=275.61ms p(90)=16.48ms p(95)=17.69ms  p(99.9)=25ms   
     http_reqs......................: 435808  3603.07275/s
     iteration_duration.............: avg=13.76ms min=8.41ms  med=13.35ms max=295.95ms p(90)=16.78ms p(95)=18ms     p(99.9)=25.4ms 
     iterations.....................: 435708  3602.245994/s
     success_rate...................: 100.00% ✓ 435708      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1307034     ✗ 0     
     data_received..................: 38 GB   315 MB/s
     data_sent......................: 524 MB  4.3 MB/s
     http_req_blocked...............: avg=2.39µs  min=781ns   med=1.81µs  max=3.52ms   p(90)=3.02µs  p(95)=3.82µs   p(99.9)=24.14µs
     http_req_connecting............: avg=219ns   min=0s      med=0s      max=3.47ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.57ms min=8.15ms  med=13.17ms max=278.17ms p(90)=16.67ms p(95)=17.92ms  p(99.9)=25.32ms
       { expected_response:true }...: avg=13.57ms min=8.15ms  med=13.17ms max=278.17ms p(90)=16.67ms p(95)=17.92ms  p(99.9)=25.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 435778
     http_req_receiving.............: avg=67.51µs min=23.71µs med=43.66µs max=78.59ms  p(90)=90.84µs p(95)=164.14µs p(99.9)=1.67ms 
     http_req_sending...............: avg=30.41µs min=4.16µs  med=7.71µs  max=228.41ms p(90)=15.66µs p(95)=90.2µs   p(99.9)=1.66ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.47ms min=8.09ms  med=13.07ms max=277.46ms p(90)=16.57ms p(95)=17.79ms  p(99.9)=25.13ms
     http_reqs......................: 435778  3603.175258/s
     iteration_duration.............: avg=13.76ms min=8.31ms  med=13.36ms max=303.87ms p(90)=16.86ms p(95)=18.11ms  p(99.9)=25.59ms
     iterations.....................: 435678  3602.348421/s
     success_rate...................: 100.00% ✓ 435678      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1300593     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 521 MB  4.3 MB/s
     http_req_blocked...............: avg=2.38µs  min=781ns  med=1.82µs  max=4.06ms   p(90)=3.01µs  p(95)=3.75µs   p(99.9)=23.03µs
     http_req_connecting............: avg=218ns   min=0s     med=0s      max=3.99ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.63ms min=8.18ms med=13.23ms max=266.95ms p(90)=16.77ms p(95)=18.03ms  p(99.9)=25.63ms
       { expected_response:true }...: avg=13.63ms min=8.18ms med=13.23ms max=266.95ms p(90)=16.77ms p(95)=18.03ms  p(99.9)=25.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 433631
     http_req_receiving.............: avg=67µs    min=23.9µs med=42.94µs max=119.94ms p(90)=88.89µs p(95)=169.61µs p(99.9)=1.7ms  
     http_req_sending...............: avg=31.03µs min=4.15µs med=7.69µs  max=147.6ms  p(90)=15.35µs p(95)=92.47µs  p(99.9)=1.79ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.54ms min=8.1ms  med=13.14ms max=266.43ms p(90)=16.67ms p(95)=17.91ms  p(99.9)=25.42ms
     http_reqs......................: 433631  3585.209266/s
     iteration_duration.............: avg=13.83ms min=8.31ms med=13.42ms max=284.56ms p(90)=16.96ms p(95)=18.22ms  p(99.9)=25.85ms
     iterations.....................: 433531  3584.382478/s
     success_rate...................: 100.00% ✓ 433531      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: nitro-router-fed (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1299723     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 521 MB  4.3 MB/s
     http_req_blocked...............: avg=2.84µs  min=912ns   med=2.28µs  max=3.64ms   p(90)=3.67µs  p(95)=4.45µs   p(99.9)=30.69µs
     http_req_connecting............: avg=207ns   min=0s      med=0s      max=3.61ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.63ms min=8.09ms  med=13.19ms max=288.66ms p(90)=16.88ms p(95)=18.24ms  p(99.9)=25.87ms
       { expected_response:true }...: avg=13.63ms min=8.09ms  med=13.19ms max=288.66ms p(90)=16.88ms p(95)=18.24ms  p(99.9)=25.87ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 433341
     http_req_receiving.............: avg=74.37µs min=24.48µs med=46.05µs max=223.54ms p(90)=97.62µs p(95)=189.42µs p(99.9)=2.03ms 
     http_req_sending...............: avg=34.29µs min=4.4µs   med=8.64µs  max=160.97ms p(90)=17.61µs p(95)=101.71µs p(99.9)=2.02ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.53ms min=8.05ms  med=13.08ms max=268.94ms p(90)=16.76ms p(95)=18.1ms   p(99.9)=25.64ms
     http_reqs......................: 433341  3582.836505/s
     iteration_duration.............: avg=13.84ms min=8.26ms  med=13.38ms max=300.45ms p(90)=17.08ms p(95)=18.44ms  p(99.9)=26.1ms 
     iterations.....................: 433241  3582.009711/s
     success_rate...................: 100.00% ✓ 433241      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1290690     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.44µs  min=802ns   med=1.88µs  max=3.31ms   p(90)=3.19µs  p(95)=4.04µs  p(99.9)=27.43µs
     http_req_connecting............: avg=183ns   min=0s      med=0s      max=3.22ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.73ms min=8.21ms  med=13.33ms max=279.8ms  p(90)=16.89ms p(95)=18.13ms p(99.9)=25.52ms
       { expected_response:true }...: avg=13.73ms min=8.21ms  med=13.33ms max=279.8ms  p(90)=16.89ms p(95)=18.13ms p(99.9)=25.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 430330
     http_req_receiving.............: avg=68.32µs min=24.19µs med=43.43µs max=19.81ms  p(90)=93.89µs p(95)=169.5µs p(99.9)=1.76ms 
     http_req_sending...............: avg=32.51µs min=4.16µs  med=8.11µs  max=176.61ms p(90)=17.65µs p(95)=93.43µs p(99.9)=1.84ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.63ms min=8.09ms  med=13.23ms max=279.06ms p(90)=16.78ms p(95)=18ms    p(99.9)=25.28ms
     http_reqs......................: 430330  3557.827503/s
     iteration_duration.............: avg=13.93ms min=8.38ms  med=13.53ms max=288.34ms p(90)=17.08ms p(95)=18.32ms p(99.9)=25.76ms
     iterations.....................: 430230  3557.000736/s
     success_rate...................: 100.00% ✓ 430230      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1290702     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.45µs  min=801ns  med=1.86µs  max=6.65ms   p(90)=3µs     p(95)=3.7µs    p(99.9)=24.78µs
     http_req_connecting............: avg=213ns   min=0s     med=0s      max=3.99ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.74ms min=8.08ms med=13.34ms max=289.36ms p(90)=16.92ms p(95)=18.16ms  p(99.9)=25.45ms
       { expected_response:true }...: avg=13.74ms min=8.08ms med=13.34ms max=289.36ms p(90)=16.92ms p(95)=18.16ms  p(99.9)=25.45ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 430334
     http_req_receiving.............: avg=69.56µs min=24.3µs med=43.89µs max=183.49ms p(90)=91.11µs p(95)=168.57µs p(99.9)=1.82ms 
     http_req_sending...............: avg=31.17µs min=4.22µs med=7.83µs  max=168.57ms p(90)=15.6µs  p(95)=90.9µs   p(99.9)=1.8ms  
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.64ms min=8.05ms med=13.25ms max=267ms    p(90)=16.81ms p(95)=18.05ms  p(99.9)=25.16ms
     http_reqs......................: 430334  3557.973767/s
     iteration_duration.............: avg=13.93ms min=8.21ms med=13.53ms max=297.88ms p(90)=17.11ms p(95)=18.35ms  p(99.9)=25.68ms
     iterations.....................: 430234  3557.146973/s
     success_rate...................: 100.00% ✓ 430234      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-11-22-1912)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1283859     ✗ 0     
     data_received..................: 37 GB   309 MB/s
     data_sent......................: 514 MB  4.3 MB/s
     http_req_blocked...............: avg=2.9µs   min=791ns   med=1.95µs  max=7.94ms   p(90)=3.36µs  p(95)=4.24µs   p(99.9)=26.53µs
     http_req_connecting............: avg=532ns   min=0s      med=0s      max=7.8ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.81ms min=8.32ms  med=13.38ms max=263ms    p(90)=16.98ms p(95)=18.27ms  p(99.9)=26.04ms
       { expected_response:true }...: avg=13.81ms min=8.32ms  med=13.38ms max=263ms    p(90)=16.98ms p(95)=18.27ms  p(99.9)=26.04ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 428053
     http_req_receiving.............: avg=71.62µs min=23.32µs med=44.04µs max=166.22ms p(90)=97.3µs  p(95)=176.09µs p(99.9)=2ms    
     http_req_sending...............: avg=32.65µs min=4.37µs  med=8.38µs  max=169ms    p(90)=18.08µs p(95)=96.47µs  p(99.9)=1.91ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.7ms  min=8.24ms  med=13.28ms max=261.81ms p(90)=16.86ms p(95)=18.14ms  p(99.9)=25.68ms
     http_reqs......................: 428053  3538.566357/s
     iteration_duration.............: avg=14.01ms min=8.57ms  med=13.57ms max=304.27ms p(90)=17.17ms p(95)=18.46ms  p(99.9)=26.25ms
     iterations.....................: 427953  3537.739691/s
     success_rate...................: 100.00% ✓ 427953      ✗ 0     
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

     checks.........................: 100.00% ✓ 1232826     ✗ 0     
     data_received..................: 36 GB   297 MB/s
     data_sent......................: 494 MB  4.1 MB/s
     http_req_blocked...............: avg=2.45µs  min=791ns   med=1.87µs  max=3.47ms   p(90)=3.25µs  p(95)=4.11µs   p(99.9)=26.72µs
     http_req_connecting............: avg=207ns   min=0s      med=0s      max=3.43ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.39ms min=8.57ms  med=14.04ms max=285.24ms p(90)=17.42ms p(95)=18.65ms  p(99.9)=26.24ms
       { expected_response:true }...: avg=14.39ms min=8.57ms  med=14.04ms max=285.24ms p(90)=17.42ms p(95)=18.65ms  p(99.9)=26.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 411042
     http_req_receiving.............: avg=68.84µs min=22.93µs med=43.5µs  max=177.1ms  p(90)=96.01µs p(95)=177.21µs p(99.9)=1.56ms 
     http_req_sending...............: avg=30.89µs min=4.28µs  med=8µs     max=131.21ms p(90)=17.49µs p(95)=95.71µs  p(99.9)=1.59ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.29ms min=8.53ms  med=13.95ms max=284.61ms p(90)=17.31ms p(95)=18.53ms  p(99.9)=25.93ms
     http_reqs......................: 411042  3397.992922/s
     iteration_duration.............: avg=14.59ms min=8.69ms  med=14.23ms max=300.2ms  p(90)=17.61ms p(95)=18.84ms  p(99.9)=26.48ms
     iterations.....................: 410942  3397.166244/s
     success_rate...................: 100.00% ✓ 410942      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.21-nightly.46ee6fa7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1230432     ✗ 0     
     data_received..................: 36 GB   297 MB/s
     data_sent......................: 493 MB  4.1 MB/s
     http_req_blocked...............: avg=2.98µs  min=912ns   med=2.4µs   max=3.46ms   p(90)=3.91µs   p(95)=4.73µs   p(99.9)=32.17µs
     http_req_connecting............: avg=210ns   min=0s      med=0s      max=3.42ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.42ms min=8.31ms  med=14.03ms max=285.9ms  p(90)=17.54ms  p(95)=18.84ms  p(99.9)=26.48ms
       { expected_response:true }...: avg=14.42ms min=8.31ms  med=14.03ms max=285.9ms  p(90)=17.54ms  p(95)=18.84ms  p(99.9)=26.48ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 410244
     http_req_receiving.............: avg=75µs    min=23.82µs med=47.33µs max=235.22ms p(90)=100.61µs p(95)=190.89µs p(99.9)=1.86ms 
     http_req_sending...............: avg=33.47µs min=4.32µs  med=9µs     max=98.08ms  p(90)=18.3µs   p(95)=104.77µs p(99.9)=1.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.31ms min=8.27ms  med=13.93ms max=285.39ms p(90)=17.42ms  p(95)=18.7ms   p(99.9)=26.25ms
     http_reqs......................: 410244  3391.192506/s
     iteration_duration.............: avg=14.61ms min=8.43ms  med=14.22ms max=295.68ms p(90)=17.73ms  p(95)=19.04ms  p(99.9)=26.7ms 
     iterations.....................: 410144  3390.365877/s
     success_rate...................: 100.00% ✓ 410144      ✗ 0     
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

     checks.........................: 100.00% ✓ 559254      ✗ 0     
     data_received..................: 16 GB   134 MB/s
     data_sent......................: 224 MB  1.8 MB/s
     http_req_blocked...............: avg=4.18µs  min=962ns   med=3.32µs  max=3.76ms   p(90)=5.32µs   p(95)=6.18µs   p(99.9)=35.76µs 
     http_req_connecting............: avg=523ns   min=0s      med=0s      max=3.71ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=31.93ms min=18.51ms med=31.45ms max=297.61ms p(90)=37.02ms  p(95)=39ms     p(99.9)=51.61ms 
       { expected_response:true }...: avg=31.93ms min=18.51ms med=31.45ms max=297.61ms p(90)=37.02ms  p(95)=39ms     p(99.9)=51.61ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 186518
     http_req_receiving.............: avg=79.35µs min=26.28µs med=64.51µs max=50.66ms  p(90)=109.16µs p(95)=132.32µs p(99.9)=999.45µs
     http_req_sending...............: avg=27.63µs min=4.6µs   med=13.35µs max=85.28ms  p(90)=21.46µs  p(95)=26.27µs  p(99.9)=894.67µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=31.82ms min=18.38ms med=31.35ms max=297.15ms p(90)=36.91ms  p(95)=38.89ms  p(99.9)=51.4ms  
     http_reqs......................: 186518  1529.236739/s
     iteration_duration.............: avg=32.17ms min=20.95ms med=31.68ms max=306.77ms p(90)=37.25ms  p(95)=39.24ms  p(99.9)=51.97ms 
     iterations.....................: 186418  1528.416852/s
     success_rate...................: 100.00% ✓ 186418      ✗ 0     
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

     checks.........................: 100.00% ✓ 525603      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 211 MB  1.7 MB/s
     http_req_blocked...............: avg=2.73µs  min=942ns   med=2.1µs   max=3.52ms   p(90)=3.54µs  p(95)=4.21µs  p(99.9)=26.21µs 
     http_req_connecting............: avg=340ns   min=0s      med=0s      max=3.48ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=34.03ms min=17.95ms med=33.42ms max=293.32ms p(90)=40.71ms p(95)=42.99ms p(99.9)=55.38ms 
       { expected_response:true }...: avg=34.03ms min=17.95ms med=33.42ms max=293.32ms p(90)=40.71ms p(95)=42.99ms p(99.9)=55.38ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 175301
     http_req_receiving.............: avg=69.58µs min=25.48µs med=58.47µs max=58.75ms  p(90)=95.9µs  p(95)=112.7µs p(99.9)=700.62µs
     http_req_sending...............: avg=21.46µs min=4.57µs  med=9.79µs  max=115.18ms p(90)=16.71µs p(95)=20.48µs p(99.9)=756.63µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=33.94ms min=17.83ms med=33.33ms max=293.08ms p(90)=40.62ms p(95)=42.9ms  p(99.9)=55.22ms 
     http_reqs......................: 175301  1437.382572/s
     iteration_duration.............: avg=34.23ms min=20.56ms med=33.62ms max=303.03ms p(90)=40.91ms p(95)=43.17ms p(99.9)=55.7ms  
     iterations.....................: 175201  1436.56262/s
     success_rate...................: 100.00% ✓ 175201      ✗ 0     
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

     checks.........................: 100.00% ✓ 525120      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 210 MB  1.7 MB/s
     http_req_blocked...............: avg=3.24µs  min=821ns   med=2.17µs  max=5.18ms   p(90)=4.3µs    p(95)=5.27µs   p(99.9)=33.77µs
     http_req_connecting............: avg=540ns   min=0s      med=0s      max=4.11ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.02ms min=17.6ms  med=33.68ms max=301.65ms p(90)=39.61ms  p(95)=41.36ms  p(99.9)=50.3ms 
       { expected_response:true }...: avg=34.02ms min=17.6ms  med=33.68ms max=301.65ms p(90)=39.61ms  p(95)=41.36ms  p(99.9)=50.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 175140
     http_req_receiving.............: avg=79.28µs min=27.02µs med=56.08µs max=142.12ms p(90)=116.53µs p(95)=156.93µs p(99.9)=1.24ms 
     http_req_sending...............: avg=28.18µs min=4.67µs  med=9.3µs   max=156.77ms p(90)=21.62µs  p(95)=31.84µs  p(99.9)=1.16ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.91ms min=17.46ms med=33.58ms max=301.2ms  p(90)=39.51ms  p(95)=41.25ms  p(99.9)=50.07ms
     http_reqs......................: 175140  1436.352742/s
     iteration_duration.............: avg=34.26ms min=20.5ms  med=33.91ms max=323.94ms p(90)=39.83ms  p(95)=41.57ms  p(99.9)=50.65ms
     iterations.....................: 175040  1435.532625/s
     success_rate...................: 100.00% ✓ 175040      ✗ 0     
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

     checks.........................: 100.00% ✓ 218772     ✗ 0    
     data_received..................: 6.4 GB  52 MB/s
     data_sent......................: 88 MB   718 kB/s
     http_req_blocked...............: avg=4.79µs  min=1.05µs  med=2.96µs  max=4.25ms   p(90)=4.52µs   p(95)=5.17µs   p(99.9)=47.75µs 
     http_req_connecting............: avg=1.58µs  min=0s      med=0s      max=4.21ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=81.96ms min=20.13ms med=79.78ms max=345.96ms p(90)=96.4ms   p(95)=104.14ms p(99.9)=202.14ms
       { expected_response:true }...: avg=81.96ms min=20.13ms med=79.78ms max=345.96ms p(90)=96.4ms   p(95)=104.14ms p(99.9)=202.14ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 73024
     http_req_receiving.............: avg=80.37µs min=28.43µs med=72.31µs max=40.98ms  p(90)=106.07µs p(95)=118.69µs p(99.9)=584.86µs
     http_req_sending...............: avg=19.93µs min=4.77µs  med=14.15µs max=58.81ms  p(90)=19.58µs  p(95)=21.64µs  p(99.9)=571.61µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=81.86ms min=20.04ms med=79.67ms max=345.58ms p(90)=96.31ms  p(95)=104.02ms p(99.9)=201.99ms
     http_reqs......................: 73024   597.632851/s
     iteration_duration.............: avg=82.29ms min=25.6ms  med=80.03ms max=356.58ms p(90)=96.64ms  p(95)=104.41ms p(99.9)=203.26ms
     iterations.....................: 72924   596.814445/s
     success_rate...................: 100.00% ✓ 72924      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-nightly (HotChocolate subgraphs) (v3.0.0-preview.0-nightly.b135f054)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 189021     ✗ 0    
     data_received..................: 5.5 GB  45 MB/s
     data_sent......................: 76 MB   620 kB/s
     http_req_blocked...............: avg=4.42µs  min=1.02µs  med=2.77µs  max=3.5ms    p(90)=4.23µs   p(95)=4.8µs    p(99.9)=42.35µs 
     http_req_connecting............: avg=1.4µs   min=0s      med=0s      max=3.47ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=94.87ms min=20.18ms med=93.39ms max=303.05ms p(90)=118.24ms p(95)=126.18ms p(99.9)=165.63ms
       { expected_response:true }...: avg=94.87ms min=20.18ms med=93.39ms max=303.05ms p(90)=118.24ms p(95)=126.18ms p(99.9)=165.63ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63107
     http_req_receiving.............: avg=77.22µs min=27.63µs med=68.34µs max=112.01ms p(90)=101.84µs p(95)=114.42µs p(99.9)=475.97µs
     http_req_sending...............: avg=23.57µs min=4.84µs  med=13.78µs max=133.13ms p(90)=20.09µs  p(95)=22.25µs  p(99.9)=518.47µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.77ms min=19.84ms med=93.3ms  max=302.45ms p(90)=118.15ms p(95)=126.08ms p(99.9)=164.98ms
     http_reqs......................: 63107   516.358009/s
     iteration_duration.............: avg=95.23ms min=35.15ms med=93.65ms max=329.26ms p(90)=118.5ms  p(95)=126.43ms p(99.9)=167.45ms
     iterations.....................: 63007   515.539782/s
     success_rate...................: 100.00% ✓ 63007      ✗ 0    
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

     checks.........................: 100.00% ✓ 179508     ✗ 0    
     data_received..................: 5.2 GB  43 MB/s
     data_sent......................: 72 MB   589 kB/s
     http_req_blocked...............: avg=4.27µs   min=1.01µs  med=2.59µs  max=4.15ms   p(90)=4.03µs   p(95)=4.58µs   p(99.9)=54.61µs 
     http_req_connecting............: avg=1.38µs   min=0s      med=0s      max=3.92ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=99.92ms  min=19.84ms med=98.17ms max=311.74ms p(90)=126.6ms  p(95)=135.57ms p(99.9)=173.33ms
       { expected_response:true }...: avg=99.92ms  min=19.84ms med=98.17ms max=311.74ms p(90)=126.6ms  p(95)=135.57ms p(99.9)=173.33ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 59936
     http_req_receiving.............: avg=78.77µs  min=27.41µs med=71.45µs max=97.54ms  p(90)=103.39µs p(95)=115.52µs p(99.9)=488.11µs
     http_req_sending...............: avg=22.18µs  min=4.54µs  med=13.25µs max=137.85ms p(90)=18.92µs  p(95)=20.84µs  p(99.9)=416.92µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=99.82ms  min=19.72ms med=98.07ms max=311.5ms  p(90)=126.5ms  p(95)=135.47ms p(99.9)=172.82ms
     http_reqs......................: 59936   490.447126/s
     iteration_duration.............: avg=100.29ms min=31.8ms  med=98.44ms max=325.36ms p(90)=126.84ms p(95)=135.81ms p(99.9)=174.32ms
     iterations.....................: 59836   489.628842/s
     success_rate...................: 100.00% ✓ 59836      ✗ 0    
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

     checks.........................: 100.00% ✓ 142248     ✗ 0    
     data_received..................: 4.2 GB  34 MB/s
     data_sent......................: 57 MB   466 kB/s
     http_req_blocked...............: avg=4.29µs   min=982ns   med=2.68µs  max=3.07ms   p(90)=4.02µs   p(95)=4.55µs   p(99.9)=213.87µs
     http_req_connecting............: avg=1.35µs   min=0s      med=0s      max=2.98ms   p(90)=0s       p(95)=0s       p(99.9)=144.12µs
     http_req_duration..............: avg=126.09ms min=21.03ms med=124.4ms max=339.54ms p(90)=156.37ms p(95)=166.97ms p(99.9)=211.98ms
       { expected_response:true }...: avg=126.09ms min=21.03ms med=124.4ms max=339.54ms p(90)=156.37ms p(95)=166.97ms p(99.9)=211.98ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 47516
     http_req_receiving.............: avg=76.84µs  min=28.73µs med=68.98µs max=108.64ms p(90)=101.46µs p(95)=113.59µs p(99.9)=477.93µs
     http_req_sending...............: avg=24.14µs  min=5.22µs  med=13.69µs max=152.7ms  p(90)=19.35µs  p(95)=21.2µs   p(99.9)=580.77µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=125.99ms min=20.91ms med=124.3ms max=337.42ms p(90)=156.26ms p(95)=166.84ms p(99.9)=211.19ms
     http_reqs......................: 47516   388.405446/s
     iteration_duration.............: avg=126.56ms min=37.35ms med=124.7ms max=349.5ms  p(90)=156.65ms p(95)=167.27ms p(99.9)=214.5ms 
     iterations.....................: 47416   387.588026/s
     success_rate...................: 100.00% ✓ 47416      ✗ 0    
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

     checks.........................: 100.00% ✓ 106899     ✗ 0    
     data_received..................: 3.1 GB  26 MB/s
     data_sent......................: 43 MB   351 kB/s
     http_req_blocked...............: avg=6.31µs   min=1.31µs  med=3.64µs   max=3.55ms   p(90)=5.16µs   p(95)=5.81µs   p(99.9)=1.02ms  
     http_req_connecting............: avg=2.4µs    min=0s      med=0s       max=3.51ms   p(90)=0s       p(95)=0s       p(99.9)=994.44µs
     http_req_duration..............: avg=167.79ms min=17.08ms med=154.68ms max=738.9ms  p(90)=186.05ms p(95)=202.66ms p(99.9)=680.36ms
       { expected_response:true }...: avg=167.79ms min=17.08ms med=154.68ms max=738.9ms  p(90)=186.05ms p(95)=202.66ms p(99.9)=680.36ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 35733
     http_req_receiving.............: avg=97.98µs  min=35.38µs med=89.12µs  max=88.51ms  p(90)=119.78µs p(95)=132.17µs p(99.9)=564.87µs
     http_req_sending...............: avg=32.07µs  min=5.98µs  med=17.59µs  max=117.43ms p(90)=22.41µs  p(95)=24.31µs  p(99.9)=502.85µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=167.66ms min=16.94ms med=154.57ms max=738.77ms p(90)=185.89ms p(95)=202.45ms p(99.9)=680.27ms
     http_reqs......................: 35733   292.324605/s
     iteration_duration.............: avg=168.51ms min=45.47ms med=155.02ms max=739.17ms p(90)=186.34ms p(95)=203.13ms p(99.9)=680.62ms
     iterations.....................: 35633   291.506525/s
     success_rate...................: 100.00% ✓ 35633      ✗ 0    
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

     checks.........................: 100.00% ✓ 98601      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   323 kB/s
     http_req_blocked...............: avg=11.49µs  min=1.07µs  med=2.99µs   max=8.78ms   p(90)=4.3µs    p(95)=4.83µs   p(99.9)=4.9ms   
     http_req_connecting............: avg=8.18µs   min=0s      med=0s       max=8.73ms   p(90)=0s       p(95)=0s       p(99.9)=4.86ms  
     http_req_duration..............: avg=181.86ms min=22.96ms med=181.8ms  max=375.62ms p(90)=195.27ms p(95)=200.02ms p(99.9)=265.4ms 
       { expected_response:true }...: avg=181.86ms min=22.96ms med=181.8ms  max=375.62ms p(90)=195.27ms p(95)=200.02ms p(99.9)=265.4ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 32967
     http_req_receiving.............: avg=90.87µs  min=33.75µs med=84.59µs  max=53.11ms  p(90)=114.37µs p(95)=125.98µs p(99.9)=530.61µs
     http_req_sending...............: avg=30.58µs  min=4.89µs  med=15.42µs  max=90.97ms  p(90)=19.63µs  p(95)=21.53µs  p(99.9)=507.66µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=181.73ms min=22.79ms med=181.7ms  max=375.1ms  p(90)=195.17ms p(95)=199.91ms p(99.9)=265.28ms
     http_reqs......................: 32967   269.019064/s
     iteration_duration.............: avg=182.63ms min=54.82ms med=182.11ms max=387.35ms p(90)=195.54ms p(95)=200.35ms p(99.9)=271.6ms 
     iterations.....................: 32867   268.203039/s
     success_rate...................: 100.00% ✓ 32867      ✗ 0    
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

