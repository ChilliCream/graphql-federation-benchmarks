## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.17 | 4,922 | 4,932 | 4,801 | 1.1% | 399 MB | 83.0 KB |  |
| fusion-net-11 | 16.7.7 | 4,827 | 4,878 | 4,761 | 1.2% | 400 MB | 84.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.17 | 4,752 | 4,758 | 4,746 | 0.1% | 153 MB | 32.9 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 4,747 | 4,752 | 4,737 | 0.1% | 156 MB | 33.7 KB |  |
| fusion-aot-11 | 16.7.7 | 4,736 | 4,745 | 4,730 | 0.1% | 141 MB | 30.4 KB |  |
| fusion-fed-net-11 | 16.7.7 | 4,693 | 4,705 | 4,692 | 0.1% | 418 MB | 91.2 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.17 | 4,640 | 4,689 | 4,624 | 0.5% | 417 MB | 92.0 KB |  |
| feddi-gateway | 2026-11-03-0517 | 4,634 | 4,647 | 4,538 | 1.0% | 2,319 MB | 512.5 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.17 | 4,610 | 4,675 | 4,592 | 0.7% | 149 MB | 33.1 KB |  |
| hive-router | v0.3.17 | 4,098 | 4,114 | 4,071 | 0.4% | 197 MB | 49.2 KB |  |
| hive-router-nightly | v0.3.19-nightly.9815b25d | 3,874 | 3,888 | 3,864 | 0.3% | 197 MB | 52.1 KB |  |
| caliban | 3.2.1 | 1,515 | 1,516 | 1,513 | 0.1% | 11,577 MB | 7,825.1 KB |  |
| cosmo | 0.373.0 | 1,318 | 1,324 | 1,317 | 0.2% | 548 MB | 426.0 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 552 | 557 | 545 | 0.8% | 3,013 MB | 5,588.5 KB |  |
| hive-gateway | 2.15.10 | 268 | 272 | 267 | 0.8% | 3,813 MB | 14,570.3 KB |  |
| apollo-gateway | 2.14.4 | 239 | 240 | 237 | 0.5% | 2,449 MB | 10,494.8 KB |  |
| apollo-router | v2.19.1 | — | — | — | — | — | — | non-compatible response (5137 across 5/5 runs) |
| apollo-router-nightly | v3.0.0-preview.0-nightly.a909a280 | — | — | — | — | — | — | non-compatible response (2699 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (4653 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (140271 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 896442      ✗ 0     
     data_received..................: 26 GB   431 MB/s
     data_sent......................: 360 MB  5.9 MB/s
     http_req_blocked...............: avg=67.95µs  min=791ns    med=2.1µs   max=148.95ms p(90)=3.72µs   p(95)=4.83µs   p(99.9)=25.85ms 
     http_req_connecting............: avg=64.39µs  min=0s       med=0s      max=148.91ms p(90)=0s       p(95)=0s       p(99.9)=25.6ms  
     http_req_duration..............: avg=45.62ms  min=739.55µs med=38.67ms max=300.77ms p(90)=95.76ms  p(95)=118.52ms p(99.9)=169.84ms
       { expected_response:true }...: avg=45.62ms  min=739.55µs med=38.67ms max=300.77ms p(90)=95.76ms  p(95)=118.52ms p(99.9)=169.84ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 299814
     http_req_receiving.............: avg=338.46µs min=24.05µs  med=51.57µs max=127.37ms p(90)=200.08µs p(95)=346.91µs p(99.9)=46ms    
     http_req_sending...............: avg=152.68µs min=4.01µs   med=8.43µs  max=215.31ms p(90)=16µs     p(95)=111.09µs p(99.9)=27.89ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=45.13ms  min=692.46µs med=38.33ms max=300.19ms p(90)=94.55ms  p(95)=117.24ms p(99.9)=165.79ms
     http_reqs......................: 299814  4922.246543/s
     iteration_duration.............: avg=47.67ms  min=1.25ms   med=39.58ms max=328.38ms p(90)=100.49ms p(95)=125.64ms p(99.9)=209.75ms
     iterations.....................: 298814  4905.828876/s
     success_rate...................: 100.00% ✓ 298814      ✗ 0     
     vus............................: 52      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 879099      ✗ 0     
     data_received..................: 26 GB   422 MB/s
     data_sent......................: 353 MB  5.8 MB/s
     http_req_blocked...............: avg=72.19µs  min=811ns    med=2.38µs  max=149.53ms p(90)=3.89µs   p(95)=4.98µs   p(99.9)=26.77ms 
     http_req_connecting............: avg=67.74µs  min=0s       med=0s      max=149.45ms p(90)=0s       p(95)=0s       p(99.9)=26ms    
     http_req_duration..............: avg=46.07ms  min=726.57µs med=38.72ms max=321.08ms p(90)=96.28ms  p(95)=118.97ms p(99.9)=176.98ms
       { expected_response:true }...: avg=46.07ms  min=726.57µs med=38.72ms max=321.08ms p(90)=96.28ms  p(95)=118.97ms p(99.9)=176.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 294033
     http_req_receiving.............: avg=356.2µs  min=24.01µs  med=52.17µs max=218.65ms p(90)=204.46µs p(95)=352.87µs p(99.9)=47.71ms 
     http_req_sending...............: avg=162.03µs min=3.9µs    med=8.97µs  max=264.26ms p(90)=16.71µs  p(95)=114.13µs p(99.9)=30.8ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=45.55ms  min=685.68µs med=38.35ms max=280.6ms  p(90)=95.03ms  p(95)=117.53ms p(99.9)=172.74ms
     http_reqs......................: 294033  4827.654021/s
     iteration_duration.............: avg=48.61ms  min=1.12ms   med=39.95ms max=337.22ms p(90)=102.52ms p(95)=128.39ms p(99.9)=216.13ms
     iterations.....................: 293033  4811.235272/s
     success_rate...................: 100.00% ✓ 293033      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 866739      ✗ 0     
     data_received..................: 25 GB   416 MB/s
     data_sent......................: 348 MB  5.7 MB/s
     http_req_blocked...............: avg=62.72µs  min=771ns    med=2.04µs  max=125.29ms p(90)=3.62µs   p(95)=4.74µs   p(99.9)=23.26ms 
     http_req_connecting............: avg=59.09µs  min=0s       med=0s      max=125.11ms p(90)=0s       p(95)=0s       p(99.9)=22.33ms 
     http_req_duration..............: avg=47.48ms  min=803.14µs med=39.5ms  max=285.01ms p(90)=100.77ms p(95)=126.07ms p(99.9)=182.88ms
       { expected_response:true }...: avg=47.48ms  min=803.14µs med=39.5ms  max=285.01ms p(90)=100.77ms p(95)=126.07ms p(99.9)=182.88ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 289913
     http_req_receiving.............: avg=318.13µs min=20.74µs  med=51.34µs max=127.47ms p(90)=210.91µs p(95)=368.73µs p(99.9)=42.49ms 
     http_req_sending...............: avg=142.92µs min=4.07µs   med=8.44µs  max=115.86ms p(90)=16.14µs  p(95)=116.94µs p(99.9)=25.55ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.01ms  min=743.22µs med=39.18ms max=284.59ms p(90)=99.72ms  p(95)=124.95ms p(99.9)=178.65ms
     http_reqs......................: 289913  4752.5164/s
     iteration_duration.............: avg=49.3ms   min=1.39ms   med=40.51ms max=341.4ms  p(90)=105.19ms p(95)=132.29ms p(99.9)=205.96ms
     iterations.....................: 288913  4736.123495/s
     success_rate...................: 100.00% ✓ 288913      ✗ 0     
     vus............................: 57      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 865164      ✗ 0     
     data_received..................: 25 GB   415 MB/s
     data_sent......................: 348 MB  5.7 MB/s
     http_req_blocked...............: avg=62.31µs  min=801ns    med=2.12µs  max=171.15ms p(90)=3.78µs   p(95)=4.96µs   p(99.9)=22.77ms 
     http_req_connecting............: avg=59.03µs  min=0s       med=0s      max=170.89ms p(90)=0s       p(95)=0s       p(99.9)=22.5ms  
     http_req_duration..............: avg=47.75ms  min=783.67µs med=40.14ms max=329.64ms p(90)=101.75ms p(95)=126.21ms p(99.9)=179.35ms
       { expected_response:true }...: avg=47.75ms  min=783.67µs med=40.14ms max=329.64ms p(90)=101.75ms p(95)=126.21ms p(99.9)=179.35ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 289388
     http_req_receiving.............: avg=329.9µs  min=25.86µs  med=50.87µs max=121.11ms p(90)=205.76µs p(95)=362.29µs p(99.9)=44.62ms 
     http_req_sending...............: avg=146.87µs min=4.11µs   med=8.62µs  max=126.92ms p(90)=16.88µs  p(95)=117.57µs p(99.9)=26.35ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.27ms  min=741.71µs med=39.8ms  max=323.85ms p(90)=100.49ms p(95)=124.94ms p(99.9)=175.82ms
     http_reqs......................: 289388  4747.284104/s
     iteration_duration.............: avg=49.39ms  min=1.29ms   med=40.93ms max=338.47ms p(90)=105.65ms p(95)=131.64ms p(99.9)=200.8ms 
     iterations.....................: 288388  4730.87954/s
     success_rate...................: 100.00% ✓ 288388      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 862935      ✗ 0     
     data_received..................: 25 GB   414 MB/s
     data_sent......................: 347 MB  5.7 MB/s
     http_req_blocked...............: avg=58.02µs  min=761ns    med=2.05µs  max=145.94ms p(90)=3.61µs   p(95)=4.71µs   p(99.9)=20.73ms 
     http_req_connecting............: avg=54.9µs   min=0s       med=0s      max=113.77ms p(90)=0s       p(95)=0s       p(99.9)=20.63ms 
     http_req_duration..............: avg=48.01ms  min=773.73µs med=40.37ms max=320.5ms  p(90)=102.81ms p(95)=127.62ms p(99.9)=185.55ms
       { expected_response:true }...: avg=48.01ms  min=773.73µs med=40.37ms max=320.5ms  p(90)=102.81ms p(95)=127.62ms p(99.9)=185.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288645
     http_req_receiving.............: avg=339.13µs min=24.75µs  med=50.81µs max=156.73ms p(90)=211.15µs p(95)=369.24µs p(99.9)=49.46ms 
     http_req_sending...............: avg=139.81µs min=3.99µs   med=8.54µs  max=211.17ms p(90)=16.32µs  p(95)=117.56µs p(99.9)=25.12ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.53ms  min=730.81µs med=40.08ms max=320.01ms p(90)=101.81ms p(95)=126.46ms p(99.9)=175.64ms
     http_reqs......................: 288645  4736.105161/s
     iteration_duration.............: avg=49.52ms  min=1.28ms   med=41.17ms max=382.89ms p(90)=105.85ms p(95)=131.85ms p(99.9)=216.99ms
     iterations.....................: 287645  4719.697098/s
     success_rate...................: 100.00% ✓ 287645      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 855081      ✗ 0     
     data_received..................: 25 GB   411 MB/s
     data_sent......................: 344 MB  5.6 MB/s
     http_req_blocked...............: avg=72.77µs  min=872ns    med=2.71µs  max=151.77ms p(90)=4.27µs   p(95)=5.45µs   p(99.9)=28.93ms 
     http_req_connecting............: avg=68.63µs  min=0s       med=0s      max=134.25ms p(90)=0s       p(95)=0s       p(99.9)=28.43ms 
     http_req_duration..............: avg=47.91ms  min=739.26µs med=40.39ms max=322.79ms p(90)=100.87ms p(95)=125.25ms p(99.9)=182.02ms
       { expected_response:true }...: avg=47.91ms  min=739.26µs med=40.39ms max=322.79ms p(90)=100.87ms p(95)=125.25ms p(99.9)=182.02ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 286027
     http_req_receiving.............: avg=360.99µs min=21.18µs  med=54.78µs max=208.81ms p(90)=215.16µs p(95)=367.51µs p(99.9)=47.99ms 
     http_req_sending...............: avg=167.5µs  min=4.02µs   med=9.34µs  max=263.57ms p(90)=17.19µs  p(95)=119.4µs  p(99.9)=32ms    
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.38ms  min=703.13µs med=40.04ms max=322.31ms p(90)=99.51ms  p(95)=123.84ms p(99.9)=178.18ms
     http_reqs......................: 286027  4693.556129/s
     iteration_duration.............: avg=49.98ms  min=1.15ms   med=41.36ms max=331.78ms p(90)=106.46ms p(95)=132.39ms p(99.9)=206.21ms
     iterations.....................: 285027  4677.146642/s
     success_rate...................: 100.00% ✓ 285027      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 845433      ✗ 0     
     data_received..................: 25 GB   406 MB/s
     data_sent......................: 340 MB  5.6 MB/s
     http_req_blocked...............: avg=75.54µs  min=842ns    med=2.59µs  max=154.64ms p(90)=4.26µs   p(95)=5.45µs   p(99.9)=31.52ms 
     http_req_connecting............: avg=70.92µs  min=0s       med=0s      max=154.61ms p(90)=0s       p(95)=0s       p(99.9)=30.12ms 
     http_req_duration..............: avg=48.34ms  min=760.72µs med=40.84ms max=334.69ms p(90)=101.33ms p(95)=126.25ms p(99.9)=187.35ms
       { expected_response:true }...: avg=48.34ms  min=760.72µs med=40.84ms max=334.69ms p(90)=101.33ms p(95)=126.25ms p(99.9)=187.35ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 282811
     http_req_receiving.............: avg=359.67µs min=26.21µs  med=55.04µs max=131.27ms p(90)=212.15µs p(95)=367.89µs p(99.9)=48.08ms 
     http_req_sending...............: avg=169.63µs min=4µs      med=9.44µs  max=332.99ms p(90)=17.48µs  p(95)=119.54µs p(99.9)=30.17ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.81ms  min=712.85µs med=40.47ms max=301.59ms p(90)=99.95ms  p(95)=124.93ms p(99.9)=181.21ms
     http_reqs......................: 282811  4640.308387/s
     iteration_duration.............: avg=50.54ms  min=955.59µs med=41.78ms max=416.98ms p(90)=107.36ms p(95)=133.91ms p(99.9)=212.07ms
     iterations.....................: 281811  4623.90058/s
     success_rate...................: 100.00% ✓ 281811      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 843000      ✗ 0     
     data_received..................: 25 GB   405 MB/s
     data_sent......................: 339 MB  5.6 MB/s
     http_req_blocked...............: avg=51.6µs   min=761ns    med=2.02µs  max=104.18ms p(90)=3.62µs   p(95)=4.68µs   p(99.9)=15.31ms 
     http_req_connecting............: avg=48.24µs  min=0s       med=0s      max=99.75ms  p(90)=0s       p(95)=0s       p(99.9)=15.17ms 
     http_req_duration..............: avg=48.92ms  min=636.98µs med=40.92ms max=309.66ms p(90)=104.07ms p(95)=129.61ms p(99.9)=199.03ms
       { expected_response:true }...: avg=48.92ms  min=636.98µs med=40.92ms max=309.66ms p(90)=104.07ms p(95)=129.61ms p(99.9)=199.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 282000
     http_req_receiving.............: avg=305.86µs min=24.64µs  med=51.1µs  max=194.45ms p(90)=208.24µs p(95)=373.08µs p(99.9)=40.44ms 
     http_req_sending...............: avg=128.72µs min=4.01µs   med=8.46µs  max=113.21ms p(90)=16.53µs  p(95)=119.93µs p(99.9)=22.17ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.48ms  min=601.44µs med=40.63ms max=296ms    p(90)=103.19ms p(95)=128.67ms p(99.9)=193.46ms
     http_reqs......................: 282000  4634.408773/s
     iteration_duration.............: avg=50.69ms  min=1.16ms   med=41.99ms max=352.93ms p(90)=108.19ms p(95)=134.77ms p(99.9)=217.41ms
     iterations.....................: 281000  4617.9747/s
     success_rate...................: 100.00% ✓ 281000      ✗ 0     
     vus............................: 95      min=50        max=500 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 840315      ✗ 0     
     data_received..................: 25 GB   404 MB/s
     data_sent......................: 338 MB  5.5 MB/s
     http_req_blocked...............: avg=64.1µs   min=921ns    med=2.54µs  max=115.45ms p(90)=4.09µs   p(95)=5.19µs   p(99.9)=22.94ms 
     http_req_connecting............: avg=60.13µs  min=0s       med=0s      max=115.32ms p(90)=0s       p(95)=0s       p(99.9)=21.57ms 
     http_req_duration..............: avg=49.2ms   min=787.26µs med=41.03ms max=275.48ms p(90)=106.01ms p(95)=132.32ms p(99.9)=192.75ms
       { expected_response:true }...: avg=49.2ms   min=787.26µs med=41.03ms max=275.48ms p(90)=106.01ms p(95)=132.32ms p(99.9)=192.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 281105
     http_req_receiving.............: avg=351.41µs min=25.54µs  med=53.04µs max=126.57ms p(90)=221.12µs p(95)=390.42µs p(99.9)=52.35ms 
     http_req_sending...............: avg=149.89µs min=4.04µs   med=8.97µs  max=129.91ms p(90)=17.11µs  p(95)=124.41µs p(99.9)=26.24ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.69ms  min=738.46µs med=40.7ms  max=266.53ms p(90)=104.99ms p(95)=131.09ms p(99.9)=181.09ms
     http_reqs......................: 281105  4610.912231/s
     iteration_duration.............: avg=50.85ms  min=1.33ms   med=41.81ms max=333.13ms p(90)=109.66ms p(95)=137.79ms p(99.9)=217.71ms
     iterations.....................: 280105  4594.50942/s
     success_rate...................: 100.00% ✓ 280105      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 748020      ✗ 0     
     data_received..................: 22 GB   358 MB/s
     data_sent......................: 301 MB  4.9 MB/s
     http_req_blocked...............: avg=45.01µs  min=781ns    med=2.22µs  max=105.72ms p(90)=4.04µs   p(95)=5.3µs    p(99.9)=10ms    
     http_req_connecting............: avg=41.57µs  min=0s       med=0s      max=103.9ms  p(90)=0s       p(95)=0s       p(99.9)=9.39ms  
     http_req_duration..............: avg=55.88ms  min=879.24µs med=47.07ms max=306.89ms p(90)=118.57ms p(95)=147.45ms p(99.9)=213.81ms
       { expected_response:true }...: avg=55.88ms  min=879.24µs med=47.07ms max=306.89ms p(90)=118.57ms p(95)=147.45ms p(99.9)=213.81ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 250340
     http_req_receiving.............: avg=272.16µs min=25.6µs   med=53.03µs max=184.63ms p(90)=212.66µs p(95)=382.27µs p(99.9)=39.77ms 
     http_req_sending...............: avg=121.38µs min=4.12µs   med=9.1µs   max=171.91ms p(90)=19.25µs  p(95)=128.8µs  p(99.9)=21.86ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=55.48ms  min=837.7µs  med=46.78ms max=297.64ms p(90)=117.81ms p(95)=146.49ms p(99.9)=208.85ms
     http_reqs......................: 250340  4098.020145/s
     iteration_duration.............: avg=57.13ms  min=1.36ms   med=48.09ms max=355.29ms p(90)=120.91ms p(95)=150.65ms p(99.9)=230.07ms
     iterations.....................: 249340  4081.650327/s
     success_rate...................: 100.00% ✓ 249340      ✗ 0     
     vus............................: 61      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.19-nightly.9815b25d)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 707193      ✗ 0     
     data_received..................: 21 GB   339 MB/s
     data_sent......................: 284 MB  4.7 MB/s
     http_req_blocked...............: avg=51.22µs  min=1µs      med=2.8µs   max=103.73ms p(90)=4.56µs   p(95)=5.86µs   p(99.9)=11.93ms 
     http_req_connecting............: avg=47.11µs  min=0s       med=0s      max=103.63ms p(90)=0s       p(95)=0s       p(99.9)=11.24ms 
     http_req_duration..............: avg=58.92ms  min=899.83µs med=49.65ms max=323.01ms p(90)=125.13ms p(95)=156.97ms p(99.9)=219.4ms 
       { expected_response:true }...: avg=58.92ms  min=899.83µs med=49.65ms max=323.01ms p(90)=125.13ms p(95)=156.97ms p(99.9)=219.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 236731
     http_req_receiving.............: avg=293.95µs min=24.17µs  med=56.34µs max=88.74ms  p(90)=232.76µs p(95)=413.52µs p(99.9)=42.24ms 
     http_req_sending...............: avg=134.37µs min=4.04µs   med=9.72µs  max=280.76ms p(90)=19.71µs  p(95)=137.86µs p(99.9)=23.77ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=58.49ms  min=834.41µs med=49.35ms max=289.42ms p(90)=124.26ms p(95)=155.92ms p(99.9)=215.66ms
     http_reqs......................: 236731  3874.216173/s
     iteration_duration.............: avg=60.44ms  min=1.69ms   med=50.7ms  max=333.5ms  p(90)=128.55ms p(95)=161.1ms  p(99.9)=239.79ms
     iterations.....................: 235731  3857.850694/s
     success_rate...................: 100.00% ✓ 235731      ✗ 0     
     vus............................: 62      min=0         max=497 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 280080      ✗ 0    
     data_received..................: 8.3 GB  133 MB/s
     data_sent......................: 113 MB  1.8 MB/s
     http_req_blocked...............: avg=5.91µs   min=972ns   med=2.68µs   max=14.12ms  p(90)=4.84µs   p(95)=5.87µs   p(99.9)=391.07µs
     http_req_connecting............: avg=2.51µs   min=0s      med=0s       max=14.04ms  p(90)=0s       p(95)=0s       p(99.9)=316.81µs
     http_req_duration..............: avg=151.1ms  min=1.9ms   med=125.56ms max=854.5ms  p(90)=315.04ms p(95)=373.17ms p(99.9)=601.72ms
       { expected_response:true }...: avg=151.1ms  min=1.9ms   med=125.56ms max=854.5ms  p(90)=315.04ms p(95)=373.17ms p(99.9)=601.72ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 94360
     http_req_receiving.............: avg=77.06µs  min=27.16µs med=59.79µs  max=67.78ms  p(90)=100.72µs p(95)=119.18µs p(99.9)=1.93ms  
     http_req_sending...............: avg=34.24µs  min=4.94µs  med=11.82µs  max=143.25ms p(90)=19.92µs  p(95)=24.17µs  p(99.9)=3.84ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=150.99ms min=1.85ms  med=125.44ms max=854.39ms p(90)=314.95ms p(95)=373.1ms  p(99.9)=601.64ms
     http_reqs......................: 94360   1515.247008/s
     iteration_duration.............: avg=152.96ms min=6.03ms  med=127.53ms max=854.74ms p(90)=316.3ms  p(95)=374.23ms p(99.9)=602.33ms
     iterations.....................: 93360   1499.188858/s
     success_rate...................: 100.00% ✓ 93360       ✗ 0    
     vus............................: 68      min=0         max=495
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.373.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 244071      ✗ 0    
     data_received..................: 7.2 GB  115 MB/s
     data_sent......................: 99 MB   1.6 MB/s
     http_req_blocked...............: avg=5.65µs   min=1.15µs  med=2.76µs   max=11.05ms  p(90)=4.38µs   p(95)=5.3µs    p(99.9)=264.71µs
     http_req_connecting............: avg=2.29µs   min=0s      med=0s       max=10.97ms  p(90)=0s       p(95)=0s       p(99.9)=193.43µs
     http_req_duration..............: avg=173.2ms  min=2.03ms  med=170.57ms max=472.34ms p(90)=328.54ms p(95)=351.63ms p(99.9)=413.26ms
       { expected_response:true }...: avg=173.2ms  min=2.03ms  med=170.57ms max=472.34ms p(90)=328.54ms p(95)=351.63ms p(99.9)=413.26ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 82357
     http_req_receiving.............: avg=81.85µs  min=26.72µs med=62.08µs  max=154.74ms p(90)=99.9µs   p(95)=116.61µs p(99.9)=1.53ms  
     http_req_sending...............: avg=35.99µs  min=5.01µs  med=11.71µs  max=195.83ms p(90)=17.71µs  p(95)=21.24µs  p(99.9)=3.84ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=173.08ms min=1.96ms  med=170.42ms max=472.27ms p(90)=328.43ms p(95)=351.54ms p(99.9)=413.19ms
     http_reqs......................: 82357   1318.76898/s
     iteration_duration.............: avg=175.55ms min=5.57ms  med=173.25ms max=472.52ms p(90)=329.31ms p(95)=352.23ms p(99.9)=413.61ms
     iterations.....................: 81357   1302.756146/s
     success_rate...................: 100.00% ✓ 81357       ✗ 0    
     vus............................: 77      min=0         max=493
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 103359     ✗ 0    
     data_received..................: 3.1 GB  48 MB/s
     data_sent......................: 43 MB   663 kB/s
     http_req_blocked...............: avg=8.23µs   min=931ns   med=2.65µs   max=15.95ms  p(90)=4.3µs    p(95)=5.22µs   p(99.9)=1.31ms  
     http_req_connecting............: avg=4.65µs   min=0s      med=0s       max=15.89ms  p(90)=0s       p(95)=0s       p(99.9)=1.29ms  
     http_req_duration..............: avg=404.54ms min=3.44ms  med=371.44ms max=1.68s    p(90)=808.48ms p(95)=885.23ms p(99.9)=1.26s   
       { expected_response:true }...: avg=404.54ms min=3.44ms  med=371.44ms max=1.68s    p(90)=808.48ms p(95)=885.23ms p(99.9)=1.26s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 35453
     http_req_receiving.............: avg=78.81µs  min=29.45µs med=66.44µs  max=86.79ms  p(90)=104.1µs  p(95)=118.29µs p(99.9)=913.42µs
     http_req_sending...............: avg=36.79µs  min=5.11µs  med=12.87µs  max=188.22ms p(90)=19.51µs  p(95)=21.92µs  p(99.9)=2.18ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=404.42ms min=3.36ms  med=371.38ms max=1.68s    p(90)=808.39ms p(95)=885.14ms p(99.9)=1.26s   
     http_reqs......................: 35453   552.315374/s
     iteration_duration.............: avg=416.49ms min=22.58ms med=385.31ms max=1.68s    p(90)=812.48ms p(95)=888.36ms p(99.9)=1.27s   
     iterations.....................: 34453   536.736569/s
     success_rate...................: 100.00% ✓ 34453      ✗ 0    
     vus............................: 65      min=0        max=497
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 51369      ✗ 0    
     data_received..................: 1.6 GB  24 MB/s
     data_sent......................: 22 MB   322 kB/s
     http_req_blocked...............: avg=20.28µs  min=1.09µs  med=3.27µs   max=13.43ms p(90)=5µs      p(95)=6.36µs   p(99.9)=5.62ms
     http_req_connecting............: avg=15.35µs  min=0s      med=0s       max=13.39ms p(90)=0s       p(95)=0s       p(99.9)=5.49ms
     http_req_duration..............: avg=800.13ms min=5.4ms   med=725.06ms max=3.85s   p(90)=1.6s     p(95)=1.84s    p(99.9)=3.19s 
       { expected_response:true }...: avg=800.13ms min=5.4ms   med=725.06ms max=3.85s   p(90)=1.6s     p(95)=1.84s    p(99.9)=3.19s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 18123
     http_req_receiving.............: avg=90.3µs   min=33.18µs med=85.64µs  max=4.66ms  p(90)=122.15µs p(95)=136.75µs p(99.9)=1.02ms
     http_req_sending...............: avg=34.33µs  min=5.47µs  med=16.08µs  max=64.14ms p(90)=21.15µs  p(95)=24.24µs  p(99.9)=2.83ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=800.01ms min=5.27ms  med=724.89ms max=3.85s   p(90)=1.6s     p(95)=1.84s    p(99.9)=3.19s 
     http_reqs......................: 18123   268.344716/s
     iteration_duration.............: avg=846.9ms  min=31.47ms med=775.71ms max=3.86s   p(90)=1.63s    p(95)=1.85s    p(99.9)=3.25s 
     iterations.....................: 17123   253.537857/s
     success_rate...................: 100.00% ✓ 17123      ✗ 0    
     vus............................: 73      min=0        max=499
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 46320      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   288 kB/s
     http_req_blocked...............: avg=14.21µs  min=1.08µs  med=3.07µs   max=9.4ms   p(90)=4.72µs   p(95)=6.05µs   p(99.9)=2.25ms
     http_req_connecting............: avg=9.57µs   min=0s      med=0s       max=9.34ms  p(90)=0s       p(95)=0s       p(99.9)=2.22ms
     http_req_duration..............: avg=883.5ms  min=7.63ms  med=798.2ms  max=2.94s   p(90)=1.8s     p(95)=1.92s    p(99.9)=2.74s 
       { expected_response:true }...: avg=883.5ms  min=7.63ms  med=798.2ms  max=2.94s   p(90)=1.8s     p(95)=1.92s    p(99.9)=2.74s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16440
     http_req_receiving.............: avg=93.06µs  min=31.52µs med=85.35µs  max=18.45ms p(90)=122.74µs p(95)=137.06µs p(99.9)=1.1ms 
     http_req_sending...............: avg=35.71µs  min=5.46µs  med=16.47µs  max=70.93ms p(90)=21.65µs  p(95)=25.31µs  p(99.9)=2.45ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=883.37ms min=7.55ms  med=798.05ms max=2.94s   p(90)=1.8s     p(95)=1.92s    p(99.9)=2.74s 
     http_reqs......................: 16440   239.626815/s
     iteration_duration.............: avg=940.7ms  min=64.35ms med=892.57ms max=2.94s   p(90)=1.82s    p(95)=1.93s    p(99.9)=2.79s 
     iterations.....................: 15440   225.050974/s
     success_rate...................: 100.00% ✓ 15440      ✗ 0    
     vus............................: 81      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

