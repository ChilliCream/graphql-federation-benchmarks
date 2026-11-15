## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-aot-11 | 16.8.0-p.12 | 3,591 | 3,595 | 3,572 | 0.3% | 126 MB | 35.9 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.12 | 3,576 | 3,578 | 3,551 | 0.3% | 386 MB | 110.6 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.12 | 3,564 | 3,575 | 3,549 | 0.3% | 398 MB | 114.3 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.12 | 3,527 | 3,536 | 3,516 | 0.3% | 150 MB | 43.4 KB |  |
| fusion-net-11 | 16.7.5 | 3,452 | 3,462 | 3,441 | 0.2% | 381 MB | 113.0 KB |  |
| fusion-aot-11 | 16.7.5 | 3,400 | 3,417 | 3,378 | 0.4% | 132 MB | 39.8 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,265 | 3,308 | 3,247 | 0.8% | 2,313 MB | 725.5 KB |  |
| fusion-fed-net-11 | 16.7.5 | 2,776 | 2,782 | 2,767 | 0.3% | 399 MB | 147.3 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 2,728 | 2,757 | 2,718 | 0.7% | 157 MB | 58.8 KB |  |
| hive-router | v0.3.10 | 2,048 | 2,055 | 2,047 | 0.2% | 92 MB | 45.9 KB |  |
| grafbase | 0.53.5 | 1,450 | 1,456 | 1,444 | 0.4% | 100 MB | 70.5 KB |  |
| cosmo | 0.365.2 | 1,409 | 1,411 | 1,407 | 0.1% | 150 MB | 109.2 KB |  |
| caliban | 3.2.0 | 1,386 | 1,388 | 1,385 | 0.1% | 5,008 MB | 3,700.1 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 528 | 530 | 527 | 0.2% | 2,747 MB | 5,326.6 KB |  |
| apollo-router | v2.19.0 | 484 | 485 | 482 | 0.3% | 175 MB | 369.7 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 419 | 419 | 418 | 0.1% | 205 MB | 501.5 KB |  |
| apollo-gateway | 2.14.4 | 271 | 271 | 269 | 0.3% | 2,144 MB | 8,100.6 KB |  |
| hive-gateway | 2.15.6 | 268 | 268 | 267 | 0.2% | 3,705 MB | 14,156.7 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.12)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1302972     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 522 MB  4.3 MB/s
     http_req_blocked...............: avg=2.46µs  min=792ns   med=1.89µs  max=16.11ms  p(90)=3µs     p(95)=3.64µs   p(99.9)=25.36µs
     http_req_connecting............: avg=217ns   min=0s      med=0s      max=4.05ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.61ms min=8.1ms   med=13.19ms max=292.71ms p(90)=16.65ms p(95)=17.91ms  p(99.9)=25.19ms
       { expected_response:true }...: avg=13.61ms min=8.1ms   med=13.19ms max=292.71ms p(90)=16.65ms p(95)=17.91ms  p(99.9)=25.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 434424
     http_req_receiving.............: avg=68.89µs min=25.35µs med=44.54µs max=169.18ms p(90)=89.74µs p(95)=172.28µs p(99.9)=1.64ms 
     http_req_sending...............: avg=31.52µs min=4.47µs  med=8.11µs  max=149.34ms p(90)=15.43µs p(95)=96.09µs  p(99.9)=1.64ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.51ms min=8.05ms  med=13.09ms max=292.59ms p(90)=16.54ms p(95)=17.79ms  p(99.9)=25.02ms
     http_reqs......................: 434424  3591.582753/s
     iteration_duration.............: avg=13.8ms  min=8.24ms  med=13.38ms max=303.07ms p(90)=16.83ms p(95)=18.09ms  p(99.9)=25.4ms 
     iterations.....................: 434324  3590.756007/s
     success_rate...................: 100.00% ✓ 434324      ✗ 0     
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

     checks.........................: 100.00% ✓ 1297479     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 520 MB  4.3 MB/s
     http_req_blocked...............: avg=2.45µs  min=832ns   med=1.92µs  max=3.56ms   p(90)=3.06µs  p(95)=3.74µs   p(99.9)=22.87µs
     http_req_connecting............: avg=204ns   min=0s      med=0s      max=3.5ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.67ms min=8.12ms  med=13.24ms max=280.49ms p(90)=16.84ms p(95)=18.13ms  p(99.9)=25.77ms
       { expected_response:true }...: avg=13.67ms min=8.12ms  med=13.24ms max=280.49ms p(90)=16.84ms p(95)=18.13ms  p(99.9)=25.77ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 432593
     http_req_receiving.............: avg=67.08µs min=23.78µs med=42.21µs max=103.45ms p(90)=87.79µs p(95)=169.42µs p(99.9)=1.78ms 
     http_req_sending...............: avg=31.1µs  min=4.41µs  med=8.08µs  max=81.04ms  p(90)=15.76µs p(95)=93.45µs  p(99.9)=1.87ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.57ms min=8.08ms  med=13.15ms max=279.99ms p(90)=16.73ms p(95)=18.01ms  p(99.9)=25.54ms
     http_reqs......................: 432593  3576.569605/s
     iteration_duration.............: avg=13.86ms min=8.29ms  med=13.44ms max=293.58ms p(90)=17.03ms p(95)=18.32ms  p(99.9)=25.98ms
     iterations.....................: 432493  3575.74283/s
     success_rate...................: 100.00% ✓ 432493      ✗ 0     
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

     checks.........................: 100.00% ✓ 1293330     ✗ 0     
     data_received..................: 38 GB   312 MB/s
     data_sent......................: 518 MB  4.3 MB/s
     http_req_blocked...............: avg=2.47µs  min=802ns   med=1.89µs  max=3.89ms   p(90)=3.14µs  p(95)=3.9µs    p(99.9)=23.95µs
     http_req_connecting............: avg=218ns   min=0s      med=0s      max=3.85ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.71ms min=8.21ms  med=13.29ms max=271.96ms p(90)=16.86ms p(95)=18.13ms  p(99.9)=25.53ms
       { expected_response:true }...: avg=13.71ms min=8.21ms  med=13.29ms max=271.96ms p(90)=16.86ms p(95)=18.13ms  p(99.9)=25.53ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 431210
     http_req_receiving.............: avg=68.47µs min=24.46µs med=43.24µs max=10.83ms  p(90)=92.53µs p(95)=175.24µs p(99.9)=1.77ms 
     http_req_sending...............: avg=31.46µs min=4.44µs  med=8.04µs  max=190.87ms p(90)=16.77µs p(95)=93.77µs  p(99.9)=1.77ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.61ms min=8.13ms  med=13.2ms  max=271.74ms p(90)=16.75ms p(95)=18ms     p(99.9)=25.32ms
     http_reqs......................: 431210  3564.871661/s
     iteration_duration.............: avg=13.91ms min=8.37ms  med=13.49ms max=289.76ms p(90)=17.05ms p(95)=18.32ms  p(99.9)=25.75ms
     iterations.....................: 431110  3564.044947/s
     success_rate...................: 100.00% ✓ 431110      ✗ 0     
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

     checks.........................: 100.00% ✓ 1279620     ✗ 0     
     data_received..................: 37 GB   309 MB/s
     data_sent......................: 513 MB  4.2 MB/s
     http_req_blocked...............: avg=3.31µs  min=891ns  med=2.32µs  max=8.97ms   p(90)=3.66µs  p(95)=4.37µs   p(99.9)=29.66µs
     http_req_connecting............: avg=624ns   min=0s     med=0s      max=8.93ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.86ms min=8.19ms med=13.4ms  max=276.78ms p(90)=17.08ms p(95)=18.44ms  p(99.9)=25.99ms
       { expected_response:true }...: avg=13.86ms min=8.19ms med=13.4ms  max=276.78ms p(90)=17.08ms p(95)=18.44ms  p(99.9)=25.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 426640
     http_req_receiving.............: avg=75.29µs min=23.6µs med=46.14µs max=161.23ms p(90)=96.07µs p(95)=200.47µs p(99.9)=2.03ms 
     http_req_sending...............: avg=34.36µs min=4.36µs med=8.62µs  max=106.3ms  p(90)=16.6µs  p(95)=107.88µs p(99.9)=1.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.75ms min=8.13ms med=13.3ms  max=275.95ms p(90)=16.95ms p(95)=18.29ms  p(99.9)=25.77ms
     http_reqs......................: 426640  3527.247667/s
     iteration_duration.............: avg=14.05ms min=8.38ms med=13.59ms max=292.42ms p(90)=17.27ms p(95)=18.63ms  p(99.9)=26.24ms
     iterations.....................: 426540  3526.420917/s
     success_rate...................: 100.00% ✓ 426540      ✗ 0     
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

     checks.........................: 100.00% ✓ 1252494     ✗ 0     
     data_received..................: 37 GB   302 MB/s
     data_sent......................: 502 MB  4.1 MB/s
     http_req_blocked...............: avg=2.44µs  min=821ns   med=1.85µs  max=5.24ms   p(90)=3.07µs  p(95)=3.79µs   p(99.9)=24.95µs
     http_req_connecting............: avg=236ns   min=0s      med=0s      max=3.71ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.16ms min=8.08ms  med=13.75ms max=281.61ms p(90)=17.56ms p(95)=18.88ms  p(99.9)=26.61ms
       { expected_response:true }...: avg=14.16ms min=8.08ms  med=13.75ms max=281.61ms p(90)=17.56ms p(95)=18.88ms  p(99.9)=26.61ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 417598
     http_req_receiving.............: avg=69.64µs min=23.57µs med=42.12µs max=190.83ms p(90)=91.28µs p(95)=173.86µs p(99.9)=2.07ms 
     http_req_sending...............: avg=31.51µs min=4.42µs  med=7.84µs  max=135.79ms p(90)=16.6µs  p(95)=91.68µs  p(99.9)=1.93ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.06ms min=8.03ms  med=13.65ms max=280.9ms  p(90)=17.46ms p(95)=18.76ms  p(99.9)=26.29ms
     http_reqs......................: 417598  3452.649905/s
     iteration_duration.............: avg=14.36ms min=8.31ms  med=13.94ms max=291.78ms p(90)=17.75ms p(95)=19.07ms  p(99.9)=26.82ms
     iterations.....................: 417498  3451.823118/s
     success_rate...................: 100.00% ✓ 417498      ✗ 0     
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

     checks.........................: 100.00% ✓ 1233651     ✗ 0     
     data_received..................: 36 GB   298 MB/s
     data_sent......................: 494 MB  4.1 MB/s
     http_req_blocked...............: avg=2.42µs  min=821ns   med=1.85µs  max=3.98ms   p(90)=3.14µs  p(95)=3.91µs   p(99.9)=24.86µs
     http_req_connecting............: avg=212ns   min=0s      med=0s      max=3.94ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.38ms min=8.31ms  med=13.97ms max=279.28ms p(90)=17.74ms p(95)=19.09ms  p(99.9)=27.43ms
       { expected_response:true }...: avg=14.38ms min=8.31ms  med=13.97ms max=279.28ms p(90)=17.74ms p(95)=19.09ms  p(99.9)=27.43ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 411317
     http_req_receiving.............: avg=68.72µs min=24.29µs med=42.22µs max=96.29ms  p(90)=91.89µs p(95)=175.41µs p(99.9)=1.89ms 
     http_req_sending...............: avg=30.91µs min=4.15µs  med=7.81µs  max=139.34ms p(90)=16.7µs  p(95)=93.5µs   p(99.9)=1.68ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.28ms min=8.22ms  med=13.87ms max=278.95ms p(90)=17.63ms p(95)=18.97ms  p(99.9)=27.17ms
     http_reqs......................: 411317  3400.157142/s
     iteration_duration.............: avg=14.58ms min=8.45ms  med=14.16ms max=290.24ms p(90)=17.93ms p(95)=19.28ms  p(99.9)=27.65ms
     iterations.....................: 411217  3399.330491/s
     success_rate...................: 100.00% ✓ 411217      ✗ 0     
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

     checks.........................: 100.00% ✓ 1184775     ✗ 0     
     data_received..................: 35 GB   285 MB/s
     data_sent......................: 475 MB  3.9 MB/s
     http_req_blocked...............: avg=3.02µs  min=922ns   med=2.41µs  max=3.56ms   p(90)=3.99µs  p(95)=4.85µs   p(99.9)=32.73µs
     http_req_connecting............: avg=224ns   min=0s      med=0s      max=3.52ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.97ms min=8.23ms  med=14.62ms max=305.08ms p(90)=18.13ms p(95)=19.4ms   p(99.9)=27.86ms
       { expected_response:true }...: avg=14.97ms min=8.23ms  med=14.62ms max=305.08ms p(90)=18.13ms p(95)=19.4ms   p(99.9)=27.86ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 395025
     http_req_receiving.............: avg=73.28µs min=23.52µs med=46.04µs max=29.51ms  p(90)=98.68µs p(95)=190.47µs p(99.9)=1.88ms 
     http_req_sending...............: avg=33.97µs min=4.41µs  med=9.06µs  max=23.99ms  p(90)=19.19µs p(95)=105.91µs p(99.9)=1.89ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.87ms min=8.16ms  med=14.52ms max=304.51ms p(90)=18.02ms p(95)=19.26ms  p(99.9)=27.58ms
     http_reqs......................: 395025  3265.450221/s
     iteration_duration.............: avg=15.18ms min=8.45ms  med=14.82ms max=336.23ms p(90)=18.33ms p(95)=19.6ms   p(99.9)=28.08ms
     iterations.....................: 394925  3264.623577/s
     success_rate...................: 100.00% ✓ 394925      ✗ 0     
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

     checks.........................: 100.00% ✓ 1011009     ✗ 0     
     data_received..................: 30 GB   243 MB/s
     data_sent......................: 405 MB  3.3 MB/s
     http_req_blocked...............: avg=2.99µs  min=891ns   med=2.31µs  max=4.31ms   p(90)=3.84µs  p(95)=4.66µs   p(99.9)=32.65µs
     http_req_connecting............: avg=297ns   min=0s      med=0s      max=4.26ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.58ms min=11.66ms med=17.13ms max=292.88ms p(90)=20.72ms p(95)=22ms     p(99.9)=29.57ms
       { expected_response:true }...: avg=17.58ms min=11.66ms med=17.13ms max=292.88ms p(90)=20.72ms p(95)=22ms     p(99.9)=29.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 337103
     http_req_receiving.............: avg=73.3µs  min=24.42µs med=47.59µs max=236.12ms p(90)=98.23µs p(95)=162.66µs p(99.9)=1.69ms 
     http_req_sending...............: avg=30.16µs min=4.52µs  med=8.76µs  max=103.78ms p(90)=17.87µs p(95)=90.48µs  p(99.9)=1.53ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.47ms min=11.6ms  med=17.03ms max=292.33ms p(90)=20.61ms p(95)=21.88ms  p(99.9)=29.31ms
     http_reqs......................: 337103  2776.699377/s
     iteration_duration.............: avg=17.79ms min=11.86ms med=17.34ms max=314.95ms p(90)=20.92ms p(95)=22.2ms   p(99.9)=29.85ms
     iterations.....................: 337003  2775.875683/s
     success_rate...................: 100.00% ✓ 337003      ✗ 0     
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

     checks.........................: 100.00% ✓ 993567      ✗ 0     
     data_received..................: 29 GB   239 MB/s
     data_sent......................: 398 MB  3.3 MB/s
     http_req_blocked...............: avg=2.71µs  min=831ns   med=2.08µs  max=3.5ms    p(90)=3.55µs  p(95)=4.33µs  p(99.9)=29.02µs
     http_req_connecting............: avg=263ns   min=0s      med=0s      max=3.46ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=17.89ms min=11.79ms med=17.45ms max=295.08ms p(90)=21.03ms p(95)=22.34ms p(99.9)=29.59ms
       { expected_response:true }...: avg=17.89ms min=11.79ms med=17.45ms max=295.08ms p(90)=21.03ms p(95)=22.34ms p(99.9)=29.59ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 331289
     http_req_receiving.............: avg=70.49µs min=24.09µs med=45.21µs max=251.22ms p(90)=93.65µs p(95)=150.6µs p(99.9)=1.48ms 
     http_req_sending...............: avg=28.7µs  min=4.65µs  med=8.47µs  max=171.9ms  p(90)=17.27µs p(95)=85.11µs p(99.9)=1.44ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.79ms min=11.74ms med=17.36ms max=270.23ms p(90)=20.92ms p(95)=22.23ms p(99.9)=29.23ms
     http_reqs......................: 331289  2728.696701/s
     iteration_duration.............: avg=18.1ms  min=11.95ms med=17.66ms max=310.1ms  p(90)=21.23ms p(95)=22.54ms p(99.9)=29.8ms 
     iterations.....................: 331189  2727.87304/s
     success_rate...................: 100.00% ✓ 331189      ✗ 0     
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

     checks.........................: 100.00% ✓ 748695      ✗ 0     
     data_received..................: 22 GB   179 MB/s
     data_sent......................: 300 MB  2.5 MB/s
     http_req_blocked...............: avg=2.95µs  min=862ns   med=2.15µs  max=4.59ms   p(90)=3.75µs  p(95)=4.47µs   p(99.9)=27.52µs 
     http_req_connecting............: avg=448ns   min=0s      med=0s      max=4.54ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.82ms min=17.34ms med=23.49ms max=292.26ms p(90)=26.79ms p(95)=27.86ms  p(99.9)=33.28ms 
       { expected_response:true }...: avg=23.82ms min=17.34ms med=23.49ms max=292.26ms p(90)=26.79ms p(95)=27.86ms  p(99.9)=33.28ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 249665
     http_req_receiving.............: avg=64.51µs min=25.3µs  med=49.91µs max=101.97ms p(90)=88.95µs p(95)=109.67µs p(99.9)=827.47µs
     http_req_sending...............: avg=23.83µs min=4.57µs  med=9.29µs  max=86.86ms  p(90)=16.43µs p(95)=22.03µs  p(99.9)=878.72µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.73ms min=17.28ms med=23.4ms  max=291.44ms p(90)=26.71ms p(95)=27.77ms  p(99.9)=33.13ms 
     http_reqs......................: 249665  2048.68057/s
     iteration_duration.............: avg=24.03ms min=17.5ms  med=23.68ms max=302.66ms p(90)=27ms    p(95)=28.06ms  p(99.9)=33.55ms 
     iterations.....................: 249565  2047.859998/s
     success_rate...................: 100.00% ✓ 249565      ✗ 0     
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

     checks.........................: 100.00% ✓ 530322      ✗ 0     
     data_received..................: 16 GB   127 MB/s
     data_sent......................: 213 MB  1.7 MB/s
     http_req_blocked...............: avg=3.28µs  min=801ns   med=2.18µs  max=4.11ms   p(90)=4.44µs   p(95)=5.36µs   p(99.9)=37.05µs
     http_req_connecting............: avg=539ns   min=0s      med=0s      max=4.06ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.68ms min=17.63ms med=33.37ms max=303.82ms p(90)=39.17ms  p(95)=40.87ms  p(99.9)=50.07ms
       { expected_response:true }...: avg=33.68ms min=17.63ms med=33.37ms max=303.82ms p(90)=39.17ms  p(95)=40.87ms  p(99.9)=50.07ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 176874
     http_req_receiving.............: avg=79.32µs min=25.65µs med=54.57µs max=161.48ms p(90)=116.94µs p(95)=154.97µs p(99.9)=1.26ms 
     http_req_sending...............: avg=28.5µs  min=4.5µs   med=9.08µs  max=223.8ms  p(90)=22.03µs  p(95)=31.38µs  p(99.9)=1.23ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.58ms min=17.41ms med=33.26ms max=286.51ms p(90)=39.08ms  p(95)=40.76ms  p(99.9)=49.78ms
     http_reqs......................: 176874  1450.468323/s
     iteration_duration.............: avg=33.93ms min=20.42ms med=33.6ms  max=315.33ms p(90)=39.4ms   p(95)=41.08ms  p(99.9)=50.37ms
     iterations.....................: 176774  1449.648265/s
     success_rate...................: 100.00% ✓ 176774      ✗ 0     
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

     checks.........................: 100.00% ✓ 515352      ✗ 0     
     data_received..................: 15 GB   123 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=3.73µs  min=932ns   med=2.22µs  max=9.58ms   p(90)=3.71µs  p(95)=4.38µs   p(99.9)=33.11µs 
     http_req_connecting............: avg=1.18µs  min=0s      med=0s      max=9.55ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.71ms min=18.9ms  med=34.16ms max=295.29ms p(90)=41.39ms p(95)=43.68ms  p(99.9)=55.74ms 
       { expected_response:true }...: avg=34.71ms min=18.9ms  med=34.16ms max=295.29ms p(90)=41.39ms p(95)=43.68ms  p(99.9)=55.74ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 171884
     http_req_receiving.............: avg=71.15µs min=27.64µs med=60.06µs max=83.19ms  p(90)=97.81µs p(95)=114.52µs p(99.9)=670.59µs
     http_req_sending...............: avg=23.72µs min=4.7µs   med=10.21µs max=179.11ms p(90)=17.23µs p(95)=20.82µs  p(99.9)=771.59µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.61ms min=18.77ms med=34.07ms max=294.42ms p(90)=41.29ms p(95)=43.59ms  p(99.9)=55.43ms 
     http_reqs......................: 171884  1409.263266/s
     iteration_duration.............: avg=34.92ms min=20.87ms med=34.35ms max=311.96ms p(90)=41.58ms p(95)=43.88ms  p(99.9)=56.05ms 
     iterations.....................: 171784  1408.443374/s
     success_rate...................: 100.00% ✓ 171784      ✗ 0     
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

     checks.........................: 100.00% ✓ 507135      ✗ 0     
     data_received..................: 15 GB   121 MB/s
     data_sent......................: 203 MB  1.7 MB/s
     http_req_blocked...............: avg=3.25µs  min=972ns   med=2.37µs  max=4.1ms    p(90)=3.97µs  p(95)=4.68µs   p(99.9)=30.5µs  
     http_req_connecting............: avg=568ns   min=0s      med=0s      max=4.06ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.26ms min=18.37ms med=34.74ms max=293.65ms p(90)=41.61ms p(95)=43.9ms   p(99.9)=59.8ms  
       { expected_response:true }...: avg=35.26ms min=18.37ms med=34.74ms max=293.65ms p(90)=41.61ms p(95)=43.9ms   p(99.9)=59.8ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 169145
     http_req_receiving.............: avg=69.85µs min=25.81µs med=58.77µs max=5.1ms    p(90)=95.78µs p(95)=112.56µs p(99.9)=819.49µs
     http_req_sending...............: avg=22.5µs  min=4.76µs  med=11.01µs max=149.99ms p(90)=17.59µs p(95)=21.3µs   p(99.9)=731.96µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=35.17ms min=18.24ms med=34.64ms max=293.42ms p(90)=41.52ms p(95)=43.81ms  p(99.9)=59.41ms 
     http_reqs......................: 169145  1386.805704/s
     iteration_duration.............: avg=35.48ms min=21.5ms  med=34.94ms max=309.64ms p(90)=41.82ms p(95)=44.11ms  p(99.9)=60.13ms 
     iterations.....................: 169045  1385.985812/s
     success_rate...................: 100.00% ✓ 169045      ✗ 0     
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

     checks.........................: 100.00% ✓ 193407     ✗ 0    
     data_received..................: 5.7 GB  46 MB/s
     data_sent......................: 78 MB   634 kB/s
     http_req_blocked...............: avg=4.61µs  min=1.06µs  med=2.94µs  max=3.97ms   p(90)=4.4µs    p(95)=5.02µs   p(99.9)=44.18µs 
     http_req_connecting............: avg=1.48µs  min=0s      med=0s      max=3.93ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.72ms min=20.21ms med=90.95ms max=320.67ms p(90)=110.6ms  p(95)=119.97ms p(99.9)=212.6ms 
       { expected_response:true }...: avg=92.72ms min=20.21ms med=90.95ms max=320.67ms p(90)=110.6ms  p(95)=119.97ms p(99.9)=212.6ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 64569
     http_req_receiving.............: avg=77.71µs min=28.16µs med=72µs    max=7.63ms   p(90)=105.75µs p(95)=118.14µs p(99.9)=480.78µs
     http_req_sending...............: avg=19.19µs min=4.78µs  med=13.94µs max=64.91ms  p(90)=19.59µs  p(95)=21.64µs  p(99.9)=509.9µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.63ms min=20.11ms med=90.85ms max=319.74ms p(90)=110.5ms  p(95)=119.87ms p(99.9)=212.52ms
     http_reqs......................: 64569   528.176036/s
     iteration_duration.............: avg=93.08ms min=31.47ms med=91.2ms  max=340.4ms  p(90)=110.86ms p(95)=120.26ms p(99.9)=213.54ms
     iterations.....................: 64469   527.358034/s
     success_rate...................: 100.00% ✓ 64469      ✗ 0    
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

     checks.........................: 100.00% ✓ 177276     ✗ 0    
     data_received..................: 5.2 GB  42 MB/s
     data_sent......................: 71 MB   582 kB/s
     http_req_blocked...............: avg=7.95µs   min=1.2µs   med=3.12µs  max=8.27ms   p(90)=4.56µs   p(95)=5.18µs   p(99.9)=53.73µs 
     http_req_connecting............: avg=4.49µs   min=0s      med=0s      max=8.22ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=101.17ms min=20.45ms med=99.2ms  max=335.18ms p(90)=128.28ms p(95)=137.36ms p(99.9)=179.84ms
       { expected_response:true }...: avg=101.17ms min=20.45ms med=99.2ms  max=335.18ms p(90)=128.28ms p(95)=137.36ms p(99.9)=179.84ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 59192
     http_req_receiving.............: avg=78.85µs  min=30.28µs med=71.67µs max=108.43ms p(90)=103.55µs p(95)=115.45µs p(99.9)=519.68µs
     http_req_sending...............: avg=25.35µs  min=5.44µs  med=14.48µs max=133.44ms p(90)=19.99µs  p(95)=22.06µs  p(99.9)=635.4µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=101.06ms min=20.3ms  med=99.11ms max=323.55ms p(90)=128.19ms p(95)=137.25ms p(99.9)=179.35ms
     http_reqs......................: 59192   484.297716/s
     iteration_duration.............: avg=101.56ms min=29.6ms  med=99.47ms max=349.05ms p(90)=128.55ms p(95)=137.6ms  p(99.9)=182.24ms
     iterations.....................: 59092   483.479535/s
     success_rate...................: 100.00% ✓ 59092      ✗ 0    
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

     checks.........................: 100.00% ✓ 153534     ✗ 0    
     data_received..................: 4.5 GB  37 MB/s
     data_sent......................: 62 MB   503 kB/s
     http_req_blocked...............: avg=5.32µs   min=1.3µs   med=3.36µs   max=3.59ms   p(90)=4.84µs   p(95)=5.46µs   p(99.9)=113.37µs
     http_req_connecting............: avg=1.73µs   min=0s      med=0s       max=3.55ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=116.81ms min=20.68ms med=115.18ms max=337.24ms p(90)=144.33ms p(95)=153.66ms p(99.9)=199.41ms
       { expected_response:true }...: avg=116.81ms min=20.68ms med=115.18ms max=337.24ms p(90)=144.33ms p(95)=153.66ms p(99.9)=199.41ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51278
     http_req_receiving.............: avg=88.15µs  min=31.14µs med=79.19µs  max=100.65ms p(90)=110.92µs p(95)=122.39µs p(99.9)=527.63µs
     http_req_sending...............: avg=25.83µs  min=5.75µs  med=15.8µs   max=145.16ms p(90)=21.4µs   p(95)=23.48µs  p(99.9)=525.85µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=116.7ms  min=20.61ms med=115.08ms max=319.87ms p(90)=144.22ms p(95)=153.52ms p(99.9)=198.34ms
     http_reqs......................: 51278   419.216922/s
     iteration_duration.............: avg=117.26ms min=31.95ms med=115.47ms max=360.67ms p(90)=144.6ms  p(95)=153.94ms p(99.9)=200.28ms
     iterations.....................: 51178   418.399385/s
     success_rate...................: 100.00% ✓ 51178      ✗ 0    
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

     checks.........................: 100.00% ✓ 99483      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   326 kB/s
     http_req_blocked...............: avg=8.03µs   min=1.16µs  med=3.66µs   max=5.63ms   p(90)=5.14µs   p(95)=5.72µs   p(99.9)=1.86ms  
     http_req_connecting............: avg=3.76µs   min=0s      med=0s       max=5.38ms   p(90)=0s       p(95)=0s       p(99.9)=1.58ms  
     http_req_duration..............: avg=180.24ms min=22.68ms med=180.81ms max=364.25ms p(90)=191.75ms p(95)=195.83ms p(99.9)=263.09ms
       { expected_response:true }...: avg=180.24ms min=22.68ms med=180.81ms max=364.25ms p(90)=191.75ms p(95)=195.83ms p(99.9)=263.09ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33261
     http_req_receiving.............: avg=95.48µs  min=35.78µs med=87.85µs  max=85.58ms  p(90)=117.9µs  p(95)=129.35µs p(99.9)=425.28µs
     http_req_sending...............: avg=31.85µs  min=5.75µs  med=17.75µs  max=120.38ms p(90)=22.32µs  p(95)=24.15µs  p(99.9)=711.69µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=180.12ms min=22.6ms  med=180.69ms max=364.07ms p(90)=191.63ms p(95)=195.71ms p(99.9)=263ms   
     http_reqs......................: 33261   271.279953/s
     iteration_duration.............: avg=181.02ms min=39.13ms med=181.22ms max=376.91ms p(90)=192.04ms p(95)=196.11ms p(99.9)=264.78ms
     iterations.....................: 33161   270.464343/s
     success_rate...................: 100.00% ✓ 33161      ✗ 0    
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

     checks.........................: 100.00% ✓ 98064      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   322 kB/s
     http_req_blocked...............: avg=7.2µs    min=1.43µs  med=3.71µs   max=4.2ms    p(90)=5.28µs   p(95)=5.94µs   p(99.9)=1.61ms  
     http_req_connecting............: avg=3.18µs   min=0s      med=0s       max=4.16ms   p(90)=0s       p(95)=0s       p(99.9)=1.58ms  
     http_req_duration..............: avg=182.87ms min=17.3ms  med=169.15ms max=806.59ms p(90)=209.44ms p(95)=227.72ms p(99.9)=715.24ms
       { expected_response:true }...: avg=182.87ms min=17.3ms  med=169.15ms max=806.59ms p(90)=209.44ms p(95)=227.72ms p(99.9)=715.24ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32788
     http_req_receiving.............: avg=96.02µs  min=34.12µs med=89.5µs   max=73.51ms  p(90)=120.07µs p(95)=132.22µs p(99.9)=604.48µs
     http_req_sending...............: avg=27.52µs  min=6.06µs  med=18.14µs  max=66.92ms  p(90)=22.91µs  p(95)=24.86µs  p(99.9)=495.44µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=182.75ms min=17.15ms med=169.04ms max=806.53ms p(90)=209.32ms p(95)=227.55ms p(99.9)=715.1ms 
     http_reqs......................: 32788   268.401349/s
     iteration_duration.............: avg=183.65ms min=58.55ms med=169.54ms max=806.79ms p(90)=209.78ms p(95)=228.35ms p(99.9)=715.48ms
     iterations.....................: 32688   267.582753/s
     success_rate...................: 100.00% ✓ 32688      ✗ 0    
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

