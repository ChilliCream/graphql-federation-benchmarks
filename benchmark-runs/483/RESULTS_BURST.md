## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.6 | 4,856 | 4,878 | 4,755 | 1.0% | 407 MB | 85.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.16 | 4,812 | 4,818 | 4,802 | 0.1% | 421 MB | 89.6 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.16 | 4,806 | 4,810 | 4,661 | 1.6% | 194 MB | 41.3 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.16 | 4,794 | 4,801 | 4,778 | 0.2% | 424 MB | 90.6 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.16 | 4,750 | 4,766 | 4,700 | 0.5% | 164 MB | 35.4 KB |  |
| fusion-fed-net-11 | 16.7.6 | 4,737 | 4,747 | 4,726 | 0.2% | 425 MB | 92.0 KB |  |
| feddi-gateway | 2026-11-03-0517 | 4,644 | 4,653 | 4,546 | 1.0% | 2,293 MB | 505.6 KB |  |
| fusion-aot-11 | 16.7.6 | 4,589 | 4,675 | 4,583 | 0.8% | 155 MB | 34.7 KB |  |
| fusion-fed-aot-11 | 16.7.6 | 4,582 | 4,646 | 4,558 | 0.8% | 169 MB | 37.8 KB |  |
| caliban | 3.2.1 | 1,532 | 1,535 | 1,529 | 0.2% | 11,632 MB | 7,774.9 KB |  |
| cosmo | 0.372.0 | 1,332 | 1,345 | 1,325 | 0.6% | 684 MB | 525.7 KB |  |
| hive-gateway-router-runtime | 2.15.8 | 540 | 541 | 535 | 0.4% | 3,042 MB | 5,768.9 KB |  |
| hive-gateway | 2.15.8 | 271 | 272 | 268 | 0.6% | 3,618 MB | 13,671.6 KB |  |
| apollo-gateway | 2.14.4 | 240 | 240 | 237 | 0.5% | 2,465 MB | 10,515.9 KB |  |
| apollo-router | v2.19.1 | — | — | — | — | — | — | non-compatible response (10386 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (8323 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (156684 across 5/5 runs) |
| hive-router | — | — | — | — | — | — | — | benchmark run failed |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 884787      ✗ 0     
     data_received..................: 26 GB   425 MB/s
     data_sent......................: 356 MB  5.8 MB/s
     http_req_blocked...............: avg=67.56µs  min=802ns    med=2.04µs  max=164.33ms p(90)=3.55µs   p(95)=4.62µs   p(99.9)=24.61ms 
     http_req_connecting............: avg=63.97µs  min=0s       med=0s      max=164.27ms p(90)=0s       p(95)=0s       p(99.9)=24.23ms 
     http_req_duration..............: avg=46.04ms  min=722.93µs med=39.21ms max=252.62ms p(90)=95.54ms  p(95)=119.57ms p(99.9)=178.75ms
       { expected_response:true }...: avg=46.04ms  min=722.93µs med=39.21ms max=252.62ms p(90)=95.54ms  p(95)=119.57ms p(99.9)=178.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 295929
     http_req_receiving.............: avg=386.47µs min=25.85µs  med=52.24µs max=128.41ms p(90)=199.65µs p(95)=347.02µs p(99.9)=56.17ms 
     http_req_sending...............: avg=158.09µs min=4.2µs    med=8.69µs  max=195.55ms p(90)=15.94µs  p(95)=110.25µs p(99.9)=28.38ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=45.5ms   min=688.45µs med=38.85ms max=249ms    p(90)=94.3ms   p(95)=118.26ms p(99.9)=167.84ms
     http_reqs......................: 295929  4856.922809/s
     iteration_duration.............: avg=48.29ms  min=1.19ms   med=40.21ms max=332.2ms  p(90)=101.99ms p(95)=127.13ms p(99.9)=211.29ms
     iterations.....................: 294929  4840.510349/s
     success_rate...................: 100.00% ✓ 294929      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 876609      ✗ 0     
     data_received..................: 26 GB   421 MB/s
     data_sent......................: 352 MB  5.8 MB/s
     http_req_blocked...............: avg=68.48µs  min=801ns    med=2.15µs  max=179.17ms p(90)=3.76µs   p(95)=4.87µs   p(99.9)=25.47ms 
     http_req_connecting............: avg=64.69µs  min=0s       med=0s      max=178.99ms p(90)=0s       p(95)=0s       p(99.9)=24.8ms  
     http_req_duration..............: avg=46.45ms  min=755.41µs med=39.17ms max=315.19ms p(90)=97.09ms  p(95)=120.91ms p(99.9)=173.66ms
       { expected_response:true }...: avg=46.45ms  min=755.41µs med=39.17ms max=315.19ms p(90)=97.09ms  p(95)=120.91ms p(99.9)=173.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 293203
     http_req_receiving.............: avg=338.38µs min=25.58µs  med=53.17µs max=123.2ms  p(90)=203.37µs p(95)=350.78µs p(99.9)=45.9ms  
     http_req_sending...............: avg=160.2µs  min=4.05µs   med=8.79µs  max=124.95ms p(90)=16.38µs  p(95)=112.43µs p(99.9)=29.59ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=45.95ms  min=706.62µs med=38.81ms max=314.88ms p(90)=95.73ms  p(95)=119.71ms p(99.9)=169.61ms
     http_reqs......................: 293203  4812.337819/s
     iteration_duration.............: avg=48.75ms  min=1.26ms   med=40.36ms max=324.16ms p(90)=102.49ms p(95)=128.73ms p(99.9)=198.32ms
     iterations.....................: 292203  4795.924829/s
     success_rate...................: 100.00% ✓ 292203      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 875949      ✗ 0     
     data_received..................: 26 GB   421 MB/s
     data_sent......................: 352 MB  5.8 MB/s
     http_req_blocked...............: avg=59.95µs  min=772ns    med=1.99µs  max=122.74ms p(90)=3.58µs   p(95)=4.7µs    p(99.9)=20.56ms 
     http_req_connecting............: avg=56.22µs  min=0s       med=0s      max=111.53ms p(90)=0s       p(95)=0s       p(99.9)=20.19ms 
     http_req_duration..............: avg=47.14ms  min=776.72µs med=39.6ms  max=285.47ms p(90)=101.09ms p(95)=125.09ms p(99.9)=175.96ms
       { expected_response:true }...: avg=47.14ms  min=776.72µs med=39.6ms  max=285.47ms p(90)=101.09ms p(95)=125.09ms p(99.9)=175.96ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 292983
     http_req_receiving.............: avg=310.27µs min=25.34µs  med=50.36µs max=142.58ms p(90)=208.06µs p(95)=364.74µs p(99.9)=42.76ms 
     http_req_sending...............: avg=145.77µs min=3.88µs   med=8.31µs  max=237.44ms p(90)=15.95µs  p(95)=115.66µs p(99.9)=26.85ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.68ms  min=731.01µs med=39.3ms  max=281.49ms p(90)=99.98ms  p(95)=123.9ms  p(99.9)=172.88ms
     http_reqs......................: 292983  4806.843358/s
     iteration_duration.............: avg=48.78ms  min=1.38ms   med=40.54ms max=318.68ms p(90)=104.33ms p(95)=130.1ms  p(99.9)=202.91ms
     iterations.....................: 291983  4790.436798/s
     success_rate...................: 100.00% ✓ 291983      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 873306      ✗ 0     
     data_received..................: 26 GB   420 MB/s
     data_sent......................: 351 MB  5.8 MB/s
     http_req_blocked...............: avg=63.69µs  min=801ns    med=2.03µs  max=133.37ms p(90)=3.62µs   p(95)=4.69µs   p(99.9)=23.2ms  
     http_req_connecting............: avg=60.51µs  min=0s       med=0s      max=133.29ms p(90)=0s       p(95)=0s       p(99.9)=22.74ms 
     http_req_duration..............: avg=47.03ms  min=720.29µs med=39.23ms max=325.64ms p(90)=100.2ms  p(95)=124.65ms p(99.9)=177.02ms
       { expected_response:true }...: avg=47.03ms  min=720.29µs med=39.23ms max=325.64ms p(90)=100.2ms  p(95)=124.65ms p(99.9)=177.02ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 292102
     http_req_receiving.............: avg=316.09µs min=25.62µs  med=52.15µs max=222.65ms p(90)=205.27µs p(95)=357.54µs p(99.9)=43.77ms 
     http_req_sending...............: avg=151.15µs min=3.92µs   med=8.58µs  max=175.96ms p(90)=16.19µs  p(95)=113.69µs p(99.9)=27.52ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.56ms  min=684.99µs med=38.9ms  max=303.89ms p(90)=99.12ms  p(95)=123.43ms p(99.9)=172.92ms
     http_reqs......................: 292102  4794.42884/s
     iteration_duration.............: avg=48.94ms  min=1.12ms   med=40.24ms max=342.15ms p(90)=104.95ms p(95)=130.56ms p(99.9)=203ms   
     iterations.....................: 291102  4778.015297/s
     success_rate...................: 100.00% ✓ 291102      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 866070      ✗ 0     
     data_received..................: 25 GB   416 MB/s
     data_sent......................: 348 MB  5.7 MB/s
     http_req_blocked...............: avg=66.98µs  min=802ns    med=2.12µs  max=129.29ms p(90)=3.72µs   p(95)=4.88µs   p(99.9)=24.43ms 
     http_req_connecting............: avg=62.96µs  min=0s       med=0s      max=129.19ms p(90)=0s       p(95)=0s       p(99.9)=23.65ms 
     http_req_duration..............: avg=47.55ms  min=768.17µs med=39.97ms max=291.12ms p(90)=100.61ms p(95)=125.63ms p(99.9)=180.5ms 
       { expected_response:true }...: avg=47.55ms  min=768.17µs med=39.97ms max=291.12ms p(90)=100.61ms p(95)=125.63ms p(99.9)=180.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 289690
     http_req_receiving.............: avg=323.98µs min=22.64µs  med=52.07µs max=117.91ms p(90)=201.15µs p(95)=361.9µs  p(99.9)=44.83ms 
     http_req_sending...............: avg=148.29µs min=4.13µs   med=8.75µs  max=205.33ms p(90)=16.96µs  p(95)=116.92µs p(99.9)=26.8ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.07ms  min=729.6µs  med=39.66ms max=290.74ms p(90)=99.43ms  p(95)=124.5ms  p(99.9)=176.69ms
     http_reqs......................: 289690  4750.976063/s
     iteration_duration.............: avg=49.34ms  min=1.35ms   med=40.84ms max=339.04ms p(90)=105.25ms p(95)=131.56ms p(99.9)=204.16ms
     iterations.....................: 288690  4734.575855/s
     success_rate...................: 100.00% ✓ 288690      ✗ 0     
     vus............................: 57      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 862926      ✗ 0     
     data_received..................: 25 GB   415 MB/s
     data_sent......................: 347 MB  5.7 MB/s
     http_req_blocked...............: avg=66.97µs  min=822ns    med=2.1µs   max=162.57ms p(90)=3.73µs   p(95)=4.84µs   p(99.9)=23.25ms 
     http_req_connecting............: avg=62.86µs  min=0s       med=0s      max=162.48ms p(90)=0s       p(95)=0s       p(99.9)=22.3ms  
     http_req_duration..............: avg=47.5ms   min=743.84µs med=40ms    max=342.67ms p(90)=100.23ms p(95)=125.77ms p(99.9)=182.93ms
       { expected_response:true }...: avg=47.5ms   min=743.84µs med=40ms    max=342.67ms p(90)=100.23ms p(95)=125.77ms p(99.9)=182.93ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288642
     http_req_receiving.............: avg=373.82µs min=24.08µs  med=52.39µs max=253.65ms p(90)=210.46µs p(95)=366.09µs p(99.9)=54.14ms 
     http_req_sending...............: avg=147.87µs min=4.09µs   med=8.69µs  max=120.11ms p(90)=16.38µs  p(95)=115.15µs p(99.9)=26.97ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.98ms  min=708.04µs med=39.66ms max=316.93ms p(90)=99.04ms  p(95)=124.4ms  p(99.9)=176.29ms
     http_reqs......................: 288642  4737.36739/s
     iteration_duration.............: avg=49.52ms  min=1.18ms   med=40.97ms max=352.38ms p(90)=105.77ms p(95)=132.12ms p(99.9)=209.06ms
     iterations.....................: 287642  4720.954784/s
     success_rate...................: 100.00% ✓ 287642      ✗ 0     
     vus............................: 54      min=0         max=500 
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

     checks.........................: 100.00% ✓ 845118      ✗ 0     
     data_received..................: 25 GB   406 MB/s
     data_sent......................: 340 MB  5.6 MB/s
     http_req_blocked...............: avg=55.75µs  min=791ns    med=2.03µs  max=122.92ms p(90)=3.7µs    p(95)=4.77µs   p(99.9)=19.21ms 
     http_req_connecting............: avg=52.08µs  min=0s       med=0s      max=122.83ms p(90)=0s       p(95)=0s       p(99.9)=18.7ms  
     http_req_duration..............: avg=48.91ms  min=648.05µs med=41.12ms max=274.62ms p(90)=103.71ms p(95)=129.29ms p(99.9)=196.36ms
       { expected_response:true }...: avg=48.91ms  min=648.05µs med=41.12ms max=274.62ms p(90)=103.71ms p(95)=129.29ms p(99.9)=196.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 282706
     http_req_receiving.............: avg=301.21µs min=24.9µs   med=51.02µs max=98.13ms  p(90)=206.56µs p(95)=373.07µs p(99.9)=39.94ms 
     http_req_sending...............: avg=130.39µs min=3.97µs   med=8.62µs  max=155.57ms p(90)=16.52µs  p(95)=119.38µs p(99.9)=23.26ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.48ms  min=612.28µs med=40.83ms max=274.13ms p(90)=102.73ms p(95)=128.16ms p(99.9)=191.82ms
     http_reqs......................: 282706  4644.953655/s
     iteration_duration.............: avg=50.56ms  min=1.15ms   med=42.03ms max=344.41ms p(90)=107.35ms p(95)=134.21ms p(99.9)=217.24ms
     iterations.....................: 281706  4628.523322/s
     success_rate...................: 100.00% ✓ 281706      ✗ 0     
     vus............................: 49      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 836310      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=66.01µs  min=972ns    med=2.6µs   max=139.55ms p(90)=4.14µs   p(95)=5.28µs   p(99.9)=24.72ms 
     http_req_connecting............: avg=62.21µs  min=0s       med=0s      max=130.46ms p(90)=0s       p(95)=0s       p(99.9)=24.41ms 
     http_req_duration..............: avg=49.32ms  min=784.9µs  med=41.62ms max=294.51ms p(90)=105.08ms p(95)=131.05ms p(99.9)=188.75ms
       { expected_response:true }...: avg=49.32ms  min=784.9µs  med=41.62ms max=294.51ms p(90)=105.08ms p(95)=131.05ms p(99.9)=188.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 279770
     http_req_receiving.............: avg=345.82µs min=25.77µs  med=53.36µs max=135.82ms p(90)=222.94µs p(95)=388.57µs p(99.9)=43.94ms 
     http_req_sending...............: avg=152.15µs min=4.06µs   med=9.17µs  max=204.66ms p(90)=17.51µs  p(95)=125.21µs p(99.9)=26.97ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.82ms  min=742.31µs med=41.26ms max=265.63ms p(90)=103.86ms p(95)=129.71ms p(99.9)=184.74ms
     http_reqs......................: 279770  4589.113188/s
     iteration_duration.............: avg=51.1ms   min=1.22ms   med=42.32ms max=367.9ms  p(90)=109.16ms p(95)=137.44ms p(99.9)=217.9ms 
     iterations.....................: 278770  4572.710024/s
     success_rate...................: 100.00% ✓ 278770      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 835308      ✗ 0     
     data_received..................: 25 GB   401 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=65.85µs  min=962ns    med=2.56µs  max=123.49ms p(90)=4.19µs   p(95)=5.32µs   p(99.9)=23.38ms 
     http_req_connecting............: avg=62.37µs  min=0s       med=0s      max=123.4ms  p(90)=0s       p(95)=0s       p(99.9)=23.27ms 
     http_req_duration..............: avg=49.13ms  min=792.38µs med=40.88ms max=396.46ms p(90)=105.56ms p(95)=132.52ms p(99.9)=188.58ms
       { expected_response:true }...: avg=49.13ms  min=792.38µs med=40.88ms max=396.46ms p(90)=105.56ms p(95)=132.52ms p(99.9)=188.58ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 279436
     http_req_receiving.............: avg=347.66µs min=25.04µs  med=53.7µs  max=261.56ms p(90)=223.1µs  p(95)=392.2µs  p(99.9)=46.6ms  
     http_req_sending...............: avg=156.49µs min=4.01µs   med=9.02µs  max=176.36ms p(90)=17.75µs  p(95)=126.64µs p(99.9)=28.4ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.63ms  min=751.86µs med=40.56ms max=304.28ms p(90)=104.43ms p(95)=131.33ms p(99.9)=183.48ms
     http_reqs......................: 279436  4582.740983/s
     iteration_duration.............: avg=51.16ms  min=1.31ms   med=41.93ms max=396.68ms p(90)=109.62ms p(95)=138.74ms p(99.9)=224.99ms
     iterations.....................: 278436  4566.341016/s
     success_rate...................: 100.00% ✓ 278436      ✗ 0     
     vus............................: 56      min=0         max=498 
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

     checks.........................: 100.00% ✓ 283302      ✗ 0    
     data_received..................: 8.3 GB  134 MB/s
     data_sent......................: 115 MB  1.8 MB/s
     http_req_blocked...............: avg=6.21µs   min=941ns   med=2.69µs   max=15.67ms  p(90)=4.79µs   p(95)=5.88µs   p(99.9)=495.49µs
     http_req_connecting............: avg=2.83µs   min=0s      med=0s       max=15.6ms   p(90)=0s       p(95)=0s       p(99.9)=408.11µs
     http_req_duration..............: avg=149.36ms min=1.9ms   med=127.4ms  max=814.78ms p(90)=309.82ms p(95)=366.13ms p(99.9)=641.93ms
       { expected_response:true }...: avg=149.36ms min=1.9ms   med=127.4ms  max=814.78ms p(90)=309.82ms p(95)=366.13ms p(99.9)=641.93ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 95434
     http_req_receiving.............: avg=83.2µs   min=26.95µs med=61.37µs  max=110.9ms  p(90)=104.76µs p(95)=127.96µs p(99.9)=2.27ms  
     http_req_sending...............: avg=36.66µs  min=5.14µs  med=12.1µs   max=98.29ms  p(90)=20.45µs  p(95)=25.18µs  p(99.9)=4.31ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=149.24ms min=1.85ms  med=127.26ms max=814.66ms p(90)=309.64ms p(95)=366.03ms p(99.9)=641.81ms
     http_reqs......................: 95434   1532.275945/s
     iteration_duration.............: avg=151.19ms min=6.36ms  med=129.22ms max=815.05ms p(90)=310.91ms p(95)=367.27ms p(99.9)=642.64ms
     iterations.....................: 94434   1516.220074/s
     success_rate...................: 100.00% ✓ 94434       ✗ 0    
     vus............................: 71      min=0         max=495
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 246660      ✗ 0    
     data_received..................: 7.3 GB  117 MB/s
     data_sent......................: 100 MB  1.6 MB/s
     http_req_blocked...............: avg=4.92µs   min=972ns   med=2.27µs   max=6.91ms   p(90)=3.93µs   p(95)=4.88µs   p(99.9)=245.59µs
     http_req_connecting............: avg=2.04µs   min=0s      med=0s       max=6.8ms    p(90)=0s       p(95)=0s       p(99.9)=188.9µs 
     http_req_duration..............: avg=171.39ms min=1.98ms  med=169.63ms max=490.66ms p(90)=325.55ms p(95)=349.25ms p(99.9)=419.52ms
       { expected_response:true }...: avg=171.39ms min=1.98ms  med=169.63ms max=490.66ms p(90)=325.55ms p(95)=349.25ms p(99.9)=419.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 83220
     http_req_receiving.............: avg=77.35µs  min=26.71µs med=60.57µs  max=206.38ms p(90)=98.05µs  p(95)=113.05µs p(99.9)=1.17ms  
     http_req_sending...............: avg=26.95µs  min=5.02µs  med=11.04µs  max=47.96ms  p(90)=17.74µs  p(95)=20.99µs  p(99.9)=3.4ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=171.29ms min=1.92ms  med=169.51ms max=490.57ms p(90)=325.46ms p(95)=349.13ms p(99.9)=419.45ms
     http_reqs......................: 83220   1332.850094/s
     iteration_duration.............: avg=173.71ms min=4.6ms   med=172.39ms max=490.85ms p(90)=326.34ms p(95)=349.89ms p(99.9)=420.01ms
     iterations.....................: 82220   1316.834111/s
     success_rate...................: 100.00% ✓ 82220       ✗ 0    
     vus............................: 78      min=0         max=493
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 101100     ✗ 0    
     data_received..................: 3.0 GB  47 MB/s
     data_sent......................: 42 MB   649 kB/s
     http_req_blocked...............: avg=10.15µs  min=1.17µs  med=3.02µs   max=53.89ms  p(90)=4.69µs   p(95)=5.74µs   p(99.9)=1.32ms
     http_req_connecting............: avg=6.15µs   min=0s      med=0s       max=53.74ms  p(90)=0s       p(95)=0s       p(99.9)=1.3ms 
     http_req_duration..............: avg=413.5ms  min=3.4ms   med=379.32ms max=1.67s    p(90)=819.44ms p(95)=894.74ms p(99.9)=1.37s 
       { expected_response:true }...: avg=413.5ms  min=3.4ms   med=379.32ms max=1.67s    p(90)=819.44ms p(95)=894.74ms p(99.9)=1.37s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 34700
     http_req_receiving.............: avg=217.47µs min=29.48µs med=69.38µs  max=249.62ms p(90)=105.25µs p(95)=119.42µs p(99.9)=31.5ms
     http_req_sending...............: avg=24.46µs  min=5.13µs  med=13.71µs  max=11.63ms  p(90)=20.12µs  p(95)=22.93µs  p(99.9)=2.71ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=413.25ms min=3.32ms  med=379.26ms max=1.67s    p(90)=819.32ms p(95)=894.65ms p(99.9)=1.36s 
     http_reqs......................: 34700   540.434525/s
     iteration_duration.............: avg=426ms    min=6.44ms  med=394.92ms max=1.67s    p(90)=823.5ms  p(95)=897.58ms p(99.9)=1.37s 
     iterations.....................: 33700   524.860043/s
     success_rate...................: 100.00% ✓ 33700      ✗ 0    
     vus............................: 67      min=0        max=496
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 51363      ✗ 0    
     data_received..................: 1.6 GB  24 MB/s
     data_sent......................: 22 MB   325 kB/s
     http_req_blocked...............: avg=13.85µs  min=1.1µs   med=3.24µs   max=16.35ms p(90)=4.91µs   p(95)=6.27µs   p(99.9)=2.04ms
     http_req_connecting............: avg=9.15µs   min=0s      med=0s       max=16.29ms p(90)=0s       p(95)=0s       p(99.9)=2.02ms
     http_req_duration..............: avg=799.97ms min=5.3ms   med=689.66ms max=3.74s   p(90)=1.61s    p(95)=1.85s    p(99.9)=3.18s 
       { expected_response:true }...: avg=799.97ms min=5.3ms   med=689.66ms max=3.74s   p(90)=1.61s    p(95)=1.85s    p(99.9)=3.18s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 18121
     http_req_receiving.............: avg=94.24µs  min=32.62µs med=88.11µs  max=15.55ms p(90)=123.61µs p(95)=139.58µs p(99.9)=1.45ms
     http_req_sending...............: avg=28.82µs  min=5µs     med=16.08µs  max=38.35ms p(90)=21.27µs  p(95)=24.24µs  p(99.9)=2.46ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=799.85ms min=5.19ms  med=689.58ms max=3.74s   p(90)=1.61s    p(95)=1.85s    p(99.9)=3.18s 
     http_reqs......................: 18121   271.017922/s
     iteration_duration.............: avg=846.76ms min=36.03ms med=755.24ms max=3.74s   p(90)=1.62s    p(95)=1.86s    p(99.9)=3.21s 
     iterations.....................: 17121   256.061908/s
     success_rate...................: 100.00% ✓ 17121      ✗ 0    
     vus............................: 5       min=0        max=500
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

     checks.........................: 100.00% ✓ 46407      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   288 kB/s
     http_req_blocked...............: avg=14.2µs   min=1.36µs  med=3.43µs   max=12.16ms  p(90)=5.14µs   p(95)=6.59µs   p(99.9)=2.06ms 
     http_req_connecting............: avg=8.79µs   min=0s      med=0s       max=12.09ms  p(90)=0s       p(95)=0s       p(99.9)=2.04ms 
     http_req_duration..............: avg=881.51ms min=7.64ms  med=815.23ms max=3.03s    p(90)=1.78s    p(95)=1.91s    p(99.9)=2.69s  
       { expected_response:true }...: avg=881.51ms min=7.64ms  med=815.23ms max=3.03s    p(90)=1.78s    p(95)=1.91s    p(99.9)=2.69s  
     http_req_failed................: 0.00%   ✓ 0          ✗ 16469
     http_req_receiving.............: avg=92.14µs  min=34.48µs med=84.85µs  max=6.22ms   p(90)=121.98µs p(95)=137.34µs p(99.9)=913.3µs
     http_req_sending...............: avg=34.53µs  min=5.8µs   med=16.07µs  max=124.98ms p(90)=21.63µs  p(95)=25.13µs  p(99.9)=2.53ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=881.39ms min=7.48ms  med=815.16ms max=3.03s    p(90)=1.78s    p(95)=1.91s    p(99.9)=2.69s  
     http_reqs......................: 16469   240.123319/s
     iteration_duration.............: avg=938.57ms min=40.38ms med=875.39ms max=3.03s    p(90)=1.81s    p(95)=1.92s    p(99.9)=2.72s  
     iterations.....................: 15469   225.542997/s
     success_rate...................: 100.00% ✓ 15469      ✗ 0    
     vus............................: 86      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

