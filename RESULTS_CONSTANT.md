## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.14 | 5,428 | 5,452 | 5,400 | 0.4% | 386 MB | 72.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.14 | 5,368 | 5,378 | 5,302 | 0.6% | 380 MB | 72.5 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.14 | 5,286 | 5,295 | 5,273 | 0.2% | 123 MB | 23.8 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.14 | 5,192 | 5,208 | 5,162 | 0.4% | 131 MB | 25.9 KB |  |
| fusion-net-11 | 16.7.5 | 4,977 | 5,019 | 4,945 | 0.6% | 372 MB | 76.6 KB |  |
| fusion-fed-net-11 | 16.7.5 | 4,902 | 4,920 | 4,892 | 0.2% | 389 MB | 81.2 KB |  |
| fusion-aot-11 | 16.7.5 | 4,768 | 4,824 | 4,755 | 0.6% | 132 MB | 28.2 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 4,512 | 4,526 | 4,501 | 0.2% | 128 MB | 29.0 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,322 | 4,486 | 4,230 | 2.3% | 2,304 MB | 545.8 KB |  |
| hive-router | v0.3.10 | 2,947 | 2,950 | 2,921 | 0.5% | 88 MB | 30.7 KB |  |
| grafbase | 0.53.5 | 1,864 | 1,870 | 1,853 | 0.4% | 106 MB | 58.3 KB |  |
| cosmo | 0.365.2 | 1,440 | 1,443 | 1,438 | 0.1% | 172 MB | 122.0 KB |  |
| caliban | 3.2.0 | 1,420 | 1,423 | 1,419 | 0.1% | 4,705 MB | 3,393.0 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 544 | 547 | 543 | 0.3% | 2,736 MB | 5,149.9 KB |  |
| apollo-router | v2.19.0 | 480 | 481 | 479 | 0.1% | 173 MB | 368.9 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 398 | 401 | 397 | 0.4% | 210 MB | 541.1 KB |  |
| hive-gateway | 2.15.6 | 275 | 276 | 274 | 0.3% | 3,610 MB | 13,443.2 KB |  |
| apollo-gateway | 2.14.4 | 268 | 269 | 267 | 0.3% | 2,152 MB | 8,222.3 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.14)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1955730     ✗ 0     
     data_received..................: 57 GB   475 MB/s
     data_sent......................: 784 MB  6.5 MB/s
     http_req_blocked...............: avg=2.5µs   min=831ns    med=1.96µs  max=6.64ms   p(90)=3.01µs  p(95)=3.58µs   p(99.9)=25.93µs
     http_req_connecting............: avg=150ns   min=0s       med=0s      max=4.04ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9ms     min=778.2µs  med=8.1ms   max=288.62ms p(90)=14.43ms p(95)=17.5ms   p(99.9)=30.02ms
       { expected_response:true }...: avg=9ms     min=778.2µs  med=8.1ms   max=288.62ms p(90)=14.43ms p(95)=17.5ms   p(99.9)=30.02ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 652010
     http_req_receiving.............: avg=90.26µs min=25.25µs  med=45.34µs max=72.25ms  p(90)=84.47µs p(95)=184.24µs p(99.9)=5.87ms 
     http_req_sending...............: avg=41.84µs min=4.37µs   med=8.18µs  max=123.66ms p(90)=13.37µs p(95)=96.98µs  p(99.9)=4.81ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.87ms  min=721.67µs med=7.99ms  max=288.13ms p(90)=14.23ms p(95)=17.24ms  p(99.9)=29.54ms
     http_reqs......................: 652010  5428.61143/s
     iteration_duration.............: avg=9.19ms  min=1.03ms   med=8.28ms  max=306.51ms p(90)=14.64ms p(95)=17.72ms  p(99.9)=30.27ms
     iterations.....................: 651910  5427.778834/s
     success_rate...................: 100.00% ✓ 651910      ✗ 0     
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

     checks.........................: 100.00% ✓ 1934235     ✗ 0     
     data_received..................: 56 GB   470 MB/s
     data_sent......................: 775 MB  6.5 MB/s
     http_req_blocked...............: avg=2.53µs  min=751ns    med=1.96µs  max=4.93ms   p(90)=3.18µs  p(95)=3.87µs   p(99.9)=28.79µs
     http_req_connecting............: avg=142ns   min=0s       med=0s      max=3.48ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.09ms  min=800.13µs med=8.16ms  max=240.42ms p(90)=14.57ms p(95)=17.8ms   p(99.9)=30.54ms
       { expected_response:true }...: avg=9.09ms  min=800.13µs med=8.16ms  max=240.42ms p(90)=14.57ms p(95)=17.8ms   p(99.9)=30.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 644845
     http_req_receiving.............: avg=92.05µs min=24.34µs  med=45.83µs max=21.01ms  p(90)=88.81µs p(95)=191.57µs p(99.9)=5.98ms 
     http_req_sending...............: avg=42.22µs min=4.2µs    med=8.13µs  max=227.97ms p(90)=14.02µs p(95)=101.94µs p(99.9)=4.74ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.96ms  min=753.63µs med=8.05ms  max=239.79ms p(90)=14.35ms p(95)=17.52ms  p(99.9)=30.06ms
     http_reqs......................: 644845  5368.83208/s
     iteration_duration.............: avg=9.29ms  min=972.28µs med=8.34ms  max=330.09ms p(90)=14.79ms p(95)=18.03ms  p(99.9)=30.99ms
     iterations.....................: 644745  5367.999502/s
     success_rate...................: 100.00% ✓ 644745      ✗ 0     
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

     checks.........................: 100.00% ✓ 1904421     ✗ 0     
     data_received..................: 56 GB   463 MB/s
     data_sent......................: 763 MB  6.4 MB/s
     http_req_blocked...............: avg=2.4µs   min=772ns    med=1.85µs  max=6.52ms   p(90)=2.94µs  p(95)=3.5µs    p(99.9)=27.71µs
     http_req_connecting............: avg=142ns   min=0s       med=0s      max=4.14ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.25ms  min=856.99µs med=8.39ms  max=305.88ms p(90)=14.73ms p(95)=17.67ms  p(99.9)=29.89ms
       { expected_response:true }...: avg=9.25ms  min=856.99µs med=8.39ms  max=305.88ms p(90)=14.73ms p(95)=17.67ms  p(99.9)=29.89ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 634907
     http_req_receiving.............: avg=89.56µs min=24.22µs  med=44.29µs max=281.73ms p(90)=84.36µs p(95)=190.48µs p(99.9)=5.82ms 
     http_req_sending...............: avg=40.43µs min=4.14µs   med=7.91µs  max=224.42ms p(90)=13.41µs p(95)=100.29µs p(99.9)=4.49ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.12ms  min=781.18µs med=8.28ms  max=298.16ms p(90)=14.52ms p(95)=17.42ms  p(99.9)=29.38ms
     http_reqs......................: 634907  5286.056736/s
     iteration_duration.............: avg=9.44ms  min=1.28ms   med=8.57ms  max=327.53ms p(90)=14.93ms p(95)=17.89ms  p(99.9)=30.25ms
     iterations.....................: 634807  5285.224164/s
     success_rate...................: 100.00% ✓ 634807      ✗ 0     
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

     checks.........................: 100.00% ✓ 1870740     ✗ 0     
     data_received..................: 55 GB   454 MB/s
     data_sent......................: 750 MB  6.2 MB/s
     http_req_blocked...............: avg=3.77µs  min=772ns    med=1.94µs  max=155.58ms p(90)=3µs     p(95)=3.55µs   p(99.9)=26.4µs 
     http_req_connecting............: avg=1.43µs  min=0s       med=0s      max=153.58ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.42ms  min=861.98µs med=8.57ms  max=253.78ms p(90)=14.89ms p(95)=17.81ms  p(99.9)=29.76ms
       { expected_response:true }...: avg=9.42ms  min=861.98µs med=8.57ms  max=253.78ms p(90)=14.89ms p(95)=17.81ms  p(99.9)=29.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 623680
     http_req_receiving.............: avg=89.36µs min=24.37µs  med=45.86µs max=61.46ms  p(90)=85.38µs p(95)=192.93µs p(99.9)=5.46ms 
     http_req_sending...............: avg=41.41µs min=4.56µs   med=8.18µs  max=125.3ms  p(90)=13.63µs p(95)=99.41µs  p(99.9)=4.21ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.29ms  min=802.04µs med=8.47ms  max=202.34ms p(90)=14.69ms p(95)=17.56ms  p(99.9)=29.42ms
     http_reqs......................: 623680  5192.417331/s
     iteration_duration.............: avg=9.61ms  min=1.33ms   med=8.76ms  max=300.53ms p(90)=15.1ms  p(95)=18.03ms  p(99.9)=30ms   
     iterations.....................: 623580  5191.584786/s
     success_rate...................: 100.00% ✓ 623580      ✗ 0     
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

     checks.........................: 100.00% ✓ 1793187     ✗ 0     
     data_received..................: 52 GB   436 MB/s
     data_sent......................: 719 MB  6.0 MB/s
     http_req_blocked...............: avg=3.99µs   min=921ns    med=2.43µs  max=156.58ms p(90)=3.73µs  p(95)=4.42µs   p(99.9)=32.5µs 
     http_req_connecting............: avg=1.14µs   min=0s       med=0s      max=156.55ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.82ms   min=838.08µs med=8.9ms   max=231.04ms p(90)=15.38ms p(95)=18.48ms  p(99.9)=31.34ms
       { expected_response:true }...: avg=9.82ms   min=838.08µs med=8.9ms   max=231.04ms p(90)=15.38ms p(95)=18.48ms  p(99.9)=31.34ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 597829
     http_req_receiving.............: avg=101.84µs min=25.59µs  med=48.37µs max=106.17ms p(90)=96.33µs p(95)=216.65µs p(99.9)=6.38ms 
     http_req_sending...............: avg=46.32µs  min=4.44µs   med=8.83µs  max=75.03ms  p(90)=15.35µs p(95)=107.09µs p(99.9)=5.05ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.67ms   min=768.97µs med=8.78ms  max=183.41ms p(90)=15.15ms p(95)=18.21ms  p(99.9)=30.9ms 
     http_reqs......................: 597829  4977.519876/s
     iteration_duration.............: avg=10.02ms  min=1.25ms   med=9.09ms  max=294.53ms p(90)=15.59ms p(95)=18.7ms   p(99.9)=31.63ms
     iterations.....................: 597729  4976.687277/s
     success_rate...................: 100.00% ✓ 597729      ✗ 0     
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

     checks.........................: 100.00% ✓ 1766631     ✗ 0     
     data_received..................: 52 GB   429 MB/s
     data_sent......................: 708 MB  5.9 MB/s
     http_req_blocked...............: avg=4.75µs  min=811ns    med=1.99µs  max=127.85ms p(90)=3.3µs   p(95)=4.07µs   p(99.9)=28.27µs
     http_req_connecting............: avg=2.21µs  min=0s       med=0s      max=127.73ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.97ms  min=978.84µs med=9.11ms  max=222.34ms p(90)=15.35ms p(95)=18.19ms  p(99.9)=31.32ms
       { expected_response:true }...: avg=9.97ms  min=978.84µs med=9.11ms  max=222.34ms p(90)=15.35ms p(95)=18.19ms  p(99.9)=31.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 588977
     http_req_receiving.............: avg=101.9µs min=24.56µs  med=47.58µs max=28.7ms   p(90)=96.53µs p(95)=201.1µs  p(99.9)=7.03ms 
     http_req_sending...............: avg=45.92µs min=4.37µs   med=8.33µs  max=155.58ms p(90)=16.11µs p(95)=102.81µs p(99.9)=5.06ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.82ms  min=894.46µs med=8.99ms  max=192.42ms p(90)=15.11ms p(95)=17.9ms   p(99.9)=30.66ms
     http_reqs......................: 588977  4902.885131/s
     iteration_duration.............: avg=10.17ms min=1.39ms   med=9.31ms  max=276.9ms  p(90)=15.55ms p(95)=18.41ms  p(99.9)=31.62ms
     iterations.....................: 588877  4902.05269/s
     success_rate...................: 100.00% ✓ 588877      ✗ 0     
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

     checks.........................: 100.00% ✓ 1717935     ✗ 0     
     data_received..................: 50 GB   417 MB/s
     data_sent......................: 688 MB  5.7 MB/s
     http_req_blocked...............: avg=3.22µs  min=831ns    med=1.9µs  max=71.23ms  p(90)=3.04µs  p(95)=3.62µs   p(99.9)=26.97µs
     http_req_connecting............: avg=914ns   min=0s       med=0s     max=71ms     p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.28ms min=930.54µs med=9.59ms max=262.79ms p(90)=15.21ms p(95)=17.68ms  p(99.9)=28.86ms
       { expected_response:true }...: avg=10.28ms min=930.54µs med=9.59ms max=262.79ms p(90)=15.21ms p(95)=17.68ms  p(99.9)=28.86ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 572745
     http_req_receiving.............: avg=92.27µs min=24.6µs   med=45.8µs max=109.22ms p(90)=92.94µs p(95)=211.18µs p(99.9)=5.49ms 
     http_req_sending...............: avg=39.3µs  min=4.13µs   med=8.03µs max=172.93ms p(90)=13.94µs p(95)=101.36µs p(99.9)=3.79ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.15ms min=869.55µs med=9.48ms max=249.58ms p(90)=15.02ms p(95)=17.46ms  p(99.9)=28.47ms
     http_reqs......................: 572745  4768.086183/s
     iteration_duration.............: avg=10.46ms min=1.47ms   med=9.77ms max=284.08ms p(90)=15.41ms p(95)=17.89ms  p(99.9)=29.13ms
     iterations.....................: 572645  4767.253686/s
     success_rate...................: 100.00% ✓ 572645      ✗ 0     
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

     checks.........................: 100.00% ✓ 1626051     ✗ 0     
     data_received..................: 47 GB   395 MB/s
     data_sent......................: 652 MB  5.4 MB/s
     http_req_blocked...............: avg=3.03µs   min=971ns    med=2.42µs  max=6.66ms   p(90)=3.72µs  p(95)=4.36µs   p(99.9)=31.99µs
     http_req_connecting............: avg=185ns    min=0s       med=0s      max=3.69ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.85ms  min=1.01ms   med=10.19ms max=295.1ms  p(90)=16ms    p(95)=18.64ms  p(99.9)=31.34ms
       { expected_response:true }...: avg=10.85ms  min=1.01ms   med=10.19ms max=295.1ms  p(90)=16ms    p(95)=18.64ms  p(99.9)=31.34ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 542117
     http_req_receiving.............: avg=100.86µs min=25.22µs  med=48.15µs max=123.38ms p(90)=99.34µs p(95)=221.49µs p(99.9)=5.96ms 
     http_req_sending...............: avg=42.38µs  min=4.46µs   med=8.76µs  max=147.56ms p(90)=15.57µs p(95)=107.71µs p(99.9)=4.27ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.71ms  min=967.16µs med=10.07ms max=294.89ms p(90)=15.8ms  p(95)=18.39ms  p(99.9)=30.78ms
     http_reqs......................: 542117  4512.359637/s
     iteration_duration.............: avg=11.06ms  min=1.61ms   med=10.38ms max=320.7ms  p(90)=16.21ms p(95)=18.86ms  p(99.9)=31.63ms
     iterations.....................: 542017  4511.527278/s
     success_rate...................: 100.00% ✓ 542017      ✗ 0     
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

     checks.........................: 100.00% ✓ 1557081     ✗ 0     
     data_received..................: 45 GB   378 MB/s
     data_sent......................: 624 MB  5.2 MB/s
     http_req_blocked...............: avg=3.09µs  min=962ns    med=2.51µs  max=4.65ms   p(90)=3.87µs  p(95)=4.54µs   p(99.9)=37.82µs
     http_req_connecting............: avg=172ns   min=0s       med=0s      max=3.84ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.34ms min=710.63µs med=11.11ms max=291.47ms p(90)=17.53ms p(95)=19.96ms  p(99.9)=31.69ms
       { expected_response:true }...: avg=11.34ms min=710.63µs med=11.11ms max=291.47ms p(90)=17.53ms p(95)=19.96ms  p(99.9)=31.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 519127
     http_req_receiving.............: avg=90.39µs min=24.22µs  med=48.26µs max=163.13ms p(90)=96.23µs p(95)=217.93µs p(99.9)=4.8ms  
     http_req_sending...............: avg=43.93µs min=4.41µs   med=9.47µs  max=218.93ms p(90)=16.64µs p(95)=117.8µs  p(99.9)=3.98ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.21ms min=665.75µs med=10.99ms max=291.3ms  p(90)=17.35ms p(95)=19.74ms  p(99.9)=31.34ms
     http_reqs......................: 519127  4322.284859/s
     iteration_duration.............: avg=11.55ms min=1.23ms   med=11.3ms  max=306.28ms p(90)=17.73ms p(95)=20.17ms  p(99.9)=31.97ms
     iterations.....................: 519027  4321.452253/s
     success_rate...................: 100.00% ✓ 519027      ✗ 0     
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

     checks.........................: 100.00% ✓ 1062129     ✗ 0     
     data_received..................: 31 GB   258 MB/s
     data_sent......................: 426 MB  3.5 MB/s
     http_req_blocked...............: avg=3.7µs   min=1.03µs  med=2.63µs  max=9.02ms   p(90)=4.03µs  p(95)=4.7µs    p(99.9)=38.03µs
     http_req_connecting............: avg=733ns   min=0s      med=0s      max=8.98ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.74ms min=1.28ms  med=16.78ms max=270.8ms  p(90)=22.47ms p(95)=24.02ms  p(99.9)=31.15ms
       { expected_response:true }...: avg=16.74ms min=1.28ms  med=16.78ms max=270.8ms  p(90)=22.47ms p(95)=24.02ms  p(99.9)=31.15ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 354143
     http_req_receiving.............: avg=76.85µs min=26.25µs med=54.13µs max=142.05ms p(90)=95.69µs p(95)=182.96µs p(99.9)=1.25ms 
     http_req_sending...............: avg=34.93µs min=4.35µs  med=10.23µs max=149.4ms  p(90)=17.26µs p(95)=110.87µs p(99.9)=1.3ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.62ms min=1.19ms  med=16.66ms max=263.19ms p(90)=22.35ms p(95)=23.9ms   p(99.9)=31.02ms
     http_reqs......................: 354143  2947.058865/s
     iteration_duration.............: avg=16.93ms min=3.07ms  med=16.97ms max=300.57ms p(90)=22.66ms p(95)=24.21ms  p(99.9)=31.36ms
     iterations.....................: 354043  2946.226698/s
     success_rate...................: 100.00% ✓ 354043      ✗ 0     
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

     checks.........................: 100.00% ✓ 672375      ✗ 0     
     data_received..................: 20 GB   163 MB/s
     data_sent......................: 269 MB  2.2 MB/s
     http_req_blocked...............: avg=3.93µs  min=962ns  med=3.06µs  max=3.5ms    p(90)=5.25µs   p(95)=6.28µs   p(99.9)=44.43µs
     http_req_connecting............: avg=382ns   min=0s     med=0s      max=3.46ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.5ms  min=1.86ms med=25.9ms  max=288.14ms p(90)=34.51ms  p(95)=37.36ms  p(99.9)=51.93ms
       { expected_response:true }...: avg=26.5ms  min=1.86ms med=25.9ms  max=288.14ms p(90)=34.51ms  p(95)=37.36ms  p(99.9)=51.93ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 224225
     http_req_receiving.............: avg=93.24µs min=27.1µs med=62.17µs max=62.97ms  p(90)=126.57µs p(95)=216.42µs p(99.9)=2.02ms 
     http_req_sending...............: avg=39.38µs min=4.86µs med=12.07µs max=130.23ms p(90)=25.14µs  p(95)=122.51µs p(99.9)=1.93ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.37ms min=1.79ms med=25.78ms max=280.36ms p(90)=34.37ms  p(95)=37.22ms  p(99.9)=51.63ms
     http_reqs......................: 224225  1864.526076/s
     iteration_duration.............: avg=26.75ms min=2.73ms med=26.13ms max=310.55ms p(90)=34.75ms  p(95)=37.6ms   p(99.9)=52.2ms 
     iterations.....................: 224125  1863.694534/s
     success_rate...................: 100.00% ✓ 224125      ✗ 0     
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

     checks.........................: 100.00% ✓ 519450      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 208 MB  1.7 MB/s
     http_req_blocked...............: avg=3.47µs  min=1.04µs  med=2.65µs  max=3.52ms   p(90)=4.16µs  p(95)=4.82µs   p(99.9)=35.35µs 
     http_req_connecting............: avg=521ns   min=0s      med=0s      max=3.49ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.42ms min=2.08ms  med=33.48ms max=312.53ms p(90)=49.99ms p(95)=55.08ms  p(99.9)=79.49ms 
       { expected_response:true }...: avg=34.42ms min=2.08ms  med=33.48ms max=312.53ms p(90)=49.99ms p(95)=55.08ms  p(99.9)=79.49ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 173250
     http_req_receiving.............: avg=71.49µs min=27.17µs med=61.38µs max=7.02ms   p(90)=95.91µs p(95)=110.65µs p(99.9)=712.35µs
     http_req_sending...............: avg=23.37µs min=5.07µs  med=11.06µs max=236.26ms p(90)=16.27µs p(95)=19.7µs   p(99.9)=763.61µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.33ms min=1.98ms  med=33.39ms max=311.94ms p(90)=49.89ms p(95)=54.99ms  p(99.9)=79.25ms 
     http_reqs......................: 173250  1440.315385/s
     iteration_duration.............: avg=34.64ms min=3.79ms  med=33.68ms max=320.85ms p(90)=50.19ms p(95)=55.29ms  p(99.9)=79.99ms 
     iterations.....................: 173150  1439.484034/s
     success_rate...................: 100.00% ✓ 173150      ✗ 0     
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

     checks.........................: 100.00% ✓ 512589      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 205 MB  1.7 MB/s
     http_req_blocked...............: avg=3.78µs  min=1.11µs  med=2.91µs  max=4.43ms   p(90)=4.49µs  p(95)=5.22µs   p(99.9)=39.08µs 
     http_req_connecting............: avg=562ns   min=0s      med=0s      max=4.39ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.86ms min=2.15ms  med=33.88ms max=301.15ms p(90)=49.45ms p(95)=54.6ms   p(99.9)=82.59ms 
       { expected_response:true }...: avg=34.86ms min=2.15ms  med=33.88ms max=301.15ms p(90)=49.45ms p(95)=54.6ms   p(99.9)=82.59ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 170963
     http_req_receiving.............: avg=76.64µs min=29.13µs med=63.55µs max=121.84ms p(90)=99.58µs p(95)=114.91µs p(99.9)=904.89µs
     http_req_sending...............: avg=22.68µs min=5.07µs  med=12.35µs max=71.88ms  p(90)=18.37µs p(95)=22.06µs  p(99.9)=777.9µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.76ms min=2.04ms  med=33.78ms max=300.88ms p(90)=49.35ms p(95)=54.51ms  p(99.9)=82.24ms 
     http_reqs......................: 170963  1420.981747/s
     iteration_duration.............: avg=35.1ms  min=5.89ms  med=34.1ms  max=320.3ms  p(90)=49.67ms p(95)=54.82ms  p(99.9)=83ms    
     iterations.....................: 170863  1420.150584/s
     success_rate...................: 100.00% ✓ 170863      ✗ 0     
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

     checks.........................: 100.00% ✓ 196530     ✗ 0    
     data_received..................: 5.7 GB  48 MB/s
     data_sent......................: 79 MB   654 kB/s
     http_req_blocked...............: avg=4.01µs  min=992ns   med=2.45µs  max=3.49ms   p(90)=3.82µs   p(95)=4.41µs   p(99.9)=46.76µs 
     http_req_connecting............: avg=1.3µs   min=0s      med=0s      max=3.45ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=91.24ms min=3.93ms  med=88.33ms max=322.32ms p(90)=114.02ms p(95)=127ms    p(99.9)=222.79ms
       { expected_response:true }...: avg=91.24ms min=3.93ms  med=88.33ms max=322.32ms p(90)=114.02ms p(95)=127ms    p(99.9)=222.79ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 65610
     http_req_receiving.............: avg=78.83µs min=28.39µs med=68.52µs max=75.81ms  p(90)=103.14µs p(95)=116.63µs p(99.9)=556.4µs 
     http_req_sending...............: avg=23.9µs  min=4.89µs  med=12.46µs max=102.34ms p(90)=18.4µs   p(95)=20.29µs  p(99.9)=534.45µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.13ms min=3.83ms  med=88.24ms max=321.73ms p(90)=113.91ms p(95)=126.87ms p(99.9)=221.71ms
     http_reqs......................: 65610   544.204841/s
     iteration_duration.............: avg=91.6ms  min=29.91ms med=88.58ms max=337.41ms p(90)=114.26ms p(95)=127.3ms  p(99.9)=224.54ms
     iterations.....................: 65510   543.375387/s
     success_rate...................: 100.00% ✓ 65510      ✗ 0    
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

     checks.........................: 100.00% ✓ 173385     ✗ 0    
     data_received..................: 5.1 GB  42 MB/s
     data_sent......................: 70 MB   577 kB/s
     http_req_blocked...............: avg=4.43µs   min=1.03µs  med=2.59µs   max=3.82ms   p(90)=3.91µs   p(95)=4.42µs   p(99.9)=70.35µs 
     http_req_connecting............: avg=1.62µs   min=0s      med=0s       max=3.78ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=103.42ms min=4.51ms  med=101.31ms max=314.59ms p(90)=139.96ms p(95)=151.8ms  p(99.9)=203.19ms
       { expected_response:true }...: avg=103.42ms min=4.51ms  med=101.31ms max=314.59ms p(90)=139.96ms p(95)=151.8ms  p(99.9)=203.19ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 57895
     http_req_receiving.............: avg=76.92µs  min=29.49µs med=68.87µs  max=94.14ms  p(90)=99.41µs  p(95)=112.04µs p(99.9)=539.76µs
     http_req_sending...............: avg=21.52µs  min=4.85µs  med=12.94µs  max=185.6ms  p(90)=18.54µs  p(95)=20.31µs  p(99.9)=441.68µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=103.33ms min=4.41ms  med=101.21ms max=314.1ms  p(90)=139.86ms p(95)=151.68ms p(99.9)=202.73ms
     http_reqs......................: 57895   480.085498/s
     iteration_duration.............: avg=103.84ms min=19.24ms med=101.58ms max=322.19ms p(90)=140.23ms p(95)=152.08ms p(99.9)=204.42ms
     iterations.....................: 57795   479.256264/s
     success_rate...................: 100.00% ✓ 57795      ✗ 0    
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

     checks.........................: 100.00% ✓ 144054     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   479 kB/s
     http_req_blocked...............: avg=8.85µs   min=1.1µs   med=2.75µs   max=9.12ms   p(90)=4.04µs   p(95)=4.54µs   p(99.9)=1.05ms  
     http_req_connecting............: avg=5.76µs   min=0s      med=0s       max=8.94ms   p(90)=0s       p(95)=0s       p(99.9)=966.01µs
     http_req_duration..............: avg=124.48ms min=5.3ms   med=121.85ms max=327.96ms p(90)=163.39ms p(95)=175.91ms p(99.9)=228.73ms
       { expected_response:true }...: avg=124.48ms min=5.3ms   med=121.85ms max=327.96ms p(90)=163.39ms p(95)=175.91ms p(99.9)=228.73ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48118
     http_req_receiving.............: avg=78.28µs  min=29.62µs med=74.05µs  max=58ms     p(90)=103.59µs p(95)=115.89µs p(99.9)=459.05µs
     http_req_sending...............: avg=22.59µs  min=4.68µs  med=14.13µs  max=104.05ms p(90)=18.81µs  p(95)=20.33µs  p(99.9)=569.03µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=124.38ms min=5.22ms  med=121.76ms max=327.54ms p(90)=163.28ms p(95)=175.79ms p(99.9)=228.53ms
     http_reqs......................: 48118   398.704073/s
     iteration_duration.............: avg=124.98ms min=24.73ms med=122.16ms max=336.44ms p(90)=163.68ms p(95)=176.17ms p(99.9)=232.22ms
     iterations.....................: 48018   397.875477/s
     success_rate...................: 100.00% ✓ 48018      ✗ 0    
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

     checks.........................: 100.00% ✓ 99639      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   330 kB/s
     http_req_blocked...............: avg=5.16µs   min=1.09µs  med=3.03µs   max=2.62ms   p(90)=4.33µs   p(95)=4.92µs   p(99.9)=854.22µs
     http_req_connecting............: avg=1.86µs   min=0s      med=0s       max=2.59ms   p(90)=0s       p(95)=0s       p(99.9)=745.76µs
     http_req_duration..............: avg=180.03ms min=5.68ms  med=164.39ms max=834.21ms p(90)=207.79ms p(95)=236.98ms p(99.9)=685.83ms
       { expected_response:true }...: avg=180.03ms min=5.68ms  med=164.39ms max=834.21ms p(90)=207.79ms p(95)=236.98ms p(99.9)=685.83ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33313
     http_req_receiving.............: avg=94.28µs  min=30.42µs med=87.53µs  max=108.09ms p(90)=117.13µs p(95)=128.61µs p(99.9)=572.06µs
     http_req_sending...............: avg=31.54µs  min=5.14µs  med=16.98µs  max=77.85ms  p(90)=21.04µs  p(95)=22.81µs  p(99.9)=707.57µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=179.91ms min=5.6ms   med=164.28ms max=834.09ms p(90)=207.65ms p(95)=236.69ms p(99.9)=685.72ms
     http_reqs......................: 33313   275.102375/s
     iteration_duration.............: avg=180.82ms min=43.79ms med=164.76ms max=834.48ms p(90)=208.15ms p(95)=237.81ms p(99.9)=686.11ms
     iterations.....................: 33213   274.276564/s
     success_rate...................: 100.00% ✓ 33213      ✗ 0    
     vus............................: 25      min=25       max=50 
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

     checks.........................: 100.00% ✓ 97098      ✗ 0    
     data_received..................: 2.8 GB  24 MB/s
     data_sent......................: 39 MB   322 kB/s
     http_req_blocked...............: avg=5.59µs   min=1.17µs  med=3.32µs   max=3.21ms   p(90)=4.64µs   p(95)=5.19µs   p(99.9)=970.16µs
     http_req_connecting............: avg=2.02µs   min=0s      med=0s       max=3.17ms   p(90)=0s       p(95)=0s       p(99.9)=880.31µs
     http_req_duration..............: avg=184.64ms min=7.56ms  med=178.4ms  max=365.94ms p(90)=206.58ms p(95)=211.66ms p(99.9)=276.47ms
       { expected_response:true }...: avg=184.64ms min=7.56ms  med=178.4ms  max=365.94ms p(90)=206.58ms p(95)=211.66ms p(99.9)=276.47ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32466
     http_req_receiving.............: avg=89.74µs  min=33.13µs med=83.02µs  max=46.92ms  p(90)=111.98µs p(95)=122.16µs p(99.9)=485µs   
     http_req_sending...............: avg=42.11µs  min=5.35µs  med=16.09µs  max=202.51ms p(90)=20.3µs   p(95)=22.12µs  p(99.9)=547.45µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.51ms min=7.47ms  med=178.29ms max=365.87ms p(90)=206.48ms p(95)=211.54ms p(99.9)=275.95ms
     http_reqs......................: 32466   268.399776/s
     iteration_duration.............: avg=185.47ms min=31.83ms med=178.66ms max=372.63ms p(90)=206.86ms p(95)=211.92ms p(99.9)=284.29ms
     iterations.....................: 32366   267.573066/s
     success_rate...................: 100.00% ✓ 32366      ✗ 0    
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

