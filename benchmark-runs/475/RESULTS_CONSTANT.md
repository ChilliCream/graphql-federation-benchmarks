## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.10 | 5,132 | 5,148 | 5,114 | 0.2% | 361 MB | 72.1 KB |  |
| fusion-net-11 | 16.7.5 | 5,019 | 5,034 | 5,002 | 0.3% | 380 MB | 77.5 KB |  |
| fusion-fed-net-11 | 16.7.5 | 4,836 | 4,857 | 4,827 | 0.2% | 363 MB | 76.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.10 | 4,778 | 4,787 | 4,756 | 0.3% | 388 MB | 83.2 KB |  |
| fusion-aot-11 | 16.7.5 | 4,770 | 4,781 | 4,764 | 0.1% | 126 MB | 27.0 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.10 | 4,769 | 4,837 | 4,747 | 0.7% | 141 MB | 30.2 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.10 | 4,620 | 4,625 | 4,605 | 0.2% | 136 MB | 30.2 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 4,486 | 4,495 | 4,455 | 0.4% | 142 MB | 32.4 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,051 | 4,272 | 3,776 | 4.4% | 2,303 MB | 582.1 KB |  |
| hive-router | v0.3.10 | 2,996 | 3,013 | 2,924 | 1.2% | 91 MB | 31.0 KB |  |
| grafbase | 0.53.5 | 1,798 | 1,802 | 1,792 | 0.2% | 107 MB | 61.1 KB |  |
| cosmo | 0.365.2 | 1,422 | 1,423 | 1,418 | 0.1% | 170 MB | 122.4 KB |  |
| caliban | 3.2.0 | 1,419 | 1,420 | 1,414 | 0.2% | 3,926 MB | 2,832.9 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 546 | 549 | 545 | 0.3% | 2,762 MB | 5,179.8 KB |  |
| apollo-router | v2.19.0 | 485 | 486 | 484 | 0.2% | 173 MB | 365.6 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 431 | 432 | 431 | 0.1% | 192 MB | 456.5 KB |  |
| apollo-gateway | 2.14.4 | 273 | 274 | 273 | 0.2% | 2,154 MB | 8,079.9 KB |  |
| hive-gateway | 2.15.6 | 265 | 265 | 263 | 0.3% | 3,478 MB | 13,438.8 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1849053     ✗ 0     
     data_received..................: 54 GB   449 MB/s
     data_sent......................: 741 MB  6.2 MB/s
     http_req_blocked...............: avg=3.12µs   min=862ns    med=2.36µs  max=7.73ms   p(90)=3.57µs  p(95)=4.19µs   p(99.9)=30.53µs
     http_req_connecting............: avg=331ns    min=0s       med=0s      max=7.7ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.52ms   min=859.97µs med=8.64ms  max=262.59ms p(90)=14.76ms p(95)=17.96ms  p(99.9)=30.53ms
       { expected_response:true }...: avg=9.52ms   min=859.97µs med=8.64ms  max=262.59ms p(90)=14.76ms p(95)=17.96ms  p(99.9)=30.53ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 616451
     http_req_receiving.............: avg=100.56µs min=24.45µs  med=46.53µs max=148.59ms p(90)=89.83µs p(95)=201.89µs p(99.9)=6.5ms  
     http_req_sending...............: avg=43.46µs  min=4.49µs   med=8.62µs  max=244.48ms p(90)=14.55µs p(95)=103.65µs p(99.9)=4.91ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.38ms   min=800.38µs med=8.53ms  max=113.57ms p(90)=14.52ms p(95)=17.68ms  p(99.9)=30.12ms
     http_reqs......................: 616451  5132.474562/s
     iteration_duration.............: avg=9.72ms   min=1.25ms   med=8.82ms  max=309.75ms p(90)=14.97ms p(95)=18.18ms  p(99.9)=30.84ms
     iterations.....................: 616351  5131.641978/s
     success_rate...................: 100.00% ✓ 616351      ✗ 0     
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

     checks.........................: 100.00% ✓ 1808571     ✗ 0     
     data_received..................: 53 GB   439 MB/s
     data_sent......................: 725 MB  6.0 MB/s
     http_req_blocked...............: avg=2.46µs  min=791ns    med=1.91µs  max=5.9ms    p(90)=3.11µs  p(95)=3.74µs   p(99.9)=25.74µs
     http_req_connecting............: avg=151ns   min=0s       med=0s      max=3.47ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.74ms  min=840.92µs med=8.94ms  max=275.61ms p(90)=14.96ms p(95)=17.66ms  p(99.9)=29.57ms
       { expected_response:true }...: avg=9.74ms  min=840.92µs med=8.94ms  max=275.61ms p(90)=14.96ms p(95)=17.66ms  p(99.9)=29.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 602957
     http_req_receiving.............: avg=88.34µs min=24.17µs  med=44.92µs max=164.11ms p(90)=89.53µs p(95)=189.99µs p(99.9)=5.57ms 
     http_req_sending...............: avg=41.45µs min=4.32µs   med=7.88µs  max=184.94ms p(90)=14.36µs p(95)=101.04µs p(99.9)=4.51ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.61ms  min=769.8µs  med=8.83ms  max=268.62ms p(90)=14.76ms p(95)=17.41ms  p(99.9)=29.08ms
     http_reqs......................: 602957  5019.746897/s
     iteration_duration.............: avg=9.94ms  min=1.29ms   med=9.12ms  max=293.14ms p(90)=15.16ms p(95)=17.87ms  p(99.9)=29.86ms
     iterations.....................: 602857  5018.914376/s
     success_rate...................: 100.00% ✓ 602857      ✗ 0     
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

     checks.........................: 100.00% ✓ 1742772     ✗ 0     
     data_received..................: 51 GB   423 MB/s
     data_sent......................: 698 MB  5.8 MB/s
     http_req_blocked...............: avg=3.02µs   min=832ns    med=2.35µs  max=15.61ms  p(90)=3.67µs  p(95)=4.44µs   p(99.9)=33.1µs 
     http_req_connecting............: avg=163ns    min=0s       med=0s      max=3.9ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.1ms   min=990.95µs med=9.23ms  max=267.45ms p(90)=15.6ms  p(95)=18.52ms  p(99.9)=31.29ms
       { expected_response:true }...: avg=10.1ms   min=990.95µs med=9.23ms  max=267.45ms p(90)=15.6ms  p(95)=18.52ms  p(99.9)=31.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 581024
     http_req_receiving.............: avg=106.05µs min=24.95µs  med=48.89µs max=19.21ms  p(90)=98.25µs p(95)=206.68µs p(99.9)=7.41ms 
     http_req_sending...............: avg=45.7µs   min=4.45µs   med=8.59µs  max=130.11ms p(90)=16.4µs  p(95)=106.18µs p(99.9)=5.16ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.95ms   min=909.42µs med=9.11ms  max=267.24ms p(90)=15.37ms p(95)=18.23ms  p(99.9)=30.73ms
     http_reqs......................: 581024  4836.688036/s
     iteration_duration.............: avg=10.31ms  min=1.38ms   med=9.43ms  max=278.56ms p(90)=15.81ms p(95)=18.75ms  p(99.9)=31.59ms
     iterations.....................: 580924  4835.855593/s
     success_rate...................: 100.00% ✓ 580924      ✗ 0     
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

     checks.........................: 100.00% ✓ 1721994     ✗ 0     
     data_received..................: 50 GB   418 MB/s
     data_sent......................: 690 MB  5.7 MB/s
     http_req_blocked...............: avg=2.59µs   min=771ns    med=2µs     max=9.46ms   p(90)=3.11µs  p(95)=3.77µs   p(99.9)=26.96µs
     http_req_connecting............: avg=170ns    min=0s       med=0s      max=4.15ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.23ms  min=1ms      med=9.52ms  max=277.59ms p(90)=15.33ms p(95)=18.01ms  p(99.9)=30.41ms
       { expected_response:true }...: avg=10.23ms  min=1ms      med=9.52ms  max=277.59ms p(90)=15.33ms p(95)=18.01ms  p(99.9)=30.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 574098
     http_req_receiving.............: avg=100.04µs min=24.45µs  med=48.05µs max=190.04ms p(90)=94.26µs p(95)=199.08µs p(99.9)=6.89ms 
     http_req_sending...............: avg=42.06µs  min=4.51µs   med=8.41µs  max=196.73ms p(90)=14.91µs p(95)=100.35µs p(99.9)=4.41ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.09ms  min=929.52µs med=9.4ms   max=276.66ms p(90)=15.11ms p(95)=17.75ms  p(99.9)=29.81ms
     http_reqs......................: 574098  4778.965092/s
     iteration_duration.............: avg=10.44ms  min=1.34ms   med=9.71ms  max=286.72ms p(90)=15.54ms p(95)=18.23ms  p(99.9)=30.7ms 
     iterations.....................: 573998  4778.132662/s
     success_rate...................: 100.00% ✓ 573998      ✗ 0     
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

     checks.........................: 100.00% ✓ 1718904     ✗ 0     
     data_received..................: 50 GB   417 MB/s
     data_sent......................: 689 MB  5.7 MB/s
     http_req_blocked...............: avg=4.85µs  min=812ns    med=1.85µs  max=244.03ms p(90)=2.92µs  p(95)=3.46µs   p(99.9)=25.27µs
     http_req_connecting............: avg=2.64µs  min=0s       med=0s      max=243.87ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.27ms min=904.93µs med=9.67ms  max=285.45ms p(90)=15.03ms p(95)=17.36ms  p(99.9)=28.4ms 
       { expected_response:true }...: avg=10.27ms min=904.93µs med=9.67ms  max=285.45ms p(90)=15.03ms p(95)=17.36ms  p(99.9)=28.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 573068
     http_req_receiving.............: avg=87.62µs min=25.48µs  med=45.46µs max=110.51ms p(90)=90.05µs p(95)=197.42µs p(99.9)=4.93ms 
     http_req_sending...............: avg=39.29µs min=4.3µs    med=7.82µs  max=113.22ms p(90)=14.01µs p(95)=99.81µs  p(99.9)=3.66ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.14ms min=841.15µs med=9.56ms  max=237.93ms p(90)=14.86ms p(95)=17.15ms  p(99.9)=28.03ms
     http_reqs......................: 573068  4770.751117/s
     iteration_duration.............: avg=10.46ms min=1.54ms   med=9.85ms  max=307.96ms p(90)=15.23ms p(95)=17.57ms  p(99.9)=28.66ms
     iterations.....................: 572968  4769.918624/s
     success_rate...................: 100.00% ✓ 572968      ✗ 0     
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

     checks.........................: 100.00% ✓ 1718397     ✗ 0     
     data_received..................: 50 GB   417 MB/s
     data_sent......................: 689 MB  5.7 MB/s
     http_req_blocked...............: avg=2.38µs  min=781ns    med=1.83µs  max=5.63ms   p(90)=2.89µs  p(95)=3.42µs   p(99.9)=25.37µs
     http_req_connecting............: avg=157ns   min=0s       med=0s      max=3.81ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.28ms min=927.39µs med=9.67ms  max=267.82ms p(90)=15.08ms p(95)=17.44ms  p(99.9)=28.03ms
       { expected_response:true }...: avg=10.28ms min=927.39µs med=9.67ms  max=267.82ms p(90)=15.08ms p(95)=17.44ms  p(99.9)=28.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 572899
     http_req_receiving.............: avg=89.92µs min=25.07µs  med=45.73µs max=161.2ms  p(90)=89.52µs p(95)=200.71µs p(99.9)=5.19ms 
     http_req_sending...............: avg=37.53µs min=4.16µs   med=7.88µs  max=175.97ms p(90)=13.77µs p(95)=100.61µs p(99.9)=3.56ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.15ms min=854.28µs med=9.57ms  max=267.31ms p(90)=14.9ms  p(95)=17.22ms  p(99.9)=27.7ms 
     http_reqs......................: 572899  4769.132463/s
     iteration_duration.............: avg=10.46ms min=1.58ms   med=9.85ms  max=279.16ms p(90)=15.28ms p(95)=17.65ms  p(99.9)=28.31ms
     iterations.....................: 572799  4768.300007/s
     success_rate...................: 100.00% ✓ 572799      ✗ 0     
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

     checks.........................: 100.00% ✓ 1664895     ✗ 0     
     data_received..................: 49 GB   404 MB/s
     data_sent......................: 667 MB  5.6 MB/s
     http_req_blocked...............: avg=3.04µs  min=931ns    med=2.39µs  max=6.65ms   p(90)=3.77µs  p(95)=4.48µs   p(99.9)=36.35µs
     http_req_connecting............: avg=156ns   min=0s       med=0s      max=3.08ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.59ms min=1.06ms   med=9.9ms   max=274.21ms p(90)=15.71ms p(95)=18.59ms  p(99.9)=31.23ms
       { expected_response:true }...: avg=10.59ms min=1.06ms   med=9.9ms   max=274.21ms p(90)=15.71ms p(95)=18.59ms  p(99.9)=31.23ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 555065
     http_req_receiving.............: avg=100.1µs min=24.77µs  med=47.3µs  max=158.96ms p(90)=97.36µs p(95)=212.94µs p(99.9)=6.53ms 
     http_req_sending...............: avg=43.57µs min=4.64µs   med=8.89µs  max=84.91ms  p(90)=16.62µs p(95)=110.27µs p(99.9)=4.53ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.45ms min=999.32µs med=9.78ms  max=273.8ms  p(90)=15.48ms p(95)=18.3ms   p(99.9)=30.82ms
     http_reqs......................: 555065  4620.123986/s
     iteration_duration.............: avg=10.8ms  min=1.48ms   med=10.09ms max=290.17ms p(90)=15.92ms p(95)=18.82ms  p(99.9)=31.54ms
     iterations.....................: 554965  4619.291628/s
     success_rate...................: 100.00% ✓ 554965      ✗ 0     
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

     checks.........................: 100.00% ✓ 1616889     ✗ 0     
     data_received..................: 47 GB   393 MB/s
     data_sent......................: 648 MB  5.4 MB/s
     http_req_blocked...............: avg=2.61µs  min=801ns    med=2µs     max=5.32ms   p(90)=3.22µs  p(95)=3.86µs   p(99.9)=26.35µs
     http_req_connecting............: avg=180ns   min=0s       med=0s      max=3.94ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.92ms min=1.01ms   med=10.35ms max=286.38ms p(90)=15.8ms  p(95)=18.16ms  p(99.9)=30.41ms
       { expected_response:true }...: avg=10.92ms min=1.01ms   med=10.35ms max=286.38ms p(90)=15.8ms  p(95)=18.16ms  p(99.9)=30.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 539063
     http_req_receiving.............: avg=93.17µs min=24.74µs  med=46.71µs max=24.15ms  p(90)=94.39µs p(95)=205.12µs p(99.9)=5.63ms 
     http_req_sending...............: avg=41.13µs min=4.44µs   med=8.3µs   max=158.51ms p(90)=15.46µs p(95)=103.15µs p(99.9)=3.98ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.79ms min=967.67µs med=10.23ms max=285.87ms p(90)=15.61ms p(95)=17.93ms  p(99.9)=29.96ms
     http_reqs......................: 539063  4486.933726/s
     iteration_duration.............: avg=11.12ms min=1.66ms   med=10.54ms max=296.61ms p(90)=16ms    p(95)=18.37ms  p(99.9)=30.73ms
     iterations.....................: 538963  4486.101368/s
     success_rate...................: 100.00% ✓ 538963      ✗ 0     
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

     checks.........................: 100.00% ✓ 1459536     ✗ 0     
     data_received..................: 43 GB   354 MB/s
     data_sent......................: 585 MB  4.9 MB/s
     http_req_blocked...............: avg=2.85µs  min=871ns    med=2.01µs  max=9.83ms   p(90)=3.18µs  p(95)=3.76µs   p(99.9)=31.21µs
     http_req_connecting............: avg=472ns   min=0s       med=0s      max=7.71ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=12.13ms min=766.17µs med=12.28ms max=295.96ms p(90)=18.33ms p(95)=20.17ms  p(99.9)=29.74ms
       { expected_response:true }...: avg=12.13ms min=766.17µs med=12.28ms max=295.96ms p(90)=18.33ms p(95)=20.17ms  p(99.9)=29.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 486612
     http_req_receiving.............: avg=86.97µs min=26.27µs  med=48.41µs max=196.59ms p(90)=90.43µs p(95)=197.51µs p(99.9)=3.18ms 
     http_req_sending...............: avg=36.04µs min=4.57µs   med=8.69µs  max=181.21ms p(90)=14.84µs p(95)=106.16µs p(99.9)=2.34ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=12.01ms min=691.52µs med=12.17ms max=118.54ms p(90)=18.2ms  p(95)=20.03ms  p(99.9)=29.4ms 
     http_reqs......................: 486612  4051.342797/s
     iteration_duration.............: avg=12.32ms min=1.28ms   med=12.46ms max=320.31ms p(90)=18.52ms p(95)=20.36ms  p(99.9)=29.98ms
     iterations.....................: 486512  4050.510236/s
     success_rate...................: 100.00% ✓ 486512      ✗ 0     
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

     checks.........................: 100.00% ✓ 1079979     ✗ 0     
     data_received..................: 32 GB   262 MB/s
     data_sent......................: 433 MB  3.6 MB/s
     http_req_blocked...............: avg=2.56µs  min=872ns   med=2.15µs  max=2.66ms   p(90)=3.35µs  p(95)=3.97µs   p(99.9)=26.61µs
     http_req_connecting............: avg=146ns   min=0s      med=0s      max=2.63ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.46ms min=1.23ms  med=16.52ms max=268.36ms p(90)=22.1ms  p(95)=23.62ms  p(99.9)=30.83ms
       { expected_response:true }...: avg=16.46ms min=1.23ms  med=16.52ms max=268.36ms p(90)=22.1ms  p(95)=23.62ms  p(99.9)=30.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 360093
     http_req_receiving.............: avg=71.31µs min=27.09µs med=52.53µs max=61.82ms  p(90)=88.71µs p(95)=143.15µs p(99.9)=1.17ms 
     http_req_sending...............: avg=32.03µs min=4.5µs   med=9.47µs  max=191.22ms p(90)=15.63µs p(95)=97.15µs  p(99.9)=1.23ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.36ms min=1.18ms  med=16.42ms max=268.01ms p(90)=22ms    p(95)=23.51ms  p(99.9)=30.65ms
     http_reqs......................: 360093  2996.612094/s
     iteration_duration.............: avg=16.65ms min=2.33ms  med=16.71ms max=284.44ms p(90)=22.29ms p(95)=23.8ms   p(99.9)=31.05ms
     iterations.....................: 359993  2995.779917/s
     success_rate...................: 100.00% ✓ 359993      ✗ 0     
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

     checks.........................: 100.00% ✓ 648615      ✗ 0     
     data_received..................: 19 GB   158 MB/s
     data_sent......................: 260 MB  2.2 MB/s
     http_req_blocked...............: avg=3.91µs  min=1.01µs  med=3.01µs  max=3.59ms   p(90)=5µs      p(95)=6.02µs   p(99.9)=44.46µs
     http_req_connecting............: avg=454ns   min=0s      med=0s      max=3.56ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=27.5ms  min=1.81ms  med=26.87ms max=297.65ms p(90)=35.5ms   p(95)=38.39ms  p(99.9)=52.9ms 
       { expected_response:true }...: avg=27.5ms  min=1.81ms  med=26.87ms max=297.65ms p(90)=35.5ms   p(95)=38.39ms  p(99.9)=52.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 216305
     http_req_receiving.............: avg=90.08µs min=27.17µs med=63.53µs max=171.94ms p(90)=121.49µs p(95)=190.71µs p(99.9)=1.46ms 
     http_req_sending...............: avg=36.07µs min=4.93µs  med=11.57µs max=172.06ms p(90)=22.47µs  p(95)=103.9µs  p(99.9)=1.43ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=27.37ms min=1.72ms  med=26.75ms max=297.06ms p(90)=35.38ms  p(95)=38.25ms  p(99.9)=52.71ms
     http_reqs......................: 216305  1798.639364/s
     iteration_duration.............: avg=27.74ms min=7.26ms  med=27.1ms  max=309.31ms p(90)=35.72ms  p(95)=38.62ms  p(99.9)=53.16ms
     iterations.....................: 216205  1797.807835/s
     success_rate...................: 100.00% ✓ 216205      ✗ 0     
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

     checks.........................: 100.00% ✓ 513147      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 206 MB  1.7 MB/s
     http_req_blocked...............: avg=3.5µs   min=1.12µs  med=2.63µs  max=3.6ms    p(90)=4.1µs   p(95)=4.76µs   p(99.9)=33.42µs 
     http_req_connecting............: avg=572ns   min=0s      med=0s      max=3.56ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.84ms min=2.14ms  med=33.88ms max=300.94ms p(90)=50.52ms p(95)=55.67ms  p(99.9)=80.83ms 
       { expected_response:true }...: avg=34.84ms min=2.14ms  med=33.88ms max=300.94ms p(90)=50.52ms p(95)=55.67ms  p(99.9)=80.83ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 171149
     http_req_receiving.............: avg=71.38µs min=26.39µs med=60.09µs max=78.74ms  p(90)=95.83µs p(95)=111.92µs p(99.9)=708.65µs
     http_req_sending...............: avg=24.1µs  min=5.11µs  med=11.15µs max=242.7ms  p(90)=16.61µs p(95)=20.3µs   p(99.9)=762.58µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.74ms min=2.01ms  med=33.79ms max=300.4ms  p(90)=50.42ms p(95)=55.58ms  p(99.9)=80.52ms 
     http_reqs......................: 171149  1422.947327/s
     iteration_duration.............: avg=35.07ms min=4.72ms  med=34.09ms max=313.67ms p(90)=50.72ms p(95)=55.87ms  p(99.9)=81.26ms 
     iterations.....................: 171049  1422.115919/s
     success_rate...................: 100.00% ✓ 171049      ✗ 0     
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

     checks.........................: 100.00% ✓ 511821      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 205 MB  1.7 MB/s
     http_req_blocked...............: avg=3.12µs  min=892ns   med=2.27µs  max=3.72ms   p(90)=3.84µs  p(95)=4.55µs   p(99.9)=30.86µs 
     http_req_connecting............: avg=539ns   min=0s      med=0s      max=3.69ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.93ms min=2.12ms  med=33.91ms max=305.61ms p(90)=49.83ms p(95)=55.03ms  p(99.9)=82.64ms 
       { expected_response:true }...: avg=34.93ms min=2.12ms  med=33.91ms max=305.61ms p(90)=49.83ms p(95)=55.03ms  p(99.9)=82.64ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 170707
     http_req_receiving.............: avg=70.69µs min=26.51µs med=58.86µs max=88.86ms  p(90)=92.97µs p(95)=107.58µs p(99.9)=796.67µs
     http_req_sending...............: avg=19.54µs min=4.64µs  med=10.83µs max=106.49ms p(90)=17.27µs p(95)=20.65µs  p(99.9)=714.47µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.84ms min=2.07ms  med=33.82ms max=285.16ms p(90)=49.74ms p(95)=54.95ms  p(99.9)=82.52ms 
     http_reqs......................: 170707  1419.114166/s
     iteration_duration.............: avg=35.16ms min=5.29ms  med=34.11ms max=320.76ms p(90)=50.03ms p(95)=55.24ms  p(99.9)=82.89ms 
     iterations.....................: 170607  1418.28285/s
     success_rate...................: 100.00% ✓ 170607      ✗ 0     
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

     checks.........................: 100.00% ✓ 197199     ✗ 0    
     data_received..................: 5.8 GB  48 MB/s
     data_sent......................: 79 MB   656 kB/s
     http_req_blocked...............: avg=4.58µs  min=1.12µs  med=2.94µs  max=3.93ms   p(90)=4.38µs   p(95)=5.02µs   p(99.9)=46.65µs 
     http_req_connecting............: avg=1.39µs  min=0s      med=0s      max=3.89ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=90.93ms min=3.85ms  med=92.4ms  max=325.47ms p(90)=128.7ms  p(95)=141.31ms p(99.9)=237.91ms
       { expected_response:true }...: avg=90.93ms min=3.85ms  med=92.4ms  max=325.47ms p(90)=128.7ms  p(95)=141.31ms p(99.9)=237.91ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 65833
     http_req_receiving.............: avg=80.37µs min=28.79µs med=71.57µs max=112.89ms p(90)=104.48µs p(95)=116.6µs  p(99.9)=568.45µs
     http_req_sending...............: avg=22.7µs  min=5.2µs   med=14.4µs  max=113.21ms p(90)=19.86µs  p(95)=21.82µs  p(99.9)=582.66µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=90.83ms min=3.74ms  med=92.29ms max=324.83ms p(90)=128.6ms  p(95)=141.2ms  p(99.9)=237.55ms
     http_reqs......................: 65833   546.045368/s
     iteration_duration.............: avg=91.3ms  min=12.87ms med=92.82ms max=342.33ms p(90)=128.94ms p(95)=141.6ms  p(99.9)=238.69ms
     iterations.....................: 65733   545.215928/s
     success_rate...................: 100.00% ✓ 65733      ✗ 0    
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

     checks.........................: 100.00% ✓ 175470     ✗ 0    
     data_received..................: 5.1 GB  43 MB/s
     data_sent......................: 70 MB   584 kB/s
     http_req_blocked...............: avg=4.46µs   min=1.09µs  med=2.73µs   max=4.06ms   p(90)=4.11µs   p(95)=4.65µs   p(99.9)=46.53µs 
     http_req_connecting............: avg=1.53µs   min=0s      med=0s       max=4.01ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=102.19ms min=4.49ms  med=100.21ms max=310.57ms p(90)=138.06ms p(95)=149.19ms p(99.9)=193.76ms
       { expected_response:true }...: avg=102.19ms min=4.49ms  med=100.21ms max=310.57ms p(90)=138.06ms p(95)=149.19ms p(99.9)=193.76ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 58590
     http_req_receiving.............: avg=76.19µs  min=28.92µs med=70.63µs  max=87.78ms  p(90)=101.13µs p(95)=114.04µs p(99.9)=423.01µs
     http_req_sending...............: avg=20.76µs  min=4.75µs  med=13.51µs  max=69.48ms  p(90)=18.75µs  p(95)=20.46µs  p(99.9)=472.96µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=102.09ms min=4.42ms  med=100.13ms max=310.37ms p(90)=137.96ms p(95)=149.1ms  p(99.9)=192.7ms 
     http_reqs......................: 58590   485.892787/s
     iteration_duration.............: avg=102.59ms min=23.56ms med=100.49ms max=323.13ms p(90)=138.31ms p(95)=149.44ms p(99.9)=194.96ms
     iterations.....................: 58490   485.063477/s
     success_rate...................: 100.00% ✓ 58490      ✗ 0    
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

     checks.........................: 100.00% ✓ 156012     ✗ 0    
     data_received..................: 4.6 GB  38 MB/s
     data_sent......................: 63 MB   519 kB/s
     http_req_blocked...............: avg=5.21µs   min=1.11µs  med=3.17µs   max=4.02ms   p(90)=4.61µs   p(95)=5.18µs   p(99.9)=188.46µs
     http_req_connecting............: avg=1.83µs   min=0s      med=0s       max=3.98ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=114.93ms min=5.36ms  med=112.72ms max=318.29ms p(90)=150.17ms p(95)=161.56ms p(99.9)=208.31ms
       { expected_response:true }...: avg=114.93ms min=5.36ms  med=112.72ms max=318.29ms p(90)=150.17ms p(95)=161.56ms p(99.9)=208.31ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 52104
     http_req_receiving.............: avg=82.34µs  min=29.93µs med=76.94µs  max=62.16ms  p(90)=107.46µs p(95)=119.67µs p(99.9)=549.22µs
     http_req_sending...............: avg=22.09µs  min=5.3µs   med=15.82µs  max=78.8ms   p(90)=20.87µs  p(95)=22.64µs  p(99.9)=511.64µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=114.83ms min=5.27ms  med=112.61ms max=317.84ms p(90)=150.07ms p(95)=161.46ms p(99.9)=208.2ms 
     http_reqs......................: 52104   431.77385/s
     iteration_duration.............: avg=115.4ms  min=25.52ms med=113.01ms max=335.17ms p(90)=150.43ms p(95)=161.85ms p(99.9)=211.3ms 
     iterations.....................: 52004   430.945173/s
     success_rate...................: 100.00% ✓ 52004      ✗ 0    
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

     checks.........................: 100.00% ✓ 99066      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   329 kB/s
     http_req_blocked...............: avg=11.75µs  min=1.04µs  med=2.99µs   max=9.82ms   p(90)=4.3µs    p(95)=4.83µs   p(99.9)=5.14ms  
     http_req_connecting............: avg=8.34µs   min=0s      med=0s       max=9.76ms   p(90)=0s       p(95)=0s       p(99.9)=4.96ms  
     http_req_duration..............: avg=180.98ms min=7.59ms  med=179.77ms max=355.64ms p(90)=220.91ms p(95)=227.31ms p(99.9)=285.7ms 
       { expected_response:true }...: avg=180.98ms min=7.59ms  med=179.77ms max=355.64ms p(90)=220.91ms p(95)=227.31ms p(99.9)=285.7ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 33122
     http_req_receiving.............: avg=89.63µs  min=28.08µs med=84.17µs  max=59.25ms  p(90)=112.73µs p(95)=122.26µs p(99.9)=556.18µs
     http_req_sending...............: avg=26.1µs   min=5.04µs  med=16.21µs  max=82.74ms  p(90)=20.11µs  p(95)=21.9µs   p(99.9)=1.07ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=180.87ms min=7.49ms  med=179.62ms max=355.31ms p(90)=220.79ms p(95)=227.2ms  p(99.9)=285.54ms
     http_reqs......................: 33122   273.783515/s
     iteration_duration.............: avg=181.79ms min=74.1ms  med=180.86ms max=373.02ms p(90)=221.2ms  p(95)=227.58ms p(99.9)=287.07ms
     iterations.....................: 33022   272.956924/s
     success_rate...................: 100.00% ✓ 33022      ✗ 0    
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

     checks.........................: 100.00% ✓ 96090      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   319 kB/s
     http_req_blocked...............: avg=6.07µs   min=1.1µs   med=3.05µs   max=4.04ms   p(90)=4.33µs   p(95)=4.88µs   p(99.9)=1.2ms   
     http_req_connecting............: avg=2.85µs   min=0s      med=0s       max=4ms      p(90)=0s       p(95)=0s       p(99.9)=1.18ms  
     http_req_duration..............: avg=186.61ms min=5.82ms  med=170.26ms max=762.44ms p(90)=213.89ms p(95)=245.55ms p(99.9)=684.11ms
       { expected_response:true }...: avg=186.61ms min=5.82ms  med=170.26ms max=762.44ms p(90)=213.89ms p(95)=245.55ms p(99.9)=684.11ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32130
     http_req_receiving.............: avg=84.86µs  min=31.05µs med=81.53µs  max=7.86ms   p(90)=110.34µs p(95)=121.74µs p(99.9)=444.6µs 
     http_req_sending...............: avg=20.26µs  min=5.17µs  med=15.86µs  max=29.32ms  p(90)=20.21µs  p(95)=21.88µs  p(99.9)=431.41µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=186.51ms min=5.7ms   med=170.17ms max=762.35ms p(90)=213.79ms p(95)=245.46ms p(99.9)=684.05ms
     http_reqs......................: 32130   265.624577/s
     iteration_duration.............: avg=187.41ms min=72.74ms med=170.61ms max=762.64ms p(90)=214.2ms  p(95)=246.08ms p(99.9)=684.41ms
     iterations.....................: 32030   264.797859/s
     success_rate...................: 100.00% ✓ 32030      ✗ 0    
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

