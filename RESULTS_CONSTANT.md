## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.12 | 5,451 | 5,472 | 5,421 | 0.3% | 403 MB | 75.7 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.12 | 5,215 | 5,264 | 5,210 | 0.4% | 401 MB | 78.8 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.12 | 5,137 | 5,148 | 5,124 | 0.2% | 124 MB | 24.7 KB |  |
| fusion-net-11 | 16.7.5 | 5,098 | 5,121 | 5,093 | 0.2% | 377 MB | 75.6 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.12 | 4,944 | 4,960 | 4,922 | 0.3% | 130 MB | 26.9 KB |  |
| fusion-fed-net-11 | 16.7.5 | 4,899 | 4,923 | 4,873 | 0.5% | 387 MB | 80.9 KB |  |
| fusion-aot-11 | 16.7.5 | 4,831 | 4,848 | 4,814 | 0.3% | 128 MB | 27.1 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 4,577 | 4,583 | 4,574 | 0.1% | 126 MB | 28.2 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,273 | 4,380 | 3,983 | 3.5% | 2,294 MB | 549.7 KB |  |
| hive-router | v0.3.10 | 3,102 | 3,115 | 3,058 | 0.7% | 95 MB | 31.3 KB |  |
| grafbase | 0.53.5 | 1,746 | 1,747 | 1,745 | 0.0% | 105 MB | 61.4 KB |  |
| caliban | 3.2.0 | 1,495 | 1,501 | 1,486 | 0.4% | 4,969 MB | 3,403.4 KB |  |
| cosmo | 0.365.2 | 1,435 | 1,438 | 1,434 | 0.1% | 165 MB | 117.4 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 551 | 554 | 549 | 0.3% | 2,759 MB | 5,126.7 KB |  |
| apollo-router | v2.19.0 | 483 | 484 | 481 | 0.2% | 172 MB | 365.2 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 412 | 413 | 408 | 0.5% | 203 MB | 503.9 KB |  |
| hive-gateway | 2.15.6 | 269 | 269 | 268 | 0.2% | 3,443 MB | 13,107.7 KB |  |
| apollo-gateway | 2.14.4 | 268 | 268 | 267 | 0.2% | 2,163 MB | 8,264.6 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.12)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1964082     ✗ 0     
     data_received..................: 57 GB   477 MB/s
     data_sent......................: 787 MB  6.6 MB/s
     http_req_blocked...............: avg=2.47µs  min=822ns    med=1.95µs  max=5.55ms   p(90)=3µs     p(95)=3.58µs   p(99.9)=26.82µs
     http_req_connecting............: avg=151ns   min=0s       med=0s      max=3.82ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.96ms  min=801.21µs med=8.03ms  max=274.13ms p(90)=14.41ms p(95)=17.55ms  p(99.9)=29.95ms
       { expected_response:true }...: avg=8.96ms  min=801.21µs med=8.03ms  max=274.13ms p(90)=14.41ms p(95)=17.55ms  p(99.9)=29.95ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 654794
     http_req_receiving.............: avg=91.21µs min=25.16µs  med=44.98µs max=174.89ms p(90)=84.61µs p(95)=185.98µs p(99.9)=6.03ms 
     http_req_sending...............: avg=41.93µs min=4.34µs   med=8.19µs  max=123.51ms p(90)=13.69µs p(95)=99.28µs  p(99.9)=4.66ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.82ms  min=742.03µs med=7.93ms  max=261.57ms p(90)=14.18ms p(95)=17.27ms  p(99.9)=29.53ms
     http_reqs......................: 654794  5451.67386/s
     iteration_duration.............: avg=9.15ms  min=1.15ms   med=8.22ms  max=282.52ms p(90)=14.62ms p(95)=17.77ms  p(99.9)=30.18ms
     iterations.....................: 654694  5450.841282/s
     success_rate...................: 100.00% ✓ 654694      ✗ 0     
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

     checks.........................: 100.00% ✓ 1879176     ✗ 0     
     data_received..................: 55 GB   456 MB/s
     data_sent......................: 753 MB  6.3 MB/s
     http_req_blocked...............: avg=2.62µs  min=791ns    med=2.06µs max=5.6ms    p(90)=3.26µs  p(95)=3.88µs   p(99.9)=27.68µs
     http_req_connecting............: avg=150ns   min=0s       med=0s     max=3.97ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.37ms  min=818.99µs med=8.44ms max=265.18ms p(90)=14.91ms p(95)=18.08ms  p(99.9)=31.06ms
       { expected_response:true }...: avg=9.37ms  min=818.99µs med=8.44ms max=265.18ms p(90)=14.91ms p(95)=18.08ms  p(99.9)=31.06ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 626492
     http_req_receiving.............: avg=94.33µs min=24.31µs  med=47.1µs max=75.69ms  p(90)=89.59µs p(95)=196.99µs p(99.9)=6.09ms 
     http_req_sending...............: avg=42.98µs min=4.38µs   med=8.33µs max=82.95ms  p(90)=14.21µs p(95)=102.63µs p(99.9)=4.92ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.23ms  min=756.05µs med=8.32ms max=264.65ms p(90)=14.69ms p(95)=17.81ms  p(99.9)=30.55ms
     http_reqs......................: 626492  5215.542677/s
     iteration_duration.............: avg=9.56ms  min=1.24ms   med=8.62ms max=311.53ms p(90)=15.12ms p(95)=18.3ms   p(99.9)=31.32ms
     iterations.....................: 626392  5214.710177/s
     success_rate...................: 100.00% ✓ 626392      ✗ 0     
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

     checks.........................: 100.00% ✓ 1851117     ✗ 0     
     data_received..................: 54 GB   450 MB/s
     data_sent......................: 742 MB  6.2 MB/s
     http_req_blocked...............: avg=5.42µs  min=812ns    med=1.92µs  max=233.31ms p(90)=3.12µs  p(95)=3.74µs   p(99.9)=27.54µs
     http_req_connecting............: avg=3.07µs  min=0s       med=0s      max=232.75ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.52ms  min=872.17µs med=8.65ms  max=216.91ms p(90)=15.08ms p(95)=18.06ms  p(99.9)=30.58ms
       { expected_response:true }...: avg=9.52ms  min=872.17µs med=8.65ms  max=216.91ms p(90)=15.08ms p(95)=18.06ms  p(99.9)=30.58ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 617139
     http_req_receiving.............: avg=90.16µs min=24.39µs  med=44.91µs max=30.32ms  p(90)=87.72µs p(95)=195.69µs p(99.9)=5.6ms  
     http_req_sending...............: avg=41.06µs min=4.22µs   med=8.02µs  max=75.19ms  p(90)=13.77µs p(95)=100.98µs p(99.9)=4.57ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.38ms  min=810.11µs med=8.54ms  max=216.1ms  p(90)=14.88ms p(95)=17.8ms   p(99.9)=30.07ms
     http_reqs......................: 617139  5137.850519/s
     iteration_duration.............: avg=9.71ms  min=1.35ms   med=8.83ms  max=299.03ms p(90)=15.28ms p(95)=18.28ms  p(99.9)=30.84ms
     iterations.....................: 617039  5137.017992/s
     success_rate...................: 100.00% ✓ 617039      ✗ 0     
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

     checks.........................: 100.00% ✓ 1836705     ✗ 0     
     data_received..................: 54 GB   446 MB/s
     data_sent......................: 736 MB  6.1 MB/s
     http_req_blocked...............: avg=7.13µs  min=881ns    med=2.41µs  max=209.88ms p(90)=3.65µs  p(95)=4.3µs    p(99.9)=31.65µs
     http_req_connecting............: avg=4.11µs  min=0s       med=0s      max=189.97ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.58ms  min=802.55µs med=8.63ms  max=215.29ms p(90)=15.14ms p(95)=18.24ms  p(99.9)=31.45ms
       { expected_response:true }...: avg=9.58ms  min=802.55µs med=8.63ms  max=215.29ms p(90)=15.14ms p(95)=18.24ms  p(99.9)=31.45ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 612335
     http_req_receiving.............: avg=97.8µs  min=24.94µs  med=47.27µs max=133.13ms p(90)=90.23µs p(95)=200.97µs p(99.9)=6.18ms 
     http_req_sending...............: avg=45.62µs min=4.68µs   med=8.87µs  max=185.83ms p(90)=14.98µs p(95)=104.04µs p(99.9)=4.86ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.44ms  min=739.11µs med=8.51ms  max=187.43ms p(90)=14.91ms p(95)=17.97ms  p(99.9)=30.89ms
     http_reqs......................: 612335  5098.447212/s
     iteration_duration.............: avg=9.79ms  min=1.18ms   med=8.83ms  max=329.73ms p(90)=15.35ms p(95)=18.47ms  p(99.9)=31.75ms
     iterations.....................: 612235  5097.614589/s
     success_rate...................: 100.00% ✓ 612235      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.12)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1781469     ✗ 0     
     data_received..................: 52 GB   433 MB/s
     data_sent......................: 714 MB  5.9 MB/s
     http_req_blocked...............: avg=2.8µs   min=772ns    med=1.9µs   max=8.26ms   p(90)=3.04µs  p(95)=3.62µs   p(99.9)=28.84µs
     http_req_connecting............: avg=476ns   min=0s       med=0s      max=8.18ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.9ms   min=907.72µs med=9.1ms   max=287.23ms p(90)=15.68ms p(95)=18.37ms  p(99.9)=30.32ms
       { expected_response:true }...: avg=9.9ms   min=907.72µs med=9.1ms   max=287.23ms p(90)=15.68ms p(95)=18.37ms  p(99.9)=30.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 593923
     http_req_receiving.............: avg=90.63µs min=25.2µs   med=46.85µs max=158.57ms p(90)=88.48µs p(95)=197.21µs p(99.9)=5.17ms 
     http_req_sending...............: avg=38.66µs min=4.26µs   med=7.99µs  max=133.7ms  p(90)=13.74µs p(95)=101.51µs p(99.9)=3.88ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.77ms  min=837.26µs med=8.98ms  max=280.64ms p(90)=15.5ms  p(95)=18.14ms  p(99.9)=30.06ms
     http_reqs......................: 593923  4944.630148/s
     iteration_duration.............: avg=10.09ms min=1.26ms   med=9.28ms  max=330.4ms  p(90)=15.88ms p(95)=18.58ms  p(99.9)=30.6ms 
     iterations.....................: 593823  4943.797611/s
     success_rate...................: 100.00% ✓ 593823      ✗ 0     
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

     checks.........................: 100.00% ✓ 1765380     ✗ 0     
     data_received..................: 52 GB   429 MB/s
     data_sent......................: 707 MB  5.9 MB/s
     http_req_blocked...............: avg=2.59µs  min=802ns    med=1.93µs max=7.02ms   p(90)=3.22µs  p(95)=4.03µs   p(99.9)=26.4µs 
     http_req_connecting............: avg=166ns   min=0s       med=0s     max=4.14ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.98ms  min=994.25µs med=9.16ms max=272.49ms p(90)=15.37ms p(95)=18.08ms  p(99.9)=30.69ms
       { expected_response:true }...: avg=9.98ms  min=994.25µs med=9.16ms max=272.49ms p(90)=15.37ms p(95)=18.08ms  p(99.9)=30.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 588560
     http_req_receiving.............: avg=99.7µs  min=26.19µs  med=47.5µs max=178.15ms p(90)=95.32µs p(95)=196.68µs p(99.9)=6.71ms 
     http_req_sending...............: avg=44.03µs min=4.14µs   med=8.1µs  max=166.06ms p(90)=15.73µs p(95)=100.58µs p(99.9)=4.86ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.84ms  min=915.9µs  med=9.04ms max=266.39ms p(90)=15.15ms p(95)=17.8ms   p(99.9)=30.21ms
     http_reqs......................: 588560  4899.457967/s
     iteration_duration.............: avg=10.18ms min=1.2ms    med=9.35ms max=297.53ms p(90)=15.57ms p(95)=18.3ms   p(99.9)=30.96ms
     iterations.....................: 588460  4898.625519/s
     success_rate...................: 100.00% ✓ 588460      ✗ 0     
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

     checks.........................: 100.00% ✓ 1740987     ✗ 0     
     data_received..................: 51 GB   423 MB/s
     data_sent......................: 698 MB  5.8 MB/s
     http_req_blocked...............: avg=2.52µs  min=762ns    med=2.01µs  max=4.68ms   p(90)=3.21µs  p(95)=3.83µs   p(99.9)=26.92µs
     http_req_connecting............: avg=150ns   min=0s       med=0s      max=3.51ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.13ms min=940.05µs med=9.39ms  max=286.15ms p(90)=15.24ms p(95)=17.91ms  p(99.9)=29.66ms
       { expected_response:true }...: avg=10.13ms min=940.05µs med=9.39ms  max=286.15ms p(90)=15.24ms p(95)=17.91ms  p(99.9)=29.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 580429
     http_req_receiving.............: avg=96.2µs  min=24.36µs  med=45.69µs max=148.15ms p(90)=94.38µs p(95)=213.21µs p(99.9)=6.09ms 
     http_req_sending...............: avg=40.17µs min=4.33µs   med=8.22µs  max=117.35ms p(90)=14.32µs p(95)=103.37µs p(99.9)=4.27ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10ms    min=854.21µs med=9.27ms  max=275.56ms p(90)=15.03ms p(95)=17.67ms  p(99.9)=29.23ms
     http_reqs......................: 580429  4831.852602/s
     iteration_duration.............: avg=10.33ms min=1.48ms   med=9.57ms  max=301.68ms p(90)=15.44ms p(95)=18.12ms  p(99.9)=30.04ms
     iterations.....................: 580329  4831.020139/s
     success_rate...................: 100.00% ✓ 580329      ✗ 0     
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

     checks.........................: 100.00% ✓ 1649661     ✗ 0     
     data_received..................: 48 GB   401 MB/s
     data_sent......................: 661 MB  5.5 MB/s
     http_req_blocked...............: avg=2.74µs  min=801ns   med=2.06µs  max=12.27ms  p(90)=3.37µs  p(95)=4.08µs   p(99.9)=30.48µs
     http_req_connecting............: avg=181ns   min=0s      med=0s      max=4.08ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.69ms min=1.03ms  med=10ms    max=257.95ms p(90)=15.83ms p(95)=18.45ms  p(99.9)=31.42ms
       { expected_response:true }...: avg=10.69ms min=1.03ms  med=10ms    max=257.95ms p(90)=15.83ms p(95)=18.45ms  p(99.9)=31.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 549987
     http_req_receiving.............: avg=97.41µs min=25.23µs med=46.8µs  max=30.53ms  p(90)=96.37µs p(95)=211.26µs p(99.9)=6ms    
     http_req_sending...............: avg=42.08µs min=4.55µs  med=8.39µs  max=168.03ms p(90)=15.76µs p(95)=105.7µs  p(99.9)=4.33ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.55ms min=985.1µs med=9.88ms  max=252.7ms  p(90)=15.63ms p(95)=18.21ms  p(99.9)=30.92ms
     http_reqs......................: 549987  4577.732313/s
     iteration_duration.............: avg=10.9ms  min=1.6ms   med=10.19ms max=343.59ms p(90)=16.04ms p(95)=18.67ms  p(99.9)=31.76ms
     iterations.....................: 549887  4576.899978/s
     success_rate...................: 100.00% ✓ 549887      ✗ 0     
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

     checks.........................: 100.00% ✓ 1539480     ✗ 0     
     data_received..................: 45 GB   374 MB/s
     data_sent......................: 617 MB  5.1 MB/s
     http_req_blocked...............: avg=2.49µs  min=761ns    med=1.96µs  max=3.84ms   p(90)=3.1µs   p(95)=3.68µs   p(99.9)=29.74µs
     http_req_connecting............: avg=182ns   min=0s       med=0s      max=3.81ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.49ms min=774.43µs med=11.52ms max=290.64ms p(90)=17.63ms p(95)=19.57ms  p(99.9)=29.79ms
       { expected_response:true }...: avg=11.49ms min=774.43µs med=11.52ms max=290.64ms p(90)=17.63ms p(95)=19.57ms  p(99.9)=29.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 513260
     http_req_receiving.............: avg=79.99µs min=24.18µs  med=46.29µs max=82.93ms  p(90)=90.03µs p(95)=200.62µs p(99.9)=3.47ms 
     http_req_sending...............: avg=37.07µs min=4.41µs   med=8.4µs   max=153.22ms p(90)=14.54µs p(95)=107.83µs p(99.9)=2.7ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.37ms min=693.28µs med=11.41ms max=280.88ms p(90)=17.5ms  p(95)=19.42ms  p(99.9)=29.4ms 
     http_reqs......................: 513260  4273.207946/s
     iteration_duration.............: avg=11.68ms min=1.19ms   med=11.7ms  max=300.37ms p(90)=17.82ms p(95)=19.77ms  p(99.9)=30ms   
     iterations.....................: 513160  4272.375384/s
     success_rate...................: 100.00% ✓ 513160      ✗ 0     
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

     checks.........................: 100.00% ✓ 1118019     ✗ 0     
     data_received..................: 33 GB   271 MB/s
     data_sent......................: 448 MB  3.7 MB/s
     http_req_blocked...............: avg=2.77µs  min=891ns   med=2.18µs  max=5.52ms   p(90)=3.62µs  p(95)=4.38µs   p(99.9)=33.93µs
     http_req_connecting............: avg=234ns   min=0s      med=0s      max=3.26ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=15.89ms min=1.22ms  med=15.86ms max=288.71ms p(90)=21.23ms p(95)=22.7ms   p(99.9)=29.92ms
       { expected_response:true }...: avg=15.89ms min=1.22ms  med=15.86ms max=288.71ms p(90)=21.23ms p(95)=22.7ms   p(99.9)=29.92ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 372773
     http_req_receiving.............: avg=75.6µs  min=23.79µs med=51.71µs max=211.46ms p(90)=94.9µs  p(95)=181.77µs p(99.9)=1.34ms 
     http_req_sending...............: avg=34.03µs min=4.25µs  med=9.43µs  max=123.23ms p(90)=17.67µs p(95)=107.64µs p(99.9)=1.38ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=15.78ms min=1.17ms  med=15.76ms max=260.38ms p(90)=21.12ms p(95)=22.59ms  p(99.9)=29.77ms
     http_reqs......................: 372773  3102.01/s
     iteration_duration.............: avg=16.09ms min=3.58ms  med=16.05ms max=296.93ms p(90)=21.42ms p(95)=22.9ms   p(99.9)=30.17ms
     iterations.....................: 372673  3101.177855/s
     success_rate...................: 100.00% ✓ 372673      ✗ 0     
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

     checks.........................: 100.00% ✓ 629811      ✗ 0     
     data_received..................: 18 GB   153 MB/s
     data_sent......................: 252 MB  2.1 MB/s
     http_req_blocked...............: avg=3.8µs   min=851ns   med=2.3µs   max=8.06ms   p(90)=4.17µs   p(95)=5.19µs   p(99.9)=33.94µs
     http_req_connecting............: avg=1.02µs  min=0s      med=0s      max=8.03ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=28.33ms min=1.86ms  med=27.74ms max=276.33ms p(90)=36.42ms  p(95)=39.32ms  p(99.9)=53.25ms
       { expected_response:true }...: avg=28.33ms min=1.86ms  med=27.74ms max=276.33ms p(90)=36.42ms  p(95)=39.32ms  p(99.9)=53.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 210037
     http_req_receiving.............: avg=81.59µs min=28.48µs med=60.56µs max=29.05ms  p(90)=113.29µs p(95)=156.64µs p(99.9)=1.2ms  
     http_req_sending...............: avg=31.07µs min=4.82µs  med=10.39µs max=179.11ms p(90)=20.93µs  p(95)=47.37µs  p(99.9)=1.17ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=28.22ms min=1.79ms  med=27.63ms max=270.62ms p(90)=36.3ms   p(95)=39.2ms   p(99.9)=53.01ms
     http_reqs......................: 210037  1746.64347/s
     iteration_duration.............: avg=28.57ms min=8.78ms  med=27.95ms max=308.25ms p(90)=36.63ms  p(95)=39.53ms  p(99.9)=53.53ms
     iterations.....................: 209937  1745.811881/s
     success_rate...................: 100.00% ✓ 209937      ✗ 0     
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

     checks.........................: 100.00% ✓ 539286      ✗ 0     
     data_received..................: 16 GB   131 MB/s
     data_sent......................: 216 MB  1.8 MB/s
     http_req_blocked...............: avg=4.42µs  min=952ns   med=2.44µs  max=8.86ms   p(90)=4.19µs  p(95)=4.92µs   p(99.9)=34.33µs 
     http_req_connecting............: avg=1.59µs  min=0s      med=0s      max=8.82ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.13ms min=2.1ms   med=32.22ms max=286.69ms p(90)=47.05ms p(95)=51.86ms  p(99.9)=77.55ms 
       { expected_response:true }...: avg=33.13ms min=2.1ms   med=32.22ms max=286.69ms p(90)=47.05ms p(95)=51.86ms  p(99.9)=77.55ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 179862
     http_req_receiving.............: avg=71.66µs min=25.83µs med=58.77µs max=115.35ms p(90)=97.1µs  p(95)=114.08µs p(99.9)=838.87µs
     http_req_sending...............: avg=22.53µs min=4.4µs   med=11.45µs max=216.6ms  p(90)=18.82µs p(95)=22.5µs   p(99.9)=760.56µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.04ms min=2.02ms  med=32.13ms max=271.66ms p(90)=46.96ms p(95)=51.76ms  p(99.9)=77.3ms  
     http_reqs......................: 179862  1495.363857/s
     iteration_duration.............: avg=33.36ms min=5.42ms  med=32.43ms max=300.66ms p(90)=47.27ms p(95)=52.08ms  p(99.9)=78.08ms 
     iterations.....................: 179762  1494.532462/s
     success_rate...................: 100.00% ✓ 179762      ✗ 0     
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

     checks.........................: 100.00% ✓ 517605      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=7.66µs  min=1.11µs med=2.51µs  max=47.3ms   p(90)=3.91µs  p(95)=4.56µs   p(99.9)=32.33µs 
     http_req_connecting............: avg=4.85µs  min=0s     med=0s      max=47.22ms  p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.53ms min=2.05ms med=33.58ms max=241.5ms  p(90)=50.06ms p(95)=55.17ms  p(99.9)=79.66ms 
       { expected_response:true }...: avg=34.53ms min=2.05ms med=33.58ms max=241.5ms  p(90)=50.06ms p(95)=55.17ms  p(99.9)=79.66ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 172635
     http_req_receiving.............: avg=72.43µs min=26.7µs med=60.52µs max=152.92ms p(90)=97.33µs p(95)=113.61µs p(99.9)=685.19µs
     http_req_sending...............: avg=26.61µs min=4.88µs med=11.41µs max=158.13ms p(90)=17.08µs p(95)=20.86µs  p(99.9)=813.36µs
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.43ms min=1.99ms med=33.49ms max=237.88ms p(90)=49.97ms p(95)=55.07ms  p(99.9)=79.27ms 
     http_reqs......................: 172635  1435.299715/s
     iteration_duration.............: avg=34.77ms min=4.64ms med=33.78ms max=300.23ms p(90)=50.27ms p(95)=55.38ms  p(99.9)=80.29ms 
     iterations.....................: 172535  1434.468308/s
     success_rate...................: 100.00% ✓ 172535      ✗ 0     
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

     checks.........................: 100.00% ✓ 199089     ✗ 0    
     data_received..................: 5.8 GB  48 MB/s
     data_sent......................: 80 MB   662 kB/s
     http_req_blocked...............: avg=7.2µs   min=961ns   med=2.51µs  max=9.13ms   p(90)=3.99µs   p(95)=4.56µs   p(99.9)=43.14µs 
     http_req_connecting............: avg=4.28µs  min=0s      med=0s      max=9.09ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=90.06ms min=3.76ms  med=87.12ms max=319.95ms p(90)=111.43ms p(95)=123.78ms p(99.9)=222.04ms
       { expected_response:true }...: avg=90.06ms min=3.76ms  med=87.12ms max=319.95ms p(90)=111.43ms p(95)=123.78ms p(99.9)=222.04ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 66463
     http_req_receiving.............: avg=80.39µs min=28.7µs  med=67.49µs max=116.98ms p(90)=101.9µs  p(95)=114.69µs p(99.9)=580.3µs 
     http_req_sending...............: avg=19.19µs min=4.61µs  med=12.27µs max=84.68ms  p(90)=18.22µs  p(95)=20.03µs  p(99.9)=635.86µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=89.96ms min=3.7ms   med=87.02ms max=319.76ms p(90)=111.34ms p(95)=123.68ms p(99.9)=221.77ms
     http_reqs......................: 66463   551.350533/s
     iteration_duration.............: avg=90.42ms min=24.58ms med=87.36ms max=340.13ms p(90)=111.67ms p(95)=124.08ms p(99.9)=223.32ms
     iterations.....................: 66363   550.520973/s
     success_rate...................: 100.00% ✓ 66363      ✗ 0    
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

     checks.........................: 100.00% ✓ 174459     ✗ 0    
     data_received..................: 5.1 GB  42 MB/s
     data_sent......................: 70 MB   580 kB/s
     http_req_blocked...............: avg=4.55µs   min=1.09µs  med=2.72µs   max=4.08ms   p(90)=4.1µs    p(95)=4.64µs   p(99.9)=54.3µs  
     http_req_connecting............: avg=1.62µs   min=0s      med=0s       max=4.04ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=102.79ms min=4.56ms  med=100.71ms max=321.92ms p(90)=138.54ms p(95)=149.92ms p(99.9)=196.7ms 
       { expected_response:true }...: avg=102.79ms min=4.56ms  med=100.71ms max=321.92ms p(90)=138.54ms p(95)=149.92ms p(99.9)=196.7ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 58253
     http_req_receiving.............: avg=79.36µs  min=28.01µs med=71.91µs  max=143.57ms p(90)=101.33µs p(95)=113.95µs p(99.9)=411.15µs
     http_req_sending...............: avg=26.41µs  min=4.94µs  med=13.9µs   max=155.31ms p(90)=19.11µs  p(95)=20.8µs   p(99.9)=479.26µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=102.68ms min=4.48ms  med=100.62ms max=321.81ms p(90)=138.44ms p(95)=149.82ms p(99.9)=196.18ms
     http_reqs......................: 58253   483.08535/s
     iteration_duration.............: avg=103.19ms min=24.43ms med=100.99ms max=335.29ms p(90)=138.78ms p(95)=150.19ms p(99.9)=198.36ms
     iterations.....................: 58153   482.256061/s
     success_rate...................: 100.00% ✓ 58153      ✗ 0    
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

     checks.........................: 100.00% ✓ 149151     ✗ 0    
     data_received..................: 4.4 GB  36 MB/s
     data_sent......................: 60 MB   496 kB/s
     http_req_blocked...............: avg=7.73µs   min=1.14µs  med=2.96µs   max=7.78ms   p(90)=4.32µs   p(95)=4.82µs   p(99.9)=1.43ms  
     http_req_connecting............: avg=4.25µs   min=0s      med=0s       max=7.75ms   p(90)=0s       p(95)=0s       p(99.9)=309.01µs
     http_req_duration..............: avg=120.24ms min=5.51ms  med=117.97ms max=334.06ms p(90)=157.15ms p(95)=169.33ms p(99.9)=219.19ms
       { expected_response:true }...: avg=120.24ms min=5.51ms  med=117.97ms max=334.06ms p(90)=157.15ms p(95)=169.33ms p(99.9)=219.19ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49817
     http_req_receiving.............: avg=80.53µs  min=28.71µs med=75.05µs  max=85.35ms  p(90)=103.55µs p(95)=115.67µs p(99.9)=487.44µs
     http_req_sending...............: avg=27.43µs  min=5.25µs  med=15.43µs  max=137.87ms p(90)=20.11µs  p(95)=21.83µs  p(99.9)=1.28ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=120.13ms min=5.39ms  med=117.86ms max=329.59ms p(90)=157.05ms p(95)=169.22ms p(99.9)=217.72ms
     http_reqs......................: 49817   412.758047/s
     iteration_duration.............: avg=120.72ms min=31.31ms med=118.27ms max=346.27ms p(90)=157.41ms p(95)=169.62ms p(99.9)=219.91ms
     iterations.....................: 49717   411.929499/s
     success_rate...................: 100.00% ✓ 49717      ✗ 0    
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

     checks.........................: 100.00% ✓ 97359      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   324 kB/s
     http_req_blocked...............: avg=6.36µs   min=1.11µs  med=3.19µs   max=4.16ms   p(90)=4.55µs   p(95)=5.15µs   p(99.9)=1.42ms  
     http_req_connecting............: avg=2.81µs   min=0s      med=0s       max=4.13ms   p(90)=0s       p(95)=0s       p(99.9)=1.22ms  
     http_req_duration..............: avg=184.15ms min=5.77ms  med=167.28ms max=782.27ms p(90)=216.19ms p(95)=251.5ms  p(99.9)=666.24ms
       { expected_response:true }...: avg=184.15ms min=5.77ms  med=167.28ms max=782.27ms p(90)=216.19ms p(95)=251.5ms  p(99.9)=666.24ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32553
     http_req_receiving.............: avg=98.48µs  min=29.08µs med=86.99µs  max=161.35ms p(90)=116.77µs p(95)=128.29µs p(99.9)=804.65µs
     http_req_sending...............: avg=21.83µs  min=5.21µs  med=16.45µs  max=62.69ms  p(90)=20.61µs  p(95)=22.29µs  p(99.9)=487.8µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.03ms min=5.7ms   med=167.17ms max=782.15ms p(90)=216.05ms p(95)=251.22ms p(99.9)=666.13ms
     http_reqs......................: 32553   269.432293/s
     iteration_duration.............: avg=184.98ms min=31.29ms med=167.63ms max=782.53ms p(90)=216.53ms p(95)=252.4ms  p(99.9)=666.53ms
     iterations.....................: 32453   268.604621/s
     success_rate...................: 100.00% ✓ 32453      ✗ 0    
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

     checks.........................: 100.00% ✓ 97236      ✗ 0    
     data_received..................: 2.8 GB  24 MB/s
     data_sent......................: 39 MB   323 kB/s
     http_req_blocked...............: avg=11.61µs  min=1.18µs  med=3.32µs   max=8.31ms   p(90)=4.62µs   p(95)=5.13µs   p(99.9)=4.87ms  
     http_req_connecting............: avg=7.77µs   min=0s      med=0s       max=8.27ms   p(90)=0s       p(95)=0s       p(99.9)=4.43ms  
     http_req_duration..............: avg=184.39ms min=7.58ms  med=184.13ms max=386.01ms p(90)=194.94ms p(95)=199.48ms p(99.9)=273.53ms
       { expected_response:true }...: avg=184.39ms min=7.58ms  med=184.13ms max=386.01ms p(90)=194.94ms p(95)=199.48ms p(99.9)=273.53ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32512
     http_req_receiving.............: avg=88.01µs  min=31.15µs med=82.44µs  max=73.68ms  p(90)=111.87µs p(95)=122.75µs p(99.9)=424.91µs
     http_req_sending...............: avg=26.6µs   min=4.93µs  med=16.3µs   max=72.96ms  p(90)=20.65µs  p(95)=22.37µs  p(99.9)=1.46ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.27ms min=7.45ms  med=184.02ms max=382.26ms p(90)=194.83ms p(95)=199.37ms p(99.9)=272.31ms
     http_reqs......................: 32512   268.725732/s
     iteration_duration.............: avg=185.22ms min=59.34ms med=184.47ms max=397.84ms p(90)=195.21ms p(95)=199.77ms p(99.9)=277.94ms
     iterations.....................: 32412   267.899189/s
     success_rate...................: 100.00% ✓ 32412      ✗ 0    
     vus............................: 2       min=2        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

