## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.2 | 5,072 | 5,096 | 5,054 | 0.3% | 390 MB | 78.7 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.7 | 5,061 | 5,121 | 5,019 | 0.8% | 378 MB | 76.5 KB |  |
| fusion-fed-net-11 | 16.7.2 | 4,837 | 4,841 | 4,824 | 0.1% | 386 MB | 81.7 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.7 | 4,813 | 4,840 | 4,792 | 0.4% | 129 MB | 27.5 KB |  |
| fusion-aot-11 | 16.7.2 | 4,763 | 4,780 | 4,744 | 0.3% | 125 MB | 26.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.7 | 4,735 | 4,762 | 4,732 | 0.3% | 391 MB | 84.5 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.7 | 4,618 | 4,623 | 4,610 | 0.1% | 137 MB | 30.4 KB |  |
| fusion-fed-aot-11 | 16.7.2 | 4,530 | 4,552 | 4,523 | 0.3% | 135 MB | 30.4 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,232 | 4,349 | 4,221 | 1.3% | 2,299 MB | 556.3 KB |  |
| hive-router | v0.3.6 | 2,938 | 2,946 | 2,922 | 0.3% | 89 MB | 31.1 KB |  |
| grafbase | 0.53.5 | 1,863 | 1,869 | 1,859 | 0.2% | 111 MB | 61.1 KB |  |
| cosmo | 0.363.0 | 1,489 | 1,490 | 1,487 | 0.1% | 165 MB | 113.5 KB |  |
| caliban | 3.2.0 | 1,371 | 1,374 | 1,369 | 0.1% | 4,505 MB | 3,364.8 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 538 | 539 | 535 | 0.3% | 2,742 MB | 5,219.6 KB |  |
| apollo-router | v2.19.0 | 484 | 486 | 484 | 0.2% | 173 MB | 366.5 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 401 | 402 | 400 | 0.2% | 202 MB | 515.2 KB |  |
| apollo-gateway | 2.14.4 | 270 | 270 | 269 | 0.2% | 2,202 MB | 8,350.8 KB |  |
| hive-gateway | 2.15.3 | 269 | 270 | 269 | 0.2% | 3,542 MB | 13,482.9 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1827369     ✗ 0     
     data_received..................: 53 GB   444 MB/s
     data_sent......................: 732 MB  6.1 MB/s
     http_req_blocked...............: avg=2.46µs  min=801ns    med=1.89µs  max=5.48ms   p(90)=3.02µs  p(95)=3.63µs   p(99.9)=24.65µs
     http_req_connecting............: avg=149ns   min=0s       med=0s      max=3.97ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.64ms  min=791.34µs med=8.83ms  max=248.81ms p(90)=14.83ms p(95)=17.54ms  p(99.9)=29.4ms 
       { expected_response:true }...: avg=9.64ms  min=791.34µs med=8.83ms  max=248.81ms p(90)=14.83ms p(95)=17.54ms  p(99.9)=29.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 609223
     http_req_receiving.............: avg=90.21µs min=23.67µs  med=45.13µs max=225.36ms p(90)=87.86µs p(95)=186.51µs p(99.9)=5.98ms 
     http_req_sending...............: avg=41.19µs min=4.44µs   med=8.01µs  max=140.48ms p(90)=14.25µs p(95)=98.71µs  p(99.9)=4.71ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.51ms  min=744.29µs med=8.73ms  max=248.36ms p(90)=14.63ms p(95)=17.27ms  p(99.9)=28.85ms
     http_reqs......................: 609223  5072.242085/s
     iteration_duration.............: avg=9.84ms  min=1.11ms   med=9.02ms  max=341.01ms p(90)=15.04ms p(95)=17.76ms  p(99.9)=29.71ms
     iterations.....................: 609123  5071.409509/s
     success_rate...................: 100.00% ✓ 609123      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1823574     ✗ 0     
     data_received..................: 53 GB   443 MB/s
     data_sent......................: 731 MB  6.1 MB/s
     http_req_blocked...............: avg=2.88µs  min=891ns    med=2.28µs  max=7.52ms   p(90)=3.53µs  p(95)=4.18µs   p(99.9)=33.36µs
     http_req_connecting............: avg=157ns   min=0s       med=0s      max=3.41ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.65ms  min=806.49µs med=8.75ms  max=238.42ms p(90)=15.09ms p(95)=18.05ms  p(99.9)=30.93ms
       { expected_response:true }...: avg=9.65ms  min=806.49µs med=8.75ms  max=238.42ms p(90)=15.09ms p(95)=18.05ms  p(99.9)=30.93ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 607958
     http_req_receiving.............: avg=93.58µs min=23.94µs  med=45.66µs max=25.19ms  p(90)=90.54µs p(95)=195.04µs p(99.9)=6.08ms 
     http_req_sending...............: avg=44.07µs min=4.28µs   med=8.3µs   max=158.17ms p(90)=15.12µs p(95)=104µs    p(99.9)=5.13ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.52ms  min=768.57µs med=8.64ms  max=238.3ms  p(90)=14.86ms p(95)=17.78ms  p(99.9)=30.34ms
     http_reqs......................: 607958  5061.299852/s
     iteration_duration.............: avg=9.86ms  min=1.26ms   med=8.94ms  max=345.27ms p(90)=15.3ms  p(95)=18.27ms  p(99.9)=31.26ms
     iterations.....................: 607858  5060.467343/s
     success_rate...................: 100.00% ✓ 607858      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1743162     ✗ 0     
     data_received..................: 51 GB   423 MB/s
     data_sent......................: 699 MB  5.8 MB/s
     http_req_blocked...............: avg=2.67µs  min=772ns    med=1.96µs  max=9.93ms   p(90)=3.13µs  p(95)=3.81µs   p(99.9)=26.66µs
     http_req_connecting............: avg=304ns   min=0s       med=0s      max=9.88ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.11ms min=995.56µs med=9.35ms  max=225.81ms p(90)=15.34ms p(95)=17.94ms  p(99.9)=29.83ms
       { expected_response:true }...: avg=10.11ms min=995.56µs med=9.35ms  max=225.81ms p(90)=15.34ms p(95)=17.94ms  p(99.9)=29.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 581154
     http_req_receiving.............: avg=96.9µs  min=23.96µs  med=47.47µs max=24.12ms  p(90)=93.09µs p(95)=194µs    p(99.9)=6.5ms  
     http_req_sending...............: avg=43.43µs min=4.52µs   med=8.34µs  max=163.56ms p(90)=15.55µs p(95)=100.27µs p(99.9)=4.79ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.97ms  min=917.04µs med=9.23ms  max=224.39ms p(90)=15.13ms p(95)=17.69ms  p(99.9)=29.29ms
     http_reqs......................: 581154  4837.77884/s
     iteration_duration.............: avg=10.31ms min=1.11ms   med=9.55ms  max=355.25ms p(90)=15.55ms p(95)=18.17ms  p(99.9)=30.18ms
     iterations.....................: 581054  4836.946397/s
     success_rate...................: 100.00% ✓ 581054      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1734108     ✗ 0     
     data_received..................: 51 GB   421 MB/s
     data_sent......................: 695 MB  5.8 MB/s
     http_req_blocked...............: avg=2.49µs  min=782ns    med=1.91µs  max=5.11ms   p(90)=3.05µs  p(95)=3.67µs   p(99.9)=26.69µs
     http_req_connecting............: avg=157ns   min=0s       med=0s      max=3.99ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.17ms min=901.08µs med=9.48ms  max=260.74ms p(90)=15.13ms p(95)=17.72ms  p(99.9)=29.03ms
       { expected_response:true }...: avg=10.17ms min=901.08µs med=9.48ms  max=260.74ms p(90)=15.13ms p(95)=17.72ms  p(99.9)=29.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 578136
     http_req_receiving.............: avg=91.95µs min=24.5µs   med=45.63µs max=30.48ms  p(90)=91.54µs p(95)=204.13µs p(99.9)=5.72ms 
     http_req_sending...............: avg=40.77µs min=4.52µs   med=8.15µs  max=101.83ms p(90)=14.68µs p(95)=104.59µs p(99.9)=4.25ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.04ms min=844.52µs med=9.37ms  max=260.51ms p(90)=14.92ms p(95)=17.46ms  p(99.9)=28.64ms
     http_reqs......................: 578136  4813.188406/s
     iteration_duration.............: avg=10.37ms min=1.49ms   med=9.67ms  max=291.02ms p(90)=15.33ms p(95)=17.93ms  p(99.9)=29.34ms
     iterations.....................: 578036  4812.355871/s
     success_rate...................: 100.00% ✓ 578036      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1716309     ✗ 0     
     data_received..................: 50 GB   417 MB/s
     data_sent......................: 688 MB  5.7 MB/s
     http_req_blocked...............: avg=2.42µs  min=772ns    med=1.85µs  max=6.47ms   p(90)=2.95µs  p(95)=3.5µs    p(99.9)=26.82µs
     http_req_connecting............: avg=155ns   min=0s       med=0s      max=3.7ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.29ms min=868.55µs med=9.66ms  max=273.98ms p(90)=15.09ms p(95)=17.44ms  p(99.9)=28.32ms
       { expected_response:true }...: avg=10.29ms min=868.55µs med=9.66ms  max=273.98ms p(90)=15.09ms p(95)=17.44ms  p(99.9)=28.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 572203
     http_req_receiving.............: avg=88.8µs  min=23.3µs   med=44.88µs max=113.64ms p(90)=89.37µs p(95)=200.11µs p(99.9)=5.43ms 
     http_req_sending...............: avg=38.15µs min=4.2µs    med=7.92µs  max=139.6ms  p(90)=13.96µs p(95)=100.74µs p(99.9)=3.69ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.16ms min=826.18µs med=9.55ms  max=273.55ms p(90)=14.91ms p(95)=17.22ms  p(99.9)=27.86ms
     http_reqs......................: 572203  4763.624331/s
     iteration_duration.............: avg=10.47ms min=1.44ms   med=9.84ms  max=283.04ms p(90)=15.29ms p(95)=17.65ms  p(99.9)=28.59ms
     iterations.....................: 572103  4762.791825/s
     success_rate...................: 100.00% ✓ 572103      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1706373     ✗ 0     
     data_received..................: 50 GB   414 MB/s
     data_sent......................: 684 MB  5.7 MB/s
     http_req_blocked...............: avg=3.09µs   min=942ns    med=2.49µs  max=7.37ms   p(90)=3.82µs  p(95)=4.56µs   p(99.9)=31.58µs
     http_req_connecting............: avg=150ns    min=0s       med=0s      max=3.33ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.33ms  min=1.03ms   med=9.51ms  max=271.36ms p(90)=15.79ms p(95)=18.63ms  p(99.9)=31.24ms
       { expected_response:true }...: avg=10.33ms  min=1.03ms   med=9.51ms  max=271.36ms p(90)=15.79ms p(95)=18.63ms  p(99.9)=31.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 568891
     http_req_receiving.............: avg=104.03µs min=25.62µs  med=49.54µs max=102.42ms p(90)=98.31µs p(95)=207.6µs  p(99.9)=6.78ms 
     http_req_sending...............: avg=46.4µs   min=4.32µs   med=8.91µs  max=214.31ms p(90)=16.17µs p(95)=106.57µs p(99.9)=5.14ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.18ms  min=971.92µs med=9.39ms  max=270.94ms p(90)=15.57ms p(95)=18.36ms  p(99.9)=30.78ms
     http_reqs......................: 568891  4735.392789/s
     iteration_duration.............: avg=10.53ms  min=1.21ms   med=9.71ms  max=283.05ms p(90)=16ms    p(95)=18.85ms  p(99.9)=31.52ms
     iterations.....................: 568791  4734.560399/s
     success_rate...................: 100.00% ✓ 568791      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1664334     ✗ 0     
     data_received..................: 49 GB   404 MB/s
     data_sent......................: 667 MB  5.6 MB/s
     http_req_blocked...............: avg=2.65µs  min=811ns   med=2.01µs  max=7.99ms   p(90)=3.33µs  p(95)=4.06µs   p(99.9)=30.63µs
     http_req_connecting............: avg=174ns   min=0s      med=0s      max=4.04ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.6ms  min=1.08ms  med=9.97ms  max=273.84ms p(90)=15.57ms p(95)=18.1ms   p(99.9)=30.15ms
       { expected_response:true }...: avg=10.6ms  min=1.08ms  med=9.97ms  max=273.84ms p(90)=15.57ms p(95)=18.1ms   p(99.9)=30.15ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 554878
     http_req_receiving.............: avg=96.52µs min=25.07µs med=46.69µs max=161.5ms  p(90)=96.26µs p(95)=203.9µs  p(99.9)=6.1ms  
     http_req_sending...............: avg=41.94µs min=4.36µs  med=8.19µs  max=158.96ms p(90)=16.15µs p(95)=104.11µs p(99.9)=4.52ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.46ms min=1ms     med=9.86ms  max=273.36ms p(90)=15.37ms p(95)=17.84ms  p(99.9)=29.73ms
     http_reqs......................: 554878  4618.632645/s
     iteration_duration.............: avg=10.8ms  min=1.64ms  med=10.16ms max=283.4ms  p(90)=15.78ms p(95)=18.32ms  p(99.9)=30.4ms 
     iterations.....................: 554778  4617.800276/s
     success_rate...................: 100.00% ✓ 554778      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1632573     ✗ 0     
     data_received..................: 48 GB   396 MB/s
     data_sent......................: 654 MB  5.4 MB/s
     http_req_blocked...............: avg=2.52µs  min=771ns   med=1.92µs  max=8.58ms   p(90)=3.15µs  p(95)=3.83µs   p(99.9)=27.04µs
     http_req_connecting............: avg=176ns   min=0s      med=0s      max=3.96ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.81ms min=1.08ms  med=10.24ms max=256.85ms p(90)=15.65ms p(95)=18.05ms  p(99.9)=29.78ms
       { expected_response:true }...: avg=10.81ms min=1.08ms  med=10.24ms max=256.85ms p(90)=15.65ms p(95)=18.05ms  p(99.9)=29.78ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 544291
     http_req_receiving.............: avg=94.65µs min=25.73µs med=47.01µs max=59.84ms  p(90)=97.29µs p(95)=205.54µs p(99.9)=5.54ms 
     http_req_sending...............: avg=39.73µs min=4.39µs  med=8.13µs  max=103.03ms p(90)=15.85µs p(95)=104.1µs  p(99.9)=3.88ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.68ms min=1.02ms  med=10.13ms max=256.43ms p(90)=15.45ms p(95)=17.81ms  p(99.9)=29.47ms
     http_reqs......................: 544291  4530.48984/s
     iteration_duration.............: avg=11.01ms min=1.68ms  med=10.43ms max=288.52ms p(90)=15.85ms p(95)=18.26ms  p(99.9)=30ms   
     iterations.....................: 544191  4529.657474/s
     success_rate...................: 100.00% ✓ 544191      ✗ 0     
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

     checks.........................: 100.00% ✓ 1525176     ✗ 0     
     data_received..................: 44 GB   370 MB/s
     data_sent......................: 611 MB  5.1 MB/s
     http_req_blocked...............: avg=2.57µs  min=832ns    med=2µs     max=4.64ms   p(90)=3.2µs   p(95)=3.81µs   p(99.9)=29.47µs
     http_req_connecting............: avg=170ns   min=0s       med=0s      max=3.43ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.6ms  min=829.17µs med=11.33ms max=293.31ms p(90)=16.71ms p(95)=18.65ms  p(99.9)=28.72ms
       { expected_response:true }...: avg=11.6ms  min=829.17µs med=11.33ms max=293.31ms p(90)=16.71ms p(95)=18.65ms  p(99.9)=28.72ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 508492
     http_req_receiving.............: avg=80.93µs min=23.23µs  med=47.24µs max=105.23ms p(90)=90.58µs p(95)=203.76µs p(99.9)=3.56ms 
     http_req_sending...............: avg=38.55µs min=4.62µs   med=8.61µs  max=214.7ms  p(90)=14.94µs p(95)=109.4µs  p(99.9)=2.99ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.48ms min=759.06µs med=11.22ms max=265.02ms p(90)=16.56ms p(95)=18.47ms  p(99.9)=28.48ms
     http_reqs......................: 508492  4232.871073/s
     iteration_duration.............: avg=11.79ms min=1.1ms    med=11.52ms max=304.12ms p(90)=16.9ms  p(95)=18.85ms  p(99.9)=28.99ms
     iterations.....................: 508392  4232.038637/s
     success_rate...................: 100.00% ✓ 508392      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1059102     ✗ 0     
     data_received..................: 31 GB   257 MB/s
     data_sent......................: 424 MB  3.5 MB/s
     http_req_blocked...............: avg=3.35µs  min=1.03µs  med=2.62µs  max=7.84ms   p(90)=4.03µs  p(95)=4.71µs   p(99.9)=35.86µs
     http_req_connecting............: avg=392ns   min=0s      med=0s      max=7.74ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.78ms min=1.39ms  med=16.86ms max=273.26ms p(90)=22.44ms p(95)=23.96ms  p(99.9)=31.5ms 
       { expected_response:true }...: avg=16.78ms min=1.39ms  med=16.86ms max=273.26ms p(90)=22.44ms p(95)=23.96ms  p(99.9)=31.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 353134
     http_req_receiving.............: avg=75.38µs min=26.07µs med=53.35µs max=119.93ms p(90)=93.77µs p(95)=170.03µs p(99.9)=1.31ms 
     http_req_sending...............: avg=35.05µs min=4.72µs  med=10.65µs max=164.05ms p(90)=17.82µs p(95)=108.7µs  p(99.9)=1.43ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.67ms min=1.34ms  med=16.75ms max=269.14ms p(90)=22.32ms p(95)=23.84ms  p(99.9)=31.27ms
     http_reqs......................: 353134  2938.402955/s
     iteration_duration.............: avg=16.98ms min=2.94ms  med=17.05ms max=292.55ms p(90)=22.63ms p(95)=24.15ms  p(99.9)=31.72ms
     iterations.....................: 353034  2937.570862/s
     success_rate...................: 100.00% ✓ 353034      ✗ 0     
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

     checks.........................: 100.00% ✓ 671763      ✗ 0     
     data_received..................: 20 GB   163 MB/s
     data_sent......................: 269 MB  2.2 MB/s
     http_req_blocked...............: avg=3.89µs  min=812ns   med=2.23µs  max=10.34ms  p(90)=4.15µs  p(95)=5.25µs   p(99.9)=33.6µs 
     http_req_connecting............: avg=1.16µs  min=0s      med=0s      max=10.26ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.55ms min=1.88ms  med=26.01ms max=300.69ms p(90)=34.53ms p(95)=37.32ms  p(99.9)=51.13ms
       { expected_response:true }...: avg=26.55ms min=1.88ms  med=26.01ms max=300.69ms p(90)=34.53ms p(95)=37.32ms  p(99.9)=51.13ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 224021
     http_req_receiving.............: avg=83.29µs min=27.11µs med=56.68µs max=92.81ms  p(90)=116.3µs p(95)=180.13µs p(99.9)=1.5ms  
     http_req_sending...............: avg=32.28µs min=4.76µs  med=9.7µs   max=110.21ms p(90)=21.82µs p(95)=94.81µs  p(99.9)=1.63ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.43ms min=1.8ms   med=25.9ms  max=300.36ms p(90)=34.41ms p(95)=37.2ms   p(99.9)=50.84ms
     http_reqs......................: 224021  1863.003017/s
     iteration_duration.............: avg=26.78ms min=7.68ms  med=26.22ms max=313.23ms p(90)=34.75ms p(95)=37.54ms  p(99.9)=51.42ms
     iterations.....................: 223921  1862.171397/s
     success_rate...................: 100.00% ✓ 223921      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.363.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 537075      ✗ 0     
     data_received..................: 16 GB   130 MB/s
     data_sent......................: 215 MB  1.8 MB/s
     http_req_blocked...............: avg=2.99µs  min=962ns   med=2.14µs  max=3.9ms    p(90)=3.62µs  p(95)=4.27µs   p(99.9)=32.73µs 
     http_req_connecting............: avg=534ns   min=0s      med=0s      max=3.86ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.29ms min=2.08ms  med=32.42ms max=289.98ms p(90)=47.86ms p(95)=52.79ms  p(99.9)=76.04ms 
       { expected_response:true }...: avg=33.29ms min=2.08ms  med=32.42ms max=289.98ms p(90)=47.86ms p(95)=52.79ms  p(99.9)=76.04ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 179125
     http_req_receiving.............: avg=67.85µs min=25.27µs med=56.55µs max=146.81ms p(90)=92.45µs p(95)=107.72µs p(99.9)=698.14µs
     http_req_sending...............: avg=20.32µs min=4.55µs  med=9.82µs  max=105.76ms p(90)=16.21µs p(95)=19.95µs  p(99.9)=751.35µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.2ms  min=1.97ms  med=32.33ms max=289.53ms p(90)=47.77ms p(95)=52.7ms   p(99.9)=75.87ms 
     http_reqs......................: 179125  1489.333037/s
     iteration_duration.............: avg=33.5ms  min=4.28ms  med=32.62ms max=299.17ms p(90)=48.05ms p(95)=52.98ms  p(99.9)=76.4ms  
     iterations.....................: 179025  1488.501588/s
     success_rate...................: 100.00% ✓ 179025      ✗ 0     
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

     checks.........................: 100.00% ✓ 494805      ✗ 0     
     data_received..................: 14 GB   120 MB/s
     data_sent......................: 198 MB  1.6 MB/s
     http_req_blocked...............: avg=3.16µs  min=922ns   med=2.24µs  max=4.38ms   p(90)=3.78µs  p(95)=4.44µs   p(99.9)=31.99µs 
     http_req_connecting............: avg=606ns   min=0s      med=0s      max=4.33ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=36.14ms min=2.11ms  med=35.05ms max=299.63ms p(90)=51.71ms p(95)=57.08ms  p(99.9)=85.48ms 
       { expected_response:true }...: avg=36.14ms min=2.11ms  med=35.05ms max=299.63ms p(90)=51.71ms p(95)=57.08ms  p(99.9)=85.48ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 165035
     http_req_receiving.............: avg=66.73µs min=27.18µs med=56.81µs max=73.35ms  p(90)=90.69µs p(95)=104.53µs p(99.9)=690.28µs
     http_req_sending...............: avg=20.62µs min=4.98µs  med=10.76µs max=240.75ms p(90)=16.99µs p(95)=20.33µs  p(99.9)=689.18µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=36.05ms min=2.05ms  med=34.97ms max=298.91ms p(90)=51.62ms p(95)=56.99ms  p(99.9)=85.29ms 
     http_reqs......................: 165035  1371.856746/s
     iteration_duration.............: avg=36.37ms min=5.44ms  med=35.26ms max=315.87ms p(90)=51.91ms p(95)=57.28ms  p(99.9)=85.84ms 
     iterations.....................: 164935  1371.025494/s
     success_rate...................: 100.00% ✓ 164935      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 194505     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   647 kB/s
     http_req_blocked...............: avg=4.15µs  min=1.22µs  med=3.16µs  max=2.86ms   p(90)=4.66µs   p(95)=5.33µs   p(99.9)=50.27µs 
     http_req_connecting............: avg=687ns   min=0s      med=0s      max=2.44ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.18ms min=3.91ms  med=89.83ms max=317.24ms p(90)=112.66ms p(95)=124.28ms p(99.9)=218.82ms
       { expected_response:true }...: avg=92.18ms min=3.91ms  med=89.83ms max=317.24ms p(90)=112.66ms p(95)=124.28ms p(99.9)=218.82ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64935
     http_req_receiving.............: avg=81.05µs min=28.73µs med=72.71µs max=71.7ms   p(90)=106.23µs p(95)=118.94µs p(99.9)=597.34µs
     http_req_sending...............: avg=21.55µs min=5.01µs  med=14.94µs max=62.76ms  p(90)=20.77µs  p(95)=22.83µs  p(99.9)=567.35µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.08ms min=3.85ms  med=89.73ms max=316.71ms p(90)=112.55ms p(95)=124.19ms p(99.9)=218.73ms
     http_reqs......................: 64935   538.615879/s
     iteration_duration.............: avg=92.56ms min=10.81ms med=90.09ms max=325.93ms p(90)=112.91ms p(95)=124.54ms p(99.9)=220.06ms
     iterations.....................: 64835   537.78641/s
     success_rate...................: 100.00% ✓ 64835      ✗ 0    
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

     checks.........................: 100.00% ✓ 174909     ✗ 0    
     data_received..................: 5.1 GB  42 MB/s
     data_sent......................: 70 MB   582 kB/s
     http_req_blocked...............: avg=4.18µs   min=1.06µs  med=2.62µs   max=3.63ms   p(90)=4.05µs   p(95)=4.6µs    p(99.9)=48.23µs 
     http_req_connecting............: avg=1.35µs   min=0s      med=0s       max=3.61ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=102.53ms min=4.53ms  med=100.45ms max=299.66ms p(90)=138.67ms p(95)=149.86ms p(99.9)=196.11ms
       { expected_response:true }...: avg=102.53ms min=4.53ms  med=100.45ms max=299.66ms p(90)=138.67ms p(95)=149.86ms p(99.9)=196.11ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 58403
     http_req_receiving.............: avg=73.8µs   min=28.94µs med=67.65µs  max=22.51ms  p(90)=98.3µs   p(95)=111.28µs p(99.9)=480.12µs
     http_req_sending...............: avg=18.22µs  min=5.04µs  med=13.07µs  max=50.29ms  p(90)=18.86µs  p(95)=20.62µs  p(99.9)=501.3µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=102.44ms min=4.41ms  med=100.36ms max=286.49ms p(90)=138.57ms p(95)=149.77ms p(99.9)=196.01ms
     http_reqs......................: 58403   484.319504/s
     iteration_duration.............: avg=102.93ms min=21.27ms med=100.73ms max=306.6ms  p(90)=138.93ms p(95)=150.11ms p(99.9)=197.91ms
     iterations.....................: 58303   483.490232/s
     success_rate...................: 100.00% ✓ 58303      ✗ 0    
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

     checks.........................: 100.00% ✓ 145059     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   482 kB/s
     http_req_blocked...............: avg=6.52µs   min=1.33µs  med=3.36µs   max=7.44ms   p(90)=4.7µs    p(95)=5.29µs   p(99.9)=218.59µs
     http_req_connecting............: avg=2.88µs   min=0s      med=0s       max=7.39ms   p(90)=0s       p(95)=0s       p(99.9)=89.12µs 
     http_req_duration..............: avg=123.61ms min=5.49ms  med=121.24ms max=304.92ms p(90)=161.75ms p(95)=174.57ms p(99.9)=225.22ms
       { expected_response:true }...: avg=123.61ms min=5.49ms  med=121.24ms max=304.92ms p(90)=161.75ms p(95)=174.57ms p(99.9)=225.22ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48453
     http_req_receiving.............: avg=79.25µs  min=31.5µs  med=74.6µs   max=32.74ms  p(90)=103.99µs p(95)=115.78µs p(99.9)=440.78µs
     http_req_sending...............: avg=20.85µs  min=5.7µs   med=15.77µs  max=17.6ms   p(90)=20.83µs  p(95)=22.66µs  p(99.9)=760.9µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=123.51ms min=5.36ms  med=121.14ms max=300.72ms p(90)=161.64ms p(95)=174.49ms p(99.9)=225.13ms
     http_reqs......................: 48453   401.4404/s
     iteration_duration.............: avg=124.11ms min=27.65ms med=121.54ms max=317.8ms  p(90)=162.05ms p(95)=174.87ms p(99.9)=227.49ms
     iterations.....................: 48353   400.611885/s
     success_rate...................: 100.00% ✓ 48353      ✗ 0    
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

     checks.........................: 100.00% ✓ 97917      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   325 kB/s
     http_req_blocked...............: avg=6.21µs   min=1.07µs  med=2.88µs   max=3.95ms   p(90)=4.11µs   p(95)=4.62µs   p(99.9)=1.58ms  
     http_req_connecting............: avg=3.09µs   min=0s      med=0s       max=3.89ms   p(90)=0s       p(95)=0s       p(99.9)=1.55ms  
     http_req_duration..............: avg=183.12ms min=7.55ms  med=183.89ms max=394.59ms p(90)=194.03ms p(95)=198.98ms p(99.9)=267.75ms
       { expected_response:true }...: avg=183.12ms min=7.55ms  med=183.89ms max=394.59ms p(90)=194.03ms p(95)=198.98ms p(99.9)=267.75ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32739
     http_req_receiving.............: avg=84.43µs  min=28.99µs med=77.79µs  max=67.26ms  p(90)=106.52µs p(95)=116.8µs  p(99.9)=472.02µs
     http_req_sending...............: avg=22.62µs  min=5.18µs  med=14.73µs  max=74.26ms  p(90)=18.96µs  p(95)=20.7µs   p(99.9)=405.42µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.01ms min=7.45ms  med=183.79ms max=394.21ms p(90)=193.92ms p(95)=198.87ms p(99.9)=267.68ms
     http_reqs......................: 32739   270.63847/s
     iteration_duration.............: avg=183.93ms min=32.71ms med=184.22ms max=401.64ms p(90)=194.3ms  p(95)=199.25ms p(99.9)=271.05ms
     iterations.....................: 32639   269.811815/s
     success_rate...................: 100.00% ✓ 32639      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 97683      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   324 kB/s
     http_req_blocked...............: avg=9.16µs   min=1.11µs  med=3.09µs   max=8.95ms   p(90)=4.4µs    p(95)=4.95µs   p(99.9)=3.15ms  
     http_req_connecting............: avg=5.59µs   min=0s      med=0s       max=7.44ms   p(90)=0s       p(95)=0s       p(99.9)=2.99ms  
     http_req_duration..............: avg=183.67ms min=5.72ms  med=168.71ms max=731.49ms p(90)=225.23ms p(95)=256.84ms p(99.9)=680.3ms 
       { expected_response:true }...: avg=183.67ms min=5.72ms  med=168.71ms max=731.49ms p(90)=225.23ms p(95)=256.84ms p(99.9)=680.3ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 32661
     http_req_receiving.............: avg=87.95µs  min=32.47µs med=84.91µs  max=10.03ms  p(90)=113.7µs  p(95)=124.25µs p(99.9)=671.57µs
     http_req_sending...............: avg=20.87µs  min=5.38µs  med=16.19µs  max=8.13ms   p(90)=20.38µs  p(95)=22.13µs  p(99.9)=1.62ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.56ms min=5.57ms  med=168.61ms max=731.39ms p(90)=225.13ms p(95)=256.72ms p(99.9)=680.19ms
     http_reqs......................: 32661   269.613549/s
     iteration_duration.............: avg=184.46ms min=84.57ms med=169.09ms max=731.74ms p(90)=225.65ms p(95)=257.22ms p(99.9)=680.57ms
     iterations.....................: 32561   268.788058/s
     success_rate...................: 100.00% ✓ 32561      ✗ 0    
     vus............................: 15      min=15       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

