## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-aot-11 | 16.8.0-p.12 | 3,580 | 3,586 | 3,572 | 0.2% | 120 MB | 34.3 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.12 | 3,541 | 3,565 | 3,531 | 0.4% | 390 MB | 112.9 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.12 | 3,529 | 3,550 | 3,521 | 0.3% | 379 MB | 110.0 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.12 | 3,517 | 3,522 | 3,511 | 0.1% | 135 MB | 39.2 KB |  |
| fusion-net-11 | 16.7.5 | 3,429 | 3,434 | 3,420 | 0.2% | 384 MB | 114.8 KB |  |
| fusion-aot-11 | 16.7.5 | 3,423 | 3,440 | 3,409 | 0.4% | 125 MB | 37.3 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,284 | 3,320 | 3,229 | 1.1% | 2,296 MB | 715.9 KB |  |
| fusion-fed-net-11 | 16.7.5 | 2,790 | 2,796 | 2,774 | 0.3% | 412 MB | 151.1 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 2,754 | 2,769 | 2,751 | 0.3% | 154 MB | 57.2 KB |  |
| hive-router | v0.3.10 | 2,026 | 2,032 | 2,019 | 0.2% | 108 MB | 54.7 KB |  |
| grafbase | 0.53.5 | 1,448 | 1,453 | 1,441 | 0.3% | 99 MB | 70.2 KB |  |
| cosmo | 0.365.2 | 1,371 | 1,378 | 1,363 | 0.4% | 152 MB | 113.8 KB |  |
| caliban | 3.2.0 | 1,334 | 1,338 | 1,333 | 0.2% | 5,570 MB | 4,276.0 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 520 | 522 | 520 | 0.2% | 2,763 MB | 5,440.0 KB |  |
| apollo-router | v2.19.0 | 482 | 482 | 481 | 0.1% | 182 MB | 386.2 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 384 | 386 | 383 | 0.3% | 204 MB | 545.1 KB |  |
| hive-gateway | 2.15.6 | 265 | 266 | 264 | 0.3% | 3,620 MB | 13,986.8 KB |  |
| apollo-gateway | 2.14.4 | 264 | 265 | 264 | 0.2% | 2,151 MB | 8,343.4 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.12)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1298793     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 520 MB  4.3 MB/s
     http_req_blocked...............: avg=2.46µs  min=821ns   med=1.9µs   max=3.86ms   p(90)=3.1µs   p(95)=3.77µs   p(99.9)=24.34µs
     http_req_connecting............: avg=229ns   min=0s      med=0s      max=3.82ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.65ms min=8.22ms  med=13.24ms max=273.46ms p(90)=16.68ms p(95)=17.92ms  p(99.9)=25.4ms 
       { expected_response:true }...: avg=13.65ms min=8.22ms  med=13.24ms max=273.46ms p(90)=16.68ms p(95)=17.92ms  p(99.9)=25.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 433031
     http_req_receiving.............: avg=69.69µs min=25.06µs med=44.53µs max=183.15ms p(90)=91µs    p(95)=175.55µs p(99.9)=1.62ms 
     http_req_sending...............: avg=31.71µs min=4.44µs  med=8.08µs  max=152.45ms p(90)=15.76µs p(95)=95.82µs  p(99.9)=1.62ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.55ms min=8.16ms  med=13.14ms max=273.33ms p(90)=16.57ms p(95)=17.8ms   p(99.9)=25.17ms
     http_reqs......................: 433031  3580.027645/s
     iteration_duration.............: avg=13.85ms min=8.36ms  med=13.43ms max=298.34ms p(90)=16.87ms p(95)=18.11ms  p(99.9)=25.61ms
     iterations.....................: 432931  3579.200908/s
     success_rate...................: 100.00% ✓ 432931      ✗ 0     
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

     checks.........................: 100.00% ✓ 1284612     ✗ 0     
     data_received..................: 38 GB   310 MB/s
     data_sent......................: 515 MB  4.3 MB/s
     http_req_blocked...............: avg=2.89µs  min=882ns   med=2.3µs   max=4.03ms   p(90)=3.7µs   p(95)=4.44µs   p(99.9)=31.74µs
     http_req_connecting............: avg=218ns   min=0s      med=0s      max=3.97ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.8ms  min=8ms     med=13.34ms max=272.39ms p(90)=17.1ms  p(95)=18.44ms  p(99.9)=26.25ms
       { expected_response:true }...: avg=13.8ms  min=8ms     med=13.34ms max=272.39ms p(90)=17.1ms  p(95)=18.44ms  p(99.9)=26.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 428304
     http_req_receiving.............: avg=75.46µs min=24.53µs med=46.22µs max=168.57ms p(90)=97.98µs p(95)=191.36µs p(99.9)=1.94ms 
     http_req_sending...............: avg=33.5µs  min=4.43µs  med=8.63µs  max=94.05ms  p(90)=17.3µs  p(95)=102.29µs p(99.9)=1.81ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.69ms min=7.95ms  med=13.24ms max=263.45ms p(90)=16.98ms p(95)=18.3ms   p(99.9)=26.05ms
     http_reqs......................: 428304  3541.245043/s
     iteration_duration.............: avg=14ms    min=8.16ms  med=13.54ms max=288.57ms p(90)=17.29ms p(95)=18.64ms  p(99.9)=26.48ms
     iterations.....................: 428204  3540.418237/s
     success_rate...................: 100.00% ✓ 428204      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.12)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1280574     ✗ 0     
     data_received..................: 37 GB   309 MB/s
     data_sent......................: 513 MB  4.2 MB/s
     http_req_blocked...............: avg=2.83µs  min=881ns   med=2.27µs  max=3.53ms   p(90)=3.59µs  p(95)=4.34µs   p(99.9)=30.47µs
     http_req_connecting............: avg=210ns   min=0s      med=0s      max=3.49ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.84ms min=8.14ms  med=13.4ms  max=302.57ms p(90)=17.12ms p(95)=18.46ms  p(99.9)=26.21ms
       { expected_response:true }...: avg=13.84ms min=8.14ms  med=13.4ms  max=302.57ms p(90)=17.12ms p(95)=18.46ms  p(99.9)=26.21ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 426958
     http_req_receiving.............: avg=75.13µs min=24.83µs med=46.78µs max=143.67ms p(90)=96.93µs p(95)=189.37µs p(99.9)=2.01ms 
     http_req_sending...............: avg=34.29µs min=4.31µs  med=8.52µs  max=199.53ms p(90)=16.77µs p(95)=101.59µs p(99.9)=1.81ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.73ms min=8.09ms  med=13.29ms max=302.48ms p(90)=17ms    p(95)=18.32ms  p(99.9)=25.8ms 
     http_reqs......................: 426958  3529.884202/s
     iteration_duration.............: avg=14.04ms min=8.34ms  med=13.59ms max=311.27ms p(90)=17.31ms p(95)=18.65ms  p(99.9)=26.43ms
     iterations.....................: 426858  3529.05745/s
     success_rate...................: 100.00% ✓ 426858      ✗ 0     
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

     checks.........................: 100.00% ✓ 1276110     ✗ 0     
     data_received..................: 37 GB   308 MB/s
     data_sent......................: 511 MB  4.2 MB/s
     http_req_blocked...............: avg=2.94µs  min=892ns   med=2.36µs  max=3.99ms   p(90)=3.72µs  p(95)=4.44µs   p(99.9)=28.45µs
     http_req_connecting............: avg=242ns   min=0s      med=0s      max=3.95ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.89ms min=8.21ms  med=13.46ms max=284.03ms p(90)=17.07ms p(95)=18.38ms  p(99.9)=26.09ms
       { expected_response:true }...: avg=13.89ms min=8.21ms  med=13.46ms max=284.03ms p(90)=17.07ms p(95)=18.38ms  p(99.9)=26.09ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 425470
     http_req_receiving.............: avg=73.05µs min=23.21µs med=44.98µs max=199.96ms p(90)=94.65µs p(95)=188.98µs p(99.9)=1.9ms  
     http_req_sending...............: avg=35.67µs min=4.63µs  med=9.06µs  max=181.88ms p(90)=17.87µs p(95)=104.46µs p(99.9)=1.99ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.78ms min=8.16ms  med=13.36ms max=283.73ms p(90)=16.95ms p(95)=18.24ms  p(99.9)=25.81ms
     http_reqs......................: 425470  3517.416462/s
     iteration_duration.............: avg=14.09ms min=8.39ms  med=13.66ms max=294.58ms p(90)=17.27ms p(95)=18.58ms  p(99.9)=26.31ms
     iterations.....................: 425370  3516.589749/s
     success_rate...................: 100.00% ✓ 425370      ✗ 0     
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

     checks.........................: 100.00% ✓ 1244244     ✗ 0     
     data_received..................: 36 GB   300 MB/s
     data_sent......................: 499 MB  4.1 MB/s
     http_req_blocked...............: avg=2.91µs  min=912ns   med=2.32µs  max=3.45ms   p(90)=3.74µs  p(95)=4.54µs   p(99.9)=31.71µs
     http_req_connecting............: avg=206ns   min=0s      med=0s      max=3.41ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.25ms min=8.25ms  med=13.79ms max=277.1ms  p(90)=17.74ms p(95)=19.15ms  p(99.9)=27.51ms
       { expected_response:true }...: avg=14.25ms min=8.25ms  med=13.79ms max=277.1ms  p(90)=17.74ms p(95)=19.15ms  p(99.9)=27.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 414848
     http_req_receiving.............: avg=74.41µs min=24.11µs med=45.56µs max=115.38ms p(90)=99.09µs p(95)=187.29µs p(99.9)=2.12ms 
     http_req_sending...............: avg=35.12µs min=4.41µs  med=8.66µs  max=208.94ms p(90)=18.02µs p(95)=100.57µs p(99.9)=2.05ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.14ms min=8.16ms  med=13.69ms max=276.49ms p(90)=17.63ms p(95)=19.02ms  p(99.9)=27.26ms
     http_reqs......................: 414848  3429.839817/s
     iteration_duration.............: avg=14.45ms min=8.45ms  med=13.99ms max=292.18ms p(90)=17.94ms p(95)=19.35ms  p(99.9)=27.74ms
     iterations.....................: 414748  3429.013046/s
     success_rate...................: 100.00% ✓ 414748      ✗ 0     
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

     checks.........................: 100.00% ✓ 1242243     ✗ 0     
     data_received..................: 36 GB   300 MB/s
     data_sent......................: 498 MB  4.1 MB/s
     http_req_blocked...............: avg=2.77µs  min=811ns   med=2.19µs  max=3.98ms   p(90)=3.52µs  p(95)=4.24µs   p(99.9)=30.17µs
     http_req_connecting............: avg=214ns   min=0s      med=0s      max=3.56ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.28ms min=8.28ms  med=13.84ms max=272.86ms p(90)=17.67ms p(95)=19.02ms  p(99.9)=27.42ms
       { expected_response:true }...: avg=14.28ms min=8.28ms  med=13.84ms max=272.86ms p(90)=17.67ms p(95)=19.02ms  p(99.9)=27.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 414181
     http_req_receiving.............: avg=71.16µs min=24.11µs med=45.24µs max=12.18ms  p(90)=93.1µs  p(95)=182.84µs p(99.9)=1.86ms 
     http_req_sending...............: avg=32.4µs  min=4.19µs  med=8.17µs  max=197ms    p(90)=16.32µs p(95)=97.82µs  p(99.9)=1.79ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.18ms min=8.23ms  med=13.74ms max=272.31ms p(90)=17.55ms p(95)=18.91ms  p(99.9)=27.17ms
     http_reqs......................: 414181  3423.87527/s
     iteration_duration.............: avg=14.48ms min=8.41ms  med=14.03ms max=290.86ms p(90)=17.86ms p(95)=19.22ms  p(99.9)=27.66ms
     iterations.....................: 414081  3423.048608/s
     success_rate...................: 100.00% ✓ 414081      ✗ 0     
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

     checks.........................: 100.00% ✓ 1191597     ✗ 0     
     data_received..................: 35 GB   287 MB/s
     data_sent......................: 477 MB  3.9 MB/s
     http_req_blocked...............: avg=2.49µs  min=772ns   med=1.91µs  max=3.46ms   p(90)=3.23µs  p(95)=4.02µs  p(99.9)=26.18µs
     http_req_connecting............: avg=216ns   min=0s      med=0s      max=3.42ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=14.9ms  min=8.78ms  med=14.57ms max=312.52ms p(90)=17.96ms p(95)=19.13ms p(99.9)=26.47ms
       { expected_response:true }...: avg=14.9ms  min=8.78ms  med=14.57ms max=312.52ms p(90)=17.96ms p(95)=19.13ms p(99.9)=26.47ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 397299
     http_req_receiving.............: avg=66.62µs min=23.34µs med=43.37µs max=64.69ms  p(90)=90.06µs p(95)=165.2µs p(99.9)=1.49ms 
     http_req_sending...............: avg=30.86µs min=4.3µs   med=8.15µs  max=226.27ms p(90)=16.75µs p(95)=92.66µs p(99.9)=1.57ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=14.8ms  min=8.72ms  med=14.48ms max=311.91ms p(90)=17.86ms p(95)=19.02ms p(99.9)=26.18ms
     http_reqs......................: 397299  3284.694763/s
     iteration_duration.............: avg=15.09ms min=8.93ms  med=14.76ms max=323.45ms p(90)=18.15ms p(95)=19.32ms p(99.9)=26.69ms
     iterations.....................: 397199  3283.868007/s
     success_rate...................: 100.00% ✓ 397199      ✗ 0     
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

     checks.........................: 100.00% ✓ 1016031     ✗ 0     
     data_received..................: 30 GB   244 MB/s
     data_sent......................: 407 MB  3.4 MB/s
     http_req_blocked...............: avg=2.57µs  min=812ns   med=1.9µs   max=5.27ms   p(90)=3.29µs  p(95)=4.2µs    p(99.9)=23.72µs
     http_req_connecting............: avg=267ns   min=0s      med=0s      max=4.09ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.5ms  min=11.79ms med=17.07ms max=288.43ms p(90)=20.56ms p(95)=21.79ms  p(99.9)=28.74ms
       { expected_response:true }...: avg=17.5ms  min=11.79ms med=17.07ms max=288.43ms p(90)=20.56ms p(95)=21.79ms  p(99.9)=28.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 338777
     http_req_receiving.............: avg=68.67µs min=24.35µs med=46.25µs max=194.61ms p(90)=91.61µs p(95)=142.11µs p(99.9)=1.54ms 
     http_req_sending...............: avg=27.15µs min=4.21µs  med=7.93µs  max=70.93ms  p(90)=15.72µs p(95)=78.18µs  p(99.9)=1.4ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.4ms  min=11.68ms med=16.98ms max=284.02ms p(90)=20.46ms p(95)=21.67ms  p(99.9)=28.36ms
     http_reqs......................: 338777  2790.717922/s
     iteration_duration.............: avg=17.7ms  min=12.07ms med=17.27ms max=299.6ms  p(90)=20.75ms p(95)=21.99ms  p(99.9)=28.97ms
     iterations.....................: 338677  2789.89416/s
     success_rate...................: 100.00% ✓ 338677      ✗ 0     
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

     checks.........................: 100.00% ✓ 1002879     ✗ 0     
     data_received..................: 29 GB   241 MB/s
     data_sent......................: 402 MB  3.3 MB/s
     http_req_blocked...............: avg=2.84µs  min=791ns   med=1.85µs  max=9.5ms    p(90)=3.04µs  p(95)=3.71µs   p(99.9)=24.7µs 
     http_req_connecting............: avg=627ns   min=0s      med=0s      max=9.37ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.73ms min=11.89ms med=17.3ms  max=284.24ms p(90)=20.81ms p(95)=22.07ms  p(99.9)=28.85ms
       { expected_response:true }...: avg=17.73ms min=11.89ms med=17.3ms  max=284.24ms p(90)=20.81ms p(95)=22.07ms  p(99.9)=28.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 334393
     http_req_receiving.............: avg=64.54µs min=23.55µs med=43.64µs max=91.22ms  p(90)=87.09µs p(95)=143.25µs p(99.9)=1.29ms 
     http_req_sending...............: avg=28.07µs min=4.3µs   med=7.87µs  max=158.78ms p(90)=15.02µs p(95)=82.25µs  p(99.9)=1.26ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.64ms min=11.84ms med=17.21ms max=258.18ms p(90)=20.71ms p(95)=21.96ms  p(99.9)=28.62ms
     http_reqs......................: 334393  2754.466514/s
     iteration_duration.............: avg=17.93ms min=12.07ms med=17.5ms  max=297.91ms p(90)=21.01ms p(95)=22.26ms  p(99.9)=29.09ms
     iterations.....................: 334293  2753.642793/s
     success_rate...................: 100.00% ✓ 334293      ✗ 0     
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

     checks.........................: 100.00% ✓ 740499      ✗ 0     
     data_received..................: 22 GB   177 MB/s
     data_sent......................: 297 MB  2.4 MB/s
     http_req_blocked...............: avg=3.48µs  min=852ns   med=2.1µs   max=8.78ms   p(90)=3.52µs  p(95)=4.16µs   p(99.9)=28.15µs 
     http_req_connecting............: avg=948ns   min=0s      med=0s      max=8.72ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=24.09ms min=17.18ms med=23.75ms max=305.92ms p(90)=27.13ms p(95)=28.22ms  p(99.9)=33.63ms 
       { expected_response:true }...: avg=24.09ms min=17.18ms med=23.75ms max=305.92ms p(90)=27.13ms p(95)=28.22ms  p(99.9)=33.63ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 246933
     http_req_receiving.............: avg=62.55µs min=23.27µs med=49.04µs max=36.44ms  p(90)=87.16µs p(95)=107.59µs p(99.9)=807.61µs
     http_req_sending...............: avg=23.54µs min=4.57µs  med=9.21µs  max=161.35ms p(90)=16.39µs p(95)=21.87µs  p(99.9)=920.81µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=24ms    min=17.08ms med=23.67ms max=305.05ms p(90)=27.04ms p(95)=28.13ms  p(99.9)=33.49ms 
     http_reqs......................: 246933  2026.453045/s
     iteration_duration.............: avg=24.3ms  min=17.4ms  med=23.95ms max=319.48ms p(90)=27.33ms p(95)=28.42ms  p(99.9)=33.84ms 
     iterations.....................: 246833  2025.632396/s
     success_rate...................: 100.00% ✓ 246833      ✗ 0     
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

     checks.........................: 100.00% ✓ 529422      ✗ 0     
     data_received..................: 16 GB   127 MB/s
     data_sent......................: 212 MB  1.7 MB/s
     http_req_blocked...............: avg=3.82µs  min=811ns   med=2.72µs  max=4.47ms   p(90)=4.96µs   p(95)=5.9µs    p(99.9)=42.57µs
     http_req_connecting............: avg=576ns   min=0s      med=0s      max=3.8ms    p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.72ms min=17.63ms med=33.38ms max=305.1ms  p(90)=39.42ms  p(95)=41.19ms  p(99.9)=50.5ms 
       { expected_response:true }...: avg=33.72ms min=17.63ms med=33.38ms max=305.1ms  p(90)=39.42ms  p(95)=41.19ms  p(99.9)=50.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 176574
     http_req_receiving.............: avg=85.13µs min=27.68µs med=59.58µs max=78.76ms  p(90)=124.58µs p(95)=168.93µs p(99.9)=1.46ms 
     http_req_sending...............: avg=33.5µs  min=4.47µs  med=10.54µs max=240.33ms p(90)=22.85µs  p(95)=41.14µs  p(99.9)=1.41ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.61ms min=17.44ms med=33.27ms max=304.63ms p(90)=39.3ms   p(95)=41.07ms  p(99.9)=50.18ms
     http_reqs......................: 176574  1448.036442/s
     iteration_duration.............: avg=33.98ms min=20.01ms med=33.63ms max=314.53ms p(90)=39.65ms  p(95)=41.42ms  p(99.9)=50.81ms
     iterations.....................: 176474  1447.216369/s
     success_rate...................: 100.00% ✓ 176474      ✗ 0     
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

     checks.........................: 100.00% ✓ 501615      ✗ 0     
     data_received..................: 15 GB   120 MB/s
     data_sent......................: 201 MB  1.6 MB/s
     http_req_blocked...............: avg=2.67µs  min=892ns   med=2.12µs  max=1.98ms   p(90)=3.59µs  p(95)=4.27µs  p(99.9)=28.44µs 
     http_req_connecting............: avg=237ns   min=0s      med=0s      max=1.95ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=35.66ms min=17.97ms med=35.1ms  max=289.37ms p(90)=42.67ms p(95)=45.1ms  p(99.9)=57.59ms 
       { expected_response:true }...: avg=35.66ms min=17.97ms med=35.1ms  max=289.37ms p(90)=42.67ms p(95)=45.1ms  p(99.9)=57.59ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 167305
     http_req_receiving.............: avg=71.57µs min=25.61µs med=57.81µs max=128.96ms p(90)=95.91µs p(95)=112.5µs p(99.9)=692.75µs
     http_req_sending...............: avg=21.94µs min=4.67µs  med=9.86µs  max=151.85ms p(90)=16.37µs p(95)=19.89µs p(99.9)=726.29µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=35.57ms min=17.85ms med=35.02ms max=288.9ms  p(90)=42.59ms p(95)=45.01ms p(99.9)=57.4ms  
     http_reqs......................: 167305  1371.698372/s
     iteration_duration.............: avg=35.87ms min=19.58ms med=35.3ms  max=300.98ms p(90)=42.87ms p(95)=45.29ms p(99.9)=57.89ms 
     iterations.....................: 167205  1370.878493/s
     success_rate...................: 100.00% ✓ 167205      ✗ 0     
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

     checks.........................: 100.00% ✓ 487956      ✗ 0     
     data_received..................: 14 GB   117 MB/s
     data_sent......................: 196 MB  1.6 MB/s
     http_req_blocked...............: avg=3.5µs   min=1.08µs  med=2.61µs  max=3.86ms   p(90)=4.06µs  p(95)=4.7µs    p(99.9)=32.8µs  
     http_req_connecting............: avg=613ns   min=0s      med=0s      max=3.82ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=36.66ms min=18.4ms  med=36.08ms max=312.43ms p(90)=43.72ms p(95)=46.28ms  p(99.9)=62.24ms 
       { expected_response:true }...: avg=36.66ms min=18.4ms  med=36.08ms max=312.43ms p(90)=43.72ms p(95)=46.28ms  p(99.9)=62.24ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 162752
     http_req_receiving.............: avg=71.94µs min=28.01µs med=59.62µs max=169.83ms p(90)=92.72µs p(95)=106.81µs p(99.9)=769.22µs
     http_req_sending...............: avg=21.51µs min=4.98µs  med=11.51µs max=169.3ms  p(90)=17.1µs  p(95)=20.4µs   p(99.9)=719.11µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=36.56ms min=18.28ms med=35.99ms max=312.22ms p(90)=43.63ms p(95)=46.19ms  p(99.9)=61.85ms 
     http_reqs......................: 162752  1334.120972/s
     iteration_duration.............: avg=36.88ms min=20.16ms med=36.29ms max=319.54ms p(90)=43.93ms p(95)=46.49ms  p(99.9)=62.76ms 
     iterations.....................: 162652  1333.301246/s
     success_rate...................: 100.00% ✓ 162652      ✗ 0     
     vus............................: 11      min=0         max=50  
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

     checks.........................: 100.00% ✓ 190656     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 76 MB   625 kB/s
     http_req_blocked...............: avg=4.27µs  min=942ns   med=2.47µs  max=3.88ms   p(90)=3.87µs   p(95)=4.44µs   p(99.9)=43.69µs 
     http_req_connecting............: avg=1.54µs  min=0s      med=0s      max=3.84ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=94.09ms min=20.24ms med=92.59ms max=336.38ms p(90)=110.8ms  p(95)=119.63ms p(99.9)=214.17ms
       { expected_response:true }...: avg=94.09ms min=20.24ms med=92.59ms max=336.38ms p(90)=110.8ms  p(95)=119.63ms p(99.9)=214.17ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63652
     http_req_receiving.............: avg=75.15µs min=29.21µs med=68.06µs max=19.43ms  p(90)=100.84µs p(95)=113.05µs p(99.9)=466.19µs
     http_req_sending...............: avg=21.11µs min=4.82µs  med=12.59µs max=134.68ms p(90)=18.25µs  p(95)=20.13µs  p(99.9)=473.38µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94ms    min=20.15ms med=92.5ms  max=335.95ms p(90)=110.69ms p(95)=119.52ms p(99.9)=214.1ms 
     http_reqs......................: 63652   520.616635/s
     iteration_duration.............: avg=94.44ms min=39.52ms med=92.84ms max=356.83ms p(90)=111.04ms p(95)=119.88ms p(99.9)=216.48ms
     iterations.....................: 63552   519.798724/s
     success_rate...................: 100.00% ✓ 63552      ✗ 0    
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

     checks.........................: 100.00% ✓ 176463     ✗ 0    
     data_received..................: 5.2 GB  42 MB/s
     data_sent......................: 71 MB   579 kB/s
     http_req_blocked...............: avg=5.1µs    min=1.26µs  med=3.32µs   max=4.9ms    p(90)=4.84µs   p(95)=5.45µs   p(99.9)=54.64µs 
     http_req_connecting............: avg=1.48µs   min=0s      med=0s       max=4.88ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=101.62ms min=19.64ms med=99.88ms  max=322.76ms p(90)=128.9ms  p(95)=138.33ms p(99.9)=178.21ms
       { expected_response:true }...: avg=101.62ms min=19.64ms med=99.88ms  max=322.76ms p(90)=128.9ms  p(95)=138.33ms p(99.9)=178.21ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 58921
     http_req_receiving.............: avg=82.28µs  min=30.32µs med=73.93µs  max=125.08ms p(90)=105.49µs p(95)=117.31µs p(99.9)=544.39µs
     http_req_sending...............: avg=23.02µs  min=5.62µs  med=15.12µs  max=112.61ms p(90)=20.6µs   p(95)=22.69µs  p(99.9)=593.7µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=101.52ms min=19.52ms med=99.78ms  max=320.86ms p(90)=128.79ms p(95)=138.21ms p(99.9)=178.11ms
     http_reqs......................: 58921   482.073576/s
     iteration_duration.............: avg=102.02ms min=29.8ms  med=100.15ms max=331.73ms p(90)=129.15ms p(95)=138.6ms  p(99.9)=179.83ms
     iterations.....................: 58821   481.255406/s
     success_rate...................: 100.00% ✓ 58821      ✗ 0    
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

     checks.........................: 100.00% ✓ 140655     ✗ 0    
     data_received..................: 4.1 GB  34 MB/s
     data_sent......................: 56 MB   461 kB/s
     http_req_blocked...............: avg=7.71µs   min=1.09µs  med=2.81µs   max=8.52ms   p(90)=4.21µs   p(95)=4.73µs   p(99.9)=691.73µs
     http_req_connecting............: avg=4.54µs   min=0s      med=0s       max=7.85ms   p(90)=0s       p(95)=0s       p(99.9)=367.66µs
     http_req_duration..............: avg=127.53ms min=20.94ms med=125.79ms max=349.48ms p(90)=158.51ms p(95)=168.91ms p(99.9)=217.9ms 
       { expected_response:true }...: avg=127.53ms min=20.94ms med=125.79ms max=349.48ms p(90)=158.51ms p(95)=168.91ms p(99.9)=217.9ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 46985
     http_req_receiving.............: avg=77.68µs  min=29.27µs med=70.5µs   max=68.78ms  p(90)=102.38µs p(95)=114.69µs p(99.9)=531.25µs
     http_req_sending...............: avg=26.88µs  min=4.95µs  med=13.49µs  max=166.77ms p(90)=19.02µs  p(95)=20.84µs  p(99.9)=837.91µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=127.43ms min=20.82ms med=125.69ms max=349.12ms p(90)=158.4ms  p(95)=168.83ms p(99.9)=216.97ms
     http_reqs......................: 46985   384.084172/s
     iteration_duration.............: avg=128.01ms min=31.5ms  med=126.05ms max=369.08ms p(90)=158.75ms p(95)=169.19ms p(99.9)=222.73ms
     iterations.....................: 46885   383.26671/s
     success_rate...................: 100.00% ✓ 46885      ✗ 0    
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

     checks.........................: 100.00% ✓ 97050      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   319 kB/s
     http_req_blocked...............: avg=5.08µs   min=1.37µs  med=3.62µs   max=1.62ms   p(90)=5.15µs   p(95)=5.83µs   p(99.9)=448.73µs
     http_req_connecting............: avg=1.13µs   min=0s      med=0s       max=1.59ms   p(90)=0s       p(95)=0s       p(99.9)=419.02µs
     http_req_duration..............: avg=184.79ms min=17.76ms med=170.35ms max=774.41ms p(90)=222.47ms p(95)=247.08ms p(99.9)=702.99ms
       { expected_response:true }...: avg=184.79ms min=17.76ms med=170.35ms max=774.41ms p(90)=222.47ms p(95)=247.08ms p(99.9)=702.99ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32450
     http_req_receiving.............: avg=102.16µs min=37.54µs med=90.65µs  max=76.95ms  p(90)=123.16µs p(95)=136.69µs p(99.9)=724.13µs
     http_req_sending...............: avg=31.32µs  min=6.46µs  med=18.64µs  max=58.45ms  p(90)=23.52µs  p(95)=25.5µs   p(99.9)=478.7µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.65ms min=17.66ms med=170.23ms max=774.32ms p(90)=222.3ms  p(95)=246.83ms p(99.9)=702.87ms
     http_reqs......................: 32450   265.850769/s
     iteration_duration.............: avg=185.59ms min=54.49ms med=170.73ms max=774.63ms p(90)=222.84ms p(95)=247.59ms p(99.9)=703.3ms 
     iterations.....................: 32350   265.031506/s
     success_rate...................: 100.00% ✓ 32350      ✗ 0    
     vus............................: 32      min=0        max=50 
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

     checks.........................: 100.00% ✓ 97044      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   318 kB/s
     http_req_blocked...............: avg=6.18µs   min=1.13µs  med=2.95µs   max=3.68ms   p(90)=4.24µs   p(95)=4.76µs   p(99.9)=1.53ms  
     http_req_connecting............: avg=2.98µs   min=0s      med=0s       max=3.64ms   p(90)=0s       p(95)=0s       p(99.9)=1.44ms  
     http_req_duration..............: avg=184.8ms  min=22.71ms med=184.69ms max=370.41ms p(90)=196.41ms p(95)=201.6ms  p(99.9)=266.01ms
       { expected_response:true }...: avg=184.8ms  min=22.71ms med=184.69ms max=370.41ms p(90)=196.41ms p(95)=201.6ms  p(99.9)=266.01ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32448
     http_req_receiving.............: avg=89.43µs  min=28.69µs med=84.24µs  max=55.77ms  p(90)=113.29µs p(95)=124.12µs p(99.9)=509.26µs
     http_req_sending...............: avg=24.56µs  min=5.41µs  med=15.63µs  max=44.32ms  p(90)=19.59µs  p(95)=21.25µs  p(99.9)=445.03µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.69ms min=22.58ms med=184.57ms max=368.85ms p(90)=196.29ms p(95)=201.48ms p(99.9)=265.93ms
     http_reqs......................: 32448   264.743332/s
     iteration_duration.............: avg=185.57ms min=66.51ms med=185.01ms max=381.08ms p(90)=196.67ms p(95)=201.87ms p(99.9)=268ms   
     iterations.....................: 32348   263.927432/s
     success_rate...................: 100.00% ✓ 32348      ✗ 0    
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

