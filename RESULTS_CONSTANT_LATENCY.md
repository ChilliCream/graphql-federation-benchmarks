## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.14 | 3,606 | 3,619 | 3,600 | 0.2% | 389 MB | 110.4 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.14 | 3,551 | 3,559 | 3,532 | 0.3% | 386 MB | 111.2 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.14 | 3,543 | 3,556 | 3,528 | 0.3% | 138 MB | 40.0 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.14 | 3,542 | 3,558 | 3,523 | 0.4% | 142 MB | 41.0 KB |  |
| fusion-net-11 | 16.7.5 | 3,456 | 3,471 | 3,449 | 0.3% | 375 MB | 111.2 KB |  |
| fusion-aot-11 | 16.7.5 | 3,400 | 3,435 | 3,393 | 0.5% | 143 MB | 43.0 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,295 | 3,312 | 3,239 | 0.9% | 2,308 MB | 717.4 KB |  |
| fusion-fed-net-11 | 16.7.5 | 2,808 | 2,810 | 2,800 | 0.2% | 407 MB | 148.4 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 2,765 | 2,768 | 2,744 | 0.4% | 134 MB | 49.5 KB |  |
| hive-router | v0.3.10 | 2,069 | 2,073 | 2,054 | 0.4% | 109 MB | 53.8 KB |  |
| grafbase | 0.53.5 | 1,447 | 1,450 | 1,428 | 0.7% | 101 MB | 71.2 KB |  |
| cosmo | 0.365.2 | 1,409 | 1,411 | 1,407 | 0.1% | 150 MB | 109.3 KB |  |
| caliban | 3.2.0 | 1,378 | 1,379 | 1,376 | 0.1% | 4,602 MB | 3,419.8 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 534 | 535 | 533 | 0.2% | 2,750 MB | 5,273.3 KB |  |
| apollo-router | v2.19.0 | 479 | 479 | 479 | 0.0% | 180 MB | 385.5 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 402 | 402 | 399 | 0.3% | 206 MB | 524.8 KB |  |
| apollo-gateway | 2.14.4 | 266 | 266 | 265 | 0.2% | 2,139 MB | 8,234.3 KB |  |
| hive-gateway | 2.15.6 | 258 | 259 | 258 | 0.2% | 3,497 MB | 13,880.6 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.14)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1308282     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 524 MB  4.3 MB/s
     http_req_blocked...............: avg=2.75µs  min=911ns   med=2.19µs  max=3.62ms   p(90)=3.44µs  p(95)=4.11µs   p(99.9)=29.78µs
     http_req_connecting............: avg=217ns   min=0s      med=0s      max=3.58ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.54ms min=8.11ms  med=13.08ms max=287.79ms p(90)=16.76ms p(95)=18.08ms  p(99.9)=26.31ms
       { expected_response:true }...: avg=13.54ms min=8.11ms  med=13.08ms max=287.79ms p(90)=16.76ms p(95)=18.08ms  p(99.9)=26.31ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 436194
     http_req_receiving.............: avg=72.62µs min=24.37µs med=44.14µs max=135.01ms p(90)=93.29µs p(95)=186.76µs p(99.9)=2.11ms 
     http_req_sending...............: avg=34.48µs min=4.45µs  med=8.59µs  max=126.42ms p(90)=17.17µs p(95)=101.59µs p(99.9)=1.96ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.44ms min=8.05ms  med=12.98ms max=287.59ms p(90)=16.64ms p(95)=17.94ms  p(99.9)=26ms   
     http_reqs......................: 436194  3606.434117/s
     iteration_duration.............: avg=13.74ms min=8.26ms  med=13.28ms max=297.05ms p(90)=16.96ms p(95)=18.28ms  p(99.9)=26.53ms
     iterations.....................: 436094  3605.607321/s
     success_rate...................: 100.00% ✓ 436094      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.14)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1288569     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 516 MB  4.3 MB/s
     http_req_blocked...............: avg=2.48µs  min=831ns   med=1.89µs  max=6.49ms   p(90)=3.11µs  p(95)=3.86µs   p(99.9)=25.55µs
     http_req_connecting............: avg=214ns   min=0s      med=0s      max=3.78ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.76ms min=8.15ms  med=13.35ms max=281.58ms p(90)=16.92ms p(95)=18.18ms  p(99.9)=25.95ms
       { expected_response:true }...: avg=13.76ms min=8.15ms  med=13.35ms max=281.58ms p(90)=16.92ms p(95)=18.18ms  p(99.9)=25.95ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429623
     http_req_receiving.............: avg=68.35µs min=24.69µs med=42.92µs max=110.4ms  p(90)=91.89µs p(95)=170.25µs p(99.9)=1.76ms 
     http_req_sending...............: avg=32.59µs min=4.4µs   med=8.05µs  max=205.87ms p(90)=16.67µs p(95)=94.29µs  p(99.9)=1.81ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.66ms min=8.1ms   med=13.25ms max=277.73ms p(90)=16.81ms p(95)=18.06ms  p(99.9)=25.71ms
     http_reqs......................: 429623  3551.980617/s
     iteration_duration.............: avg=13.96ms min=8.26ms  med=13.54ms max=291.38ms p(90)=17.12ms p(95)=18.37ms  p(99.9)=26.19ms
     iterations.....................: 429523  3551.15385/s
     success_rate...................: 100.00% ✓ 429523      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.14)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1285629     ✗ 0     
     data_received..................: 38 GB   310 MB/s
     data_sent......................: 515 MB  4.3 MB/s
     http_req_blocked...............: avg=2.98µs  min=922ns   med=2.36µs  max=4.5ms    p(90)=3.81µs   p(95)=4.61µs   p(99.9)=33.2µs 
     http_req_connecting............: avg=231ns   min=0s      med=0s      max=3.81ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.79ms min=8.23ms  med=13.34ms max=300.37ms p(90)=16.96ms  p(95)=18.31ms  p(99.9)=26.61ms
       { expected_response:true }...: avg=13.79ms min=8.23ms  med=13.34ms max=300.37ms p(90)=16.96ms  p(95)=18.31ms  p(99.9)=26.61ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 428643
     http_req_receiving.............: avg=74.55µs min=24.03µs med=45.73µs max=27ms     p(90)=100.68µs p(95)=197.04µs p(99.9)=2.04ms 
     http_req_sending...............: avg=34.47µs min=4.31µs  med=9µs     max=116.37ms p(90)=18.87µs  p(95)=106.11µs p(99.9)=1.96ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.68ms min=8.18ms  med=13.24ms max=300.14ms p(90)=16.84ms  p(95)=18.18ms  p(99.9)=26.32ms
     http_reqs......................: 428643  3543.820022/s
     iteration_duration.............: avg=13.99ms min=8.43ms  med=13.54ms max=309.35ms p(90)=17.16ms  p(95)=18.51ms  p(99.9)=26.86ms
     iterations.....................: 428543  3542.993269/s
     success_rate...................: 100.00% ✓ 428543      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.14)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1285341     ✗ 0     
     data_received..................: 38 GB   310 MB/s
     data_sent......................: 515 MB  4.3 MB/s
     http_req_blocked...............: avg=3.3µs   min=852ns   med=2.29µs  max=9.23ms   p(90)=3.56µs  p(95)=4.24µs   p(99.9)=30.39µs
     http_req_connecting............: avg=667ns   min=0s      med=0s      max=9.17ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.8ms  min=8.1ms   med=13.34ms max=274.4ms  p(90)=17.06ms p(95)=18.41ms  p(99.9)=26.01ms
       { expected_response:true }...: avg=13.8ms  min=8.1ms   med=13.34ms max=274.4ms  p(90)=17.06ms p(95)=18.41ms  p(99.9)=26.01ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 428547
     http_req_receiving.............: avg=73.02µs min=24.83µs med=47.15µs max=169.4ms  p(90)=93.75µs p(95)=189.08µs p(99.9)=1.78ms 
     http_req_sending...............: avg=33.73µs min=4.48µs  med=8.53µs  max=190.12ms p(90)=15.88µs p(95)=101.73µs p(99.9)=1.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.69ms min=8.04ms  med=13.24ms max=273.59ms p(90)=16.94ms p(95)=18.27ms  p(99.9)=25.85ms
     http_reqs......................: 428547  3542.967314/s
     iteration_duration.............: avg=13.99ms min=8.25ms  med=13.53ms max=296.55ms p(90)=17.25ms p(95)=18.6ms   p(99.9)=26.26ms
     iterations.....................: 428447  3542.140574/s
     success_rate...................: 100.00% ✓ 428447      ✗ 0     
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

     checks.........................: 100.00% ✓ 1253796     ✗ 0     
     data_received..................: 37 GB   302 MB/s
     data_sent......................: 502 MB  4.2 MB/s
     http_req_blocked...............: avg=2.57µs  min=822ns   med=1.85µs  max=7.56ms   p(90)=3.13µs  p(95)=3.93µs   p(99.9)=23.45µs
     http_req_connecting............: avg=291ns   min=0s      med=0s      max=6.25ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.14ms min=8.15ms  med=13.72ms max=262.2ms  p(90)=17.55ms p(95)=18.91ms  p(99.9)=26.7ms 
       { expected_response:true }...: avg=14.14ms min=8.15ms  med=13.72ms max=262.2ms  p(90)=17.55ms p(95)=18.91ms  p(99.9)=26.7ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 418032
     http_req_receiving.............: avg=68.96µs min=24.08µs med=42.56µs max=118.94ms p(90)=92.03µs p(95)=173.84µs p(99.9)=1.98ms 
     http_req_sending...............: avg=31.83µs min=4.01µs  med=7.86µs  max=123.41ms p(90)=16.99µs p(95)=93.23µs  p(99.9)=1.92ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.04ms min=8.1ms   med=13.63ms max=261.7ms  p(90)=17.45ms p(95)=18.79ms  p(99.9)=26.43ms
     http_reqs......................: 418032  3456.310771/s
     iteration_duration.............: avg=14.34ms min=8.34ms  med=13.92ms max=282.81ms p(90)=17.74ms p(95)=19.1ms   p(99.9)=26.92ms
     iterations.....................: 417932  3455.483965/s
     success_rate...................: 100.00% ✓ 417932      ✗ 0     
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

     checks.........................: 100.00% ✓ 1233810     ✗ 0     
     data_received..................: 36 GB   298 MB/s
     data_sent......................: 494 MB  4.1 MB/s
     http_req_blocked...............: avg=2.34µs  min=781ns   med=1.81µs  max=3.37ms   p(90)=2.99µs  p(95)=3.66µs   p(99.9)=24.15µs
     http_req_connecting............: avg=202ns   min=0s      med=0s      max=3.33ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.38ms min=8.19ms  med=13.97ms max=283.68ms p(90)=17.75ms p(95)=19.08ms  p(99.9)=27.11ms
       { expected_response:true }...: avg=14.38ms min=8.19ms  med=13.97ms max=283.68ms p(90)=17.75ms p(95)=19.08ms  p(99.9)=27.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 411370
     http_req_receiving.............: avg=66.22µs min=23.94µs med=41.57µs max=113.68ms p(90)=87.09µs p(95)=165.26µs p(99.9)=1.74ms 
     http_req_sending...............: avg=30.1µs  min=4.18µs  med=7.66µs  max=159.87ms p(90)=15.07µs p(95)=91.62µs  p(99.9)=1.69ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.29ms min=8.14ms  med=13.87ms max=283.08ms p(90)=17.65ms p(95)=18.97ms  p(99.9)=26.95ms
     http_reqs......................: 411370  3400.663259/s
     iteration_duration.............: avg=14.58ms min=8.36ms  med=14.15ms max=294.6ms  p(90)=17.94ms p(95)=19.27ms  p(99.9)=27.34ms
     iterations.....................: 411270  3399.836591/s
     success_rate...................: 100.00% ✓ 411270      ✗ 0     
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

     checks.........................: 100.00% ✓ 1195644     ✗ 0     
     data_received..................: 35 GB   288 MB/s
     data_sent......................: 479 MB  4.0 MB/s
     http_req_blocked...............: avg=2.77µs  min=811ns  med=1.91µs  max=7.97ms   p(90)=3.12µs  p(95)=3.8µs    p(99.9)=25.19µs
     http_req_connecting............: avg=529ns   min=0s     med=0s      max=7.81ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.85ms min=8.48ms med=14.51ms max=301.86ms p(90)=17.88ms p(95)=19.11ms  p(99.9)=26.79ms
       { expected_response:true }...: avg=14.85ms min=8.48ms med=14.51ms max=301.86ms p(90)=17.88ms p(95)=19.11ms  p(99.9)=26.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 398648
     http_req_receiving.............: avg=74.01µs min=22.3µs med=43.73µs max=186.87ms p(90)=87.57µs p(95)=159.69µs p(99.9)=1.38ms 
     http_req_sending...............: avg=29.91µs min=4.28µs med=8.14µs  max=106.03ms p(90)=15.52µs p(95)=92.15µs  p(99.9)=1.53ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.75ms min=8.43ms med=14.41ms max=116.58ms p(90)=17.79ms p(95)=19ms     p(99.9)=26.56ms
     http_reqs......................: 398648  3295.473776/s
     iteration_duration.............: avg=15.04ms min=8.62ms med=14.69ms max=312.63ms p(90)=18.07ms p(95)=19.29ms  p(99.9)=27.11ms
     iterations.....................: 398548  3294.647114/s
     success_rate...................: 100.00% ✓ 398548      ✗ 0     
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

     checks.........................: 100.00% ✓ 1022448     ✗ 0     
     data_received..................: 30 GB   246 MB/s
     data_sent......................: 410 MB  3.4 MB/s
     http_req_blocked...............: avg=2.91µs  min=831ns   med=1.86µs  max=10.01ms  p(90)=3.27µs  p(95)=4.09µs   p(99.9)=26.12µs
     http_req_connecting............: avg=625ns   min=0s      med=0s      max=9.96ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.39ms min=11.6ms  med=16.96ms max=294.38ms p(90)=20.4ms  p(95)=21.6ms   p(99.9)=29.03ms
       { expected_response:true }...: avg=17.39ms min=11.6ms  med=16.96ms max=294.38ms p(90)=20.4ms  p(95)=21.6ms   p(99.9)=29.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 340916
     http_req_receiving.............: avg=66.27µs min=24.02µs med=43.58µs max=62.27ms  p(90)=90.61µs p(95)=150.35µs p(99.9)=1.5ms  
     http_req_sending...............: avg=28.42µs min=4.34µs  med=8.01µs  max=117.7ms  p(90)=16.77µs p(95)=83.98µs  p(99.9)=1.65ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.29ms min=11.54ms med=16.87ms max=292.22ms p(90)=20.29ms p(95)=21.49ms  p(99.9)=28.79ms
     http_reqs......................: 340916  2808.593231/s
     iteration_duration.............: avg=17.59ms min=11.85ms med=17.16ms max=305.46ms p(90)=20.6ms  p(95)=21.8ms   p(99.9)=29.24ms
     iterations.....................: 340816  2807.769393/s
     success_rate...................: 100.00% ✓ 340816      ✗ 0     
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

     checks.........................: 100.00% ✓ 1006761     ✗ 0     
     data_received..................: 29 GB   242 MB/s
     data_sent......................: 403 MB  3.3 MB/s
     http_req_blocked...............: avg=2.67µs  min=792ns   med=1.91µs  max=6.3ms    p(90)=3.18µs  p(95)=3.93µs   p(99.9)=23.27µs
     http_req_connecting............: avg=417ns   min=0s      med=0s      max=6.26ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.66ms min=11.94ms med=17.27ms max=292.69ms p(90)=20.57ms p(95)=21.78ms  p(99.9)=28.36ms
       { expected_response:true }...: avg=17.66ms min=11.94ms med=17.27ms max=292.69ms p(90)=20.57ms p(95)=21.78ms  p(99.9)=28.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 335687
     http_req_receiving.............: avg=66.04µs min=25.13µs med=45.81µs max=20.77ms  p(90)=88.74µs p(95)=138.24µs p(99.9)=1.29ms 
     http_req_sending...............: avg=28.53µs min=4.55µs  med=8.08µs  max=190.68ms p(90)=15.82µs p(95)=79.81µs  p(99.9)=1.47ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.57ms min=11.86ms med=17.18ms max=292.03ms p(90)=20.47ms p(95)=21.66ms  p(99.9)=28.1ms 
     http_reqs......................: 335687  2765.022771/s
     iteration_duration.............: avg=17.87ms min=12.16ms med=17.47ms max=303.04ms p(90)=20.77ms p(95)=21.97ms  p(99.9)=28.6ms 
     iterations.....................: 335587  2764.199081/s
     success_rate...................: 100.00% ✓ 335587      ✗ 0     
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

     checks.........................: 100.00% ✓ 756069      ✗ 0     
     data_received..................: 22 GB   181 MB/s
     data_sent......................: 303 MB  2.5 MB/s
     http_req_blocked...............: avg=2.68µs  min=832ns   med=1.99µs  max=4.21ms   p(90)=3.43µs  p(95)=4.1µs    p(99.9)=25.99µs 
     http_req_connecting............: avg=370ns   min=0s      med=0s      max=4.14ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.59ms min=17.14ms med=23.25ms max=283.17ms p(90)=26.5ms  p(95)=27.58ms  p(99.9)=32.78ms 
       { expected_response:true }...: avg=23.59ms min=17.14ms med=23.25ms max=283.17ms p(90)=26.5ms  p(95)=27.58ms  p(99.9)=32.78ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 252123
     http_req_receiving.............: avg=64.24µs min=25.18µs med=49.42µs max=126.42ms p(90)=88.48µs p(95)=110.39µs p(99.9)=812.52µs
     http_req_sending...............: avg=25.93µs min=4.32µs  med=8.83µs  max=250.83ms p(90)=16.53µs p(95)=22.68µs  p(99.9)=878.91µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.5ms  min=17.04ms med=23.17ms max=282.81ms p(90)=26.41ms p(95)=27.49ms  p(99.9)=32.57ms 
     http_reqs......................: 252123  2069.058367/s
     iteration_duration.............: avg=23.8ms  min=17.31ms med=23.45ms max=303.21ms p(90)=26.7ms  p(95)=27.78ms  p(99.9)=32.97ms 
     iterations.....................: 252023  2068.237713/s
     success_rate...................: 100.00% ✓ 252023      ✗ 0     
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

     checks.........................: 100.00% ✓ 529239      ✗ 0     
     data_received..................: 16 GB   127 MB/s
     data_sent......................: 212 MB  1.7 MB/s
     http_req_blocked...............: avg=3.93µs  min=851ns   med=2.15µs  max=7.38ms   p(90)=4.45µs   p(95)=5.44µs   p(99.9)=31.56µs
     http_req_connecting............: avg=1.17µs  min=0s      med=0s      max=7.35ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.75ms min=18.11ms med=33.41ms max=312.43ms p(90)=39.35ms  p(95)=41.11ms  p(99.9)=49.97ms
       { expected_response:true }...: avg=33.75ms min=18.11ms med=33.41ms max=312.43ms p(90)=39.35ms  p(95)=41.11ms  p(99.9)=49.97ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 176513
     http_req_receiving.............: avg=78.83µs min=26.96µs med=54.87µs max=65.92ms  p(90)=118.05µs p(95)=157.24µs p(99.9)=1.37ms 
     http_req_sending...............: avg=28.8µs  min=4.18µs  med=9.02µs  max=168.33ms p(90)=22.13µs  p(95)=32.01µs  p(99.9)=1.59ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.64ms min=18.02ms med=33.31ms max=287.97ms p(90)=39.25ms  p(95)=41ms     p(99.9)=49.79ms
     http_reqs......................: 176513  1447.579997/s
     iteration_duration.............: avg=34ms    min=20.68ms med=33.65ms max=327.11ms p(90)=39.57ms  p(95)=41.32ms  p(99.9)=50.2ms 
     iterations.....................: 176413  1446.759898/s
     success_rate...................: 100.00% ✓ 176413      ✗ 0     
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

     checks.........................: 100.00% ✓ 515400      ✗ 0     
     data_received..................: 15 GB   123 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=3.67µs  min=1.09µs  med=2.84µs  max=10.27ms  p(90)=4.53µs   p(95)=5.25µs   p(99.9)=37.08µs 
     http_req_connecting............: avg=430ns   min=0s      med=0s      max=5.81ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.68ms min=18.51ms med=34.13ms max=291.27ms p(90)=41.37ms  p(95)=43.7ms   p(99.9)=55.67ms 
       { expected_response:true }...: avg=34.68ms min=18.51ms med=34.13ms max=291.27ms p(90)=41.37ms  p(95)=43.7ms   p(99.9)=55.67ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 171900
     http_req_receiving.............: avg=76.21µs min=25.62µs med=63.62µs max=106.1ms  p(90)=104.04µs p(95)=122.17µs p(99.9)=759.74µs
     http_req_sending...............: avg=24.25µs min=4.84µs  med=11.71µs max=241.11ms p(90)=18.56µs  p(95)=22.5µs   p(99.9)=809.76µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.58ms min=18.36ms med=34.03ms max=290.49ms p(90)=41.27ms  p(95)=43.6ms   p(99.9)=55.57ms 
     http_reqs......................: 171900  1409.448526/s
     iteration_duration.............: avg=34.91ms min=20.92ms med=34.34ms max=326.97ms p(90)=41.58ms  p(95)=43.91ms  p(99.9)=56.03ms 
     iterations.....................: 171800  1408.628603/s
     success_rate...................: 100.00% ✓ 171800      ✗ 0     
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

     checks.........................: 100.00% ✓ 504051      ✗ 0     
     data_received..................: 15 GB   121 MB/s
     data_sent......................: 202 MB  1.7 MB/s
     http_req_blocked...............: avg=3.75µs  min=1.06µs  med=2.79µs  max=6.51ms   p(90)=4.38µs  p(95)=5.09µs  p(99.9)=32.79µs 
     http_req_connecting............: avg=659ns   min=0s      med=0s      max=6.39ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=35.47ms min=18.22ms med=34.96ms max=289.16ms p(90)=41.91ms p(95)=44.23ms p(99.9)=57.52ms 
       { expected_response:true }...: avg=35.47ms min=18.22ms med=34.96ms max=289.16ms p(90)=41.91ms p(95)=44.23ms p(99.9)=57.52ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 168117
     http_req_receiving.............: avg=75.96µs min=26.93µs med=61.7µs  max=145.97ms p(90)=97.52µs p(95)=113.8µs p(99.9)=856.42µs
     http_req_sending...............: avg=24.1µs  min=5.08µs  med=12.04µs max=157.87ms p(90)=18.15µs p(95)=21.88µs p(99.9)=778.16µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=35.37ms min=18.12ms med=34.87ms max=288ms    p(90)=41.82ms p(95)=44.14ms p(99.9)=57.27ms 
     http_reqs......................: 168117  1378.281293/s
     iteration_duration.............: avg=35.7ms  min=21.6ms  med=35.17ms max=307.84ms p(90)=42.12ms p(95)=44.45ms p(99.9)=57.9ms  
     iterations.....................: 168017  1377.461458/s
     success_rate...................: 100.00% ✓ 168017      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 195579     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   642 kB/s
     http_req_blocked...............: avg=4.61µs  min=1.05µs  med=2.91µs  max=4.37ms   p(90)=4.44µs   p(95)=5.07µs   p(99.9)=44.88µs 
     http_req_connecting............: avg=1.46µs  min=0s      med=0s      max=4.33ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=91.68ms min=20.47ms med=90.17ms max=325.65ms p(90)=107.53ms p(95)=116.42ms p(99.9)=209.55ms
       { expected_response:true }...: avg=91.68ms min=20.47ms med=90.17ms max=325.65ms p(90)=107.53ms p(95)=116.42ms p(99.9)=209.55ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 65293
     http_req_receiving.............: avg=82.28µs min=28.11µs med=73.91µs max=71.94ms  p(90)=107.14µs p(95)=119.95µs p(99.9)=566.89µs
     http_req_sending...............: avg=23.84µs min=4.87µs  med=14.3µs  max=109.5ms  p(90)=20.09µs  p(95)=22.23µs  p(99.9)=582.4µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.58ms min=20.3ms  med=90.07ms max=324.99ms p(90)=107.42ms p(95)=116.32ms p(99.9)=209.39ms
     http_reqs......................: 65293   534.201846/s
     iteration_duration.............: avg=92.04ms min=37.88ms med=90.42ms max=344.09ms p(90)=107.78ms p(95)=116.74ms p(99.9)=211.16ms
     iterations.....................: 65193   533.383685/s
     success_rate...................: 100.00% ✓ 65193      ✗ 0    
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

     checks.........................: 100.00% ✓ 175422     ✗ 0    
     data_received..................: 5.1 GB  42 MB/s
     data_sent......................: 70 MB   576 kB/s
     http_req_blocked...............: avg=6.85µs   min=1.07µs  med=2.58µs   max=8.47ms   p(90)=3.98µs   p(95)=4.53µs   p(99.9)=49.12µs 
     http_req_connecting............: avg=3.98µs   min=0s      med=0s       max=8.45ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=102.23ms min=20.21ms med=100.35ms max=327.13ms p(90)=129.56ms p(95)=138.78ms p(99.9)=181.27ms
       { expected_response:true }...: avg=102.23ms min=20.21ms med=100.35ms max=327.13ms p(90)=129.56ms p(95)=138.78ms p(99.9)=181.27ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 58574
     http_req_receiving.............: avg=142.27µs min=28.11µs med=67.42µs  max=193.77ms p(90)=100.36µs p(95)=112.95µs p(99.9)=814.15µs
     http_req_sending...............: avg=18.25µs  min=5.03µs  med=12.95µs  max=29.61ms  p(90)=18.85µs  p(95)=20.81µs  p(99.9)=611.29µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=102.07ms min=20.07ms med=100.25ms max=198.23ms p(90)=129.46ms p(95)=138.55ms p(99.9)=176.2ms 
     http_reqs......................: 58574   479.276706/s
     iteration_duration.............: avg=102.62ms min=25.94ms med=100.62ms max=351.19ms p(90)=129.83ms p(95)=139.1ms  p(99.9)=183.76ms
     iterations.....................: 58474   478.458464/s
     success_rate...................: 100.00% ✓ 58474      ✗ 0    
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

     checks.........................: 100.00% ✓ 147552     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 59 MB   484 kB/s
     http_req_blocked...............: avg=4.7µs    min=1.05µs  med=2.77µs   max=3.49ms   p(90)=4.13µs   p(95)=4.66µs   p(99.9)=150.6µs 
     http_req_connecting............: avg=1.77µs   min=0s      med=0s       max=3.45ms   p(90)=0s       p(95)=0s       p(99.9)=77.77µs 
     http_req_duration..............: avg=121.56ms min=20.74ms med=119.83ms max=356.5ms  p(90)=150.44ms p(95)=160.62ms p(99.9)=211.49ms
       { expected_response:true }...: avg=121.56ms min=20.74ms med=119.83ms max=356.5ms  p(90)=150.44ms p(95)=160.62ms p(99.9)=211.49ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49284
     http_req_receiving.............: avg=84.91µs  min=30.09µs med=73.88µs  max=195.59ms p(90)=105.4µs  p(95)=117.36µs p(99.9)=456.85µs
     http_req_sending...............: avg=22.25µs  min=4.89µs  med=14.04µs  max=89.38ms  p(90)=19.19µs  p(95)=20.94µs  p(99.9)=467.26µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=121.46ms min=20.59ms med=119.73ms max=355.98ms p(90)=150.33ms p(95)=160.5ms  p(99.9)=211.08ms
     http_reqs......................: 49284   402.902716/s
     iteration_duration.............: avg=122.01ms min=41.02ms med=120.11ms max=365.33ms p(90)=150.7ms  p(95)=160.89ms p(99.9)=213.79ms
     iterations.....................: 49184   402.085204/s
     success_rate...................: 100.00% ✓ 49184      ✗ 0    
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

     checks.........................: 100.00% ✓ 97707      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   320 kB/s
     http_req_blocked...............: avg=6.58µs   min=1.31µs  med=3.42µs   max=3.76ms   p(90)=4.86µs   p(95)=5.47µs   p(99.9)=1.45ms  
     http_req_connecting............: avg=2.9µs    min=0s      med=0s       max=3.72ms   p(90)=0s       p(95)=0s       p(99.9)=1.42ms  
     http_req_duration..............: avg=183.53ms min=22.07ms med=182.08ms max=386.65ms p(90)=212.12ms p(95)=218.08ms p(99.9)=288.77ms
       { expected_response:true }...: avg=183.53ms min=22.07ms med=182.08ms max=386.65ms p(90)=212.12ms p(95)=218.08ms p(99.9)=288.77ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32669
     http_req_receiving.............: avg=100µs    min=35.56µs med=86.35µs  max=164.81ms p(90)=116.57µs p(95)=127.94µs p(99.9)=572.96µs
     http_req_sending...............: avg=38.89µs  min=6.1µs   med=17.18µs  max=110.92ms p(90)=21.9µs   p(95)=23.81µs  p(99.9)=501.23µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.39ms min=21.97ms med=181.96ms max=386.12ms p(90)=211.98ms p(95)=217.95ms p(99.9)=288.46ms
     http_reqs......................: 32669   266.456402/s
     iteration_duration.............: avg=184.32ms min=43.16ms med=182.39ms max=405.72ms p(90)=212.41ms p(95)=218.38ms p(99.9)=294.32ms
     iterations.....................: 32569   265.640777/s
     success_rate...................: 100.00% ✓ 32569      ✗ 0    
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

     checks.........................: 100.00% ✓ 94386      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   310 kB/s
     http_req_blocked...............: avg=5.86µs   min=1.5µs   med=3.64µs   max=4.53ms   p(90)=5.15µs   p(95)=5.79µs   p(99.9)=723.92µs
     http_req_connecting............: avg=1.77µs   min=0s      med=0s       max=3.03ms   p(90)=0s       p(95)=0s       p(99.9)=695.94µs
     http_req_duration..............: avg=189.97ms min=17.19ms med=177.24ms max=747.4ms  p(90)=220.2ms  p(95)=243.68ms p(99.9)=681.82ms
       { expected_response:true }...: avg=189.97ms min=17.19ms med=177.24ms max=747.4ms  p(90)=220.2ms  p(95)=243.68ms p(99.9)=681.82ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31562
     http_req_receiving.............: avg=92.63µs  min=36.07µs med=88.57µs  max=15.81ms  p(90)=118.65µs p(95)=130.44µs p(99.9)=388.65µs
     http_req_sending...............: avg=26.89µs  min=6.85µs  med=17.64µs  max=50.77ms  p(90)=22.54µs  p(95)=24.39µs  p(99.9)=720.25µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=189.85ms min=17.1ms  med=177.13ms max=747.32ms p(90)=220.07ms p(95)=243.58ms p(99.9)=681.72ms
     http_reqs......................: 31562   258.54603/s
     iteration_duration.............: avg=190.79ms min=61.38ms med=177.67ms max=747.65ms p(90)=220.57ms p(95)=244.4ms  p(99.9)=682.22ms
     iterations.....................: 31462   257.726862/s
     success_rate...................: 100.00% ✓ 31462      ✗ 0    
     vus............................: 37      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

