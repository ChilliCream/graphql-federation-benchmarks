## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.10 | 3,465 | 3,496 | 3,453 | 0.5% | 388 MB | 114.8 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.10 | 3,446 | 3,469 | 3,422 | 0.5% | 123 MB | 36.7 KB |  |
| fusion-net-11 | 16.7.5 | 3,407 | 3,420 | 3,399 | 0.2% | 386 MB | 116.1 KB |  |
| fusion-aot-11 | 16.7.5 | 3,392 | 3,405 | 3,367 | 0.5% | 135 MB | 40.9 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,257 | 3,276 | 3,206 | 0.9% | 2,292 MB | 720.6 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.10 | 2,833 | 2,839 | 2,807 | 0.4% | 403 MB | 145.8 KB |  |
| fusion-fed-net-11 | 16.7.5 | 2,795 | 2,806 | 2,762 | 0.6% | 411 MB | 150.5 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.10 | 2,781 | 2,784 | 2,767 | 0.2% | 138 MB | 51.0 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 2,730 | 2,740 | 2,725 | 0.2% | 152 MB | 57.2 KB |  |
| hive-router | v0.3.10 | 2,054 | 2,065 | 2,052 | 0.3% | 99 MB | 49.5 KB |  |
| grafbase | 0.53.5 | 1,452 | 1,453 | 1,438 | 0.4% | 100 MB | 70.5 KB |  |
| cosmo | 0.365.2 | 1,406 | 1,407 | 1,405 | 0.1% | 151 MB | 110.2 KB |  |
| caliban | 3.2.0 | 1,390 | 1,393 | 1,389 | 0.1% | 4,977 MB | 3,666.8 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 537 | 538 | 536 | 0.2% | 2,758 MB | 5,258.3 KB |  |
| apollo-router | v2.19.0 | 527 | 528 | 527 | 0.1% | 177 MB | 344.7 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 386 | 386 | 385 | 0.1% | 204 MB | 541.8 KB |  |
| apollo-gateway | 2.14.4 | 268 | 269 | 267 | 0.3% | 2,158 MB | 8,244.6 KB |  |
| hive-gateway | 2.15.6 | 259 | 259 | 257 | 0.3% | 3,748 MB | 14,817.1 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1257138     ✗ 0     
     data_received..................: 37 GB   303 MB/s
     data_sent......................: 504 MB  4.2 MB/s
     http_req_blocked...............: avg=2.47µs  min=781ns  med=1.87µs  max=3.87ms   p(90)=3.1µs   p(95)=3.87µs   p(99.9)=24.83µs
     http_req_connecting............: avg=241ns   min=0s     med=0s      max=3.82ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.11ms min=8.27ms med=13.71ms max=289.39ms p(90)=17.38ms p(95)=18.65ms  p(99.9)=25.68ms
       { expected_response:true }...: avg=14.11ms min=8.27ms med=13.71ms max=289.39ms p(90)=17.38ms p(95)=18.65ms  p(99.9)=25.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 419146
     http_req_receiving.............: avg=66.48µs min=23.9µs med=41.81µs max=104.73ms p(90)=88.9µs  p(95)=168.49µs p(99.9)=1.73ms 
     http_req_sending...............: avg=31.33µs min=4.23µs med=7.85µs  max=149.71ms p(90)=16.16µs p(95)=92.16µs  p(99.9)=1.73ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.01ms min=8.21ms med=13.61ms max=289.12ms p(90)=17.27ms p(95)=18.54ms  p(99.9)=25.47ms
     http_reqs......................: 419146  3465.239975/s
     iteration_duration.............: avg=14.31ms min=8.45ms med=13.9ms  max=298.58ms p(90)=17.57ms p(95)=18.84ms  p(99.9)=25.89ms
     iterations.....................: 419046  3464.413237/s
     success_rate...................: 100.00% ✓ 419046      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1250526    ✗ 0     
     data_received..................: 37 GB   302 MB/s
     data_sent......................: 501 MB  4.1 MB/s
     http_req_blocked...............: avg=2.8µs   min=921ns   med=2.21µs  max=4.06ms   p(90)=3.51µs  p(95)=4.21µs   p(99.9)=30.27µs
     http_req_connecting............: avg=231ns   min=0s      med=0s      max=4.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.19ms min=8.43ms  med=13.76ms max=273.63ms p(90)=17.36ms p(95)=18.68ms  p(99.9)=26.21ms
       { expected_response:true }...: avg=14.19ms min=8.43ms  med=13.76ms max=273.63ms p(90)=17.36ms p(95)=18.68ms  p(99.9)=26.21ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 416942
     http_req_receiving.............: avg=71.48µs min=24.07µs med=46.48µs max=16.3ms   p(90)=93.12µs p(95)=182.99µs p(99.9)=1.78ms 
     http_req_sending...............: avg=32.18µs min=4.32µs  med=8.38µs  max=119.6ms  p(90)=16.55µs p(95)=100.78µs p(99.9)=1.6ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.08ms min=8.32ms  med=13.66ms max=273.07ms p(90)=17.25ms p(95)=18.56ms  p(99.9)=25.98ms
     http_reqs......................: 416942  3446.73263/s
     iteration_duration.............: avg=14.38ms min=8.64ms  med=13.95ms max=297.18ms p(90)=17.56ms p(95)=18.88ms  p(99.9)=26.43ms
     iterations.....................: 416842  3445.90596/s
     success_rate...................: 100.00% ✓ 416842     ✗ 0     
     vus............................: 50      min=50       max=50  
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 1236252     ✗ 0     
     data_received..................: 36 GB   298 MB/s
     data_sent......................: 495 MB  4.1 MB/s
     http_req_blocked...............: avg=2.47µs  min=811ns   med=1.86µs  max=6.12ms   p(90)=3.16µs  p(95)=4.01µs   p(99.9)=24.21µs
     http_req_connecting............: avg=212ns   min=0s      med=0s      max=3.48ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.35ms min=8.12ms  med=13.92ms max=281.72ms p(90)=17.84ms p(95)=19.22ms  p(99.9)=26.74ms
       { expected_response:true }...: avg=14.35ms min=8.12ms  med=13.92ms max=281.72ms p(90)=17.84ms p(95)=19.22ms  p(99.9)=26.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 412184
     http_req_receiving.............: avg=71.07µs min=24.73µs med=44.44µs max=155.22ms p(90)=94.7µs  p(95)=172.67µs p(99.9)=2.04ms 
     http_req_sending...............: avg=33.03µs min=4.46µs  med=7.92µs  max=186.1ms  p(90)=17.06µs p(95)=92.82µs  p(99.9)=2.07ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.24ms min=8.05ms  med=13.82ms max=281.18ms p(90)=17.73ms p(95)=19.09ms  p(99.9)=26.45ms
     http_reqs......................: 412184  3407.606731/s
     iteration_duration.............: avg=14.55ms min=8.29ms  med=14.12ms max=296.67ms p(90)=18.03ms p(95)=19.41ms  p(99.9)=27ms   
     iterations.....................: 412084  3406.780011/s
     success_rate...................: 100.00% ✓ 412084      ✗ 0     
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

     checks.........................: 100.00% ✓ 1230870     ✗ 0     
     data_received..................: 36 GB   297 MB/s
     data_sent......................: 493 MB  4.1 MB/s
     http_req_blocked...............: avg=2.85µs  min=862ns   med=2.23µs  max=3.96ms   p(90)=3.57µs  p(95)=4.28µs   p(99.9)=29.73µs
     http_req_connecting............: avg=238ns   min=0s      med=0s      max=3.89ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.41ms min=8.19ms  med=13.96ms max=276.09ms p(90)=17.87ms p(95)=19.25ms  p(99.9)=27.35ms
       { expected_response:true }...: avg=14.41ms min=8.19ms  med=13.96ms max=276.09ms p(90)=17.87ms p(95)=19.25ms  p(99.9)=27.35ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 410390
     http_req_receiving.............: avg=70.63µs min=23.47µs med=43.3µs  max=108.39ms p(90)=92.19µs p(95)=181.24µs p(99.9)=1.88ms 
     http_req_sending...............: avg=33µs    min=4.38µs  med=8.46µs  max=92.3ms   p(90)=16.79µs p(95)=99.85µs  p(99.9)=1.98ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.31ms min=8.1ms   med=13.86ms max=275.85ms p(90)=17.76ms p(95)=19.12ms  p(99.9)=27.15ms
     http_reqs......................: 410390  3392.678244/s
     iteration_duration.............: avg=14.61ms min=8.36ms  med=14.15ms max=301.74ms p(90)=18.06ms p(95)=19.44ms  p(99.9)=27.59ms
     iterations.....................: 410290  3391.851548/s
     success_rate...................: 100.00% ✓ 410290      ✗ 0     
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

     checks.........................: 100.00% ✓ 1181811     ✗ 0     
     data_received..................: 34 GB   285 MB/s
     data_sent......................: 474 MB  3.9 MB/s
     http_req_blocked...............: avg=2.99µs  min=962ns   med=2.39µs  max=4.31ms   p(90)=3.81µs  p(95)=4.56µs   p(99.9)=33.73µs
     http_req_connecting............: avg=235ns   min=0s      med=0s      max=4.28ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=15.02ms min=8.56ms  med=14.65ms max=303.58ms p(90)=18.16ms p(95)=19.42ms  p(99.9)=27.61ms
       { expected_response:true }...: avg=15.02ms min=8.56ms  med=14.65ms max=303.58ms p(90)=18.16ms p(95)=19.42ms  p(99.9)=27.61ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 394037
     http_req_receiving.............: avg=73.42µs min=24.37µs med=48µs    max=59.84ms  p(90)=95.22µs p(95)=182.65µs p(99.9)=1.66ms 
     http_req_sending...............: avg=33.37µs min=4.54µs  med=9.05µs  max=123.26ms p(90)=17.25µs p(95)=102.48µs p(99.9)=1.66ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.91ms min=8.51ms  med=14.55ms max=303.06ms p(90)=18.04ms p(95)=19.29ms  p(99.9)=27.36ms
     http_reqs......................: 394037  3257.582229/s
     iteration_duration.............: avg=15.22ms min=8.71ms  med=14.85ms max=318.16ms p(90)=18.35ms p(95)=19.62ms  p(99.9)=27.83ms
     iterations.....................: 393937  3256.755509/s
     success_rate...................: 100.00% ✓ 393937      ✗ 0     
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

     checks.........................: 100.00% ✓ 1031538     ✗ 0     
     data_received..................: 30 GB   248 MB/s
     data_sent......................: 413 MB  3.4 MB/s
     http_req_blocked...............: avg=2.54µs  min=821ns   med=1.9µs   max=4.98ms   p(90)=3.19µs  p(95)=3.97µs   p(99.9)=24.34µs
     http_req_connecting............: avg=267ns   min=0s      med=0s      max=3.93ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.23ms min=11.65ms med=16.83ms max=283.68ms p(90)=20.09ms p(95)=21.28ms  p(99.9)=27.7ms 
       { expected_response:true }...: avg=17.23ms min=11.65ms med=16.83ms max=283.68ms p(90)=20.09ms p(95)=21.28ms  p(99.9)=27.7ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 343946
     http_req_receiving.............: avg=64.92µs min=23.95µs med=43.1µs  max=77.64ms  p(90)=89µs    p(95)=142.43µs p(99.9)=1.49ms 
     http_req_sending...............: avg=27.91µs min=4.42µs  med=8µs     max=151.72ms p(90)=16.22µs p(95)=82.65µs  p(99.9)=1.29ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.14ms min=11.59ms med=16.75ms max=283.48ms p(90)=19.99ms p(95)=21.16ms  p(99.9)=27.48ms
     http_reqs......................: 343946  2833.166327/s
     iteration_duration.............: avg=17.44ms min=11.81ms med=17.03ms max=292.48ms p(90)=20.29ms p(95)=21.48ms  p(99.9)=27.9ms 
     iterations.....................: 343846  2832.342603/s
     success_rate...................: 100.00% ✓ 343846      ✗ 0     
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

     checks.........................: 100.00% ✓ 1017834     ✗ 0     
     data_received..................: 30 GB   245 MB/s
     data_sent......................: 408 MB  3.4 MB/s
     http_req_blocked...............: avg=2.42µs  min=801ns   med=1.8µs   max=3.95ms   p(90)=3.11µs  p(95)=3.85µs   p(99.9)=24.15µs
     http_req_connecting............: avg=259ns   min=0s      med=0s      max=3.92ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.47ms min=11.64ms med=17.06ms max=308.56ms p(90)=20.46ms p(95)=21.67ms  p(99.9)=28.57ms
       { expected_response:true }...: avg=17.47ms min=11.64ms med=17.06ms max=308.56ms p(90)=20.46ms p(95)=21.67ms  p(99.9)=28.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 339378
     http_req_receiving.............: avg=66.29µs min=24.5µs  med=44.98µs max=96.9ms   p(90)=92.12µs p(95)=140.38µs p(99.9)=1.31ms 
     http_req_sending...............: avg=27.33µs min=4.1µs   med=7.72µs  max=206.52ms p(90)=16.2µs  p(95)=79.7µs   p(99.9)=1.3ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.38ms min=11.53ms med=16.97ms max=307.97ms p(90)=20.36ms p(95)=21.56ms  p(99.9)=28.33ms
     http_reqs......................: 339378  2795.493944/s
     iteration_duration.............: avg=17.67ms min=11.84ms med=17.26ms max=324.45ms p(90)=20.65ms p(95)=21.86ms  p(99.9)=28.82ms
     iterations.....................: 339278  2794.670233/s
     success_rate...................: 100.00% ✓ 339278      ✗ 0     
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

     checks.........................: 100.00% ✓ 1012737     ✗ 0     
     data_received..................: 30 GB   243 MB/s
     data_sent......................: 406 MB  3.3 MB/s
     http_req_blocked...............: avg=2.98µs  min=802ns   med=1.87µs  max=8.44ms   p(90)=3.14µs  p(95)=3.85µs  p(99.9)=23.89µs
     http_req_connecting............: avg=730ns   min=0s      med=0s      max=8.4ms    p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=17.56ms min=11.78ms med=17.2ms  max=295.59ms p(90)=20.34ms p(95)=21.48ms p(99.9)=28.08ms
       { expected_response:true }...: avg=17.56ms min=11.78ms med=17.2ms  max=295.59ms p(90)=20.34ms p(95)=21.48ms p(99.9)=28.08ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 337679
     http_req_receiving.............: avg=63.35µs min=23.35µs med=43.03µs max=75.31ms  p(90)=86.05µs p(95)=132.8µs p(99.9)=1.2ms  
     http_req_sending...............: avg=26.7µs  min=4.24µs  med=7.83µs  max=113.85ms p(90)=15.66µs p(95)=77.37µs p(99.9)=1.31ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.47ms min=11.7ms  med=17.11ms max=294.51ms p(90)=20.24ms p(95)=21.37ms p(99.9)=27.84ms
     http_reqs......................: 337679  2781.382484/s
     iteration_duration.............: avg=17.76ms min=12.04ms med=17.39ms max=313.52ms p(90)=20.54ms p(95)=21.67ms p(99.9)=28.31ms
     iterations.....................: 337579  2780.558807/s
     success_rate...................: 100.00% ✓ 337579      ✗ 0     
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

     checks.........................: 100.00% ✓ 994350      ✗ 0     
     data_received..................: 29 GB   239 MB/s
     data_sent......................: 398 MB  3.3 MB/s
     http_req_blocked...............: avg=2.42µs  min=801ns   med=1.8µs   max=4.24ms   p(90)=3µs     p(95)=3.68µs   p(99.9)=24.03µs
     http_req_connecting............: avg=285ns   min=0s      med=0s      max=4.19ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.89ms min=11.81ms med=17.48ms max=272.52ms p(90)=20.88ms p(95)=22.12ms  p(99.9)=29.08ms
       { expected_response:true }...: avg=17.89ms min=11.81ms med=17.48ms max=272.52ms p(90)=20.88ms p(95)=22.12ms  p(99.9)=29.08ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 331550
     http_req_receiving.............: avg=65.16µs min=24.05µs med=44.33µs max=181.48ms p(90)=88.77µs p(95)=137.58µs p(99.9)=1.22ms 
     http_req_sending...............: avg=26.81µs min=4.28µs  med=7.81µs  max=193.68ms p(90)=15.75µs p(95)=77.15µs  p(99.9)=1.29ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.79ms min=11.69ms med=17.39ms max=272.24ms p(90)=20.78ms p(95)=22.01ms  p(99.9)=28.89ms
     http_reqs......................: 331550  2730.791534/s
     iteration_duration.............: avg=18.09ms min=12.09ms med=17.68ms max=303.52ms p(90)=21.08ms p(95)=22.32ms  p(99.9)=29.32ms
     iterations.....................: 331450  2729.96789/s
     success_rate...................: 100.00% ✓ 331450      ✗ 0     
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

     checks.........................: 100.00% ✓ 750609      ✗ 0     
     data_received..................: 22 GB   180 MB/s
     data_sent......................: 301 MB  2.5 MB/s
     http_req_blocked...............: avg=2.8µs   min=882ns   med=2.08µs  max=8.44ms   p(90)=3.62µs  p(95)=4.31µs   p(99.9)=27.67µs 
     http_req_connecting............: avg=352ns   min=0s      med=0s      max=8.41ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.76ms min=17.15ms med=23.41ms max=295.76ms p(90)=26.81ms p(95)=27.9ms   p(99.9)=33.61ms 
       { expected_response:true }...: avg=23.76ms min=17.15ms med=23.41ms max=295.76ms p(90)=26.81ms p(95)=27.9ms   p(99.9)=33.61ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 250303
     http_req_receiving.............: avg=63.26µs min=23.87µs med=47.69µs max=34.36ms  p(90)=90.18µs p(95)=113.27µs p(99.9)=906.93µs
     http_req_sending...............: avg=23.93µs min=4.53µs  med=9.28µs  max=249.43ms p(90)=17.46µs p(95)=23.66µs  p(99.9)=905.48µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.67ms min=17.03ms med=23.32ms max=293.95ms p(90)=26.72ms p(95)=27.81ms  p(99.9)=33.47ms 
     http_reqs......................: 250303  2054.105973/s
     iteration_duration.............: avg=23.97ms min=17.42ms med=23.61ms max=320.05ms p(90)=27.01ms p(95)=28.1ms   p(99.9)=34ms    
     iterations.....................: 250203  2053.285325/s
     success_rate...................: 100.00% ✓ 250203      ✗ 0     
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

     checks.........................: 100.00% ✓ 530901      ✗ 0     
     data_received..................: 16 GB   127 MB/s
     data_sent......................: 213 MB  1.7 MB/s
     http_req_blocked...............: avg=3.22µs  min=791ns   med=2.18µs  max=3.51ms   p(90)=4.56µs   p(95)=5.47µs   p(99.9)=37.42µs
     http_req_connecting............: avg=481ns   min=0s      med=0s      max=3.46ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.65ms min=17.45ms med=33.4ms  max=312.41ms p(90)=39.33ms  p(95)=40.93ms  p(99.9)=49.29ms
       { expected_response:true }...: avg=33.65ms min=17.45ms med=33.4ms  max=312.41ms p(90)=39.33ms  p(95)=40.93ms  p(99.9)=49.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 177067
     http_req_receiving.............: avg=80.31µs min=26.56µs med=54.03µs max=195.08ms p(90)=118.21µs p(95)=159.71µs p(99.9)=1.5ms  
     http_req_sending...............: avg=29.87µs min=4.14µs  med=9.06µs  max=196.66ms p(90)=21.82µs  p(95)=34.06µs  p(99.9)=1.3ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.54ms min=17.37ms med=33.29ms max=311.89ms p(90)=39.22ms  p(95)=40.82ms  p(99.9)=49.13ms
     http_reqs......................: 177067  1452.150615/s
     iteration_duration.............: avg=33.89ms min=20.51ms med=33.63ms max=321.89ms p(90)=39.54ms  p(95)=41.15ms  p(99.9)=49.54ms
     iterations.....................: 176967  1451.330501/s
     success_rate...................: 100.00% ✓ 176967      ✗ 0     
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

     checks.........................: 100.00% ✓ 514362      ✗ 0     
     data_received..................: 15 GB   123 MB/s
     data_sent......................: 206 MB  1.7 MB/s
     http_req_blocked...............: avg=3.12µs  min=971ns   med=2.15µs  max=4.28ms   p(90)=3.73µs  p(95)=4.42µs   p(99.9)=30.25µs 
     http_req_connecting............: avg=633ns   min=0s      med=0s      max=4.22ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.77ms min=18.18ms med=34.21ms max=307.1ms  p(90)=41.49ms p(95)=43.81ms  p(99.9)=55.54ms 
       { expected_response:true }...: avg=34.77ms min=18.18ms med=34.21ms max=307.1ms  p(90)=41.49ms p(95)=43.81ms  p(99.9)=55.54ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 171554
     http_req_receiving.............: avg=69.65µs min=25.64µs med=57.63µs max=162.06ms p(90)=95.62µs p(95)=112.21µs p(99.9)=651.53µs
     http_req_sending...............: avg=21.13µs min=4.67µs  med=10.3µs  max=96.24ms  p(90)=17.08µs p(95)=20.75µs  p(99.9)=750.02µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.67ms min=18.06ms med=34.12ms max=282.53ms p(90)=41.4ms  p(95)=43.72ms  p(99.9)=55.41ms 
     http_reqs......................: 171554  1406.691044/s
     iteration_duration.............: avg=34.98ms min=20.69ms med=34.41ms max=316.18ms p(90)=41.68ms p(95)=44ms     p(99.9)=55.8ms  
     iterations.....................: 171454  1405.871075/s
     success_rate...................: 100.00% ✓ 171454      ✗ 0     
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

     checks.........................: 100.00% ✓ 508479      ✗ 0     
     data_received..................: 15 GB   122 MB/s
     data_sent......................: 204 MB  1.7 MB/s
     http_req_blocked...............: avg=3.84µs  min=971ns   med=2.97µs  max=4.23ms   p(90)=4.62µs  p(95)=5.36µs   p(99.9)=35.78µs 
     http_req_connecting............: avg=568ns   min=0s      med=0s      max=4.19ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.16ms min=18.27ms med=34.63ms max=313.05ms p(90)=41.46ms p(95)=43.75ms  p(99.9)=56.29ms 
       { expected_response:true }...: avg=35.16ms min=18.27ms med=34.63ms max=313.05ms p(90)=41.46ms p(95)=43.75ms  p(99.9)=56.29ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 169593
     http_req_receiving.............: avg=73.24µs min=26.71µs med=61.75µs max=24.94ms  p(90)=98.56µs p(95)=115.43µs p(99.9)=836.75µs
     http_req_sending...............: avg=24.63µs min=4.98µs  med=12.17µs max=152.13ms p(90)=18.33µs p(95)=22.18µs  p(99.9)=781.04µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=35.06ms min=18.21ms med=34.54ms max=312.34ms p(90)=41.36ms p(95)=43.64ms  p(99.9)=56.17ms 
     http_reqs......................: 169593  1390.41724/s
     iteration_duration.............: avg=35.39ms min=21.94ms med=34.85ms max=322.25ms p(90)=41.68ms p(95)=43.97ms  p(99.9)=56.59ms 
     iterations.....................: 169493  1389.597384/s
     success_rate...................: 100.00% ✓ 169493      ✗ 0     
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

     checks.........................: 100.00% ✓ 196716     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 79 MB   645 kB/s
     http_req_blocked...............: avg=5.45µs  min=1.05µs  med=2.69µs  max=78.15ms  p(90)=4.14µs   p(95)=4.74µs   p(99.9)=47.05µs 
     http_req_connecting............: avg=1.35µs  min=0s      med=0s      max=3.56ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=91.16ms min=20.06ms med=89.65ms max=330.61ms p(90)=107.13ms p(95)=115.79ms p(99.9)=212.42ms
       { expected_response:true }...: avg=91.16ms min=20.06ms med=89.65ms max=330.61ms p(90)=107.13ms p(95)=115.79ms p(99.9)=212.42ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 65672
     http_req_receiving.............: avg=80.65µs min=27.74µs med=70.39µs max=83.73ms  p(90)=104.03µs p(95)=116.74µs p(99.9)=527.53µs
     http_req_sending...............: avg=24.22µs min=5.03µs  med=13.73µs max=105.49ms p(90)=19.53µs  p(95)=21.56µs  p(99.9)=514.38µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.06ms min=19.98ms med=89.55ms max=322.85ms p(90)=107.03ms p(95)=115.65ms p(99.9)=211.96ms
     http_reqs......................: 65672   537.280712/s
     iteration_duration.............: avg=91.51ms min=42.03ms med=89.9ms  max=346.22ms p(90)=107.38ms p(95)=116.08ms p(99.9)=213.74ms
     iterations.....................: 65572   536.462585/s
     success_rate...................: 100.00% ✓ 65572      ✗ 0    
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

     checks.........................: 100.00% ✓ 193233     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 78 MB   634 kB/s
     http_req_blocked...............: avg=4.44µs  min=982ns   med=2.86µs  max=3.83ms   p(90)=4.41µs   p(95)=5µs      p(99.9)=41.77µs 
     http_req_connecting............: avg=1.39µs  min=0s      med=0s      max=3.8ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.81ms min=19.9ms  med=91.02ms max=331.47ms p(90)=117.14ms p(95)=125.57ms p(99.9)=159.3ms 
       { expected_response:true }...: avg=92.81ms min=19.9ms  med=91.02ms max=331.47ms p(90)=117.14ms p(95)=125.57ms p(99.9)=159.3ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 64511
     http_req_receiving.............: avg=75.89µs min=26.5µs  med=69.95µs max=45.92ms  p(90)=102.61µs p(95)=114.72µs p(99.9)=558.26µs
     http_req_sending...............: avg=17.22µs min=4.83µs  med=13.44µs max=19.72ms  p(90)=19.46µs  p(95)=21.53µs  p(99.9)=487.69µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.71ms min=19.78ms med=90.93ms max=330.98ms p(90)=117.04ms p(95)=125.47ms p(99.9)=159.18ms
     http_reqs......................: 64511   527.913812/s
     iteration_duration.............: avg=93.16ms min=35.58ms med=91.28ms max=337.54ms p(90)=117.39ms p(95)=125.83ms p(99.9)=161.43ms
     iterations.....................: 64411   527.095481/s
     success_rate...................: 100.00% ✓ 64411      ✗ 0    
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

     checks.........................: 100.00% ✓ 141462     ✗ 0    
     data_received..................: 4.1 GB  34 MB/s
     data_sent......................: 57 MB   464 kB/s
     http_req_blocked...............: avg=4.87µs   min=982ns   med=2.75µs   max=4.12ms   p(90)=4.16µs   p(95)=4.71µs   p(99.9)=353.4µs 
     http_req_connecting............: avg=1.91µs   min=0s      med=0s       max=4.08ms   p(90)=0s       p(95)=0s       p(99.9)=291.75µs
     http_req_duration..............: avg=126.8ms  min=20.67ms med=124.98ms max=374.3ms  p(90)=157.56ms p(95)=168.02ms p(99.9)=216.7ms 
       { expected_response:true }...: avg=126.8ms  min=20.67ms med=124.98ms max=374.3ms  p(90)=157.56ms p(95)=168.02ms p(99.9)=216.7ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 47254
     http_req_receiving.............: avg=78.76µs  min=28.09µs med=70.11µs  max=77.32ms  p(90)=101.09µs p(95)=112.91µs p(99.9)=509.98µs
     http_req_sending...............: avg=23.81µs  min=5µs     med=13.5µs   max=114.38ms p(90)=19.07µs  p(95)=20.85µs  p(99.9)=466.34µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=126.7ms  min=20.6ms  med=124.88ms max=373.84ms p(90)=157.47ms p(95)=167.92ms p(99.9)=215.95ms
     http_reqs......................: 47254   386.285264/s
     iteration_duration.............: avg=127.28ms min=46.05ms med=125.26ms max=383.16ms p(90)=157.85ms p(95)=168.28ms p(99.9)=219.75ms
     iterations.....................: 47154   385.467798/s
     success_rate...................: 100.00% ✓ 47154      ✗ 0    
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

     checks.........................: 100.00% ✓ 98568      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   323 kB/s
     http_req_blocked...............: avg=6.13µs   min=1.11µs  med=2.98µs   max=3.71ms   p(90)=4.33µs   p(95)=4.88µs   p(99.9)=1.49ms  
     http_req_connecting............: avg=2.93µs   min=0s      med=0s       max=3.67ms   p(90)=0s       p(95)=0s       p(99.9)=1.47ms  
     http_req_duration..............: avg=181.94ms min=21.97ms med=182.44ms max=383.26ms p(90)=194.75ms p(95)=199.69ms p(99.9)=261.04ms
       { expected_response:true }...: avg=181.94ms min=21.97ms med=182.44ms max=383.26ms p(90)=194.75ms p(95)=199.69ms p(99.9)=261.04ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32956
     http_req_receiving.............: avg=92.89µs  min=31.22µs med=86.94µs  max=70.55ms  p(90)=115.98µs p(95)=126.79µs p(99.9)=515.92µs
     http_req_sending...............: avg=30.04µs  min=5.47µs  med=16.47µs  max=105.81ms p(90)=20.84µs  p(95)=22.69µs  p(99.9)=542.89µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=181.81ms min=21.87ms med=182.32ms max=382.66ms p(90)=194.64ms p(95)=199.56ms p(99.9)=260.72ms
     http_reqs......................: 32956   268.871987/s
     iteration_duration.............: avg=182.71ms min=40.32ms med=182.8ms  max=400.78ms p(90)=195.02ms p(95)=199.97ms p(99.9)=266.62ms
     iterations.....................: 32856   268.056136/s
     success_rate...................: 100.00% ✓ 32856      ✗ 0    
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

     checks.........................: 100.00% ✓ 94743      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   312 kB/s
     http_req_blocked...............: avg=6.74µs   min=1.48µs  med=3.52µs   max=3.64ms   p(90)=4.93µs   p(95)=5.54µs   p(99.9)=1.51ms  
     http_req_connecting............: avg=2.97µs   min=0s      med=0s       max=3.6ms    p(90)=0s       p(95)=0s       p(99.9)=1.49ms  
     http_req_duration..............: avg=189.28ms min=17.3ms  med=175.77ms max=806.76ms p(90)=219.67ms p(95)=237.31ms p(99.9)=697.69ms
       { expected_response:true }...: avg=189.28ms min=17.3ms  med=175.77ms max=806.76ms p(90)=219.67ms p(95)=237.31ms p(99.9)=697.69ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31681
     http_req_receiving.............: avg=94.33µs  min=34.15µs med=85.41µs  max=64.45ms  p(90)=115.24µs p(95)=126.52µs p(99.9)=918.66µs
     http_req_sending...............: avg=25.16µs  min=6.23µs  med=16.88µs  max=69.1ms   p(90)=21.59µs  p(95)=23.4µs   p(99.9)=571.99µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=189.16ms min=17.16ms med=175.65ms max=806.65ms p(90)=219.56ms p(95)=237.11ms p(99.9)=697.59ms
     http_reqs......................: 31681   259.498956/s
     iteration_duration.............: avg=190.11ms min=49.67ms med=176.16ms max=807.01ms p(90)=220ms    p(95)=237.76ms p(99.9)=697.93ms
     iterations.....................: 31581   258.679857/s
     success_rate...................: 100.00% ✓ 31581      ✗ 0    
     vus............................: 30      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

