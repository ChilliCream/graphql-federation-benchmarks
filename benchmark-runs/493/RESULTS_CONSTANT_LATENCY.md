## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-aot-11 | 16.8.0-p.17 | 3,609 | 3,636 | 3,587 | 0.6% | 112 MB | 31.7 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.17 | 3,602 | 3,616 | 3,577 | 0.4% | 363 MB | 103.2 KB |  |
| fusion-net-11 | 16.7.7 | 3,584 | 3,595 | 3,569 | 0.3% | 358 MB | 102.2 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 3,582 | 3,593 | 3,570 | 0.2% | 113 MB | 32.4 KB |  |
| fusion-aot-11 | 16.7.7 | 3,579 | 3,591 | 3,565 | 0.3% | 118 MB | 33.9 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.17 | 3,556 | 3,567 | 3,543 | 0.3% | 367 MB | 105.7 KB |  |
| fusion-fed-net-11 | 16.7.7 | 3,540 | 3,552 | 3,532 | 0.2% | 371 MB | 107.4 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.17 | 3,524 | 3,540 | 3,517 | 0.3% | 119 MB | 34.6 KB |  |
| feddi-gateway | 2026-11-03-0517 | 3,458 | 3,480 | 3,446 | 0.4% | 2,296 MB | 679.9 KB |  |
| hive-router | v0.3.17 | 3,392 | 3,396 | 3,369 | 0.3% | 93 MB | 28.0 KB |  |
| hive-router-nightly | v0.3.19-nightly.9815b25d | 3,342 | 3,348 | 3,330 | 0.2% | 91 MB | 27.9 KB |  |
| caliban | 3.2.1 | 1,544 | 1,546 | 1,540 | 0.1% | 5,525 MB | 3,664.1 KB |  |
| grafbase | 0.53.5 | 1,444 | 1,458 | 1,441 | 0.5% | 99 MB | 70.4 KB |  |
| cosmo | 0.373.0 | 1,436 | 1,439 | 1,434 | 0.1% | 150 MB | 107.1 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 589 | 589 | 589 | 0.0% | 2,604 MB | 4,526.5 KB |  |
| apollo-router | v2.19.1 | 488 | 494 | 487 | 0.6% | 180 MB | 377.7 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.a909a280 | 471 | 471 | 470 | 0.1% | 200 MB | 434.3 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 389 | 390 | 389 | 0.1% | 203 MB | 534.5 KB |  |
| hive-gateway | 2.15.10 | 287 | 290 | 286 | 0.7% | 3,262 MB | 11,637.9 KB |  |
| apollo-gateway | 2.14.4 | 273 | 273 | 272 | 0.2% | 2,141 MB | 8,029.7 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1309314     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 525 MB  4.3 MB/s
     http_req_blocked...............: avg=2.83µs  min=822ns   med=2.23µs  max=3.92ms   p(90)=3.56µs  p(95)=4.3µs    p(99.9)=32.72µs
     http_req_connecting............: avg=223ns   min=0s      med=0s      max=3.87ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.54ms min=8.11ms  med=13.09ms max=282.42ms p(90)=16.64ms p(95)=17.95ms  p(99.9)=26.11ms
       { expected_response:true }...: avg=13.54ms min=8.11ms  med=13.09ms max=282.42ms p(90)=16.64ms p(95)=17.95ms  p(99.9)=26.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 436538
     http_req_receiving.............: avg=72.85µs min=24.73µs med=46.09µs max=28.92ms  p(90)=95.42µs p(95)=189.51µs p(99.9)=1.85ms 
     http_req_sending...............: avg=33.07µs min=4.24µs  med=8.3µs   max=159.82ms p(90)=16.86µs p(95)=101.52µs p(99.9)=1.8ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.43ms min=8.05ms  med=12.99ms max=282.21ms p(90)=16.52ms p(95)=17.81ms  p(99.9)=25.8ms 
     http_reqs......................: 436538  3609.154631/s
     iteration_duration.............: avg=13.73ms min=8.28ms  med=13.29ms max=296.06ms p(90)=16.83ms p(95)=18.14ms  p(99.9)=26.33ms
     iterations.....................: 436438  3608.327864/s
     success_rate...................: 100.00% ✓ 436438      ✗ 0     
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

     checks.........................: 100.00% ✓ 1306758     ✗ 0     
     data_received..................: 38 GB   315 MB/s
     data_sent......................: 524 MB  4.3 MB/s
     http_req_blocked...............: avg=2.4µs   min=791ns   med=1.83µs  max=3.63ms   p(90)=3.07µs  p(95)=3.84µs   p(99.9)=23.99µs
     http_req_connecting............: avg=223ns   min=0s      med=0s      max=3.6ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.57ms min=8.19ms  med=13.17ms max=262.65ms p(90)=16.66ms p(95)=17.89ms  p(99.9)=25.13ms
       { expected_response:true }...: avg=13.57ms min=8.19ms  med=13.17ms max=262.65ms p(90)=16.66ms p(95)=17.89ms  p(99.9)=25.13ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 435686
     http_req_receiving.............: avg=67.81µs min=23.34µs med=42.38µs max=127.94ms p(90)=91.94µs p(95)=169.47µs p(99.9)=1.79ms 
     http_req_sending...............: avg=30.98µs min=4.21µs  med=7.84µs  max=185.27ms p(90)=16.41µs p(95)=91.82µs  p(99.9)=1.63ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.47ms min=8.14ms  med=13.07ms max=262.28ms p(90)=16.56ms p(95)=17.77ms  p(99.9)=24.88ms
     http_reqs......................: 435686  3602.060597/s
     iteration_duration.............: avg=13.76ms min=8.34ms  med=13.36ms max=292.15ms p(90)=16.85ms p(95)=18.07ms  p(99.9)=25.35ms
     iterations.....................: 435586  3601.233841/s
     success_rate...................: 100.00% ✓ 435586      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1300284     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 521 MB  4.3 MB/s
     http_req_blocked...............: avg=2.83µs  min=932ns   med=2.28µs  max=4.21ms   p(90)=3.59µs  p(95)=4.33µs   p(99.9)=28.39µs
     http_req_connecting............: avg=221ns   min=0s      med=0s      max=4.17ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.63ms min=8.13ms  med=13.19ms max=270.37ms p(90)=16.86ms p(95)=18.17ms  p(99.9)=26.05ms
       { expected_response:true }...: avg=13.63ms min=8.13ms  med=13.19ms max=270.37ms p(90)=16.86ms p(95)=18.17ms  p(99.9)=26.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 433528
     http_req_receiving.............: avg=71.54µs min=24.47µs med=44.85µs max=88.43ms  p(90)=93.01µs p(95)=181.83µs p(99.9)=2ms    
     http_req_sending...............: avg=33.7µs  min=4.34µs  med=8.54µs  max=185.46ms p(90)=16.35µs p(95)=99.76µs  p(99.9)=1.95ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.53ms min=8.07ms  med=13.09ms max=269.92ms p(90)=16.74ms p(95)=18.03ms  p(99.9)=25.81ms
     http_reqs......................: 433528  3584.413171/s
     iteration_duration.............: avg=13.83ms min=8.3ms   med=13.38ms max=287.32ms p(90)=17.05ms p(95)=18.37ms  p(99.9)=26.29ms
     iterations.....................: 433428  3583.586371/s
     success_rate...................: 100.00% ✓ 433428      ✗ 0     
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

     checks.........................: 100.00% ✓ 1299822     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 521 MB  4.3 MB/s
     http_req_blocked...............: avg=2.48µs  min=821ns   med=1.93µs  max=4.03ms   p(90)=3.14µs  p(95)=3.89µs   p(99.9)=25.76µs
     http_req_connecting............: avg=209ns   min=0s      med=0s      max=3.98ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.64ms min=8.16ms  med=13.23ms max=257.85ms p(90)=16.67ms p(95)=17.9ms   p(99.9)=25.27ms
       { expected_response:true }...: avg=13.64ms min=8.16ms  med=13.23ms max=257.85ms p(90)=16.67ms p(95)=17.9ms   p(99.9)=25.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 433374
     http_req_receiving.............: avg=70.27µs min=24.17µs med=46.08µs max=159.57ms p(90)=93.36µs p(95)=171.67µs p(99.9)=1.69ms 
     http_req_sending...............: avg=31.57µs min=4.07µs  med=8.18µs  max=161.32ms p(90)=16.15µs p(95)=94.37µs  p(99.9)=1.66ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.54ms min=8.11ms  med=13.13ms max=257.79ms p(90)=16.56ms p(95)=17.78ms  p(99.9)=25.01ms
     http_reqs......................: 433374  3582.84064/s
     iteration_duration.............: avg=13.83ms min=8.29ms  med=13.42ms max=295.51ms p(90)=16.86ms p(95)=18.09ms  p(99.9)=25.54ms
     iterations.....................: 433274  3582.013908/s
     success_rate...................: 100.00% ✓ 433274      ✗ 0     
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

     checks.........................: 100.00% ✓ 1298706     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 520 MB  4.3 MB/s
     http_req_blocked...............: avg=2.65µs  min=811ns   med=2.11µs  max=3.92ms   p(90)=3.34µs  p(95)=3.98µs   p(99.9)=27.78µs
     http_req_connecting............: avg=227ns   min=0s      med=0s      max=3.88ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.65ms min=8.26ms  med=13.24ms max=207.98ms p(90)=16.75ms p(95)=18.03ms  p(99.9)=25.56ms
       { expected_response:true }...: avg=13.65ms min=8.26ms  med=13.24ms max=207.98ms p(90)=16.75ms p(95)=18.03ms  p(99.9)=25.56ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 433002
     http_req_receiving.............: avg=71.36µs min=25.14µs med=46.13µs max=63.65ms  p(90)=93.41µs p(95)=181.79µs p(99.9)=1.73ms 
     http_req_sending...............: avg=32.15µs min=4.23µs  med=8.31µs  max=64.21ms  p(90)=16.3µs  p(95)=99.14µs  p(99.9)=1.73ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.55ms min=8.21ms  med=13.14ms max=207.68ms p(90)=16.64ms p(95)=17.9ms   p(99.9)=25.35ms
     http_reqs......................: 433002  3579.72326/s
     iteration_duration.............: avg=13.85ms min=8.42ms  med=13.43ms max=339.84ms p(90)=16.94ms p(95)=18.22ms  p(99.9)=25.8ms 
     iterations.....................: 432902  3578.896537/s
     success_rate...................: 100.00% ✓ 432902      ✗ 0     
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

     checks.........................: 100.00% ✓ 1290255     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.39µs  min=782ns   med=1.83µs  max=4.05ms   p(90)=2.99µs  p(95)=3.73µs   p(99.9)=23.82µs
     http_req_connecting............: avg=215ns   min=0s      med=0s      max=4.01ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.75ms min=8.17ms  med=13.35ms max=267.76ms p(90)=16.87ms p(95)=18.1ms   p(99.9)=25.13ms
       { expected_response:true }...: avg=13.75ms min=8.17ms  med=13.35ms max=267.76ms p(90)=16.87ms p(95)=18.1ms   p(99.9)=25.13ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 430185
     http_req_receiving.............: avg=67.57µs min=23.53µs med=43.11µs max=145.01ms p(90)=92.15µs p(95)=169.83µs p(99.9)=1.57ms 
     http_req_sending...............: avg=31.89µs min=4.23µs  med=7.81µs  max=156.68ms p(90)=16.31µs p(95)=93.41µs  p(99.9)=1.76ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.65ms min=8.12ms  med=13.26ms max=267.21ms p(90)=16.77ms p(95)=17.99ms  p(99.9)=24.94ms
     http_reqs......................: 430185  3556.64903/s
     iteration_duration.............: avg=13.94ms min=8.32ms  med=13.54ms max=284.61ms p(90)=17.06ms p(95)=18.29ms  p(99.9)=25.37ms
     iterations.....................: 430085  3555.822258/s
     success_rate...................: 100.00% ✓ 430085      ✗ 0     
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

     checks.........................: 100.00% ✓ 1284288     ✗ 0     
     data_received..................: 38 GB   310 MB/s
     data_sent......................: 515 MB  4.3 MB/s
     http_req_blocked...............: avg=2.76µs  min=782ns   med=1.84µs  max=9.12ms   p(90)=3µs     p(95)=3.67µs   p(99.9)=25.85µs
     http_req_connecting............: avg=569ns   min=0s      med=0s      max=9.08ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.81ms min=7.93ms  med=13.42ms max=274.17ms p(90)=16.94ms p(95)=18.19ms  p(99.9)=25.91ms
       { expected_response:true }...: avg=13.81ms min=7.93ms  med=13.42ms max=274.17ms p(90)=16.94ms p(95)=18.19ms  p(99.9)=25.91ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 428196
     http_req_receiving.............: avg=68.85µs min=24.57µs med=43.98µs max=123.71ms p(90)=90.63µs p(95)=166.76µs p(99.9)=1.83ms 
     http_req_sending...............: avg=30.95µs min=4.19µs  med=7.89µs  max=59.37ms  p(90)=15.67µs p(95)=91.97µs  p(99.9)=1.85ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.71ms min=7.88ms  med=13.32ms max=273.42ms p(90)=16.84ms p(95)=18.07ms  p(99.9)=25.63ms
     http_reqs......................: 428196  3540.233884/s
     iteration_duration.............: avg=14ms    min=8.06ms  med=13.61ms max=285.66ms p(90)=17.13ms p(95)=18.38ms  p(99.9)=26.14ms
     iterations.....................: 428096  3539.407105/s
     success_rate...................: 100.00% ✓ 428096      ✗ 0     
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

     checks.........................: 100.00% ✓ 1278528     ✗ 0     
     data_received..................: 37 GB   308 MB/s
     data_sent......................: 512 MB  4.2 MB/s
     http_req_blocked...............: avg=2.9µs   min=882ns   med=2.32µs  max=4.06ms   p(90)=3.74µs  p(95)=4.49µs   p(99.9)=31.97µs
     http_req_connecting............: avg=215ns   min=0s      med=0s      max=4ms      p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.86ms min=8.18ms  med=13.43ms max=288.4ms  p(90)=17.07ms p(95)=18.37ms  p(99.9)=26ms   
       { expected_response:true }...: avg=13.86ms min=8.18ms  med=13.43ms max=288.4ms  p(90)=17.07ms p(95)=18.37ms  p(99.9)=26ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 426276
     http_req_receiving.............: avg=71.96µs min=23.93µs med=44.74µs max=150.47ms p(90)=95.03µs p(95)=185.66µs p(99.9)=1.85ms 
     http_req_sending...............: avg=34.44µs min=4.38µs  med=8.71µs  max=135.12ms p(90)=17.58µs p(95)=101.82µs p(99.9)=1.9ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.76ms min=8.14ms  med=13.33ms max=288.23ms p(90)=16.95ms p(95)=18.24ms  p(99.9)=25.81ms
     http_reqs......................: 426276  3524.217644/s
     iteration_duration.............: avg=14.06ms min=8.36ms  med=13.63ms max=302.45ms p(90)=17.27ms p(95)=18.57ms  p(99.9)=26.22ms
     iterations.....................: 426176  3523.390899/s
     success_rate...................: 100.00% ✓ 426176      ✗ 0     
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

     checks.........................: 100.00% ✓ 1254603     ✗ 0     
     data_received..................: 37 GB   302 MB/s
     data_sent......................: 503 MB  4.2 MB/s
     http_req_blocked...............: avg=3.31µs  min=911ns   med=2.33µs  max=9.55ms   p(90)=3.68µs  p(95)=4.4µs    p(99.9)=29.9µs 
     http_req_connecting............: avg=607ns   min=0s      med=0s      max=9.08ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.14ms min=8.24ms  med=13.77ms max=314.87ms p(90)=17.17ms p(95)=18.38ms  p(99.9)=26.21ms
       { expected_response:true }...: avg=14.14ms min=8.24ms  med=13.77ms max=314.87ms p(90)=17.17ms p(95)=18.38ms  p(99.9)=26.21ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 418301
     http_req_receiving.............: avg=69.71µs min=24.07µs med=45.06µs max=54.52ms  p(90)=90.15µs p(95)=175.01µs p(99.9)=1.68ms 
     http_req_sending...............: avg=33.11µs min=4.37µs  med=8.58µs  max=274.44ms p(90)=16.2µs  p(95)=98.55µs  p(99.9)=1.8ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.04ms min=8.19ms  med=13.67ms max=314.5ms  p(90)=17.06ms p(95)=18.26ms  p(99.9)=25.96ms
     http_reqs......................: 418301  3458.183687/s
     iteration_duration.............: avg=14.33ms min=8.43ms  med=13.96ms max=329.25ms p(90)=17.35ms p(95)=18.58ms  p(99.9)=26.44ms
     iterations.....................: 418201  3457.356966/s
     success_rate...................: 100.00% ✓ 418201      ✗ 0     
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

     checks.........................: 100.00% ✓ 1230717     ✗ 0     
     data_received..................: 36 GB   297 MB/s
     data_sent......................: 493 MB  4.1 MB/s
     http_req_blocked...............: avg=2.59µs  min=812ns  med=1.95µs  max=4.77ms   p(90)=3.44µs  p(95)=4.42µs   p(99.9)=25.7µs 
     http_req_connecting............: avg=236ns   min=0s     med=0s      max=3.68ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.42ms min=8.38ms med=14.06ms max=283.4ms  p(90)=17.43ms p(95)=18.66ms  p(99.9)=26.06ms
       { expected_response:true }...: avg=14.42ms min=8.38ms med=14.06ms max=283.4ms  p(90)=17.43ms p(95)=18.66ms  p(99.9)=26.06ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 410339
     http_req_receiving.............: avg=69.82µs min=22.6µs med=44.58µs max=149.6ms  p(90)=98.44µs p(95)=173.36µs p(99.9)=1.62ms 
     http_req_sending...............: avg=31.45µs min=4.28µs med=8.25µs  max=189.23ms p(90)=18.76µs p(95)=94.83µs  p(99.9)=1.7ms  
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.32ms min=8.34ms med=13.96ms max=283.01ms p(90)=17.32ms p(95)=18.54ms  p(99.9)=25.83ms
     http_reqs......................: 410339  3392.159608/s
     iteration_duration.............: avg=14.61ms min=8.5ms  med=14.25ms max=301.07ms p(90)=17.62ms p(95)=18.85ms  p(99.9)=26.29ms
     iterations.....................: 410239  3391.332935/s
     success_rate...................: 100.00% ✓ 410239      ✗ 0     
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

     checks.........................: 100.00% ✓ 1212825     ✗ 0     
     data_received..................: 35 GB   292 MB/s
     data_sent......................: 486 MB  4.0 MB/s
     http_req_blocked...............: avg=3.11µs  min=952ns  med=2.49µs  max=4.21ms   p(90)=4.05µs   p(95)=4.89µs   p(99.9)=34.12µs
     http_req_connecting............: avg=238ns   min=0s     med=0s      max=4.16ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.62ms min=8.63ms med=14.23ms max=283.78ms p(90)=17.88ms  p(95)=19.2ms   p(99.9)=27.32ms
       { expected_response:true }...: avg=14.62ms min=8.63ms med=14.23ms max=283.78ms p(90)=17.88ms  p(95)=19.2ms   p(99.9)=27.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 404375
     http_req_receiving.............: avg=77.81µs min=24.1µs med=48.38µs max=179.29ms p(90)=103.47µs p(95)=193.89µs p(99.9)=2.01ms 
     http_req_sending...............: avg=34.87µs min=4.62µs med=9.23µs  max=57.79ms  p(90)=18.96µs  p(95)=106.63µs p(99.9)=1.97ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.51ms min=8.57ms med=14.12ms max=283.48ms p(90)=17.75ms  p(95)=19.06ms  p(99.9)=27.05ms
     http_reqs......................: 404375  3342.702614/s
     iteration_duration.............: avg=14.83ms min=8.75ms med=14.43ms max=294.27ms p(90)=18.07ms  p(95)=19.4ms   p(99.9)=27.56ms
     iterations.....................: 404275  3341.875979/s
     success_rate...................: 100.00% ✓ 404275      ✗ 0     
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

     checks.........................: 100.00% ✓ 564663      ✗ 0     
     data_received..................: 17 GB   135 MB/s
     data_sent......................: 226 MB  1.9 MB/s
     http_req_blocked...............: avg=3.91µs  min=1µs     med=3.17µs  max=2.95ms   p(90)=5.22µs   p(95)=6.13µs   p(99.9)=37.62µs 
     http_req_connecting............: avg=363ns   min=0s      med=0s      max=2.9ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=31.62ms min=17.83ms med=31.16ms max=275.79ms p(90)=36.58ms  p(95)=38.51ms  p(99.9)=50.82ms 
       { expected_response:true }...: avg=31.62ms min=17.83ms med=31.16ms max=275.79ms p(90)=36.58ms  p(95)=38.51ms  p(99.9)=50.82ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 188321
     http_req_receiving.............: avg=83.33µs min=27.82µs med=66.43µs max=209.07ms p(90)=111.14µs p(95)=134.19µs p(99.9)=1.01ms  
     http_req_sending...............: avg=27.88µs min=4.97µs  med=13.23µs max=240.55ms p(90)=21.64µs  p(95)=26.56µs  p(99.9)=883.09µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=31.51ms min=17.73ms med=31.05ms max=275.21ms p(90)=36.47ms  p(95)=38.4ms   p(99.9)=50.67ms 
     http_reqs......................: 188321  1544.19738/s
     iteration_duration.............: avg=31.86ms min=20.71ms med=31.39ms max=308.8ms  p(90)=36.81ms  p(95)=38.74ms  p(99.9)=51.12ms 
     iterations.....................: 188221  1543.377399/s
     success_rate...................: 100.00% ✓ 188221      ✗ 0     
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

     checks.........................: 100.00% ✓ 528318      ✗ 0     
     data_received..................: 15 GB   127 MB/s
     data_sent......................: 212 MB  1.7 MB/s
     http_req_blocked...............: avg=3.24µs  min=811ns   med=2.16µs  max=3.61ms   p(90)=4.53µs   p(95)=5.5µs    p(99.9)=37.41µs
     http_req_connecting............: avg=533ns   min=0s      med=0s      max=3.56ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.81ms min=17.63ms med=33.51ms max=316.22ms p(90)=39.46ms  p(95)=41.17ms  p(99.9)=50.17ms
       { expected_response:true }...: avg=33.81ms min=17.63ms med=33.51ms max=316.22ms p(90)=39.46ms  p(95)=41.17ms  p(99.9)=50.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 176206
     http_req_receiving.............: avg=79.49µs min=25.98µs med=54.59µs max=103.73ms p(90)=117.62µs p(95)=158.36µs p(99.9)=1.3ms  
     http_req_sending...............: avg=27.54µs min=4.25µs  med=9.07µs  max=140.21ms p(90)=22.13µs  p(95)=35.58µs  p(99.9)=1.16ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.7ms  min=17.51ms med=33.41ms max=296.5ms  p(90)=39.36ms  p(95)=41.06ms  p(99.9)=49.89ms
     http_reqs......................: 176206  1444.968667/s
     iteration_duration.............: avg=34.06ms min=21.28ms med=33.75ms max=323.3ms  p(90)=39.68ms  p(95)=41.38ms  p(99.9)=50.48ms
     iterations.....................: 176106  1444.148622/s
     success_rate...................: 100.00% ✓ 176106      ✗ 0     
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

     checks.........................: 100.00% ✓ 525270      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 211 MB  1.7 MB/s
     http_req_blocked...............: avg=2.97µs  min=811ns   med=2.11µs  max=3.95ms   p(90)=3.7µs   p(95)=4.43µs   p(99.9)=31.55µs 
     http_req_connecting............: avg=527ns   min=0s      med=0s      max=3.92ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.05ms min=17.99ms med=33.49ms max=313.1ms  p(90)=40.59ms p(95)=42.88ms  p(99.9)=54.94ms 
       { expected_response:true }...: avg=34.05ms min=17.99ms med=33.49ms max=313.1ms  p(90)=40.59ms p(95)=42.88ms  p(99.9)=54.94ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 175190
     http_req_receiving.............: avg=69.97µs min=24.89µs med=56.9µs  max=80.88ms  p(90)=95.97µs p(95)=113.49µs p(99.9)=707.04µs
     http_req_sending...............: avg=20.66µs min=4.48µs  med=9.84µs  max=108.16ms p(90)=16.95µs p(95)=20.77µs  p(99.9)=746.86µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.96ms min=17.86ms med=33.4ms  max=272.39ms p(90)=40.5ms  p(95)=42.8ms   p(99.9)=54.75ms 
     http_reqs......................: 175190  1436.321514/s
     iteration_duration.............: avg=34.26ms min=20.1ms  med=33.68ms max=321.57ms p(90)=40.79ms p(95)=43.07ms  p(99.9)=55.26ms 
     iterations.....................: 175090  1435.501649/s
     success_rate...................: 100.00% ✓ 175090      ✗ 0     
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

     checks.........................: 100.00% ✓ 215934     ✗ 0    
     data_received..................: 6.3 GB  52 MB/s
     data_sent......................: 87 MB   708 kB/s
     http_req_blocked...............: avg=3.51µs  min=981ns   med=2.7µs   max=2.11ms   p(90)=4.19µs   p(95)=4.78µs   p(99.9)=44.1µs  
     http_req_connecting............: avg=582ns   min=0s      med=0s      max=2.07ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=83.05ms min=20.44ms med=81.03ms max=320.18ms p(90)=97.75ms  p(95)=106.87ms p(99.9)=201.53ms
       { expected_response:true }...: avg=83.05ms min=20.44ms med=81.03ms max=320.18ms p(90)=97.75ms  p(95)=106.87ms p(99.9)=201.53ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 72078
     http_req_receiving.............: avg=77.54µs min=27.02µs med=68.35µs max=74.87ms  p(90)=102.41µs p(95)=115.05µs p(99.9)=533.15µs
     http_req_sending...............: avg=20.65µs min=5.06µs  med=13.72µs max=140.09ms p(90)=19.54µs  p(95)=21.49µs  p(99.9)=545.57µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=82.95ms min=20.37ms med=80.94ms max=319.66ms p(90)=97.65ms  p(95)=106.75ms p(99.9)=201.42ms
     http_reqs......................: 72078   589.860694/s
     iteration_duration.............: avg=83.37ms min=33.75ms med=81.28ms max=329.46ms p(90)=97.98ms  p(95)=107.17ms p(99.9)=203.35ms
     iterations.....................: 71978   589.04233/s
     success_rate...................: 100.00% ✓ 71978      ✗ 0    
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

     checks.........................: 100.00% ✓ 178740     ✗ 0    
     data_received..................: 5.2 GB  43 MB/s
     data_sent......................: 72 MB   587 kB/s
     http_req_blocked...............: avg=5.16µs   min=1.2µs   med=3.06µs  max=4.16ms   p(90)=4.51µs   p(95)=5.09µs   p(99.9)=54.55µs 
     http_req_connecting............: avg=1.87µs   min=0s      med=0s      max=3.91ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=100.33ms min=20.08ms med=98.46ms max=321.19ms p(90)=126.89ms p(95)=136.07ms p(99.9)=176.88ms
       { expected_response:true }...: avg=100.33ms min=20.08ms med=98.46ms max=321.19ms p(90)=126.89ms p(95)=136.07ms p(99.9)=176.88ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 59680
     http_req_receiving.............: avg=80.17µs  min=29.16µs med=70.51µs max=143.51ms p(90)=103.04µs p(95)=115.41µs p(99.9)=518.78µs
     http_req_sending...............: avg=22.85µs  min=5.23µs  med=14.02µs max=101.38ms p(90)=19.72µs  p(95)=21.86µs  p(99.9)=552.62µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=100.23ms min=19.83ms med=98.37ms max=320.3ms  p(90)=126.8ms  p(95)=135.96ms p(99.9)=176.77ms
     http_reqs......................: 59680   488.409026/s
     iteration_duration.............: avg=100.72ms min=25.71ms med=98.74ms max=345.01ms p(90)=127.15ms p(95)=136.34ms p(99.9)=178.05ms
     iterations.....................: 59580   487.590646/s
     success_rate...................: 100.00% ✓ 59580      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-nightly (HotChocolate subgraphs) (v3.0.0-preview.0-nightly.a909a280)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 172506     ✗ 0    
     data_received..................: 5.0 GB  41 MB/s
     data_sent......................: 69 MB   566 kB/s
     http_req_blocked...............: avg=4.07µs   min=1.11µs  med=3.09µs   max=3.34ms   p(90)=4.52µs   p(95)=5.11µs   p(99.9)=69.08µs 
     http_req_connecting............: avg=714ns    min=0s      med=0s       max=1.91ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=103.96ms min=20.06ms med=102.36ms max=319.05ms p(90)=130.39ms p(95)=139.65ms p(99.9)=180.88ms
       { expected_response:true }...: avg=103.96ms min=20.06ms med=102.36ms max=319.05ms p(90)=130.39ms p(95)=139.65ms p(99.9)=180.88ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 57602
     http_req_receiving.............: avg=82.03µs  min=29.69µs med=71.97µs  max=116.22ms p(90)=104.57µs p(95)=116.7µs  p(99.9)=487.65µs
     http_req_sending...............: avg=19.59µs  min=5.38µs  med=14.27µs  max=51.15ms  p(90)=20.15µs  p(95)=22.2µs   p(99.9)=514.93µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=103.86ms min=19.99ms med=102.27ms max=318.75ms p(90)=130.31ms p(95)=139.56ms p(99.9)=180.8ms 
     http_reqs......................: 57602   471.256505/s
     iteration_duration.............: avg=104.36ms min=34.61ms med=102.65ms max=328.47ms p(90)=130.65ms p(95)=139.92ms p(99.9)=182.83ms
     iterations.....................: 57502   470.43838/s
     success_rate...................: 100.00% ✓ 57502      ✗ 0    
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

     checks.........................: 100.00% ✓ 142569     ✗ 0    
     data_received..................: 4.2 GB  34 MB/s
     data_sent......................: 57 MB   467 kB/s
     http_req_blocked...............: avg=6.78µs   min=1.06µs  med=2.9µs    max=7.41ms   p(90)=4.29µs   p(95)=4.8µs    p(99.9)=202.81µs
     http_req_connecting............: avg=3.62µs   min=0s      med=0s       max=7.29ms   p(90)=0s       p(95)=0s       p(99.9)=111.61µs
     http_req_duration..............: avg=125.82ms min=20.94ms med=124.04ms max=318.33ms p(90)=156.27ms p(95)=166.83ms p(99.9)=214.34ms
       { expected_response:true }...: avg=125.82ms min=20.94ms med=124.04ms max=318.33ms p(90)=156.27ms p(95)=166.83ms p(99.9)=214.34ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 47623
     http_req_receiving.............: avg=80.68µs  min=28.14µs med=75.78µs  max=57.09ms  p(90)=105.52µs p(95)=116.99µs p(99.9)=475.93µs
     http_req_sending...............: avg=33.82µs  min=5.03µs  med=14.67µs  max=202.68ms p(90)=19.54µs  p(95)=21.26µs  p(99.9)=997.69µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=125.71ms min=20.84ms med=123.94ms max=316.39ms p(90)=156.15ms p(95)=166.66ms p(99.9)=213.07ms
     http_reqs......................: 47623   389.272821/s
     iteration_duration.............: avg=126.29ms min=42.57ms med=124.34ms max=331.71ms p(90)=156.57ms p(95)=167.12ms p(99.9)=215.71ms
     iterations.....................: 47523   388.455416/s
     success_rate...................: 100.00% ✓ 47523      ✗ 0    
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

     checks.........................: 100.00% ✓ 105069     ✗ 0    
     data_received..................: 3.1 GB  25 MB/s
     data_sent......................: 42 MB   346 kB/s
     http_req_blocked...............: avg=6.27µs   min=1.06µs  med=3.06µs   max=3.94ms   p(90)=4.42µs   p(95)=5µs      p(99.9)=1.6ms   
     http_req_connecting............: avg=3.02µs   min=0s      med=0s       max=3.89ms   p(90)=0s       p(95)=0s       p(99.9)=1.57ms  
     http_req_duration..............: avg=170.71ms min=17.69ms med=156.83ms max=772.74ms p(90)=195.39ms p(95)=212.06ms p(99.9)=699.78ms
       { expected_response:true }...: avg=170.71ms min=17.69ms med=156.83ms max=772.74ms p(90)=195.39ms p(95)=212.06ms p(99.9)=699.78ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 35123
     http_req_receiving.............: avg=99.24µs  min=30.59µs med=82.91µs  max=168.14ms p(90)=112.71µs p(95)=123.97µs p(99.9)=725.73µs
     http_req_sending...............: avg=23.92µs  min=5.25µs  med=15.94µs  max=81.97ms  p(90)=20.2µs   p(95)=21.92µs  p(99.9)=360.32µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=170.58ms min=17.56ms med=156.73ms max=772.65ms p(90)=195.27ms p(95)=211.93ms p(99.9)=699.68ms
     http_reqs......................: 35123   287.739296/s
     iteration_duration.............: avg=171.41ms min=40.63ms med=157.17ms max=772.99ms p(90)=195.75ms p(95)=212.43ms p(99.9)=700.01ms
     iterations.....................: 35023   286.920063/s
     success_rate...................: 100.00% ✓ 35023      ✗ 0    
     vus............................: 14      min=0        max=50 
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

     checks.........................: 100.00% ✓ 100350     ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   329 kB/s
     http_req_blocked...............: avg=6.53µs   min=1.31µs  med=3.63µs   max=3.62ms   p(90)=5.12µs   p(95)=5.73µs   p(99.9)=1.26ms  
     http_req_connecting............: avg=2.65µs   min=0s      med=0s       max=3.58ms   p(90)=0s       p(95)=0s       p(99.9)=1.24ms  
     http_req_duration..............: avg=178.69ms min=22.53ms med=183.9ms  max=392.34ms p(90)=191.6ms  p(95)=195.36ms p(99.9)=263.46ms
       { expected_response:true }...: avg=178.69ms min=22.53ms med=183.9ms  max=392.34ms p(90)=191.6ms  p(95)=195.36ms p(99.9)=263.46ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33550
     http_req_receiving.............: avg=95.53µs  min=36.99µs med=85.41µs  max=145.87ms p(90)=115.68µs p(95)=127.29µs p(99.9)=486.98µs
     http_req_sending...............: avg=31.07µs  min=6.27µs  med=17.34µs  max=145.56ms p(90)=22.37µs  p(95)=24.3µs   p(99.9)=517.54µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=178.56ms min=22.39ms med=183.79ms max=391.73ms p(90)=191.48ms p(95)=195.22ms p(99.9)=263.21ms
     http_reqs......................: 33550   273.703986/s
     iteration_duration.............: avg=179.46ms min=37.41ms med=184.18ms max=408.48ms p(90)=191.89ms p(95)=195.65ms p(99.9)=265.04ms
     iterations.....................: 33450   272.888177/s
     success_rate...................: 100.00% ✓ 33450      ✗ 0    
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

