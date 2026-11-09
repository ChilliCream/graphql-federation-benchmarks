## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 5,059 | 5,069 | 5,050 | 0.2% | 383 MB | 77.5 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 4,981 | 4,993 | 4,976 | 0.1% | 361 MB | 74.2 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,808 | 4,820 | 4,796 | 0.2% | 384 MB | 81.8 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,784 | 4,790 | 4,757 | 0.3% | 385 MB | 82.5 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,749 | 4,771 | 4,721 | 0.4% | 127 MB | 27.3 KB |  |
| fusion-aot-11 | 16.7.3 | 4,733 | 4,743 | 4,720 | 0.2% | 129 MB | 27.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,602 | 4,612 | 4,593 | 0.2% | 126 MB | 28.0 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,544 | 4,570 | 4,525 | 0.5% | 139 MB | 31.3 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,300 | 4,426 | 4,227 | 1.8% | 2,304 MB | 548.7 KB |  |
| hive-router | v0.3.10 | 2,931 | 2,951 | 2,916 | 0.4% | 90 MB | 31.5 KB |  |
| grafbase | 0.53.5 | 1,779 | 1,782 | 1,776 | 0.2% | 103 MB | 59.6 KB |  |
| caliban | 3.2.0 | 1,521 | 1,523 | 1,519 | 0.1% | 5,185 MB | 3,490.5 KB |  |
| cosmo | 0.365.2 | 1,472 | 1,473 | 1,470 | 0.1% | 166 MB | 115.6 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 537 | 538 | 536 | 0.1% | 2,737 MB | 5,218.6 KB |  |
| apollo-router | v2.19.0 | 529 | 529 | 528 | 0.1% | 174 MB | 336.2 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 415 | 421 | 404 | 1.5% | 196 MB | 482.4 KB |  |
| hive-gateway | 2.15.6 | 275 | 276 | 273 | 0.4% | 4,166 MB | 15,513.0 KB |  |
| apollo-gateway | 2.14.4 | 274 | 276 | 273 | 0.5% | 2,135 MB | 7,978.6 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1822902     ✗ 0     
     data_received..................: 53 GB   443 MB/s
     data_sent......................: 730 MB  6.1 MB/s
     http_req_blocked...............: avg=2.98µs  min=952ns    med=2.32µs  max=7.68ms   p(90)=3.52µs  p(95)=4.16µs   p(99.9)=30.18µs
     http_req_connecting............: avg=144ns   min=0s       med=0s      max=3.4ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.66ms  min=824.96µs med=8.76ms  max=330.89ms p(90)=15.13ms p(95)=18.14ms  p(99.9)=30.43ms
       { expected_response:true }...: avg=9.66ms  min=824.96µs med=8.76ms  max=330.89ms p(90)=15.13ms p(95)=18.14ms  p(99.9)=30.43ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 607734
     http_req_receiving.............: avg=93.68µs min=24.39µs  med=46.43µs max=21.82ms  p(90)=88.42µs p(95)=192.95µs p(99.9)=6.2ms  
     http_req_sending...............: avg=43.99µs min=4.48µs   med=8.46µs  max=135.46ms p(90)=14.65µs p(95)=102.47µs p(99.9)=5.08ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.52ms  min=760.77µs med=8.65ms  max=330.27ms p(90)=14.9ms  p(95)=17.88ms  p(99.9)=30.02ms
     http_reqs......................: 607734  5059.743606/s
     iteration_duration.............: avg=9.86ms  min=1.18ms   med=8.95ms  max=349.98ms p(90)=15.34ms p(95)=18.36ms  p(99.9)=30.78ms
     iterations.....................: 607634  5058.911047/s
     success_rate...................: 100.00% ✓ 607634      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1794897     ✗ 0     
     data_received..................: 52 GB   436 MB/s
     data_sent......................: 719 MB  6.0 MB/s
     http_req_blocked...............: avg=2.49µs  min=771ns    med=1.93µs  max=7.69ms   p(90)=2.97µs  p(95)=3.55µs   p(99.9)=26.31µs
     http_req_connecting............: avg=148ns   min=0s       med=0s      max=4.04ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.82ms  min=831.49µs med=9.04ms  max=285.53ms p(90)=14.96ms p(95)=17.63ms  p(99.9)=29.7ms 
       { expected_response:true }...: avg=9.82ms  min=831.49µs med=9.04ms  max=285.53ms p(90)=14.96ms p(95)=17.63ms  p(99.9)=29.7ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 598399
     http_req_receiving.............: avg=94.38µs min=24.95µs  med=46.97µs max=55.21ms  p(90)=89.09µs p(95)=193.35µs p(99.9)=6.26ms 
     http_req_sending...............: avg=40.92µs min=4.34µs   med=8.17µs  max=170.63ms p(90)=14.1µs  p(95)=98.3µs   p(99.9)=4.4ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.68ms  min=762.18µs med=8.93ms  max=285.07ms p(90)=14.75ms p(95)=17.37ms  p(99.9)=29.17ms
     http_reqs......................: 598399  4981.919032/s
     iteration_duration.............: avg=10.01ms min=1.07ms   med=9.23ms  max=296.84ms p(90)=15.17ms p(95)=17.84ms  p(99.9)=30.02ms
     iterations.....................: 598299  4981.086491/s
     success_rate...................: 100.00% ✓ 598299      ✗ 0     
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

     checks.........................: 100.00% ✓ 1732695     ✗ 0     
     data_received..................: 51 GB   421 MB/s
     data_sent......................: 694 MB  5.8 MB/s
     http_req_blocked...............: avg=3.35µs   min=972ns    med=2.41µs  max=11.49ms  p(90)=3.7µs   p(95)=4.41µs   p(99.9)=32.41µs
     http_req_connecting............: avg=450ns    min=0s       med=0s      max=11.47ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.16ms  min=1.03ms   med=9.31ms  max=314.95ms p(90)=15.66ms p(95)=18.59ms  p(99.9)=31.6ms 
       { expected_response:true }...: avg=10.16ms  min=1.03ms   med=9.31ms  max=314.95ms p(90)=15.66ms p(95)=18.59ms  p(99.9)=31.6ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 577665
     http_req_receiving.............: avg=103.92µs min=26.73µs  med=49.37µs max=34.08ms  p(90)=97.63µs p(95)=205.84µs p(99.9)=6.78ms 
     http_req_sending...............: avg=44.79µs  min=4.73µs   med=8.83µs  max=275.25ms p(90)=16.23µs p(95)=106.24µs p(99.9)=4.99ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.02ms  min=952.08µs med=9.19ms  max=314.07ms p(90)=15.43ms p(95)=18.32ms  p(99.9)=31.05ms
     http_reqs......................: 577665  4808.582103/s
     iteration_duration.............: avg=10.37ms  min=1.41ms   med=9.51ms  max=341.44ms p(90)=15.88ms p(95)=18.82ms  p(99.9)=31.88ms
     iterations.....................: 577565  4807.749686/s
     success_rate...................: 100.00% ✓ 577565      ✗ 0     
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

     checks.........................: 100.00% ✓ 1724013     ✗ 0     
     data_received..................: 50 GB   419 MB/s
     data_sent......................: 691 MB  5.8 MB/s
     http_req_blocked...............: avg=2.58µs   min=781ns    med=1.96µs  max=16.53ms  p(90)=3.17µs  p(95)=3.87µs   p(99.9)=27.5µs 
     http_req_connecting............: avg=69ns     min=0s       med=0s      max=2.46ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.23ms  min=1ms      med=9.47ms  max=281.22ms p(90)=15.46ms p(95)=18.13ms  p(99.9)=30.91ms
       { expected_response:true }...: avg=10.23ms  min=1ms      med=9.47ms  max=281.22ms p(90)=15.46ms p(95)=18.13ms  p(99.9)=30.91ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 574771
     http_req_receiving.............: avg=100.45µs min=25.81µs  med=47.97µs max=200.17ms p(90)=96.31µs p(95)=199.96µs p(99.9)=6.9ms  
     http_req_sending...............: avg=43.11µs  min=4.25µs   med=8.23µs  max=178.84ms p(90)=15.63µs p(95)=100.71µs p(99.9)=4.79ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.08ms  min=922.79µs med=9.35ms  max=265.59ms p(90)=15.24ms p(95)=17.86ms  p(99.9)=30.35ms
     http_reqs......................: 574771  4784.586903/s
     iteration_duration.............: avg=10.43ms  min=1.17ms   med=9.66ms  max=295.51ms p(90)=15.66ms p(95)=18.34ms  p(99.9)=31.22ms
     iterations.....................: 574671  4783.754469/s
     success_rate...................: 100.00% ✓ 574671      ✗ 0     
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

     checks.........................: 100.00% ✓ 1711173     ✗ 0     
     data_received..................: 50 GB   416 MB/s
     data_sent......................: 686 MB  5.7 MB/s
     http_req_blocked...............: avg=3.41µs  min=801ns    med=1.86µs  max=69.13ms  p(90)=2.98µs  p(95)=3.56µs   p(99.9)=29.25µs
     http_req_connecting............: avg=1.17µs  min=0s       med=0s      max=69.09ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.32ms min=908.01µs med=9.68ms  max=242.33ms p(90)=15.21ms p(95)=17.67ms  p(99.9)=28.66ms
       { expected_response:true }...: avg=10.32ms min=908.01µs med=9.68ms  max=242.33ms p(90)=15.21ms p(95)=17.67ms  p(99.9)=28.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 570491
     http_req_receiving.............: avg=91.54µs min=25.65µs  med=46.35µs max=107.85ms p(90)=92.05µs p(95)=203.65µs p(99.9)=5.46ms 
     http_req_sending...............: avg=40.23µs min=4.16µs   med=7.92µs  max=210.56ms p(90)=14.21µs p(95)=102.4µs  p(99.9)=4.05ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.18ms min=847.11µs med=9.57ms  max=234.93ms p(90)=15.02ms p(95)=17.44ms  p(99.9)=28.29ms
     http_reqs......................: 570491  4749.282923/s
     iteration_duration.............: avg=10.51ms min=1.17ms   med=9.86ms  max=279.32ms p(90)=15.4ms  p(95)=17.88ms  p(99.9)=28.89ms
     iterations.....................: 570391  4748.450432/s
     success_rate...................: 100.00% ✓ 570391      ✗ 0     
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

     checks.........................: 100.00% ✓ 1705314     ✗ 0     
     data_received..................: 50 GB   414 MB/s
     data_sent......................: 683 MB  5.7 MB/s
     http_req_blocked...............: avg=2.57µs  min=832ns    med=2.03µs  max=5.55ms   p(90)=3.26µs  p(95)=3.88µs   p(99.9)=29.21µs
     http_req_connecting............: avg=156ns   min=0s       med=0s      max=3.92ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.35ms min=916.32µs med=9.68ms  max=268.5ms  p(90)=15.32ms p(95)=17.85ms  p(99.9)=29.28ms
       { expected_response:true }...: avg=10.35ms min=916.32µs med=9.68ms  max=268.5ms  p(90)=15.32ms p(95)=17.85ms  p(99.9)=29.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 568538
     http_req_receiving.............: avg=91.9µs  min=23.93µs  med=45.34µs max=66.52ms  p(90)=91.78µs p(95)=205.34µs p(99.9)=5.75ms 
     http_req_sending...............: avg=39.13µs min=4.43µs   med=8.12µs  max=98.39ms  p(90)=14.71µs p(95)=104.71µs p(99.9)=3.81ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.22ms min=838.94µs med=9.56ms  max=268.32ms p(90)=15.12ms p(95)=17.61ms  p(99.9)=28.86ms
     http_reqs......................: 568538  4733.077433/s
     iteration_duration.............: avg=10.54ms min=1.43ms   med=9.86ms  max=280.16ms p(90)=15.51ms p(95)=18.06ms  p(99.9)=29.54ms
     iterations.....................: 568438  4732.244933/s
     success_rate...................: 100.00% ✓ 568438      ✗ 0     
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

     checks.........................: 100.00% ✓ 1658550     ✗ 0     
     data_received..................: 48 GB   403 MB/s
     data_sent......................: 665 MB  5.5 MB/s
     http_req_blocked...............: avg=2.62µs  min=791ns   med=2.01µs  max=9.43ms   p(90)=3.34µs  p(95)=4.09µs   p(99.9)=29.31µs
     http_req_connecting............: avg=164ns   min=0s      med=0s      max=4.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.64ms min=1.03ms  med=9.99ms  max=288.65ms p(90)=15.65ms p(95)=18.21ms  p(99.9)=30.57ms
       { expected_response:true }...: avg=10.64ms min=1.03ms  med=9.99ms  max=288.65ms p(90)=15.65ms p(95)=18.21ms  p(99.9)=30.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 552950
     http_req_receiving.............: avg=95.28µs min=24.08µs med=45.75µs max=40.18ms  p(90)=95.91µs p(95)=204.14µs p(99.9)=6.15ms 
     http_req_sending...............: avg=41.28µs min=4.19µs  med=8.35µs  max=22.49ms  p(90)=16.4µs  p(95)=105.76µs p(99.9)=4.26ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.5ms  min=992.7µs med=9.88ms  max=268.95ms p(90)=15.44ms p(95)=17.95ms  p(99.9)=30.04ms
     http_reqs......................: 552950  4602.662875/s
     iteration_duration.............: avg=10.84ms min=1.35ms  med=10.18ms max=298.45ms p(90)=15.85ms p(95)=18.42ms  p(99.9)=30.87ms
     iterations.....................: 552850  4601.830492/s
     success_rate...................: 100.00% ✓ 552850      ✗ 0     
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

     checks.........................: 100.00% ✓ 1637520     ✗ 0     
     data_received..................: 48 GB   398 MB/s
     data_sent......................: 656 MB  5.5 MB/s
     http_req_blocked...............: avg=2.49µs  min=801ns    med=1.89µs  max=4.73ms   p(90)=3.09µs  p(95)=3.77µs   p(99.9)=26.27µs
     http_req_connecting............: avg=156ns   min=0s       med=0s      max=3.32ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.78ms min=1.03ms   med=10.19ms max=277.22ms p(90)=15.67ms p(95)=18.02ms  p(99.9)=29.86ms
       { expected_response:true }...: avg=10.78ms min=1.03ms   med=10.19ms max=277.22ms p(90)=15.67ms p(95)=18.02ms  p(99.9)=29.86ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 545940
     http_req_receiving.............: avg=92.49µs min=24.73µs  med=46.01µs max=45.3ms   p(90)=94.48µs p(95)=200.84µs p(99.9)=5.48ms 
     http_req_sending...............: avg=40.62µs min=4.35µs   med=8.07µs  max=256.78ms p(90)=15.57µs p(95)=102.77µs p(99.9)=4.15ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.65ms min=986.52µs med=10.07ms max=276.8ms  p(90)=15.48ms p(95)=17.78ms  p(99.9)=29.59ms
     http_reqs......................: 545940  4544.029996/s
     iteration_duration.............: avg=10.98ms min=1.63ms   med=10.38ms max=328.92ms p(90)=15.87ms p(95)=18.23ms  p(99.9)=30.15ms
     iterations.....................: 545840  4543.197664/s
     success_rate...................: 100.00% ✓ 545840      ✗ 0     
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

     checks.........................: 100.00% ✓ 1549518     ✗ 0     
     data_received..................: 45 GB   376 MB/s
     data_sent......................: 621 MB  5.2 MB/s
     http_req_blocked...............: avg=2.67µs  min=801ns    med=2.08µs  max=4.54ms   p(90)=3.4µs   p(95)=4.06µs   p(99.9)=32.17µs
     http_req_connecting............: avg=187ns   min=0s       med=0s      max=3.73ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.41ms min=742.26µs med=11.24ms max=279.65ms p(90)=16.91ms p(95)=19ms     p(99.9)=29.35ms
       { expected_response:true }...: avg=11.41ms min=742.26µs med=11.24ms max=279.65ms p(90)=16.91ms p(95)=19ms     p(99.9)=29.35ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 516606
     http_req_receiving.............: avg=81.6µs  min=23.94µs  med=46.22µs max=13.16ms  p(90)=91.77µs p(95)=202.18µs p(99.9)=3.87ms 
     http_req_sending...............: avg=39.3µs  min=4.48µs   med=8.62µs  max=134.99ms p(90)=15.55µs p(95)=110.77µs p(99.9)=3.06ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.29ms min=684.63µs med=11.13ms max=279.24ms p(90)=16.76ms p(95)=18.81ms  p(99.9)=29.11ms
     http_reqs......................: 516606  4300.883717/s
     iteration_duration.............: avg=11.6ms  min=1.16ms   med=11.42ms max=294.31ms p(90)=17.1ms  p(95)=19.19ms  p(99.9)=29.6ms 
     iterations.....................: 516506  4300.05119/s
     success_rate...................: 100.00% ✓ 516506      ✗ 0     
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

     checks.........................: 100.00% ✓ 1056573     ✗ 0     
     data_received..................: 31 GB   256 MB/s
     data_sent......................: 423 MB  3.5 MB/s
     http_req_blocked...............: avg=2.73µs  min=852ns   med=2.16µs  max=3.53ms   p(90)=3.49µs  p(95)=4.15µs   p(99.9)=28.26µs
     http_req_connecting............: avg=268ns   min=0s      med=0s      max=3.51ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.83ms min=1.35ms  med=16.89ms max=265.73ms p(90)=22.62ms p(95)=24.14ms  p(99.9)=31.37ms
       { expected_response:true }...: avg=16.83ms min=1.35ms  med=16.89ms max=265.73ms p(90)=22.62ms p(95)=24.14ms  p(99.9)=31.37ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 352291
     http_req_receiving.............: avg=68.7µs  min=24.56µs med=50.48µs max=208.65ms p(90)=87.34µs p(95)=131.54µs p(99.9)=1.15ms 
     http_req_sending...............: avg=29.96µs min=4.4µs   med=9.37µs  max=88.04ms  p(90)=15.8µs  p(95)=93.24µs  p(99.9)=1.18ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.73ms min=1.29ms  med=16.8ms  max=265.28ms p(90)=22.52ms p(95)=24.03ms  p(99.9)=31.26ms
     http_reqs......................: 352291  2931.368297/s
     iteration_duration.............: avg=17.02ms min=3.57ms  med=17.08ms max=292.34ms p(90)=22.81ms p(95)=24.33ms  p(99.9)=31.6ms 
     iterations.....................: 352191  2930.53621/s
     success_rate...................: 100.00% ✓ 352191      ✗ 0     
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

     checks.........................: 100.00% ✓ 641496      ✗ 0     
     data_received..................: 19 GB   156 MB/s
     data_sent......................: 257 MB  2.1 MB/s
     http_req_blocked...............: avg=3.22µs  min=822ns   med=2.31µs  max=3.6ms    p(90)=4.39µs   p(95)=5.42µs   p(99.9)=40.29µs
     http_req_connecting............: avg=408ns   min=0s      med=0s      max=3.56ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=27.82ms min=1.87ms  med=27.13ms max=285.27ms p(90)=35.98ms  p(95)=38.93ms  p(99.9)=53.3ms 
       { expected_response:true }...: avg=27.82ms min=1.87ms  med=27.13ms max=285.27ms p(90)=35.98ms  p(95)=38.93ms  p(99.9)=53.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 213932
     http_req_receiving.............: avg=80.95µs min=26.97µs med=58.97µs max=131.25ms p(90)=113.45µs p(95)=153.44µs p(99.9)=1.14ms 
     http_req_sending...............: avg=30.35µs min=4.7µs   med=10.16µs max=252.58ms p(90)=21.17µs  p(95)=38.83µs  p(99.9)=1.12ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=27.71ms min=1.8ms   med=27.03ms max=284.61ms p(90)=35.86ms  p(95)=38.8ms   p(99.9)=53.06ms
     http_reqs......................: 213932  1779.008064/s
     iteration_duration.............: avg=28.04ms min=4.51ms  med=27.34ms max=318.44ms p(90)=36.19ms  p(95)=39.14ms  p(99.9)=53.58ms
     iterations.....................: 213832  1778.176488/s
     success_rate...................: 100.00% ✓ 213832      ✗ 0     
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

     checks.........................: 100.00% ✓ 548592      ✗ 0     
     data_received..................: 16 GB   133 MB/s
     data_sent......................: 220 MB  1.8 MB/s
     http_req_blocked...............: avg=3.79µs  min=1µs     med=3.14µs  max=4.14ms   p(90)=4.93µs   p(95)=5.73µs   p(99.9)=38.86µs 
     http_req_connecting............: avg=311ns   min=0s      med=0s      max=2.65ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.54ms min=1.99ms  med=31.66ms max=286.15ms p(90)=46.04ms  p(95)=50.8ms   p(99.9)=75.73ms 
       { expected_response:true }...: avg=32.54ms min=1.99ms  med=31.66ms max=286.15ms p(90)=46.04ms  p(95)=50.8ms   p(99.9)=75.73ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 182964
     http_req_receiving.............: avg=76.85µs min=27.07µs med=64.43µs max=68.1ms   p(90)=104.81µs p(95)=123.12µs p(99.9)=903.5µs 
     http_req_sending...............: avg=26.42µs min=5.12µs  med=13.84µs max=157.12ms p(90)=21.17µs  p(95)=25.25µs  p(99.9)=869.66µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.44ms min=1.93ms  med=31.56ms max=285.97ms p(90)=45.95ms  p(95)=50.69ms  p(99.9)=75.47ms 
     http_reqs......................: 182964  1521.372576/s
     iteration_duration.............: avg=32.8ms  min=5.11ms  med=31.89ms max=294.91ms p(90)=46.27ms  p(95)=51.03ms  p(99.9)=76.39ms 
     iterations.....................: 182864  1520.541062/s
     success_rate...................: 100.00% ✓ 182864      ✗ 0     
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

     checks.........................: 100.00% ✓ 530886      ✗ 0     
     data_received..................: 16 GB   129 MB/s
     data_sent......................: 213 MB  1.8 MB/s
     http_req_blocked...............: avg=2.9µs   min=862ns   med=2.09µs  max=3.6ms    p(90)=3.56µs  p(95)=4.25µs   p(99.9)=27.83µs 
     http_req_connecting............: avg=496ns   min=0s      med=0s      max=3.57ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.68ms min=2.04ms  med=32.83ms max=284.28ms p(90)=48.67ms p(95)=53.61ms  p(99.9)=77.28ms 
       { expected_response:true }...: avg=33.68ms min=2.04ms  med=32.83ms max=284.28ms p(90)=48.67ms p(95)=53.61ms  p(99.9)=77.28ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 177062
     http_req_receiving.............: avg=71.54µs min=26.05µs med=59.45µs max=152.28ms p(90)=94.93µs p(95)=109.47µs p(99.9)=721.55µs
     http_req_sending...............: avg=20.2µs  min=4.62µs  med=9.9µs   max=134.17ms p(90)=16.04µs p(95)=19.56µs  p(99.9)=726.02µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.59ms min=1.98ms  med=32.74ms max=283.8ms  p(90)=48.58ms p(95)=53.52ms  p(99.9)=76.91ms 
     http_reqs......................: 177062  1472.192261/s
     iteration_duration.............: avg=33.89ms min=4.21ms  med=33.03ms max=294.98ms p(90)=48.86ms p(95)=53.8ms   p(99.9)=77.68ms 
     iterations.....................: 176962  1471.360805/s
     success_rate...................: 100.00% ✓ 176962      ✗ 0     
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

     checks.........................: 100.00% ✓ 193959     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   645 kB/s
     http_req_blocked...............: avg=4.24µs  min=1.06µs  med=2.57µs  max=4.24ms   p(90)=4µs      p(95)=4.54µs   p(99.9)=44.43µs 
     http_req_connecting............: avg=1.43µs  min=0s      med=0s      max=4.2ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.44ms min=3.89ms  med=91.12ms max=306.85ms p(90)=115.17ms p(95)=126.27ms p(99.9)=222.4ms 
       { expected_response:true }...: avg=92.44ms min=3.89ms  med=91.12ms max=306.85ms p(90)=115.17ms p(95)=126.27ms p(99.9)=222.4ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 64753
     http_req_receiving.............: avg=83.25µs min=28.48µs med=67.59µs max=159.08ms p(90)=100.53µs p(95)=113.23µs p(99.9)=557.23µs
     http_req_sending...............: avg=20.89µs min=5.27µs  med=12.9µs  max=158.4ms  p(90)=18.73µs  p(95)=20.48µs  p(99.9)=534.77µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.34ms min=3.78ms  med=91.02ms max=306.04ms p(90)=115.06ms p(95)=126.17ms p(99.9)=220.76ms
     http_reqs......................: 64753   537.294798/s
     iteration_duration.............: avg=92.81ms min=14.93ms med=91.35ms max=329.69ms p(90)=115.41ms p(95)=126.58ms p(99.9)=224.75ms
     iterations.....................: 64653   536.465037/s
     success_rate...................: 100.00% ✓ 64653      ✗ 0    
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

     checks.........................: 100.00% ✓ 191223     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   636 kB/s
     http_req_blocked...............: avg=4.68µs  min=1.06µs  med=2.92µs  max=3.46ms   p(90)=4.42µs   p(95)=4.98µs   p(99.9)=48.72µs 
     http_req_connecting............: avg=1.56µs  min=0s      med=0s      max=3.44ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.76ms min=4.41ms  med=91.68ms max=311.83ms p(90)=126.28ms p(95)=136.8ms  p(99.9)=182.91ms
       { expected_response:true }...: avg=93.76ms min=4.41ms  med=91.68ms max=311.83ms p(90)=126.28ms p(95)=136.8ms  p(99.9)=182.91ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63841
     http_req_receiving.............: avg=74.8µs  min=28.53µs med=69.95µs max=9.35ms   p(90)=101.12µs p(95)=113.46µs p(99.9)=498.35µs
     http_req_sending...............: avg=20.89µs min=4.62µs  med=13.75µs max=105.38ms p(90)=19.44µs  p(95)=21.32µs  p(99.9)=506.08µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.66ms min=4.35ms  med=91.59ms max=311.15ms p(90)=126.18ms p(95)=136.71ms p(99.9)=182.39ms
     http_reqs......................: 63841   529.457571/s
     iteration_duration.............: avg=94.14ms min=28.83ms med=91.95ms max=326.74ms p(90)=126.55ms p(95)=137.06ms p(99.9)=184.34ms
     iterations.....................: 63741   528.628233/s
     success_rate...................: 100.00% ✓ 63741      ✗ 0    
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

     checks.........................: 100.00% ✓ 150165     ✗ 0    
     data_received..................: 4.4 GB  36 MB/s
     data_sent......................: 60 MB   499 kB/s
     http_req_blocked...............: avg=9.6µs    min=1.28µs  med=3.35µs   max=9.75ms   p(90)=4.72µs   p(95)=5.29µs   p(99.9)=154.64µs
     http_req_connecting............: avg=5.86µs   min=0s      med=0s       max=9.71ms   p(90)=0s       p(95)=0s       p(99.9)=73.33µs 
     http_req_duration..............: avg=119.41ms min=5.37ms  med=117.12ms max=327.86ms p(90)=156.6ms  p(95)=168.64ms p(99.9)=219.58ms
       { expected_response:true }...: avg=119.41ms min=5.37ms  med=117.12ms max=327.86ms p(90)=156.6ms  p(95)=168.64ms p(99.9)=219.58ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 50155
     http_req_receiving.............: avg=85.37µs  min=31.05µs med=76.93µs  max=92.95ms  p(90)=106.88µs p(95)=118.63µs p(99.9)=506.21µs
     http_req_sending...............: avg=25.58µs  min=5.57µs  med=16.02µs  max=80.63ms  p(90)=21µs     p(95)=22.85µs  p(99.9)=680.66µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=119.3ms  min=5.25ms  med=117.02ms max=322.65ms p(90)=156.51ms p(95)=168.53ms p(99.9)=218.87ms
     http_reqs......................: 50155   415.578011/s
     iteration_duration.............: avg=119.9ms  min=20.31ms med=117.42ms max=344.04ms p(90)=156.87ms p(95)=168.95ms p(99.9)=222.22ms
     iterations.....................: 50055   414.749424/s
     success_rate...................: 100.00% ✓ 50055      ✗ 0    
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

     checks.........................: 100.00% ✓ 99720      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   331 kB/s
     http_req_blocked...............: avg=6.88µs   min=1.39µs  med=3.79µs   max=4.27ms   p(90)=5.28µs   p(95)=5.92µs   p(99.9)=1.18ms  
     http_req_connecting............: avg=2.8µs    min=0s      med=0s       max=4.23ms   p(90)=0s       p(95)=0s       p(99.9)=1.15ms  
     http_req_duration..............: avg=179.8ms  min=5.72ms  med=162.46ms max=777.61ms p(90)=203.25ms p(95)=231.53ms p(99.9)=712.98ms
       { expected_response:true }...: avg=179.8ms  min=5.72ms  med=162.46ms max=777.61ms p(90)=203.25ms p(95)=231.53ms p(99.9)=712.98ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33340
     http_req_receiving.............: avg=94.17µs  min=35.21µs med=88.95µs  max=40.91ms  p(90)=119.22µs p(95)=131.06µs p(99.9)=606.96µs
     http_req_sending...............: avg=25.9µs   min=6.36µs  med=18.38µs  max=99.11ms  p(90)=22.82µs  p(95)=24.7µs   p(99.9)=502.58µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=179.68ms min=5.59ms  med=162.36ms max=777.46ms p(90)=203.13ms p(95)=231.41ms p(99.9)=712.88ms
     http_reqs......................: 33340   275.97557/s
     iteration_duration.............: avg=180.61ms min=39.8ms  med=162.83ms max=777.88ms p(90)=203.65ms p(95)=232.28ms p(99.9)=713.31ms
     iterations.....................: 33240   275.147809/s
     success_rate...................: 100.00% ✓ 33240      ✗ 0    
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

     checks.........................: 100.00% ✓ 99417      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   330 kB/s
     http_req_blocked...............: avg=5.98µs   min=1.14µs  med=3.06µs   max=3.62ms   p(90)=4.33µs   p(95)=4.84µs   p(99.9)=1.26ms  
     http_req_connecting............: avg=2.72µs   min=0s      med=0s       max=3.59ms   p(90)=0s       p(95)=0s       p(99.9)=1.24ms  
     http_req_duration..............: avg=180.32ms min=7.53ms  med=179.42ms max=397.43ms p(90)=205.28ms p(95)=211.4ms  p(99.9)=283.94ms
       { expected_response:true }...: avg=180.32ms min=7.53ms  med=179.42ms max=397.43ms p(90)=205.28ms p(95)=211.4ms  p(99.9)=283.94ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33239
     http_req_receiving.............: avg=90.78µs  min=30.8µs  med=83.87µs  max=84.25ms  p(90)=113.03µs p(95)=123.92µs p(99.9)=538.46µs
     http_req_sending...............: avg=31.1µs   min=5.2µs   med=16.02µs  max=205.42ms p(90)=20.09µs  p(95)=21.88µs  p(99.9)=497.06µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=180.2ms  min=7.44ms  med=179.31ms max=390.07ms p(90)=205.15ms p(95)=211.29ms p(99.9)=283.53ms
     http_reqs......................: 33239   274.715758/s
     iteration_duration.............: avg=181.14ms min=41.68ms med=179.91ms max=408.98ms p(90)=205.56ms p(95)=211.69ms p(99.9)=288.33ms
     iterations.....................: 33139   273.889272/s
     success_rate...................: 100.00% ✓ 33139      ✗ 0    
     vus............................: 5       min=5        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

