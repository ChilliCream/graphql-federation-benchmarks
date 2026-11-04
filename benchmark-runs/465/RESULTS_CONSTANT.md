## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 5,121 | 5,155 | 5,021 | 1.0% | 380 MB | 75.9 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 5,102 | 5,114 | 5,069 | 0.3% | 380 MB | 76.3 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,885 | 4,912 | 4,877 | 0.3% | 377 MB | 79.0 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,877 | 4,880 | 4,858 | 0.2% | 136 MB | 28.6 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,809 | 4,831 | 4,793 | 0.3% | 394 MB | 84.0 KB |  |
| fusion-aot-11 | 16.7.3 | 4,777 | 4,817 | 4,755 | 0.5% | 130 MB | 27.9 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,586 | 4,618 | 4,560 | 0.5% | 131 MB | 29.3 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,489 | 4,513 | 4,471 | 0.4% | 137 MB | 31.3 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,180 | 4,494 | 4,019 | 4.3% | 2,304 MB | 564.4 KB |  |
| hive-router | v0.3.10 | 3,032 | 3,066 | 2,977 | 1.1% | 91 MB | 30.7 KB |  |
| grafbase | 0.53.5 | 1,876 | 1,881 | 1,871 | 0.2% | 117 MB | 64.0 KB |  |
| caliban | 3.2.0 | 1,525 | 1,530 | 1,515 | 0.5% | 5,184 MB | 3,481.2 KB |  |
| cosmo | 0.365.2 | 1,487 | 1,491 | 1,485 | 0.2% | 167 MB | 115.0 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 537 | 538 | 536 | 0.1% | 2,757 MB | 5,256.6 KB |  |
| apollo-router | v2.19.0 | 487 | 488 | 485 | 0.2% | 173 MB | 363.3 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 432 | 432 | 432 | 0.0% | 201 MB | 477.4 KB |  |
| apollo-gateway | 2.14.4 | 277 | 277 | 276 | 0.2% | 2,143 MB | 7,922.5 KB |  |
| hive-gateway | 2.15.6 | 265 | 267 | 264 | 0.4% | 3,522 MB | 13,607.7 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1845012     ✗ 0     
     data_received..................: 54 GB   448 MB/s
     data_sent......................: 739 MB  6.2 MB/s
     http_req_blocked...............: avg=2.96µs  min=812ns    med=2.08µs  max=8.51ms   p(90)=3.3µs   p(95)=3.95µs   p(99.9)=29.37µs
     http_req_connecting............: avg=459ns   min=0s       med=0s      max=8.48ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.55ms  min=786.84µs med=8.69ms  max=266.27ms p(90)=14.87ms p(95)=17.66ms  p(99.9)=29.73ms
       { expected_response:true }...: avg=9.55ms  min=786.84µs med=8.69ms  max=266.27ms p(90)=14.87ms p(95)=17.66ms  p(99.9)=29.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 615104
     http_req_receiving.............: avg=93.81µs min=23.86µs  med=44.95µs max=131.5ms  p(90)=89.62µs p(95)=190.41µs p(99.9)=6.48ms 
     http_req_sending...............: avg=42.72µs min=4.27µs   med=8.14µs  max=177.24ms p(90)=14.46µs p(95)=99.74µs  p(99.9)=4.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.41ms  min=744.18µs med=8.58ms  max=264.68ms p(90)=14.64ms p(95)=17.4ms   p(99.9)=29.25ms
     http_reqs......................: 615104  5121.44312/s
     iteration_duration.............: avg=9.74ms  min=977.84µs med=8.87ms  max=282.76ms p(90)=15.07ms p(95)=17.88ms  p(99.9)=30.01ms
     iterations.....................: 615004  5120.610505/s
     success_rate...................: 100.00% ✓ 615004      ✗ 0     
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

     checks.........................: 100.00% ✓ 1838412     ✗ 0     
     data_received..................: 54 GB   447 MB/s
     data_sent......................: 737 MB  6.1 MB/s
     http_req_blocked...............: avg=2.47µs  min=772ns    med=1.9µs   max=6.87ms   p(90)=3.06µs  p(95)=3.71µs  p(99.9)=25.95µs
     http_req_connecting............: avg=145ns   min=0s       med=0s      max=3.15ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=9.58ms  min=818.79µs med=8.77ms  max=287.5ms  p(90)=14.75ms p(95)=17.48ms p(99.9)=29.4ms 
       { expected_response:true }...: avg=9.58ms  min=818.79µs med=8.77ms  max=287.5ms  p(90)=14.75ms p(95)=17.48ms p(99.9)=29.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 612904
     http_req_receiving.............: avg=93.61µs min=23.99µs  med=45.34µs max=146.16ms p(90)=89.45µs p(95)=189.1µs p(99.9)=6.26ms 
     http_req_sending...............: avg=41.3µs  min=4.31µs   med=7.98µs  max=91.05ms  p(90)=14.47µs p(95)=98.51µs p(99.9)=4.61ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=9.45ms  min=738.57µs med=8.66ms  max=286.95ms p(90)=14.54ms p(95)=17.23ms p(99.9)=28.86ms
     http_reqs......................: 612904  5102.649414/s
     iteration_duration.............: avg=9.78ms  min=976.8µs  med=8.95ms  max=297.77ms p(90)=14.96ms p(95)=17.7ms  p(99.9)=29.68ms
     iterations.....................: 612804  5101.816878/s
     success_rate...................: 100.00% ✓ 612804      ✗ 0     
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

     checks.........................: 100.00% ✓ 1760253     ✗ 0     
     data_received..................: 51 GB   428 MB/s
     data_sent......................: 705 MB  5.9 MB/s
     http_req_blocked...............: avg=2.76µs   min=761ns    med=1.9µs   max=8.45ms   p(90)=3.11µs  p(95)=3.88µs   p(99.9)=27.38µs
     http_req_connecting............: avg=397ns    min=0s       med=0s      max=8.26ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.01ms  min=965.24µs med=9.2ms   max=306.35ms p(90)=15.31ms p(95)=18.07ms  p(99.9)=30.84ms
       { expected_response:true }...: avg=10.01ms  min=965.24µs med=9.2ms   max=306.35ms p(90)=15.31ms p(95)=18.07ms  p(99.9)=30.84ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 586851
     http_req_receiving.............: avg=100.98µs min=25.19µs  med=47.41µs max=106.66ms p(90)=95.95µs p(95)=196.54µs p(99.9)=6.92ms 
     http_req_sending...............: avg=43.32µs  min=3.89µs   med=8.18µs  max=102.69ms p(90)=15.9µs  p(95)=101.19µs p(99.9)=4.99ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.86ms   min=901.45µs med=9.08ms  max=305.27ms p(90)=15.08ms p(95)=17.79ms  p(99.9)=30.29ms
     http_reqs......................: 586851  4885.317297/s
     iteration_duration.............: avg=10.21ms  min=1.35ms   med=9.4ms   max=317.41ms p(90)=15.51ms p(95)=18.28ms  p(99.9)=31.12ms
     iterations.....................: 586751  4884.484834/s
     success_rate...................: 100.00% ✓ 586751      ✗ 0     
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

     checks.........................: 100.00% ✓ 1757370     ✗ 0     
     data_received..................: 51 GB   427 MB/s
     data_sent......................: 704 MB  5.9 MB/s
     http_req_blocked...............: avg=2.52µs  min=782ns    med=1.82µs  max=9.17ms   p(90)=2.95µs  p(95)=3.52µs   p(99.9)=24.31µs
     http_req_connecting............: avg=295ns   min=0s       med=0s      max=9.11ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.04ms min=917.01µs med=9.37ms  max=270.23ms p(90)=14.93ms p(95)=17.43ms  p(99.9)=28.6ms 
       { expected_response:true }...: avg=10.04ms min=917.01µs med=9.37ms  max=270.23ms p(90)=14.93ms p(95)=17.43ms  p(99.9)=28.6ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 585890
     http_req_receiving.............: avg=88.56µs min=23.68µs  med=43.88µs max=147.15ms p(90)=88.05µs p(95)=197.47µs p(99.9)=5.64ms 
     http_req_sending...............: avg=41.45µs min=4.27µs   med=7.92µs  max=214.01ms p(90)=14.35µs p(95)=101.75µs p(99.9)=4.25ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.91ms  min=840.63µs med=9.27ms  max=230.38ms p(90)=14.73ms p(95)=17.19ms  p(99.9)=28.25ms
     http_reqs......................: 585890  4877.706377/s
     iteration_duration.............: avg=10.23ms min=1.09ms   med=9.55ms  max=284.53ms p(90)=15.12ms p(95)=17.64ms  p(99.9)=28.89ms
     iterations.....................: 585790  4876.873847/s
     success_rate...................: 100.00% ✓ 585790      ✗ 0     
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

     checks.........................: 100.00% ✓ 1733166     ✗ 0     
     data_received..................: 51 GB   421 MB/s
     data_sent......................: 695 MB  5.8 MB/s
     http_req_blocked...............: avg=2.46µs  min=781ns    med=1.9µs   max=7.97ms   p(90)=3.04µs  p(95)=3.71µs   p(99.9)=25.95µs
     http_req_connecting............: avg=136ns   min=0s       med=0s      max=3.38ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.17ms min=1.03ms   med=9.43ms  max=281.97ms p(90)=15.36ms p(95)=17.9ms   p(99.9)=30.14ms
       { expected_response:true }...: avg=10.17ms min=1.03ms   med=9.43ms  max=281.97ms p(90)=15.36ms p(95)=17.9ms   p(99.9)=30.14ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 577822
     http_req_receiving.............: avg=93.57µs min=25.54µs  med=47.42µs max=123.97ms p(90)=93.11µs p(95)=191.44µs p(99.9)=5.83ms 
     http_req_sending...............: avg=41.31µs min=4.24µs   med=8.02µs  max=269.71ms p(90)=14.87µs p(95)=98.52µs  p(99.9)=4.43ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.04ms min=961.54µs med=9.31ms  max=253.29ms p(90)=15.16ms p(95)=17.66ms  p(99.9)=29.71ms
     http_reqs......................: 577822  4809.843659/s
     iteration_duration.............: avg=10.37ms min=1.46ms   med=9.62ms  max=297.7ms  p(90)=15.56ms p(95)=18.11ms  p(99.9)=30.42ms
     iterations.....................: 577722  4809.01125/s
     success_rate...................: 100.00% ✓ 577722      ✗ 0     
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

     checks.........................: 100.00% ✓ 1721178     ✗ 0     
     data_received..................: 50 GB   418 MB/s
     data_sent......................: 690 MB  5.7 MB/s
     http_req_blocked...............: avg=3.12µs  min=801ns    med=1.89µs  max=104.83ms p(90)=2.99µs  p(95)=3.53µs   p(99.9)=24.32µs
     http_req_connecting............: avg=728ns   min=0s       med=0s      max=35.91ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.25ms min=949.82µs med=9.63ms  max=255.64ms p(90)=15.07ms p(95)=17.48ms  p(99.9)=28.37ms
       { expected_response:true }...: avg=10.25ms min=949.82µs med=9.63ms  max=255.64ms p(90)=15.07ms p(95)=17.48ms  p(99.9)=28.37ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 573826
     http_req_receiving.............: avg=87.65µs min=24.32µs  med=44.55µs max=138.01ms p(90)=86.91µs p(95)=197.64µs p(99.9)=5.44ms 
     http_req_sending...............: avg=39.02µs min=4.38µs   med=8.06µs  max=238.19ms p(90)=13.83µs p(95)=99.45µs  p(99.9)=3.77ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.13ms min=884.88µs med=9.52ms  max=253.25ms p(90)=14.89ms p(95)=17.25ms  p(99.9)=28.02ms
     http_reqs......................: 573826  4777.007764/s
     iteration_duration.............: avg=10.44ms min=1.45ms   med=9.81ms  max=273.68ms p(90)=15.27ms p(95)=17.68ms  p(99.9)=28.58ms
     iterations.....................: 573726  4776.17528/s
     success_rate...................: 100.00% ✓ 573726      ✗ 0     
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

     checks.........................: 100.00% ✓ 1652667     ✗ 0     
     data_received..................: 48 GB   401 MB/s
     data_sent......................: 662 MB  5.5 MB/s
     http_req_blocked...............: avg=4.5µs    min=792ns   med=2.45µs  max=132.72ms p(90)=3.86µs  p(95)=4.63µs   p(99.9)=32.3µs 
     http_req_connecting............: avg=1.5µs    min=0s      med=0s      max=132.56ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.67ms  min=1.09ms  med=9.95ms  max=302.14ms p(90)=15.94ms p(95)=18.69ms  p(99.9)=31.32ms
       { expected_response:true }...: avg=10.67ms  min=1.09ms  med=9.95ms  max=302.14ms p(90)=15.94ms p(95)=18.69ms  p(99.9)=31.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 550989
     http_req_receiving.............: avg=101.54µs min=25.56µs med=47.53µs max=82.7ms   p(90)=98.84µs p(95)=215.07µs p(99.9)=6.67ms 
     http_req_sending...............: avg=48.09µs  min=4.57µs  med=8.92µs  max=147.29ms p(90)=17.05µs p(95)=110.02µs p(99.9)=4.95ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.52ms  min=1ms     med=9.83ms  max=191.61ms p(90)=15.72ms p(95)=18.42ms  p(99.9)=30.89ms
     http_reqs......................: 550989  4586.275473/s
     iteration_duration.............: avg=10.88ms  min=1.5ms   med=10.15ms max=312.52ms p(90)=16.15ms p(95)=18.91ms  p(99.9)=31.6ms 
     iterations.....................: 550889  4585.443102/s
     success_rate...................: 100.00% ✓ 550889      ✗ 0     
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

     checks.........................: 100.00% ✓ 1617726     ✗ 0     
     data_received..................: 47 GB   393 MB/s
     data_sent......................: 648 MB  5.4 MB/s
     http_req_blocked...............: avg=2.67µs  min=822ns   med=2.12µs  max=4.02ms   p(90)=3.41µs  p(95)=4.09µs   p(99.9)=27.29µs
     http_req_connecting............: avg=176ns   min=0s      med=0s      max=3.98ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.91ms min=1.05ms  med=10.29ms max=285.05ms p(90)=15.9ms  p(95)=18.42ms  p(99.9)=30.76ms
       { expected_response:true }...: avg=10.91ms min=1.05ms  med=10.29ms max=285.05ms p(90)=15.9ms  p(95)=18.42ms  p(99.9)=30.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 539342
     http_req_receiving.............: avg=99.77µs min=25.26µs med=47.41µs max=48.95ms  p(90)=97.09µs p(95)=212.39µs p(99.9)=6.59ms 
     http_req_sending...............: avg=41.81µs min=4.55µs  med=8.44µs  max=23.88ms  p(90)=15.88µs p(95)=106.48µs p(99.9)=4.37ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.77ms min=1ms     med=10.18ms max=267.15ms p(90)=15.69ms p(95)=18.16ms  p(99.9)=30.36ms
     http_reqs......................: 539342  4489.215904/s
     iteration_duration.............: avg=11.11ms min=1.5ms   med=10.49ms max=310.82ms p(90)=16.1ms  p(95)=18.63ms  p(99.9)=31.03ms
     iterations.....................: 539242  4488.383554/s
     success_rate...................: 100.00% ✓ 539242      ✗ 0     
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

     checks.........................: 100.00% ✓ 1505922     ✗ 0     
     data_received..................: 44 GB   365 MB/s
     data_sent......................: 603 MB  5.0 MB/s
     http_req_blocked...............: avg=3µs     min=841ns    med=2.05µs  max=8.29ms   p(90)=3.19µs  p(95)=3.76µs   p(99.9)=28.34µs
     http_req_connecting............: avg=582ns   min=0s       med=0s      max=8.23ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.75ms min=755.74µs med=11.55ms max=266.43ms p(90)=16.83ms p(95)=18.68ms  p(99.9)=28.41ms
       { expected_response:true }...: avg=11.75ms min=755.74µs med=11.55ms max=266.43ms p(90)=16.83ms p(95)=18.68ms  p(99.9)=28.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 502074
     http_req_receiving.............: avg=82.33µs min=23.92µs  med=47.19µs max=188.72ms p(90)=89.78µs p(95)=203.37µs p(99.9)=3.83ms 
     http_req_sending...............: avg=38.38µs min=4.59µs   med=8.73µs  max=127.64ms p(90)=14.93µs p(95)=108.51µs p(99.9)=2.94ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.63ms min=704.32µs med=11.44ms max=265.31ms p(90)=16.68ms p(95)=18.51ms  p(99.9)=28.08ms
     http_reqs......................: 502074  4180.080186/s
     iteration_duration.............: avg=11.94ms min=1.31ms   med=11.73ms max=288.57ms p(90)=17.02ms p(95)=18.89ms  p(99.9)=28.64ms
     iterations.....................: 501974  4179.247624/s
     success_rate...................: 100.00% ✓ 501974      ✗ 0     
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

     checks.........................: 100.00% ✓ 1093224     ✗ 0     
     data_received..................: 32 GB   265 MB/s
     data_sent......................: 438 MB  3.6 MB/s
     http_req_blocked...............: avg=3.39µs  min=1.01µs  med=2.78µs  max=3.73ms   p(90)=4.23µs  p(95)=4.96µs   p(99.9)=38.74µs
     http_req_connecting............: avg=276ns   min=0s      med=0s      max=3.69ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.25ms min=1.41ms  med=16.17ms max=311.96ms p(90)=21.93ms p(95)=23.52ms  p(99.9)=31.45ms
       { expected_response:true }...: avg=16.25ms min=1.41ms  med=16.17ms max=311.96ms p(90)=21.93ms p(95)=23.52ms  p(99.9)=31.45ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 364508
     http_req_receiving.............: avg=79.85µs min=25.97µs med=53.99µs max=42.61ms  p(90)=99.8µs  p(95)=206.15µs p(99.9)=1.58ms 
     http_req_sending...............: avg=39.56µs min=4.89µs  med=10.91µs max=232.51ms p(90)=18.6µs  p(95)=117.62µs p(99.9)=1.64ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.13ms min=1.34ms  med=16.05ms max=311.73ms p(90)=21.81ms p(95)=23.39ms  p(99.9)=31.23ms
     http_reqs......................: 364508  3032.752416/s
     iteration_duration.............: avg=16.45ms min=3.08ms  med=16.37ms max=322.9ms  p(90)=22.14ms p(95)=23.72ms  p(99.9)=31.67ms
     iterations.....................: 364408  3031.920403/s
     success_rate...................: 100.00% ✓ 364408      ✗ 0     
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

     checks.........................: 100.00% ✓ 676797      ✗ 0     
     data_received..................: 20 GB   164 MB/s
     data_sent......................: 271 MB  2.3 MB/s
     http_req_blocked...............: avg=4.16µs  min=881ns   med=2.31µs  max=8.58ms   p(90)=4.48µs   p(95)=5.55µs   p(99.9)=40.22µs
     http_req_connecting............: avg=1.3µs   min=0s      med=0s      max=8.53ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.35ms min=1.85ms  med=25.86ms max=291.91ms p(90)=34.34ms  p(95)=37.08ms  p(99.9)=51.13ms
       { expected_response:true }...: avg=26.35ms min=1.85ms  med=25.86ms max=291.91ms p(90)=34.34ms  p(95)=37.08ms  p(99.9)=51.13ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 225699
     http_req_receiving.............: avg=82.65µs min=27.95µs med=55.37µs max=12.48ms  p(90)=118.67µs p(95)=190.74µs p(99.9)=1.53ms 
     http_req_sending...............: avg=32.99µs min=4.77µs  med=9.52µs  max=107.16ms p(90)=21.96µs  p(95)=103.95µs p(99.9)=1.64ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.23ms min=1.79ms  med=25.75ms max=291.29ms p(90)=34.21ms  p(95)=36.95ms  p(99.9)=50.94ms
     http_reqs......................: 225699  1876.77359/s
     iteration_duration.............: avg=26.58ms min=6.61ms  med=26.08ms max=321.24ms p(90)=34.56ms  p(95)=37.29ms  p(99.9)=51.45ms
     iterations.....................: 225599  1875.942052/s
     success_rate...................: 100.00% ✓ 225599      ✗ 0     
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

     checks.........................: 100.00% ✓ 550173      ✗ 0     
     data_received..................: 16 GB   133 MB/s
     data_sent......................: 221 MB  1.8 MB/s
     http_req_blocked...............: avg=4.08µs  min=1.11µs med=3.27µs  max=3.63ms   p(90)=5.11µs   p(95)=5.91µs   p(99.9)=38.09µs 
     http_req_connecting............: avg=486ns   min=0s     med=0s      max=3.59ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.46ms min=2ms    med=31.52ms max=286.91ms p(90)=45.94ms  p(95)=50.63ms  p(99.9)=76.58ms 
       { expected_response:true }...: avg=32.46ms min=2ms    med=31.52ms max=286.91ms p(90)=45.94ms  p(95)=50.63ms  p(99.9)=76.58ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 183491
     http_req_receiving.............: avg=76.88µs min=26.1µs med=63.69µs max=117.61ms p(90)=103.59µs p(95)=121.77µs p(99.9)=941.27µs
     http_req_sending...............: avg=25.28µs min=5.02µs med=13.33µs max=123.5ms  p(90)=20.65µs  p(95)=24.81µs  p(99.9)=830.69µs
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.35ms min=1.94ms med=31.42ms max=286.33ms p(90)=45.83ms  p(95)=50.52ms  p(99.9)=76.3ms  
     http_reqs......................: 183491  1525.637383/s
     iteration_duration.............: avg=32.7ms  min=5.32ms med=31.75ms max=310.33ms p(90)=46.16ms  p(95)=50.85ms  p(99.9)=77.25ms 
     iterations.....................: 183391  1524.805932/s
     success_rate...................: 100.00% ✓ 183391      ✗ 0     
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

     checks.........................: 100.00% ✓ 536427      ✗ 0     
     data_received..................: 16 GB   130 MB/s
     data_sent......................: 215 MB  1.8 MB/s
     http_req_blocked...............: avg=2.97µs  min=942ns   med=2.12µs  max=3.82ms   p(90)=3.59µs  p(95)=4.29µs   p(99.9)=32.8µs  
     http_req_connecting............: avg=539ns   min=0s      med=0s      max=3.78ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.33ms min=2.06ms  med=32.46ms max=281.53ms p(90)=48.15ms p(95)=53.14ms  p(99.9)=76.37ms 
       { expected_response:true }...: avg=33.33ms min=2.06ms  med=32.46ms max=281.53ms p(90)=48.15ms p(95)=53.14ms  p(99.9)=76.37ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 178909
     http_req_receiving.............: avg=68.8µs  min=25.76µs med=58.06µs max=100.52ms p(90)=92.96µs p(95)=107.52µs p(99.9)=661.47µs
     http_req_sending...............: avg=23.03µs min=4.73µs  med=10.07µs max=170.72ms p(90)=16.27µs p(95)=19.85µs  p(99.9)=735.36µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.24ms min=1.94ms  med=32.37ms max=281.4ms  p(90)=48.06ms p(95)=53.06ms  p(99.9)=76ms    
     http_reqs......................: 178909  1487.533392/s
     iteration_duration.............: avg=33.55ms min=4.41ms  med=32.66ms max=295.45ms p(90)=48.34ms p(95)=53.33ms  p(99.9)=76.71ms 
     iterations.....................: 178809  1486.701945/s
     success_rate...................: 100.00% ✓ 178809      ✗ 0     
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

     checks.........................: 100.00% ✓ 194130     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   646 kB/s
     http_req_blocked...............: avg=4.57µs  min=1.23µs  med=2.92µs  max=3.62ms   p(90)=4.32µs   p(95)=4.92µs   p(99.9)=51.05µs 
     http_req_connecting............: avg=1.41µs  min=0s      med=0s      max=3.58ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.36ms min=3.88ms  med=90.51ms max=334.02ms p(90)=116.86ms p(95)=128.63ms p(99.9)=227.41ms
       { expected_response:true }...: avg=92.36ms min=3.88ms  med=90.51ms max=334.02ms p(90)=116.86ms p(95)=128.63ms p(99.9)=227.41ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64810
     http_req_receiving.............: avg=80.83µs min=28.56µs med=69.77µs max=157.91ms p(90)=102.14µs p(95)=113.85µs p(99.9)=574.47µs
     http_req_sending...............: avg=26.07µs min=5.21µs  med=13.65µs max=160.99ms p(90)=19.33µs  p(95)=21.31µs  p(99.9)=568.16µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.25ms min=3.76ms  med=90.41ms max=315.21ms p(90)=116.75ms p(95)=128.49ms p(99.9)=226.9ms 
     http_reqs......................: 64810   537.665673/s
     iteration_duration.............: avg=92.73ms min=29.48ms med=90.75ms max=339.36ms p(90)=117.09ms p(95)=128.88ms p(99.9)=229.08ms
     iterations.....................: 64710   536.83607/s
     success_rate...................: 100.00% ✓ 64710      ✗ 0    
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

     checks.........................: 100.00% ✓ 175869     ✗ 0    
     data_received..................: 5.1 GB  43 MB/s
     data_sent......................: 71 MB   585 kB/s
     http_req_blocked...............: avg=5.2µs    min=1.06µs  med=2.45µs   max=9.54ms   p(90)=3.83µs   p(95)=4.35µs   p(99.9)=56.22µs 
     http_req_connecting............: avg=2.25µs   min=0s      med=0s       max=7ms      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=101.95ms min=4.39ms  med=99.97ms  max=312.19ms p(90)=137.85ms p(95)=148.61ms p(99.9)=192.97ms
       { expected_response:true }...: avg=101.95ms min=4.39ms  med=99.97ms  max=312.19ms p(90)=137.85ms p(95)=148.61ms p(99.9)=192.97ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 58723
     http_req_receiving.............: avg=74.15µs  min=28.22µs med=66.48µs  max=64.92ms  p(90)=97.16µs  p(95)=109.95µs p(99.9)=473.76µs
     http_req_sending...............: avg=17.94µs  min=4.98µs  med=12.57µs  max=31.08ms  p(90)=18.22µs  p(95)=19.94µs  p(99.9)=522.12µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=101.86ms min=4.31ms  med=99.88ms  max=310.68ms p(90)=137.75ms p(95)=148.53ms p(99.9)=192.66ms
     http_reqs......................: 58723   487.018108/s
     iteration_duration.............: avg=102.36ms min=25ms    med=100.24ms max=323.95ms p(90)=138.1ms  p(95)=148.89ms p(99.9)=194.93ms
     iterations.....................: 58623   486.18876/s
     success_rate...................: 100.00% ✓ 58623      ✗ 0    
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

     checks.........................: 100.00% ✓ 156327     ✗ 0    
     data_received..................: 4.6 GB  38 MB/s
     data_sent......................: 63 MB   520 kB/s
     http_req_blocked...............: avg=4.82µs   min=1.07µs  med=3.04µs   max=3.47ms   p(90)=4.46µs   p(95)=4.99µs   p(99.9)=61.79µs 
     http_req_connecting............: avg=1.63µs   min=0s      med=0s       max=3.43ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=114.7ms  min=5.22ms  med=112.39ms max=325.85ms p(90)=150.14ms p(95)=162.3ms  p(99.9)=207.64ms
       { expected_response:true }...: avg=114.7ms  min=5.22ms  med=112.39ms max=325.85ms p(90)=150.14ms p(95)=162.3ms  p(99.9)=207.64ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 52209
     http_req_receiving.............: avg=79.04µs  min=28.39µs med=75.7µs   max=58.07ms  p(90)=104.57µs p(95)=116.46µs p(99.9)=486.5µs 
     http_req_sending...............: avg=21.38µs  min=4.68µs  med=15.02µs  max=46.97ms  p(90)=19.91µs  p(95)=21.67µs  p(99.9)=501.2µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=114.6ms  min=5.1ms   med=112.29ms max=325.26ms p(90)=150.03ms p(95)=162.18ms p(99.9)=207.36ms
     http_reqs......................: 52209   432.692635/s
     iteration_duration.............: avg=115.16ms min=23.85ms med=112.68ms max=334.36ms p(90)=150.4ms  p(95)=162.59ms p(99.9)=208.87ms
     iterations.....................: 52109   431.863865/s
     success_rate...................: 100.00% ✓ 52109      ✗ 0    
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

     checks.........................: 100.00% ✓ 100557     ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   334 kB/s
     http_req_blocked...............: avg=6.63µs   min=1.29µs  med=3.41µs   max=3.99ms   p(90)=4.8µs    p(95)=5.4µs    p(99.9)=1.28ms  
     http_req_connecting............: avg=2.95µs   min=0s      med=0s       max=3.95ms   p(90)=0s       p(95)=0s       p(99.9)=1.26ms  
     http_req_duration..............: avg=178.29ms min=7.4ms   med=175.73ms max=406.29ms p(90)=190.8ms  p(95)=196.16ms p(99.9)=269.82ms
       { expected_response:true }...: avg=178.29ms min=7.4ms   med=175.73ms max=406.29ms p(90)=190.8ms  p(95)=196.16ms p(99.9)=269.82ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33619
     http_req_receiving.............: avg=97.96µs  min=34.33µs med=87.25µs  max=132.67ms p(90)=116.25µs p(95)=127.21µs p(99.9)=544.42µs
     http_req_sending...............: avg=29.34µs  min=6.09µs  med=17.32µs  max=132.83ms p(90)=21.7µs   p(95)=23.47µs  p(99.9)=558.42µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=178.17ms min=7.32ms  med=175.62ms max=405.89ms p(90)=190.67ms p(95)=196.05ms p(99.9)=269.43ms
     http_reqs......................: 33619   277.912943/s
     iteration_duration.............: avg=179.09ms min=45.5ms  med=176.11ms max=416.68ms p(90)=191.07ms p(95)=196.45ms p(99.9)=273.56ms
     iterations.....................: 33519   277.086289/s
     success_rate...................: 100.00% ✓ 33519      ✗ 0    
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

     checks.........................: 100.00% ✓ 96183      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   319 kB/s
     http_req_blocked...............: avg=6.25µs   min=1.11µs  med=3.13µs   max=4.16ms   p(90)=4.43µs   p(95)=4.98µs   p(99.9)=1.31ms  
     http_req_connecting............: avg=2.92µs   min=0s      med=0s       max=4.12ms   p(90)=0s       p(95)=0s       p(99.9)=1.27ms  
     http_req_duration..............: avg=186.43ms min=5.87ms  med=170.49ms max=776.37ms p(90)=215.76ms p(95)=253.11ms p(99.9)=716.21ms
       { expected_response:true }...: avg=186.43ms min=5.87ms  med=170.49ms max=776.37ms p(90)=215.76ms p(95)=253.11ms p(99.9)=716.21ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32161
     http_req_receiving.............: avg=90.51µs  min=30.7µs  med=87.02µs  max=16.89ms  p(90)=115.81µs p(95)=126.71µs p(99.9)=732.76µs
     http_req_sending...............: avg=28.76µs  min=5.4µs   med=16.43µs  max=73.44ms  p(90)=20.29µs  p(95)=21.89µs  p(99.9)=582.95µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=186.31ms min=5.75ms  med=170.38ms max=776.27ms p(90)=215.63ms p(95)=253.01ms p(99.9)=716.12ms
     http_reqs......................: 32161   265.773797/s
     iteration_duration.............: avg=187.26ms min=44.47ms med=170.83ms max=776.6ms  p(90)=216.22ms p(95)=253.88ms p(99.9)=716.45ms
     iterations.....................: 32061   264.947411/s
     success_rate...................: 100.00% ✓ 32061      ✗ 0    
     vus............................: 3       min=3        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

