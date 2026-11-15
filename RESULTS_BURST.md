## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-fed-net-11 | 16.8.0-p.12 | 4,795 | 4,820 | 4,784 | 0.3% | 418 MB | 89.2 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.12 | 4,777 | 4,788 | 4,774 | 0.1% | 428 MB | 91.8 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.12 | 4,617 | 4,625 | 4,610 | 0.1% | 160 MB | 35.6 KB |  |
| fusion-net-11 | 16.7.5 | 4,608 | 4,620 | 4,603 | 0.2% | 426 MB | 94.7 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.12 | 4,513 | 4,527 | 4,498 | 0.2% | 151 MB | 34.3 KB |  |
| fusion-aot-11 | 16.7.5 | 4,497 | 4,534 | 4,431 | 1.1% | 165 MB | 37.6 KB |  |
| fusion-fed-net-11 | 16.7.5 | 4,465 | 4,508 | 4,365 | 1.3% | 403 MB | 92.4 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 4,407 | 4,410 | 4,399 | 0.1% | 162 MB | 37.7 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,127 | 4,178 | 4,039 | 1.5% | 2,291 MB | 568.4 KB |  |
| hive-router | v0.3.10 | 2,634 | 2,648 | 2,621 | 0.4% | 168 MB | 65.5 KB |  |
| caliban | 3.2.0 | 1,448 | 1,450 | 1,446 | 0.1% | 10,750 MB | 7,602.0 KB |  |
| cosmo | 0.365.2 | 1,340 | 1,341 | 1,337 | 0.1% | 629 MB | 480.5 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 505 | 506 | 501 | 0.5% | 3,172 MB | 6,432.4 KB |  |
| hive-gateway | 2.15.6 | 246 | 247 | 244 | 0.6% | 3,812 MB | 15,867.5 KB |  |
| apollo-gateway | 2.14.4 | 240 | 241 | 239 | 0.3% | 2,481 MB | 10,587.6 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (9545 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (7606 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (126463 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.12)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 873783      ✗ 0     
     data_received..................: 26 GB   420 MB/s
     data_sent......................: 351 MB  5.8 MB/s
     http_req_blocked...............: avg=71.44µs  min=792ns    med=2.16µs  max=139.6ms  p(90)=3.77µs   p(95)=4.91µs   p(99.9)=27.92ms 
     http_req_connecting............: avg=66.97µs  min=0s       med=0s      max=130.95ms p(90)=0s       p(95)=0s       p(99.9)=26.92ms 
     http_req_duration..............: avg=46.67ms  min=762.63µs med=39.33ms max=287.91ms p(90)=98.12ms  p(95)=121.3ms  p(99.9)=182.1ms 
       { expected_response:true }...: avg=46.67ms  min=762.63µs med=39.33ms max=287.91ms p(90)=98.12ms  p(95)=121.3ms  p(99.9)=182.1ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 292261
     http_req_receiving.............: avg=374.81µs min=23.33µs  med=52.56µs max=137.85ms p(90)=203.4µs  p(95)=354.93µs p(99.9)=51.25ms 
     http_req_sending...............: avg=163.16µs min=4.03µs   med=8.82µs  max=178.28ms p(90)=17.08µs  p(95)=113.86µs p(99.9)=29.95ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.14ms  min=707.09µs med=38.96ms max=287.66ms p(90)=96.77ms  p(95)=119.92ms p(99.9)=173.67ms
     http_reqs......................: 292261  4795.092932/s
     iteration_duration.............: avg=48.9ms   min=1.17ms   med=40.4ms  max=365.86ms p(90)=103.66ms p(95)=128.6ms  p(99.9)=206.06ms
     iterations.....................: 291261  4778.686046/s
     success_rate...................: 100.00% ✓ 291261      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 870306      ✗ 0     
     data_received..................: 26 GB   418 MB/s
     data_sent......................: 350 MB  5.7 MB/s
     http_req_blocked...............: avg=61.84µs  min=791ns    med=2.09µs  max=161.66ms p(90)=3.68µs   p(95)=4.8µs    p(99.9)=22.21ms 
     http_req_connecting............: avg=57.56µs  min=0s       med=0s      max=131.96ms p(90)=0s       p(95)=0s       p(99.9)=21.52ms 
     http_req_duration..............: avg=47.22ms  min=751.35µs med=39.73ms max=290.14ms p(90)=99.53ms  p(95)=124.7ms  p(99.9)=179.71ms
       { expected_response:true }...: avg=47.22ms  min=751.35µs med=39.73ms max=290.14ms p(90)=99.53ms  p(95)=124.7ms  p(99.9)=179.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 291102
     http_req_receiving.............: avg=321.81µs min=24.91µs  med=51.62µs max=116.53ms p(90)=207.6µs  p(95)=363.78µs p(99.9)=44.53ms 
     http_req_sending...............: avg=147.25µs min=3.89µs   med=8.6µs   max=214.08ms p(90)=16.39µs  p(95)=114.82µs p(99.9)=26.86ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.76ms  min=705.43µs med=39.42ms max=289.64ms p(90)=98.42ms  p(95)=123.57ms p(99.9)=173.96ms
     http_reqs......................: 291102  4777.755607/s
     iteration_duration.............: avg=49.1ms   min=1.19ms   med=40.71ms max=412.53ms p(90)=103.74ms p(95)=130.35ms p(99.9)=205.83ms
     iterations.....................: 290102  4761.342956/s
     success_rate...................: 100.00% ✓ 290102      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 842325      ✗ 0     
     data_received..................: 25 GB   404 MB/s
     data_sent......................: 339 MB  5.5 MB/s
     http_req_blocked...............: avg=54.07µs  min=801ns    med=2.03µs  max=121.11ms p(90)=3.67µs   p(95)=4.79µs   p(99.9)=17.57ms 
     http_req_connecting............: avg=50.79µs  min=0s       med=0s      max=120.94ms p(90)=0s       p(95)=0s       p(99.9)=17.1ms  
     http_req_duration..............: avg=49.27ms  min=820.88µs med=41.16ms max=301.71ms p(90)=105.97ms p(95)=131.51ms p(99.9)=186.82ms
       { expected_response:true }...: avg=49.27ms  min=820.88µs med=41.16ms max=301.71ms p(90)=105.97ms p(95)=131.51ms p(99.9)=186.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 281775
     http_req_receiving.............: avg=308.07µs min=25.24µs  med=50µs    max=193.26ms p(90)=214.06µs p(95)=378.24µs p(99.9)=42.72ms 
     http_req_sending...............: avg=132.65µs min=4.1µs    med=8.41µs  max=187.75ms p(90)=16.92µs  p(95)=122.52µs p(99.9)=23.4ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.83ms  min=778.68µs med=40.87ms max=301.47ms p(90)=104.88ms p(95)=130.25ms p(99.9)=183.11ms
     http_reqs......................: 281775  4617.150652/s
     iteration_duration.............: avg=50.73ms  min=1.34ms   med=41.98ms max=320.4ms  p(90)=108.88ms p(95)=135.37ms p(99.9)=210.51ms
     iterations.....................: 280775  4600.764704/s
     success_rate...................: 100.00% ✓ 280775      ✗ 0     
     vus............................: 58      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 839649      ✗ 0     
     data_received..................: 25 GB   403 MB/s
     data_sent......................: 338 MB  5.5 MB/s
     http_req_blocked...............: avg=71.76µs  min=862ns    med=2.61µs  max=136.38ms p(90)=4.18µs   p(95)=5.38µs   p(99.9)=27.57ms 
     http_req_connecting............: avg=67.38µs  min=0s       med=0s      max=136.15ms p(90)=0s       p(95)=0s       p(99.9)=26.88ms 
     http_req_duration..............: avg=49.08ms  min=777.87µs med=41.09ms max=259.94ms p(90)=104.09ms p(95)=128.63ms p(99.9)=184.18ms
       { expected_response:true }...: avg=49.08ms  min=777.87µs med=41.09ms max=259.94ms p(90)=104.09ms p(95)=128.63ms p(99.9)=184.18ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280883
     http_req_receiving.............: avg=396.84µs min=24.79µs  med=53.92µs max=132.84ms p(90)=219.05µs p(95)=376.13µs p(99.9)=60.91ms 
     http_req_sending...............: avg=159.36µs min=4.02µs   med=9.29µs  max=231.91ms p(90)=17.77µs  p(95)=121.6µs  p(99.9)=28.79ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.52ms  min=725.09µs med=40.75ms max=259.84ms p(90)=102.74ms p(95)=126.98ms p(99.9)=176.81ms
     http_reqs......................: 280883  4608.197219/s
     iteration_duration.............: avg=50.87ms  min=1.15ms   med=41.96ms max=402.88ms p(90)=108.25ms p(95)=135.08ms p(99.9)=208.76ms
     iterations.....................: 279883  4591.79111/s
     success_rate...................: 100.00% ✓ 279883      ✗ 0     
     vus............................: 55      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 822972      ✗ 0     
     data_received..................: 24 GB   395 MB/s
     data_sent......................: 331 MB  5.4 MB/s
     http_req_blocked...............: avg=61.46µs  min=952ns    med=2.63µs  max=127.61ms p(90)=4.25µs   p(95)=5.41µs   p(99.9)=21.82ms
     http_req_connecting............: avg=57.44µs  min=0s       med=0s      max=127.51ms p(90)=0s       p(95)=0s       p(99.9)=21.48ms
     http_req_duration..............: avg=50.28ms  min=804.24µs med=41.4ms  max=318.6ms  p(90)=109.23ms p(95)=136.6ms  p(99.9)=192.6ms
       { expected_response:true }...: avg=50.28ms  min=804.24µs med=41.4ms  max=318.6ms  p(90)=109.23ms p(95)=136.6ms  p(99.9)=192.6ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 275324
     http_req_receiving.............: avg=325.19µs min=25.22µs  med=52.57µs max=144.87ms p(90)=229.13µs p(95)=403.96µs p(99.9)=41.96ms
     http_req_sending...............: avg=143.54µs min=4.06µs   med=9.23µs  max=236.13ms p(90)=18.33µs  p(95)=131.15µs p(99.9)=26.34ms
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=49.81ms  min=764.23µs med=41.11ms max=290.1ms  p(90)=108.14ms p(95)=135.21ms p(99.9)=188.2ms
     http_reqs......................: 275324  4513.312627/s
     iteration_duration.............: avg=51.92ms  min=1.23ms   med=42.28ms max=329.85ms p(90)=112.59ms p(95)=140.92ms p(99.9)=212.5ms
     iterations.....................: 274324  4496.919895/s
     success_rate...................: 100.00% ✓ 274324      ✗ 0     
     vus............................: 57      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 820500      ✗ 0     
     data_received..................: 24 GB   394 MB/s
     data_sent......................: 330 MB  5.4 MB/s
     http_req_blocked...............: avg=54.83µs  min=832ns    med=2.28µs  max=128.79ms p(90)=3.9µs    p(95)=5.03µs   p(99.9)=18.67ms 
     http_req_connecting............: avg=51.39µs  min=0s       med=0s      max=115.92ms p(90)=0s       p(95)=0s       p(99.9)=18.58ms 
     http_req_duration..............: avg=50.69ms  min=840.84µs med=42.57ms max=304.34ms p(90)=107.93ms p(95)=133.38ms p(99.9)=187.77ms
       { expected_response:true }...: avg=50.69ms  min=840.84µs med=42.57ms max=304.34ms p(90)=107.93ms p(95)=133.38ms p(99.9)=187.77ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 274500
     http_req_receiving.............: avg=325.7µs  min=24.36µs  med=51.58µs max=101.18ms p(90)=226.02µs p(95)=391.78µs p(99.9)=47.97ms 
     http_req_sending...............: avg=132.62µs min=4.03µs   med=8.77µs  max=190.69ms p(90)=17.59µs  p(95)=123.97µs p(99.9)=23.8ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.23ms  min=785.24µs med=42.27ms max=303.74ms p(90)=106.9ms  p(95)=132.17ms p(99.9)=182.02ms
     http_reqs......................: 274500  4497.300577/s
     iteration_duration.............: avg=52.09ms  min=1.35ms   med=43.47ms max=335.42ms p(90)=110.79ms p(95)=137.35ms p(99.9)=205.54ms
     iterations.....................: 273500  4480.916968/s
     success_rate...................: 100.00% ✓ 273500      ✗ 0     
     vus............................: 59      min=0         max=497 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 816081      ✗ 0     
     data_received..................: 24 GB   391 MB/s
     data_sent......................: 328 MB  5.4 MB/s
     http_req_blocked...............: avg=59.11µs  min=791ns    med=2.24µs  max=127.32ms p(90)=3.89µs   p(95)=5.03µs   p(99.9)=20.29ms 
     http_req_connecting............: avg=55.72µs  min=0s       med=0s      max=125.22ms p(90)=0s       p(95)=0s       p(99.9)=19.04ms 
     http_req_duration..............: avg=50.85ms  min=918.84µs med=42.4ms  max=266.3ms  p(90)=107.62ms p(95)=133.45ms p(99.9)=193.62ms
       { expected_response:true }...: avg=50.85ms  min=918.84µs med=42.4ms  max=266.3ms  p(90)=107.62ms p(95)=133.45ms p(99.9)=193.62ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 273027
     http_req_receiving.............: avg=319.93µs min=26.55µs  med=52.53µs max=130.56ms p(90)=217.84µs p(95)=384.48µs p(99.9)=45.86ms 
     http_req_sending...............: avg=141.83µs min=4.02µs   med=8.97µs  max=152.42ms p(90)=17.69µs  p(95)=121.61µs p(99.9)=25.19ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.39ms  min=856.28µs med=42.11ms max=252.7ms  p(90)=106.67ms p(95)=132.31ms p(99.9)=187.67ms
     http_reqs......................: 273027  4465.259666/s
     iteration_duration.............: avg=52.37ms  min=1.42ms   med=43.13ms max=355.56ms p(90)=110.53ms p(95)=138.28ms p(99.9)=215.95ms
     iterations.....................: 272027  4448.905021/s
     success_rate...................: 100.00% ✓ 272027      ✗ 0     
     vus............................: 63      min=0         max=497 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 806115      ✗ 0     
     data_received..................: 24 GB   386 MB/s
     data_sent......................: 324 MB  5.3 MB/s
     http_req_blocked...............: avg=46.37µs  min=802ns    med=2.1µs   max=116.88ms p(90)=3.86µs   p(95)=5.11µs   p(99.9)=13.43ms 
     http_req_connecting............: avg=43.14µs  min=0s       med=0s      max=116.83ms p(90)=0s       p(95)=0s       p(99.9)=13.13ms 
     http_req_duration..............: avg=51.95ms  min=990.95µs med=43.87ms max=340.12ms p(90)=110.89ms p(95)=137.1ms  p(99.9)=194.14ms
       { expected_response:true }...: avg=51.95ms  min=990.95µs med=43.87ms max=340.12ms p(90)=110.89ms p(95)=137.1ms  p(99.9)=194.14ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 269705
     http_req_receiving.............: avg=298.84µs min=25.65µs  med=49.83µs max=220.22ms p(90)=222.69µs p(95)=381.15µs p(99.9)=41.16ms 
     http_req_sending...............: avg=126.52µs min=4.39µs   med=8.47µs  max=83.26ms  p(90)=18.5µs   p(95)=125.96µs p(99.9)=22.78ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.52ms  min=925.25µs med=43.62ms max=305.06ms p(90)=110.13ms p(95)=136.11ms p(99.9)=184.62ms
     http_reqs......................: 269705  4407.574726/s
     iteration_duration.............: avg=53.01ms  min=1.53ms   med=44.54ms max=350.1ms  p(90)=112.96ms p(95)=139.24ms p(99.9)=208.86ms
     iterations.....................: 268705  4391.23252/s
     success_rate...................: 100.00% ✓ 268705      ✗ 0     
     vus............................: 65      min=0         max=496 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 752187      ✗ 0     
     data_received..................: 22 GB   361 MB/s
     data_sent......................: 302 MB  5.0 MB/s
     http_req_blocked...............: avg=40.56µs  min=782ns   med=2.1µs   max=98.87ms  p(90)=3.7µs    p(95)=4.82µs   p(99.9)=6.26ms  
     http_req_connecting............: avg=37.3µs   min=0s      med=0s      max=98.64ms  p(90)=0s       p(95)=0s       p(99.9)=6.15ms  
     http_req_duration..............: avg=55.54ms  min=725.2µs med=46.24ms max=277.46ms p(90)=116.44ms p(95)=144.11ms p(99.9)=218.75ms
       { expected_response:true }...: avg=55.54ms  min=725.2µs med=46.24ms max=277.46ms p(90)=116.44ms p(95)=144.11ms p(99.9)=218.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 251729
     http_req_receiving.............: avg=247.57µs min=21.45µs med=50.87µs max=101.47ms p(90)=210.83µs p(95)=370.71µs p(99.9)=34.04ms 
     http_req_sending...............: avg=115.23µs min=4.23µs  med=8.83µs  max=174.22ms p(90)=17.88µs  p(95)=122.58µs p(99.9)=20.83ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=55.17ms  min=678.3µs med=45.98ms max=277.37ms p(90)=115.71ms p(95)=143.22ms p(99.9)=216.24ms
     http_reqs......................: 251729  4127.230695/s
     iteration_duration.............: avg=56.82ms  min=1.2ms   med=47.3ms  max=304.07ms p(90)=118.68ms p(95)=147.47ms p(99.9)=228.97ms
     iterations.....................: 250729  4110.835163/s
     success_rate...................: 100.00% ✓ 250729      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 482823      ✗ 0     
     data_received..................: 14 GB   230 MB/s
     data_sent......................: 195 MB  3.2 MB/s
     http_req_blocked...............: avg=19.86µs  min=1.04µs  med=2.93µs  max=59.4ms   p(90)=4.67µs   p(95)=6.01µs   p(99.9)=1.79ms  
     http_req_connecting............: avg=16.08µs  min=0s      med=0s      max=59.35ms  p(90)=0s       p(95)=0s       p(99.9)=1.62ms  
     http_req_duration..............: avg=87.78ms  min=1.18ms  med=82.37ms max=315.08ms p(90)=172.18ms p(95)=186.76ms p(99.9)=235.92ms
       { expected_response:true }...: avg=87.78ms  min=1.18ms  med=82.37ms max=315.08ms p(90)=172.18ms p(95)=186.76ms p(99.9)=235.92ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 161941
     http_req_receiving.............: avg=160.96µs min=28.44µs med=59.38µs max=71.03ms  p(90)=193.45µs p(95)=384.76µs p(99.9)=15.88ms 
     http_req_sending...............: avg=74.74µs  min=4.49µs  med=11.35µs max=175.93ms p(90)=21.32µs  p(95)=135.65µs p(99.9)=9.58ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=87.54ms  min=1.14ms  med=82.18ms max=314.46ms p(90)=171.84ms p(95)=186.39ms p(99.9)=234.99ms
     http_reqs......................: 161941  2634.581464/s
     iteration_duration.............: avg=88.58ms  min=3.21ms  med=83.33ms max=350.67ms p(90)=172.64ms p(95)=187.23ms p(99.9)=236.62ms
     iterations.....................: 160941  2618.31269/s
     success_rate...................: 100.00% ✓ 160941      ✗ 0     
     vus............................: 78      min=0         max=493 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 268233      ✗ 0    
     data_received..................: 7.9 GB  127 MB/s
     data_sent......................: 109 MB  1.7 MB/s
     http_req_blocked...............: avg=7.8µs    min=1.21µs med=3.47µs   max=22.35ms  p(90)=5.61µs   p(95)=6.79µs   p(99.9)=525.25µs
     http_req_connecting............: avg=3.6µs    min=0s     med=0s       max=22.28ms  p(90)=0s       p(95)=0s       p(99.9)=451.07µs
     http_req_duration..............: avg=157.66ms min=1.98ms med=135.77ms max=939.9ms  p(90)=326.22ms p(95)=382.71ms p(99.9)=645.44ms
       { expected_response:true }...: avg=157.66ms min=1.98ms med=135.77ms max=939.9ms  p(90)=326.22ms p(95)=382.71ms p(99.9)=645.44ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 90411
     http_req_receiving.............: avg=90.34µs  min=28.8µs med=67.03µs  max=24.32ms  p(90)=109.46µs p(95)=134.52µs p(99.9)=2.69ms  
     http_req_sending...............: avg=43.46µs  min=5.3µs  med=13.97µs  max=118.4ms  p(90)=22.11µs  p(95)=27.49µs  p(99.9)=5.14ms  
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=157.53ms min=1.93ms med=135.63ms max=939.84ms p(90)=326.11ms p(95)=382.58ms p(99.9)=645.33ms
     http_reqs......................: 90411   1448.394678/s
     iteration_duration.............: avg=159.7ms  min=6.04ms med=138.04ms max=940.14ms p(90)=327.66ms p(95)=383.92ms p(99.9)=647.1ms 
     iterations.....................: 89411   1432.374562/s
     success_rate...................: 100.00% ✓ 89411       ✗ 0    
     vus............................: 75      min=0         max=493
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 248061      ✗ 0    
     data_received..................: 7.3 GB  117 MB/s
     data_sent......................: 101 MB  1.6 MB/s
     http_req_blocked...............: avg=5.11µs   min=952ns   med=2.24µs   max=15.56ms  p(90)=3.89µs   p(95)=4.83µs   p(99.9)=341.56µs
     http_req_connecting............: avg=2.21µs   min=0s      med=0s       max=15.51ms  p(90)=0s       p(95)=0s       p(99.9)=294.3µs 
     http_req_duration..............: avg=170.41ms min=2.02ms  med=168.6ms  max=466.21ms p(90)=323.83ms p(95)=347.06ms p(99.9)=422.2ms 
       { expected_response:true }...: avg=170.41ms min=2.02ms  med=168.6ms  max=466.21ms p(90)=323.83ms p(95)=347.06ms p(99.9)=422.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 83687
     http_req_receiving.............: avg=74.53µs  min=25.87µs med=58.76µs  max=118.55ms p(90)=95.31µs  p(95)=109.95µs p(99.9)=1.29ms  
     http_req_sending...............: avg=27.61µs  min=4.55µs  med=10.06µs  max=94.89ms  p(90)=16.32µs  p(95)=19.82µs  p(99.9)=3.17ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=170.3ms  min=1.96ms  med=168.48ms max=466.12ms p(90)=323.72ms p(95)=346.95ms p(99.9)=422.13ms
     http_reqs......................: 83687   1340.440247/s
     iteration_duration.............: avg=172.7ms  min=4.45ms  med=171.43ms max=466.43ms p(90)=324.69ms p(95)=347.68ms p(99.9)=422.46ms
     iterations.....................: 82687   1324.422942/s
     success_rate...................: 100.00% ✓ 82687       ✗ 0    
     vus............................: 77      min=0         max=493
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 94698      ✗ 0    
     data_received..................: 2.9 GB  44 MB/s
     data_sent......................: 39 MB   606 kB/s
     http_req_blocked...............: avg=6.95µs   min=972ns   med=2.79µs   max=9.45ms   p(90)=4.47µs   p(95)=5.43µs   p(99.9)=613.85µs
     http_req_connecting............: avg=3.21µs   min=0s      med=0s       max=9.38ms   p(90)=0s       p(95)=0s       p(99.9)=561.53µs
     http_req_duration..............: avg=440.8ms  min=3.66ms  med=408.58ms max=2s       p(90)=872.14ms p(95)=939.12ms p(99.9)=1.42s   
       { expected_response:true }...: avg=440.8ms  min=3.66ms  med=408.58ms max=2s       p(90)=872.14ms p(95)=939.12ms p(99.9)=1.42s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 32566
     http_req_receiving.............: avg=85.01µs  min=30.81µs med=72.74µs  max=114.9ms  p(90)=110.53µs p(95)=124.89µs p(99.9)=926.61µs
     http_req_sending...............: avg=32.78µs  min=5.03µs  med=13.4µs   max=129.61ms p(90)=19.79µs  p(95)=22.42µs  p(99.9)=2.67ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=440.68ms min=3.57ms  med=408.49ms max=2s       p(90)=872.09ms p(95)=939ms    p(99.9)=1.42s   
     http_reqs......................: 32566   505.030091/s
     iteration_duration.............: avg=455ms    min=25.48ms med=426.26ms max=2s       p(90)=876.04ms p(95)=942ms    p(99.9)=1.42s   
     iterations.....................: 31566   489.522197/s
     success_rate...................: 100.00% ✓ 31566      ✗ 0    
     vus............................: 80      min=0        max=498
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 46698      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 20 MB   296 kB/s
     http_req_blocked...............: avg=13.8µs   min=1.18µs  med=3.3µs    max=9.96ms p(90)=5.02µs   p(95)=6.65µs   p(99.9)=2.08ms  
     http_req_connecting............: avg=8.9µs    min=0s      med=0s       max=9.87ms p(90)=0s       p(95)=0s       p(99.9)=2.06ms  
     http_req_duration..............: avg=878.75ms min=5.68ms  med=803.88ms max=4.98s  p(90)=1.75s    p(95)=1.98s    p(99.9)=3.98s   
       { expected_response:true }...: avg=878.75ms min=5.68ms  med=803.88ms max=4.98s  p(90)=1.75s    p(95)=1.98s    p(99.9)=3.98s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16566
     http_req_receiving.............: avg=94.36µs  min=30.98µs med=90.29µs  max=6.06ms p(90)=127.21µs p(95)=142.94µs p(99.9)=548.32µs
     http_req_sending...............: avg=31.55µs  min=5.44µs  med=16.92µs  max=27.4ms p(90)=21.86µs  p(95)=25.3µs   p(99.9)=5.46ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s     p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=878.63ms min=5.6ms   med=803.77ms max=4.98s  p(90)=1.75s    p(95)=1.98s    p(99.9)=3.98s   
     http_reqs......................: 16566   246.319598/s
     iteration_duration.............: avg=935.22ms min=63.69ms med=870.22ms max=4.99s  p(90)=1.78s    p(95)=1.99s    p(99.9)=4.02s   
     iterations.....................: 15566   231.450613/s
     success_rate...................: 100.00% ✓ 15566      ✗ 0    
     vus............................: 69      min=0        max=499
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

     checks.........................: 100.00% ✓ 46500     ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   289 kB/s
     http_req_blocked...............: avg=23.31µs  min=1.1µs   med=3.2µs    max=20.34ms  p(90)=4.86µs   p(95)=6.38µs  p(99.9)=5.91ms 
     http_req_connecting............: avg=17.87µs  min=0s      med=0s       max=20.27ms  p(90)=0s       p(95)=0s      p(99.9)=5.7ms  
     http_req_duration..............: avg=880.35ms min=7.57ms  med=800.46ms max=3.06s    p(90)=1.79s    p(95)=1.91s   p(99.9)=2.77s  
       { expected_response:true }...: avg=880.35ms min=7.57ms  med=800.46ms max=3.06s    p(90)=1.79s    p(95)=1.91s   p(99.9)=2.77s  
     http_req_failed................: 0.00%   ✓ 0         ✗ 16500
     http_req_receiving.............: avg=195.78µs min=32.12µs med=86.44µs  max=100.86ms p(90)=123.65µs p(95)=139.2µs p(99.9)=56.74ms
     http_req_sending...............: avg=29.25µs  min=5.25µs  med=16.15µs  max=7.46ms   p(90)=21.04µs  p(95)=24.61µs p(99.9)=3.52ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=880.12ms min=7.48ms  med=800.36ms max=3.06s    p(90)=1.79s    p(95)=1.91s   p(99.9)=2.77s  
     http_reqs......................: 16500   240.87146/s
     iteration_duration.............: avg=937.13ms min=14.78ms med=859.42ms max=3.07s    p(90)=1.81s    p(95)=1.92s   p(99.9)=2.78s  
     iterations.....................: 15500   226.27319/s
     success_rate...................: 100.00% ✓ 15500     ✗ 0    
     vus............................: 78      min=0       max=500
     vus_max........................: 500     min=500     max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

