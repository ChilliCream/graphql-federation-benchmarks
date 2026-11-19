## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.16 | 5,479 | 5,494 | 5,418 | 0.5% | 374 MB | 69.9 KB |  |
| fusion-net-11 | 16.7.6 | 5,419 | 5,455 | 5,369 | 0.7% | 383 MB | 72.3 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.16 | 5,363 | 5,387 | 5,330 | 0.4% | 387 MB | 74.0 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.16 | 5,357 | 5,380 | 5,352 | 0.2% | 138 MB | 26.3 KB |  |
| fusion-aot-11 | 16.7.6 | 5,326 | 5,333 | 5,309 | 0.2% | 113 MB | 21.7 KB |  |
| fusion-fed-net-11 | 16.7.6 | 5,316 | 5,335 | 5,309 | 0.2% | 391 MB | 75.4 KB |  |
| fusion-fed-aot-11 | 16.7.6 | 5,282 | 5,297 | 5,261 | 0.3% | 123 MB | 23.8 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.16 | 5,140 | 5,181 | 5,133 | 0.4% | 134 MB | 26.8 KB |  |
| feddi-gateway | 2026-11-03-0517 | 5,107 | 5,118 | 5,102 | 0.1% | 2,283 MB | 457.7 KB |  |
| grafbase | 0.53.5 | 1,894 | 1,895 | 1,888 | 0.1% | 115 MB | 62.3 KB |  |
| cosmo | 0.372.0 | 1,446 | 1,448 | 1,445 | 0.1% | 164 MB | 116.3 KB |  |
| caliban | 3.2.1 | 1,443 | 1,445 | 1,442 | 0.1% | 5,909 MB | 4,192.9 KB |  |
| hive-gateway-router-runtime | 2.15.8 | 593 | 596 | 592 | 0.3% | 2,635 MB | 4,550.8 KB |  |
| apollo-router | v2.19.1 | 487 | 488 | 486 | 0.2% | 175 MB | 367.8 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 397 | 398 | 396 | 0.2% | 197 MB | 507.7 KB |  |
| hive-gateway | 2.15.8 | 288 | 289 | 287 | 0.3% | 3,285 MB | 11,678.9 KB |  |
| apollo-gateway | 2.14.4 | 271 | 273 | 271 | 0.3% | 2,172 MB | 8,207.2 KB |  |
| hive-router | — | — | — | — | — | — | — | benchmark run failed |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1974099     ✗ 0     
     data_received..................: 58 GB   480 MB/s
     data_sent......................: 791 MB  6.6 MB/s
     http_req_blocked...............: avg=2.49µs  min=762ns    med=1.92µs  max=6.16ms   p(90)=3.08µs  p(95)=3.71µs   p(99.9)=27.15µs
     http_req_connecting............: avg=131ns   min=0s       med=0s      max=3.5ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.91ms  min=797.89µs med=7.96ms  max=271.27ms p(90)=14.36ms p(95)=17.61ms  p(99.9)=30.34ms
       { expected_response:true }...: avg=8.91ms  min=797.89µs med=7.96ms  max=271.27ms p(90)=14.36ms p(95)=17.61ms  p(99.9)=30.34ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 658133
     http_req_receiving.............: avg=92.18µs min=25.6µs   med=46.02µs max=174.95ms p(90)=85.9µs  p(95)=185.69µs p(99.9)=5.75ms 
     http_req_sending...............: avg=42.57µs min=4.35µs   med=8.07µs  max=201.66ms p(90)=13.79µs p(95)=99.33µs  p(99.9)=4.87ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.77ms  min=728.26µs med=7.85ms  max=270.7ms  p(90)=14.13ms p(95)=17.34ms  p(99.9)=29.81ms
     http_reqs......................: 658133  5479.567875/s
     iteration_duration.............: avg=9.1ms   min=921.13µs med=8.15ms  max=281.95ms p(90)=14.57ms p(95)=17.83ms  p(99.9)=30.65ms
     iterations.....................: 658033  5478.735283/s
     success_rate...................: 100.00% ✓ 658033      ✗ 0     
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

     checks.........................: 100.00% ✓ 1952229     ✗ 0     
     data_received..................: 57 GB   474 MB/s
     data_sent......................: 782 MB  6.5 MB/s
     http_req_blocked...............: avg=4.69µs  min=882ns    med=2.36µs  max=79.76ms  p(90)=3.54µs  p(95)=4.17µs   p(99.9)=31µs   
     http_req_connecting............: avg=1.9µs   min=0s       med=0s      max=79.72ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.01ms  min=798.04µs med=8.04ms  max=227.97ms p(90)=14.64ms p(95)=18ms     p(99.9)=31.12ms
       { expected_response:true }...: avg=9.01ms  min=798.04µs med=8.04ms  max=227.97ms p(90)=14.64ms p(95)=18ms     p(99.9)=31.12ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 650843
     http_req_receiving.............: avg=98.07µs min=26.17µs  med=47.14µs max=98.56ms  p(90)=87.88µs p(95)=192.85µs p(99.9)=6.72ms 
     http_req_sending...............: avg=47.75µs min=4.19µs   med=8.66µs  max=134.51ms p(90)=14.18µs p(95)=101.63µs p(99.9)=5.31ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.86ms  min=730.42µs med=7.93ms  max=173.58ms p(90)=14.39ms p(95)=17.7ms   p(99.9)=30.44ms
     http_reqs......................: 650843  5419.015357/s
     iteration_duration.............: avg=9.21ms  min=1.11ms   med=8.23ms  max=291.51ms p(90)=14.85ms p(95)=18.22ms  p(99.9)=31.41ms
     iterations.....................: 650743  5418.182743/s
     success_rate...................: 100.00% ✓ 650743      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1932411     ✗ 0     
     data_received..................: 56 GB   469 MB/s
     data_sent......................: 774 MB  6.4 MB/s
     http_req_blocked...............: avg=2.45µs  min=772ns    med=1.9µs   max=6.57ms   p(90)=2.98µs  p(95)=3.58µs   p(99.9)=26.17µs
     http_req_connecting............: avg=144ns   min=0s       med=0s      max=4.14ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.11ms  min=813.39µs med=8.19ms  max=291.62ms p(90)=14.57ms p(95)=17.68ms  p(99.9)=30.08ms
       { expected_response:true }...: avg=9.11ms  min=813.39µs med=8.19ms  max=291.62ms p(90)=14.57ms p(95)=17.68ms  p(99.9)=30.08ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 644237
     http_req_receiving.............: avg=94.58µs min=22.71µs  med=47.11µs max=60.51ms  p(90)=87.73µs p(95)=189.64µs p(99.9)=6.34ms 
     http_req_sending...............: avg=42.37µs min=4.42µs   med=8.13µs  max=215.18ms p(90)=13.66µs p(95)=98.13µs  p(99.9)=4.82ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.97ms  min=745.07µs med=8.08ms  max=291.54ms p(90)=14.35ms p(95)=17.41ms  p(99.9)=29.71ms
     http_reqs......................: 644237  5363.768434/s
     iteration_duration.............: avg=9.3ms   min=983.23µs med=8.37ms  max=300.45ms p(90)=14.78ms p(95)=17.9ms   p(99.9)=30.4ms 
     iterations.....................: 644137  5362.935858/s
     success_rate...................: 100.00% ✓ 644137      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1930092     ✗ 0     
     data_received..................: 56 GB   469 MB/s
     data_sent......................: 773 MB  6.4 MB/s
     http_req_blocked...............: avg=2.39µs  min=802ns    med=1.89µs  max=5.3ms    p(90)=2.96µs  p(95)=3.52µs   p(99.9)=24.29µs
     http_req_connecting............: avg=133ns   min=0s       med=0s      max=3.43ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.12ms  min=825.4µs  med=8.24ms  max=271.61ms p(90)=14.61ms p(95)=17.66ms  p(99.9)=29.96ms
       { expected_response:true }...: avg=9.12ms  min=825.4µs  med=8.24ms  max=271.61ms p(90)=14.61ms p(95)=17.66ms  p(99.9)=29.96ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 643464
     http_req_receiving.............: avg=89.79µs min=23.98µs  med=44.13µs max=157.34ms p(90)=83.94µs p(95)=189.39µs p(99.9)=5.89ms 
     http_req_sending...............: avg=40.32µs min=4.17µs   med=8µs     max=122.01ms p(90)=13.63µs p(95)=99.44µs  p(99.9)=4.53ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.99ms  min=757.77µs med=8.13ms  max=262.62ms p(90)=14.4ms  p(95)=17.41ms  p(99.9)=29.58ms
     http_reqs......................: 643464  5357.394074/s
     iteration_duration.............: avg=9.31ms  min=1.15ms   med=8.42ms  max=282.4ms  p(90)=14.81ms p(95)=17.87ms  p(99.9)=30.21ms
     iterations.....................: 643364  5356.561488/s
     success_rate...................: 100.00% ✓ 643364      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1918824     ✗ 0     
     data_received..................: 56 GB   466 MB/s
     data_sent......................: 769 MB  6.4 MB/s
     http_req_blocked...............: avg=2.81µs  min=802ns    med=1.95µs  max=8.54ms   p(90)=3.07µs  p(95)=3.66µs   p(99.9)=29.63µs
     http_req_connecting............: avg=393ns   min=0s       med=0s      max=8.51ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.17ms  min=818.73µs med=8.25ms  max=277.58ms p(90)=14.72ms p(95)=17.91ms  p(99.9)=30.73ms
       { expected_response:true }...: avg=9.17ms  min=818.73µs med=8.25ms  max=277.58ms p(90)=14.72ms p(95)=17.91ms  p(99.9)=30.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 639708
     http_req_receiving.............: avg=91.96µs min=24.55µs  med=44.99µs max=251.7ms  p(90)=85.43µs p(95)=190.11µs p(99.9)=5.93ms 
     http_req_sending...............: avg=42.14µs min=4.31µs   med=8.21µs  max=134.85ms p(90)=13.89µs p(95)=101.19µs p(99.9)=4.89ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.04ms  min=776.95µs med=8.15ms  max=249.35ms p(90)=14.5ms  p(95)=17.65ms  p(99.9)=30.21ms
     http_reqs......................: 639708  5326.108616/s
     iteration_duration.............: avg=9.37ms  min=1.16ms   med=8.44ms  max=293.61ms p(90)=14.92ms p(95)=18.14ms  p(99.9)=31.01ms
     iterations.....................: 639608  5325.276032/s
     success_rate...................: 100.00% ✓ 639608      ✗ 0     
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

     checks.........................: 100.00% ✓ 1915560     ✗ 0     
     data_received..................: 56 GB   465 MB/s
     data_sent......................: 768 MB  6.4 MB/s
     http_req_blocked...............: avg=2.97µs  min=921ns    med=2.34µs  max=9.03ms   p(90)=3.56µs  p(95)=4.21µs   p(99.9)=34.61µs
     http_req_connecting............: avg=134ns   min=0s       med=0s      max=3.48ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.18ms  min=828.75µs med=8.19ms  max=256.81ms p(90)=14.79ms p(95)=18.16ms  p(99.9)=31.23ms
       { expected_response:true }...: avg=9.18ms  min=828.75µs med=8.19ms  max=256.81ms p(90)=14.79ms p(95)=18.16ms  p(99.9)=31.23ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 638620
     http_req_receiving.............: avg=98.73µs min=24.99µs  med=47.66µs max=110.37ms p(90)=91.01µs p(95)=198.85µs p(99.9)=6.41ms 
     http_req_sending...............: avg=44.57µs min=4.43µs   med=8.63µs  max=86.26ms  p(90)=14.76µs p(95)=105.39µs p(99.9)=5.09ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.04ms  min=759.62µs med=8.08ms  max=255.96ms p(90)=14.54ms p(95)=17.88ms  p(99.9)=30.84ms
     http_reqs......................: 638620  5316.883955/s
     iteration_duration.............: avg=9.38ms  min=1.11ms   med=8.38ms  max=284.87ms p(90)=15ms    p(95)=18.4ms   p(99.9)=31.56ms
     iterations.....................: 638520  5316.051397/s
     success_rate...................: 100.00% ✓ 638520      ✗ 0     
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

     checks.........................: 100.00% ✓ 1903116     ✗ 0     
     data_received..................: 56 GB   462 MB/s
     data_sent......................: 763 MB  6.3 MB/s
     http_req_blocked...............: avg=2.63µs  min=771ns    med=1.89µs  max=7.42ms   p(90)=3.04µs  p(95)=3.67µs   p(99.9)=28.26µs
     http_req_connecting............: avg=252ns   min=0s       med=0s      max=7.39ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.25ms  min=860.72µs med=8.34ms  max=260.51ms p(90)=14.73ms p(95)=17.88ms  p(99.9)=30.58ms
       { expected_response:true }...: avg=9.25ms  min=860.72µs med=8.34ms  max=260.51ms p(90)=14.73ms p(95)=17.88ms  p(99.9)=30.58ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 634472
     http_req_receiving.............: avg=91.04µs min=24.52µs  med=45.33µs max=143.94ms p(90)=87.51µs p(95)=195.04µs p(99.9)=5.91ms 
     http_req_sending...............: avg=42.13µs min=4.17µs   med=7.94µs  max=71.72ms  p(90)=13.79µs p(95)=102.74µs p(99.9)=4.76ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.12ms  min=803.19µs med=8.24ms  max=248.24ms p(90)=14.51ms p(95)=17.61ms  p(99.9)=30.19ms
     http_reqs......................: 634472  5282.342493/s
     iteration_duration.............: avg=9.44ms  min=1.36ms   med=8.53ms  max=287.79ms p(90)=14.93ms p(95)=18.1ms   p(99.9)=30.86ms
     iterations.....................: 634372  5281.509936/s
     success_rate...................: 100.00% ✓ 634372      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1851975     ✗ 0     
     data_received..................: 54 GB   450 MB/s
     data_sent......................: 742 MB  6.2 MB/s
     http_req_blocked...............: avg=2.54µs  min=801ns    med=1.98µs max=5.84ms   p(90)=3.12µs  p(95)=3.72µs   p(99.9)=26.49µs
     http_req_connecting............: avg=149ns   min=0s       med=0s     max=3.65ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.51ms  min=828.57µs med=8.61ms max=275.59ms p(90)=15.12ms p(95)=18.21ms  p(99.9)=30.58ms
       { expected_response:true }...: avg=9.51ms  min=828.57µs med=8.61ms max=275.59ms p(90)=15.12ms p(95)=18.21ms  p(99.9)=30.58ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 617425
     http_req_receiving.............: avg=93.93µs min=24.77µs  med=46.9µs max=55.45ms  p(90)=90.16µs p(95)=201.15µs p(99.9)=5.79ms 
     http_req_sending...............: avg=42.29µs min=4.47µs   med=8.24µs max=143.83ms p(90)=14.06µs p(95)=103.58µs p(99.9)=4.84ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.37ms  min=760.12µs med=8.49ms max=275.46ms p(90)=14.9ms  p(95)=17.94ms  p(99.9)=30.2ms 
     http_reqs......................: 617425  5140.448238/s
     iteration_duration.............: avg=9.7ms   min=1.35ms   med=8.79ms max=289.08ms p(90)=15.32ms p(95)=18.43ms  p(99.9)=30.92ms
     iterations.....................: 617325  5139.615676/s
     success_rate...................: 100.00% ✓ 617325      ✗ 0     
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

     checks.........................: 100.00% ✓ 1840014     ✗ 0     
     data_received..................: 54 GB   446 MB/s
     data_sent......................: 737 MB  6.1 MB/s
     http_req_blocked...............: avg=2.67µs  min=802ns    med=1.98µs  max=9.53ms   p(90)=3.21µs  p(95)=3.86µs   p(99.9)=28.87µs
     http_req_connecting............: avg=194ns   min=0s       med=0s      max=4.32ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.57ms  min=696.34µs med=8.67ms  max=263.64ms p(90)=14.77ms p(95)=18.18ms  p(99.9)=29.85ms
       { expected_response:true }...: avg=9.57ms  min=696.34µs med=8.67ms  max=263.64ms p(90)=14.77ms p(95)=18.18ms  p(99.9)=29.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 613438
     http_req_receiving.............: avg=95.58µs min=24.61µs  med=46.25µs max=123.78ms p(90)=89.9µs  p(95)=194.35µs p(99.9)=6.75ms 
     http_req_sending...............: avg=44.7µs  min=4.45µs   med=8.33µs  max=200.24ms p(90)=14.7µs  p(95)=107.67µs p(99.9)=4.94ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.43ms  min=620.32µs med=8.58ms  max=263.08ms p(90)=14.48ms p(95)=17.9ms   p(99.9)=29.33ms
     http_reqs......................: 613438  5107.87789/s
     iteration_duration.............: avg=9.77ms  min=1.06ms   med=8.86ms  max=282.31ms p(90)=14.99ms p(95)=18.4ms   p(99.9)=30.13ms
     iterations.....................: 613338  5107.045226/s
     success_rate...................: 100.00% ✓ 613338      ✗ 0     
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

     checks.........................: 100.00% ✓ 683298      ✗ 0     
     data_received..................: 20 GB   166 MB/s
     data_sent......................: 274 MB  2.3 MB/s
     http_req_blocked...............: avg=3.17µs  min=821ns   med=2.24µs  max=4.17ms   p(90)=4.3µs    p(95)=5.28µs   p(99.9)=34.55µs
     http_req_connecting............: avg=416ns   min=0s      med=0s      max=4.13ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.1ms  min=1.91ms  med=25.63ms max=301.02ms p(90)=33.93ms  p(95)=36.62ms  p(99.9)=49.63ms
       { expected_response:true }...: avg=26.1ms  min=1.91ms  med=25.63ms max=301.02ms p(90)=33.93ms  p(95)=36.62ms  p(99.9)=49.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 227866
     http_req_receiving.............: avg=97.43µs min=26.15µs med=54.91µs max=190.18ms p(90)=117.91µs p(95)=191.18µs p(99.9)=1.92ms 
     http_req_sending...............: avg=34.38µs min=4.52µs  med=9.38µs  max=251.89ms p(90)=22.09µs  p(95)=102.8µs  p(99.9)=1.49ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=25.97ms min=1.81ms  med=25.52ms max=160.68ms p(90)=33.81ms  p(95)=36.48ms  p(99.9)=49.16ms
     http_reqs......................: 227866  1894.853371/s
     iteration_duration.............: avg=26.33ms min=2.78ms  med=25.84ms max=327.11ms p(90)=34.14ms  p(95)=36.84ms  p(99.9)=49.96ms
     iterations.....................: 227766  1894.021806/s
     success_rate...................: 100.00% ✓ 227766      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.372.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 521598      ✗ 0     
     data_received..................: 15 GB   127 MB/s
     data_sent......................: 209 MB  1.7 MB/s
     http_req_blocked...............: avg=3.48µs  min=1.08µs med=2.66µs  max=4.25ms   p(90)=4.11µs   p(95)=4.78µs   p(99.9)=33.82µs 
     http_req_connecting............: avg=540ns   min=0s     med=0s      max=4.21ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.27ms min=2.01ms med=33.35ms max=304.17ms p(90)=49.76ms  p(95)=54.83ms  p(99.9)=78.37ms 
       { expected_response:true }...: avg=34.27ms min=2.01ms med=33.35ms max=304.17ms p(90)=49.76ms  p(95)=54.83ms  p(99.9)=78.37ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 173966
     http_req_receiving.............: avg=76.2µs  min=28.5µs med=64.16µs max=178.78ms p(90)=100.96µs p(95)=117.16µs p(99.9)=756.25µs
     http_req_sending...............: avg=22.75µs min=4.9µs  med=11.17µs max=171.77ms p(90)=16.93µs  p(95)=20.85µs  p(99.9)=773.23µs
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.17ms min=1.96ms med=33.26ms max=289.74ms p(90)=49.67ms  p(95)=54.73ms  p(99.9)=77.97ms 
     http_reqs......................: 173966  1446.54765/s
     iteration_duration.............: avg=34.5ms  min=4.29ms med=33.56ms max=320.65ms p(90)=49.97ms  p(95)=55.05ms  p(99.9)=78.93ms 
     iterations.....................: 173866  1445.716138/s
     success_rate...................: 100.00% ✓ 173866      ✗ 0     
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

     checks.........................: 100.00% ✓ 520635      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 209 MB  1.7 MB/s
     http_req_blocked...............: avg=3.59µs  min=892ns   med=2.16µs  max=6.48ms   p(90)=3.6µs   p(95)=4.26µs   p(99.9)=29.75µs 
     http_req_connecting............: avg=1.11µs  min=0s      med=0s      max=6.44ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.33ms min=2.22ms  med=33.32ms max=258.42ms p(90)=49.04ms p(95)=54.16ms  p(99.9)=82.62ms 
       { expected_response:true }...: avg=34.33ms min=2.22ms  med=33.32ms max=258.42ms p(90)=49.04ms p(95)=54.16ms  p(99.9)=82.62ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 173645
     http_req_receiving.............: avg=66.52µs min=26.35µs med=56.33µs max=28.62ms  p(90)=90.8µs  p(95)=105.01µs p(99.9)=715.15µs
     http_req_sending...............: avg=20.25µs min=4.76µs  med=10.88µs max=91.14ms  p(90)=16.96µs p(95)=20.31µs  p(99.9)=736.4µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.25ms min=2.13ms  med=33.24ms max=256.09ms p(90)=48.95ms p(95)=54.08ms  p(99.9)=82.4ms  
     http_reqs......................: 173645  1443.673519/s
     iteration_duration.............: avg=34.56ms min=4.45ms  med=33.53ms max=300.23ms p(90)=49.24ms p(95)=54.38ms  p(99.9)=83.42ms 
     iterations.....................: 173545  1442.842125/s
     success_rate...................: 100.00% ✓ 173545      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 214281     ✗ 0    
     data_received..................: 6.3 GB  52 MB/s
     data_sent......................: 86 MB   713 kB/s
     http_req_blocked...............: avg=3.66µs  min=992ns   med=2.19µs  max=3.53ms   p(90)=3.5µs    p(95)=4.06µs   p(99.9)=47.15µs 
     http_req_connecting............: avg=1.19µs  min=0s      med=0s      max=3.49ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=83.69ms min=3.55ms  med=80.83ms max=328.94ms p(90)=102.85ms p(95)=114.7ms  p(99.9)=218.88ms
       { expected_response:true }...: avg=83.69ms min=3.55ms  med=80.83ms max=328.94ms p(90)=102.85ms p(95)=114.7ms  p(99.9)=218.88ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 71527
     http_req_receiving.............: avg=74.05µs min=27.21µs med=64.84µs max=74.51ms  p(90)=97.19µs  p(95)=109.98µs p(99.9)=506.07µs
     http_req_sending...............: avg=19.44µs min=4.85µs  med=11.2µs  max=134.03ms p(90)=17.07µs  p(95)=18.84µs  p(99.9)=541.95µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=83.59ms min=3.44ms  med=80.75ms max=328.37ms p(90)=102.76ms p(95)=114.62ms p(99.9)=218.54ms
     http_reqs......................: 71527   593.564376/s
     iteration_duration.............: avg=84.01ms min=14.5ms  med=81.06ms max=335.43ms p(90)=103.07ms p(95)=114.96ms p(99.9)=219.96ms
     iterations.....................: 71427   592.73453/s
     success_rate...................: 100.00% ✓ 71427      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 176052     ✗ 0    
     data_received..................: 5.1 GB  43 MB/s
     data_sent......................: 71 MB   585 kB/s
     http_req_blocked...............: avg=4.38µs   min=1.08µs  med=2.74µs  max=3.47ms   p(90)=4.07µs   p(95)=4.59µs   p(99.9)=50.91µs 
     http_req_connecting............: avg=1.45µs   min=0s      med=0s      max=3.43ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=101.85ms min=4.44ms  med=99.68ms max=318.28ms p(90)=137.69ms p(95)=148.67ms p(99.9)=192.82ms
       { expected_response:true }...: avg=101.85ms min=4.44ms  med=99.68ms max=318.28ms p(90)=137.69ms p(95)=148.67ms p(99.9)=192.82ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 58784
     http_req_receiving.............: avg=79.32µs  min=28.85µs med=70.59µs max=97.79ms  p(90)=101.47µs p(95)=114.47µs p(99.9)=549.51µs
     http_req_sending...............: avg=19.06µs  min=5.13µs  med=13.74µs max=59.1ms   p(90)=19.11µs  p(95)=20.85µs  p(99.9)=445.32µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=101.76ms min=4.37ms  med=99.58ms max=307.89ms p(90)=137.6ms  p(95)=148.55ms p(99.9)=192.46ms
     http_reqs......................: 58784   487.468014/s
     iteration_duration.............: avg=102.26ms min=23.08ms med=99.96ms max=324.37ms p(90)=137.93ms p(95)=148.95ms p(99.9)=194.36ms
     iterations.....................: 58684   486.638761/s
     success_rate...................: 100.00% ✓ 58684      ✗ 0    
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

     checks.........................: 100.00% ✓ 143697     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   478 kB/s
     http_req_blocked...............: avg=5.76µs   min=1.12µs  med=3.43µs   max=4.23ms   p(90)=4.82µs   p(95)=5.41µs   p(99.9)=759.34µs
     http_req_connecting............: avg=2.1µs    min=0s      med=0s       max=4.19ms   p(90)=0s       p(95)=0s       p(99.9)=737.89µs
     http_req_duration..............: avg=124.77ms min=5.46ms  med=122.33ms max=337.87ms p(90)=163.39ms p(95)=176.27ms p(99.9)=228.48ms
       { expected_response:true }...: avg=124.77ms min=5.46ms  med=122.33ms max=337.87ms p(90)=163.39ms p(95)=176.27ms p(99.9)=228.48ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 47999
     http_req_receiving.............: avg=86.91µs  min=30.73µs med=79.56µs  max=110.06ms p(90)=109.45µs p(95)=121.05µs p(99.9)=437.45µs
     http_req_sending...............: avg=26.29µs  min=5.83µs  med=16.26µs  max=168.7ms  p(90)=21.06µs  p(95)=22.77µs  p(99.9)=471.26µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=124.66ms min=5.39ms  med=122.23ms max=337.73ms p(90)=163.28ms p(95)=176.18ms p(99.9)=227.92ms
     http_reqs......................: 47999   397.715504/s
     iteration_duration.............: avg=125.28ms min=13.64ms med=122.63ms max=346.38ms p(90)=163.69ms p(95)=176.57ms p(99.9)=231.01ms
     iterations.....................: 47899   396.886913/s
     success_rate...................: 100.00% ✓ 47899      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 104337     ✗ 0    
     data_received..................: 3.1 GB  25 MB/s
     data_sent......................: 42 MB   346 kB/s
     http_req_blocked...............: avg=7.48µs  min=1.07µs  med=2.96µs   max=7.64ms   p(90)=4.27µs   p(95)=4.79µs   p(99.9)=1.28ms  
     http_req_connecting............: avg=4.19µs  min=0s      med=0s       max=7.37ms   p(90)=0s       p(95)=0s       p(99.9)=1.14ms  
     http_req_duration..............: avg=171.9ms min=5.27ms  med=155.1ms  max=773.33ms p(90)=197.89ms p(95)=222.54ms p(99.9)=712.42ms
       { expected_response:true }...: avg=171.9ms min=5.27ms  med=155.1ms  max=773.33ms p(90)=197.89ms p(95)=222.54ms p(99.9)=712.42ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 34879
     http_req_receiving.............: avg=82.77µs min=30.53µs med=79.89µs  max=12.97ms  p(90)=109.29µs p(95)=120.19µs p(99.9)=416.93µs
     http_req_sending...............: avg=19.09µs min=5.22µs  med=15.31µs  max=20.88ms  p(90)=19.48µs  p(95)=21.04µs  p(99.9)=548.03µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=171.8ms min=5.2ms   med=155ms    max=773.22ms p(90)=197.78ms p(95)=222.42ms p(99.9)=712.3ms 
     http_reqs......................: 34879   288.400377/s
     iteration_duration.............: avg=172.6ms min=29.7ms  med=155.41ms max=773.62ms p(90)=198.22ms p(95)=223ms    p(99.9)=712.66ms
     iterations.....................: 34779   287.573517/s
     success_rate...................: 100.00% ✓ 34779      ✗ 0    
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

     checks.........................: 100.00% ✓ 98289      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   326 kB/s
     http_req_blocked...............: avg=5.72µs   min=1.27µs  med=3.38µs   max=3.41ms   p(90)=4.72µs   p(95)=5.3µs    p(99.9)=535.05µs
     http_req_connecting............: avg=2.11µs   min=0s      med=0s       max=3.38ms   p(90)=0s       p(95)=0s       p(99.9)=484.95µs
     http_req_duration..............: avg=182.43ms min=7.61ms  med=181.51ms max=417.88ms p(90)=206.18ms p(95)=211.08ms p(99.9)=276ms   
       { expected_response:true }...: avg=182.43ms min=7.61ms  med=181.51ms max=417.88ms p(90)=206.18ms p(95)=211.08ms p(99.9)=276ms   
     http_req_failed................: 0.00%   ✓ 0          ✗ 32863
     http_req_receiving.............: avg=86.82µs  min=33.8µs  med=84.31µs  max=3.12ms   p(90)=113.31µs p(95)=123.42µs p(99.9)=501.98µs
     http_req_sending...............: avg=20.88µs  min=5.92µs  med=16.58µs  max=15.02ms  p(90)=20.93µs  p(95)=22.66µs  p(99.9)=576.1µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=182.32ms min=7.52ms  med=181.4ms  max=417.68ms p(90)=206.07ms p(95)=210.97ms p(99.9)=275.76ms
     http_reqs......................: 32863   271.655982/s
     iteration_duration.............: avg=183.22ms min=31.14ms med=181.79ms max=424.08ms p(90)=206.46ms p(95)=211.37ms p(99.9)=276.6ms 
     iterations.....................: 32763   270.82935/s
     success_rate...................: 100.00% ✓ 32763      ✗ 0    
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

