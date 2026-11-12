## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.10 | 5,149 | 5,165 | 5,098 | 0.6% | 379 MB | 75.4 KB |  |
| fusion-net-11 | 16.7.5 | 5,067 | 5,074 | 5,024 | 0.5% | 384 MB | 77.6 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.10 | 4,943 | 4,955 | 4,935 | 0.2% | 389 MB | 80.5 KB |  |
| fusion-fed-net-11 | 16.7.5 | 4,883 | 4,906 | 4,845 | 0.6% | 388 MB | 81.3 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.10 | 4,823 | 4,854 | 4,723 | 1.2% | 135 MB | 28.6 KB |  |
| fusion-aot-11 | 16.7.5 | 4,811 | 4,822 | 4,785 | 0.3% | 127 MB | 27.0 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.10 | 4,645 | 4,654 | 4,624 | 0.2% | 133 MB | 29.4 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 4,616 | 4,619 | 4,590 | 0.3% | 127 MB | 28.1 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,168 | 4,461 | 4,093 | 3.8% | 2,297 MB | 564.3 KB |  |
| hive-router | v0.3.10 | 2,867 | 2,870 | 2,856 | 0.2% | 89 MB | 31.8 KB |  |
| grafbase | 0.53.5 | 1,859 | 1,864 | 1,852 | 0.2% | 110 MB | 60.5 KB |  |
| caliban | 3.2.0 | 1,434 | 1,436 | 1,429 | 0.2% | 5,057 MB | 3,611.5 KB |  |
| cosmo | 0.365.2 | 1,426 | 1,427 | 1,424 | 0.1% | 170 MB | 121.8 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 535 | 540 | 534 | 0.4% | 2,743 MB | 5,249.6 KB |  |
| apollo-router | v2.19.0 | 524 | 525 | 524 | 0.1% | 173 MB | 338.7 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 430 | 431 | 429 | 0.2% | 202 MB | 480.7 KB |  |
| hive-gateway | 2.15.6 | 268 | 268 | 266 | 0.3% | 3,603 MB | 13,766.7 KB |  |
| apollo-gateway | 2.14.4 | 266 | 267 | 265 | 0.3% | 2,156 MB | 8,300.1 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1855395     ✗ 0     
     data_received..................: 54 GB   451 MB/s
     data_sent......................: 744 MB  6.2 MB/s
     http_req_blocked...............: avg=3.66µs  min=792ns    med=1.91µs  max=162.26ms p(90)=3.06µs  p(95)=3.67µs   p(99.9)=26.44µs
     http_req_connecting............: avg=1.36µs  min=0s       med=0s      max=162.12ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.49ms  min=831.3µs  med=8.67ms  max=249.66ms p(90)=14.55ms p(95)=17.51ms  p(99.9)=29.59ms
       { expected_response:true }...: avg=9.49ms  min=831.3µs  med=8.67ms  max=249.66ms p(90)=14.55ms p(95)=17.51ms  p(99.9)=29.59ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 618565
     http_req_receiving.............: avg=91.54µs min=24.73µs  med=45.27µs max=200.8ms  p(90)=87.96µs p(95)=193.56µs p(99.9)=5.88ms 
     http_req_sending...............: avg=42.39µs min=4.36µs   med=7.99µs  max=200.75ms p(90)=14.14µs p(95)=100.73µs p(99.9)=4.64ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.36ms  min=786.06µs med=8.57ms  max=242.33ms p(90)=14.32ms p(95)=17.24ms  p(99.9)=29.14ms
     http_reqs......................: 618565  5149.853112/s
     iteration_duration.............: avg=9.69ms  min=1.07ms   med=8.86ms  max=300.15ms p(90)=14.75ms p(95)=17.73ms  p(99.9)=29.86ms
     iterations.....................: 618465  5149.020564/s
     success_rate...................: 100.00% ✓ 618465      ✗ 0     
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

     checks.........................: 100.00% ✓ 1825590     ✗ 0     
     data_received..................: 53 GB   443 MB/s
     data_sent......................: 732 MB  6.1 MB/s
     http_req_blocked...............: avg=2.68µs  min=762ns    med=1.84µs  max=8.44ms   p(90)=2.93µs  p(95)=3.51µs   p(99.9)=24.6µs 
     http_req_connecting............: avg=401ns   min=0s       med=0s      max=8.41ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.65ms  min=841.27µs med=8.87ms  max=274.18ms p(90)=14.76ms p(95)=17.39ms  p(99.9)=29.21ms
       { expected_response:true }...: avg=9.65ms  min=841.27µs med=8.87ms  max=274.18ms p(90)=14.76ms p(95)=17.39ms  p(99.9)=29.21ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 608630
     http_req_receiving.............: avg=88.66µs min=23.86µs  med=44.74µs max=173.24ms p(90)=87.09µs p(95)=187.97µs p(99.9)=5.58ms 
     http_req_sending...............: avg=39.95µs min=3.97µs   med=7.82µs  max=159.24ms p(90)=13.71µs p(95)=97.72µs  p(99.9)=4.37ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.52ms  min=790.6µs  med=8.77ms  max=267.18ms p(90)=14.56ms p(95)=17.16ms  p(99.9)=28.84ms
     http_reqs......................: 608630  5067.342161/s
     iteration_duration.............: avg=9.85ms  min=1.08ms   med=9.06ms  max=288.94ms p(90)=14.96ms p(95)=17.61ms  p(99.9)=29.5ms 
     iterations.....................: 608530  5066.509579/s
     success_rate...................: 100.00% ✓ 608530      ✗ 0     
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

     checks.........................: 100.00% ✓ 1781325     ✗ 0     
     data_received..................: 52 GB   433 MB/s
     data_sent......................: 714 MB  5.9 MB/s
     http_req_blocked...............: avg=2.59µs  min=821ns    med=1.96µs  max=12.06ms  p(90)=3.19µs  p(95)=3.92µs   p(99.9)=27.1µs 
     http_req_connecting............: avg=161ns   min=0s       med=0s      max=3.62ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.89ms  min=990.39µs med=9.06ms  max=302.11ms p(90)=15.1ms  p(95)=18.03ms  p(99.9)=30.57ms
       { expected_response:true }...: avg=9.89ms  min=990.39µs med=9.06ms  max=302.11ms p(90)=15.1ms  p(95)=18.03ms  p(99.9)=30.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 593875
     http_req_receiving.............: avg=99.2µs  min=25.15µs  med=47.82µs max=202.39ms p(90)=94.31µs p(95)=195.01µs p(99.9)=6.64ms 
     http_req_sending...............: avg=44.7µs  min=4.6µs    med=8.39µs  max=190.51ms p(90)=15.57µs p(95)=102.22µs p(99.9)=4.98ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.74ms  min=920.4µs  med=8.94ms  max=274.74ms p(90)=14.87ms p(95)=17.76ms  p(99.9)=30.13ms
     http_reqs......................: 593875  4943.727881/s
     iteration_duration.............: avg=10.09ms min=1.37ms   med=9.25ms  max=315.96ms p(90)=15.31ms p(95)=18.25ms  p(99.9)=30.85ms
     iterations.....................: 593775  4942.895429/s
     success_rate...................: 100.00% ✓ 593775      ✗ 0     
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

     checks.........................: 100.00% ✓ 1759713     ✗ 0     
     data_received..................: 51 GB   427 MB/s
     data_sent......................: 705 MB  5.9 MB/s
     http_req_blocked...............: avg=3.06µs   min=951ns    med=2.48µs  max=4.89ms   p(90)=3.84µs  p(95)=4.62µs   p(99.9)=34.09µs
     http_req_connecting............: avg=161ns    min=0s       med=0s      max=4.2ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10ms     min=983.27µs med=9.09ms  max=183ms    p(90)=15.56ms p(95)=18.61ms  p(99.9)=31.65ms
       { expected_response:true }...: avg=10ms     min=983.27µs med=9.09ms  max=183ms    p(90)=15.56ms p(95)=18.61ms  p(99.9)=31.65ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 586671
     http_req_receiving.............: avg=106.66µs min=24.79µs  med=49.33µs max=89.08ms  p(90)=98.78µs p(95)=203.62µs p(99.9)=7.4ms  
     http_req_sending...............: avg=46.29µs  min=4.6µs    med=8.92µs  max=76.93ms  p(90)=16.46µs p(95)=105.19µs p(99.9)=5.33ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.85ms   min=907.91µs med=8.97ms  max=182.49ms p(90)=15.31ms p(95)=18.32ms  p(99.9)=31.13ms
     http_reqs......................: 586671  4883.893095/s
     iteration_duration.............: avg=10.21ms  min=1.34ms   med=9.29ms  max=376.29ms p(90)=15.77ms p(95)=18.85ms  p(99.9)=32.01ms
     iterations.....................: 586571  4883.060619/s
     success_rate...................: 100.00% ✓ 586571      ✗ 0     
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

     checks.........................: 100.00% ✓ 1738107     ✗ 0     
     data_received..................: 51 GB   422 MB/s
     data_sent......................: 696 MB  5.8 MB/s
     http_req_blocked...............: avg=2.44µs  min=791ns    med=1.9µs   max=6.68ms   p(90)=3.04µs  p(95)=3.65µs   p(99.9)=24.61µs
     http_req_connecting............: avg=155ns   min=0s       med=0s      max=3.8ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.15ms min=906.43µs med=9.49ms  max=282.09ms p(90)=15.07ms p(95)=17.7ms   p(99.9)=28.69ms
       { expected_response:true }...: avg=10.15ms min=906.43µs med=9.49ms  max=282.09ms p(90)=15.07ms p(95)=17.7ms   p(99.9)=28.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 579469
     http_req_receiving.............: avg=92.59µs min=25.01µs  med=46.01µs max=90.55ms  p(90)=90.4µs  p(95)=202.37µs p(99.9)=5.65ms 
     http_req_sending...............: avg=40.43µs min=4.45µs   med=8.21µs  max=270.4ms  p(90)=14.6µs  p(95)=102.6µs  p(99.9)=4.03ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.02ms min=860.45µs med=9.38ms  max=276.53ms p(90)=14.87ms p(95)=17.45ms  p(99.9)=28.36ms
     http_reqs......................: 579469  4823.827414/s
     iteration_duration.............: avg=10.34ms min=1.1ms    med=9.67ms  max=290.11ms p(90)=15.27ms p(95)=17.92ms  p(99.9)=28.98ms
     iterations.....................: 579369  4822.994957/s
     success_rate...................: 100.00% ✓ 579369      ✗ 0     
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

     checks.........................: 100.00% ✓ 1733547     ✗ 0     
     data_received..................: 51 GB   421 MB/s
     data_sent......................: 695 MB  5.8 MB/s
     http_req_blocked...............: avg=4.36µs  min=831ns    med=2.03µs  max=199.33ms p(90)=3.38µs  p(95)=4.05µs   p(99.9)=28.62µs
     http_req_connecting............: avg=1.5µs   min=0s       med=0s      max=52.55ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.17ms min=899.7µs  med=9.45ms  max=247.79ms p(90)=15.22ms p(95)=17.91ms  p(99.9)=29.64ms
       { expected_response:true }...: avg=10.17ms min=899.7µs  med=9.45ms  max=247.79ms p(90)=15.22ms p(95)=17.91ms  p(99.9)=29.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 577949
     http_req_receiving.............: avg=92.16µs min=23.59µs  med=44.93µs max=54ms     p(90)=92.93µs p(95)=207.23µs p(99.9)=5.74ms 
     http_req_sending...............: avg=44.45µs min=4.29µs   med=8.1µs   max=168.04ms p(90)=15.1µs  p(95)=106.73µs p(99.9)=4.07ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.04ms min=852.62µs med=9.34ms  max=168.73ms p(90)=15.01ms p(95)=17.67ms  p(99.9)=29.23ms
     http_reqs......................: 577949  4811.470267/s
     iteration_duration.............: avg=10.37ms min=1.32ms   med=9.63ms  max=300.23ms p(90)=15.42ms p(95)=18.13ms  p(99.9)=29.87ms
     iterations.....................: 577849  4810.63776/s
     success_rate...................: 100.00% ✓ 577849      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1674048     ✗ 0     
     data_received..................: 49 GB   407 MB/s
     data_sent......................: 671 MB  5.6 MB/s
     http_req_blocked...............: avg=3.18µs  min=841ns   med=2µs     max=16.37ms  p(90)=3.25µs  p(95)=3.94µs   p(99.9)=27.78µs
     http_req_connecting............: avg=702ns   min=0s      med=0s      max=16.29ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.54ms min=1.08ms  med=9.92ms  max=266.23ms p(90)=15.39ms p(95)=17.96ms  p(99.9)=29.74ms
       { expected_response:true }...: avg=10.54ms min=1.08ms  med=9.92ms  max=266.23ms p(90)=15.39ms p(95)=17.96ms  p(99.9)=29.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 558116
     http_req_receiving.............: avg=94.34µs min=25.51µs med=46.58µs max=121.4ms  p(90)=94.26µs p(95)=201.88µs p(99.9)=5.92ms 
     http_req_sending...............: avg=42.38µs min=4.52µs  med=8.52µs  max=112.64ms p(90)=15.98µs p(95)=104.59µs p(99.9)=4.5ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.4ms  min=997.9µs med=9.81ms  max=265.42ms p(90)=15.19ms p(95)=17.71ms  p(99.9)=29.33ms
     http_reqs......................: 558116  4645.759024/s
     iteration_duration.............: avg=10.74ms min=1.68ms  med=10.11ms max=295.2ms  p(90)=15.59ms p(95)=18.18ms  p(99.9)=30.04ms
     iterations.....................: 558016  4644.926624/s
     success_rate...................: 100.00% ✓ 558016      ✗ 0     
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

     checks.........................: 100.00% ✓ 1663563     ✗ 0     
     data_received..................: 49 GB   404 MB/s
     data_sent......................: 667 MB  5.5 MB/s
     http_req_blocked...............: avg=2.86µs  min=791ns   med=1.93µs  max=10.68ms  p(90)=3.24µs  p(95)=3.98µs   p(99.9)=28.57µs
     http_req_connecting............: avg=499ns   min=0s      med=0s      max=10.64ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.61ms min=1.08ms  med=9.96ms  max=274.72ms p(90)=15.53ms p(95)=18.12ms  p(99.9)=30.72ms
       { expected_response:true }...: avg=10.61ms min=1.08ms  med=9.96ms  max=274.72ms p(90)=15.53ms p(95)=18.12ms  p(99.9)=30.72ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 554621
     http_req_receiving.............: avg=95.8µs  min=24.48µs med=46µs    max=101.61ms p(90)=96.01µs p(95)=204.78µs p(99.9)=6.23ms 
     http_req_sending...............: avg=45.56µs min=4.25µs  med=8.21µs  max=177.01ms p(90)=16.29µs p(95)=104.83µs p(99.9)=4.52ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.46ms min=1.01ms  med=9.85ms  max=232.71ms p(90)=15.32ms p(95)=17.86ms  p(99.9)=30.27ms
     http_reqs......................: 554621  4616.529087/s
     iteration_duration.............: avg=10.81ms min=1.34ms  med=10.15ms max=288.44ms p(90)=15.74ms p(95)=18.33ms  p(99.9)=31.04ms
     iterations.....................: 554521  4615.696712/s
     success_rate...................: 100.00% ✓ 554521      ✗ 0     
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

     checks.........................: 100.00% ✓ 1501746     ✗ 0     
     data_received..................: 44 GB   364 MB/s
     data_sent......................: 602 MB  5.0 MB/s
     http_req_blocked...............: avg=2.66µs  min=831ns    med=2.1µs   max=4.03ms   p(90)=3.41µs  p(95)=4.09µs   p(99.9)=29.76µs
     http_req_connecting............: avg=177ns   min=0s       med=0s      max=3.47ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.78ms min=786.44µs med=11.73ms max=282.26ms p(90)=18ms    p(95)=19.96ms  p(99.9)=30.05ms
       { expected_response:true }...: avg=11.78ms min=786.44µs med=11.73ms max=282.26ms p(90)=18ms    p(95)=19.96ms  p(99.9)=30.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 500682
     http_req_receiving.............: avg=80.94µs min=24.18µs  med=46.99µs max=103.33ms p(90)=93.51µs p(95)=200.85µs p(99.9)=3.5ms  
     http_req_sending...............: avg=38.79µs min=4.51µs   med=8.88µs  max=145.62ms p(90)=15.89µs p(95)=110.25µs p(99.9)=2.91ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.66ms min=709.51µs med=11.63ms max=273.81ms p(90)=17.86ms p(95)=19.8ms   p(99.9)=29.8ms 
     http_reqs......................: 500682  4168.28266/s
     iteration_duration.............: avg=11.97ms min=1.12ms   med=11.92ms max=301.86ms p(90)=18.19ms p(95)=20.16ms  p(99.9)=30.27ms
     iterations.....................: 500582  4167.450139/s
     success_rate...................: 100.00% ✓ 500582      ✗ 0     
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

     checks.........................: 100.00% ✓ 1033443     ✗ 0     
     data_received..................: 30 GB   251 MB/s
     data_sent......................: 414 MB  3.4 MB/s
     http_req_blocked...............: avg=3.14µs  min=912ns   med=2.29µs  max=13.41ms  p(90)=3.71µs  p(95)=4.4µs    p(99.9)=30.98µs
     http_req_connecting............: avg=518ns   min=0s      med=0s      max=13.35ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.21ms min=1.26ms  med=17.29ms max=285.22ms p(90)=23.18ms p(95)=24.73ms  p(99.9)=31.85ms
       { expected_response:true }...: avg=17.21ms min=1.26ms  med=17.29ms max=285.22ms p(90)=23.18ms p(95)=24.73ms  p(99.9)=31.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 344581
     http_req_receiving.............: avg=70.92µs min=24.94µs med=52.97µs max=168.12ms p(90)=90.35µs p(95)=129.81µs p(99.9)=1.08ms 
     http_req_sending...............: avg=30.65µs min=4.62µs  med=9.86µs  max=83.79ms  p(90)=16.96µs p(95)=92.12µs  p(99.9)=1.17ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.11ms min=1.19ms  med=17.2ms  max=250.53ms p(90)=23.08ms p(95)=24.62ms  p(99.9)=31.72ms
     http_reqs......................: 344581  2867.24373/s
     iteration_duration.............: avg=17.4ms  min=3.24ms  med=17.48ms max=299.32ms p(90)=23.37ms p(95)=24.92ms  p(99.9)=32.07ms
     iterations.....................: 344481  2866.411634/s
     success_rate...................: 100.00% ✓ 344481      ✗ 0     
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

     checks.........................: 100.00% ✓ 670446      ✗ 0     
     data_received..................: 20 GB   163 MB/s
     data_sent......................: 269 MB  2.2 MB/s
     http_req_blocked...............: avg=3.24µs  min=912ns   med=2.33µs  max=3.59ms   p(90)=4.48µs   p(95)=5.56µs   p(99.9)=39.43µs
     http_req_connecting............: avg=398ns   min=0s      med=0s      max=3.56ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.59ms min=1.81ms  med=26.03ms max=278.68ms p(90)=34.51ms  p(95)=37.29ms  p(99.9)=51.52ms
       { expected_response:true }...: avg=26.59ms min=1.81ms  med=26.03ms max=278.68ms p(90)=34.51ms  p(95)=37.29ms  p(99.9)=51.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 223582
     http_req_receiving.............: avg=84.08µs min=26.99µs med=56.8µs  max=96.93ms  p(90)=119.82µs p(95)=188.58µs p(99.9)=1.54ms 
     http_req_sending...............: avg=35.28µs min=4.62µs  med=9.93µs  max=183.79ms p(90)=22.68µs  p(95)=105.13µs p(99.9)=1.42ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.47ms min=1.76ms  med=25.91ms max=278.07ms p(90)=34.39ms  p(95)=37.17ms  p(99.9)=51.32ms
     http_reqs......................: 223582  1859.171074/s
     iteration_duration.............: avg=26.83ms min=8.09ms  med=26.24ms max=319.31ms p(90)=34.72ms  p(95)=37.51ms  p(99.9)=51.89ms
     iterations.....................: 223482  1858.339535/s
     success_rate...................: 100.00% ✓ 223482      ✗ 0     
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

     checks.........................: 100.00% ✓ 517332      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=3.59µs  min=952ns   med=2.36µs  max=6.65ms   p(90)=3.96µs  p(95)=4.65µs   p(99.9)=28.94µs 
     http_req_connecting............: avg=880ns   min=0s      med=0s      max=6.53ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.55ms min=2.02ms  med=33.57ms max=291.7ms  p(90)=49.31ms p(95)=54.39ms  p(99.9)=82.51ms 
       { expected_response:true }...: avg=34.55ms min=2.02ms  med=33.57ms max=291.7ms  p(90)=49.31ms p(95)=54.39ms  p(99.9)=82.51ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 172544
     http_req_receiving.............: avg=71.54µs min=27.66µs med=59.77µs max=101.25ms p(90)=94.68µs p(95)=110.35µs p(99.9)=790.55µs
     http_req_sending...............: avg=20.91µs min=4.74µs  med=11.13µs max=95.37ms  p(90)=17.63µs p(95)=21.14µs  p(99.9)=733.5µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.46ms min=1.96ms  med=33.48ms max=288.73ms p(90)=49.22ms p(95)=54.3ms   p(99.9)=82.12ms 
     http_reqs......................: 172544  1434.579596/s
     iteration_duration.............: avg=34.78ms min=5.91ms  med=33.77ms max=305.35ms p(90)=49.52ms p(95)=54.61ms  p(99.9)=83.04ms 
     iterations.....................: 172444  1433.748168/s
     success_rate...................: 100.00% ✓ 172444      ✗ 0     
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

     checks.........................: 100.00% ✓ 514512      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 206 MB  1.7 MB/s
     http_req_blocked...............: avg=2.73µs  min=892ns   med=2.12µs  max=3.21ms   p(90)=3.52µs  p(95)=4.17µs   p(99.9)=26.42µs 
     http_req_connecting............: avg=302ns   min=0s      med=0s      max=3.17ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.76ms min=2.06ms  med=33.84ms max=285.4ms  p(90)=50.34ms p(95)=55.51ms  p(99.9)=79.95ms 
       { expected_response:true }...: avg=34.76ms min=2.06ms  med=33.84ms max=285.4ms  p(90)=50.34ms p(95)=55.51ms  p(99.9)=79.95ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 171604
     http_req_receiving.............: avg=69.69µs min=25.36µs med=59.46µs max=26.72ms  p(90)=95.34µs p(95)=111.18µs p(99.9)=662.83µs
     http_req_sending...............: avg=20.21µs min=4.71µs  med=10.04µs max=80.69ms  p(90)=15.83µs p(95)=19.47µs  p(99.9)=732.15µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.67ms min=2ms     med=33.75ms max=285.13ms p(90)=50.25ms p(95)=55.42ms  p(99.9)=79.72ms 
     http_reqs......................: 171604  1426.836677/s
     iteration_duration.............: avg=34.97ms min=4.01ms  med=34.04ms max=304.76ms p(90)=50.53ms p(95)=55.71ms  p(99.9)=80.3ms  
     iterations.....................: 171504  1426.005206/s
     success_rate...................: 100.00% ✓ 171504      ✗ 0     
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

     checks.........................: 100.00% ✓ 193311     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   643 kB/s
     http_req_blocked...............: avg=4.74µs  min=1.17µs  med=2.98µs  max=3.73ms   p(90)=4.41µs   p(95)=5.03µs   p(99.9)=46.58µs 
     http_req_connecting............: avg=1.52µs  min=0s      med=0s      max=3.69ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.75ms min=3.97ms  med=90.09ms max=323.29ms p(90)=112.07ms p(95)=122.47ms p(99.9)=220.13ms
       { expected_response:true }...: avg=92.75ms min=3.97ms  med=90.09ms max=323.29ms p(90)=112.07ms p(95)=122.47ms p(99.9)=220.13ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64537
     http_req_receiving.............: avg=78.86µs min=29.58µs med=70.21µs max=88.92ms  p(90)=102.56µs p(95)=114.65µs p(99.9)=554.92µs
     http_req_sending...............: avg=21.4µs  min=5.08µs  med=13.85µs max=92.06ms  p(90)=19.49µs  p(95)=21.4µs   p(99.9)=546.04µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.65ms min=3.85ms  med=90ms    max=322.93ms p(90)=111.97ms p(95)=122.38ms p(99.9)=219.91ms
     http_reqs......................: 64537   535.360706/s
     iteration_duration.............: avg=93.12ms min=26.72ms med=90.34ms max=341ms    p(90)=112.32ms p(95)=122.73ms p(99.9)=222.91ms
     iterations.....................: 64437   534.531165/s
     success_rate...................: 100.00% ✓ 64437      ✗ 0    
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

     checks.........................: 100.00% ✓ 189417     ✗ 0    
     data_received..................: 5.5 GB  46 MB/s
     data_sent......................: 76 MB   630 kB/s
     http_req_blocked...............: avg=5.02µs  min=1.21µs  med=3.32µs  max=4.19ms   p(90)=4.82µs   p(95)=5.44µs   p(99.9)=47.31µs 
     http_req_connecting............: avg=1.48µs  min=0s      med=0s      max=4.15ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=94.63ms min=4.49ms  med=92.54ms max=306.31ms p(90)=127.82ms p(95)=138.45ms p(99.9)=180.41ms
       { expected_response:true }...: avg=94.63ms min=4.49ms  med=92.54ms max=306.31ms p(90)=127.82ms p(95)=138.45ms p(99.9)=180.41ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63239
     http_req_receiving.............: avg=79.41µs min=29.34µs med=73.21µs max=101.65ms p(90)=103.62µs p(95)=115.74µs p(99.9)=521.04µs
     http_req_sending...............: avg=21.26µs min=5.26µs  med=15.2µs  max=82.88ms  p(90)=20.72µs  p(95)=22.75µs  p(99.9)=576.65µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.53ms min=4.38ms  med=92.44ms max=306.17ms p(90)=127.71ms p(95)=138.33ms p(99.9)=180.26ms
     http_reqs......................: 63239   524.516834/s
     iteration_duration.............: avg=95.03ms min=11.59ms med=92.84ms max=319.77ms p(90)=128.09ms p(95)=138.72ms p(99.9)=182.08ms
     iterations.....................: 63139   523.687414/s
     success_rate...................: 100.00% ✓ 63139      ✗ 0    
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

     checks.........................: 100.00% ✓ 155658     ✗ 0    
     data_received..................: 4.5 GB  38 MB/s
     data_sent......................: 62 MB   517 kB/s
     http_req_blocked...............: avg=4.94µs   min=1.09µs  med=2.84µs  max=3.64ms   p(90)=4.23µs   p(95)=4.76µs   p(99.9)=72.31µs 
     http_req_connecting............: avg=1.89µs   min=0s      med=0s      max=3.6ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=115.2ms  min=5.29ms  med=112.8ms max=332.39ms p(90)=150.91ms p(95)=162.58ms p(99.9)=208.41ms
       { expected_response:true }...: avg=115.2ms  min=5.29ms  med=112.8ms max=332.39ms p(90)=150.91ms p(95)=162.58ms p(99.9)=208.41ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51986
     http_req_receiving.............: avg=83.48µs  min=27.87µs med=75.13µs max=159.93ms p(90)=105.04µs p(95)=117.11µs p(99.9)=500.9µs 
     http_req_sending...............: avg=22.36µs  min=5.04µs  med=14.64µs max=88.29ms  p(90)=19.58µs  p(95)=21.37µs  p(99.9)=478.93µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=115.1ms  min=5.22ms  med=112.7ms max=326.42ms p(90)=150.81ms p(95)=162.47ms p(99.9)=208.28ms
     http_reqs......................: 51986   430.770316/s
     iteration_duration.............: avg=115.66ms min=21.34ms med=113.1ms max=345.38ms p(90)=151.22ms p(95)=162.93ms p(99.9)=210.03ms
     iterations.....................: 51886   429.941689/s
     success_rate...................: 100.00% ✓ 51886      ✗ 0    
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

     checks.........................: 100.00% ✓ 96945      ✗ 0    
     data_received..................: 2.8 GB  24 MB/s
     data_sent......................: 39 MB   322 kB/s
     http_req_blocked...............: avg=6.11µs   min=1.12µs  med=2.91µs   max=4.21ms   p(90)=4.17µs   p(95)=4.68µs   p(99.9)=1.36ms  
     http_req_connecting............: avg=3.04µs   min=0s      med=0s       max=4.15ms   p(90)=0s       p(95)=0s       p(99.9)=1.34ms  
     http_req_duration..............: avg=184.97ms min=5.74ms  med=167.94ms max=753.75ms p(90)=223.72ms p(95)=254.79ms p(99.9)=676.47ms
       { expected_response:true }...: avg=184.97ms min=5.74ms  med=167.94ms max=753.75ms p(90)=223.72ms p(95)=254.79ms p(99.9)=676.47ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32415
     http_req_receiving.............: avg=87.54µs  min=32.2µs  med=84.76µs  max=8.92ms   p(90)=113.99µs p(95)=125.35µs p(99.9)=775.48µs
     http_req_sending...............: avg=19.32µs  min=5.18µs  med=16.48µs  max=15.21ms  p(90)=20.76µs  p(95)=22.47µs  p(99.9)=441.83µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.86ms min=5.66ms  med=167.84ms max=753.64ms p(90)=223.61ms p(95)=254.66ms p(99.9)=676.38ms
     http_reqs......................: 32415   268.201317/s
     iteration_duration.............: avg=185.76ms min=32.07ms med=168.34ms max=753.98ms p(90)=224.03ms p(95)=255.4ms  p(99.9)=676.85ms
     iterations.....................: 32315   267.373918/s
     success_rate...................: 100.00% ✓ 32315      ✗ 0    
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

     checks.........................: 100.00% ✓ 96534      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   320 kB/s
     http_req_blocked...............: avg=6.18µs   min=1.13µs  med=2.93µs   max=3.69ms   p(90)=4.19µs   p(95)=4.71µs   p(99.9)=1.55ms  
     http_req_connecting............: avg=3.04µs   min=0s      med=0s       max=3.64ms   p(90)=0s       p(95)=0s       p(99.9)=1.52ms  
     http_req_duration..............: avg=185.73ms min=7.48ms  med=185.83ms max=381.48ms p(90)=195.45ms p(95)=200.4ms  p(99.9)=269.69ms
       { expected_response:true }...: avg=185.73ms min=7.48ms  med=185.83ms max=381.48ms p(90)=195.45ms p(95)=200.4ms  p(99.9)=269.69ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32278
     http_req_receiving.............: avg=85.5µs   min=29.4µs  med=81.02µs  max=68.17ms  p(90)=110.12µs p(95)=119.96µs p(99.9)=448.3µs 
     http_req_sending...............: avg=28.89µs  min=5.31µs  med=15.56µs  max=101.43ms p(90)=19.42µs  p(95)=21.04µs  p(99.9)=449.74µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=185.62ms min=7.35ms  med=185.72ms max=380.98ms p(90)=195.34ms p(95)=200.29ms p(99.9)=269.61ms
     http_reqs......................: 32278   266.871792/s
     iteration_duration.............: avg=186.56ms min=24.98ms med=186.11ms max=393.01ms p(90)=195.7ms  p(95)=200.68ms p(99.9)=270.65ms
     iterations.....................: 32178   266.045/s
     success_rate...................: 100.00% ✓ 32178      ✗ 0    
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

